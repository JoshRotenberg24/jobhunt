#!/usr/bin/env python3
"""
Fixture-based tests for live_roles.py — runs fully offline.

The environment blocks outbound to job boards, so these tests stub the HTTP
layer (live_roles._get) with payloads shaped exactly like the real Lever /
Greenhouse / Ashby API responses, then assert on:
  - date parsing per platform (epoch-ms, ISO, updated_at fallback)
  - the --days / --all-dates windowing
  - knockout classification (geo, language) and RevOps caution
  - fit filtering (title include-list)
  - URL de-dupe
  - error handling: blocked boards reported, exit code 2 when ALL fail
Run:  python3 scripts/test_live_roles.py
"""
import contextlib
import datetime as dt
import email.utils
import io
import json
import os
import sys
import tempfile
import unittest
import unittest.mock as mock
import urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import live_roles  # noqa: E402

TODAY = dt.date.today()


def epoch_ms(d):
    """UTC midnight of date d as epoch milliseconds (Lever createdAt format)."""
    return int(dt.datetime(d.year, d.month, d.day, 12, 0).replace(
        tzinfo=dt.timezone.utc).timestamp() * 1000)


def iso(d):
    return f"{d.isoformat()}T09:30:00Z"


# ---------------------------------------------------------------- fixtures
LEVER_FIXTURE = [
    {   # fit + posted today -> shortlist
        "text": "Customer Success Manager",
        "categories": {"location": "Remote (US)", "commitment": "Full-time"},
        "hostedUrl": "https://jobs.lever.co/acme/aaa-111",
        "createdAt": epoch_ms(TODAY),
    },
    {   # fit but 30 days old -> excluded at --days 1, included at --all-dates
        "text": "Onboarding Manager",
        "categories": {"location": "Remote", "commitment": "Full-time"},
        "hostedUrl": "https://jobs.lever.co/acme/bbb-222",
        "createdAt": epoch_ms(TODAY - dt.timedelta(days=30)),
    },
    {   # geo knockout (LATAM), posted today
        "text": "Enterprise Customer Success Manager (Remote LATAM)",
        "categories": {"location": "Remote - LATAM", "commitment": "Full-time"},
        "hostedUrl": "https://jobs.lever.co/acme/ccc-333",
        "createdAt": epoch_ms(TODAY),
    },
    {   # non-fit title -> filtered out entirely
        "text": "Staff Backend Engineer",
        "categories": {"location": "Remote (US)", "commitment": "Full-time"},
        "hostedUrl": "https://jobs.lever.co/acme/ddd-444",
        "createdAt": epoch_ms(TODAY),
    },
    {   # language knockout, posted today
        "text": "Bilingual Customer Success Manager (Spanish)",
        "categories": {"location": "Remote (US)", "commitment": "Full-time"},
        "hostedUrl": "https://jobs.lever.co/acme/eee-555",
        "createdAt": epoch_ms(TODAY),
    },
]

GREENHOUSE_FIXTURE = {
    "jobs": [
        {   # fit, updated today (greenhouse exposes updated_at) -> shortlist w/ tag
            "title": "Marketing Operations Manager",
            "location": {"name": "Remote - US"},
            "absolute_url": "https://boards.greenhouse.io/globex/jobs/123",
            "updated_at": iso(TODAY),
        },
        {   # duplicate URL of the same job (simulates repost/second board entry)
            "title": "Marketing Operations Manager",
            "location": {"name": "Remote - US"},
            "absolute_url": "https://boards.greenhouse.io/globex/jobs/123",
            "updated_at": iso(TODAY),
        },
    ]
}

ASHBY_FIXTURE = {
    "jobs": [
        {   # RevOps caution bucket, published today
            "title": "Revenue Operations Manager",
            "location": "Remote (US)",
            "employmentType": "FullTime",
            "jobUrl": "https://jobs.ashbyhq.com/initech/rev-1",
            "publishedAt": iso(TODAY),
        },
        {   # fit, published 3 days ago -> in --days 7, out of --days 1
            "title": "HubSpot Administrator",
            "location": "Remote (US)",
            "employmentType": "Contract",
            "jobUrl": "https://jobs.ashbyhq.com/initech/hub-1",
            "publishedAt": iso(TODAY - dt.timedelta(days=3)),
        },
    ]
}

