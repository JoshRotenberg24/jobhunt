# micro1 AI Interview — Prep

**Format:** ~33 min, AI interviewer (Zara), recorded video + audio + transcript, per-question
time limits, speak or type.
**Topics:** Driving Adoption · Daily Use of ChatGPT Work & Claude Cowork · Connectors ·
Multi-Connector Workflow Walkthrough · Power Usage of AI Agents · Switching Between ChatGPT
and Claude.
**Prepared:** 2026-08-06

---

## 1. What is actually being screened

This is not a marketing-ops interview with AI questions bolted on. Six topics, and five of
them are about whether you personally operate these tools every day. micro1 places domain
experts on AI training and evaluation work, and this topic list reads like a screen for
someone who can (a) run real multi-tool agentic work and (b) get other humans to adopt it.

Two things follow from that:

**They are testing recency and specificity, not credentials.** Nobody can fake a connector
walkthrough. The questions are designed so that a person who used the tools this week sounds
different from a person who read about them. Every answer needs a proper noun in it: a named
connector, a named workflow, a named failure.

**"Driving Adoption" is where your 15 years pay for themselves.** Most candidates in this
pool are power users who have never had to make a skeptical account manager change how they
work on a Tuesday. You have run onboarding at Wix, partner enablement at Birdeye, and CRM
adoption advisory at Accelo. That is the topic to win outright.

---

## 2. Mechanics, and how the scoring actually works

- **Structure beats brilliance.** The scoring engine weighs communication clarity alongside
  technical accuracy. A disorganized expert scores below an organized average candidate.
  Answer in visible structure, out loud: "Three things. First... second... third."
- **Integrity score is a gate, not a factor.** Proctoring watches tab switching, eye movement,
  and screen overlays. Fail integrity and technical performance does not matter. So: close
  every other tab, no second monitor, no notes on screen, do not look off-camera to read.
  Keep paper notes out of frame or do not use them at all. Prep by rehearsing, not by
  scripting.
- **Zara asks follow-ups on what you just said.** Every unsupported claim is a trapdoor. Do
  not say "I built a multi-agent system" unless you can narrate it for ninety more seconds.
- **Per-question time limits.** Roughly five minutes a topic. Lead with the answer, then
  support it. Do not build to a conclusion you never reach.
- **Speak, do not type.** Typing burns the clock and flattens the communication score. If a
  question genuinely needs a list, say the list.

---

## 3. The answer shape to use every time

Rehearse this until it is automatic. It fits inside a time limit and it front-loads the part
that scores.

1. **Headline (one sentence).** The direct answer.
2. **Concrete instance (two or three sentences).** One real workflow, named tools, named data.
3. **The judgment call.** What you decided and why, including the tradeoff. This is the part
   that separates an operator from someone describing a feature list.
4. **Result or lesson, with honest scope.** What changed, and at what scale it was measured.

Under pressure, most people skip step 3. It is the highest-scoring sentence in the answer.

---

## 4. Talk tracks by topic

Fill every `[bracket]` with something real before interview day. Where the profile has no
number, stay qualitative and specific rather than reaching for one.

### Topic 1 — Driving Adoption

**Headline:** Adoption fails at the workflow level, not the tool level. Handing someone a
blank chat box is not a rollout, so I ship the workflow preloaded and make one person
visibly successful before I go wide.

**The five-beat spine (say it as a spine, it is memorable):**

1. **Start where the pain is measurable.** Pick the workflow people already complain about,
   not the most impressive demo. If nobody was annoyed by it before, nobody will change for it.
2. **Build a lighthouse user first.** One person, one workflow, real output their peers can
   see. Peer proof moves a team, mandates do not.
3. **Ship the SOP, not the tool.** Preloaded prompts, project instructions, connectors already
   configured. The unlock is that a new user's first attempt works.
4. **Set the trust boundary explicitly.** Read-only first, human approves anything that writes.
   Most resistance is risk management, not laziness. Naming the boundary removes the objection.
5. **Measure behavior, then kill what nobody uses.** Weekly active on the specific workflow,
   time to first useful output, rework rate. Vanity metrics like seats licensed tell you nothing.

