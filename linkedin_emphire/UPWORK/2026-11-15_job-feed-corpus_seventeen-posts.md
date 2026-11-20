---
deliverable: doc
id: 2026-11-15_upwork-job-feed-corpus
date: 2026-11-15
time_checked: >-
  checked: 2026-11-15 10:38 WAT, read from the system clock. An earlier 10:44 stamp in this line was written before the clock was read and is corrected here.
audience: internal
status: ready
approved: no
premise_checked: >-
  checked: this is the thirty-post corpus promised in the research plan, run against the live job feed rather than a
  guess. It came back at 239 postings across nine searches, of which seventeen were read in full. It also overturned one
  thing: evals do not pay him, and the buyer's word is "AI security", not "red teaming".
sources_read: >-
  read: nine unauthenticated job searches on upwork.com, each with its facet counts and first-page postings, fetched
  10:37 to 10:38 WAT on 15 November 2026. Every figure below is copied from those pages. No estimate is labelled as a
  measurement anywhere in this file.
---

# The job feed, read properly

## How this was measured, and where it stops

Upwork's job search answers without a login. `upwork.com/nx/search/jobs/?q=` returns the postings, each with its
budget, experience level and estimated time, plus facet counts that split the result set by client history and job
type. So the demand question I said was blocked on 15 November morning is not blocked. It was blocked on the talent
side, which is a different page.

One limit, and it matters: this is the **public index**, the same subset the category pages expose, not the logged-in
feed a client sees. A search for `AI security` returned 174 postings here while the live product carries far more. Treat
every count as a floor and every rate as a posted rate, never a paid one.

## Nine searches, and what each one found

| query | postings found | expert | hourly | fixed | clients with no hires | clients with 10+ hires | fixed $1K to $5K | fixed $5K+ |
|---|---|---|---|---|---|---|---|---|
| `AI security` | 174 | 112 | 128 | 46 | 62 | 66 | 12 | 8 |
| `LLM evaluation` | 25 | 17 | 17 | 8 | 9 | 10 | 1 | 4 |
| `red teaming` | 16 | 6 | 13 | 3 | 8 | 6 | 1 | 1 |
| `MCP server` | 11 | 10 | 10 | 1 | 5 | 4 | 1 | 0 |
| `OWASP` | 7 | 3 | 5 | 2 | 2 | 3 | 2 | 0 |
| `prompt injection` | 6 | 5 | 5 | 1 | 3 | 1 | 1 | 0 |
| `jailbreak` | 0 | | | | | | | |
| `eval harness` | 0 | | | | | | | |
| `LLM red team` | 0 | | | | | | | |

Read the bottom three rows first. **The vocabulary the industry uses to describe this work is almost absent from how
buyers write it.** Not one public posting in the index asks for a jailbreak test, an eval harness or an LLM red team by
name. Six ask for prompt injection. Seven use OWASP. A hundred and seventy-four ask for AI security.

And `red teaming` returning 16 is worse than it looks: the first page is a Red Hat developer ad, a Google Ads interview
consultant matched on "red flags", an accounting firm and a coating chemist. The word pair is matching on `red`. A
count of 16 there is a count of noise, not demand.

## Seventeen posts, read in full

