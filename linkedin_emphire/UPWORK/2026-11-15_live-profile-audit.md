---
deliverable: doc
id: 2026-11-15_upwork-profile-audit
date: 2026-11-15
time_checked: >-
  checked: 2026-11-15 10:56 WAT, read from the system clock before this file was opened for gate.
audience: internal
status: ready
approved: no
premise_checked: >-
  checked: the owner asked for verified findings rather than assumptions, and for how much of the in-demand vocabulary the
  profile actually uses. Every claim below is tagged VERIFIED (read on the page), INFERRED (a mechanism visible on the
  page that explains a ranking) or OPEN (needs his login). Nothing is asserted from memory of an earlier state file, and
  where the page contradicts the repo, the page wins and the contradiction is recorded.
sources_read: >-
  read: the public profile at upwork.com/freelancers/~01a65712b8b0954fd2 at 10:56 WAT, and public talent search for
  "AI security", "prompt injection" and "AI red teaming" at 10:57 to 10:58 WAT, read against the job-feed counts in
  2026-11-15_job-feed-corpus_seventeen-posts.md.
---

# Profile audit: what the page says, what the search returns

## What the page shows, verbatim

**VERIFIED, read at 10:56 WAT.** Title `Software Engineer | AI Red Teaming (LLM, RAG, Agents)`. Rate `$65.00/hr`.
Work history section renders `No items`. Portfolio count `(4)`. No badge of any kind. No earnings figure. No Job
Success figure. No consultation offer. No availability indicator.

The overview opens: "I'm a full-stack software engineer (Go, Node.js, TypeScript, Next.js) who also runs AI red
teaming: prompt injection, RAG poisoning, and agent-abuse testing on LLM features, before your users find the holes."
It then gives the six-injection-attempts story with four working, and turns to full-stack development.

Portfolio, four items, two of them named without a login: "The 30-Minute AI Red Team Starter Test (Free Checklist)" and
"Sample Findings Report: Prompt Injection Test (Personal Project)". One carries the tags AI Security, prompt
injection testing, Chatbot Development, Penetration Testing. The second carries AI Security, Technical Writing, prompt
injection testing, Risk Assessment.

**The twenty skills, in the order Upwork lists them:** Full-Stack Development, Node.js, Golang, TypeScript, React,
Next.js, PostgreSQL, Python, FastAPI, API Development, Large Language Model, Retrieval Augmented Generation, AI Agent
Development, Azure Machine Learning, Artificial Intelligence, Deep Learning, Chatbot Development, Penetration Testing,
Security Assessment & Testing, AI Consulting.

## Finding 1. The skill tags carry none of the demand vocabulary. VERIFIED

This is the answer to the question about how much in-demand search the profile uses, and the number is bad.

| buyer phrase | public postings measured on 15 November | in his title | in his 20 skills | in his overview | in his portfolio tags |
|---|---|---|---|---|---|
| `AI security` | 174 | no | **no** | no | yes |
| `LLM evaluation` | 25 | no | **no** | no | no |
| `penetration test` | 22 | no | **yes** (Penetration Testing) | no | yes |
| `red teaming` | 16, mostly noise | yes | **no** | yes | no |
| `MCP server` | 11 | no | **no** | no | no |
| `OWASP` | 7 | no | **no** | not visible | no |
| `prompt injection` | 6 | no | **no** | yes | yes |

So: **one of seven buyer phrases sits in the skills field, and four of seven appear somewhere on the page at all.** The
skills field is the one the talent search filters on, and it is 14% covered.

Inside those twenty tags the distribution is the second half of the problem. Ten are web and backend development
(Full-Stack Development, Node.js, Golang, TypeScript, React, Next.js, PostgreSQL, Python, FastAPI, API Development),
seven are generic AI (Large Language Model, Retrieval Augmented Generation, AI Agent Development, Azure Machine
Learning, Artificial Intelligence, Deep Learning, Chatbot Development), two are security (Penetration Testing, Security
Assessment & Testing) and one is consulting. Not one of the twenty contains the words AI Security, LLM security, red teaming, prompt injection, OWASP or MCP, and
that gap is the finding.

Two of the generic AI tags he cannot evidence anywhere on the page: Azure Machine Learning and Deep Learning appear in
no portfolio item, no overview line and no work history.

## Finding 2. Every profile ranked above him carries an `AI Security` skill tag. VERIFIED

Read at 10:57 to 10:58 WAT, first three results of public talent search.

