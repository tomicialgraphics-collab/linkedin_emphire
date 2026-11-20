---
deliverable: comment
id: 2026-11-09_comment_damien-filiatrault-commit-and-push
date: 2026-11-09
audience: public comment on Damien Filiatrault's Commit and Push episode post
status: ready
approved: no
warm: no
profile_checked: >-
  Damien Filiatrault, founder of Scalable Path and host of Commit and Push, posting an episode with Ivan Lee of Datasaur on
  private AI. The transcript is in the post. The numbers used in the comment come from that transcript and were computed
  with the playbook's own wilson.py on 9 November: 95 of 100 gives 88.8 to 97.8, 190 of 200 gives 91.0 to 97.3, and 199 of
  200 gives 97.2 to 99.9.
thread: a 95% gate on a 200-case suite is a smoke alarm, not a promise
---

## What is in the episode

Ivan Lee describes working backwards from a custom evaluation per client: 100 to 200 cases with answers a human verified, then a gate of 95% accuracy, or 99.5% for a more important process, agreed before sign-off. The benchmark is kept as an artifact so a model upgrade can be checked for regression. He also describes a client stranded when a model was deprecated five months early, and another still running Llama 3.2 with a benchmark score of 98%.

## Why this comment

The practice is the right one and it is the same argument the playbook makes. The gap is arithmetic. A 95% gate on a 100-case suite is consistent with a true rate of 88.8%, and the 99.5% gate cannot be demonstrated at 200 cases even with one failure. That is a contribution, not a correction of the method, and it is the kind of thing the audience of engineering leaders can check in a minute.

## Comment, paste as is

The custom benchmark is the right instinct, and one number in it needs tightening.

A 95% gate on 100 cases has a 95% interval from 88.8 to 97.8. On 200 cases the same result runs 91.0 to 97.3. That is a fine smoke alarm and a bad promise, because the client hears 95 and buys a floor the suite cannot show.

The 99.5% gate is the one I would renegotiate before the next sign-off. Even 199 of 200 leaves the lower bound at 97.2, so at that sample size the threshold cannot be demonstrated at all. Either the suite grows or the gate moves.

None of that touches the best thing in the episode, which is keeping the benchmark as a versioned artifact. That is what survives a deprecation arriving five months early.

Every gate needs two numbers, the rate and the interval. The rest of the statement of work can stay as it is.

## What not to say

No mention of the playbook, no link, and no suggestion that the guest does not understand his own numbers. He does. The point is that the client does not, and the fix is one extra number in the gate rather than a different method.

## Held

The stronger post in this episode is the deprecation story: an evaluation suite is the only asset that transfers when a vendor withdraws a model on five months' notice, and most clients discover they never owned one.
