---
deliverable: reply
id: 2026-11-08_reply_paolo-perrone-pipe-attribution
date: 2026-11-08
audience: public
status: ready
approved: no
warm: yes
profile_checked: Paolo Perrone, profiled on 2026-11-07 and again on 2026-11-08. Writes Shipping Production AI, states a readership past a million AI engineers, publishes through Substack with an O'Reilly title. Second exchange with him on 8 November, and his replies are short and mechanical, so the answer to him is short too.
thread: his second reply under my comment on his agent budget post, agreeing that a wrapper destroys the refusal and adding that this is why his gates run bare, because with one pipe in front the exit code you read belongs to the pipe
verified: nothing external is claimed. The shell behaviour referenced is standard and is stated as behaviour rather than as a measurement of his system.
---

# Reply to Paolo Perrone, 8 November 2026

## What he said

He agreed and sharpened it: with a pipe in front, the code you read belongs to the pipe. That is a one-line exchange and the
reply should stay in the same register. Anything longer would be talking over him in his own thread.

The addition worth making is small and true. Turning on pipefail gets the code right, but not the attribution: with two
stages you know the pipeline failed, not which stage refused, and a 2 arriving from the second stage looks exactly like a 2
from the first. Which means the code has to carry its emitter, or it only works while the pipeline has one part.

## Reply

Pipefail gets the code right and loses the attribution. With two stages you know the pipe failed, not which part refused, and
a 2 from the second stage reads exactly like a 2 from the first.

Same shape as the original problem, one layer up. The code needs to arrive with who emitted it, or it only works while the
pipeline has two parts.

## What not to say

No expansion into a fourth proposal. This is his thread and a three-line exchange, and the useful contribution is one
observation, not a design. No mention of the client repo, no numbers, and no link.

## Held for later

If it keeps going, the interesting end of it is that everything in this conversation is the same finding: a refusal is only
useful if it survives every boundary it crosses on the way out. That is a conversation, and probably a post.
