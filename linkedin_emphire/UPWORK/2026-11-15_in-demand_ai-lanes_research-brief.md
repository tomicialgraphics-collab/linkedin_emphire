---
deliverable: doc
id: 2026-11-15_upwork-in-demand-ai-lanes
date: 2026-11-15
time_checked: >-
  checked: 2026-11-15 10:12 WAT, read from the system clock in the sandbox before this file was opened for gate.
audience: internal
status: ready
approved: no
premise_checked: >-
  checked: the owner asked which AI red teaming, AI security, AI evaluation and AI integration work is actually in
  demand on Upwork, wants to explore talent profiles himself against keywords this file supplies, and will paste what
  those profiles look like. So this file has to do two jobs: hold what the platform and the indices say about demand,
  and give him search strings precise enough that two different searches return the same population. No number here is
  invented; each carries its source and its sample, and anything this side cannot verify is labelled as such.
sources_read: >-
  read: upwork.com hire pages for AI developers, AI automation engineers, AI consultants, AI integration developers,
  AI model integration specialists, AI compliance skills, security consultants, penetration testers, prompt engineers,
  software testers and load testing engineers, each checked on 15 November 2026 and each carrying the November 2026
  label; the OpenAI and Upwork joint report page and its figures as published 10 November 2026; UpHunt's index of
  3,515,581 public job posts and its 303,185-post role and rate study; Upwatcher's AI segment pages; CyberSN figures
  reported 20 October 2026. Blocked: upwork.com talent search results, which need a login, so no population counts,
  proposal counts or search-result sizes are claimed here.
---

# The four lanes: what Upwork is actually buying, 15 November 2026

This is the research half. The second half is yours: open talent search, paste the terms below, and send me what the
profiles look like. I will turn them into one comparison table and tell you which lane to lead with.

## How to read every number here

| label | meaning |
|---|---|
| **Primary** | read on an upwork.com page on 15 November 2026 |
| **Index** | a third party's scrape of public Upwork posts, with its own sample and method stated |
| **Report** | a joint Upwork report or a company release |
| **Inference** | mine, from the above, and marked every time |

Anything labelled Index is context for choosing a lane, not a price you can quote back to a client. The two things I
cannot see are the ones that decide individual jobs: how many proposals a given post has, and what the client has
actually paid before. That is what your pastes and the job page itself are for.

## The market, in five lines

1. **The feed shrank and the AI slice grew through it.** 1,185,547 posts in the first half of 2025 against 959,063 in
   the first half of 2026, down 19.1%, while posts mentioning AI rose 21.2%, 128,969 to 156,280. AI's share of new
   posts went from 9.03% in January 2025 to 20.11% in August 2026. (Index: UpHunt, 3,515,581 posts, January 2025 to
   August 2026.)
2. **AI work holds its price while general work loses its floor.** The median fixed budget is $100 across the platform
   and $158 on AI posts. The hourly median held at $30 for nineteen months, then printed $27 platform-wide in August
   2026 while AI stayed at $30. (Index, same source.)
3. **Bigger scope, not a bigger rate.** Fixed-price budgets on AI-related posts are 52.4% higher after controls,
   posted hourly rates 1.5% higher, and hired hourly contracts log 40.6% more hours in the first 90 days. (Report:
   OpenAI and Upwork, *The Rebundling of Freelance Work in the AI Age*, 10 November 2026.)
4. **The money is in the vendor's own books too.** AI-related gross services volume grew 22% year on year while total
   gross services volume fell 4% and active clients fell 4% to 763,000. (Report: Upwork Q2 2026 release, as cited by
   the index above.)
5. **Security work is the counter-cyclical slice.** Cybersecurity postings fell 26.4% January to September 2026 while
   AI security engineer postings rose 268.3% and cyber data scientist postings rose 203.5%. (Index: CyberSN figures
   reported 20 October 2026.)

Read together: the platform is not short of AI work, it is short of AI work that pays a premium for time. What pays
more is scope and outcome. That single fact should decide how you price all four lanes.

## Where the words moved, because the keywords are the product

Client vocabulary on Upwork rotated hard in a year. Mentions in public posts, first half 2025 against first half 2026:

