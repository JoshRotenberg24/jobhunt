# Interview Prep — micro1 AI Interview

**Role:** Workflow Annotator — Product Management & Marketing
**Format:** AI Interview (micro1 screens with its own AI recruiter) · up to 33 minutes
**Focus areas:** Driving Adoption · Daily Use of ChatGPT Work & Claude Cowork · Connectors · Multi-Connector Workflow Walkthrough · Power Usage of AI Agents · Switching Between ChatGPT and Claude

---

## 0. Read this first — the interview is not what the job posting said

The posting said "no prior experience in AI is required — your domain knowledge is what matters."
**The focus areas say the opposite.** Every one of the six is about hands-on, daily, power-user
fluency with ChatGPT and Claude — connectors, agents, multi-tool workflows.

Read that as: they are screening for someone who can *generate authentic AI-tool workflow data*,
not just marketing workflow data. The product management and marketing background is the
container; the AI tool fluency is the actual test.

**That's good news for you.** This is the strongest ground you have. But it changes what you
rehearse — do not walk in ready to talk about PRDs and campaign briefs.

### ⚠️ The one thing to verify before you go in

Your master profile lists **ChatGPT and Claude** as competencies, and this repo proves heavy
**Claude Code / Cowork** usage. It does **not** establish that you use:

- **ChatGPT Work** (the Business/Enterprise tier — company knowledge, admin-managed connectors)
- **ChatGPT connectors** specifically (Drive, SharePoint, Slack, GitHub, HubSpot)

**Be precise about which you actually use and at what tier.** An AI interviewer drills on
follow-ups — "which connectors do you have enabled?" / "walk me through a company-knowledge
query" — and a bluff collapses in one question. If you're on ChatGPT Plus rather than a Business
workspace, say so plainly and pivot to what you *do* run. Honest depth beats claimed breadth,
and it will score better than a hedge.

---

## 1. How to win an AI interview (tactics that are specific to this format)

An AI interviewer scores a **transcript against a rubric**. It has no rapport to win, no read on
your charm, and no benefit of the doubt. What it rewards:

| Do this | Why |
| :--- | :--- |
| **Name specific entities** — "Google Drive connector," "MCP," "subagent," "Claude Skill," "Notion" | Rubrics match on named tools and concepts. Generic phrasing ("AI tools," "automation platforms") scores near zero. |
| **Number your answers out loud** — "Three things. First… Second… Third…" | Structure survives transcription. It also stops you rambling. |
| **60–120 seconds per answer, then land it** | 6 focus areas ÷ 33 min ≈ 5 min each. Long answers cost you a whole topic. End with a clear stop so it asks the next question. |
| **One concrete instance per claim** | Every abstract statement gets a follow-up probe. Pre-empt it: claim → instance → outcome. |
| **Say the decision points out loud** | This role is literally about capturing decision points. Narrating "here's where I had to choose X over Y, because…" is you *doing the job* during the interview. |
| **Answer the question that was asked, first** | Don't open with context. Lead with the answer, then support it. |

What loses:
- Reading a script aloud — it flattens your delivery and the transcript reads canned.
- "It depends" without then picking.
- Filling silence. Stop talking when you're done; let it ask.
- Bluffing a tool. **"I haven't used X. The closest thing I've done is Y"** is a *scoring* answer, not a losing one — especially at an AI data lab where honest capability boundaries are the whole product.

**Have this file open on a second screen.** Reading a prep sheet is not cheating. Having Claude
generate live answers in another window *is* — and this company builds AI evaluations for a
living. Don't.

---

## 2. Your anchor story — the multi-connector walkthrough

**This is the centerpiece. Rehearse this once out loud before the call.**

They have an entire focus area called "Multi-Connector Workflow Walkthrough." You have a
genuinely unusual answer: **you built an agentic job-search system that runs inside Claude Code /
Cowork** — the very repo this prep lives in. It is real, it is running, and it hits every single
focus area at once.

Deliver it as discrete steps with the trigger, the tool, the decision point, and the output —
the exact structure micro1 wants annotators to produce. You are demonstrating the deliverable
while answering the question.

