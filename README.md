# jobhunt

A job-search toolkit that runs **inside Claude Code** — no separate app, no terminal
program to babysit. You open this repo in a Claude Code session (web, desktop, or CLI),
drop in a job-posting link, and the tool scores your fit, tailors your resume, and
produces a polished, balanced 2-page resume + cover letter optimized to pass modern ATS.

## How to use it

In a Claude Code session opened on this repo:

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

## What's in here

| Path | What it is |
| :--- | :--- |
| `.claude/skills/tailor-resume/SKILL.md` | The tool — the workflow Claude follows. |
| `.claude/skills/tailor-resume/ats-playbook.md` | Evidence-based ATS/formatting ruleset. |
| `profile/master-profile.md` | **Single source of truth** — bullets, roles, verified metrics, skills. Edit as your career evolves. |
| `build/render_resume.py` | Resume JSON → polished PDF + DOCX; reports pages + balance. |
| `build/render_cover_letter.py` | Cover-letter JSON → one-page PDF + DOCX. |
| `build/score_meter.py` | Fit JSON → score-meter gauge PNG + inline text meter. |
| `research/job-market-and-ats-research-2026.md` | Cited research behind the playbook (with confidence levels + verification pass). |
| `applications/<company>/` | Generated resume, cover letter, and match report per job. |

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
- A lightweight application tracker across `applications/<company>/`.
- Optional font embedding (e.g., Carlito) for closer DOCX/PDF visual parity.
