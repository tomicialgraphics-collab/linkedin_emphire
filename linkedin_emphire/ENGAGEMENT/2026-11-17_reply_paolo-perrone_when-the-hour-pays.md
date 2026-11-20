---
deliverable: comment
id: 2026-11-17_reply_paolo-perrone_when-the-hour-pays
date: 2026-11-17
audience: public
status: ready
approved: no
warm: yes
reply_to: >-
  Paolo Perrone, the author, following up on the reply about per-step tracking under his 16 November post. His question:
  for the slow steps, does the one-hour cache ever pay for itself.
time_checked: >-
  checked: 2026-11-17 00:38 WAT, read from the system clock before this file was written.
profile_checked: >-
  Paolo Perrone, the author, who has now asked two consecutive specific questions about method. He quotes a schema and
  moves straight to the next decision, so he wants arithmetic rather than opinion, and the reply gives the numbers with
  the band they hold in.
thread: >-
  the exchange so far: a token split is not a spend split, the useful split is cached against uncached, the tracking is
  per step with a prefix hash, and a gap between steps longer than the cache lifetime is a scheduling problem. His
  question is the natural next one, whether paying for the long cache is worth it on the steps that are slow.
premise_checked: >-
  checked: the multipliers are the ones read from two current prompt-cache cost tables earlier the same evening, 0.1x
  for a read, 1.25x for a five-minute write and 2x for a one-hour write. The arithmetic is done in prefix-units and
  stated in the reply so he can check it, and every break-even is derived rather than quoted. Nothing is claimed about
  his workload, his provider or his models.
sources_read: >-
  read: his two messages, the reply they follow, and the two prompt-cache cost tables fetched earlier in the evening.
  No page was opened for this reply and none is needed, because the calculation uses only the multipliers already
  checked.
---

## Comment, paste as is

<!-- gate:body:start -->
It does, and the arithmetic is short enough to do in your head. A one-hour write is 2x base input against 1.25x for the five-minute one, so it costs an extra 0.75 of the prefix, once.

Against a five-minute cache that keeps expiring on slow steps, that extra pays back on the next call in the hour. Ten calls spend 2 + 0.9 on the prefix, where ten misses in the short cache spend 12.5. Against no cache at all it needs a third call: 2 + 0.2 beats 3.

So the band where it earns is gaps between five minutes and an hour. Under five, the short cache is cheaper every time. Past an hour, neither one gets a read, you're paying a write on every call, and the short write is the cheaper of the two. That case is a scheduling problem wearing a caching hat.

Worth checking the multiplier for your model before committing, because the ratios above are the whole calculation and they're the one thing that moves.

<!-- gate:body:end -->

## The arithmetic, so it can be checked

Prefix of size P in base-input units. A read is 0.1P, a five-minute write 1.25P, a one-hour write 2P.

Ten calls spread across an hour, each more than five minutes after the last, so the short cache has always expired:

- short cache: 1.25 x 10 = 12.5P
- long cache: 2P then nine reads, so 2 + 0.9 = 2.9P
- no cache: 10P.

Break-even against the short cache is 2 + 0.1(n-1) = 1.25n, which solves at n just over 1.65, so the second call inside the hour pays for it. Against no cache it is 2 + 0.1(n-1) = n, which solves at 2.11, so three calls.

## Why the band rather than a yes

The honest answer depends on the gap distribution, not on the cache. A run whose steps are three minutes apart should never buy the hour; a run whose steps are twenty minutes apart should, from the second call.

And there is a case where the question has no good answer: once the gap passes the hour, nothing is being reused and the only difference is which write costs more. Saying that is more useful than recommending the expensive cache because slow feels like the problem it must solve.

## What this is not

Not a claim about his pipeline. He asked whether the hour ever pays, and the reply says when and refuses to generalise past the multipliers, which are the part that would need re-checking per model and per provider.

## If he replies

The question worth having is whether the gap is a property of the run or of the queue. If the slow steps are waiting on a shared worker pool, the fix is concurrency, and no cache setting survives that.
