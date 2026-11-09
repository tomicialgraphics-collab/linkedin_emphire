---
deliverable: comment
id: 2026-11-08_artur-walisko-self-verification
date: 2026-11-08
audience: public
status: ready
approved: no
warm: yes
profile_checked: 2026-11-08 from his profile and this post. Artur Walisko is a first degree connection, an AI systems and risk analyst working on LLM evaluation and AI governance with seventeen years of operational analysis behind him, publishing as AW Analysis. He runs experiments and shows the working, and he asks readers for their experience rather than for agreement.
thread: his post describing an experiment where several models analysed data and were then asked to verify their own conclusions, the Palo Alto figures of 109 machine identities and 79 agent identities per human identity, his correction that the 79 sits inside the 109 rather than beside it, and his conclusion that verification has to lead back to the original source
verified: the figures and the correction are his, taken from his reading of the report, and the comment treats them as his rather than as independently checked. The two technical claims in the comment are standard: resampling the same model reduces variance rather than bias, and a containment error can survive a review that reads the same representation.
---

# Comment on Artur Walisko's self-verification post, 8 November 2026

## Why this angle

Shayne Beavan has already made the strongest general point under the post, that an agent's account of what it did is still the
agent's word, and a second version of it would add nothing. The opening left is the specific shape of the error Artur found: the
number was right and the relation between the numbers was wrong. That is a containment error rather than a factual one, and it is
the class self-review is worst at, because the review reads the same flattened representation the error came from.

From there the mechanical explanation is short and true: a second pass reduces variance, not bias.

## Comment

The detail about 79 sitting inside 109 is the most useful part of this, because of the kind of mistake it was. The figure was
right and the relation between the two was wrong. That is a containment error rather than a factual one, and it is the class
self-review is worst at, since the review reads the same flattened representation the error came from.

Which is the mechanical reason self-verification fails. Asking again reduces variance, not bias. You get a second sample from
the same distribution with the same blind spots, and it comes back confident, because nothing in that second pass had access to
the source.

Fresh source or nothing. The same model twice is a second opinion from the same person.

## What not to say

No restatement of his conclusion about going back to the original sources, which he has already established and argued well. No
disagreement with the numbers. No mention of my own work, and no answer to the question he asked in his follow up post, which is
addressed to everyone and better answered by whatever the thread produces rather than by a reply from me in the same hour.

## Held for a later turn

If he replies, the interesting extension is what a source-level check looks like when the source is itself a model output, which
is most of the web now. That is a real problem for his kind of analysis and it has no clean answer.
