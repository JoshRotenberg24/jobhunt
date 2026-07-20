---
name: find-roles
description: >
  Search for live, currently-open job roles that fit Joshua Rotenberg, using web
  search. Use whenever asked to find, search, source, or discover roles/jobs/openings
  to apply to — as opposed to tailoring a resume for one specific posting you already
  have. Covers full-time roles AND part-time / contract / fractional / freelance work.
  Reads the master profile to know his target role types, seniority, and location,
  accepts optional filters (titles, remote/location, comp, company stage, employment type),
  runs a quick Fit read + knockout scan on each hit, and saves a ranked shortlist to searches/<date>.md.
  Hands the strongest matches off to /tailor-resume. Never invents postings — every role
  on the shortlist must trace to a real search result with a link.
argument-hint: <optional filters — e.g. "remote HubSpot ops", "part-time contract", "fractional RevOps", "Denver CS lead">
---

# Find Roles

Source **live, currently-open roles** that genuinely fit **Joshua Rotenberg**, rank them
by a fast Fit read, and produce a shortlist he can act on. This is the *front* of the
funnel; `/tailor-resume` is the back. Guiding principle: **truthful sourcing** — every
role listed must come from a real search result with a working link. Never fabricate a
posting, company, or link, and never guess a salary the listing doesn't state.

## Files this skill depends on (read every run)
- `profile/master-profile.md` — target role types, seniority, location, and the content
  used for the quick Fit read. The ONLY source of true candidate facts.
- `.claude/skills/tailor-resume/SKILL.md` — the Fit Score rubric (Step 4) and the
  knockout rule, reused here in lightweight form.

---

## Step 1 — Build the search profile
Read `profile/master-profile.md` and derive the search targets **before** searching:
- **Role types** — from the Summary Variants table (Marketing Ops / CRM, Customer
  Success / Onboarding, Strategic Account / Client Success, Growth Marketing, AI /
  Agentic Ops, Content, Marketing Generalist / Head of Marketing, Analytics /
  Consulting, Client Experience / AM). Turn each into 2–4 concrete title strings
  (e.g. "Marketing Operations Manager", "HubSpot Administrator", "RevOps Manager").
- **Seniority** — manager / lead / senior IC range implied by 15+ yrs; avoid entry-level
  and avoid VP/C-suite unless the user asks.
- **Location & mode** — his base is **Arvada, Colorado**. Default to **remote (US)** plus
  **Denver / Colorado metro**; widen only if the user says so.
- **Employment type** — search **both full-time roles AND part-time / contract /
  fractional / freelance** work by default. Part-time and contract fit him well (he runs
  Solenzo LLC and already works as a **fractional** success/implementation manager), and
  fractional/contract engagements can run alongside it. Note the type on every result so
  the shortlist separates a W-2 full-time role from a contract or fractional gig.

Then apply the user's **filters** from the argument (titles, location/remote, comp floor,
company stage/industry, must-have tool like HubSpot, and **employment type** — e.g.
"part-time", "contract", "fractional", "freelance", or "full-time only"). User filters
override the defaults: if the user asks only for contract/part-time work, drop full-time
from the plan (and vice-versa). If the argument is empty, use the full default profile
above (both employment types).

State the resolved search plan to the user in 1–2 lines before searching (which titles,
where, remote vs onsite, and which employment types), so they can redirect early.

## Step 0 — Try the ATS APIs FIRST (the only reliable "posted today" source)
Before searching, run `python scripts/live_roles.py --days <N>` (N=1 for "today").
It queries the Lever/Greenhouse/Ashby JSON APIs listed in `scripts/boards.json` and
returns **only currently-open roles with real publish timestamps** — so links can't be
dead and "posted today" is actually enforceable. Add relevant company handles to
`scripts/boards.json` as you discover them.

- **If the script returns roles:** those are your verified, dated shortlist core. Trust
  them over any search snippet. Still run Step 2 search to widen coverage beyond the
  boards in the config.
- **If the script reports every board 403/blocked:** the environment's network policy
  denies outbound to job boards. Say so plainly, and warn the user that WebSearch-only
  results (Step 2) **cannot be liveness-verified or date-confirmed from inside the
  session** — the "posted today" guarantee is impossible here without opening network
  access. Do NOT present snippet results as confirmed-live; see the liveness rules below.

