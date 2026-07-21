# portable/

A **standalone, LLM-agnostic** version of this toolkit for anyone else to use —
no Claude Code, no Python, no this-repo dependencies.

## `job-search-kit.md`

One self-contained file that turns any capable LLM (Claude, ChatGPT, Gemini,
Copilot, …) into a personal job-search assistant. Give it to another person and
they can:

1. **Upload / paste their resume(s)** — Phase 1 intake.
2. **Answer profile-building questions** — Phase 2 interview.
3. **See what roles they're qualified for** — Phase 4 role fit + Fit Score.
4. **Build a tailored resume per role** — Phase 5, from a pasted job description.

### How they use it
1. Open a fresh chat in any strong LLM.
2. Paste the **entire** `job-search-kit.md` file as the first message.
3. Add: *"I want to run the Job-Search Kit. Let's start with Phase 1."*
4. Follow the prompts. Save the **Master Profile** it produces and paste it back
   to start any future session without re-interviewing.

### What it carries over from the full toolkit
- The **truthful-tailoring** principle — never fabricates experience.
- The **Fit Score rubric** (0–100, five dimensions, knockout cap at 25).
- The **ATS & formatting playbook** (single-column, standard headings, real
  numbers only, no hidden-text tricks).
- The **Master Profile schema** — same structure as `profile/master-profile.md`,
  so a profile built here also drops into the Claude Code skills in this repo.

### What it deliberately drops (vs. the Claude Code version)
- No Python renderers — outputs are clean single-column text to paste into
  Google Docs / Word and export to PDF/DOCX yourself.
- No live role-search script — the person uses their LLM's own web-search/
  browsing mode to find postings, then brings a job description back for Phase 5.
