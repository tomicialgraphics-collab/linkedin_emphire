---
deliverable: comment
id: 2026-11-16_comment_jeongmin-lee_the-label-is-the-weak-part
date: 2026-11-16
audience: public
status: ready
approved: no
warm: no
time_checked: >-
  checked: 2026-11-16 22:39 WAT, read from the system clock before the first draft of this file.
profile_checked: >-
  Jeongmin Lee, a first-degree connection, OpenAI, Devin and Qwen developer ambassador, posting dense technical
  summaries of harness design. This post is two minutes old with no replies. It summarises Claude Code's Code Mode, the
  FrontierHarness comparison of 21 harnesses, Pi, Unharnessed and Alex Zhang's sPTC proposal, so the audience is people
  who will read the details rather than the headline. The comment answers the speculative-execution section and leaves
  the ranking alone.
thread: >-
  five claims: tool calls are one round trip each and the cost accumulates in context, code mode bundles calls into one
  program so results stay in code rather than the transcript, the code runs in a sandbox with permission rules and hooks
  applied per tool call plus a classifier over the whole block, lightweight harnesses win on cost and speed with
  unchanged success rates, and harnesses are converging on a single code-mode tool, with sPTC pre-running calls during
  generation and never pre-running tools with side effects.
premise_checked: >-
  checked: nothing in the comment disputes his figures and no number of his is recomputed. The claim that purity becomes
  a label the model sets follows from his own description, where the code decides what to call and permission checks run
  per call rather than per intent. The idempotency-key proposal is offered as a design, not as a result, and no claim is
  made about FrontierHarness, Pi, Unharnessed or Claude Code beyond what his summary states.
sources_read: >-
  blocked: no page opened. His post is the whole of the material. The FrontierHarness results, the Code Mode
  announcement and the sPTC proposal are all taken as he reports them, and the comment holds without any of the source
  links being followed.
---

## Comment, paste as is

<!-- gate:body:start -->
The speculative part is where I'd look. Don't pre-run tools with side effects is a correct rule that needs a pure-or-not label on every tool. In code mode that label is metadata the model sets inside a loop nobody reads before it runs.

The failure is quiet. A write gets executed speculatively, the generated code then calls the same write for real, and both report success. Nothing errors. You meet it as a record that exists twice.

There's a cheaper way than trusting the label: make the pre-run keyed rather than classified. Pre-run only calls that carry an idempotency key, and return the stored result when the real call arrives with it. A wrong guess then costs a wasted read instead of a second write, and the model never has to be right about purity.

That matters more as these runtimes get thinner. A single tool gives the model more freedom per step, so writes per second rise and every guess about side effects gets made more often.

<!-- gate:body:end -->

## Why the pre-run and not the five sections

The post is a good summary and summarising it back would be worthless to somebody who wrote it. His section on sPTC is the one place the design is still open, and it contains a rule that reads as solved and is not: do not pre-run tools with side effects.

That rule is a classification problem dressed as a prohibition. Somebody has to decide, per call, whether it has a side effect, and in a code-mode runtime that decision is made by the code the model generated. The permission layer he describes still checks each call, which is the right place for authorisation, but authorisation is not the same question as whether it is safe to run this twice.

## Why idempotency keys rather than better classification

Classification asks the model to be right about a property of a tool before it uses it, and a model that is wrong gets no feedback, because both executions succeed. Keying asks the runtime to recognise a repeat, which it can do mechanically.

It also degrades better. A wrong classification produces a duplicate write, which is expensive to find and sometimes impossible to unwind. A wrong pre-run under keying produces a wasted read and a stored value nothing asks for. The cost of being wrong drops from a correctness incident to a rounding error.

## What this is not

No link, no offer, no mention of engagements. He writes summaries for practitioners and ends with a follow invitation, so the comment earns its place by being useful on the one open design question rather than by competing with his closing.

Not a prediction that sPTC fails. The speculative approach is probably right, and this is the smallest change that makes it safe to run in front of a customer.

## If he replies

The question worth having is what happens to keys across a retry that follows a context compaction, because the same write can arrive with a re-derived key it no longer matches. That is the same shape of problem as a cache key changing when the prompt changes, and it usually surfaces as a duplicate a week after the runtime was declared correct.