## Step 2 — Search the web for openings (leads only, when the API path is blocked/partial)
Use **WebSearch** as the primary tool. **Critical:** WebSearch hits a search *index*, not
the live board — filled roles linger in the index for days/weeks, so **a role appearing in
search is NOT evidence it is still open.** WebFetch to the actual posting almost always
**403s** in this environment (job boards + their ATS APIs alike), so you usually cannot
independently confirm a snippet role is live. Therefore treat every WebSearch hit as an
**unverified lead the user must confirm by clicking**, and mark all page-level detail
(comp, posted/close dates, requirements) as **unverified**. Never state a snippet role as
confirmed-live or "posted today." Run several targeted queries, not one broad one — vary
title × location × source. Good patterns:
- `"<title>" remote jobs 2026` and `"<title>" jobs Denver Colorado`
- `"<title>" <industry> hiring` (e.g. SaaS, MarTech, B2B)
- Board-scoped: append `site:boards.greenhouse.io`, `site:jobs.lever.co`,
  `site:jobs.ashbyhq.com`, `site:linkedin.com/jobs`, or `site:builtin.com` to catch
  ATS-hosted posts.
- **Part-time / contract / fractional** (run these unless the user asked full-time only):
  `"<title>" part-time remote`, `"<title>" contract remote`, `fractional <role> hiring`
  (e.g. `fractional RevOps`, `fractional marketing ops`), `"<title>" freelance`. Also
  scope contract/fractional-heavy sources: `site:contra.com`, `site:upwork.com`,
  `site:continuum.club`, `site:gofractional.com`, `site:linkedin.com/jobs` with a
  `part-time OR contract` qualifier.
- If the user named a tool/stack (HubSpot, Salesforce), include it as an exact phrase.

Balance the queries across employment types in the plan — don't let one type crowd out
the other unless the user narrowed it.

Aim to gather **10–20 candidate postings** across role types before ranking. For each,
capture what the result gives you: company, title, location/mode, link, and any stated
comp or must-haves. Prefer results that look **current** (2026 / "posted recently"); note
when a date isn't verifiable rather than assuming freshness.

> Many boards (Greenhouse/Lever/Workday/LinkedIn) block automated fetching, so a snippet
> link is a **lead, not a confirmed-live role** — it must be labeled unverified unless it
> came from `scripts/live_roles.py`. Deep parsing happens later in `/tailor-resume`, which
> will ask for a paste if the fetch walls off.
> **Because those same boards block fetching, the `/tailor-resume <url>` handoff will
> usually need the JD pasted in** — so tell the user to have the JD text handy, and
> prefer linking the most authoritative source (company ATS) over an aggregator repost.

### Link quality & liveness — DO NOT SKIP (this is where stale/dead links come from)
The #1 failure of this skill is shipping links that 404 or point at the wrong thing.
Every one of these is mandatory:

1. **One link per role, and it must be the *specific posting* for THAT exact company +
   title.** Never reuse another role's URL, never approximate or hand-build a URL, and
   never point at a **generic landing/search page** (e.g. `jobs.lever.co/<company>` with
   no req id, `builtin.com/jobs/...search...`, `revopscareers.com`, a board's category
   page). If you do not have the exact posting URL from a search result, **do not invent
   one** — list the role with `Link: (no direct link — search "<Company>" "<Title>")`
   instead of a guessed URL.
2. **Prefer the company's own ATS req link.** Authority order: company ATS specific req
   (greenhouse/lever/ashby/workday with a job id) > LinkedIn/Built In *specific* job page
   > aggregator. **De-dupe** the same role across reposts and keep the most authoritative.
3. **Aggregators rot fast** (JobLeads, BeBee, remoteleaf, Remotive reposts, Remote
   Rocketship, jobgether). If that's the only link you have, keep it but label it
   `⚠ aggregator repost — may be expired, confirm on company careers page`.
4. **Liveness pass before finalizing (required).**
   - **Roles from `scripts/live_roles.py` (Step 0) are already verified live** — they came
     straight from the ATS API. Use them as-is.
   - **Roles from WebSearch only cannot be liveness-verified from inside a locked-down
     session.** Re-searching just re-hits the same lagging index, so a role re-appearing in
     search is NOT proof it is open (this is exactly how expired roles get shipped). Do the
     re-search to drop obvious rot, but **never label a snippet-only role "confirmed live"
     or "posted today."** Mark every such link `⚠ unverified — confirm by opening` and tell
     the user the shortlist contains leads they must click to confirm.
   - **A WebFetch 403 is NOT evidence of expiry** — it's the board blocking automation. But
     the inverse is also true: a search hit is not evidence of liveness. When neither the
     API nor a fetch is available, the only real confirmation is the user opening the link.

