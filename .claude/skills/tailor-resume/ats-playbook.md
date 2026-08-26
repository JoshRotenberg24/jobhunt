# Parsing, Screening & Recruiter-Review Playbook

Operational ruleset for the `tailor-resume` skill. Rules here are mechanical (about how
documents parse and how people read) or procedural (about how applications are screened).
Nothing here predicts an employer's scoring output, and no rule should be presented to
the candidate as a guarantee.

## Mental model: what an ATS is

An ATS is a configurable hiring workflow and candidate database. Depending on the
employer and the job, it may:

- parse the resume into structured fields (contact, employers, titles, dates, skills);
- make the candidate searchable by recruiters;
- apply application-question filters or disqualification rules;
- score questionnaire responses;
- provide AI-assisted matching or ranking.

Which of these are active is an employer configuration choice, and varies by system, by
company, and often by requisition. Recruiters and hiring managers frequently retain the
actual advance/reject decision.

Consequences for this skill:

- There is **no universal scoring formula** to optimize against. Don't describe one, and
  don't imply a technique "passes" or "beats" an ATS.
- The most reliably automated gate is the **application form**: work authorization,
  location, license/clearance, minimum years, compensation, availability. A
  disqualifying answer can route an application out with no human review. These answers
  must be accurate, and they must come from the candidate.
- Everything the resume itself does breaks down into two jobs: **parse cleanly** and
  **be immediately clear to a human reviewer**.

"ATS-friendly" means only this: selectable text, conventional headings, normal readable
content.

## Parsing rules (mechanical)

1. **Single-column layout.** Multi-column layouts and text boxes can be read out of
   order, disconnecting titles from the descriptions under them.
2. **No tables for content.** Table-cell extraction is unreliable across parsers.
3. **No information carried only in images, icons, logos, charts, or photos.** Graphics
   are dropped or extracted as noise. If it matters, it must exist as text.
4. **Nothing critical in headers/footers.** Some parsers skip them. Name and contact go
   in the body.
5. **Conventional, explicit section headings** — "Experience," "Education," "Skills."
   Clever headings ("Where I've Made an Impact") give the parser nothing to map onto and
   slow a human reader down.
6. **Standard, readable fonts.** No decorative typefaces.
7. **Reverse-chronological structure**, with consistent, unambiguous date formats.
8. **Real, selectable text.** The one true document-level failure mode is a scanned,
   flattened, or image-only file, where no text exists to extract. Test: select and copy
   the text. If you can't, neither can the system.

## File format

Follow the employer's upload instructions and portal guidance. If there is no
instruction, submit a text-based PDF that preserves selectable text and clean formatting.
Keep a matching DOCX version for portals that request or clearly favor Word. Never use a
scanned, flattened, or image-only PDF.

`build/render_resume.py` emits both from the same JSON, so the two stay identical in
content.

## Terminology and discoverability

- Mirror the employer's preferred term where it truthfully describes the candidate's
  work.
- Retain a clear, widely understood synonym when it improves human readability or
  describes the work more precisely.
- Use each relevant term naturally where it's warranted — headline, summary, an
  experience or project bullet, or the skills evidence.
- Do not repeat a term solely to manipulate a presumed score.
- Every material skill in a Core Competencies section must be supported by evidence
  elsewhere in the master profile, or flagged as *candidate confirmation needed* and left
  off.

> Literal terms can help discoverability in recruiter searches and some matching
> configurations. Other systems recognize related terms or apply employer-defined
> criteria. Use accurate terminology for clarity, not keyword density.

## Prohibited tactics

Never use white or hidden text, off-screen text, font-color tricks, invisible keyword
blocks, or prompt-injection instructions aimed at an AI reviewer. Parsers extract raw
text regardless of color, and a reviewer sees it with a select-all.

> These tactics add no credible evidence and can impair parsing, undermine credibility,
> violate employer rules, or trigger manual scrutiny.

The same applies to fabricated titles, dates, credentials, and metrics — including
"tailoring" a past title toward the target role.

## Content quality

- **Quantify with real numbers only.** The only usable numbers are those under **Verified
  Quantified Metrics** in the master profile — read that section fresh each run, since it
  grows as `/excavate-profile` adds to it. Respect each metric's stated scope. Where no
  verified number exists, use a concrete qualitative outcome and flag the gap.
- **Front-load relevance.** A reviewer's first pass is a skim. The bullets that evidence
  this job's primary requirements go first, in every role.
- **Honest headline.** Lead with a self-descriptive professional headline aligned to the
  target role. Never restate a past title as something it wasn't.
- **Length follows substance.** Use one or two pages based on the quantity of relevant,
  substantiated experience. Never add weaker, irrelevant, or padded content to reach a
  page target, and never claim a page count affects screening.
- **Style is a readability choice.** Serif vs. sans-serif, accent color, and page count
  do not change how a system ranks a resume. Pick what reads well for the field.

## Referrals and cover letters

- **Referrals:** if the candidate has a genuine, relevant connection, suggest an informed
  referral or introduction. It may increase the chance of human review, but it does not
  override eligibility requirements or guarantee consideration. Don't manufacture a
  connection that isn't there.
- **Cover letters** are optional. Recommend one when the employer requests it, when a
  short narrative solves a real concern or transition, or when it can supply specific
  company- and role-relevant evidence the resume can't carry. It is not a universal lever
  on any screening system.

## Voice

Keep the candidate's real voice, specifics, and verified metrics. Generic, interchangeable
phrasing reads as unconsidered to a human reviewer regardless of how it parses.
