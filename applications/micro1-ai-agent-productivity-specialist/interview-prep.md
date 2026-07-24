# Interview Prep — AI Agent Productivity Specialist @ micro1

**Prepared:** 2026-07-24 · **Candidate:** Joshua Rotenberg
**Role:** AI Agent Productivity Specialist (Contractor, Remote, $30–90/hr)
**Company:** micro1 — AI data lab training frontier models & evaluating AI agents

---

## 1. What this role actually is (read this first)

This is **not** a role building products *for* micro1. micro1 is a data lab; you'd be an
**expert contributor / evaluator**. The customer is an AI company building "next-generation
productivity tools," and micro1 supplies vetted humans who:

- Use AI heavily on realistic professional tasks (research, analysis, automation, workflows).
- **Evaluate** what the AI agent produces — spot where it breaks, hallucinates, over/under-reasons.
- Write **high-quality feedback / training signal** that improves how the model reasons and collaborates.
- Design and document effective **workflow patterns** the model should learn from.

Mental model: you are both a **power user** (you show them how a real expert drives AI) and a
**judge** (you tell them where the agent fell short and why). The deliverable is quality — clear
reasoning about *why* an output is good or bad, not just a thumbs up/down.

### Likely process
micro1 is known for an **AI-recruiter screen** (a live, conversational AI interviewer) before any
human conversation. Expect:
1. **AI-recruiter interview** — voice/chat, ~20–40 min. It probes real depth: it will ask
   follow-ups and try to catch vague or memorized answers. Treat it like a real interviewer.
2. Possibly a **work sample / paid trial task** — you actually do the work (build or evaluate a
   workflow) and they assess your reasoning and output quality.

