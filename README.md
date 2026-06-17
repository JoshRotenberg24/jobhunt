# jobhunt

A job-search toolkit that runs **inside Claude Code** — no separate app, no terminal
program to maintain. You open this repo in any Claude Code session (web, desktop, or
CLI), drop in a job-posting link, and the tool tailors Josh's resume and optimizes it
to pass modern ATS screening.

## How to use it

In a Claude Code session opened on this repo:

```
/tailor-resume <job-posting-url>
```

…or paste the job description text after the command. The skill will:

1. Fetch/parse the job description (title, must-haves, knockout criteria, keywords).
2. Match those requirements against your **master profile** — using only true content.
3. Assemble an **ATS-safe, tailored resume** (`applications/<company>/resume.md`).
4. Produce a **match report** (`applications/<company>/match-report.md`): keyword
   coverage, honest gaps, knockout flags, metrics to supply, and a fit verdict.

> Many career sites (Greenhouse/Lever/Workday/LinkedIn) block automated fetching. If a
> URL won't load, the skill will ask you to paste the job description text.

## What's in here

| Path | What it is |
| :--- | :--- |
| `.claude/skills/tailor-resume/SKILL.md` | The tool — the workflow Claude follows. |
| `.claude/skills/tailor-resume/ats-playbook.md` | Evidence-based ATS/formatting ruleset. |
| `profile/master-profile.md` | **Single source of truth** — bullets, roles, metrics, skills. Edit this as your career evolves. |
| `research/job-market-and-ats-research-2026.md` | The cited research that informs the playbook (with confidence levels + a verification pass). |
| `applications/<company>/` | Generated, tailored resumes + match reports per job. |

## Operating principle: truthful tailoring

The tool **never fabricates** experience, employers, dates, metrics, or skills.
Tailoring means selecting, reordering, and rephrasing **real** content to mirror a
specific job — and honestly surfacing gaps rather than papering over them. No
keyword-stuffing, white-text, or hidden prompt-injection (all detectable, ineffective,
and disqualifying — see the playbook).

## Roadmap ideas (not yet built)
- A cover-letter sub-skill seeded from the match report.
- `.docx` export (single-column) via pandoc.
- Pull/sync the profile from Google Drive.
- A lightweight application tracker (status per `applications/<company>/`).