> **The 90-second version**
>
> "I'll walk you through a system I actually run. I built a job-search toolkit that lives in a
> GitHub repo and executes inside Claude Cowork. It's not a chat session — it's a workspace with
> custom skills, a source-of-truth file, deterministic scripts, and connectors.
>
> **Step 1 — Trigger.** I drop a job posting, URL or pasted text, into a session opened on the repo.
>
> **Step 2 — Skill invocation.** I call a custom skill I wrote, `/tailor-resume`. That's a folder
> of instructions plus supporting files that Claude loads on demand — a repeatable workflow, not
> a prompt I retype.
>
> **Step 3 — Retrieval + a decision point.** The skill fetches the posting. Career sites like
> Greenhouse and Workday block automated fetching, so I built an explicit fallback: if the fetch
> returns nothing real, stop and ask me to paste the description rather than hallucinate a job
> description. That's a designed failure mode, not an accident.
>
> **Step 4 — Grounding against a source of truth.** It reads `profile/master-profile.md`, a
> single file holding every true role, bullet, and verified metric. The skill's hard rule is that
> nothing may appear on the resume that isn't traceable to that file. That's my anti-hallucination
> constraint — the model selects and rephrases, it never invents.
>
> **Step 5 — Handing off to deterministic code.** It writes structured JSON, then a Python
> renderer turns that into a PDF and a DOCX. I deliberately do *not* let the model lay out the
> document. The renderer reports back page count and how full the last page is, and the skill
> iterates until it's two balanced pages. That's a measurable check the agent has to satisfy.
>
> **Step 6 — Connectors.** GitHub over MCP for version control — every application is committed
> and pushed, so I have a full history. Google Drive for pulling and storing documents.
>
> **Step 7 — Output.** A tailored resume, an honest fit score with a per-dimension breakdown, and
> a match report that names my gaps rather than hiding them.
>
> The part I'd emphasize: the hard problem wasn't prompting. It was deciding **which steps the
> model should own and which ones it shouldn't touch.**"

**Then stop.** That last line is the power-user signal, and it invites exactly the follow-up
you want.

### Follow-ups it will likely fire, and your answers

- **"How do you handle errors or bad output?"** → The fetch fallback. The page-fill check that
  forces iteration. The master-profile constraint. And the match report exists specifically so
  I can audit what the model claimed against what's true.
- **"How long did it take to build?"** → Answer honestly. Emphasize that it's *versioned and
  still evolving* — there's a roadmap in the README (Drive sync for the profile, an application
  status tracker).
- **"Who else uses it?"** → Be straight: it's mine. Then pivot — the same pattern (source-of-truth
  file + skill + deterministic renderer) is how I build client automations at Solenzo.
- **"What would you do differently?"** → Have a real answer ready. Something like: the fit-score
  rubric is still my judgment encoded as a prompt; I'd rather it were calibrated against outcomes
  — which roles actually converted to interviews. That's an honest, sophisticated critique.

### Backup story — the Solenzo client workflow

If they want something client-facing and business-flavored rather than personal tooling, use
this. It maps cleanly onto the "marketing workflow" the posting describes:

1. **Trigger** — a prospect enters the audit workflow (180+ contacts enrolled).
2. **Enrichment + scoring** — custom logic scores the business's digital footprint.
3. **Decision point** — the score routes the contact into one of three segmented campaigns:
   website visibility, missed calls, or low reviews.
4. **Generation** — hyper-personalized outreach drafted from that scoring, not a mail merge.
5. **Booking** — appointment scheduling with confirmations and reminders.
6. **Recovery branch** — no-show triggers a separate recovery sequence.
7. **Post-sale** — onboarding nurture, then long-term reactivation and review generation.
8. **Collaboration layer** — Slack, Google Docs, and Notion carry the human coordination; the
   CRM (GoHighLevel) is the system of record.

That's **20+ deployed workflows** in one system. Say the number.

---

## 3. Focus-area cheat sheet

### ① Driving Adoption

**What they're testing:** can you get *other people* to actually use these tools — or do you just
use them alone?

**Your true material:**
- **Wix** — helped build a brand-new vertical from proof-of-concept to a profitable business line;
  contributed to hiring, onboarding, and building **sales training for tenured account executives**.
  That last part is the good detail: teaching a new process to senior people who already thought
  they knew how to do the job.
- **Birdeye** — onboarded and managed **15–20 reseller partners**, drove rapid adoption of
  marketing automation, built **automated product-training sequences that reduced onboarding
  friction**, and retained all but one (**~94% retention**).
- **Accelo** — advised C-suite executives on CRM adoption and workflow design.
- **Solenzo** — get non-technical business owners to trust and adopt AI-driven systems.