| term | change | what it tells you |
|---|---|---|
| Claude Code | +8,162% | the tool name is now the request |
| Claude | +372% | same, at model level |
| vibe coding | +298% | build-it-fast work is a labelled category |
| MCP | +219% | tool and server plumbing is a request, not a detail |
| agentic | +175% | the buyer uses the word before you do |
| AI automation | +106% | biggest volume, lowest rate |
| ChatGPT | -13% | generic chat work is fading |
| fine-tuning | -58% | clients stopped paying for model surgery |
| GPT | -65% | as above |

(Index: UpHunt, same corpus.)

Two consequences for you. First, "MCP", "agentic" and "Claude" belong in your tags and your headline if you want to be
found by the buyer who is already using those words. Second, "fine-tuning" and "GPT" in a profile now read as 2024.

## The four lanes, one at a time

### Lane 1. AI red teaming

**What the buyer is buying.** A named attempt at breaking their model or agent, with reproduction steps, not a
checklist. The live posts use the words "safety risks", "reproducible", "automatically evaluated", "prompt injection",
"OWASP Top 10 for LLMs" and, in the security-adjacent ones, "garak or PyRIT".

**Rate evidence.** One live Upwork posting, "LLM Red Team Specialist, failure modes and edge cases", carries a client
range of $60 to $90 an hour. Another, "AI Red Team Engineer for LLMs", asks for offline reproducible test cases and
automated evaluation. (Primary, job pages as indexed by aggregators; ranges are what the client wrote, not what was
paid.)

**Competition.** Low supply at the top, wide supply at the bottom. Penetration testers who added "AI Security" and "AI
Red Teaming" to an existing VAPT profile are the common shape, and they sit at $30 to $42 an hour with 49 to 215 jobs
delivered. (Primary: featured profiles, 15 November 2026.)

**The shape of a winning profile here.** Certification plus a named method plus a deliverable. The strongest ones show
OSCP or CREST, then say which classes they test, then say what the client receives. Almost none show a rerunnable
artifact.

**Your opening.** You are the only one in this lane whose deliverable has a hash and a reproduction script. That is a
different claim from "I will test your model", and it is the one this lane has no supply of.

### Lane 2. AI security (defensive and governance)

**What the buyer is buying.** Three distinct things that share one keyword, and you should not treat them as one:

1. **Product security for AI features.** Threat modelling, guardrails, permission-aware retrieval, MCP runtime
   controls, prompt-injection defence in a shipped product.
2. **AI governance and compliance.** ISO 42001, NIST AI RMF, EU AI Act, AI usage policy, vendor review of AI tools.
3. **Fractional security leadership.** vCISO with an AI clause.

**Rate evidence, all Primary from featured profiles on 15 November 2026.** This lane has the widest spread of any of
the four:

| profile shape | rate | volume |
|---|---|---|
| vCISO plus ISO 42001 and AI GRC | $135/hr | 447 jobs, $1M+ earned |
| vCISO, AI security and governance for Claude deployments and MCP integrations | $165/hr | 14 jobs, $100K+ earned |
| ISO 42001 and SOC 2 consultant, AI compliance as a service | $16/hr | 184 jobs, $200K+ earned |
| AI engineer plus security architect, red teaming and governance | $20/hr | 2 jobs |

The spread is not explained by skill. It is explained by what is being sold: an audit-ready programme at $135 to $165,
or a compliance deliverable at $16 that is priced like piecework. Same keywords, different product.

**Your opening.** Your work is evidence, not attestation, so you cannot compete with a vCISO on certification and you
should not try. The opening is item 1, security review of a shipped AI feature with proof, sold to a company that
already has compliance and needs the technical half.

### Lane 3. AI evaluation, the lane with two markets inside it

This is the lane most likely to mislead you, so read the two rows together.

| segment | what it is | rate evidence |
|---|---|---|
| **Annotation and rubric grading** | grading model output against guidelines, often part-time, often via a staffing layer | median client range $15 to $30/hr on 712 "AI training / evaluation" posts, August to October 2026; 16.5% top out above $100 (Index: UpHunt, 303,185 posts) |
| **Evaluation engineering** | designing the eval, building the harness, writing the pass definition, automating it | live posts at $50 to $100/hr for "software engineer for AI model evaluation", and $115 to $150/hr for specialist AI response evaluators on a US-facing board |

