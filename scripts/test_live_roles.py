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

FIXTURES_BY_URL_TOKEN = [
    ("api.lever.co", LEVER_FIXTURE),
    ("boards-api.greenhouse.io", GREENHOUSE_FIXTURE),
    ("api.ashbyhq.com", ASHBY_FIXTURE),
]


def fake_get_ok(url):
    for token, payload in FIXTURES_BY_URL_TOKEN:
        if token in url:
            return json.loads(json.dumps(payload))  # deep copy
    raise AssertionError(f"unexpected URL {url}")


def fake_get_blocked(url):
    raise urllib.error.URLError("Tunnel connection failed: 403 Forbidden")


def make_boards_json(tmpdir):
    cfg = {"boards": [
        {"platform": "lever", "handle": "acme", "company": "Acme"},
        {"platform": "greenhouse", "handle": "globex", "company": "Globex"},
        {"platform": "ashby", "handle": "initech", "company": "Initech"},
    ]}
    path = os.path.join(tmpdir, "boards.json")
    with open(path, "w") as f:
        json.dump(cfg, f)
    return path


def run_main(argv, get_impl):
    """Run live_roles.main() with stubbed HTTP; return (stdout, exit_code)."""
    out = io.StringIO()
    code = 0
    with mock.patch.object(live_roles, "_get", side_effect=get_impl), \
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