**Your thesis (say something like this):**
> "Adoption fails when you lead with the tool. It works when you take one painful, repeated
> workflow off someone's plate, show them the finished output first, and only then explain how it
> got made. With the Birdeye partners I didn't train on features — I built the training sequence
> into the onboarding so they hit value before they had to learn anything. The AI version is the
> same: I don't tell a client 'we're using AI.' I hand them booked appointments."

**Trap:** don't describe adoption as a change-management framework. Give the specific resistant
person or team and what flipped them.

---

### ② Daily Use of ChatGPT Work & Claude Cowork

**What they're testing:** is this a daily habit with real texture, or a monthly novelty?

**Structure your answer as a day, not a list.** Something like: morning research and triage → mid-day
build/drafting → end-of-day documentation and follow-up. Name where each tool sits.

**Your genuine daily surface:**
- **Claude Cowork / Claude Code** — the job-search system in this repo, run as an actual workspace
  with custom skills. Also client-facing work: content drafting in a specific voice, agent and
  prompt construction, SEO and competitor research, structured documentation.
- **Custom skills you've written** — beyond `/tailor-resume` and `/find-roles`, you maintain a
  voice/writing skill and a LinkedIn content skill for Solenzo. **Say that you write your own
  skills.** Most candidates will say they "use ChatGPT a lot." Almost none will say they build
  reusable, versioned tooling on top of the model.
- **ChatGPT** — be specific and honest about tier and use. Research breadth, quick one-offs,
  image generation, voice, deep research.

**The differentiator line:**
> "The shift for me was going from prompting to *building*. I stopped retyping instructions and
> started writing skills — folders of instructions plus scripts that the model loads on demand.
> Once a workflow is a skill, it's versioned, it's repeatable, and it produces the same quality on
> a bad day as a good one."

**Trap:** "I use it for everything" is a non-answer. Give three named, recurring uses with the
frequency attached.

---

### ③ Connectors

**What they're testing:** do you know what a connector actually *is*, or do you just mean
copy-paste?

**Get the concept right first** — this is the highest-leverage 20 seconds in the interview:

> "Underneath most of this is **MCP — Model Context Protocol**. Anthropic open-sourced it, and
> OpenAI adopted it too, so it's become the common standard for how a model talks to an external
> system. A 'connector' is essentially a packaged MCP server for a specific app — it gives the
> model real, permissioned read and sometimes write access instead of me pasting context in."

That single paragraph separates you from ~90% of candidates.

**Connectors in your actual reach:** Google Drive, Gmail, Google Calendar, Slack, GitHub, Notion,
HubSpot, Linear, Asana, Jira, SharePoint/OneDrive, Box, Canva. *(Rosters change and differ by tier
— speak to the ones you personally have enabled, not the catalog.)*

**In this very session you are running a Google Drive connector and a GitHub MCP server.** That's
a live, checkable example — use it.

**The sophistication points to make:**
- **Permissions and scope matter.** A connector reads what the account it's authorized under can
  read. That's a real governance question in a work context, not a footnote.
- **Connectors change what you ask for.** With Drive connected you stop asking "summarize this
  doc I pasted" and start asking "find the three versions of this brief and tell me what changed."
- **Failure mode:** connectors are only as good as the underlying data hygiene. If the Drive is a
  swamp, retrieval is a swamp. You have a genuine data-hygiene background here — say so.

**The Power BI callback — use this one.** You have a pre-MCP version of this exact story, and it
plays extremely well because it shows the instinct predates the tooling:

> "I was doing a crude version of this back at Accelo in 2018. I'd build Power BI dashboards and
> show prospects what their reporting would look like once Accelo's API was syncing live data into
> it. That was the whole pitch — the data already existed, it was just trapped in a system where
> nobody looked at it. A connector is the same idea with the plumbing solved: instead of me wiring
> up an API to move data into a place a human reads it, the model reaches into the system directly.
> Same instinct, a decade of tooling later."

That answer does four things at once: names a BI tool, demonstrates API literacy, shows you
understand *why* connectors matter rather than just that they exist, and quietly establishes that
you've been doing systems integration since before it was easy.

**Trap:** don't recite a catalog of connectors you've never opened. Depth on three beats a list of twelve.

---

### ④ Multi-Connector Workflow Walkthrough

**Use the anchor story in §2.** Two rules:

1. **Narrate in discrete numbered steps** — trigger, tool, action, decision point, output.
2. **Call out the decision points explicitly.** "This is a decision point: if the fetch fails, the
   workflow stops and asks me rather than guessing." That is exactly the annotation skill they're
   hiring for, performed live.

