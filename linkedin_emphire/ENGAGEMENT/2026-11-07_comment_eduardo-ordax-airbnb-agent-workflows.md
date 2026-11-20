---
deliverable: comment
id: 2026-11-07_eduardo-ordax-airbnb-agent-workflows
date: 2026-11-07
audience: public
status: ready
approved: no
warm: no
profile_checked: 2026-11-07 via his X account, a Mirelo product post and a conference listing from his AWS period. Eduardo Ordax, founding GTM at Mirelo, previously generative AI lead at AWS, 250k-plus LinkedIn followers, advisor and public speaker, Spanish and English. He amplifies posts and quotes lines back at people, so the comment has to contain one sentence he can lift rather than a paragraph he has to summarise.
thread: his post on the two Airbnb engineers describing how agents are used in production, including the adoption percentages and the auditable data-exploration tooling
---

# Comment on Eduardo Ordax's Airbnb agents post, 7 November 2026

## What the post reports

Two Airbnb senior staff engineers on agents in production: over 97 per cent of weekly PR authors use agentic AI,
around 64 per cent of weekly pull requests are authored or assisted by agents, and adoption has moved into product,
design, finance and operations. The workflows named are background agents in containers, agents triaging monitoring
alerts and flaky incidents, and specialised tooling that encodes scientific methodology so data exploration is
reproducible and auditable.

The percentages are adoption. The tooling sentence is the one with a claim in it that can be tested, and it is
where a comment can add something without arguing with his summary.

## Draft, paste as a comment

The 64 per cent is the number I would sit with. It moves the constraint from writing code to reviewing it, and that
is exactly the volume at which review quietly becomes signature.

The line I would look at hardest is the tooling that makes data exploration reproducible and auditable. Those are
two different claims. Reproducible means same inputs, same steps, same output. Auditable needs one more thing: a
record of what the agent considered and did not do. A run that never tried the alternative leaves no trace of the
decision, and reproducibility will faithfully reproduce the blind spot.

Adoption tells you how many people are using agents. It does not tell you how many of those runs can be defended a
year later.

## Why this shape

- Answers the post on its own terms and takes the number he led with. He quotes lines back at people, so the first
  sentence is built to be quoted.
- Separates two words his source used together, reproducible and auditable, because they are not the same guarantee
  and the difference is checkable. That is the only kind of distinction worth making in someone else's summary.
- The closing pair is the whole argument in two sentences and needs no jargon, which matters for an audience this
  broad.
- No link, no numbers of mine, no reference to any test I have run.

## Posting notes

- Post soon. His posts travel and the comments under them are read by people who do not read the source thread.
- If someone says reproducible pipelines do capture the alternatives, the useful reply is that they capture what
  ran, not what was rejected, and the rejected branch is usually the decision.
- Nothing about clients, the benchmark or the review work here.
