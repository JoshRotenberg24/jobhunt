# STAR Answer Scripts — micro1 AI Agent Productivity Specialist

**Fully-written spoken answers. First person, ~60–90 sec each.** Rehearse out loud until they
feel like *yours*, not memorized. Every fact here traces to the master profile — nothing invented.
Bold = the phrase to actually land.

**How to use:** For each question, the *Situation/Task* sets the scene fast, the *Action* is the
meat (spend 60% of your airtime here), and the *Result* closes with impact + what's reusable.
When the AI recruiter follows up with "how exactly?", the **Deeper** notes are your next layer.

---

## Q1. "How is AI a core part of your daily workflow — not just occasional assistance?"

> "For me AI isn't a tool I open now and then — **it's the thing my business runs on.** At
> Solenzo I build autonomous, AI-driven marketing systems for service businesses. So a typical
> day isn't 'ask ChatGPT to write an email' — it's designing agent workflows that score a
> business's digital footprint, generate personalized outreach, qualify leads, and book
> appointments without me touching each step. I'm in Claude and ChatGPT daily, plus the native
> AI inside the platforms I build on, and I move between them depending on what the task needs.
>
> The core of my work is taking a business owner's loose, non-technical idea and turning it into
> precise prompts and agent instructions that actually produce reliable output. **I'm the bridge
> between what someone means and what the model reliably does.** That's the muscle I'd bring
> here — not occasional help, but building and running AI systems as the actual product."

**Deeper if pushed ("what does a day look like?"):** discovery with an owner → decompose the
manual process → write structured prompts/agent logic → wire it into their CRM/CMS → sample the
outputs → tighten. Name the loop.

---

## Q2. "Walk me through the most sophisticated multi-step AI workflow you've built."

> "**Situation** — a service-business owner came to me with one sentence: 'get me more of the
> right leads.' No spec, no definition of 'right.'
>
> **Task** — I had to turn that into something automated and reliable, not a one-off.
>
> **Action** — First I ran discovery to actually define a good-fit lead. Then I decomposed the
> whole manual process into an agent architecture. I built an **audit workflow that scores a
> business's digital footprint** — its website, its reviews, its visibility gaps — and uses that
> score to generate hyper-personalized outreach. The hard part wasn't the automation plumbing, it
> was the prompt and agent logic: translating the owner's non-technical feedback into structured
> instructions so the model produced outreach that was specific and true to each prospect, not
> generic mail-merge. I wired it into the CRM so it ran end to end, and I **enrolled 180-plus
> contacts** through it.
>
> **Result** — personalized outreach at scale from a one-line ask. And the reusable win is the
> *method*: intent to structured prompt to agent logic to evaluation. That's the same method I'd
> point at any new workflow."

