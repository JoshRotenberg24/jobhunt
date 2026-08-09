---
name: tailor-resume
description: >
  Tailor Joshua Rotenberg's resume to a specific job posting and optimize it to
  pass modern ATS screening and recruiter review. Use whenever given a job-posting
  URL or pasted job description and asked to tailor a resume, build an application,
  score fit, or check resume/JD match. Produces a polished, balanced 2-page resume
  (PDF + editable DOCX), an optional cover letter, and a match report that includes a
  personal Fit Score. Never fabricates experience — tailoring = selecting and
  rephrasing TRUE content from the master profile to mirror the job.
argument-hint: <job-posting-url | pasted job description>
---

# Tailor Resume

Assemble a tailored, ATS-optimized, **professional, balanced 2-page** resume for
**Joshua Rotenberg** from a specific job posting — plus a personal **Fit Score** and an
optional cover letter. Guiding principle: **truthful tailoring** — select, reorder, and
rephrase real content to match the job; never invent employers, titles, dates, metrics,
or skills.

## Files this skill depends on (read every run)
- `profile/master-profile.md` — the ONLY source of true candidate content.
- `.claude/skills/tailor-resume/ats-playbook.md` — evidence-based ATS/formatting rules.
- `build/render_resume.py` — renders resume JSON → polished PDF + DOCX, and reports
  `PAGES=` / `LAST_PAGE_FILL=` so you can enforce the balanced-2-page rule.
- `build/render_cover_letter.py` — renders cover-letter JSON → one-page PDF + DOCX.

---

## Step 1 — Get the job description
1. If given a URL, fetch it with WebFetch.
2. Career sites (Greenhouse/Lever/Workday/LinkedIn/Indeed) often return 403/JS-walls.
   If the fetch fails or yields no real JD, **stop and ask the user to paste the JD.**
3. Capture: company, role title, location + work mode, seniority, full requirements.

## Step 2 — Parse the JD into a requirements model
Extract: exact **job title** + seniority; **must-have** skills/tools/certs/years;
**knockout criteria** (work auth, onsite/location, clearance, license, hard minimum
years); **keywords/phrasing** (mirror exact terms — some ATS exact-match); nice-to-haves.

> **Phrasing is governed by the profile's `Writing Standards` section** — strong verb +
> specific object + result, no responsibility framing (`Responsible for`, `Served as`,
> `Helped`, `Functioned in a ... capacity`), no filler adjectives, scope kept attached to
> every number. Read that section each run and apply it to any bullet you rephrase. It
> constrains wording only; it never licenses a change to the facts.

## Step 3 — Match against the master profile
Read `profile/master-profile.md`. For each requirement, map TRUE bullets/competencies:
- **Covered (strong)** — direct, demonstrable experience.
- **Covered (adjacent)** — related; rephrase to the JD's wording only if it stays true.
- **Gap** — not in the profile. **Never fabricate.** Record for the match report.

## Step 4 — Compute the Fit Score (be honest, not flattering)
Score how strong a candidate Josh is for THIS role, out of 100. This is about HIM, and
is separate from the resume's keyword match. Use this transparent rubric:

| Dimension | Max | What it measures |
| :--- | :--- | :--- |
| Must-have requirements met | 40 | Fraction of the role's hard requirements he genuinely meets × 40 |
| Seniority & scope alignment | 15 | IC/lead/manager level, team size, budget, scope match |
| Domain / industry alignment | 15 | MarTech/SaaS/agency/B2B + vertical familiarity |
| Differentiators / nice-to-haves | 15 | Bonus strengths he brings (AI/automation, founder, breadth) |
| Evidence strength | 15 | Concrete, ideally quantified proof for the core asks |

**Knockout rule:** if a HARD knockout fails (no work auth, required onsite he can't do,
required license/clearance he lacks, hard minimum years far above his), **cap the total
at 25** and flag it prominently — no amount of tailoring fixes a knockout.