If they push for a workflow crossing **Slack + Google Workspace + a data source** specifically —
the combination named in the posting — build it from true material:

> Slack thread where a client raises a performance question → pull the campaign performance data
> → cross-reference the shared Google Doc holding the strategy and the agreed KPIs → draft the
> recommendation → deliver it as a readout. At Level Agency that reporting framework tracked ROI,
> CAC, LTV, and conversion KPIs and ended in a QBR readout.

Keep the tools honest — say GA4, CRM dashboards, and **Power BI** (Accelo), all of which you've
used. **Don't say Snowflake, Looker, Tableau, or Amplitude.** You don't use them, and this
interviewer will ask a second question.

If the scenario they describe involves pulling metrics from a data warehouse, that's your cue for
the Power BI story — it's the closest true analog you have, and it's a strong one.

---

### ⑤ Power Usage of AI Agents

**What they're testing:** the gap between "chats with a bot" and "operates agents."

**Your power-user inventory — lead with these:**

| Signal | Your evidence |
| :--- | :--- |
| **Custom skills / slash commands** | You wrote `/tailor-resume` and `/find-roles`; plus a voice skill and a content skill for Solenzo |
| **Source-of-truth grounding** | `master-profile.md` as the single file every output must trace to |
| **Deterministic escape hatch** | Python renderers do layout; the model never lays out the document |
| **Measurable success criteria** | Renderer returns page count + last-page fill; the agent iterates until it passes |
| **Designed failure modes** | Fetch-fails-→-ask-the-human fallback instead of hallucinating |
| **Guardrails as policy** | "Never fabricate" is written into the skill, not hoped for |
| **Connectors / MCP** | GitHub MCP, Google Drive |
| **Version control on agent work** | Every application committed and pushed to a branch |
| **Evaluation loops** | Self-improving loops and eval frameworks monitoring agent output at Solenzo |
| **Multi-agent** | Breaking manual marketing workflows into agent architectures with custom logic |

**The line that lands:**
> "The naive version of agent work is 'give the model more autonomy.' The real skill is the
> opposite — deciding precisely where autonomy helps and where it hurts. In my resume tool, the
> model does judgment work: reading a job description, matching it to true experience, scoring
> fit. It does *not* do layout, and it does *not* get to invent a fact. Layout is a Python script.
> Facts come from one file. I get the model's judgment without inheriting its unreliability."

**Also strong:** the eval-loop point. At an AI data lab, "I build evaluation frameworks to monitor
agent outputs and catch failures" is speaking their native language — micro1's business is
*evaluating AI agents.*

**Trap:** don't claim you've deployed multi-agent systems at scale. You've built agent
architectures for marketing workflows. That's true and it's plenty.

---

### ⑥ Switching Between ChatGPT and Claude

**What they're testing:** do you have an *opinion*, formed from use? A diplomatic non-answer scores
badly. Pick, justify, concede the other's strength.

**Your framework — "I choose by failure mode, not by brand":**

| Use | Reach for | Why |
| :--- | :--- | :--- |
| Multi-step work over real files, repos, documents | **Claude (Cowork / Code)** | It's built to *do* the work, not describe it — and skills make workflows repeatable |
| Writing that must hold a specific voice | **Claude** | Better instruction-following over long documents in your experience |
| Anything needing a versioned, reusable workflow | **Claude** | Skills + MCP + file system |
| Broad research sweeps, current-events breadth | **ChatGPT** | Search and deep-research breadth |
| Image generation, voice, quick one-offs | **ChatGPT** | Modality coverage |
| An org already standardized on M365 or Google | **Whichever the org has** | Adoption beats preference — tie this back to focus area ① |

**The two lines to actually say:**
> "I don't switch by preference, I switch by failure mode. If the task is 'produce a finished,
> structured artifact with real constraints,' I'm in Claude. If it's 'go find out what's true
> across a lot of sources,' I'll start in ChatGPT."

> "And when the stakes are high I'll run the same prompt through both. Where they disagree is
> usually where the underlying question is genuinely ambiguous — that disagreement is a signal, and
> it's saved me from shipping confidently wrong work more than once."

That second line is the best answer you have for this focus area. It shows evaluation instinct,
which is literally micro1's product.

**Trap:** don't trash either one. And don't say "they're basically the same" — that's the answer of
someone who uses neither seriously.

---

## 4. Likely questions, with skeletons

