#!/usr/bin/env python3
"""
live_roles.py — pull CURRENTLY-OPEN roles with REAL publish timestamps straight
from the Greenhouse / Lever / Ashby JSON APIs, so "posted in the last N days" is
actually enforceable (unlike a lagging web-search index).

Why this exists: WebSearch hits a search index, so filled roles linger for weeks
and post-dates can't be trusted. These ATS JSON endpoints return the live board
with per-role timestamps — the only reliable "posted today" source.

Usage:
  python scripts/live_roles.py --days 1            # roles published in last 1 day
  python scripts/live_roles.py --days 3 --json     # machine-readable output
  python scripts/live_roles.py --days 7 --all      # skip the title-band filter

Reads company handles from scripts/boards.json:
  {"greenhouse": ["token", ...], "lever": ["slug", ...], "ashby": ["org", ...]}

Network note: in a locked-down session the egress proxy may 403 these hosts
(boards-api.greenhouse.io, api.lever.co, api.ashbyhq.com). The script reports
each blocked board plainly rather than pretending — if every board is blocked,
that's an environment network-policy limit, not a bug here. Allowlist those three
hosts (or run the session under a policy that permits them) and it works.
"""
import argparse, json, os, sys, time, urllib.request, urllib.error
from datetime import datetime, timezone

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
HERE = os.path.dirname(os.path.abspath(__file__))

# Josh's seniority + role band. Keep = title matches an INCLUDE term and no EXCLUDE term.
INCLUDE = [
    "marketing operation", "revenue operation", "revops", "marketing ops",
    "digital marketing", "growth marketing", "demand generation", "lifecycle",
    "marketing automation", "marketing manager", "crm", "hubspot",
    "customer success", "onboarding", "implementation", "account manager",
    "client partnership", "client success", "ai ", "agentic", "automation",
    "productivity", "solutions", "customer marketing",
]
EXCLUDE = [
    "engineer", "developer", "software", "swe", "programmer", "data scientist",
    "designer", "intern", "internship", "vp ", "vice president", "chief",
    "head of", "president", "counsel", "recruiter", "sdr", "bdr", "sales development",
    "account executive", "nurse", "clinical", "therapist", "founding",
]
# US-friendly location gate (best-effort; ATS location strings vary a lot).
US_OK = ["united states", "us", "u.s", "remote", "anywhere", "colorado", "denver",
         "new york", "san francisco", "los angeles", "chicago", "phoenix", "austin",
         "boston", "seattle", "atlanta", "nationwide"]
NON_US = ["canada", "brazil", "united kingdom", "uk only", "europe", "emea", "india",
          "germany", "spain", "france", "australia", "singapore", "philippines",
          "latam", "apac", "ireland", "netherlands", "poland", "mexico"]


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def title_ok(title, keep_all):
    t = (title or "").lower()
    if keep_all:
        return True
    if any(x in t for x in EXCLUDE):
        return False
    return any(x in t for x in INCLUDE)


def loc_ok(loc):
    l = (loc or "").lower()
    if any(x in l for x in NON_US):
        return False
    if not l:
        return True  # unknown — keep, flag downstream
    return any(x in l for x in US_OK)


def within(ts_epoch, days):
    if ts_epoch is None:
        return False
    age = time.time() - ts_epoch
    return 0 <= age <= days * 86400 + 3600  # small grace


def iso(ts_epoch):
    return datetime.fromtimestamp(ts_epoch, timezone.utc).strftime("%Y-%m-%d") if ts_epoch else "?"


def greenhouse(token, days, keep_all):
    url = f"https://boards-api.greenhouse.io/v1/boards/{token}/jobs?content=false"
    out = []
    for j in fetch(url).get("jobs", []):
        upd = j.get("updated_at")
        ts = None
        if upd:
            try:
                ts = datetime.fromisoformat(upd.replace("Z", "+00:00")).timestamp()
            except ValueError:
                ts = None
        loc = (j.get("location") or {}).get("name", "")
        if within(ts, days) and title_ok(j.get("title"), keep_all) and loc_ok(loc):
            out.append({"source": "greenhouse", "company": token, "title": j.get("title"),
                        "location": loc, "date": iso(ts), "url": j.get("absolute_url")})
    return out


def lever(slug, days, keep_all):
    url = f"https://api.lever.co/v0/postings/{slug}?mode=json"
    out = []
    for j in fetch(url):
        ts = j.get("createdAt")
        ts = ts / 1000.0 if isinstance(ts, (int, float)) else None
        cat = j.get("categories") or {}
        loc = cat.get("location", "")
        if within(ts, days) and title_ok(j.get("text"), keep_all) and loc_ok(loc):
            out.append({"source": "lever", "company": slug, "title": j.get("text"),
                        "location": loc, "date": iso(ts),
                        "url": j.get("hostedUrl") or j.get("applyUrl")})
    return out


def ashby(org, days, keep_all):
    url = f"https://api.ashbyhq.com/posting-api/job-board/{org}"
    out = []
    for j in fetch(url).get("jobs", []):
        pub = j.get("publishedDate") or j.get("publishedAt")
        ts = None
        if pub:
            try:
                ts = datetime.fromisoformat(str(pub).replace("Z", "+00:00")).timestamp()
            except ValueError:
                ts = None
        loc = j.get("locationName") or j.get("location") or ""
        if within(ts, days) and title_ok(j.get("title"), keep_all) and loc_ok(loc):
            out.append({"source": "ashby", "company": org, "title": j.get("title"),
                        "location": loc, "date": iso(ts),
                        "url": j.get("jobUrl") or j.get("applyUrl")})
    return out


FETCHERS = {"greenhouse": greenhouse, "lever": lever, "ashby": ashby}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=1)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--all", action="store_true", help="skip the title-band filter")
    ap.add_argument("--boards", default=os.path.join(HERE, "boards.json"))
    args = ap.parse_args()

    cfg = json.load(open(args.boards))
    roles, blocked, empty = [], [], 0
    for source, handles in cfg.items():
        if source.startswith("_") or source not in FETCHERS:
            continue
        for h in handles:
            try:
                got = FETCHERS[source](h, args.days, args.all)
                roles += got
                if not got:
                    empty += 1
            except urllib.error.HTTPError as e:
                blocked.append(f"{source}:{h} (HTTP {e.code})")
            except Exception as e:
                blocked.append(f"{source}:{h} ({type(e).__name__})")

    roles.sort(key=lambda r: r["date"], reverse=True)

    if args.json:
        print(json.dumps({"days": args.days, "roles": roles, "blocked": blocked}, indent=2))
        return

    print(f"\n=== Live roles published in the last {args.days} day(s) ===")
    if roles:
        for r in roles:
            print(f"[{r['date']}] {r['title']}  @ {r['company']} ({r['source']})")
            print(f"          {r['location'] or 'location n/a'}  ->  {r['url']}")
    else:
        print("(none matched)")

    if blocked:
        n = len(blocked)
        total = sum(len(v) for k, v in cfg.items() if k in FETCHERS)
        print(f"\n⚠ {n}/{total} board(s) unreachable (likely egress policy / anti-bot):")
        for b in blocked[:12]:
            print(f"    - {b}")
        if n == total:
            print("  → EVERY board blocked: this environment's network policy denies the ATS")
            print("    API hosts. Allowlist boards-api.greenhouse.io, api.lever.co,")
            print("    api.ashbyhq.com (or run under a policy that permits them). Not a bug here.")
    print()


if __name__ == "__main__":
    main()