Same word, a 4x to 6x difference in price, and the difference is entirely whether you own the method or execute
someone else's. One live Upwork post for evaluation engineering shows 20 to 50 proposals, 13 interviewing and 35
invites sent, which is a competitive post that is also actively pulling candidates in. (Primary.)

**What the buyer asks for, verbatim from live posts.** "Design realistic, multi-step coding tasks", "build tasks around
codebases, specs, architecture docs and datasets", "grade outputs against rubrics", "deterministic verifiers",
"eval environments that test whether AI agents behave safely".

**Your opening.** This is your existing thesis with a different noun. An eval you own, with a written pass definition
and a rerun on every model change, is the product. Never price this lane against the annotation median, and never use
the word "evaluation" in a headline without "harness" or "suite" beside it.

### Lane 4. AI integration

**What the buyer is buying.** Connect a model to something that already exists: an agent, a RAG pipeline, an MCP
server, a CRM, a voice stack. Titles in the wild: "AI agent developer", "AI integration developer", "AI automation
engineer", "senior LLM / AI agent architect".

**Rate evidence.** The featured pages on 15 November 2026 show this lane is the most crowded and the most price-spread:

| profile | rate | volume |
|---|---|---|
| AI engineer, agents, RAG, SaaS and automation | $12/hr | 138 jobs, $400K+ earned |
| AI engineer, LangGraph and RAG | $45/hr | 13 jobs, $100K+ earned |
| AI automation engineer, MCP servers and CRM | $99/hr | 2 jobs, $4K+ earned |
| AI integration developer, HIPAA-regulated healthcare | $65/hr | 7 jobs, $20K+ earned |
| AI model integration specialist | $25/hr | 106 jobs, $100K+ earned |

The index puts the median client range for "AI agent builder" at $15 to $35 and for "AI automation" at $15 to $30, with
only 7% to 8% of posts topping $100. (Index, UpHunt.)

**Competition.** The highest-volume lane and the one with the most proposals per hire. An independent index of 1.7
million posts reports AI integration drawing 27.5 proposals per hire, against 8.2 for paralegal work that pays more.
(Index: UpHunt, as quoted on its own blog.)

**Your opening.** Do not lead here. Integration work is real money at the $65 to $99 end, but you would be competing on
stack checklists against people with 138 jobs and $400K earned, and the median post is $15 to $35. Take integration
work when it arrives through a security or eval conversation, not as the headline.

## The keyword matrix

Two different searches, two different purposes. **Talent search** tells you what supply looks like and what they charge.
**Job search** tells you what demand looks like, with proposal counts attached.

### Lane 1, AI red teaming

| use | terms |
|---|---|
| Talent search | AI red teaming, AI red team, LLM red team, prompt injection, jailbreak testing, AI penetration testing, adversarial testing LLM, OWASP LLM Top 10, agentic red team, AI safety testing |
| Job search | AI red team, LLM red team, red team AI agent, prompt injection testing, jailbreak audit, AI security assessment, LLM penetration test |
| Skills seen on real profiles | AI Security, AI Red Teaming, LLM Security, Prompt Injection, Penetration Testing, OWASP, Garak, PyRIT, MITRE ATLAS |

### Lane 2, AI security and governance

| use | terms |
|---|---|
| Talent search | AI security, LLM security, AI security engineer, AI guardrails, MCP security, AI threat modeling, model security, AI governance, ISO 42001, NIST AI RMF, EU AI Act, AI risk assessment |
| Job search | AI security review, secure AI architecture, AI guardrails, prompt injection defense, MCP security review, AI governance, ISO 42001, AI Act readiness |
| Skills seen on real profiles | AI Security, AI Governance, AI Compliance, Security Engineering, ISO 42001, NIST AI RMF, DevSecOps, Cloud Security, Application Security |

### Lane 3, AI evaluation

| use | terms |
|---|---|
| Talent search | LLM evaluation, AI evaluation, eval harness, LLM-as-a-judge, model evaluation, benchmark authoring, rubric design, hallucination testing, RAG evaluation, golden dataset, regression testing LLM |
| Job search | AI model evaluation, LLM evaluation, eval environment, benchmark creation, evaluation framework, response evaluation, RAG accuracy testing |
| Skills seen on real profiles | AI Model Evaluation, LLM Testing, AI Response Evaluation, Hallucination Testing, RAG Testing, Model Testing, Test Case Design, Python |