**Your evidence to attach:**
- Birdeye: onboarded and managed 15 to 20 reseller partners on marketing automation and
  reputation tooling, retained all but one (about 94% retention). Adoption there was the
  entire job. Partners had to change how they sold, not just log in.
- Wix: led a team of onboarding specialists in a brand-new vertical that went from proof of
  concept to a profitable line, including building the training for tenured AEs. That is
  change management for people who already thought they knew their job.
- Accelo: advised agencies on CRM adoption, where the failure mode was always the same, a
  system configured correctly and used by nobody.
- Solenzo: translating non-technical stakeholders' loose feedback into precise prompts and
  agent instructions. That is the adoption bottleneck in AI specifically. People do not know
  what to ask for.

**Resistance taxonomy (have this ready, it is a likely follow-up):**

| What you hear | What it means | The move |
| :--- | :--- | :--- |
| "It gets things wrong" | Trust in accuracy | Show citations and source-grounded retrieval, start on read-only tasks where the answer is checkable in one click |
| "Is it reading everything?" | Data and permissions anxiety | Explain permission inheritance and admin controls plainly, once, in their words |
| "I don't have time to learn it" | Workflow inertia | Do not teach the tool, replace one step of their existing workflow and leave the rest alone |
| Silence from a senior person | Fear of being replaced or exposed | Give them the reviewer role, they own quality control on the output rather than competing with it |

**Close on:** what outlasted the work. At Birdeye that was the automated product-training
sequences that kept running after I stopped delivering them live.

---

### Topic 2 — Daily Use of ChatGPT Work & Claude Cowork

**Headline:** Give an actual day, not a capability list.

Narrate a real Tuesday in three passes:

- **Morning, retrieval.** ChatGPT with company knowledge across connected apps to answer
  "what did we decide about X" without opening five tabs. It searches connected sources and
  cites them, so verification is one click.
- **Middle of the day, execution.** Claude Cowork for the long multi-step job that touches
  files: pull the source material, work through it, write the output to disk as an artifact
  I keep. Cowork's differentiator is filesystem access, so a run ends with a file, not just a
  chat transcript.
- **Ongoing, systems.** The recurring version of that job gets turned into something reusable
  (a skill, a plugin, a project with fixed instructions) so it is not re-prompted from scratch
  every week. That is the same instinct behind the 20+ GoHighLevel workflows at Solenzo:
  anything I do twice becomes a system.

**Do not claim daily use of a surface you have not touched.** If your daily driver is Claude
Code, GHL's native AI, or the API rather than Cowork specifically, say what you actually run
and what you have done in Cowork. Integrity is a gate here, and an honest "I use X daily and
have run Y in Cowork, here is the difference I noticed" scores far better than a confident
answer that collapses under one follow-up.

---

### Topic 3 — Connectors

**Headline:** A connector is a permissioned bridge between the model and a system of record,
and the interesting engineering is in scoping and trust, not in clicking connect.

**Have the technical facts straight:**

- **ChatGPT side.** Company knowledge (Business, Enterprise, Edu) pulls context from connected
  apps such as Slack, Google Drive, GitHub, SharePoint, HubSpot, and Zendesk, with citations
  back to the source. It is deliberately read-only retrieval: eligible apps expose search and
  fetch. Writes need agent mode, a write-capable app, or an automation layer. Connectors were
  renamed "apps" in December 2025. Workspace content is excluded from training unless the org
  opts in.
- **Claude side.** Cowork connects to 38+ workplace tools over MCP (Slack, Notion, Google
  Drive, HubSpot, Jira, Salesforce, Snowflake, Google Workspace, and more), and in Cowork
  those connectors gain filesystem access, so external data can land locally and local files
  can feed external actions.
- **The point to land:** connectors inherit the user's permissions. Which means bad access
  hygiene in the source system becomes an AI problem the day you connect it. That is a real
  pre-rollout audit step most people skip.

