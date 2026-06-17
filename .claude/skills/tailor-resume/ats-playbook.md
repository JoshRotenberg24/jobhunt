# ATS & Resume Optimization Playbook (2025–2026)

Evidence-based ruleset for the `tailor-resume` skill. Each rule notes its confidence
and the research behind it. Full sourcing lives in
`research/job-market-and-ats-research-2026.md`. Where the research is vendor-driven
or thinly sourced, the rule is written conservatively.

## Mental model: what actually filters candidates
- **ATS rarely auto-reject on resume *content*.** They parse, index, and **rank**
  applications for human reviewers. The dominant real-world filter is **volume**:
  when 250+ people apply and a recruiter reviews the top ~20, being ranked low is a
  functional rejection even though nothing "rejected" you. *(High confidence.)*
- **The genuine automated gate is knockout/screening questions** — work
  authorization, location/onsite, clearance, license, minimum years. A disqualifying
  answer can auto-route to rejection with no human review. **Answer these
  accurately; if Josh fails a hard knockout, the application is likely dead** —
  surface it. *(High confidence.)*
- **Match-scoring is real but mostly prioritizes, not rejects:** Workday HiredScore
  (A–D grades), iCIMS Copilot/"Role Fit," Eightfold/Ashby semantic matching rank
  candidates for recruiters. Ranking high = getting seen. *(Medium-high.)*
- **The "75% auto-rejected by ATS" stat is a myth** — traced to a ~2012 Preptel
  sales pitch with no study behind it. Don't optimize around a fiction; optimize for
  **ranking + human readability**. *(High confidence on the debunk.)*

## Formatting rules (highest-confidence, mechanical)
1. **Single-column layout only.** Multi-column and text boxes break parsing —
   parsers read all of column A then column B, disconnecting titles from
   descriptions. *(High.)*
2. **No tables** for content. Many ATS can't reliably parse table cells. *(High.)*
3. **No images, icons, logos, charts, or photos.** They parse as garbage or are
   dropped. *(High.)*
4. **Nothing critical in headers/footers.** Some parsers ignore them; keep name and
   contact in the body. *(High.)*
5. **Standard section headings** — "Experience," "Education," "Skills." Don't get
   clever ("Where I've Made an Impact"); parsers map on the standard labels. *(High.)*
6. **Standard, readable fonts**; no decorative typefaces. *(Medium-high.)*
7. **Reverse-chronological** structure. Most parsers and recruiters expect it. *(High.)*

## File type
- **Default to `.docx`** — marginally safer across older/legacy ATS. *(Medium-high.)*
- **A clean, text-based, single-column PDF is now acceptable** in all modern ATS.
  The real failure mode is an **image/scanned PDF** (e.g., "print to PDF" from Canva)
  where text is flattened and unreadable. Test: if you can highlight/copy the text,
  the ATS can read it. *(High.)*
- "ATS can't read PDFs" is an **outdated myth** — only image PDFs fail. *(High.)*

## Keywords & matching
- **Mirror the JD's exact terminology** for skills Josh genuinely has. Some systems
  (Taleo-class) exact-match, so "project management" ≠ "program management." Use the
  posting's words. *(High on mechanism.)*
- **Target a high keyword match**, but treat specific thresholds as heuristics, not
  guarantees. Jobscan recommends ~75–80% match; **there is no published evidence
  tying a match % to interview rate** — it's a product heuristic. Aim to cover the
  must-haves naturally rather than chasing a number. *(High that it's a heuristic.)*
- **A dedicated Skills/Core Competencies section** is a clean, honest place to surface
  matching tools/keywords (HubSpot, Salesforce, GA4, RevOps, lifecycle, QBRs, etc.).
- **NEVER** use white/hidden text, off-screen text, font-color tricks, or hidden
  prompt-injection instructions. Parsers extract raw text regardless of color, so
  hidden keywords appear as a visible block; recruiters reveal them with Ctrl+A; some
  ATS flag them. Outcome is rejection or blacklisting. *(High.)* Self-reported "I
  tried it" rates are high (~41% in one survey) but real prevalence is ~1–10%, and
  it doesn't work — don't do it.

## Content quality
- **Quantify with real numbers only.** Quantified bullets read as more credible and
  are associated with more callbacks; the only verified metrics available are the
  four in the master profile (Wix: +30% traffic, +25% conversion; 15+ yrs; 5+ yrs
  HubSpot). For everything else, use concrete qualitative outcomes and flag where a
  real number would help. *(Medium on the callback lift; High on "don't fabricate.")*
- **Front-load relevance.** Recruiters' initial scan is short (the well-known "~7
  seconds" figure is from a 2018 Ladders eye-tracking study, n≈30 — indicative, not
  gospel, and it measures the *initial skim*, not total evaluation). Put the
  most JD-relevant, highest-impact bullets first. *(High that the scan is brief.)*
- **Title alignment helps** — lead with an honest professional headline matching the
  target role; don't falsify past titles. *(Medium.)*
- **Length:** 2 pages is fine and often preferred for mid/senior candidates **when
  the content is substantive** (ResumeGo 2018 simulation: reviewers preferred 2-page
  resumes, esp. for mid/managerial). Don't pad to fill; cut filler that dilutes. *(Medium-high.)*

## Does tailoring actually help? (why this skill exists)
- **Yes, with the strongest evidence being causal:** a peer-reviewed randomized field
  experiment (van Inwegen, Munyikwa & Horton, *Management Science*, arXiv:2301.08083)
  found algorithmic **resume writing assistance raised hires ~8% and wages ~10%**.
  *(High.)*
- Vendor experiments report larger tailoring lifts (ResumeGo: ~31% more interviews
  from customizing to the JD; tailored cover letters ~16% vs ~11% callback). Treat
  the magnitudes as **indicative** (vendor-run), the direction as **reliable**.
  *(Medium.)*
- **Referrals dwarf cold applications** (referred candidates are several-fold more
  likely to be hired). Where Josh has a network connection to the company, the match
  report should prompt him to pursue a referral in parallel. *(Medium-high.)*

## AI-era cautions (2025–2026)
- Total application volume has surged — LinkedIn ~11k applications/minute, +45% YoY,
  driven by AI auto-apply (~250 applicants/posting is typical, though that per-posting
  number is long-standing) — so **ranking and relevance matter more, generic blasting
  matters less.** Quality-tailored + early application + referral beats volume. *(Medium-high.)*
- Employers increasingly notice **AI "sameness."** Keep Josh's real voice, specifics,
  and verified metrics — generic AI phrasing is a liability. *(Medium.)*
- Some employers ask candidates not to use AI in *interviews/assessments* and watch
  for it; that's about live evaluation, not resume prep. Tailoring a resume with AI is
  normal and widespread. *(Medium.)*