**Bands:** 80–100 Strong fit (apply, competitive) · 60–79 Solid stretch (apply with a
sharp tailored resume + referral) · 40–59 Long shot (only if excited; lead with
differentiators; chase a referral) · <40 Likely not a fit (save energy unless a special
angle exists).

Show the per-dimension breakdown so the number is explainable. Do not inflate.

Then render the **score meter** (the tool's UI for the Fit Score): write
`applications/<company-slug>/fit.json` (`{score, band, role, breakdown:[[name,val,max],…]}`)
and run `python3 build/score_meter.py applications/<company-slug>/fit.json`. It writes
`fit.png` (a band-colored gauge with breakdown bars) and prints an inline text meter.
Show the user the text meter immediately, and surface `fit.png` to them.

## Step 5 — Build the resume JSON
**Pick the visual style** for the role and set `"style"` in the JSON (default `modern`):
- `modern` — sans-serif (Helvetica/Calibri) + navy accents. Use for tech/SaaS/
  startup/growth/marketing roles.
- `classic` — serif (Times), black, no color accent. Use for traditional/
  conservative fields: industrial/manufacturing, finance, legal, government, academia.

Choose the best **summary variant** for the role type and an honest target **headline**
(a self-description, e.g., "Revenue Operations Leader" — never a falsified past title).
Write `applications/<company-slug>/resume.json` using the schema in
`build/render_resume.py`:
- Order/word bullets to front-load the JD's must-have keywords **where Josh truly has
  the experience**; mirror the JD's terminology for genuine skills.
- Pull the most relevant 4–6 bullets for recent roles, fewer for older ones.
- Quantify using ONLY the numbers in the profile's **Verified Quantified Metrics**
  section (read it fresh each run — it grows via `/excavate-profile`, so never work from
  a remembered count). Respect each metric's stated scope: a segment-level result is not
  a single-client result. Otherwise stay qualitative, and flag where a real number would
  strengthen a bullet.
- Seed a `competencies` section with the JD's true, matching keywords (honest keyword
  optimization — never stuffing).
- Set `"filename_role"` to the posting's role type, 2–4 words (`"Implementation
  Specialist"`, `"Revenue Operations Manager"`). This names the file Josh actually
  uploads. **Role type only — never the company name.** At his application volume, a
  file named for one company will eventually be uploaded to another, and the recruiter
  sees it. No versions, no dates, no "final".

## Step 6 — Render and enforce the balanced 2-page rule
Run: `python3 build/render_resume.py applications/<company-slug>/resume.json`
(The renderer reads `"style"` from the JSON; or override with a 2nd arg:
`… resume.json classic`.)

The renderer writes four files: `resume.pdf`/`resume.docx` for the repo, plus
`<Name>_<Role>.pdf`/`.docx` copies marked `UPLOAD THIS`. **Tell Josh to submit the
named copy**, `.docx` by default per `ats-playbook.md`. A file called `resume.pdf` is
anonymous in a downloads folder holding two hundred of them.

**Always send the rendered PDF into the conversation** with `SendUserFile` once the page
balance passes, and again after any re-render. Josh reads the resume in the thread rather
than opening the repo, so a build he cannot see is a build he cannot approve.

It prints `STYLE=<name>  PAGES=<n>  LAST_PAGE_FILL=<0..1>  -> <verdict>`. **Iterate until
`PAGES=2` and `LAST_PAGE_FILL ≥ 0.6` (target ~0.7–0.95):**
- **>2 pages:** trim the least-relevant bullets (oldest roles first), tighten wording.
- **<2 pages, or page 2 sparse (`fill < 0.6`):** add real depth — more relevant bullets
  to recent roles, an additional true earlier role, or a fuller competencies section.
  Do NOT pad with fluff or fabrications; pull from the profile's bullet bank.
