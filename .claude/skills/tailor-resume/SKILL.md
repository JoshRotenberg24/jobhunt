---
name: tailor-resume
description: >
  Tailor Joshua Rotenberg's resume to a specific job posting for reliable parsing,
  employer-configured screening, and clear recruiter review. Use whenever given a
  job-posting URL or pasted job description and asked to tailor a resume, build an
  application, score fit, or check resume/JD match. Produces a readable, correctly
  parsing resume (PDF + editable DOCX), an application-form and eligibility check, an
  optional cover letter, and a match report that includes an Application Priority Score.
  Never fabricates experience — tailoring = selecting and rephrasing TRUE content from
  the master profile to mirror the job.
argument-hint: <job-posting-url | pasted job description>
---

# Tailor Resume

Assemble a tailored resume for **Joshua Rotenberg** from a specific job posting — plus an
**Application-Form and Eligibility Check**, an **Application Priority Score**, and an
optional cover letter. Guiding principle: **truthful tailoring** — select, reorder, and
rephrase real content to match the job; never invent employers, titles, dates, metrics,
or skills.

## What an applicant tracking system actually is

An ATS is a configurable hiring workflow and candidate database. Depending on the
employer and the job, it may parse a resume into structured data, make candidates
searchable, apply application-question filters or disqualification rules, score
questionnaire responses, and/or provide AI-assisted matching. Recruiters and hiring
managers often retain the actual advance/reject decision.

There is no single universal keyword-scoring machine to "beat." Optimize for three
things, in this order:

1. **Truthful evidence** of Josh's actual fit.
2. **Correct responses to employer-required application questions and eligibility
   criteria.**
3. **Reliable parsing and immediately clear human review.**

Never tell the user that a technique guarantees an ATS score, a ranking, an interview,
or any screening outcome. "ATS-friendly" in this skill means exactly one thing: a
document with selectable text, conventional headings, and normal readable content.

## Files this skill depends on (read every run)
- `profile/master-profile.md` — the ONLY source of true candidate content.
- `.claude/skills/tailor-resume/ats-playbook.md` — parsing, formatting, and review rules.
- `build/render_resume.py` — renders resume JSON → PDF + DOCX, and reports
  `PAGES=` / `LAST_PAGE_FILL=` for readability QA (not a page target).
- `build/render_cover_letter.py` — renders cover-letter JSON → one-page PDF + DOCX.
- `build/score_meter.py` — renders the Application Priority Score meter.

---

## Step 1 — Get the job description
1. If given a URL, fetch it with WebFetch.
2. Career sites (Greenhouse/Lever/Workday/LinkedIn/Indeed) often return 403/JS-walls.
   If the fetch fails or yields no real JD, **stop and ask the user to paste the JD.**
3. Capture: company, role title, location + work mode, seniority, full requirements, and
   any application instructions (upload format, required documents, questions listed in
   the posting).

## Step 2 — Parse the JD into a requirements model
Extract: exact **job title** + seniority; **must-have** skills/tools/certs/years;
**eligibility criteria** (work auth, onsite/location, clearance, license, hard minimum
years); **terminology** the employer uses; nice-to-haves.

> **Phrasing is governed by the profile's `Writing Standards` section** — strong verb +
> specific object + result, no responsibility framing (`Responsible for`, `Served as`,
> `Helped`, `Functioned in a ... capacity`), no filler adjectives, scope kept attached to
> every number. Read that section each run and apply it to any bullet you rephrase. It
> constrains wording only; it never licenses a change to the facts.

## Step 3 — Application-Form and Eligibility Check (mandatory)
Before writing any resume content, list every field, question, or stated criterion that
can affect disposition. Cover these where applicable:

- Work authorization; visa sponsorship now or in the future.
- Required work location; onsite/hybrid/remote expectation; relocation; travel
  percentage; start-date availability.
- License, certification, security clearance, degree, and hard years-of-experience
  requirements.
