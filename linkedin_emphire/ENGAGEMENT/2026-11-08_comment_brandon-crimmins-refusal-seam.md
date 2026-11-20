---
deliverable: comment
id: 2026-11-08_brandon-crimmins-refusal-seam
date: 2026-11-08
audience: public
status: ready
approved: no
warm: no
profile_checked: 2026-11-08 from his headline only. Brandon Crimmins, enterprise AI strategy and transformation, working across Copilot, Salesforce AI, intelligent automation and process optimisation. LinkedIn returns 403 to fetch and a search turned up no independent profile, employer or published work, so nothing about him is asserted in the comment and the comment does not lean on his background. Third degree, no prior interaction.
thread: his post arguing that an agent can ace a demo and fail the first real exception, listing six things he wants before calling an agent production ready (access, context, freshness, grounding, recovery, traceability), and closing by asking what is the most overlooked challenge on the way from pilot to production
verified: nothing external is claimed. The six items are quoted from his own post, and the distinction between a refusal and a failure is a statement about systems rather than a claim about any named product.
---

# Comment on Brandon Crimmins's production readiness post, 8 November 2026

## Why this one

His list is good and his question at the end is genuine, which makes it the second post in the feed asking for an answer
rather than collecting agreement. Since he already has traceability in the list, the obvious comment, that refusals need
logging, is not available.

The opening is the seam instead. Two of his six items cover adjacent ground and neither covers the denial itself, which
means the gap can be named as a seventh item that belongs to him, not as a correction.

## Comment

The most overlooked one sits in the seam between two items on your list.

Access says the agent respects permissions. Recovery says it handles failed actions. Neither covers what happens when the
agent is refused, and those are different events with different correct behaviour.

A refused call must never enter the recovery path. An agent that retries, rephrases or finds another route after being told
no is escalating by persistence, and it will read as resilience in the logs, because the retry that works gets one line and
the denial gets another that nobody reads.

So the seventh item is Refusal. Named separately, logged separately, and never routed to recovery.

## What not to say

No praise paragraph before the point. No disagreement with the six, since they are sound and arguing about them would
waste the one thing worth saying. No mention of my own work, and no restating of his demo framing back at him.

## Held for a second turn

If he replies, the honest question is whether refusal belongs in his Recovery item or deserves its own, since a mature
system might treat both as denied actions with different retry policies. That is a real design argument and better as a
conversation than as a fourth paragraph in his thread.
