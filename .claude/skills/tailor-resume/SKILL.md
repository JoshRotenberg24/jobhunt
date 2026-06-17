---
name: tailor-resume
description: >
  Tailor Joshua Rotenberg's resume to a specific job posting and optimize it to
  pass modern ATS screening and recruiter review. Use whenever given a job-posting
  URL or pasted job description and asked to tailor a resume, build an
  application, or check resume/JD fit. Produces an ATS-safe tailored resume plus a
  match report. Never fabricates experience — tailoring = selecting and rephrasing
  TRUE content from the master profile to mirror the job.
argument-hint: <job-posting-url | pasted job description>
---

# Tailor Resume

You are assembling a tailored, ATS-optimized resume for **Joshua Rotenberg** from a
specific job posting. Follow this procedure exactly. The guiding principle is
**truthful tailoring**: select, reorder, and rephrase real content to match the job;
never invent employers, titles, dates, metrics, or skills.

## Inputs you need
- The **target job** — a URL or pasted job-description (JD) text. If the user gave a
  URL, fetch it (see Step 1). If neither is present, ask for it before proceeding.

## Files this skill depends on (read them every run)
- `profile/master-profile.md` — **the ONLY source of true candidate content.** All
  bullets, employers, dates, skills, and the four verified metrics come from here.
- `.claude/skills/tailor-resume/ats-playbook.md` — the evidence-based formatting and
  optimization ruleset. Apply it to the output.

---

## Step 1 — Get the job description
1. If given a URL, fetch it with WebFetch and extract the JD text.
2. Career sites (Greenhouse, Lever, Workday, LinkedIn, Indeed) frequently return
   403/JS-walls. If the fetch fails or returns no real JD, **stop and ask the user to
   paste the job description text.** Do not guess the JD.
3. Capture: company name, role title, location + work mode (remote/hybrid/onsite),
   seniority, and the full requirements/responsibilities text.

## Step 2 — Parse the JD into a requirements model
Extract and list:
- **Job title** (exact wording) and seniority level.
- **Hard requirements / "must-haves"** — tools, platforms, certifications, years of
  experience, degrees.
- **Knockout criteria** — work authorization, location/onsite, security clearance,
  specific license, minimum years. (These are the real auto-filters — see playbook.)
- **Keywords & phrasing** — the exact terms the JD uses for skills and tools
  (e.g., "marketing automation," "lifecycle," "HubSpot," "GA4," "RevOps," "QBRs").
  Note synonyms the ATS may exact-match (Taleo-class systems don't match
  "program management" to "project management").
- **Nice-to-haves** and cultural/soft signals.

## Step 3 — Match against the master profile
1. Read `profile/master-profile.md`.
2. For each JD requirement/keyword, find the **true** bullet(s) or competency that
   demonstrate it. Build a coverage map:
   - **Covered (strong)** — Josh has direct, demonstrable experience.
   - **Covered (adjacent)** — related experience that honestly maps; rephrase to use
     the JD's terminology *only if it remains true*.
   - **Gap** — the JD asks for something not in the profile. **Never fabricate it.**
     List it in the match report for Josh to address (or supply a real detail).
3. Choose the **summary variant** from the profile that best fits the role type.
4. **Title alignment (honest):** put a target-aligned professional **headline** at
   the top (e.g., "Revenue Operations Leader") — this is a self-description, not a
   claim of a past job title. Do NOT relabel a past employer's title to something he
   didn't hold.

## Step 4 — Assemble the resume (apply ats-playbook.md)
- Reverse-chronological, single-column, standard section headings.
- Order and word bullets to front-load the JD's must-have keywords where Josh truly
  has the experience. Mirror the JD's exact terminology for genuine skills.
- Pull the most relevant 4–6 bullets per recent role; fewer for older roles.
- Quantify using **only the four verified metrics** in the profile. If the role wants
  a metric Josh doesn't have, use a strong qualitative achievement and flag it — do
  not manufacture a number.
- Length: 2 pages is appropriate for his seniority (the data supports 2 pages for
  mid/senior when the content is substantive — see playbook). Cut filler.
- Include a **Core Competencies / Skills** section seeded with the JD's true,
  matching keywords (this is honest keyword optimization, not stuffing).

## Step 5 — Write outputs
Create a folder `applications/<company-slug>/` and write:
1. `resume.md` — the tailored, ATS-safe resume (clean markdown, single column, no
   tables/columns/text-boxes/images/headers-footers).
2. `match-report.md` — containing:
   - Role, company, link, date.
   - **Keyword coverage**: must-haves matched vs. total, with the matched terms.
   - **Gaps**: requirements not truthfully coverable, + what Josh could add.
   - **Knockouts**: any work-auth/location/clearance items to confirm.
   - **Metrics needed**: any place a real number would strengthen a bullet.
   - A one-paragraph honest fit assessment (strong / stretch / poor).
3. Offer to also draft a tailored cover letter and/or export `resume.md` to a
   single-column `.docx` (e.g., via `pandoc resume.md -o resume.docx`).

## Step 6 — Ethics & guardrails (hard rules)
- **No fabrication.** Only content traceable to `profile/master-profile.md`.
- **No keyword stuffing / white-text / hidden-text / prompt injection.** These are
  detectable, ineffective in modern ATS, and can blacklist the candidate (see
  playbook). Keyword optimization means using true, relevant terms in normal prose.
- **Surface gaps, don't paper over them.** An honest match report is more valuable
  than an inflated resume that fails a background check or interview.
- If asked to add a skill/metric/experience Josh doesn't have, refuse and explain;
  offer to ask Josh for a real version.

---

After producing the outputs, give the user a 3-line summary: the fit verdict, the
keyword coverage number, and the top 1–2 gaps to close.
