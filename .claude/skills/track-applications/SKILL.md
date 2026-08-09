---
name: track-applications
description: >
  Maintain and review Joshua Rotenberg's job application tracker at
  applications/tracker.md. Use whenever an application is submitted, a response arrives
  (screen, interview, rejection), a follow-up is sent, or Josh asks for a status update,
  a weekly review, response rate, pipeline, "what's due", "what did I apply to", or
  "where am I stalling". Also use right after /tailor-resume builds a new application
  folder, to add its row. Computes real funnel metrics from recorded data only, never
  from estimates, and names the one variable worth changing when the funnel is
  underperforming.
argument-hint: <blank for status | "review" for weekly | "applied <company>" | "<company> <new status>">
---

# Track Applications

The tracker exists because a job hunt is a funnel and an untracked funnel cannot be
diagnosed. Josh's stated problem is response rate. Response rate is a division problem,
and until both numbers are recorded, every explanation for a slow search is a guess.

**Source of truth:** `applications/tracker.md`. Never keep state anywhere else.

## Core rule

**Record only what happened.** No inferred dates, no assumed submissions, no estimated
response counts. An unknown stays `?` until Josh supplies it. A tracker with honest gaps
is useful. A tracker with plausible-looking filler is worse than none, because it
produces confident wrong diagnoses.

---

## Mode 1 — Status (default, no args)

Print the Active table, then:

- Rows **past due** on their next action, most overdue first
- Rows **approaching** a follow-up trigger in the next 2 days
- Anything still `Drafted` more than 3 days after being built
- Any row with `Applied = ?`, since those silently corrupt every metric

Lead with what needs action today. If nothing is due, say so in one line.

## Mode 2 — Review (`review`)

The Monday number. Compute from recorded rows only, and state the denominator every
time, because a rate off 4 applications is noise and should be labeled as such.

```
Applied (last 7 days):     n        (target: t)
Applied (all time):        N
Response rate:             r%       (x responses / N applied)
Screen rate:               s%       (x screens / N applied)
Interview rate:            i%       (x interviews / x screens)
Median days to response:   d
Drafted, never sent:       n
```

Then the stage histogram (where applications die), then **one** recommendation drawn
from the Strategy-change triggers table in the tracker. One, not a list. If the sample
is under 20 applications, say the sample is too small to diagnose and recommend volume
instead.

## Mode 3 — Update

Natural-language updates: `applied karbon`, `nametag rejected`, `penta screen 8/14`.

On update:
1. Set `Status`, `Last touch`, and today's date where relevant.
2. Recompute `Next action` and `Due` from the tracker's trigger table.
3. On a terminal status (`Rejected`, `Ghosted`, `Withdrawn`, `Archived`), move the row
   to **Closed** and record the stage it died at. The stage is the diagnostic value.
4. On `Rejected` after an interview, ask Josh once whether he got a reason. Recorded
   rejection reasons are the highest-signal data in the whole file.

## Mode 4 — Add

Called after `/tailor-resume`. Add a row with company, role, fit score, today's date as
`Built`, `Applied = ?`, `Status = Drafted`, next action "Submit", due tomorrow.

---

## Judgment rules

- **Sort Active by `Due`, not by fit score.** The tracker is an action queue.
- **A stale posting is not a live application.** Anything built over 3 weeks ago and
  never submitted should be flagged for archiving rather than sent late. Per
  `ats-playbook.md`, volume is the real filter, and a 6-week-old posting is already
  shortlisted.
- **Never let a fit score justify chasing a dead role.** An 85 that has been silent for
  21 days is closed, same as a 54.
- **Do not congratulate on activity.** Applications submitted is an input, not an
  outcome. Report it, do not celebrate it.
- **One recommendation per review.** Changing the resume, the targeting, and the volume
  in the same week means learning nothing from any of them.

## What this skill must never do

- Estimate a response rate when `Applied` is unknown. Report the gap instead.
- Mark something `Applied` because a folder exists.
- Suggest padding, exaggerating, or manufacturing anything to lift a metric. If the
  funnel is bad, the fix is targeting, positioning, or volume.