**Deeper ("what did the prompt look like?"):** describe the shape — role/context block, the
scoring criteria as explicit rules, hard constraints ("only reference details present in the
provided data — do not infer"), output format. Show you think in structured instructions.

---

## Q3. "How do you evaluate whether an AI output is good? Give an example of catching a bad one." ⭐ MOST IMPORTANT

> "I don't judge on whether the output *sounds* good — I judge the reasoning and I check it
> against ground truth.
>
> **Situation** — my outreach agent generates personalized messages autonomously, so if its
> reasoning drifts, a wrong message goes to a real prospect. **Task** — I needed to catch that
> before it shipped, not after.
>
> **Action** — I built evaluation loops: I sample the generations and check each one against the
> actual business data the agent was given. The specific failure I kept watching for was the
> model **filling a thin-data gap with a plausible-but-invented detail** — claiming something
> about a business that wasn't in the source. When I caught that, I didn't just flag 'wrong.' I
> traced root cause: the prompt was inviting the model to be 'compelling' without constraining it
> to only-provided facts. So I added an explicit constraint — reference only what's in the data,
> and if a field is empty, say nothing rather than guess — and re-sampled to confirm it held.
>
> **Result** — the hallucinated specifics went away, and I had a repeatable check instead of a
> one-time fix. **That's exactly the loop you're describing in this role** — evaluate, find the
> real limitation, and give feedback specific enough to actually change the behavior."

**This is your make-or-break answer. Have the invented-detail example crisp. Root cause > symptom.**

---

## Q4. "How do you decide when human judgment should override the AI?"

> "**Situation** — a client's Google Ads were pouring in spam and low-quality leads, and the
> obvious move was 'fix the ads.' **Action** — I did optimize the account and cut the junk, but I
> didn't stop at the obvious lever. When I looked at the full funnel, the *real* bottleneck was
> on-site conversion — the CRO — not the ad layer. **Result** — the fix was somewhere the surface
> signal wasn't pointing.
>
> That's my rule for AI too: **AI is strong on pattern and volume, weak on novel context and on
> verifying its own confidence.** So I override when two things are true — the stakes of a wrong
> autonomous action are high, or the model is reasoning confidently from context it's actually
> missing. A confident answer built on absent information is the most dangerous output there is,
> and that's exactly where a human has to step in."

---

## Q5. "You have a workflow that works great on one AI platform. The customer's model behaves differently. What do you do?"

> "I don't marry a platform — the workflow is the asset, not the tool. So I re-run the *same task*
> on the new model and watch specifically for where its strengths and failure modes differ from
> what I built around. Maybe it's better at long context but more prone to over-explaining, or it
> holds instructions differently. Then I adjust the decomposition and the prompts to fit *that*
> model instead of assuming parity. I already move between Claude, ChatGPT, and platform-native AI
> depending on the job, so **picking the right approach per task and per tool is normal for me,
> not a disruption.** The goal is a reliable outcome; the path to it is allowed to change."

---

## Q6. "How would you give feedback that actually improves a model's reasoning?"

> "Specificity and root cause — the same way I write agent instructions. Bad feedback is 'this is
> wrong.' Useful feedback is: 'the agent skipped verifying X, then assumed Y from data that wasn't
> present, and here's the corrected reasoning chain it should have followed.' I point at the step
> where the reasoning broke, not just the final answer. **My whole job at Solenzo is translating
> vague intent into precise instructions a model can reliably act on** — giving structured
> feedback to a model is that same skill pointed in the other direction. I'd want to make the
> feedback concrete enough that the correct behavior is obvious from it."

---

## Q7. "Tell me about scaling AI/tool adoption across a team." (their 'highly valued' qual)

> "**Situation** — at Wix I helped build a brand-new vertical from proof-of-concept to a
> profitable line. **Action** — I was hands-on with hiring, onboarding, and training new hires,
> and I built sales training for the tenured account executives too — so I was the person making a
> new capability actually stick, not just launch. **Result** — it became a profitable, impactful
> business line, and my manager put it in writing that she'd hire me again in an instant. I did
> the same at Birdeye — **onboarded and managed 15 to 20 reseller partners and retained all but
> one, about 94%** — by making complex tooling adoptable for non-technical people.
>
> That's the through-line: I don't just use a new capability myself, **I make it land across a
> team of people who don't think like power users.** That's what scaling AI adoption really is."

---

## Q8. "What's a limitation of current AI agents you find most important?"

> "The one I hit most is **confident gap-filling** — when the source data is thin, agents will
> generate a plausible detail rather than admit the gap, and they'll state it with the same
> confidence as a verified fact. It's dangerous precisely because it *reads* well. The second is
> losing the thread on long, multi-step tasks — drifting from the original objective a few steps
> in. I design around both: hard constraints that forbid inferring beyond provided data,
> verification checkpoints between steps, and human review at the high-stakes moments. **I treat
> those limitations as the design problem, not a reason to distrust the whole system.**"

---

## Q9. "Why are you interested in this role / this kind of work?"

> "Two reasons, and they're honest. One — this is already what I do all day. I build and evaluate
> agent systems for real business outcomes, so contributing to how frontier models reason and
> support knowledge workers is a direct extension of my actual work, not a stretch. Two — I get
> the most value out of AI when I'm at the edge of what it can do and figuring out where it breaks.
> **This role is literally paid to live at that edge** — use AI at expert depth, then make it
> better. That's the part of my week I'd do anyway."

---

## Q10. "What makes you an *advanced* AI user versus an average one?" (self-assessment trap)

> "An average user asks the model to do a task. I **design the system the task runs inside** —
> decomposition, constraints, tool integration, and an evaluation loop to catch drift. The tell is
> that I assume the model will be wrong in specific, predictable ways, and I build for that up
> front instead of being surprised by it. I also don't get attached to one tool or one prompt — I
> test, I measure against ground truth, and I change the approach when the evidence says to.
> **Average users trust the output; I interrogate it.**"

---

## Rapid-fire backups (one-liners, if time is short)
- **Tools you use daily:** Claude, ChatGPT, platform-native AI (GoHighLevel), plus CRM/CMS integrations.
- **Signature metric:** 20+ automated workflows built; audit workflow enrolled 180+ contacts.
- **Proof you make AI stick for others:** ~94% partner retention at Birdeye; built team training at Wix.
- **Judgment proof:** diagnosed CRO — not ads — as the real conversion bottleneck (full-funnel thinking).
- **Your one sentence:** *"I'm the bridge between loose business intent and reliable LLM output."*

---

## Delivery reminders for the AI-recruiter screen
1. **Answer, then stop.** Let it ask the follow-up. Don't monologue past the point.
2. **Specifics over adjectives** — "180 contacts," "an invented detail I constrained out," not "a lot" / "better."
3. **When it drills, go one layer deeper** — that's a good sign, not a trap. The Deeper notes are for this.
4. **Reframe marketing stories in AI/eval/productivity language** — they care about the agent work, not GHL.
5. **Quiet room, clear audio, pause before answering.** Composure reads as competence.