REMOTIVE_FIXTURE = {
    "jobs": [
        {   # fit + US-friendly geo + posted today -> shortlist
            "title": "Marketing Automation Specialist",
            "company_name": "Orbit Labs",
            "candidate_required_location": "USA Only",
            "job_type": "full_time",
            "url": "https://remotive.com/remote-jobs/marketing/orbit-1",
            "publication_date": f"{TODAY.isoformat()}T08:33:22",
        },
        {   # fit but geo-gated out (Europe only) -> knockout
            "title": "Customer Success Manager",
            "company_name": "EuroSoft",
            "candidate_required_location": "Europe",
            "job_type": "full_time",
            "url": "https://remotive.com/remote-jobs/csm/eurosoft-1",
            "publication_date": f"{TODAY.isoformat()}T08:33:22",
        },
        {   # excluded title band (VP) despite include-term match -> filtered out
            "title": "VP of Marketing Operations",
            "company_name": "BigCo",
            "candidate_required_location": "USA Only",
            "job_type": "full_time",
            "url": "https://remotive.com/remote-jobs/vp/bigco-1",
            "publication_date": f"{TODAY.isoformat()}T08:33:22",
        },
    ]
}

JOBICY_FIXTURE = {
    "jobs": [
        {   # fit, bare "Remote" geo passes the gate, posted today
            "jobTitle": "HubSpot CRM Manager",
            "companyName": "Nimbus",
            "jobGeo": "Remote",
            "jobType": ["full-time"],
            "url": "https://jobicy.com/jobs/nimbus-hubspot-crm",
            "pubDate": f"{TODAY.isoformat()} 10:00:00",
        },
    ]
}

REMOTEOK_FIXTURE = [
    {"legal": "API terms of service notice — not a job"},
    {   # fit, worldwide, posted today
        "position": "Lifecycle Marketing Manager",
        "company": "Skyline",
        "location": "Worldwide",
        "url": "https://remoteok.com/remote-jobs/skyline-lifecycle-1",
        "date": f"{TODAY.isoformat()}T08:00:00+00:00",
    },
]

HIMALAYAS_FIXTURE = {
    "jobs": [
        {   # fit, US restriction, epoch-seconds pubDate today
            "title": "Implementation Manager",
            "companyName": "Meadow",
            "locationRestrictions": ["United States"],
            "applicationLink": "https://himalayas.app/companies/meadow/jobs/onboarding-1",
            "pubDate": int(dt.datetime(TODAY.year, TODAY.month, TODAY.day, 12,
                                       tzinfo=dt.timezone.utc).timestamp()),
        },
    ]
}

WWR_RSS_FIXTURE = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel>
  <title>We Work Remotely: jobs</title>
  <item>
    <title>Acme Agency: Marketing Operations Lead</title>
    <region>Anywhere in the World</region>
    <type>Full-Time</type>
    <link>https://weworkremotely.com/remote-jobs/acme-agency-marketing-operations-lead</link>
    <pubDate>{email.utils.format_datetime(dt.datetime(TODAY.year, TODAY.month, TODAY.day, 9, tzinfo=dt.timezone.utc))}</pubDate>
  </item>
