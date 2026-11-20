---
deliverable: doc
id: 2026-11-13_upwork-channel-loop
date: 2026-11-13
audience: internal
status: ready
approved: no
---

# The Upwork channel, wired to LinkedIn

What the pasted screenshots on 13 November actually say, what is broken, and the loop that makes the two channels feed each
other instead of competing for the same hours.

## The reading, from the paste

| Thing | Value on 13 November | What it means |
|---|---|---|
| Headline | Software Engineer, AI Red Teaming (LLM, RAG, Agents) | Correct. No change needed. |
| Rate | $65/hr | Correct for the positioning, and it is not the constraint. |
| Earnings | $100+, 2 jobs, both in progress | Two contracts open, neither closed, so no review exists yet. |
| Total hours | blank | Either the hours are not logged or the contracts are flat-fee. Worth checking, because blank reads as zero. |
| Job Success Score | none | There is no score until a contract closes. This is the single most costly fact in the paste. |
| Proposals, last 7 days | 0 sent, 0 viewed, 0 interviews | Nothing has entered the market. The channel is not underperforming, it is idle. |
| Connects | 84, 0 earned this month | 84 connects is roughly 7 proposals at 12 each. Budget, not a tap. |
| Catalog | 2 projects approved, 5 and 6 views in 30 days, 0 orders | The catalog is a price list, not a lead source at this traffic. |
| Consultation | 1 approved, 0 views in 30 days | Same. |
| Portfolio | 4 items live, reorder screen open | Two of the four are the right proof. The ordering matters less than what is attached to proposals. |
| Open for work | On, Work now On, Boost Off | Correct. Boosting would burn the scarcest resource for impressions that do not convert at this size. |

The diagnosis is narrow. The profile is not the problem, the prices are not the problem, and the catalog is not the
problem. Zero proposals in seven days is the problem, and the missing review is the reason a proposal has nothing to
stand on.

## The arithmetic, before any ambition

- 84 connects divided by about 12 per proposal is **7 proposals**, and connects regenerate slowly (0 earned this month).
- The plan in `STRATEGY/2026-11-12_revenue-5000-by-25-dec.md` asks for 8 a week. The connects on hand do not cover one
  week at that rate, so **the quota is not the number to chase. Hit rate is.**
- At $5,000 across 43 days, one Upwork job at $600 removes twelve percent of the gap. Seven well-aimed proposals are a
  better use of 84 connects than fourteen scattershot ones.
- Every proposal should therefore be aimed at a job whose budget is **$600 or more**, with the $150 scan offered as the
  way in only where a client has already asked a small question.

## The loop: one artefact, two channels

The two systems already produce the same goods. What is missing is the wiring, so each week's LinkedIn output lands in
Upwork's attachments and each Upwork job comes back out as a LinkedIn post.

| Asset | Where it already lives | What it does on Upwork |
|---|---|---|
| Case study v5, the ten-day review, named and cleared | `CLIENTS/foray-dunin7/_v5_2026-11-13.pdf` | The attachment for any full review proposal. It is cleared for public release, so it can be sent without a permission conversation. |
| Sample findings report, six attempts and four breaks | `UPWORK/sample_findings_report.md` | The attachment for a scan or a small review. Already written, already his own system. |
| The AI Red Team Playbook | `github.com/Teamthy/Ai-Red-Team-Playbook` | Answer to "how do you test", and it is public, so no confidentiality question. Attach the repo name in the message body only if the client asks for method. |
| Post 34, the verifier that exits 0 | `VERIFIED_POSTS/2026-11-13_exit-zero-never-checked` | The argument for why verification is a separate discipline from testing. Quote one line in a proposal, never a link. |
| The host-failure benchmark, nineteen modes and an open defect register | repository | The proof for engineering-heavy builds, where the client cares that code is tested rather than that a report exists. |

Rules for the wiring:

1. **No external links in a proposal body.** Upwork reads them as steering off platform. Say "I can send the sample as an
   attachment" and attach it.
