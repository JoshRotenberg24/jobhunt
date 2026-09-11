# jobhunt — project rules

Josh Rotenberg's job search command center. Every session working in this repo should
follow this file. It exists because early sessions defaulted to gatekeeping ("you're not
qualified, skipping") when the actual job is to build the strongest honest application
and let Josh decide whether to send it.

## The core rule

**Build the tailored resume by default. Score and gaps are decision-support, not a gate.**

For every job posting Josh pastes or links:

1. Run the fit evaluation (`/tailor-resume` skill — eligibility check, Application
   Priority Score, requirement coverage, gaps).
2. Build the tailored resume (and cover letter if it earns its place) **regardless of
   the score**, unless step 3 applies.
3. The only time to hold off building and ask first: a **genuine, stated hard blocker**
   Josh has already confirmed he fails, a required license/badge/credential he doesn't
   hold, a residency requirement he doesn't meet, a language requirement he doesn't
   speak. Even then, ask, don't just decide for him. "Long shot" or "overqualified" or
   "big scope gap" are information to hand him, never a reason to withhold the resume.
4. Always say the honest score, band, and top gaps plainly. Don't inflate. Don't soften
   a real problem. But don't let a low score substitute for his decision.

If Josh says "skip," that's his call for that one posting, not a pattern to infer going
forward. Never pre-filter postings on his behalf.

## Where things live

- `profile/master-profile.md` — the only source of true candidate content. Read it fresh
  every run (metrics and confirmed facts get added over time via `/excavate-profile` and
  in-session confirmations). Never invent employers, titles, dates, metrics, or skills
  not in this file.
- `applications/<company-slug>/` — one folder per posting: `fit.json` + `fit.png` (score
  meter), `match-report.md`, the resume/cover-letter source JSON, and rendered
  `.pdf`/`.docx`.
- `build/` — the renderers (`render_resume.py`, `render_cover_letter.py`,
  `score_meter.py`). Don't hand-format resumes outside this pipeline.

## File naming

Every resume and cover letter file gets the job name in the filename, no generic
`resume.pdf` as the only deliverable. Pattern: `<Company>-<RoleShort>-Resume.pdf` /
`-CoverLetter.pdf` (and matching `.docx`). Employers with multiple postings evaluated
here (e.g. micro1) use a labeled copy like `Rotenberg Resume - micro1 - <Role>.pdf`
alongside the working `resume.json`/`.pdf` — match whichever convention the company's
existing folder already uses for consistency within that employer.

## Interview prep

When Josh has an interview lined up (or asks to prep for one), write
`applications/<company-slug>/<company>-interview-prep.md` (or a shared doc across
multiple roles at the same company, see `applications/micro1-interview-prep.md` for the
pattern). Ground every talking point in real profile evidence — same no-fabrication rule
as the resume. Lead with the closest literal match to what the interviewer will actually
ask about.

## Git

Commit and push after every application folder is created or updated — the stop-hook
checks for untracked files, and Josh expects the repo to reflect the current state of
his search without being asked. Use plain, descriptive commit messages naming the
company/role and the outcome (score, built vs. skipped, profile updates included).

## Master profile updates

When a session surfaces a new confirmed fact about Josh (a past role's real industry, a
credential he does or doesn't hold, a metric he supplies), add it to
`profile/master-profile.md` in the same pass, not just the one match report. That's what
makes the gap fix itself for every future application instead of getting re-asked.