| Question | Your 20-second skeleton |
| :--- | :--- |
| "Walk me through how you use AI in a typical day." | Morning research/triage → mid-day building (skills, agents, client automations) → end-of-day documentation. Three named tools, frequency attached. |
| "Describe a multi-step workflow using more than one connector." | **The anchor story, §2.** Numbered steps, decision points called out. |
| "What connectors do you use most?" | Name 3 you truly use. Explain what each *changed* about how you work. Then the MCP framing. |
| "How do you get a team to adopt AI tools?" | Output first, explanation second. Birdeye training sequences; Wix sales training for tenured AEs. |
| "ChatGPT or Claude?" | Failure-mode framework. Pick one for agentic work, concede the other's breadth. Then the "run both when stakes are high" line. |
| "What's the most complex thing you've automated?" | The 20+ workflow GoHighLevel system, or the 180+ contact audit workflow with scoring → routing → recovery branches. |
| "How do you know when the AI got it wrong?" | Verification: source-of-truth file, deterministic checks, eval loops, cross-model comparison. |
| "What can't AI do well in your work?" | Have a real answer. Suggested: it can't decide what's *worth* doing, and it will confidently fill a gap in the source data rather than flag it — which is why every system you build has an explicit "stop and ask" path. |
| "Tell me about a time an AI workflow failed." | Pick a genuine one. The career-site fetch blocking is a real, small, honest example — and it ends in a designed fallback. |
| "Why this role?" | You build the systems this training data teaches. You've spent two years turning vague human intent into instructions a model can execute reliably — this job is that skill, pointed at a bigger target. |
| "Any experience with annotation or data labeling?" | **"No."** Then: but I've spent two years on the consuming side of exactly this data — writing the instructions agents run on and evaluating where their outputs break down. |

---

## 5. Numbers and names to have on your tongue

**Verified metrics — use only these:**
- 15+ years across MarTech, SaaS, agency
- 5+ years building CRM and marketing automation
- 20+ GoHighLevel workflows built and deployed
- 180+ contacts enrolled in the automated audit workflow
- 15–20 Birdeye reseller partners · ~94% retention · $10K–$45K deals
- Wix: 30% traffic increase, 25% conversion improvement (e-commerce segment)
- 6 deals at Fetch & Funnel, ~$22K average, $130K+ total
- Accelo: ~$17,750/month implementation bookings (~$213K annualized)
- Accelo: Power BI dashboards demoed with API-synced platform data

**Terms to use precisely:** MCP (Model Context Protocol) · connector · skill · subagent ·
source of truth · decision point · failure mode · evaluation loop · deterministic vs. generative
steps · human-in-the-loop.

**Do NOT claim:** Snowflake · SQL · Looker · Tableau · Amplitude · authoring PRDs or roadmaps ·
annotation/labeling experience.
For every one of those, the script is: **"I haven't. The closest I've done is ___."**

**DO claim — added 2026-08-06:** **Power BI at Accelo.** You built and demonstrated Power BI
dashboards showing how Accelo's API could sync live platform data into a client's BI reporting.
That's a named BI tool with real API work behind it, and it closes the posting's analytics
nice-to-have outright. See the connector section (§3③) for the best way to deploy it.

---

## 6. Logistics — the 15 minutes before

- **Quiet room, wired headset, stable connection.** Voice AI transcription penalizes background
  noise and cross-talk, and a garbled transcript is scored as a weak answer.
- **Say the anchor story out loud once.** Once, not five times — you want it fluent, not recited.
- **This file open on a second screen.** §2, §3, and §5 are the live-reference sections.
- **Speak in complete sentences.** The transcript is the artifact being judged.
- **Pause fully at the end of each answer.** Turn-taking systems need a clean stop, and trailing off
  invites it to cut you off mid-thought.
- **Budget:** ~5 minutes per focus area. If you're 4 minutes into one topic, land it and stop.

**The single sentence to make sure you say before the 33 minutes are up:**

> "I don't just use these tools — I build reusable systems on top of them, and I design them
> around where the model *shouldn't* be trusted."

That's the sentence that separates you from every other candidate in the queue, and it's true.

---

## 7. Ask them something at the end

If given the chance, ask one question that signals you understand their business:

- "When a workflow submission gets rejected or sent back, what's the most common reason?"
  *(Shows you're thinking about the quality bar, not the volume.)*
- "Is the goal to capture how these workflows are done today, or how they'd ideally be done with
  an agent in the loop?" *(A genuinely sharp question about the data's purpose — and it's the
  ambiguity the posting's requirement #5 is asking you to flag.)*
