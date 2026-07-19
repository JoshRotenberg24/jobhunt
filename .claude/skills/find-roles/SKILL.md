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

## Step 2 — Search the web for openings
Use **WebSearch** as the primary tool. You *may* try **WebFetch** to confirm a promising
listing, but expect it to fail: in this environment job boards (Greenhouse, Lever, Ashby,
Built In, LinkedIn, Indeed, HubSpot community, fractionaljobs, aggregators like BeBee /
JobLeads) almost always return **403** to automated fetches. So treat the **search-result
snippet as the primary evidence**, and mark any page-level detail you couldn't fetch
(exact comp, posted/close dates, full requirements) as **unverified** rather than stating
it as confirmed. Run several targeted queries, not one broad one — vary title × location ×
source. Good patterns:
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

> Many boards (Greenhouse/Lever/Workday/LinkedIn) block automated fetching. That's fine
> at this stage — the search snippet + link is enough for the shortlist. Deep parsing
> happens later in `/tailor-resume`, which will ask for a paste if the fetch walls off.
> **Because those same boards block fetching, the `/tailor-resume <url>` handoff will
> usually need the JD pasted in** — so tell the user to have the JD text handy, and
> prefer linking the most authoritative source (company ATS) over an aggregator repost.

**De-dupe** the same role reposted across aggregators; keep the most authoritative link
(company ATS > LinkedIn > aggregator). When you only found an aggregator repost (BeBee,
JobLeads, Remote Rocketship), say so and flag that the original posting should be
confirmed on apply.

## Step 3 — Quick Fit read + knockout scan (per role)
This is a **fast** version of the `/tailor-resume` Fit Score — snippet-level, not a full
resume build. For each candidate, using only what the profile supports:
- **Knockout scan first.** Flag hard blockers visible in the listing: onsite in a city he
  can't do, required security clearance/license he lacks, work-auth constraints, or a
  hard minimum-years bar far above his. A hard knockout **caps the role's read at ~25 and
  gets a ⛔ flag** — no tailoring fixes it.
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
- **Link:** <url>
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