## Step 3 — Quick Fit read + knockout scan (per role)
This is a **fast** version of the `/tailor-resume` Fit Score — snippet-level, not a full
resume build. For each candidate, using only what the profile supports:
- **Knockout scan first.** Flag hard blockers visible in the listing. A hard knockout
  **caps the role's read at ~25 and gets a ⛔ flag** — no tailoring fixes it. Check for:
  - **Language:** Josh is **English only (not bilingual)** — any role requiring a second
    language / bilingual fluency (Spanish, etc.) is a hard knockout. Watch the wording:
    "bilingual required," "Spanish fluency," "must be fluent in <language>."
  - **Location:** onsite in a city he can't do, relocation required, or a remote posting
    whose allowed-work-states list **excludes Colorado** → knockout. (A soft geo
    *preference* that still allows other US states is a watch-out, not a knockout.)
  - Required security clearance/license he lacks, work-auth constraints, or a hard
    minimum-years bar far above his.
- **Quick Fit band (0–100)** using the same dimensions as the tailor-resume rubric
  (must-haves met · seniority/scope · domain · differentiators · evidence), estimated
  from the snippet. Round to a band, don't over-precision a snippet-level read:
  - **80–100 Strong** — apply, competitive.
  - **60–79 Solid stretch** — apply with a sharp tailored resume + referral.
  - **40–59 Long shot** — only if excited.
  - **<40 / ⛔ knockout** — likely skip; say why.
- One line of **why** (the match) and one line of **watch-out** (the gap or unknown).

Be honest, not flattering — a tight shortlist of real fits beats a long padded one.

## Step 4 — Write the ranked shortlist
Create `searches/<YYYY-MM-DD>.md` (append a `-2`, `-3` suffix if one exists for today).
Sort **best fit first**; put ⛔ knockouts in a separate "Screened out" section at the
bottom. Use this structure:

```
# Role Search — <YYYY-MM-DD>

**Search plan:** <titles> · <locations/mode> · <filters applied>
**Searched:** <n> postings reviewed · <m> shortlisted

## Shortlist (best fit first)

### 1. <Company> — <Title>   ·  Fit ~<band> (<Strong/Stretch/Long shot>)
- **Type:** <Full-time | Part-time | Contract | Fractional | Freelance>
- **Where:** <location / remote>  ·  **Comp:** <as stated, or "not stated">
- **Link:** <specific-posting url — or `(no direct link — search "<Company>" "<Title>")`; add `⚠ aggregator` if it's a repost>  ·  **Liveness:** <confirmed in fresh search / aggregator-only, confirm on apply>
- **Why it fits:** <one line, true to profile>
- **Watch-out:** <gap / unknown / knockout note>
- **Next:** `/tailor-resume <url>`

### 2. …

## Screened out (knockouts / weak fit)
- **<Company> — <Title>** — ⛔ <reason> — <link>
```

Keep each entry to the fields above — this is a scannable triage doc, not a report.

## Step 5 — Recommend next actions
After writing the file:
1. Show the user the shortlist top (rank, company/title, Fit band) inline — 3–5 lines.
2. Point them at `searches/<date>.md` for the full list.
3. Recommend the **top 1–3** to tailor now, and offer to run `/tailor-resume` on them.
   If the user already asked for auto-tailoring, proceed to `/tailor-resume` on the top
   picks; otherwise wait for their pick.

## Step 6 — Guardrails (hard rules)
- **Every role must be real** — traceable to a search result with a working link. If a
  search yields nothing solid, say so plainly; do not invent listings to fill the page.
- **No fabricated or mismatched links.** Each link must be the specific posting for that
  exact company + title, from a real search result. Never reuse one role's URL for
  another, never hand-build/guess a URL, and never substitute a generic board landing
  page. No exact URL → write `(no direct link — search "<Company>" "<Title>")`.
- **Run the liveness pass** (Step 2 → Link quality & liveness) on every finalist and drop
  roles a fresh re-search can no longer surface. Prefer company-ATS links; flag aggregator
  reposts as possibly expired.
- **English-only knockout:** any role requiring a second language / bilingual fluency is
  screened out (see Step 3).
- **Don't fabricate comp, dates, or requirements** the listing doesn't state — write
  "not stated" and let `/tailor-resume` extract details from the real JD later.
- **Honest Fit reads.** Snippet-level scores are estimates — label them `~` and never
  inflate a knockout into a match.
- **Freshness:** prefer current postings; flag when a date can't be verified rather than
  presenting a stale or undated post as open. Since board fetches usually 403, treat
  posted/close dates from search snippets as **unverified** (mark them `~` or "per search
  result") — never state a date as confirmed when you couldn't open the page.

---

After the run, give the user a one-paragraph summary: how many postings were reviewed,
how many made the shortlist, the top 2–3 by Fit band, and which one you'd tailor first.