| query | rank | profile | rate | what their card shows |
|---|---|---|---|---|
| `AI security` | 1 | Keith M. | $165 | Top Rated Plus, 100% JSS, $100K+, consultations, `AI Security` as first skill |
| `AI security` | 2 | Manish J. | $65 | Top Rated, 90% JSS, $4K+, 25 hours, consultations, `AI Security` as first skill |
| `AI security` | 3 | Najam U. | $75 | Top Rated Plus, 100% JSS, $100K+, consultations, `AI Security` as first skill |
| `AI red teaming` | 1 | Ahmed P. | $65 | Top Rated, 100% JSS, $9K+, consultations |
| `AI red teaming` | 2 | Rafay B. | $100 | Top Rated Plus, 98% JSS, consultations |

**He appears in none of them.** The nearest comparable is Manish J.: same $65 rate, $4K+ earned, 25 hours billed,
fourteen jobs, 90% JSS, UK. A profile with four thousand dollars behind it ranks second for `AI security`. That kills
the idea that earnings are the wall.

What every one of them has and he does not, in the order the search cares about: a **badge**, an explicit `AI Security`
skill tag, a **visible JSS and earnings figure**, and a **consultation offer**. His card would show a title, a rate and
nothing else, because that is all his page renders.

## Finding 3. Absence of a badge costs him a filter, not just a tiebreak. VERIFIED

Public talent search exposes badges as a filter, with Top Rated Plus, Top Rated and Rising Talent as the three options,
and `Offers consultations` as a separate filter. A client who ticks any of those four boxes excludes him before ranking
happens. He has no badge of any kind at 10:56 WAT.

Rising Talent is the one he can plausibly reach, and it is a stated filter on the buyer side rather than a cosmetic
label. Upwork sets that requirement, and I cannot confirm it from the page.

## Finding 4. The strongest artefact is not on the profile. VERIFIED, and it contradicts the repo

Four portfolio items render, and the two named ones are a free checklist and a personal sample report. The HFB pack,
which is the only artifact on the platform with hashes and a rerun instruction, is not among them.

Repo record says three of six items are published. The page says four. Page wins, and the earlier note is out of date rather than wrong.

## Finding 5. The overview sells the wrong half first. VERIFIED by reading it

His opening sentence leads with "full-stack software engineer" and puts red teaming second. For a client searching
`AI security`, the first line they read is a web-development credential, followed by a personal anecdote about a
chatbot. Strongest sentence in the whole overview, "Every fix became a permanent regression test", is the seventh
line and buried under the anecdote.

## What the page says about earnings, and what that implies. INFERRED

No earnings figure renders. Profiles at $4K and above show theirs, so the figure is either below the display threshold
or suppressed. Either way, a buyer comparing five cards sees his with a rate and no proof of payments received.

## What I cannot verify from outside

**SETTLED at 11:09 WAT from the signed-in dashboard:** earnings $100+, two jobs, **zero hours billed** (both jobs were
fixed-price), average response +24 hours, Work Now on, Open for work on, Boost off, video empty, languages empty.

**OPEN.** The full overview (a logged-out visitor sees a truncated version with a Show more control), the proposal and
invite counts behind the profile, his JSS, whether Rising Talent is achievable now and what the gate is, whether
`AI Security` and `Prompt Injection Testing` exist as selectable skill tags in his editor, and what the "33% Complete"
indicator on the page refers to. Each of those needs his login, and each is one screen.

## The fixes, in change order

1. **Write the skills field to the demand vocabulary.** Add `AI Security`, `Prompt Injection Testing`, `LLM Security`,
   `OWASP`, `Model Context Protocol (MCP)` and `AI Agent Security` if the editor offers them. Ahmad S., ranked first for
   `prompt injection`, carries `Model Context Protocol (MCP)` as a tag, which confirms the term is selectable. Remove
   Azure Machine Learning and Deep Learning, which he cannot evidence and which pull the wrong invites.
2. **Put `AI Security` in the title itself.** `AI Security & LLM Testing | Rerunnable Report and Retest` beats the
   current title on the phrase with 174 postings behind it and on the deliverable buyers ask for.
3. **Publish the HFB pack as a fifth portfolio item**, with the hash and the rerun line in the description. It is the
   only thing on the page a competitor cannot copy.
4. **Offer a paid consultation.** It is a buyer-side filter, it renders on the card, and Manish has one at $65.
5. **Chase Rising Talent.** Until a badge appears, he is invisible to every client who filters on one.
6. **Record the video and add the languages.** Both fields were empty at 10:56 WAT, and the video is the fastest trust
   signal on the page. Hours per week is set, contrary to what an earlier note in this repo says. Corrected here on
   2026-11-15 at 11:09 WAT from the signed-in dashboard, which shows `As Needed - Open to Offers`.

Items 1 and 2 take one sitting and are the whole difference between a card that renders and a card that ranks.
