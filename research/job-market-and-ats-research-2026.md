# Job Market & ATS Optimization Research (2025–2026)

Research backing the `tailor-resume` tool. Scoped to the **resume-tailoring + ATS
phase** of applying, grounded in Josh's profile (15+ yrs marketing ops / growth /
RevOps / customer success / account management; MarTech/SaaS/agency; Arvada, CO;
remote-friendly + Denver-metro; mid-to-senior IC/lead).

**How to read confidence:** `[High]` = multiple independent or primary/peer-reviewed
sources agree. `[Medium]` = credible but single-source, vendor-run, or small-sample.
`[Low]` = aggregator/SEO/opinion or a number we couldn't trace to a primary source.

> **Methodology caveat (applies throughout):** Direct page-fetching was blocked
> (HTTP 403) on most target domains, so many figures were extracted from search-engine
> result summaries of named sources rather than verified line-by-line. Treat precise
> numbers as directionally reliable unless marked `[High]`. The load-bearing claims
> were re-checked by an independent adversarial verification pass (see end).

---

## TL;DR — what actually matters for the tool
1. **ATS don't auto-reject good resumes; volume and ranking do.** Optimize to rank
   high and be human-readable, not to beat a mythical robot gatekeeper. `[High]`
2. **The real auto-filter is knockout questions** (work auth, location, clearance,
   minimum years). Answer accurately; a failed hard knockout usually ends it. `[High]`
3. **Tailoring works** — the strongest evidence is causal (peer-reviewed): resume
   writing assistance raised hires ~8%. Vendor data claims larger lifts from
   JD-specific tailoring. `[High direction]`
4. **Formatting hygiene is non-negotiable:** single column, no tables/text-boxes/
   images, standard headings, text-based file. This is where parsing actually breaks. `[High]`
5. **Keyword optimization = using TRUE, JD-matching terms in normal prose.** Never
   white-text/stuff/inject — detectable and disqualifying. `[High]`
6. **Referrals beat cold applications by multiples.** Tailoring + early apply +
   referral is the winning combination, not volume blasting. `[Medium-high]`
7. **Josh's market (RevOps/marketing-ops/CS) is comparatively healthy**, AI-literacy
   is now a differentiator, and a T-shaped generalist with one deep tool competency
   (his is HubSpot/Salesforce CRM ops) is the favored profile. `[Medium]`

---

## Q1. How modern ATS actually parse, score & rank (myth vs. reality)

