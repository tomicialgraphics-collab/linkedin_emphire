---
deliverable: comment
id: 2026-11-14_fuchigami-ryuichi-tri-state
date: 2026-11-14
time_checked: >-
  checked: 2026-11-14 18:19 WAT, read from the system clock in the sandbox before this file was sent for gate.
audience: public
status: ready
approved: no
warm: yes
premise_checked: >-
  checked: the post this replies to is my own, published 13 November 2026 with 272 impressions,
  and the comment answered here was written 23 minutes before the draft, in reply to that post.
  The claim in it is his: a feed that returned nothing looked exactly like a quiet news day, and
  his script now returns OK, retry or unavailable instead of two states. His three states come
  from the comment itself, not from an inference about his stack.
sources_read: >-
  none: nothing is linked. The post and both comments were read in the paste the owner supplied
  on 14 November 2026, and no page was fetched, so nothing here rests on a summary of something unread.
profile_checked: >-
  Fuchigami Ryuichi, first degree. Headline as supplied: building a Japan-born startup studio,
  solo plus AI, serial founder, ex-EIR at a US venture studio, with one exit, running 0-to-1
  validation for enterprise teams. The relevant line is the comment itself: he already fixed this
  in his own morning job, so the reply must add something his fix does not already cover rather
  than agree with it. His phrasing is concrete and short, and he names the failure mode before
  the fix, which is how someone argues who has been burned by it.
thread: my post on NOT TESTED inheriting exit 0, under Fuchigami Ryuichi's comment about a feed that could not tell an error from a quiet day
---

# Reply to Fuchigami Ryuichi, 14 November 2026

## What he actually said

His morning job has a feed. When a fetch came back with nothing, the report said the same thing as a day with no news: nothing. He wrote a small script that checks every fetch and returns three answers instead of two, OK, retry, or unavailable, and an empty result no longer gets reported as no news.

That is the same defect as the post, found independently, in a different system, and fixed at the boundary rather than at the reporting layer. Agreeing would waste his time. What is worth adding is the part his description leaves open: where a third state usually gets flattened back to two.

## Where the third state dies

The state survives until something stores it as a payload. An empty list in a row, a null, a zero row count: all of those are the same bytes as a successful fetch that found nothing, so the next reader reconstructs two states from the data and never sees the tag.

Writing the state and the reason as one value fixes it, because the summary cannot receive the empty list without receiving the reason it is empty. A flag stored beside the payload does not, because the next hop can drop the flag and keep the payload.

The second thing is the retry. Retry without a deadline is a fourth state borrowing the third one's name, and it surfaces as a hang, which more than one orchestrator reports as an empty result. So the deadline is not a nicety, it is what keeps the count at three.

## The test, which costs one run

Force each of the three states, then print the value the summary function actually receives. If two of the three print the same thing, the boundary is in the wrong place, and no amount of correct reporting downstream will recover it.

## Comment to paste

Ryuichi, three answers is the right shape, and the tag is the part that leaks.

The moment "unavailable" gets stored as an empty list, the next reader is back to two states. Nothing in that row says whether the fetch failed or the source was quiet, so the truth survives exactly one hop.

What has held up for me is writing the state and the reason as one value rather than a payload with a flag beside it. Then the summary can't be handed an empty list without also being handed the reason it's empty.

One addition to retry: give it a deadline. A retry without one is a fourth state wearing the third one's name, and it fails as a hang, which some orchestrators report as an empty result.

The test costs one run. Force each of the three states and print what the summary receives. If two of them print the same thing, the boundary is in the wrong place.

## Why not the other things in the paste

The playbook link went out in the earlier reply, so repeating it here would be the second link on one thread and would read as promotion rather than answer. Nothing else in the thread asks a question. No hashtags in a comment.
