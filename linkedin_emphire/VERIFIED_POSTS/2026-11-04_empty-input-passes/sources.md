# Sources: "The check passed because the file it reads was empty."

Post for 4 November 2026, second post of the day. Post 18 (value pluralism) went out in the morning slot.

## What this post claims

Nothing external. Every instance in the list is a failure mode observed in systems the author has built or read, stated in the first person and without a number. There is no study, no statistic, and no client story to attribute, which is deliberate: the post's authority is that the first line happened.

The originating case is the send-log check described in the author's comment on Kyle Bartlett's post about connect-ready gates, 4 November. The framing, "the reader is fine, the thing it reads is missing," came from that thread and is the author's own.

## Deliberately not claimed

- No figure for how often this happens, since there is no sample.
- No claim that any named company shipped this.
- No suggestion that evals are generally worthless, only that a pass over an empty set is not a pass.

## Checks

- 296 words, inside the 250-310 budget.
- `voice_lint.py --profile linkedin --human`: 0 errors, 0 warnings, gate 100/100, 7 contractions, 0 triads.
- No em dashes, no bold, no links, three hashtags.
- Structure differs from the 1 November post on purpose: no "here's what most teams get wrong" scaffold, a four-line list in place of three arrows, and the reveal moved to the end.