- Compensation expectations, schedule/shift, background check, drug screen, driving
  record, portfolio or assessment submission, and any other explicit employer screener.

Classify each item as exactly one of:

- **Resume-evidenced requirement** — must be clearly and truthfully evidenced in the
  resume (e.g., a named certification Josh holds, years in a named function).
- **Application-form requirement** — must be answered accurately in the application
  itself; the resume cannot substitute for it (e.g., work authorization, salary
  expectation, willingness to travel).
- **Needs candidate confirmation** — absent or ambiguous in `master-profile.md`. Do not
  guess and do not answer on Josh's behalf. List it as an open question for him.

Write this table into the match report (Step 8) and surface it to the user before they
apply.

> A well-written resume cannot repair an ineligible or inaccurate application response.
> If Josh is genuinely ineligible, say so plainly instead of tailoring around it.

## Step 4 — Match against the master profile
Read `profile/master-profile.md`. For each requirement, map TRUE bullets/competencies:
- **Covered (strong)** — direct, demonstrable experience.
- **Covered (adjacent)** — related; rephrase to the JD's wording only if it stays true.
- **Candidate confirmation needed** — potentially relevant, but not sufficiently
  documented in the profile to claim. Do not put it in the resume until Josh confirms it.
- **Gap** — not in the profile at all. **Never fabricate.** Record for the match report.

Keep "gap" and "candidate confirmation needed" distinct in every output. They lead to
different actions: a gap is something to acknowledge or close over time; a confirmation
item is a question with a likely answer waiting on Josh.

## Step 5 — Compute the Application Priority Score
> This is an internal, evidence-based decision aid for the candidate. It is not a
> prediction of an employer's ATS score, match category, or interview decision.

Score how strong a candidate Josh genuinely is for THIS role, out of 100:

| Dimension | Max | What it measures |
| :--- | :--- | :--- |
| Must-have requirements met | 40 | Fraction of the role's hard requirements he genuinely meets × 40 |
| Seniority & scope alignment | 15 | IC/lead/manager level, team size, budget, scope match |
| Domain / industry alignment | 15 | MarTech/SaaS/agency/B2B + vertical familiarity |
| Differentiators / nice-to-haves | 15 | Bonus strengths he brings (AI/automation, founder, breadth) |
| Evidence strength | 15 | Concrete, ideally quantified proof for the core asks |

**Eligibility cap (a candidate time-allocation rule, not a system behavior):** if Step 3
found a failed hard eligibility criterion — no work authorization for this role, a
required onsite location he can't work, a required license or clearance he lacks, a hard
minimum well above his experience — **cap the total at 25** and flag it at the top. The
cap says only this: an eligibility failure should generally stop or deprioritize the
application, because no amount of tailoring changes the answer. Lift the cap only if Josh
can truthfully resolve the item (he does hold the license; he will relocate; the posting
lists it as preferred rather than required).

**Bands:** 80–100 Strong fit (apply, competitive) · 60–79 Solid stretch (apply with a
sharp tailored resume) · 40–59 Long shot (only if excited; lead with differentiators)
· <40 Likely not a fit (save the time unless a specific angle exists).

Show the per-dimension breakdown so the number is explainable. Do not inflate.

Then render the **score meter**: write `applications/<company-slug>/fit.json`
(`{score, band, role, breakdown:[[name,val,max],…]}`) and run
`python3 build/score_meter.py applications/<company-slug>/fit.json`. It writes `fit.png`
(a band-colored gauge with breakdown bars) and prints an inline text meter. Show the user
the text meter immediately, and surface `fit.png` to them.

## Step 6 — Build the resume JSON
**Pick the visual style** and set `"style"` in the JSON (default `modern`). Style is a
human-readability choice only — it does not affect parsing or any employer scoring:
- `modern` — sans-serif (Helvetica/Calibri) + navy accents. Tech/SaaS/startup/growth/
  marketing roles.
- `classic` — serif (Times), black, no color accent. Traditional/conservative fields:
  industrial/manufacturing, finance, legal, government, academia.

