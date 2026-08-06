---
name: excavate-profile
description: >
  Interview Joshua Rotenberg about his work history to surface real, quantified wins
  that are missing from profile/master-profile.md, then write the verified results back
  into the profile. Use whenever asked to dig up accomplishments, add metrics, find
  numbers for the resume, fill a gap flagged in a match report, strengthen the bullet
  bank, or update the master profile. Also use after a tailoring run flags "metrics
  needed." One question at a time, never batched. Every number must come from Josh —
  the skill proposes phrasing, never facts.
argument-hint: [employer or gap to dig into, e.g. "Wix" or "Excel evidence"]
---

# Excavate Profile

Everything `/tailor-resume` can produce is capped by what's in
`profile/master-profile.md`. That file is the bottleneck, not the tailoring. This skill
widens it.

Josh has 15+ years of real work and a profile carrying only a handful of hard numbers.
The gap is not that the work didn't happen. It's that most of it was never written down,
and he systematically under-reports routine competence as "that doesn't count." It
counts. The job here is to get it out of his head and into the file, accurately.

## Hard rules

1. **One question at a time.** Never batch. Batched questions get one answer and the
   rest evaporate. This is the single most important rule in the skill.
2. **Facts come from Josh. Only phrasing comes from you.** Never propose a number and
   ask him to confirm it, which invites anchoring on a figure you invented. Ask an open
   question and take what he gives.
3. **Ranges and estimates are fine, precision theater is not.** "Somewhere between 8 and
   12 accounts at once" is a usable, honest fact. Record it as a range. Never round a
   range up into a clean number.
4. **Mark uncertainty in the profile.** If he's unsure, write it into the metrics table
   with a `(self-estimated)` tag so future tailoring runs know what will survive a
   reference check and what won't.
5. **Stop when he's done.** Josh has finite bandwidth and decision fatigue is real. Six
   to ten questions per employer is the useful range. If answers get short, wrap up and
   bank what you have rather than pushing for completeness.

## Step 1 — Pick the target

If given an employer or a gap, start there. Otherwise read the most recent
`applications/*/match-report.md` files, collect every entry under "Metrics that would
strengthen the resume," and rank by how often the same gap recurs across roles. Recurring
gaps are worth more than one-off ones because they compound across future applications.

Tell Josh which target you picked and why, in one line. Then start asking.

## Step 2 — Interview, one question at a time

Work chronologically inside an employer. Open with scope, then move to specifics. The
questions that actually produce numbers:

**Scope and volume**
- How many accounts, clients, or projects were you running at the same time?
- How big was the team you led? How many did you hire or train?
- What was the size of a typical account, in dollars or in users?

**Time**
- How long did a typical onboarding or implementation take, start to launch?
- Did that get faster while you were there? From what to what?
- What was the longest or most complex one, and why?

**Before and after**
- What was broken when you got there, and what did it look like when you left?
- What did you build that outlasted you, and is anyone still using it?
- What was the manual process you replaced, and what did it cost before?

**Data and volume of work**
- How many records, contacts, or line items were in the biggest migration you ran?
- What tool did you actually clean that data in, and what was wrong with it?
- How many training sessions did you run, and how many people attended?

**Trouble**
- What was the implementation that nearly failed, and what did you do about it?
- What did you catch early that would have blown up later?
- What did you escalate, and what happened next?

After each answer, do two things before the next question: reflect it back in one line so
he can correct it, and follow the thread if there's a number just under the surface.
"Most of them" is a prompt to ask "out of how many?"

When he says something didn't count, that's the signal to slow down, not move on. Ask
what the alternative was if he hadn't done it.

## Step 3 — Convert to bullets

Turn each confirmed win into profile-bank format: **strong verb, specific object,
measurable result.** No "responsible for," no "helped with," no "worked on."

Draft the bullet, show it to him with the raw answer next to it, and ask whether it
overstates. It is much cheaper to catch an overstatement here than in an interview
where he has to walk it back live.

## Step 4 — Write it back to the profile

Edit `profile/master-profile.md` directly:

- New bullets go in the relevant employer's section of the **Bullet Bank**.
- New hard numbers go in **Verified Quantified Metrics**, with the employer and, where
  it matters, the scope the number covers (one account, a segment, a portfolio). Scope
  errors are how honest metrics turn into dishonest resumes.
- New tools or systems he named go in the **Core Competencies Bank**.
- If a whole capability surfaced that no summary variant covers, add a variant.

Keep the file's existing structure and voice. Do not restructure it.

## Step 5 — Report and re-render

Tell him what got added, in a short list. Then check
`applications/*/match-report.md` for gaps the new material now closes, and offer to
re-render those resumes. A new metric is worth nothing until it's on a page someone
reads.

## Anti-goals

- Do not fabricate, infer, or "reconstruct likely" numbers. A missing metric stays
  missing.
- Do not turn this into a form. It's a conversation, and the good material comes from
  following threads, not from covering the checklist.
- Do not pad the profile with soft claims to make it look fuller. The profile's value is
  that everything in it is true.
