---
deliverable: dm
id: 2026-11-13_reply_behar-reference-submitted
date: 2026-11-13
audience: collaborator
status: ready
approved: no
warm: yes
profile_checked: >-
  Behar Dalipi wrote on Friday 13 November at 23:16 to say the reference form for the Anthropic AI Safety and Security
  Fellows Program was submitted the same day, that the assessment was grounded in the Host-Failure Benchmark
  collaboration, and that he is waiting on the M1 evidence for S1 and S2 under the criteria agreed on 9 November.
sources_read: no attachment in his 13 November message. The thread pasted on 13 November was read in full, 1 November to 13 November, including his four rulings of 7 November and his confirmation of 9 November. The published register at Teamthy/host-failure-benchmark main was opened on 13 November to check what the text says now, and it still reads disputed for V04 inside F-08. The pinned copy he reviewed, 4413420b, was not re-opened, and no claim here rests on it.
premise_checked: >-
  checked: on 13 November 2026. The published register at Teamthy/host-failure-benchmark main still carries V04 as
  disputed inside F-08, and N13 in the form the reviewer read, so nothing in the published text has moved since the
  four rulings. M1 is not implemented: no s1 partial-state mode and no keep-fixtures flag exist in the tree. The four
  rulings are the ones he gave on 7 November (partial with established records, exit code 3, read-only mount as the
  narrower condition, keep-fixtures as an explicit flag), confirmed by him on 9 November.
---

# Reply to Behar: the reference, and what M1 owes him

## The reply

```
Behar,

Thank you, and I want to be precise about what you did rather than just grateful for it. A reference written from the work itself, by the person who ran the adversarial tests rather than by someone repeating a summary, is the only kind that survives the first follow-up question. You had the harder half of this collaboration and you put your name to it anyway.

I will tell you the outcome either way, including if it is a no.

On M1: it is not ready, and I would rather say that than let a date do the work of a result. What is done is the design work the two of us agreed, including your S1 narrowing, which changed the shape rather than confirming it: the conflict path now frames both records into one append and one fsync, so the failure between the two writes stops existing, and the partial state is tested against a torn batch instead. That is a stronger result than the one we scoped, and it exists only as a design until the mode that fails without it is written.

When the pack arrives it will carry the five things agreed: the baseline failure on the pinned revision, the post-fix result on the revision carrying the change, the environment, the classification log showing the modes M1 does not touch, and the diff against the file hash it applies to. Two hashes and a revision, no links.

One loose end, so it does not get lost between milestones. In my 1 November message I wrote V04's status as scope and asked whether you would rather it read as settled. You did not rule on it, and the published register still says disputed inside F-08. That stays as published until you settle it, and it is a one line answer whenever you get to it.

Olusanya
```

## Why each part is there

**The reference paragraph names the thing that makes it good.** He ran the adversarial tests. A reference from the tester is worth more
than one from a person who heard about the work, and saying so is accurate rather than flattering.

**"I will tell you the outcome either way, including if it is a no"** is the only sentence in the message that costs something, which
is why it is the one he will believe.

**The M1 paragraph gives a status, not a date.** M1 is not built. Inventing a deadline to look responsive is the failure mode this
whole collaboration is built against, and he would read it exactly that way.

**Naming his S1 narrowing as having changed the shape** keeps the credit where it belongs and quietly reports progress that is real.

**The V04 paragraph closes a loop that has been open since 1 November** without asking him for anything urgent.

## What is deliberately absent

No question about what he wrote on the form. No request for anything. No thanks repeated twice.
