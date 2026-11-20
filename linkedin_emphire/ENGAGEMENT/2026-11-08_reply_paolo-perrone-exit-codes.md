---
deliverable: reply
id: 2026-11-08_reply_paolo-perrone-exit-codes
date: 2026-11-08
audience: public
status: ready
approved: no
warm: yes
profile_checked: Paolo Perrone, profile read on 2026-11-07 at the time of the comment and unchanged today. Writes Shipping Production AI on agents, inference and GPUs, states a readership past a million AI engineers, publishes through Substack and has an O'Reilly title. He engages technically and briefly, which is what this reply matches.
thread: his reply, 25 minutes after my comment on his agent budget post, agreeing with the refusal point and reporting that his own gates already split exit 1 for failed and exit 2 for refused
---

# Reply to Paolo Perrone, 8 November 2026

## What he said

He did not argue. He confirmed the split from his own practice: exit 1 is failed, exit 2 is refused, and before that
split existed an agent had no rule for a refusal. He also took the time to say so publicly on a post that already had
his own audience on it, which is worth more than a like.

The useful reply is not agreement, because he already agrees. It is the part of the split that only shows up after it is
adopted: what to do with a run that cannot tell which of the two it is, and what happens when something in the middle
flattens the code. Both come from measured work this week rather than from theory.

## Reply

That split is doing more work than it looks. We ended up needing a third: exit 3 for a run that cannot decide which of
the two it is, because the tempting default is to call anything unclassified a failure and then retry it. So 0 pass, 1
failed, 2 refused, 3 indeterminate, and the caller's rule is stop on 2, escalate on 1 and 3.

Which breaks the moment there is a wrapper in the middle. If anything between the agent and the gate normalises a
non-zero exit to failed, the refusal is gone before the agent ever sees it.

## What not to say

No restating his point back to him as if it were new. No mention of the client project the exit codes came from, and no
numbers, because they belong to someone else's repository. No link to my own work in a two-line exchange under his post.

## Held for later

The measured version, if he asks: this week's pair where two refusals returned byte-identical replies and identical host
events, and the only surviving difference was in the durable records. That is the natural follow-up to "an agent had no
rule for a refusal", and it is better as a conversation than as a paragraph in his comment thread.
