# Application Tracker

Live status of every application. One row per role. Maintained by `/track-applications`.

**Rule:** a row is created the moment an application folder is built, not when it is sent.
Drafted-but-never-sent is itself a finding, and hiding it makes the response rate look
better than it is.

---

## Active

| Company | Role | Fit | Built | Applied | Status | Last touch | Next action | Due |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Karbon | Implementation Specialist | 85 | 2026-08-06 | ? | `Unknown` | ? | Confirm whether submitted | 2026-08-09 |
| Nametag | GTM Operations Manager | 74 | 2026-07-20 | ? | `Unknown` | ? | Confirm whether submitted | 2026-08-09 |
| Superhuman | Group Manager, Growth & Website Content | 73 | 2026-06-18 | ? | `Unknown` | ? | Confirm; likely stale | 2026-08-09 |
| Monte Carlo | AI Marketing Operations Manager | 69 | 2026-07-20 | ? | `Unknown` | ? | Confirm whether submitted | 2026-08-09 |
| HR Transformed | Fractional CMGO | 64 | 2026-07-21 | ? | `Unknown` | ? | Confirm whether submitted | 2026-08-09 |
| Penta Group | Revenue Operations Manager | 60 | 2026-07-20 | ? | `Unknown` | ? | Confirm whether submitted | 2026-08-09 |
| DwyerOmega | Key Account Manager | 54 | 2026-06-18 | ? | `Unknown` | ? | Confirm; likely stale | 2026-08-09 |

> `sample-revops/` is a template, not a real application. Deliberately not tracked.

## Closed

*(none yet)*

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

Set `Next action` and `Due` from whichever rule fires first.

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

Run `/track-applications review` every Monday. It reports:

- Applications submitted last week, against target
- **Response rate** = any human reply / total applied
- **Screen rate** = screens / applied
- **Interview rate** = interviews / screens
- Median days to first response
- Stage histogram: where applications die
- Rows past due on their next action
- Drafted-but-never-sent count

## Strategy-change triggers

The point of measuring is knowing which thing to fix. Do not change more than one
variable at a time.

| Signal | Read | Change |
| :--- | :--- | :--- |
| < 10% response after 20 applied | Resume or positioning is not landing | Rework positioning, especially the Solenzo framing |
| Good response, dies at screen | Pitch or story problem, not paper | Rework the verbal narrative and the 2023 to 2024 answer |
| Dies after first interview | Role fit or depth | Re-check the fit scores being applied to |
| Strong response, low volume | The system works, throughput does not | Raise weekly application target |
| High volume, low fit scores | Applying too broadly | Raise the fit floor, currently no floor is set |

## Open question for Josh

Nothing in this repo records what was actually sent. Seven folders exist with no
submission status, so **response rate is currently uncomputable**. Filling in the
`Applied` and `Status` columns is the highest-value ten minutes available, because every
diagnosis above depends on it.
