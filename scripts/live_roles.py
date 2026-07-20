#!/usr/bin/env python3
"""
live_roles.py — Pull GENUINELY-LIVE, DATE-STAMPED roles straight from ATS APIs.

Why this exists
---------------
WebSearch returns a stale search *index*: filled roles linger for weeks, so
"liveness by re-search" ships dead links. The ATS JSON APIs (Lever, Greenhouse,
Ashby) return ONLY currently-open postings, each with a real published/updated
timestamp — so we can (a) trust every link is live and (b) actually filter to
"posted today". This only works when the environment's network policy allows
outbound to these hosts; on a locked-down policy every request 403s and the
script tells you so instead of pretending.

Usage
-----
    python scripts/live_roles.py                 # roles posted TODAY (--days 1)
    python scripts/live_roles.py --days 7        # posted within last 7 days
    python scripts/live_roles.py --all-dates     # every open role, no date filter
    python scripts/live_roles.py --out searches/2026-07-20-live.md

Reads scripts/boards.json for the list of ATS boards to query. No third-party
deps — stdlib only.
"""
import argparse
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# --- Fit heuristics (snippet-level; the real Fit Score lives in /tailor-resume) ---
# Title contains any INCLUDE term -> candidate. Order roughly by Josh's strengths.
INCLUDE = [
    "marketing operations", "marketing ops", "marops",
    "hubspot", "gohighlevel", "ghl", "crm",
    "customer success", "client success", "csm",
    "onboarding", "implementation", "customer onboarding",
    "account manager", "account management", "client experience",
    "lifecycle marketing", "marketing automation",
    "growth marketing", "demand generation",
    "revenue operations", "revops", "sales operations",  # kept, but see REVOPS_CAUTION
]
# Hard knockouts from the master profile (geo + language). Title/location match -> screened out.
KNOCKOUT_LOCATION = re.compile(
    r"\b(latam|latin america|india|emea|apac|canada only|uk only|united kingdom|europe only|"
    r"remote - canada|remote canada|philippines|brazil|mexico city|bengaluru|bangalore)\b", re.I)
KNOCKOUT_LANG = re.compile(r"\b(bilingual|spanish|español|português|portuguese|français|german fluency|fluent in)\b", re.I)
# Soft flag: dedicated-RevOps roles often demand 5+ titled RevOps yrs Josh doesn't have.
REVOPS_CAUTION = re.compile(r"\b(revenue operations|revops|sales operations)\b", re.I)

HEADERS = {"User-Agent": "Mozilla/5.0 (jobhunt live_roles.py)"}