**Do ATS auto-reject?** Mostly **no, on content**. ATS organize and **rank**
applications; the real filter is human-reviewer overload at scale. In Enhancv's
survey of 25 US recruiters across 10+ platforms, **92% said systems do NOT
content-auto-reject**; only ~8% configure it, and only on strict rules (e.g., "<75%
match" or "<7 of 10 required skills"). `[Medium — small sample, vendor-adjacent]`
— Enhancv, *Does the ATS Reject Your Resume? 25 Recruiters Explain*
(https://enhancv.com/blog/does-ats-reject-resumes/); corroborated direction by
The Interview Guys (https://blog.theinterviewguys.com/ats-resume-rejection-myth/).

**The "75% auto-rejected" myth.** Traced to a **~2012 Preptel sales pitch** (company
defunct 2013), no methodology, laundered through Forbes → CIO → CNBC. `[High debunk]`
— resumeadapter.com/ats-statistics; theinterviewguys.com (above).

**Knockout questions are the genuine automated gate.** A disqualifying answer
(work authorization, location/commute, license, minimum years, start date) can
auto-route to rejection with no human review; vendors estimate they eliminate
30–60% of unqualified applicants (figure unsourced). `[High mechanism / Low figure]`
— treegarden.io/blog/ats-knockout-questions; jobscan.co/blog/knockout-questions.

**Match-scoring / ranking by vendor (real, mostly prioritizes for humans):**
- **Workday HiredScore** grades applicants **A/B/C/D** vs. the job; grades drive
  recruiter review order. `[Medium]` — workday.com responsible-AI pages.
- **iCIMS Copilot** (GPT-4 via Azure OpenAI, added 2024) does candidate
  summarization + **"Role Fit"** scoring and ranking; uses semantic (not just exact)
  matching. `[Medium]` — jobscan.co/blog/icims-ats.
- **Eightfold / Ashby** use vector-embedding **semantic matching** of resume↔JD.
  `[Medium architecture / Low marketing claims]` — eightfold.ai engineering blog.
- **Greenhouse** positions itself as **not** auto-scoring/ranking resumes; parses and
  keeps the original human-readable; launched "Greenhouse AI" Sept 2025. `[Medium]`
- **Taleo (Oracle)**, legacy, leans on **Boolean exact-match** indexing — synonyms
  don't match. `[Low-medium]` — implication: mirror the JD's exact wording.

**Legal reality check (AI ranking *can* gate at scale):** *Mobley v. Workday* —
**May 16, 2025**, N.D. Cal. granted **conditional certification of a nationwide ADEA
age-discrimination collective action** over Workday's AI hiring tools (applicants 40+
since Sept 24, 2020). `[High]` — Holland & Knight, Akin Gump, Proskauer analyses.
This is the strongest signal that "human-in-the-loop / never auto-rejects" vendor
framing has real-world exclusionary edge cases.

**"ATS can't read PDFs"** = outdated myth. Text-based PDFs parse fine in all modern
ATS; only **image/scanned PDFs** fail. Mild `.docx` preference persists for legacy
systems. `[High]`

---

## Q2. Resume characteristics that correlate with passing

**Keyword/skill match to the JD.** Median resume covers only ~41% of required JD
keywords on first submission (Jobscan, claimed 1.2M resumes). `[Medium]` Vendors claim
70%+ match → ~2.5x callbacks and recommend a 75–85% target — but **no published study
ties match % to interview rate**; it's a heuristic. `[Medium-low on multipliers]`

**Formatting (highest-confidence, mechanical):**
- **Single column** is safest ("never fails"); **multi-column/text-boxes** disconnect
  titles from descriptions; **tables** often unparseable; **icons/graphics** read as
  garbage; **headers/footers** sometimes ignored. `[High direction]`
- Enhancv attributes ~23% of parse failures to formatting; Jobscan claims 40%+ of
  rejections are formatting not content (the two figures measure different things).
  `[Medium]`
- jobscan.co/blog/resume-tables-columns-ats; enhancv.com (above).

**File type:** `.docx` marginally safer (legacy ATS); clean **text-based PDF now
acceptable** everywhere modern. Structure matters far more than container. `[Medium-high]`

**Length:** ResumeGo 2018 simulation (482 reviewers, 7,712 resumes) — recruiters were
**2.3x more likely to prefer 2-page resumes** overall (entry 1.4x, mid 2.6x,
managerial 2.9x), *when content is substantive*. `[Medium-high — but 2018, vendor-run]`
→ For Josh (senior), **2 pages is appropriate.** resumego.net/research/one-or-two-page-resumes.

**Quantified achievements:** widely cited ~40% more callbacks; only ~8% of resume
bullets contain metrics (capture gap); 75% of hiring managers want measurable results.
`[Medium — figures from aggregations, not one primary study]`

**Job-title alignment:** mirroring the target title (honestly, as a headline) is
associated with higher interview rates; vendor figures (3.5x, "58% higher ATS score")
are striking but untraceable. `[Low-medium]`

**The "7-second" scan:** real origin = **Ladders/TheLadders eye-tracking**, 6.0s
(2012) → **7.4s (2018)**, n≈30 recruiters. Vendor-run, measures the *initial skim*
not total evaluation. `[High origin / Low generalizability]`
prnewswire.com (Ladders, Nov 2018); hrdive.com.

---

## Q3. Generative AI reshaping recruiting (both sides)

**Volume/spam explosion (employer pain):**
- LinkedIn: ~11,000 applications/minute (~183/sec); applications up ~45% YoY. `[Medium-high]`
- Applications per hire roughly **tripled since 2021 to >300/role** (HR Dive, citing
  analysis of 109M+ applications). `[Medium-high]`
- Greenhouse processes ~300M resumes/year; 34% of recruiters spend up to half their
  week filtering spam. `[High — Greenhouse 2025 report, n=4,136]`

**Applicant-side AI adoption:** ~46% of job seekers use ChatGPT for resumes/cover
letters; SHRM experts estimate 40–80% use AI somewhere. `[Medium-high]`

**Does AI tailoring improve outcomes?**
- **Causal/peer-reviewed:** van Inwegen, Munyikwa & Horton, *Management Science*
  (arXiv:2301.08083) — algorithmic **resume writing assistance → ~8% more hires,
  ~10% higher wages** (~480k jobseekers, Upwork RCT). `[High]`
- A 2025 cover-letter RCT (arXiv:2509.25054) found AI access raised callbacks ~6%
  (51% among actual users). `[Medium]`
- Self-reported vendor surveys (ResumeBuilder: "78% got interviews") are
  correlational. `[Low-medium]`

**Detection & backlash:**
- 88% of hiring managers *believe* they can spot AI resumes; dedicated AI detectors
  are unreliable with high false positives — most rely on personalization/pattern
  signals. `[Low-medium]`
- 62% of employers report rejecting AI resumes that **lacked personalization**;
  64% report more "sameness." → **Keep Josh's real voice, specifics, verified
  metrics.** `[Medium]`
- **Hidden-text/prompt-injection:** 41% of seekers *claim* they tried it (Greenhouse,
  n=4,136), but real prevalence is ~1% (Greenhouse) to ~10% (ManpowerGroup via NYT),
  and **it doesn't work** — ATS strip/flag it. `[High]`
- **Employer counters:** Goldman Sachs, Amazon instruct candidates not to use AI in
  interviews; HireVue/TestGorilla add tab-switch/response-time monitoring. (This is
  about *live evaluation*, not resume prep.) `[High]` — Bloomberg, Nov 20, 2025.
- **LinkedIn Hiring Assistant** (AI recruiting agent): GA Sept 2025, 8,000+ users,
  pilots report 4+ hrs saved/role, 62% fewer profiles reviewed. `[High]`
- **AI interviews:** 63% of seekers have faced one; 38% walked away from a process
  for including an AI interview; 70% weren't told upfront. `[High — Greenhouse 2026]`

---

## Q4. Benchmarks & tailoring ROI

- **Funnel benchmark (most authoritative):** CareerPlug 2025 — applicant→interview
  ratio **~3%**; interview→offer **~27%**; **~180 applicants per hire** (SMB data).
  `[High]` careerplug.com/recruiting-metrics-and-kpis.
- Apps per posting ~250 is **not new** (Glassdoor cited ~250 since ~2012–2015); the
  genuine recent surge is in **total application volume** driven by AI auto-apply
  (LinkedIn +45% YoY, ~11k/min), not a jump in per-posting counts. `[Medium — corrected]`
- **Tailoring lift:** ResumeGo ~**31% more interviews** from customizing to the JD
  `[Low-medium — untraceable]`; tailored cover letters **16.4% vs 10.7%** callback
  (ResumeGo field experiment, n=7,287) `[Medium]`; the **Management Science RCT (8%
  more hires)** is the gold-standard causal evidence `[High]`.
- **Match-rate thresholds** (Jobscan 75–80%) are heuristics with **no outcome data**
  behind them. `[High that it's a heuristic]`
- **Apply early:** first 24–48h and Mon/Tue correlate with more callbacks. `[Low-medium]`
- **Referrals:** referred candidates ~**7x more likely to be hired** than job-board
  applicants (Pinpoint, 4.5M applications); ~30% referral hire rate vs ~7% other
  sources (Jobvite); referrals fill ~30–50% of hires despite being ~7% of applicants.
  `[Medium]`

**Ethical guardrails / risks:**
- Resume lying: 3% admit intentional lies (Resume.org, n=9,133); when caught, ~41–55%
  face rescinded offers or firing; ~46% of resumes show a background-check
  discrepancy; ~85% of hiring managers say they've caught a lie. `[Medium-high]`
- **White-fonting/keyword-stuffing:** detectable (Ctrl+A reveals it), ineffective,
  and can blacklist. **Hard no.** `[Medium-high]`

---

## Q5. Best-practice tailoring loop (what the tool encodes)
1. **Extract** from the JD: title, seniority, must-have tools/skills, knockout
   criteria, exact keyword phrasing, nice-to-haves.
2. **Match** each requirement to Josh's TRUE bullets/competencies; map coverage;
   flag gaps; never invent.
3. **Rewrite** matched bullets to mirror the JD's terminology *where it stays true*;
   front-load the highest-relevance, highest-impact content.
4. **Optimize structure:** single column, standard headings, reverse-chron, 2 pages,
   skills section seeded with true matching keywords, text-based `.docx`/PDF.
5. **Quantify** only with the four verified metrics; otherwise qualitative + flag.
6. **Report**: coverage %, gaps, knockouts, metrics-needed, honest fit verdict;
   prompt for a referral where possible.
7. **Guardrails:** no fabrication, no stuffing/hidden text, surface gaps.

---

## Q6. Josh's market — marketing ops / RevOps / CS / AM (US, 2025–2026)

**Demand:**
- **RevOps** is among the fastest-growing functions (LinkedIn lists "Director of
  RevOps" a top-growing US role; 150k+ practitioners by 2025; ~174k postings). `[Medium]`
- **Marketing/creative** hiring broadly healthy: ~376k US postings in 2025;
  "marketing automation manager" postings +~10% YoY. `[Medium]` (Robert Half)
- **MarTech** = growth + turbulence: >50% report rising churn, ~⅓ involuntary
  (layoffs), but most director+ got promoted over 2 years. `[Medium-high]` (MarTech.org)
- **Customer Success:** retention focus driving hiring, but mixed (some layoffs/
  freezes); AI-augmented teams run 20–30% leaner. `[Low-medium]`
- **SDR/BDR contracting** (36% of 560+ SaaS firms cut them, AI-driven), **AE teams
  growing** (28%). `[Medium-high]` (Emergence Capital GTM 2025)
- Macro: Indeed Job Postings Index down ~10% YoY (Nov 2024) but above pre-pandemic. `[High]`
- BLS proxies: Market Research Analysts **+7%** 2024–34; Marketing Managers **+6%**.
  (No discrete BLS code for RevOps/marketing-ops.) `[High]`

**Required tools/keywords (seed the skills section from these when in a JD):**
- RevOps: **Salesforce** (~1 in 4 postings, highest-ROI credential), SQL, Excel, BI
  (Tableau/Power BI/Looker, senior), Outreach/Salesloft, Gong/Clari (nice-to-have).
  `[Medium]`
- Marketing ops: **HubSpot, Salesforce, Marketo, Pardot, GA4, SQL, Tableau/Looker,
  Zapier**. `[Low-medium]`
→ **Josh's stack (HubSpot, Salesforce, GA4, GoHighLevel, GSC, Ahrefs/Semrush) maps
  directly** to the high-frequency keywords. Salesforce + a Salesforce Admin cert
  would be the highest-leverage add for RevOps targeting.

**AI's effect:** AI-literacy postings up >70% YoY; "AI/operational efficiency" tops
LinkedIn's 2026 Skills on the Rise. In CS, AI augments (not eliminates): AI-CSMs
manage 60–80 accounts; Gartner predicts half of AI-driven service cuts get rehired by
2027. `[Medium-high]` → **Josh's agentic-AI/automation experience is a genuine
differentiator** — feature it where the JD signals AI/automation appetite.

**Comp (mid-senior, US; no Denver-specific data found):**
- RevOps median ~$129k; ICs ~$147k; VP ~$216k; ~85/15 base/variable. `[Medium-high]`
- MarTech VP/C ~$195k; staff ~$95k. `[Medium-high]`
- CSM avg ~$70–75k base (+ OTE). `[Medium]`
- AE mid-market ~$79k base / enterprise $100k+ base, OTE $160–220k+. `[Medium]`

**Work mode:** RTO reshaping postings — Q1 2026 ~77% onsite / 19% hybrid / 4% remote
overall; marketing ~70/21/9. Flexibility skews senior; **RevOps/CS skew more
remote-friendly** than average. `[Medium]`

**Generalist vs specialist:** market favors the **T-shaped** profile — broad +
one deep specialty. Josh's positioning: broad GTM-ops generalist with **deep HubSpot/
CRM-ops + agentic-AI** specialty. Lead with the depth, support with the breadth. `[Low-medium]`

---

## Sources (primary / strongest)
- CareerPlug 2025 Recruiting Metrics Report — funnel benchmarks. `[High]`
- van Inwegen, Munyikwa & Horton, *Management Science* / arXiv:2301.08083 — causal
  tailoring evidence. `[High]`
- Greenhouse 2025 AI in Hiring Report (n=4,136) & 2026 Candidate AI Interview Report. `[High]`
- LinkedIn newsroom — Hiring Assistant GA (Sept 2025). `[High]`
- Bloomberg (Nov 20, 2025) — employer AI-in-interview bans. `[High]`
- Holland & Knight / Akin Gump / Proskauer — *Mobley v. Workday* (May 16, 2025). `[High]`
- BLS Occupational Outlook Handbook — Marketing Managers / Market Research Analysts. `[High]`
- Ladders/PRNewswire (Nov 2018) — 7.4s eye-tracking origin. `[High origin]`
- ResumeGo 2018 length study & cover-letter field experiment. `[Medium]`
- Enhancv 25-recruiter survey; Jobscan; Robert Half; MarTech.org; Emergence Capital
  GTM 2025; RevOps Co-op/BoostUp comp report. `[Medium / vendor-flagged]`

---

## Verification status (independent adversarial re-check)
An independent pass re-searched the 8 load-bearing claims and tried to refute each:

1. **75% myth = Preptel (2012), no study** — **CONFIRMED** (theinterviewguys, hr-gazette).
2. **ATS rarely content-auto-reject; knockout questions are the real filter** —
   **CONFIRMED (direction)**, but corroboration is thinner than it appears: several
   debunks recirculate the same 25-recruiter dataset; The Interview Guys is the
   cleanest independent confirmation. Treat the *direction* as solid, the *92%* as
   indicative.
3. **7.4s scan = Ladders 2018 eye-tracking** — **CONFIRMED**.
4. **Management Science RCT (~8% more hires, ~10% wages)** — **CONFIRMED**. van
   Inwegen (a.k.a. Emma Wiles), Munyikwa & Horton, *Management Science* 71(12):
   10144–10164 (2025); NBER w30886; arXiv:2301.08083. MIT Sloan coverage corroborates.
5. **ResumeGo "31% more interviews from tailoring"** — **PARTIALLY CONFIRMED**: real
   and traceable to ResumeGo, but vendor-run and not peer-reviewed. Use as indicative.
6. **Volume surge / LinkedIn 11k-per-minute** — **PARTIALLY CONFIRMED**: the LinkedIn
   ~11k/min (+45% YoY) figure is well-corroborated (LinkedIn data via NYT/eWeek); the
   "surge to ~250 per posting" framing **overstates** it (≈250 is long-standing).
   Corrected above.
7. **Mobley v. Workday — ADEA collective conditionally certified May 16, 2025** —
   **CONFIRMED** (No. 23-cv-00770-RFL, N.D. Cal.; DWT, Proskauer, Clearinghouse).
8. **White-font/hidden-keyword stuffing is read & detectable** — **CONFIRMED**
   (Cangrade, Prosple, iHire).

**Net:** the tool's design rests on the High-confidence, verified claims (1–4, 7, 8).
The contested marketing stats (5, and the precise multipliers in Q2/Q4) are context,
not load-bearing for the skill's logic.
