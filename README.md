# jobhunt

A job-search toolkit that runs **inside Claude Code** — no separate app, no terminal
program to babysit. You open this repo in a Claude Code session (web, desktop, or CLI),
drop in a job-posting link, and the tool scores your fit, tailors your resume, and
produces a polished, balanced 2-page resume + cover letter optimized to pass modern ATS.

## How to use it

In a Claude Code session opened on this repo:

### Find roles to apply to

```
/find-roles                       # default targets (remote US + Colorado), full-time + contract
/find-roles remote HubSpot ops    # …or pass filters: titles, location, comp, stage, tool
/find-roles fractional contract   # …or narrow to part-time / contract / fractional work
```

The `find-roles` skill reads your master profile for target role types, seniority, and
location, then uses **live web search** to surface currently-open postings. By default it
covers both **full-time roles and part-time / contract / fractional** work (each result is
labeled by type). It runs a quick Fit read + knockout scan on each and saves a **ranked
shortlist** to `searches/<date>.md` — best fit first, knockouts separated out — with a
`/tailor-resume <url>` next-step for each. Pass filters to narrow the search.

### Tailor a resume for a specific posting

```
/tailor-resume <job-posting-url>
```

…or paste the job description after the command. The skill will:

1. **Parse the job** — title, must-haves, knockout criteria, keywords.
2. **Score your fit** — a transparent **Fit Score (0–100)** for how strong a candidate you
   are for *this* role (separate from the resume's keyword match), shown as a visual
   **score meter** (gauge + per-dimension breakdown bars) and an inline text meter, with
   any knockout flags.
3. **Tailor the resume** — match the JD against your master profile using only true
   content, then build it.
4. **Render it professionally** — a balanced **2-page PDF** (polished, real text, ATS-safe)
   plus an editable **DOCX**, enforcing that page 2 is full (no half-empty page).
5. **Cover letter (optional)** — a one-page letter matching the resume letterhead.
6. **Match report** — Fit Score, keyword coverage, strengths, honest gaps, knockouts,
   and a referral prompt.

Outputs land in `applications/<company>/`. See `applications/sample-revops/` for a
worked example (resume PDF/DOCX, cover letter, and match report).

> Many career sites (Greenhouse/Lever/Workday/LinkedIn) block automated fetching. If a
> URL won't load, the skill will ask you to paste the job description text.

### Track what you sent, and chase it

```
/track-applications              # what's due today, what's overdue
/track-applications review       # Monday funnel numbers + one recommendation
/track-applications applied karbon
/follow-up karbon                # writes the message the tracker says is due
```

A job hunt is a funnel, and an untracked funnel can't be diagnosed. The tracker records
what was actually sent and what came back, then computes response rate, screen rate, and
where applications die. When the funnel underperforms it names **one** variable to
change, because changing three at once teaches you nothing.

`/follow-up` writes the message for each trigger (5 days silent, post-interview,
final round quiet, graceful close). Every message is under 100 words and carries one new
piece of value, never a bare status request.

## What's in here

| Path | What it is |
| :--- | :--- |
| `.claude/skills/find-roles/SKILL.md` | Role-search tool — web-searches live openings that fit the profile and writes a ranked shortlist. |
| `.claude/skills/tailor-resume/SKILL.md` | The tool — the workflow Claude follows. |
| `searches/<date>.md` | Ranked role-search shortlists produced by `/find-roles`. |
| `.claude/skills/tailor-resume/ats-playbook.md` | Evidence-based ATS/formatting ruleset. |
| `profile/master-profile.md` | **Single source of truth** — bullets, roles, verified metrics, skills. Edit as your career evolves. |
| `build/render_resume.py` | Resume JSON → polished PDF + DOCX; reports pages + balance. Two styles: `modern` (sans + navy) or `classic` (serif, black) per role. Also writes recruiter-facing `Joshua_Rotenberg_<Role>.pdf/.docx` copies — upload those, not `resume.pdf`. |
| `build/render_cover_letter.py` | Cover-letter JSON → one-page PDF + DOCX. |
| `build/score_meter.py` | Fit JSON → score-meter gauge PNG + inline text meter. |
| `research/job-market-and-ats-research-2026.md` | Cited research behind the playbook (with confidence levels + verification pass). |
| `applications/<company>/` | Generated resume, cover letter, and match report per job. |
| `applications/tracker.md` | **Live pipeline** — status, dates, follow-up triggers, funnel metrics, strategy-change signals. |
| `.claude/skills/track-applications/SKILL.md` | Tracker maintenance and the weekly funnel review. |
| `.claude/skills/follow-up/SKILL.md` | Follow-up, thank-you, and close-the-loop messages. |

## Setup

The renderers need three Python packages. In **Claude Code on the web**, a `SessionStart`
hook (`.claude/hooks/session-start.sh`) installs them automatically each session — no
action needed. Anywhere else (or to reinstall), run:

```
pip install -r build/requirements.txt
```

- `python-docx` — native Word output (ATS-preferred submission format)
- `reportlab` — polished, text-based PDF with exact pagination (the balance check)
- `pymupdf` — optional; lets the tool rasterize a PDF to preview/verify the layout

No LibreOffice/Chromium needed. PDF and DOCX are generated purely in Python.

## Operating principle: truthful tailoring

The tool **never fabricates** experience, employers, dates, metrics, or skills. Tailoring
means selecting, reordering, and rephrasing **real** content to mirror a specific job —
and honestly surfacing gaps (and an honest Fit Score) rather than papering over them. No
keyword-stuffing, white-text, or hidden prompt-injection (all detectable, ineffective,
and disqualifying — see the playbook).

## Roadmap ideas (not yet built)
- Pull/sync the profile from Google Drive.
- A lightweight application tracker across `applications/<company>/` (status: found →
  applied → interview), tying `searches/` results to `applications/` outputs.
- Optional font embedding (e.g., Carlito) for closer DOCX/PDF visual parity.