Choose the best **summary variant** for the role type and an honest target **headline**
(a self-description, e.g., "Revenue Operations Leader" — never a falsified past title).
Write `applications/<company-slug>/resume.json` using the schema in
`build/render_resume.py`:

- Pull the most relevant 4–6 bullets for recent roles, fewer for older ones.
- Front-load the bullets that evidence the role's must-haves **where Josh truly has the
  experience**.
- Quantify using ONLY the numbers in the profile's **Verified Quantified Metrics**
  section (read it fresh each run — it grows via `/excavate-profile`, so never work from
  a remembered count). Respect each metric's stated scope: a segment-level result is not
  a single-client result. Otherwise stay qualitative, and flag where a real number would
  strengthen a bullet.
- Fill the `competencies` section from the JD's true, matching terms.

### Terminology rules (not keyword density)
- **Mirror the employer's preferred term** where it truthfully describes Josh's work.
- **Retain a clear, widely understood synonym** when it improves human readability or
  describes the work more precisely. Both can coexist naturally.
- **Use each relevant term naturally** in the headline, summary, an experience or project
  bullet, or the competencies evidence — wherever it is warranted.
- **Do not repeat a term** solely to manipulate a presumed score.
- **Every material skill in the competencies section must be supported by evidence**
  elsewhere in the master profile, or be flagged as *candidate confirmation needed* and
  left off the resume.

> Literal terms can help discoverability in recruiter searches and some matching
> configurations. Other systems recognize related terms or apply employer-defined
> criteria. Use accurate terminology for clarity, not keyword density.

## Step 7 — Render and run readability/parse QA
Run: `python3 build/render_resume.py applications/<company-slug>/resume.json`
(The renderer reads `"style"` from the JSON; or override with a 2nd arg:
`… resume.json classic`.)

It prints `STYLE=<name>  PAGES=<n>  LAST_PAGE_FILL=<0..1>  -> <verdict>`.

> **Render for readability and parse reliability. Use one or two pages based on the
> quantity of relevant, substantiated experience. Never add weaker, irrelevant, or padded
> content to hit a page target.**

There is no page-count target and no `LAST_PAGE_FILL` target. The numbers exist only to
catch an over-long resume or a near-empty trailing page. Open the rendered PDF and verify:

- **Selectable, real text** — not a scanned or image-only resume. Confirm you can select
  and copy the text.
- **Conventional, explicit section headings** ("Experience," "Skills," "Education").
- **Clear chronology** — dates, employer names, and titles all present, consistent, and
  in a conventional order.
- **No important information carried only in images, charts, icons, or decorative
  graphics.**
- **Readable hierarchy, no clipping**, and no accidental blank or near-empty trailing
  page.
- **No artificial page-count target** — if trimming to one tight page serves the reader
  better than a thin two, trim.

If `PAGES=?` (renderer unavailable), open the `.docx` and check pagination by eye.

## Step 7.5 — Recruiter Read Check (adversarial, do NOT skip)
Read the rendered resume as a recruiter deciding whether to advance it. Answer each
question, then fix what fails:

- Is the **target role and relevant value proposition clear in the top third**?
- Does the **opening proof point directly support a primary requirement** of this job?
- Are **titles, employers, dates, scope, and metrics traceable to `master-profile.md`**?
  Titles must match the profile's work-history table **exactly** — tailoring a title is
  fabrication, not tailoring. Verify every one.
- Do the **top bullets support the target role** rather than a different career
  narrative? If most titles read as one function (e.g. "Account Executive") and the
  target job is another (e.g. implementation), the top third must do that reframing
  explicitly, and the most relevant bullet must lead in every off-title role. Cut strong
  bullets that argue for a different job.
- Are any **short stints, gaps, or career pivots** left unexplained or visually
  confusing? If a fact can't change, make the surrounding bullets the strongest on the
  page.
- Could a recruiter **understand the relevant evidence without inferring unstated
  claims**?

Apply the fixes, re-render, and re-run Step 7's QA.