Watch out: "AI training", "data annotation" and "evaluation" without a method word pull the $15 to $30 population. Add
harness, suite, benchmark or verifier to every query in this lane.

### Lane 4, AI integration

| use | terms |
|---|---|
| Talent search | AI integration, AI agent development, RAG, MCP server, LangGraph, CrewAI, n8n, OpenAI API, Claude API, voice AI agent, AI automation, CRM AI integration |
| Job search | AI integration, AI agent build, RAG pipeline, MCP server, AI automation, workflow automation AI, chatbot integration |
| Skills seen on real profiles | AI Agent Development, AI Automation, Retrieval Augmented Generation, MCP servers, Claude API, OpenAI API, n8n, Make.com, LangChain, LangGraph, Supabase, Next.js, Python |

### Cross-lane terms worth one search each

`agentic`, `MCP`, `Claude Code`, `vibe coding`, `AI code review`, `no AI policy`, `AI usage policy`, `AI incident`.
Those five to eight are the 2026 words; a profile that uses them is being found by the buyer who already thinks in them.

## Read this before using the matrix at 10:26 WAT

The owner ran the matrix and the results are in `UPWORK/2026-11-15_talent-paste-analysis_lane-choice.md`. Two things in this section are now known to be wrong in practice, and the analysis supersedes them:

1. **Boolean strings do not work in the talent search box.** `AND`, `OR`, parentheses and quoted phrases arrive as literal words, and the query collapses to a word soup that matches any AI profile. Use one plain phrase per search, in double quotes if the box accepts them.
2. **The page count is not a supply count.** `AI RED TEAMING` (2,771), `ai securiy` (2,141) and `AI EVALUATION` (6,171) are all fuzzy matches on `ai`; anything showing 10,001 is a capped ceiling. Read page-one composition instead, and take demand numbers from the job feed, where proposal counts are visible.

## What to paste, so the rows compare

For each profile, these ten fields. If a field is not visible, say so and I will record it as unseen rather than guess.

1. Headline, exactly as written.
2. Hourly rate.
3. Job Success score and badge, if shown.
4. Jobs completed and total earnings.
5. Country.
6. Member since.
7. The first three lines of the overview.
8. The skills block, all of it, or the first twelve if it is long.
9. Whether the profile names a deliverable (report, harness, suite, audit) or only skills.
10. Whether it shows an artifact a buyer can open: repo, sample report, published writing, certificate.

Also paste the search you used and how many results the page claimed, if it shows a count. That tells me whether a term
is thin or crowded, which is the thing I cannot see from here.

## Three ways these pastes can mislead us

**A high badge is not demand.** A $12/hr profile with 138 jobs and $400K earned is evidence of throughput at a price,
not of a market paying for expertise. Read earnings per job, not the badge.

**A stated rate is not a realised rate.** Every rate on this page is what a freelancer typed or a client wrote. The
OpenAI and Upwork report is the warning here: posted hourly rates barely differ between AI and non-AI work, 1.5% after
controls, while fixed budgets differ by half. Price the scope, not the hour.

**Keyword-stuffed headlines lie about skill.** Several top-ranked profiles in these lanes carry 40-word headlines that
are pure search bait. Useful to us anyway: it shows which words the market rewards, which is exactly what we want to
know.

## What I will do with what you send

1. Build one table, four lanes, every profile on the same ten fields.
2. Put your $65 against the lane median and the lane's top decile, and say plainly which lane your current rate is
   defensible in and which it is not.
3. Name the three highest-value gaps between your live profile and the profiles that win in the lane you choose, in the
   order of what to change first.
4. Recommend one lane to lead with for the $5,000 by 25 December target, with the reason and the price, not a list of
   options.

## What this research cannot support

The proposal counts and hire rates that would tell us the real chance per post live behind a login, and I have not
seen them. So nothing here says a given lane will convert for you. The lane recommendation will come after your
pastes, and it will be a judgement with the evidence named, not a forecast.