**Implication for prep:** rehearse out loud, keep answers *specific and concrete*, and always be
ready to go one level deeper ("how exactly? what did the prompt look like? how did you know it
was wrong?"). AI interviewers punish hand-waving.

---

## 2. Your positioning (the through-line)

> "I don't use AI as an occasional assistant — I run my business on agentic AI. At Solenzo I
> take a manual business workflow, decompose it into an agent architecture with custom logic,
> and translate a non-technical owner's loose intent into precise prompts and agent
> instructions. Then I build evaluation loops to watch the outputs and keep tightening them.
> That's the whole job here: use AI at expert depth, then judge where it falls short and say
> exactly why."

Use the **"AI / Agentic Ops"** summary as your verbal identity. You are the *bridge between
business intent and reliable LLM output* — that phrase is gold for this role.

Three pillars to keep coming back to:
1. **Daily-driver depth** — AI is core to your workflow, not a novelty.
2. **Workflow architecture** — you build multi-step agent systems that touch real tools (CRMs, CMS, data).
3. **Evaluation instinct** — you already build feedback/eval loops to judge and improve agent output.

---

## 3. Scope-of-work → your proof (map every requirement to a real story)

| Their scope item | Your evidence (all true, from master profile) |
| :--- | :--- |
| Design/optimize AI workflows that automate complex processes | Architected a **complete GoHighLevel automation system — 20+ workflows** across capture, qualify, book, no-show recovery, onboarding, nurture/reactivation, reviews |
| Integrate AI with workplace tools, data, connected systems | Built **reusable agent infrastructure integrating with client CRMs and CMS platforms** for 24/7 automated growth engines |
| Evaluate AI outputs, find limitations, give high-quality feedback | **Designed self-improving loops and evaluation frameworks to monitor agent outputs and continuously optimize** conversion |
| Complex research/analysis/decision-support with AI | Built a **prospect "audit" workflow enrolling 180+ contacts** that scores a business's digital footprint to trigger personalized outreach; technical SEO audits, keyword-gap & competitor analysis |
| Adapt across AI platforms & evolving tech | Fluent across **ChatGPT, Claude**, GHL native AI, prompt design; comfortable picking the right tool per task |
| Improve AI adoption / share best practices | 15+ years teaching adoption: **onboarded/trained 15–20 reseller partners at Birdeye (~94% retention)**; built sales training at Wix; publish thought leadership on systems architecture |

---

## 4. STAR stories (memorize 3–4, know the details cold)

### Story A — "Turn fuzzy intent into a reliable agent" (your signature story)
- **S/T:** A service-business owner gave me a loose goal — "get me more of the right leads" —
  with no spec.
- **A:** I ran discovery to pin down what a *good* lead actually was, then decomposed the manual
  process into an agent architecture: a workflow that scores a business's digital footprint
  (site, reviews, visibility gaps) and generates hyper-personalized outreach. I translated the
  owner's non-technical feedback into structured prompts and agent instructions, then built an
  audit workflow that enrolled **180+ contacts**.
- **R:** Automated, personalized outreach at scale from a one-sentence ask. The reusable part is
  the *method* — intent → structured prompt → agent logic → eval.
- **Why it lands:** demonstrates all three pillars at once. This is your best answer to "tell me
  about a sophisticated AI workflow you built."

### Story B — "Catch the agent being wrong" (evaluation depth)
- **S/T:** My automated systems generate outreach and scoring autonomously — if the agent's
  reasoning drifts, it goes out to real prospects.
- **A:** I built **evaluation frameworks and self-improving loops** to monitor outputs: sampling
  generations, checking them against the actual business signals, and tightening prompts/logic
  where the model over-generalized or hallucinated specifics.
- **R:** Continuous optimization instead of set-and-forget. **This is the exact muscle micro1 is
  hiring for** — be ready to describe a concrete failure you caught (e.g., the agent inventing a
  detail about a business that wasn't in the data, and how you constrained it).
- **Prep note:** have ONE crisp, specific example of a hallucination/limitation you caught and
  how you diagnosed root cause vs. symptom.

### Story C — "Full-funnel troubleshooting / know when the AI is the wrong answer" (judgment)
- **S/T:** A client's Google Ads were driving spam and low-quality leads.
- **A:** I optimized the account to cut junk, then diagnosed that the *real* bottleneck was
  on-site CRO — not the ad layer.
- **R:** Shows you know **when human judgment is required** and when to stop trusting the obvious
  lever. Great answer to "how do you decide when to override the AI / when human judgment matters?"

### Story D — "Scaling AI adoption in a team" (the 'highly valued' bonus qual)
- **S/T:** At Wix, helped build a brand-new vertical from proof-of-concept to a profitable line.
- **A:** Assisted with hiring, onboarding, and training new hires, and built sales training for
  tenured AEs. At Birdeye, onboarded/trained **15–20 partners at ~94% retention**.
- **R:** Directly answers their "experience introducing, mentoring, or scaling AI adoption"
  preferred qual. Reframe: you're the person who makes a new capability *stick* across a team.

---

## 5. Likely questions + how to attack them

**"How is AI a core part of your daily workflow — not just occasional help?"**
→ Lead with Solenzo: you *architect autonomous AI systems* as the product, not a helper. Name the
tools (Claude, ChatGPT, GHL native AI), the cadence (daily), and the fact that clients' growth
engines run on the agents you build.

**"Walk me through the most sophisticated multi-step AI workflow you've built."**
→ Story A. Go deep: the decomposition, the prompt structure, the tool integrations, the eval loop.
Have the *shape* of an actual prompt/agent instruction in your head so you can describe it.

**"How do you evaluate whether an AI output is good? Give an example of catching a bad one."**
→ Story B. Emphasize: check against ground truth, look for invented specifics, judge reasoning not
just the surface answer. Give your one concrete hallucination example.

**"How do you decide when human judgment should override the AI?"**
→ Story C + principle: AI is great at pattern/volume, weak on novel context, stakes, and
verifying its own confidence. You override when the cost of a wrong autonomous action is high or
when the model is confidently reasoning from missing context.

**"You have a workflow that works on ChatGPT. The customer's platform behaves differently. What do you do?"**
→ Show adaptability (preferred qual #4): you don't marry a platform. You re-test the same task,
find where the new model's strengths/failure modes differ, and adjust prompts/decomposition
rather than assuming parity.

**"How would you give feedback that actually improves a model's reasoning?"**
→ Specificity + root cause. Not "this is wrong" but "the agent skipped verifying X, assumed Y from
absent data, and here's the corrected reasoning chain." You already do this translating fuzzy
intent into precise agent instructions — same skill pointed at model feedback.

**Curveball: "What's a limitation of current AI agents you find most important?"**
→ Pick a real one you've hit: e.g., agents confidently filling gaps with plausible-but-invented
detail when the source data is thin; or losing the thread on long multi-step tasks. Tie it to how
you *design around it* (constraints, verification steps, human checkpoints).

---

## 6. Questions to ask them
- What does a typical task/project look like — building workflows, evaluating agent transcripts, or both?
- How is output quality measured, and what does great feedback look like to you?
- Which AI platforms/agents will I be working with, and how often do they change?
- Is there a paid calibration or trial task, and how is ongoing work allocated?
- What separates your best contributors from average ones?

---

## 7. Practical prep checklist (do before the interview)
- [ ] Have **one concrete AI-failure example** ready (a specific hallucination/limitation you
      caught + how you fixed it). This is the single most important story to nail.
- [ ] Be able to **describe the shape of a real prompt / agent instruction** you've written — not
      just "I wrote a prompt."
- [ ] Rehearse Stories A–D **out loud**; time them to ~90 seconds each.
- [ ] Reframe every marketing-ops story in **agent/eval/productivity** language, not
      "marketing" language — this customer cares about AI workflows, not GHL.
- [ ] For the AI-recruiter screen: quiet room, clear audio, speak in specifics, and *pause* to
      answer follow-ups instead of monologuing.
- [ ] Don't undersell as "marketing guy who uses ChatGPT." You **build and evaluate agent
      systems** — say it that way.

## 8. Watch-outs
- **Metrics discipline:** only cite verified numbers (20+ workflows, 180+ contacts enrolled,
  ~94% Birdeye retention, 30% traffic / 25% conversion at Wix). Don't invent AI-specific metrics.
- **Don't over-claim engineering.** You architect agent *workflows* and prompt logic — you're the
  business-intent-to-reliable-output bridge, not a model-training engineer. That's exactly what
  they want; own it precisely.
- **Contractor reality:** hourly, task-based, variable volume. Fine as fractional income
  alongside Solenzo — clarify expected hours/allocation before committing.
