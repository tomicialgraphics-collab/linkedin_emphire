---
deliverable: dm
id: 2026-11-13_dm_kuldeep-patil-what-id-break-first
date: 2026-11-13
audience: client
status: ready
approved: yes
warm: yes
profile_checked: >-
  Kuldeep Patil, founder of InvisibleAct, building runtime authorization for AI agents. First degree. He read the comment
  left on his post, went to the profile, and wrote on 13 November at 15:21 asking what I would try to break first in a
  system that checks an agent's permission before execution. He is testing with a local n8n setup and simulated invoice
  actions, says he is early, and is asking what he might be missing. That is a real question from someone who can use the
  answer, not a networking line.
premise_checked: >-
  opinion: the four failure modes below come from probe work on agent systems, not from a published study, and they are
  written as things to test rather than as things known to be broken in his build. Nothing is claimed about InvisibleAct
  itself, which has not been tested here.
sources_read: >-
  none: the message arrived in full with no link. His post was read earlier on 13 November and the comment on it is in
  this repository.
---

## Message, paste as is

<!-- gate:body:start -->
Hi Kuldeep, thanks for writing, and that's a fair question to put to someone who breaks things for a living.

I'd start with the gate's inputs rather than the gate itself. Most of these systems read the action from metadata the
agent supplies, so the first thing I'd send is a request where the metadata and the effect disagree: a status update
that actually voids an invoice, a currency field that says one thing while the amount is in another unit, a negative or
rounded amount walking through a threshold. If it passes, the gate is checking a description rather than an action.

Next, approval binding. Get a legitimate approval, change one field before execution, and see whether the decision is
tied to the exact payload or just to the intent. Then replay the same approved request with a fresh id.

The one I'd expect to land is splitting. Eleven payments of 900 under a 1,000 threshold, each allowed on its own.
Almost nothing counts across a session, and an agent that is refused once will happily retry in smaller pieces.

And take the gate away. Kill the policy service mid-request and watch what the agent does next. A gate whose failure
posture is proceed is a log with a queue in front of it.

Your n8n simulation is the right place to run all four, because you can keep every decision. If it's useful, I'll run
them against your setup and tell you which ones land and what each one would cost to close.
<!-- gate:body:end -->

## What not to say

No congratulations on the company, no summary of his own pitch back to him, and no rates in this message. He asked one
question and the reply is the answer to it. Anything that reads like a proposal before he has seen whether the answer is
any good would turn a technical exchange into a sales thread.

## Why this is worth the slot

He is the second warm conversation in a week and the first from someone building the exact control I test. The offer at
the end is small and specific, which keeps it useful if he says yes and costs nothing if he does not.
