# Change log — ATS accuracy revision

## Substantive changes

**1. Positioning and description.** Frontmatter `description` and the skill intro no
longer say "optimize it to pass modern ATS screening" or "ATS-optimized." They now say
"for reliable parsing, employer-configured screening, and clear recruiter review."
*Rationale:* an ATS is a configurable workflow and candidate database, not a universal
scoring gate; the old wording promised an outcome the skill cannot produce.

**2. New "What an applicant tracking system actually is" section.** States the
configurable-workflow model explicitly and names the three optimization targets: truthful
evidence, correct application answers, reliable parsing + clear human review. Defines
"ATS-friendly" narrowly (selectable text, conventional headings, normal content).
*Rationale:* installs the correct model up front so every downstream step inherits it.

**3. New mandatory Step 3 — Application-Form and Eligibility Check.** Runs after JD
parsing and before any resume content. Enumerates work authorization/sponsorship,
location and remote/hybrid/travel/start date, license/certification/clearance/degree/hard
years, and compensation/schedule/background-check screeners. Each item is classified
resume-evidenced / application-form / needs candidate confirmation, and the section states
that a well-written resume cannot repair an ineligible or inaccurate application response.
*Rationale:* the application form is where automated disposition actually happens; the old
skill treated eligibility only as a scoring modifier.

**4. Keyword guidance replaced with terminology rules.** Removed "mirror exact terms —
some ATS exact-match" and "honest keyword optimization." Added five rules: mirror the
employer's term when truthful, retain a clear synonym when it aids readability, use each
term naturally where warranted, never repeat to game a score, and require profile evidence
behind every competency. Added the discoverability note replacing "some ATS exact-match."
*Rationale:* removes the implication of a universal exact-match pass/fail mechanic while
keeping the real benefit — recruiter-search discoverability and reader clarity.

**5. Fit Score renamed Application Priority Score, and scoped.** Carries a first-mention
disclaimer that it is an internal, evidence-based decision aid and not a prediction of any
employer's ATS score, match category, or interview decision. The knockout cap is retained
at 25 but relabeled an "eligibility cap … a candidate time-allocation rule, not a system
behavior," with explicit guidance to stop or deprioritize unless the candidate can
truthfully resolve the item. Rubric, bands, `fit.json` schema, and the `score_meter.py`
call are unchanged. Also removed "+ referral" from the 60–79 band text and "chase a
referral" from 40–59.
*Rationale:* preserves a genuinely useful triage tool without letting it read as a
simulated employer score.

**6. Two-page rule deleted.** Removed the `PAGES=2` / `LAST_PAGE_FILL ≥ 0.6` iteration
loop and the "add real depth to fill page two" instruction. Replaced with: render for
readability and parse reliability, one or two pages based on substantiated content, never
pad. The renderer and its command are retained; `PAGES`/`LAST_PAGE_FILL` are now
diagnostics for "too long" and "near-empty trailing page" only.
*Rationale:* a page count has no bearing on parsing or screening, and the old rule
actively instructed padding.

**7. New parse/readability QA list (Step 7).** Checks selectable real text, conventional
explicit headings, clear chronology/dates/employers/titles, no information only in
graphics, readable hierarchy with no clipping and no near-empty trailing page, and no
artificial page target. Style note added: serif vs. sans-serif and accent color are
human-readability choices that do not affect ranking.
*Rationale:* replaces the page-fill target with checks that map to real failure modes.

**8. File-format guidance corrected (Step 8).** Blanket DOCX preference removed. Now:
follow the employer's upload instructions; absent instruction, submit a text-based PDF;
keep a matching DOCX for portals that request or favor Word; never a scanned, flattened,
or image-only PDF.
*Rationale:* the real failure mode is image-only text, not the container format.

**9. "Tired-recruiter read" renamed Recruiter Read Check.** Removed "4:45pm," "resume
#31," and "~10 seconds." Rewritten as six questions: top-third clarity, opening proof
point against a primary requirement, traceability of titles/employers/dates/scope/metrics
to the master profile, top bullets supporting the target role, unexplained stints/gaps/
pivots, and whether evidence reads without inferring unstated claims. The title-drift and
wrong-career-read guidance is preserved inside those questions.
*Rationale:* keeps the adversarial value, drops invented precision.

**10. Ethics section — consequences corrected.** Bans on fabrication, keyword stuffing,
white/hidden text, and prompt injection retained. "Can blacklist" deleted; replaced with:
these tactics add no credible evidence and can impair parsing, undermine credibility,
violate employer rules, or trigger manual scrutiny. Added a rule that parser-vs-readability
conflicts are solved with honest conventional formatting, never a hidden workaround.

**11. Referral guidance corrected.** "Referrals beat cold applies by multiples" deleted.
Now: suggest an informed referral only where a genuine, relevant connection exists; it may
increase the chance of human review but does not override eligibility requirements or
guarantee consideration; omit the section entirely when no real connection exists.

**12. Cover letter made conditional (Step 9).** Recommend only when requested, when a
short narrative solves a real concern or transition, or when it supplies specific company-
and role-relevant evidence. Explicitly not a universal lever. Schema, renderer call, and
one-page limit preserved.