**Your credibility hook:** you have lived on the write side of this for years. GoHighLevel and
HubSpot workflows moving lead data, tagging, routing, and lifecycle stages, with strict data
hygiene protocols. You know what happens when a system of record gets written to by an
automation nobody audited. Say that. It reframes you from "AI enthusiast" to "person who has
cleaned up the mess."

---

### Topic 4 — Multi-Connector Workflow Walkthrough

**This is the hardest question in the set and the one most likely to expose a bluff.** Zara
will probe. Prepare exactly one workflow you have really run and be able to narrate it in
sequence with named connectors at each step.

**Rehearse the walkthrough on these seven beats:**

1. **The trigger.** What starts it and how often.
2. **Connector A, retrieval.** Which system, what you pulled, why that source and not another.
3. **The transformation.** What the model actually does to the data (score it, classify it,
   summarize it, draft from it). Name the judgment the model is making.
4. **Connector B, the write or the destination.** Where output lands, and whether a human
   approves before it lands.
5. **The failure mode you hit.** Every real workflow has one. Naming it is proof of reality.
6. **The verification loop.** How you know the output was right. Spot checks, an eval set,
   a rules layer, a human review gate on the first N runs.
7. **What it replaced, and the honest result.**

**The candidate workflow from your real work** (the prospect audit engine at Solenzo): a
contact enters, the system scores the business's digital footprint, that score drives
hyper-personalized outreach, and the sequence runs through booking, confirmation, reminders,
and no-show recovery. That workflow enrolled 180+ contacts, and it sits inside a 20+ workflow
GoHighLevel build spanning capture, qualification, booking, onboarding nurture, reactivation,
and review generation.

**Important framing:** narrate that one as the *systems* answer, and be clear about where the
connectors are CRM-and-API rather than ChatGPT or Cowork connectors, if that is the truth. Then
pair it with the smaller, genuinely AI-connector workflow you have run (for example, Drive or
Notion in, analysis, output written back to a doc or a CRM record). Two honest halves beat one
inflated story, and the pairing actually shows range: you have built the deterministic
automation *and* the agentic version, which is exactly the judgment the next topic asks about.

**Rehearse the whole thing out loud, timed, twice.** If it runs past four minutes, cut beat 3
down, not beat 5.

---

### Topic 5 — Power Usage of AI Agents

**Headline:** The skill is decomposition and verification, not prompting. I give an agent the
same thing I would give a contractor: a defined outcome, the context it cannot infer, the
boundaries, and a way to check the work.

**Four things to say:**

1. **Decompose before you delegate.** Break the manual workflow into steps, then decide which
   steps are model judgment and which are deterministic. Agents are for the judgment steps.
   This is literally in your work: breaking manual marketing workflows into agent architectures
   with custom scoring logic.
2. **Build the evaluation loop with the agent, not after it.** Self-improving loops and
   evaluation frameworks that monitor agent outputs and feed back into optimization. Without a
   check, an agent is just a faster way to be confidently wrong at scale.
3. **Keep the human at the write boundary, early.** Read and draft freely. Anything that
   touches a system of record or a customer gets a review gate until the error rate earns
   removal of the gate.
4. **Know when not to use an agent.** High-volume, deterministic, compliance-sensitive work
   belongs in a workflow engine, not an LLM. That answer will separate you from candidates who
   think everything is an agent problem. You can say it with authority because you have built
   both.

**Likely follow-up: "when has an agent failed for you?"** Have a real one ready. Good shapes:
the agent optimized the wrong objective because the instruction was ambiguous, or it produced
plausible output that a spot check caught, or it worked in testing and broke on real data
that did not match your assumptions. The recovery matters more than the failure.

---

### Topic 6 — Switching Between ChatGPT and Claude

**Headline:** I switch on the shape of the task, not on preference. Retrieval and quick
reasoning across company knowledge go to ChatGPT. Long multi-step execution that produces
artifacts goes to Claude Cowork.

**The decision rule, said cleanly:**

