---
deliverable: comment
id: 2026-11-13_comment_alok-sharan-llmops-pillars
date: 2026-11-13
audience: Alok Sharan, comment on his post listing the five pillars of LLMOps
status: ready
approved: no
warm: no
thread: what production observability does and does not measure about an LLM application
profile_checked: >-
  2026-11-13 from the post as pasted. Alok Sharan is a technology leader and architect working on AI and data
  transformation in fintech and has published a book of system design and behavioural interview material. The post is
  a teaching list: AI gateway, semantic cache, cost tracking, distributed tracing, fallback models, with the argument
  that a demo proves generation and production proves operation. It is written for engineers preparing for
  interviews, which is why the reply is allowed to be a quiet correction of the frame rather than a dispute.
premise_checked: >-
  opinion: the claim that these five instruments cannot see a wrong answer is structural rather than measured. A cache
  hit, a successful trace and a cheaper bill are all compatible with a confident, fluent, incorrect response, and that
  is visible from what each instrument records, not from a study.
sources_read: >-
  none: the post was pasted in full. Links inside it are a book and three regional purchase links and were not opened.
---

## Comment, paste as is

All five of these watch a request, and none of them watches the answer. A cache hit is fast, cheap and free of errors in every one of these views, and so is a confident response that happens to be wrong.

Two places I would put a check. A semantic cache keyed without the thing that differs, the date, the account, the current version of the policy, will return a fluent answer to somebody else's question, and the trace will call it a hit. And a fallback is a model change in the middle of a workflow. When it fires the dashboards stay green while the behaviour of the system has changed, because the second model was never evaluated on your inputs.

The number I would keep is not uptime. It is how often a response would have been wrong had a person read it, sampled from the traffic that actually ships.

## What not to say

No dispute of the five pillars, which are a fair teaching list and are all things a team should have. No mention of the book, no comment on the interview framing, no link, no hashtag, and no offer of evaluation work. The correction has to arrive as an addition to a list he built, or it reads as a competitor marking his homework.

## Why the slot is worth it

The post is aimed at engineers learning the stack, which means the frame it sets will be repeated in interviews and in design docs. One line under it, from someone who breaks these systems on purpose, is worth more there than a longer argument in a thread of people agreeing with each other.
