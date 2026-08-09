# Application Tracker

Live status of every application. One row per role. Maintained by `/track-applications`.

**Rule:** a row is created the moment an application folder is built, not when it is sent.
Drafted-but-never-sent is itself a finding, and hiding it makes the response rate look
better than it is.

*Last updated: 2026-08-09, from Josh's inbox confirmations.*

---

## Active

| Company | Role | Fit | Applied | Days | Status | Response | Next action | Due |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Karbon | Implementation Specialist | 85 | 2026-08-05 | 4 | `Applied` | none | Follow-up #1 | 2026-08-12 |
| Nametag | GTM Operations Manager | 74 | 2026-07-20 | 20 | `Applied` | none | Final follow-up, then close | 2026-08-10 |
| Monte Carlo | AI Marketing Operations Manager | 69 | 2026-07-20 | 20 | `Applied` | none | Final follow-up, then close | 2026-08-10 |
| HR Transformed | Fractional CMGO | 64 | 2026-07-21 | 19 | `Applied` | none | Final follow-up, then close | 2026-08-11 |

## Closed

| Company | Role | Fit | Applied | Status | Died at | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Penta Group | Revenue Operations Manager | 60 | 2026-07-20 | `Rejected` | Application review | Declined 2026-07-30, 10 days after applying. No reason given. |
| Superhuman | Group Manager, Growth & Website Content | 73 | 2026-06-17 | `Ghosted` | Application review | 53 days silent. Past every threshold. |
| DwyerOmega | Key Account Manager | 54 | never | `Withdrawn` | Not submitted | Josh judged it not a fit. Correct call, it was the lowest fit score built. |

> `sample-revops/` is a template, not a real application. Deliberately not tracked.

---

## Funnel (as of 2026-08-09)

```
Applications built:        7
Applications submitted:    6        (DwyerOmega built, never sent)
Search window:            Jun 17 to Aug 9  (7.7 weeks)
Submission rate:           0.8 / week

Human responses:           1 / 6     (17%)  — all rejections
Screens:                   0 / 6     (0%)
Interviews:                0
Median days to response:   10        (n = 1, not meaningful)

Still open:                4         (3 of them at day 19 to 20)
Ghosted:                   1
Rejected:                  1
```

**Sample size is 6. That is too small to diagnose positioning.** Per
`.claude/skills/track-applications/SKILL.md`, under 20 applications the recommendation is
volume, not a rewrite.

## Diagnosis

**The binding constraint is throughput, not evidence.**

Six applications across nearly eight weeks is under one per week. At any realistic
response rate, six submissions produce roughly one conversation, and one rejection is
about what the model predicts. Nothing in this data says the resume is broken. There is
not enough data to say anything about the resume at all.

Three of the four open applications hit day 21 within 48 hours. Without a follow-up they
convert to ghosted and the active pipeline drops to one.

**One recommendation: raise submission volume to 5 per week and re-review at 20 sent.**
At that rate the sample reaches diagnostic size in under three weeks. Changing the resume
now would mean changing the input and the volume at the same time and learning nothing
from either.

## Open question

Karbon was submitted via Indeed on **Aug 5**; the tailored resume folder was built
**Aug 6**. Superhuman shows the same one-day pattern (applied Jun 17, folder Jun 18).
Worth confirming whether the tailored resume was actually the document submitted, or
whether these went out on the generic resume with the tailoring done afterward. If the
latter, the pipeline is measuring something that was never sent.

---

## Status values

| Value | Meaning |
| :--- | :--- |
| `Drafted` | Folder built, not submitted |
| `Applied` | Submitted, no human response yet |
| `Screen` | Recruiter screen scheduled or done |
| `Interview` | Hiring manager or panel round |
| `Final` | Final round or reference stage |
| `Offer` | Offer extended |
| `Rejected` | Explicit no |
| `Ghosted` | 21+ days silent after final follow-up |
| `Withdrawn` | Josh pulled out |
| `Archived` | Closed with no further action |

## Follow-up triggers

| Trigger | Action | Timing |
| :--- | :--- | :--- |
| Applied, silent | Follow-up #1 | 5 business days |
| Follow-up #1, silent | Follow-up #2 (final) | 12 business days from apply |
| Follow-up #2, silent | Mark `Ghosted`, move to Closed | 21 calendar days from apply |
| Any interview completed | Thank-you note | Within 24 hours |
| Post-interview, silent | Follow-up | 7 calendar days |
| Final round, silent | Follow-up | 5 calendar days |
| Final round, still silent | Close-the-loop message | 14 calendar days |

Generate the message with `/follow-up <company>`.

## Weekly review

Run `/track-applications review` every Monday.

## Strategy-change triggers

Do not change more than one variable at a time.

| Signal | Read | Change |
| :--- | :--- | :--- |
| < 10% response after 20 applied | Resume or positioning is not landing | Rework positioning, especially the Solenzo framing |
| Good response, dies at screen | Pitch or story problem, not paper | Rework the verbal narrative and the 2023 to 2024 answer |
| Dies after first interview | Role fit or depth | Re-check the fit scores being applied to |
| Strong response, low volume | The system works, throughput does not | Raise weekly application target |
| High volume, low fit scores | Applying too broadly | Raise the fit floor, currently no floor is set |

**Currently firing: low volume.** 0.8 submissions/week against a 5/week target.
