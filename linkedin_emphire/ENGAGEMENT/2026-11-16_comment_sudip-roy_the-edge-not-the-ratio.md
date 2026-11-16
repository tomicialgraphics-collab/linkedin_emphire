---
deliverable: comment
id: 2026-11-16_comment_sudip-roy_the-edge-not-the-ratio
date: 2026-11-16
audience: public
status: ready
approved: no
warm: no
time_checked: >-
  checked: 2026-11-16 21:50 WAT, read from the system clock before this file was written.
profile_checked: >-
  Sudip Roy, followed, cofounder and chief technology officer at Adaption, writing a technical account with numbers in
  it rather than a launch post. The post is ten minutes old at the time of the paste. The register is set by that: the
  comment argues with the measurement rather than restating the result, and takes every figure as his.
thread: >-
  FlashStates against vLLM on a coding-agent replay with GLM 5.3 Flash, two GPUs per server: the attention cache plus a
  snapshot of the recurrent state taken at the exact token where the turn ended, and eviction that drops a snapshot and
  its conversation together. At 24 agents the two servers agree, at 40 FlashStates is 20% ahead, and at 48 vLLM's
  output collapses, which is where the 3x comes from. 33 tokens read per one at the same load, and 14 to 28% more
  output across three models on an ordinary busy day.
premise_checked: >-
  checked: every figure in the comment, 24, 40, 48, 20%, 33 to 1 and 3x, is his, used as he states it, and none is
  recomputed. Nothing is claimed about Together AI, UIUC or UT Austin beyond his attribution, and no claim is made about
  the paper, which was not opened.
sources_read: >-
  blocked: no page was opened. The post is the whole of the material and the comment stands on it alone.
---

## Comment, paste as is

The 3x is a point on a curve, and the edge of that curve is the finding.

Everything before it is gain at a fixed load. At 24 agents the two servers agree, at 40 they're 20% apart, at 48 one of them falls off. The ratio at the top of the range is the least useful number here, because a burst arrives without a label telling you which point on the chart you're standing at.

What I'd want printed next to the throughput gain is the load at which output starts to fall, and how steep the fall is. Agents per gigabyte of cache, roughly. That number survives a change of replay and a change of GPU count, and it's the one that decides how much headroom to buy rather than how good the demo looks.

The other thing worth saying out loud: this failure never returns an error. The server keeps accepting work and producing less, so request rate looks healthy while latency climbs, then timeouts, then the incident review. A graceful degradation is a feature. A cliff is a cliff.

The 33 to 1 read amplification is the sentence I'd put first, though. It explains the fall in a way the speedup never can.

## Why the edge and not the speedup

He has done the hard part already: the numbers are there, the mechanism is explained, and the ordinary-day figure is given alongside the busy-day one, which almost nobody does. Restating the result would be noise.

What the post does not do is turn the result into something an operator can size against. A 3x ratio at one load point is a headline. The load at which a server starts to fall is a capacity number, and it is the one that survives a change of replay, of GPU, or of model, which is exactly what he argues will keep changing.

The read amplification point is the same argument one level down. It is a diagnostic that predicts the cliff rather than describing it, and it would sit better in the first line than the ratio does.

## The failure shape

This is the part worth saying under a post that is otherwise about throughput. The collapse is not slower responses or errors: the server keeps taking work and emitting less. On a request-rate graph it looks like the system is coping. The first evidence is latency, then timeouts, and by then the capacity decision is already wrong.

That is the same class of defect as an empty log read as nothing happened, applied to a serving stack: a signal that looks like health because nobody compared it to anything.

## What this is not

No link, no offer, and no mention of the owner's work. He is a chief technology officer publishing a technical result, and the only currency in that thread is a sharper read of it.

Not a dispute with his conclusion. Designing the model, the serving stack and the hardware together is right, and the comment gives him a way to report the result that makes the argument for him.

## If he replies

The question worth having is whether the edge moves with the inter-turn gap, because a replay with faster agents will find the cliff sooner or later depending on how much of the conversation changes between turns. That is the parameter that decides whether his ordinary-day figure holds in production.