2. **One artefact per proposal.** A client who receives three attachments reads none of them.
3. **The LinkedIn post never mentions Upwork, and the proposal never mentions LinkedIn by URL.** Same thesis, two doors.
4. **The return leg:** once a job is under way, the anonymised lesson is a LinkedIn post. No client name, no system detail,
   no outcome that identifies them. This is the only mechanism that makes the two channels compound rather than duplicate.

## The four jobs worth 84 connects

| Archetype | What it looks like in the job feed | Tier to quote | Why it wins |
|---|---|---|---|
| Pre-launch test | "We are shipping an AI feature in three weeks and need someone to try to break it" | Red team, Standard $600, sometimes Advanced $1,500 | The scope is a week, the deliverable is a report, and the case study is the proof. |
| Something already went wrong | "Our chatbot said something it should not have" or a mention of prompt injection in the brief | Standard $600, priced as a scan plus findings | Urgency shortens the sales cycle. Quote the scan, deliver in three days, sell the fix loop after. |
| Build with testing inside | "Build a RAG chatbot" with any mention of security, compliance or production | Chatbot, Standard $900 or Advanced $2,500 | The differentiator is that the same person builds and breaks it. No other applicant says that. |
| Compliance or governance review | SOC 2, GDPR, an AI policy, a pre-audit check | Red team, Advanced $1,500 | The report format matches what an auditor asks for. The client is buying a document, not a scan. |

Skip: anything under $250, anything hourly at $15 to $25, anything asking for a tool the record has never used (MCP servers,
Kubernetes at scale), anything that asks for a test on a system he cannot access, and anything where the brief is a single
line with no scope, because those are the jobs that turn into unpaid scoping.

## The lever nobody has pulled: close a contract

There is no Job Success Score because no contract has closed. Both jobs are in progress. Until one closes with a review,
every proposal is asking a stranger to be the first, and `Rising talent` stays out of reach.

So the highest-value Upwork action this week is not a proposal. It is finishing the work already sold and asking, once, in
plain words, for the contract to be closed and for feedback if the work earned it. That is allowed, it is normal, and it
converts an open contract into the only asset Upwork's algorithm actually reads.

## The week, hour by hour, without touching the LinkedIn slots

The LinkedIn posts go at 09:00 and 21:00 WAT, and the case study work fills the middle. The Upwork block fits inside the
morning without moving anything.

| Day | Upwork block, 45 minutes | Output |
|---|---|---|
| Saturday 14 November | Read 20 jobs in the saved searches, shortlist 4, send 2 | 2 proposals, register rows |
| Sunday 15 November | Answer any reply within the hour, send 1 more | 3 total |
| Monday 17 November | Send 2, chase the two open contracts for closure | 5 total |
| Tuesday 18 November | Send 1, follow up on the oldest unanswered proposal once | 6 total |
| Wednesday 19 November | Send 1, update `connects.txt`, run `./emphire upwork` | 7 total, connects at zero |

Seven proposals is the whole connect budget. If the hit rate is nil after seven, the fix is not more proposals, it is the
targeting, and the register will show which archetype answered.

## Measuring it

- `./emphire upwork` reads `UPWORK/PROPOSALS/` and `UPWORK/connects.txt` and prints proposals sent, quota, connects left,
  and what the balance buys. Run it before the block, not after.
- `./emphire revenue` is still the only place money counts. A job that is agreed becomes a row in `STATE/REVENUE-LOG.md`,
  and a job that is not a row is not money, however good the conversation was.
- Weekly, on Sunday: proposals sent, replies, interviews, and one sentence on which archetype drew the reply. That
  sentence is the only thing that should change next week's targeting.

## What not to do

- **Do not boost.** 84 connects spent on impressions cannot buy a proposal.
- **Do not drop the catalog prices.** $150 is the way in for a client who is unsure, and it is a third of a day. The
  catalog is not the lead source; it is the price list a proposal points at.
- **Do not open a second account**, do not put contact details anywhere, and do not take payment outside escrow. The 10
  percent buys the buyer protection and the review that this account needs.
- **Do not send a proposal without an attachment** once a client has asked for proof. The case study is the reason this
  account can quote $600 on job seven.
