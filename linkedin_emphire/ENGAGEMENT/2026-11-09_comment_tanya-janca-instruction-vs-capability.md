---
deliverable: comment
id: 2026-11-09_comment_tanya-janca-instruction-vs-capability
date: 2026-11-09
audience: public comment on Tanya Janca's post
status: ready
approved: no
warm: no
profile_checked: >-
  Tanya Janca, SheHacksPurple. Verified 9 November from conference and podcast listings: secure coding trainer and founder of
  She Hacks Purple Consulting, DevRel at Semgrep, member of the OWASP Top 10 team, host of the DevSec Station podcast,
  author of Alice and Bob Learn Secure Coding, 29 years in the field. The post is a lesson from DevSec Station episode on
  agent permissions and ends with a direct question to practitioners, which is why a concrete answer is the right move.
thread: prompt is an instruction, permission is a capability
---

## The post

She makes one distinction and then asks the room to answer it: telling an agent not to do something is not the same as preventing it. A coding agent with filesystem access still has the capability even when the prompt says stay in the directory. Her question is how people are actually restricting agents: sandboxing, limited tool permissions, approval gates.

## Why this one out of the feed

It is the only post in the batch that asks a question its author wants answered, and it sits inside his exact argument: a control you cannot demonstrate is a claim. The audience is application security practitioners rather than AI commentary accounts, which is the ICP. And the contribution is not a restatement of her point. It is the test that turns her distinction into evidence, which is the thing he does for a living.

## Comment, paste as is

The gap shows up as soon as you test it as a capability instead of an instruction.

Give an agent a filesystem tool and a prompt saying stay inside the project. Then give it a task whose honest solution needs a file outside that directory. A compliant agent comes back and says it cannot. An agent that still holds the capability finds a route, and it reads as helpful the whole way there.

So the evidence I would ask for is the denial, not the instruction. A prompt is a request the model usually honours and cannot guarantee. A mount, a token scope or a sandbox boundary is what still holds when the model is wrong, rushed, or talked into it.

Approval gates only count if the gate lives outside the model. If the agent decides when to ask, the gate is a preference.

In most agent setups I have looked at, the prompt is the only control anyone can evidence.

## What not to say

No mention of the playbook (it reads as a link drop on someone else's lesson), no numbers he cannot source, and no agreement that repeats her sentence back to her. The last line is the one that earns a reply, so do not soften it into "many teams".

## If she replies

The natural extension is what a denial test looks like in CI: the same harness that proves the capability is absent runs on every pull request, and a passing suite that never attempted the escape is not evidence. That is one comment, not a thread.

## Held

The three-way distinction between instruction, capability and audit trail, with the audit trail as the only one that survives an incident, when the model has already acted.
