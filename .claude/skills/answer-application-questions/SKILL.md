---
name: answer-application-questions
description: >
  Draft Joshua Rotenberg's answers to application form questions, screening questions,
  and interview prep prompts ("tell me about a time...", "why this role", "describe your
  process"). Use whenever a job application asks a free-text question, or when asked to
  prep an answer for an interview. Pulls only from profile/master-profile.md, applies the
  profile's Writing Standards for prose, keeps metric scope honest, writes in Josh's
  voice, and saves answers to applications/<company-slug>/questions.md so they are
  reusable. Never invents clients, projects, or numbers.
argument-hint: <the application question, plus company if known>
---

# Answer Application Questions

Same source of truth and same discipline as `/tailor-resume`, applied to prose. A resume
gets skimmed; these answers get read. They are often the only place a hiring manager
hears Josh think, which makes them worth more per word than anything on the resume.

## Step 1 — Read the standards and the facts

Read `profile/master-profile.md`, specifically:
- **Writing Standards → Prose answers** — the rules this skill enforces.
- **Bullet Bank** for the employer most relevant to the question.
- **Verified Quantified Metrics** — the only numbers permitted, with their scope.
- **Numbers Worth Capturing** — if the best answer needs a number that lives here rather
  than in the verified list, that gap gets flagged to Josh, not filled by estimation.

If there's a match report for this company (`applications/<slug>/match-report.md`), read
it too. Its gap table tells you which weaknesses the answer should quietly shore up.

## Step 2 — Pick the true story, then check its shape

Choose the strongest **real** experience for the question. Then run three checks before
writing a word:

1. **Does a specific enough story exist?** The profile records roles and patterns, not
   named client narratives. If the question asks for one project and the profile only
   supports a pattern, say so to Josh up front and write it at the level the evidence
   actually supports. Do not invent a client to satisfy the question's grammar.
2. **What scope are the metrics?** Segment-level, portfolio-level, and single-account
   numbers are not interchangeable. Carry the scope into the sentence.
3. **What is the gap this answer should address?** Most questions are a chance to
   pre-empt the reservation the resume creates (an off-target title, a short stint, a
   missing domain). Use it.

## Step 3 — Draft

Structure that works for "tell me about a time" questions, without announcing itself:

1. **Scope line.** Role, size, and what was being built or fixed.
2. **The shape of the work.** What the phases actually were, concretely.
3. **One real decision, with the reasoning.** This is the part that distinguishes the
   answer. Include the tradeoff or the risk being managed.
4. **The human half.** Change management, resistance, training, stakeholder friction.
   Most candidates skip it, and most implementation failures live there.
5. **Outcome with honest scope**, plus what outlasted the work if that's true.

Length: match what was asked. "Briefly" means roughly 150–200 words. An open box with no
guidance means 200–300. Never pad to look thorough.

Apply the voice rules from the profile's Writing Standards. No em dashes, commas and
parentheses instead.

## Step 4 — Flag honestly, then save

Tell Josh, in one or two lines before the draft:
- any place the answer is written at pattern level because no single-client story exists
  in the profile,
- any metric whose scope had to be stated carefully,
- what a real number or client name would upgrade, if he can supply one.

Save to `applications/<company-slug>/questions.md`, appending under a heading for each
question with the date. These get reused: the same six questions recur across
applications, and a bank of true, well-shaped answers compounds exactly like the bullet
bank does.

If the answer surfaces a number Josh confirms on the spot, hand it to
`/excavate-profile` to write into the master profile rather than letting it live only in
this one answer.

## Anti-goals

- No invented clients, projects, timelines, or numbers. A thinner true answer beats a
  vivid false one, and the false one has to be defended live in an interview.
- No composite stories presented as a single engagement.
- No "great question," no motivational register, no listing values instead of actions.
- Do not answer at a higher seniority than the profile supports. Overclaiming scope is
  the most common way these answers fail a follow-up question.
