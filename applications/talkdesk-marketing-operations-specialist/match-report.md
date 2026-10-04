# Talkdesk — Marketing Operations Specialist

- **Company:** Talkdesk (CCaaS / customer experience automation)
- **Location:** Remote (US)
- **Pay:** $86,000-$144,000 OTE
- **Posted:** 09/25/2026 (window closes ~10 days after posting)
- **Evaluated:** 2026-10-04

## Application-Form and Eligibility Check

| Item | Classification | Status |
| :--- | :--- | :--- |
| Remote (US) work location | Application-form | Met (Arvada, CO, remote) |
| Work authorization | Application-form | Met (U.S. citizen) |
| Salary expectation (if asked) | Application-form | Josh is flexible. Suggested answer: **$105,000**, in the lower-middle of the posted range |
| 3-5 yrs B2B SaaS MOPs / RevOps / systems-adjacent | Resume-evidenced | Partial. Systems-adjacent across B2B SaaS roles; dedicated MOPs ownership is Solenzo (Feb 2024-present) |
| Required 200-word written answer | Application-form | Drafted, see below (197 words). Josh to review before submitting |

No failed eligibility items.

## Application Priority Score

```
[████████████████░░░░]  78%
```

**78 / 100 — Solid stretch** (top of band). Internal decision aid, not a prediction of any employer's system output. See `fit.png`.

| Dimension | Score |
| :--- | :--- |
| Must-have requirements met | 34 / 40 |
| Seniority & scope alignment | 12 / 15 |
| Domain / industry alignment | 10 / 15 |
| Differentiators / nice-to-haves | 13 / 15 |
| Evidence strength | 9 / 15 |

Provisional score before confirmations was 70. The confirmed API/webhook/LLM work, sync work, and lead-scoring definitions moved must-haves from 27 to 34.

## Requirement coverage (must-haves)

| Requirement | Coverage | Evidence |
| :--- | :--- | :--- |
| 3-5 yrs B2B SaaS MOPs/RevOps/systems-adjacent | Adjacent | Solenzo MOPs (2.5+ yrs, SMB clients); CRM field definitions (Wix); lead qualification system (Accelo); B2B SaaS sales/onboarding since 2017 |
| MAP + CRM admin incl. MAP-to-CRM syncs | Strong | GoHighLevel, HubSpot admin and syncs (Solenzo); Salesforce (Birdeye, Wix, Fivestars) |
| Automated workflow calling external APIs in production | Strong | Webhooks, REST, direct LLM API calls in Zapier/Make/n8n/GHL with Python/JS code steps |
| B2B funnel mechanics (MQL, lifecycle, attribution) | Strong | Lead scoring, qualification, lifecycle stages built for Solenzo; co-built Accelo lead qualification; campaign attribution and ROI/CAC/LTV reporting (Level) |
| Coaching non-technical stakeholders | Strong | Wix teams up to 30 (weekly training, 1:1 coaching); Birdeye partner training; prompt translation for clients |

**5 of 5 at Strong or Adjacent.**

## Top strengths

1. The agentic AI section describes work Josh already ships: a production scoring workflow on unstructured prospect signals that routes into personalized outreach (180+ enrolled).
2. Hands-on integration layer: webhooks, REST, LLM APIs, JSON, code steps.
3. Seat-side empathy: years as the BDR/AE the routing system serves, which is the angle of the cover letter.

## Gaps

- **Intent platform / ABM orchestration administration** (6sense, Demandbase, etc.). User-level exposure via Salesforce at Birdeye only. Named directly in the cover letter.
- **B2B SaaS MOPs at team scale.** Recent systems work is for small-business clients, not an in-house SaaS marketing team.
- **No MOPs metrics** (sync exception rate, speed-to-lead, MQL conversion).
- **Marketo admin.** Marketo use was a test at Fetch & Funnel; deliberately left off.

## Candidate confirmation needed

- **Which MAP-to-CRM sync pair.** Resume attributes it to Solenzo (GoHighLevel, HubSpot). Correct if it was something else.
- **Which intent/routing tools at Birdeye.** Resume says "ZoomInfo, intent, and routing data synced in." Know the platform names before the interview.

## Metrics needed

- Speed-to-lead or routing-time improvement on any Solenzo client build.
- Number of client CRMs/systems integrated at Solenzo.

## Required application answer (197 words)

I start where the lead was last seen. First, the form submission log in the marketing automation platform: did the record get created with a valid email and the fields routing depends on? Next, the MAP-to-CRM sync error log. Most lost demo requests die there, usually on a required CRM field the form doesn't populate, a picklist mismatch, or a duplicate rule blocking the insert. If the record did reach the CRM, I check the routing audit history: which rule fired, who it assigned, and whether that SDR was inactive or missing from the round robin.

I fix the root cause, then push test records through the edge cases (new contact, existing contact, existing account with a different owner) and confirm each lands with the right SDR. The fix goes in the routing change log, and I add an alert on sync exceptions so the next one surfaces before Sales notices.

For the agentic step, a webhook sends the form notes and firmographics to an LLM with a structured prompt that returns JSON: urgency, buying signals, and a reason. High urgency triggers priority routing and an instant SDR alert. Every score is logged and checked against conversion.

## Output files

- `Talkdesk-MarketingOpsSpecialist-Resume.pdf` / `.docx` (source: `resume.json`, modern style, 2 pages)
- `Talkdesk-MarketingOpsSpecialist-CoverLetter.pdf` / `.docx` (source: `cover-letter.json`, 1 page)
- `answer.txt` (required written answer)
- `fit.json` / `fit.png`
