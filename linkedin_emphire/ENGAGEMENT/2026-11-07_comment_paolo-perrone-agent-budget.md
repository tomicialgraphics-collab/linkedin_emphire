---
deliverable: comment
id: 2026-11-07_paolo-perrone-agent-budget
date: 2026-11-07
audience: public
status: ready
approved: no
warm: no
profile_checked: 2026-11-07 via substack.com/@paoloap, his O'Reilly author page and the newsletter itself. Paolo Perrone, The AI Engineer, 32K Substack subscribers and a stated million-plus engineers reading him across LinkedIn, Substack and Medium. Eight years shipping ML systems, writes for NVIDIA, Google and Y Combinator, publishes one piece of the AI stack a week. Audience is working engineers, so a comment earns its place only by adding a failure mode they can act on, not by agreeing with the list.
thread: his post on five agent mistakes that bleed budget, built on Andrew Ng's agent skills framework
---

# Comment on Paolo Perrone's five agent mistakes post, 7 November 2026

## What the post is

Five mistakes against Andrew Ng's framework: directing the workflow, enabling autonomy, reviewing the work,
customising the agent, understanding the foundations. Each with the wrong version and the right one, then a closing
question and a save prompt.

Every one of the five is a precondition for a session going well. None of them is what happens when the agent is
told no, which is the case that spends money with no chance of a return. That is the sixth, and it is not on the
list.

## Draft, paste as a comment

The five are preconditions. The sixth is what happens when the agent is told no.

A refusal and a failure look identical to most agents, so the agent retries. That retry burns tokens with no chance
of success, and it can run for hours before anyone notices, because the log says the call failed rather than the
call was refused.

Two changes fix it. The reply says refused, not failed, and names the rule it hit. The agent stops on refused and
escalates on failed. Cheap to add, and it is the only item on the list that stops a session paying for something
that was never allowed to happen.

## Why this shape

- Concedes the five in nine words. They are correct and a sixth version of them would be noise.
- Adds the one failure mode the framework does not cover, which is a request being denied rather than an execution
  going wrong. The audience is engineers running long sessions, and this is the case where the meter runs and the
  chance of success is zero.
- The fix is two sentences and costs nothing: distinguish the reply, and branch on it. Under a listicle, a
  mechanism has to be smaller than the list it is adding to.
- No link, no numbers of mine, no reference to any test of my own. Under a post read by a million engineers, a
  self-citation reads as a pitch and gets scrolled past.

## Posting notes

- Post soon. His posts fill fast and he is a curator, so he reads replies looking for something to quote later.
- If he replies asking how to tell refused from failed at the boundary, the useful answer is that the store or
  service has to say it, because a client cannot reliably infer a refusal from a status code. That is the point
  worth spending a second comment on.
- Nothing about clients, the benchmark or the review work in this thread.