def _get(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.loads(r.read().decode("utf-8"))


def _epoch_ms_to_date(ms):
    try:
        return dt.datetime.utcfromtimestamp(int(ms) / 1000).date()
    except Exception:
        return None


def _iso_to_date(s):
    if not s:
        return None
    try:
        return dt.datetime.fromisoformat(s.replace("Z", "+00:00")).date()
    except Exception:
        try:
            return dt.datetime.strptime(s[:10], "%Y-%m-%d").date()
        except Exception:
            return None


def fetch_lever(handle, company):
    data = _get(f"https://api.lever.co/v0/postings/{handle}?mode=json")
    out = []
    for p in data:
        cats = p.get("categories", {}) or {}
        out.append({
            "company": company, "title": p.get("text", ""),
            "location": cats.get("location", ""), "type": cats.get("commitment", ""),
            "url": p.get("hostedUrl", ""),
            "posted": _epoch_ms_to_date(p.get("createdAt")),
        })
    return out


def fetch_greenhouse(handle, company):
    data = _get(f"https://boards-api.greenhouse.io/v1/boards/{handle}/jobs")
    out = []
    for j in data.get("jobs", []):
        out.append({
            "company": company, "title": j.get("title", ""),
            "location": (j.get("location") or {}).get("name", ""), "type": "",
            "url": j.get("absolute_url", ""),
            # Greenhouse list exposes updated_at (proxy for freshness), not created.
            "posted": _iso_to_date(j.get("updated_at")),
            "date_is_updated": True,
        })
    return out


def fetch_ashby(handle, company):
    data = _get(f"https://api.ashbyhq.com/posting-api/job-board/{handle}?includeCompensation=true")
    out = []
    for j in data.get("jobs", []):
        out.append({
            "company": company, "title": j.get("title", ""),
            "location": j.get("location", ""), "type": j.get("employmentType", ""),
            "url": j.get("jobUrl") or j.get("applyUrl", ""),
            "posted": _iso_to_date(j.get("publishedAt")),
        })
    return out


FETCHERS = {"lever": fetch_lever, "greenhouse": fetch_greenhouse, "ashby": fetch_ashby}


def is_fit(title):
    t = title.lower()
    return any(k in t for k in INCLUDE)


def classify(role):
    """Return (verdict, note). verdict in {'shortlist','caution','knockout'}."""
    blob = f"{role['title']} {role['location']}"
    if KNOCKOUT_LOCATION.search(blob):
        return "knockout", "geo excludes US/CO"
    if KNOCKOUT_LANG.search(blob):
        return "knockout", "language requirement (Josh is English-only)"
    if REVOPS_CAUTION.search(role["title"]):
        return "caution", "titled RevOps/SalesOps role — often wants 5+ dedicated RevOps yrs Josh lacks; verify requirements"
    return "shortlist", ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=1,
                    help="Include roles posted within the last N days (default 1 = today).")
    ap.add_argument("--all-dates", action="store_true", help="Ignore date filter; list every open role.")
    ap.add_argument("--boards", default=os.path.join(HERE, "boards.json"))
    ap.add_argument("--out", default=None, help="Write markdown shortlist to this path.")
    args = ap.parse_args()

    cfg = json.load(open(args.boards))
    today = dt.date.today()
    cutoff = today - dt.timedelta(days=args.days - 1)

    roles, errors = [], []
    for b in cfg.get("boards", []):
        fetch = FETCHERS.get(b["platform"])
        if not fetch:
            errors.append(f"{b.get('company')}: unknown platform {b.get('platform')}")
            continue
        try:
            roles.extend(fetch(b["handle"], b.get("company", b["handle"])))
        except urllib.error.HTTPError as e:
            errors.append(f"{b['company']} ({b['platform']}): HTTP {e.code}")
        except urllib.error.URLError as e:
            errors.append(f"{b['company']} ({b['platform']}): {e.reason} "
                          f"(network policy likely blocks this host)")
        except Exception as e:  # noqa
            errors.append(f"{b['company']} ({b['platform']}): {e}")

    # De-dupe by url
    seen, deduped = set(), []
    for r in roles:
        if r["url"] and r["url"] not in seen:
            seen.add(r["url"])
            deduped.append(r)

    fit = [r for r in deduped if is_fit(r["title"])]
    if not args.all_dates:
        fit = [r for r in fit if r["posted"] and r["posted"] >= cutoff]

    shortlist, caution, knockout = [], [], []
    for r in fit:
        v, note = classify(r)
        r["note"] = note
        (shortlist if v == "shortlist" else caution if v == "caution" else knockout).append(r)

    shortlist.sort(key=lambda r: r["posted"] or today, reverse=True)

    lines = []
    scope = "all open" if args.all_dates else (
        "posted today" if args.days == 1 else f"posted within {args.days} days")
    lines.append(f"# Live roles — {today} ({scope})\n")
    lines.append(f"_Source: ATS APIs (Lever/Greenhouse/Ashby). Every link below is a currently-open "
                 f"posting; dates are real publish/update timestamps from the ATS._\n")
    if not shortlist and not caution:
        lines.append("**No matching live roles in this window.** Widen with `--days 7` or `--all-dates`, "
                     "or add more boards to `scripts/boards.json`.\n")
    if shortlist:
        lines.append("## Shortlist (fit)\n")
        for r in shortlist:
            d = r["posted"].isoformat() if r["posted"] else "date n/a"
            tag = " _(updated, not created)_" if r.get("date_is_updated") else ""
            lines.append(f"- **{r['company']} — {r['title']}** · {r['location'] or 'loc n/a'}"
                         f" · {r['type'] or 'type n/a'} · posted {d}{tag}\n  {r['url']}")
    if caution:
        lines.append("\n## Verify fit before applying\n")
        for r in caution:
            d = r["posted"].isoformat() if r["posted"] else "date n/a"
            lines.append(f"- **{r['company']} — {r['title']}** · {r['location'] or 'loc n/a'} · posted {d}"
                         f" — ⚠ {r['note']}\n  {r['url']}")
    if knockout:
        lines.append("\n## Screened out (knockouts)\n")
        for r in knockout:
            lines.append(f"- {r['company']} — {r['title']} — ⛔ {r['note']}")
    if errors:
        lines.append("\n## Boards that could not be reached\n")
        for e in errors:
            lines.append(f"- {e}")
        lines.append("\n> If these are all 403/blocked, the environment's network policy is denying "
                     "outbound to job boards. Run in an environment whose policy allows these hosts.")

    out_text = "\n".join(lines) + "\n"
    print(out_text)
    if args.out:
        os.makedirs(os.path.dirname(os.path.join(ROOT, args.out)) or ".", exist_ok=True)
        with open(os.path.join(ROOT, args.out), "w") as f:
            f.write(out_text)
        print(f"[written] {args.out}")

    # Exit non-zero if every board failed (so failures are noticeable in automation).
    if errors and not deduped:
        sys.exit(2)


if __name__ == "__main__":
    main()