| Pull toward ChatGPT | Pull toward Claude Cowork |
| :--- | :--- |
| "What do we know about X" across connected apps, with citations | "Go do this whole thing" over many steps |
| Fast one-shot answers and everyday drafting | Output that must land as files or artifacts |
| Read-only retrieval where verification speed matters | Work that reads and writes across local files plus connected tools |
| Broad app ecosystem for lookup | Repeatable jobs packaged as skills or plugins |

**Then add the nuance that scores:** the honest tradeoff is autonomy versus supervision cost.
An agentic run that takes twenty minutes and touches files needs a reviewer at the end, so I
only spend that when the output is worth reviewing. For a question I will act on in ten
seconds, the agentic path is a worse tool.

**Do not trash either product.** The interviewer is screening for judgment, and vendor
loyalty reads as a lack of it.

---

## 5. Sound bites to land

Short lines, said with conviction, that a scoring model and a human reviewer both remember:

- "Handing someone a blank chat box is not a rollout."
- "Most resistance is risk management, not laziness."
- "Anything I do twice becomes a system."
- "Connectors inherit permissions, so bad access hygiene becomes an AI problem the day you
  connect it."
- "Without a verification loop, an agent is a faster way to be confidently wrong."
- "I have built the deterministic version and the agentic version, so I know which problems
  deserve which."

---

## 6. Gaps to close before interview day

Honest read on where the profile is thin for this specific screen:

- **Named daily use of ChatGPT Work and Claude Cowork specifically.** The master profile lists
  ChatGPT and Claude as tools and agentic AI as a competency, but it records no Cowork or
  company-knowledge usage. If that usage is real, it should be captured in the profile. If it
  is light, the fix is hours on the tools this week, not better phrasing.
- **A first-person multi-connector story with AI connectors on both ends.** The 180+ contact
  audit workflow is real and strong, and it is CRM automation. Run one genuine two-connector
  job before the interview (source in, analysis, output written back) so beat 4 of the
  walkthrough is something you did, not something you designed.
- **No adoption metric exists for an AI rollout.** The 94% partner retention at Birdeye is the
  closest true number and it is a SaaS adoption number, not an AI one. Use it with its scope
  attached, do not restyle it as an AI result.
- **Numbers still missing that would strengthen answers:** concurrent client load at Solenzo,
  training sessions delivered and people trained at Wix and Birdeye, Wix team size. All three
  are on the profile's open-gap list and all three would sharpen the adoption answer. Worth
  running `/excavate-profile` before the interview.

---

## 7. Two-day prep plan

**Day before:**
1. Run one real multi-connector job end to end. Write down the connectors, the failure, and
   the fix while it is fresh.
2. Rehearse the multi-connector walkthrough out loud, timed, twice. Then the adoption spine
   once.
3. Write the six headlines (one per topic) on paper. Headlines only. Do not script sentences,
   scripted delivery reads as scripted.

**Interview day:**
1. Quiet room, wired or stable connection, phone off, single monitor, every other tab closed.
2. Camera at eye level, look at the camera, keep notes out of frame or unused. Integrity is a
   gate.
3. First ten seconds of every answer is the headline. If you catch yourself preambling, stop
   and restate the headline.
4. If a question lands on something you have not done, say what you have done that is adjacent
   and what you would do. Zara probes claims, not gaps.

---

## Sources

- [micro1 AI interview guide](https://www.micro1.ai/ai-interview-guide) ·
  [micro1 interview questions](https://www.micro1.ai/interview-questions) ·
  [micro1 experts](https://www.micro1.ai/experts)
- [Zara AI Interview: What to Expect](https://aitrainer.work/guides/zara-ai-interview-guide) ·
  [micro1 review 2026](https://aitrainer.work/guides/micro1-review/)
- [Claude Cowork](https://www.anthropic.com/product/claude-cowork) ·
  [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork) ·
  [Cowork connectors list](https://pluginsforcowork.com/guides/cowork-connectors/)
- [OpenAI: company knowledge in ChatGPT](https://openai.com/index/introducing-company-knowledge/) ·
  [Company knowledge help doc](https://help.openai.com/en/articles/12628342-company-knowledge-in-chatgpt-business-enterprise-and-edu) ·
  [Apps/connectors in ChatGPT](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt)
