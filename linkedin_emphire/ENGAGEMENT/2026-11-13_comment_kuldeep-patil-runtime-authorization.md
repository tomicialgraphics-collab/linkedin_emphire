---
deliverable: comment
id: 2026-11-13_comment_kuldeep-patil-runtime-authorization
date: 2026-11-13
audience: Kuldeep Patil, comment on his post about authorisation before an AI agent acts
status: ready
approved: no
warm: no
thread: whether agent controls run before execution or after it
profile_checked: >-
  2026-11-13 from the post as pasted. Kuldeep Patil is the founder of InvisibleAct, an early stage company building
  runtime authorisation and enforcement for AI agents, and writes for enterprise security buyers. The post is a
  series of questions rather than a claim: whether an action is allowed, whether the permission still holds, whether
  approval is required, and whether anything changed since approval was given. He asks how companies handle it today,
  which is an invitation to answer with what is actually observed rather than with agreement.
premise_checked: >-
  opinion: the pattern described here comes from the probes I run on agent systems and is not a published figure. It
  is stated as what I keep finding, and bounded to that. Nothing in the reply asserts a rate, a vendor name or a
  measurement from someone else's data.
sources_read: >-
  none: the post was pasted in full and attaches no link, so there is nothing further to open.
---

## Comment, paste as is

In the probes I run, the failure is rarely the obviously forbidden action. An agent takes a permitted action with the wrong parameter: an amount rounded up, the same invoice twice, a payee one character off, a retention window stretched by a day. A gate that matches on action type passes all of it while looking like it is working.

The half of your question that costs money is the last one, whether anything changed since approval was given. An approval is granted against a set of facts. If the amount, the counterparty or the period moves before execution, most systems still honour the permission and not the facts it rested on. Re-checking the premise at execution is where I would put the weight, because that drift needs no attacker.

Take a block you shipped last month and ask a reviewer to say whether it was right. If they cannot tell a true block from a false one, teams widen the rule until everything passes, and the control has become a log with extra steps.

## What not to say

No agreement preamble, no restatement of his questions, no mention of what he is building beyond the general problem, and
nothing that reads as an offer to test it. He has not asked for help and a founder's post about his own product is not a
lead warm enough to pitch into. No hashtags and no link.

## Why the slot is worth it

He is early and asking publicly how enterprises handle this, which means the answers he gets will shape what he builds.
The comment gives him the failure mode that pre-execution gates lose to, the parameter rather than the action, and the
one measure that tells him the gate is real. It is a useful thing to have said in front of a founder whose buyers read
these threads, and it costs nothing to say.