**13. Truth and confirmation handling strengthened.** Added **candidate confirmation
needed** as a standard status ("potentially relevant, but not sufficiently documented to
claim") in the matching step, the competencies rule, the eligibility check, the match
report, and the guardrails. The match report now carries Gaps and Candidate confirmation
needed as separate sections.
*Rationale:* the two require different actions — one is a real absence, the other is a
question for the candidate — and merging them invites inference.

**14. Match report restructured (Step 10).** Adds the eligibility table at the top,
renames Fit Score to Application Priority Score with its disclaimer, renames "Keyword
coverage" to "Requirement coverage" (evidence named, not term counts), splits gaps from
confirmation items, and rewrites the referral prompt. Metrics-needed / `/excavate-profile`
loop preserved unchanged.

## Supporting files changed

**`ats-playbook.md` — rewritten.** It is read every run, so it carried most of the
inaccurate claims. Removed: the "75% auto-rejected" debunk and all other statistics,
vendor experiment results, named vendor matching products and their grade scales, the
`Management Science` and ResumeGo and Ladders citations, LinkedIn volume figures, the
hidden-text prevalence survey, the "blacklisting" outcome, the DOCX default, the Jobscan
75–80% match heuristic, the "referrals dwarf cold applications" claim, and the dangling
reference to a nonexistent `research/job-market-and-ats-research-2026.md`. Retained and
reorganized: the configurable-workflow model, the eight mechanical parsing rules,
corrected file-format guidance, terminology rules, prohibited tactics with corrected
consequences, verified-metrics-only quantification, front-loading, honest headline,
length-follows-substance, style-is-readability, and corrected referral/cover-letter
guidance.

**`build/render_resume.py` — verdict strings only.** The module docstring no longer calls
the output a "balanced 2-page resume," an "ATS-safe" PDF, or an "ATS-preferred" DOCX.
`main()` no longer emits "ONLY 1 PAGE — add depth" or "PAGE 2 SPARSE — add depth"; it now
flags only >2 pages (long, trim) and a near-empty trailing page (fill < 0.15), and
otherwise prints OK. `PAGES=` / `LAST_PAGE_FILL=` output format, the CLI, the JSON schema,
the two styles, and both output paths are unchanged.
*Rationale:* the renderer's own verdicts were instructing the padding the skill now
forbids.

**`build/requirements.txt` — comments only.** "ATS-preferred submission format" →
"for portals that request or favor Word"; "balance check" → "page/readability QA."

## Explicitly preserved

`profile/master-profile.md` as sole source of fact; the `Writing Standards` block and its
banned constructions; **Verified Quantified Metrics** as the only usable numbers, read
fresh each run, with scope respected; the `/excavate-profile` feedback loop; the
`applications/<company-slug>/` convention and all filenames (`resume.json`, `fit.json`,
`fit.png`, `match-report.md`, `cover-letter.json`); all three renderer commands and their
schemas; the `modern`/`classic` styles and the style-in-JSON-or-2nd-arg override; the
summary-variant and honest-headline rules; the `PAGES=?` fallback; and the
refuse-and-offer-to-ask response to a request for content the profile doesn't support.

## QA checklist — claims the revised skill must not make

Run against `SKILL.md`, `ats-playbook.md`, and the renderer strings.

| # | Claim that must be absent | Verify by |
| :-- | :--- | :--- |
| 1 | A universal ATS scoring formula exists — that a resume can "pass" or "beat" an ATS, or that any technique produces a score or ranking. | Search: `pass`, `beat`, `ATS score`, `ranking`, `optimized`. Only permitted hits are the prohibitions themselves ("don't imply a technique 'passes' or 'beats' an ATS") and "ATS-friendly" used strictly for selectable text + conventional headings + readable content. |
| 2 | A two-page resume, or a filled second page, improves ATS performance. | Search: `2 page`, `two-page`, `LAST_PAGE_FILL`, `fill`, `pad`. No page or fill target may appear as a requirement; every hit must be a diagnostic or an anti-padding rule. Confirm `render_resume.py` no longer prints "add depth." |
| 3 | DOCX is universally preferred over PDF. | Search: `docx`, `Word`, `preferred`. Format guidance must lead with the employer's instructions and default to a text-based PDF; DOCX appears only as the Word-portal fallback. Includes `requirements.txt` comments. |
| 4 | Exact keyword density or match percentage guarantees screening success. | Search: `exact`, `density`, `match %`, `keyword`, `stuff`. No percentage target, no exact-match mechanic, no repetition tactic. The discoverability paragraph must be present in both files. |
| 5 | Referrals beat cold applications by a stated multiple. | Search: `referral`, `refer`. Must be conditioned on a genuine, relevant connection, and must state it does not override eligibility or guarantee consideration. No multiple, fold, or percentage. Confirm the Priority Score bands no longer prescribe chasing a referral. |
| 6 | Hidden text automatically causes blacklisting. | Search: `blacklist`, `hidden`, `white text`, `reject`. The ban stays; the consequence must read "add no credible evidence and can impair parsing, undermine credibility, violate employer rules, or trigger manual scrutiny." |
| 7 | *(additional)* Any invented statistic, study, vendor claim, or algorithm description. | Search for digits followed by `%`, and for `study`, `survey`, `research`, vendor names. None should remain in either skill file. |
| 8 | *(additional)* Any factual claim about the candidate not traceable to `profile/master-profile.md`. | The skill must route every undocumented item to **candidate confirmation needed** rather than inferring it. |