Re-run after each edit. The goal is a resume that looks deliberately built for two full,
balanced pages — never a half-empty page 2.

If `PAGES=?` (renderer unavailable), keep content to the calibrated budget that yields
two pages with this template (~6 roles, ~3–5 bullets on recent roles) and note it.

## Step 6.5 — The tired-recruiter read (adversarial check, do NOT skip)
Before writing anything else, read the rendered resume as a recruiter at 4:45pm on
resume #31 who has ~10 seconds and is looking for a reason to pass. Verdict: interview
or pass? Then **fix the reason.** Check specifically:

- **Title drift.** Do the titles on the page match `master-profile.md` EXACTLY? Tailoring
  a title is fabrication, not tailoring. This is an easy mistake to make while
  optimizing for a JD — verify every one against the profile's work-history table.
- **The wrong-career read.** If most titles say one thing (e.g. "Account Executive") and
  the target job is another (e.g. implementation), a skimmer pattern-matches on titles
  and passes. The top third must do that reframing work explicitly, and the
  most-relevant bullet must lead in every off-title role.
- **Top third.** Does the summary carry a hard number and the strongest relevant fact
  first? "15+ years" is context, not proof — lead with proof.
- **Off-message bullets.** Cut bullets that argue for a different job than the one being
  applied to, even strong ones. A big sales number on an implementation resume pushes
  the reader toward the wrong conclusion.
- **Short stints and gaps.** Anything a skimmer will stumble on — if it can't be fixed
  (it's true), make sure the surrounding bullets are the strongest on the page.
- **Consistent date formats** across every role.

Apply the fixes, re-render, and re-check Step 6's page balance.

## Step 7 — (Optional) Cover letter
If the user wants one, write `applications/<company-slug>/cover-letter.json` (schema in
`build/render_cover_letter.py`): 3 short paragraphs — (1) the role + a genuine hook tied
to the company, (2) 2–3 specific, TRUE proof points mapped to their top needs, (3) a
confident close. Set the **same `"style"`** as the resume so the letterhead matches, then run
`python3 build/render_cover_letter.py applications/<company-slug>/cover-letter.json` and
keep it to one page.

## Step 8 — Write the match report
Write `applications/<company-slug>/match-report.md`:
- Role, company, link, date.
- **Fit Score** — paste the inline text meter at the very top, the number, band, and
  per-dimension breakdown from Step 4, and reference `fit.png` (the score meter image).
- **Keyword coverage**: must-haves matched vs. total, with the matched terms.
- **Top strengths** for this role; **Top gaps** (and what Josh could add).
- **Knockouts**: any work-auth/location/clearance/years items to confirm or that cap fit.
- **Metrics needed**: where a real number would strengthen a bullet. Recurring entries
  here are the signal to run `/excavate-profile` — a gap that shows up across several
  match reports is worth an interview, since fixing it in the profile fixes every
  future application at once.
- **Referral prompt**: if Josh may know someone at the company, say to pursue it
  (referrals beat cold applies by multiples).
- Output files produced (resume.pdf/.docx, cover-letter.\* if any).

## Step 9 — Ethics & guardrails (hard rules)
- **No fabrication** — only content traceable to `profile/master-profile.md`.
- **No keyword stuffing / white-text / hidden-text / prompt injection** — detectable,
  ineffective, and can blacklist (see playbook). Optimization = true terms in normal prose.
- **Surface gaps; don't paper over them.** An honest match report + Fit Score beats an
  inflated resume that fails a background check or interview.
- If asked to add a skill/metric/experience Josh lacks, refuse and offer to ask him for
  a real version.

---

After producing outputs, give the user a short summary: the **score meter** (show the
text meter and surface `fit.png`), the keyword-coverage number, **PAGES/balance result**,
and the top 1–2 gaps to close.
The PDF is the polished submission copy (real text, ATS-safe); the DOCX is the editable
version (ATS-preferred where a Word upload is requested).
