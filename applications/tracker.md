# Application Tracker

Live status of every application. Maintained by `/track-applications`.

**Scope correction (2026-08-09):** this file previously tracked only the 7 roles with
built folders in `applications/`. Josh's inbox shows **50+ applications** ("1–50 of many"
on a `thank you for applying` search) and several live interview threads. The repo was
measuring roughly 14% of the actual search. Everything below is being rebuilt from inbox
evidence; rows marked `?` are awaiting Josh.

---

## 🔥 Live conversations (highest priority)

These are in flight right now and none of them were tracked. This is where the search
actually is.

| Company / Thread | Stage | Last event | Days | Next action | Due |
| :--- | :--- | :--- | :--- | :--- | :--- |
| LeahV (company `?`) | **First round interview** | Zoom, 2026-08-05 | 4 | Thank-you sent? If not, send today. Follow-up if silent. | 2026-08-12 |
| micro1 (role `?`) | **AI interview complete** | 2026-08-07 | 2 | Confirm what happens next, who reviews it | 2026-08-11 |
| Infinite Music | **Hiring manager contact** | Msg from Tyrese Johnson, Head of Marketing, 2026-08-05 | 4 | Replied? If not, reply today | 2026-08-09 |
| Horizon Organic Dairy | **Active thread** | Josh replied 2026-08-05 | 4 | Awaiting their response, follow up at 7 days | 2026-08-12 |

## Applied, awaiting response

| Company | Role | Fit | Applied | Days | Next action | Due |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Karbon | Implementation Specialist | 85 | 2026-08-05 | 4 | Follow-up #1 | 2026-08-12 |
| RoadRunner Recycling | ? | — | 2026-08-05 | 4 | Follow-up #1 | 2026-08-12 |
| ServiceNow | ? | — | 2026-08-05 | 4 | Follow-up #1 | 2026-08-12 |
| Community Phone | ? | — | 2026-08-03 | 6 | Follow-up #1 | 2026-08-10 |
| Kraken | ? | — | 2026-07-24 | 16 | Final follow-up | 2026-08-10 |
| Ramp | Accounting/? | — | 2026-07-24 | 16 | Final follow-up | 2026-08-10 |
| DoorDash | Platform/? | — | 2026-07-23 | 17 | Final follow-up | 2026-08-10 |
| AccuSourceHR | ? | — | 2026-07-21 | 19 | Final follow-up, then close | 2026-08-11 |
| HR Transformed | Fractional CMGO | 64 | 2026-07-21 | 19 | Final follow-up, then close | 2026-08-11 |
| Nametag | GTM Operations Manager | 74 | 2026-07-20 | 20 | Final follow-up, then close | 2026-08-10 |
| Monte Carlo | AI Marketing Ops Manager | 69 | 2026-07-20 | 20 | Final follow-up, then close | 2026-08-10 |
| ServiceNow | ? (2nd application) | — | 2026-07-08 | 32 | Close as ghosted | 2026-08-09 |

> **Incomplete.** Only the first ~10 inbox results were visible. At 50+ total there are
> roughly 35 applications still unrecorded. See *Open data gaps*.

## Closed

| Company | Role | Applied | Status | Died at | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Parachute Health | ? | 2026-08-03 | `Rejected` | Application review | Declined 2026-08-08, 5 days after applying |
| Penta Group | Revenue Operations Manager | 2026-07-20 | `Rejected` | Application review | Declined 2026-07-30, 10 days |
| Superhuman | Group Manager, Growth & Website Content | 2026-06-17 | `Ghosted` | Application review | 53 days silent |
| DwyerOmega | Key Account Manager | never | `Withdrawn` | Not submitted | Josh judged it not a fit |

---

## Revised read

**The previous diagnosis (low volume, throughput-constrained) was wrong.** It was computed
off 6 tracked applications when the real number is 50+.

What the corrected data shows:

- **Volume is not the problem.** 50+ applications is a real search.
- **The resume is not blocking interviews.** At least one first-round interview, one AI
  interview, and one direct hiring-manager contact, all within the last 5 days.
- **The tracked-vs-actual gap was the problem.** Four live conversations had no owner, no
  follow-up timing, and no next action. Interview threads go cold in days, not weeks.

**The real question has moved downstream:** what happens after first contact. That cannot
be answered yet, because outcomes for the live threads are unknown.

## Open data gaps

Blocking a real funnel diagnosis:

1. **Total applications sent.** "1–50 of many" — needs the actual count and the date range.
2. **LeahV.** Which company, which role, and what happened in the Aug 5 first round.
3. **micro1.** Which company it screens for, which role, what the AI interview was for.
4. **Infinite Music.** Was Tyrese Johnson's Aug 5 message replied to.
5. **Horizon Organic Dairy.** Which role, what stage the thread reached.
6. **Full response inventory.** How many of the 50+ produced any human reply, and how many
   reached a screen or interview.

Until #1 and #6 are known, response rate stays uncomputable. Everything else is a guess.

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

## Operating rule going forward

**Every application gets a row, whether or not `/tailor-resume` built a folder.** The
untracked applications are where the live opportunities turned out to be. A tracker that
only sees the tailored ones will keep producing confident wrong answers, which is exactly
what happened on 2026-08-09.

## Strategy-change triggers

| Signal | Read | Change |
| :--- | :--- | :--- |
| < 10% response after 20 applied | Resume or positioning is not landing | Rework positioning |
| Good response, dies at screen | Pitch or story problem, not paper | Rework the verbal narrative |
| Dies after first interview | Role fit or interview depth | Interview prep, re-check target roles |
| Strong response, low volume | Throughput | Raise weekly target |
| High volume, low fit scores | Applying too broadly | Raise the fit floor |

**Cannot determine which is firing until the live-thread outcomes are known.**
