---
deliverable: comment
id: 2026-11-16_comment_paolo-perrone_the-multiplier-not-the-percentage
date: 2026-11-16
audience: public
status: ready
approved: no
warm: no
time_checked: >-
  checked: 2026-11-16 22:16 WAT, read from the system clock before the first draft of this file.
profile_checked: >-
  Paolo Perrone, followed, writes Shipping Production AI on Substack and describes it as read by a million engineers.
  The post is five minutes old and carries no comments. It is a numbers post with a save-this call to action, so the
  people it attracts will be quoting the percentages back at him. The comment does not restate any of them.
thread: >-
  across 1,127 agent runs the token split was 52.1% context re-reads, 21.3% new input, 15.8% output, 7.4% tool fees
  and 3.4% wasted retries, and his conclusion is that an agent without KV prefix caching and context pruning is an
  expensive re-read loop rather than an autonomous engineer.
premise_checked: >-
  checked: the pricing multipliers were read from two current Anthropic prompt-cache cost tables before the text was
  fixed (a read at 0.1x base input on most models, a write at 1.25x for the five-minute cache and 2x for the
  one-hour one). The post's own five percentages are quoted, not recomputed, because the run breakdown is his. No
  claim is made about his subscribers, his customers or his own pipeline.
sources_read: >-
  read: two Anthropic prompt-caching cost tables, both current in November 2026, agreeing on the read multiplier of
  0.1x base input and the write multipliers of 1.25x and 2x. That is the whole of the research. The post is the rest
  of the material, and the comment does not depend on any other page.
---

## Comment, paste as is

52.1% of tokens comes off a log. 52.1% of spend needs a price per token type, and cached input isn't priced like fresh input: a read is often a tenth of the input rate, a write is 1.25x for five minutes or 2x for an hour. Those multipliers pull the invoice in opposite directions, so that half can be the cheapest line on it or the sign of a prefix that never settles.

The split that decides what you do next is cached against uncached. If most of it is hitting cache, you're looking at your prompt structure, not a cost problem, and the money is elsewhere. If it isn't, the prefix is changing near the front every step and you're paying the write premium to cache what you never reuse.

The bill I'd watch harder is the window, because that one doesn't take the discount. You see cost monthly. You see the window the afternoon the agent forgets the middle of its history and answers confidently about a file it read forty steps ago.

## Why the unit and not the percentages

The five figures are well measured and the conclusion is right, so repeating either adds nothing. The one thing the post does not do is convert tokens into money, and it cannot, because the conversion depends on which of those re-read tokens were served from a prefix cache and which were written to one.

That distinction is not pedantry. A cache read and a cache write sit on opposite sides of the base input price, so an identical token breakdown can describe a pipeline paying well under its apparent rate or one paying a premium on every step because the prefix moves. Same chart, opposite advice.

## The write premium, which is the part people miss

Caching is usually described as a discount, which is only true of the read. The write costs more than plain input and the multiplier depends on how long the cache lives. An agent whose system prompt, tool schemas or file layout changes near the front invalidates the prefix and pays that premium on every step to store something it never reads again.

That is why the useful question after his chart is where in the prompt the changes land, not how many tokens are being re-sent. The re-sending is the symptom. The prefix position is the cause.

## The window argument

Cost is the argument the post makes and the one that gets attention, because it has a number attached. The argument that changes behaviour is the second bill: a re-read costs a fraction in money and full price in context, and there is no discounted rate for the space it occupies.

Which produces a failure that looks nothing like a bill. The agent that has been reading files all afternoon runs out of window before it runs out of money, and the symptom is confident recall of something it saw early and silence about something it read forty steps ago.

## What this is not

No link, no offer, no mention of engagements. His audience is engineers who will check the arithmetic, so a comment that flatters the chart and adds nothing verifiable would be worse than no comment.

Not a correction of his figures. The 52.1 is quoted as his, and the point is what it costs rather than whether it is right.

## If he replies

The question worth having is whether his 1,127 runs are single-tenant or shared. Cached reads only pay off when the same prefix recurs across calls, so a breakdown pooled across many agents can show a healthy cache rate while each individual agent gets almost none of it.