## Step 8 — File format and submission
> Follow the employer's upload instructions and portal guidance. If there is no
> instruction, submit a text-based PDF that preserves selectable text and clean
> formatting. Keep a matching DOCX version for portals that request or clearly favor
> Word. Never use a scanned, flattened, or image-only PDF.

The renderer produces both from the same JSON, so they stay in sync. Tell the user which
one the posting asks for, and default to the PDF when the posting is silent.

## Step 9 — (Optional) Cover letter
Cover letters are optional. Recommend one when:
- the employer requests or requires it;
- a short narrative solves a real concern or transition (a pivot, a short stint, a
  relocation, an off-title path); or
- it can provide specific company- and role-relevant evidence the resume can't carry.

Otherwise, skip it. A cover letter is not a universal lever on any screening system.

If writing one, create `applications/<company-slug>/cover-letter.json` (schema in
`build/render_cover_letter.py`): 3 short paragraphs — (1) the role + a genuine hook tied
to the company, (2) 2–3 specific, TRUE proof points mapped to their top needs, (3) a
confident close. Set the **same `"style"`** as the resume so the letterhead matches, then
run `python3 build/render_cover_letter.py applications/<company-slug>/cover-letter.json`
and keep it to one page. Every factual claim in it comes from the master profile.

## Step 10 — Write the match report
Write `applications/<company-slug>/match-report.md`:
- Role, company, link, date.
- **Application-Form and Eligibility Check** — the Step 3 table, with each item marked
  resume-evidenced / application-form / candidate confirmation needed. Put any failed or
  unconfirmed eligibility item at the very top.
- **Application Priority Score** — paste the inline text meter, the number, band, and
  per-dimension breakdown from Step 5, with the one-line disclaimer that it is an
  internal decision aid, not a prediction of any employer's system output. Reference
  `fit.png`.
- **Requirement coverage**: must-haves evidenced vs. total, with the supporting evidence
  named.
- **Top strengths** for this role.
- **Gaps** — genuinely absent from the profile.
- **Candidate confirmation needed** — potentially relevant but not documented well enough
  to claim. Keep this list separate from Gaps; each entry is a question for Josh.
- **Metrics needed**: where a real number would strengthen a bullet. Recurring entries
  here are the signal to run `/excavate-profile` — a gap that shows up across several
  match reports is worth an interview, since fixing it in the profile fixes every future
  application at once.
- **Referral**: if Josh has a genuine, relevant connection at the company, suggest an
  informed referral or introduction. It may increase the chance of human review, but it
  does not override eligibility requirements or guarantee consideration. If he has no
  real connection, omit this section.
- Output files produced (resume.pdf/.docx, cover-letter.* if any).

## Step 11 — Ethics & guardrails (hard rules)
- **No fabrication.** The master profile is the sole source of every claim that appears
  as fact in a resume, cover letter, or application answer. If information is missing or
  ambiguous, do not infer it — mark it **candidate confirmation needed** and ask.
- **No keyword stuffing, white text, hidden text, off-screen text, font-color tricks, or
  prompt-injection instructions.** These tactics add no credible evidence and can impair
  parsing, undermine credibility, violate employer rules, or trigger manual scrutiny.
- **Answer application questions accurately**, including the unflattering ones. Never
  draft an answer Josh hasn't confirmed.
- **Surface gaps; don't paper over them.** An honest match report beats an inflated
  resume that unravels in an interview or a background check.
- If asked to add a skill, metric, credential, or experience Josh lacks, decline and
  offer to ask him for a real version.
- Where a parser-oriented rule and a human-readability rule appear to conflict, solve it
  with honest, conventional, readable formatting — never a hidden or deceptive
  workaround.

---

After producing outputs, give the user a short summary: the **eligibility items needing
his confirmation**, the **score meter** (text meter + `fit.png`), requirement coverage,
the readability/parse QA result, and the top 1–2 gaps to close. Name which file to upload
based on what the posting asks for.