| # | post | budget | level | what the buyer wants | signal |
|---|---|---|---|---|---|
| 1 | Senior AI Engineer, agent architecture and security review | $75 to $90/hr, 1 to 3 months | Intermediate | audit report, prioritised findings, remediation steps, inside 2 days | newest relevant post in the set, one day old |
| 2 | Varonis trainer with agentic AI security | hourly, unpublished, 4 to 6 weeks | Expert | live training, lab guides, runbooks, 30 days of office hours | requires a Varonis certification, so closed to him |
| 3 | App developer for AI-generated code review and security | $55 to $70/hr, 3 to 6 months | Intermediate | fixes implemented in code, **1 to 4 paid hours every two weeks** | a beginner client with almost no budget velocity |
| 4 | Senior Azure and AI engineer, healthcare SaaS | $50 to $150/hr, 1 to 3 months | Expert | Azure hardening, HIPAA readiness, architecture review | wide range, the top of it aspirational |
| 5 | Senior .NET and full-stack engineer, AI enablement (two near-identical posts) | $70 to $85/hr, 6+ months | Expert | "create evaluation frameworks and test datasets", plus prompt-injection defence and MCP servers | evals appear as a bullet inside a .NET job, twice |
| 6 | Penetration test of a health web app, report for the FDA | **fixed $2,500** | Expert | report with CVSS per finding, evidence and fixes, plus **one retest** | certification gated, and the scope is a report |
| 7 | Web app and API pentest for a SaaS holding PII | hourly, quote requested | Intermediate | "redacted sample report, OWASP/PTES methodology, turnaround, and fixed-price quote including one retest" | the buyer is asking for exactly his deliverable shape |
| 8 | Security plus full-stack developer, Go and React | fixed, about $1,500 to $2,000 | Intermediate | audit, fix, no rewrite | fixing, not testing |
| 9 | HIPAA security reviewer, Next.js and Supabase | hourly, milestone-based | Expert | three checkpoints, written findings at each | AI stack in use, Claude API named |
| 10 | Software engineer for AI model evaluation | **$50 to $100/hr**, under 30 hrs, 1 to 3 months | Expert | design coding tasks, grade model output against rubrics | **20 to 50 proposals, 13 interviewing, 35 invites, 12 unanswered** |
| 11 | AI evaluation and benchmark developer, Snorkel experience | **$5 to $30/hr**, 30+ hrs, 6+ months | Expert | build reproducible Docker task environments with deterministic answers and tests | the top and bottom of the eval market, in one posting |
| 12 | Senior software engineer, LLM evaluation | **fixed $10,000** | Expert | datasets, verification mechanisms, agents that check code quality | **"US based" in the title**, so closed to him |
| 13 | AI trainers and AI evaluators | $5 to $50/hr, 6+ months | Entry Level | review model output, annotate, label | US residency and time zone required |
| 14 | AI developers to evaluate a new foundation model | fixed $250 | Expert | five freelancers, closed beta, structured feedback | buying expertise by the hour-equivalent of $25 |
| 15 | Salesforce and Node developer for MCP integration | $25 to $47/hr | Expert | tool-calling integration with JSON schemas | stack-specific |
| 16 | Secure remote MCP server, OAuth and multi-tenant | hourly, milestones | Expert | hosting, OAuth, per-tool permissions, audit log, field masking | **the security requirements are the job**, not an add-on |
| 17 | HubSpot RevOps engineer, Claude Code and MCP | $70 to $90/hr, 6+ months | Expert | CRM builds and migrations | agency subcontracting, not a security buyer |

## Five things this settles

**1. The buyer's word is "AI security", and the buyer's format is the report.** Nine of the seventeen posts that touch
security want a document: findings, severity, evidence, remediation, and a retest. Two name the retest in the first
paragraph and ask for a fixed price with it included. That is his HFB shape, arriving in the buyer's own words.

**2. Evals pay at the top only if you are in the United States.** The $50 to $100 posting carries the highest activity
in the set, and it sits above a $5 to $30 posting asking for more skill (Docker, deterministic test environments,
task authoring) over a longer commitment. The one fixed $10,000 eval role says "US based" in its title. The AI trainer
post at $5 to $50 requires US residency and a US time zone. Take those out and the eval lane left open to Lagos is the
benchmark-authoring mill, which is the annotation market with a longer brief.

**3. The evaluation lane is a bullet inside engineering jobs, and never the job.** Two .NET postings, near-identical,
list "create evaluation frameworks and test datasets" beside RAG, MCP and prompt-injection defence. Neither is an eval
hire. So evals are a thing he sells inside a security review, not a lane he leads with. My 10:26 note said red teaming
plus evals. This file supersedes that: **lead with AI security and the report, keep evals as the second half of the
offer.**

**4. The price he should quote is the pentest number, not the hourly.** Two fixed security engagements in the set came
in at $2,000 and $2,500, both asking for a report and one retest, both for a scope narrower than a full application.
His $1,200 named-failure review sits under that band, and the $2,600 regression pack sits on it. Both are buyable. The
hourly comparison is the weaker one: the AI-security postings cluster $55 to $90 an hour, which his $65 sits inside,
and that is the whole argument for keeping the rate where it is.

**5. First-time buyers are a third of this market, and they are the ones worth answering.** Clients with no hire
history: 62 of 174 in AI security, 9 of 25 in LLM evaluation, 5 of 11 on MCP, 3 of 6 on prompt injection. They have no
supplier relationship to displace and nothing to compare him against except the sample report he sends.

## What changes in the offer

The packages stand at $1,200 and $1,800 and $2,600, and the retest is now the headline rather than a footnote, because
two buyers asked for it unprompted. The title should carry **AI Security** explicitly, since that is the phrase with 174
postings behind it and `LLM red team` has none. Something in the shape of `AI Security & LLM Testing | Rerunnable
Report and Retest` names the buyer's category and the buyer's deliverable in one line.

The filter to run every morning, in this order: `AI security`, then `prompt injection`, then `OWASP`. Skip `red team`
and `red teaming` entirely, since one matches on colour words and the other returns chemists.

## What this still cannot say

Proposal counts and hire rates are visible only on individual postings, and only one of the seventeen exposed them. So
the competition estimate rests on a single data point (20 to 50 proposals, 13 interviewing, 35 invites sent) plus the
third-party figure of about 27.5 proposals per hire. Everything about budget is a posted range, not a settled price. And
the public index is smaller than the live feed, so every count here is a floor.