</channel></rss>"""

FIXTURES_BY_URL_TOKEN = [
    ("api.lever.co", LEVER_FIXTURE),
    ("boards-api.greenhouse.io", GREENHOUSE_FIXTURE),
    ("api.ashbyhq.com", ASHBY_FIXTURE),
    ("remotive.com", REMOTIVE_FIXTURE),
    ("jobicy.com", JOBICY_FIXTURE),
    ("remoteok.com", REMOTEOK_FIXTURE),
    ("himalayas.app", HIMALAYAS_FIXTURE),
]


def fake_get_ok(url):
    for token, payload in FIXTURES_BY_URL_TOKEN:
        if token in url:
            return json.loads(json.dumps(payload))  # deep copy
    raise AssertionError(f"unexpected URL {url}")


def fake_get_raw_ok(url):
    """Raw-text stub — only the WeWorkRemotely RSS fetcher uses _get_raw directly."""
    if "weworkremotely.com" in url:
        return WWR_RSS_FIXTURE
    raise AssertionError(f"unexpected raw URL {url}")


def fake_get_blocked(url):
    raise urllib.error.URLError("Tunnel connection failed: 403 Forbidden")


def make_boards_json(tmpdir):
    cfg = {
        "boards": [
            {"platform": "lever", "handle": "acme", "company": "Acme"},
            {"platform": "greenhouse", "handle": "globex", "company": "Globex"},
            {"platform": "ashby", "handle": "initech", "company": "Initech"},
        ],
        "remote_boards": [
            {"platform": "remotive"}, {"platform": "jobicy"},
            {"platform": "remoteok"}, {"platform": "himalayas"},
            {"platform": "weworkremotely"},
        ],
    }
    path = os.path.join(tmpdir, "boards.json")
    with open(path, "w") as f:
        json.dump(cfg, f)
    return path


def run_main(argv, get_impl, get_raw_impl=None):
    """Run live_roles.main() with stubbed HTTP; return (stdout, exit_code)."""
    if get_raw_impl is None:
        get_raw_impl = fake_get_raw_ok if get_impl is fake_get_ok else get_impl
    out = io.StringIO()
    code = 0
    with mock.patch.object(live_roles, "_get", side_effect=get_impl), \
         mock.patch.object(live_roles, "_get_raw", side_effect=get_raw_impl), \
         mock.patch.object(sys, "argv", ["live_roles.py"] + argv), \
         contextlib.redirect_stdout(out):
        try:
            live_roles.main()
        except SystemExit as e:
            code = e.code or 0
    return out.getvalue(), code


class TestParsers(unittest.TestCase):
    def test_lever_dates_and_fields(self):
        with mock.patch.object(live_roles, "_get", side_effect=fake_get_ok):
            roles = live_roles.fetch_lever("acme", "Acme")
        self.assertEqual(len(roles), 5)
        csm = next(r for r in roles if r["title"] == "Customer Success Manager")
        self.assertEqual(csm["posted"], TODAY)
        self.assertEqual(csm["location"], "Remote (US)")
        self.assertEqual(csm["type"], "Full-time")
        self.assertTrue(csm["url"].startswith("https://jobs.lever.co/"))

    def test_greenhouse_marks_updated_dates(self):
        with mock.patch.object(live_roles, "_get", side_effect=fake_get_ok):
            roles = live_roles.fetch_greenhouse("globex", "Globex")
        self.assertTrue(all(r.get("date_is_updated") for r in roles))
        self.assertEqual(roles[0]["posted"], TODAY)
        self.assertEqual(roles[0]["location"], "Remote - US")

    def test_ashby_iso_dates(self):
        with mock.patch.object(live_roles, "_get", side_effect=fake_get_ok):
            roles = live_roles.fetch_ashby("initech", "Initech")
        hub = next(r for r in roles if "HubSpot" in r["title"])
        self.assertEqual(hub["posted"], TODAY - dt.timedelta(days=3))
        self.assertEqual(hub["type"], "Contract")


class TestAggregators(unittest.TestCase):
    def test_remotive_parse(self):
        with mock.patch.object(live_roles, "_get", side_effect=fake_get_ok):
            roles = live_roles.fetch_remotive({})
        self.assertEqual(len(roles), 3)
        orbit = next(r for r in roles if r["company"] == "Orbit Labs")
        self.assertEqual(orbit["posted"], TODAY)
        self.assertEqual(orbit["type"], "full-time")
        self.assertTrue(orbit["geo_gated"])
        self.assertEqual(orbit["via"], "Remotive")

    def test_remoteok_skips_legal_notice(self):
        with mock.patch.object(live_roles, "_get", side_effect=fake_get_ok):
            roles = live_roles.fetch_remoteok({})
        self.assertEqual(len(roles), 1)
        self.assertEqual(roles[0]["title"], "Lifecycle Marketing Manager")
        self.assertEqual(roles[0]["posted"], TODAY)

    def test_himalayas_epoch_seconds_and_locations(self):
        with mock.patch.object(live_roles, "_get", side_effect=fake_get_ok):
            roles = live_roles.fetch_himalayas({})
        self.assertEqual(roles[0]["posted"], TODAY)
        self.assertEqual(roles[0]["location"], "United States")

    def test_wwr_rss_company_title_split_and_date(self):
        with mock.patch.object(live_roles, "_get_raw", return_value=WWR_RSS_FIXTURE):
            roles = live_roles.fetch_weworkremotely({})
        # one item repeated across the 3 default category feeds
        self.assertEqual(len(roles), 3)
        r = roles[0]
        self.assertEqual(r["company"], "Acme Agency")
        self.assertEqual(r["title"], "Marketing Operations Lead")
        self.assertEqual(r["location"], "Anywhere in the World")
        self.assertEqual(r["posted"], TODAY)

    def test_geo_gate_blocks_non_us(self):
        v, note = live_roles.classify(
            {"title": "Customer Success Manager", "location": "Europe", "geo_gated": True})
        self.assertEqual(v, "knockout")
        self.assertIn("geo excludes US", note)

    def test_geo_gate_allows_bare_remote_and_us(self):
        for loc in ("Remote", "", "USA Only", "Worldwide", "Anywhere in the World"):
            v, _ = live_roles.classify(
                {"title": "Customer Success Manager", "location": loc, "geo_gated": True})
            self.assertEqual(v, "shortlist", f"location {loc!r} should pass")

    def test_ats_roles_not_geo_gated(self):
        # Company-ATS roles keep the old behavior: unusual location strings pass.
        v, _ = live_roles.classify(
            {"title": "Customer Success Manager", "location": "Denver, CO"})
        self.assertEqual(v, "shortlist")

    def test_exclude_title_band(self):
        self.assertFalse(live_roles.is_fit("VP of Marketing Operations"))
        self.assertFalse(live_roles.is_fit("CRM Developer"))
        self.assertFalse(live_roles.is_fit("Junior Marketing Operations Associate"))
        self.assertTrue(live_roles.is_fit("Marketing Operations Manager"))
        self.assertTrue(live_roles.is_fit("Director of Marketing Operations"))


class TestClassify(unittest.TestCase):
    def _c(self, title, location=""):
        return live_roles.classify({"title": title, "location": location})

    def test_geo_knockout(self):
        v, note = self._c("Customer Success Manager", "Remote - LATAM")
        self.assertEqual(v, "knockout")
        self.assertIn("geo", note)

    def test_language_knockout(self):
        v, _ = self._c("Bilingual Customer Success Manager (Spanish)")
        self.assertEqual(v, "knockout")

    def test_revops_caution(self):
        v, note = self._c("Revenue Operations Manager", "Remote (US)")
        self.assertEqual(v, "caution")
        self.assertIn("RevOps", note)

    def test_plain_fit(self):
        v, _ = self._c("Marketing Operations Manager", "Remote - US")
        self.assertEqual(v, "shortlist")


class TestEndToEnd(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.boards = make_boards_json(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_posted_today_window(self):
        out, code = run_main(["--days", "1", "--boards", self.boards], fake_get_ok)
        self.assertEqual(code, 0)
        # in-window fits
        self.assertIn("Customer Success Manager", out)
        self.assertIn("Marketing Operations Manager", out)
        # greenhouse date honesty tag
        self.assertIn("(updated, not created)", out)
        # out-of-window (30d, 3d) excluded from shortlist
        self.assertNotIn("Onboarding Manager", out)
        self.assertNotIn("HubSpot Administrator", out)
        # knockouts listed in screened-out, not shortlist
        self.assertIn("Screened out", out)
        self.assertIn("LATAM", out)
        self.assertIn("Bilingual", out)
        # caution bucket
        self.assertIn("Verify fit before applying", out)
        self.assertIn("Revenue Operations Manager", out)
        # non-fit engineering role never appears
        self.assertNotIn("Backend Engineer", out)
        # remote-board roles flow through with source attribution
        self.assertIn("Orbit Labs", out)
        self.assertIn("via Remotive", out)
        self.assertIn("via RemoteOK", out)
        self.assertIn("via Jobicy", out)
        self.assertIn("via Himalayas", out)
        self.assertIn("via WeWorkRemotely", out)
        # geo gate: Europe-only aggregator role screened out, not shortlisted
        self.assertIn("EuroSoft", out)
        self.assertIn("geo excludes US (Europe)", out)
        # title exclusion band: VP role never appears
        self.assertNotIn("VP of Marketing Operations", out)

    def test_seven_day_window_includes_3day_old(self):
        out, _ = run_main(["--days", "7", "--boards", self.boards], fake_get_ok)
        self.assertIn("HubSpot Administrator", out)
        self.assertNotIn("Onboarding Manager", out)  # 30d still out

    def test_all_dates_includes_everything_fit(self):
        out, _ = run_main(["--all-dates", "--boards", self.boards], fake_get_ok)
        self.assertIn("Onboarding Manager", out)
        self.assertIn("HubSpot Administrator", out)

    def test_dedupe_by_url(self):
        out, _ = run_main(["--days", "1", "--boards", self.boards], fake_get_ok)
        self.assertEqual(out.count("boards.greenhouse.io/globex/jobs/123"), 1)

    def test_all_boards_blocked_exits_2_and_reports(self):
        out, code = run_main(["--days", "1", "--boards", self.boards], fake_get_blocked)
        self.assertEqual(code, 2)
        self.assertIn("could not be reached", out)
        self.assertIn("network policy", out)
        # must not fabricate roles
        self.assertNotIn("## Shortlist (fit)", out)

    def test_partial_failure_still_returns_other_boards(self):
        def flaky(url):
            if "lever" in url:
                raise urllib.error.URLError("403")
            return fake_get_ok(url)
        out, code = run_main(["--days", "1", "--boards", self.boards], flaky)
        self.assertEqual(code, 0)  # partial data -> not a total failure
        self.assertIn("Marketing Operations Manager", out)   # greenhouse ok
        self.assertIn("Acme (lever)", out)                   # failure reported

    def test_out_writes_file(self):
        rel = os.path.join("searches", "_test_live.md")
        out, _ = run_main(["--days", "1", "--boards", self.boards, "--out", rel],
                          fake_get_ok)
        dest = os.path.join(live_roles.ROOT, rel)
        try:
            self.assertTrue(os.path.exists(dest))
            with open(dest) as f:
                self.assertIn("Live roles", f.read())
        finally:
            if os.path.exists(dest):
                os.remove(dest)


if __name__ == "__main__":
    unittest.main(verbosity=2)
