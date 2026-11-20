---
deliverable: dm
id: 2026-11-10_reply_martina-brazelton-issuer-out-of-the-loop
date: 2026-11-10
audience: reply to Martina Brazelton in his own message thread
status: ready
approved: no
warm: yes
profile_checked: >-
  2026-11-10, from her own two messages only. A public search for her name and for Anchored Autonomy returned nothing
  usable, so nothing is claimed about her role, employer or title beyond the name of her work that she used herself. What
  she said, in her words: a trust score should not be another number we are expected to trust; the evidence, governing
  conditions and basis for its conclusions should be independently verifiable without relying on the issuer; independent
  testing and reproducibility are essential especially with probabilistic inference; and she asked how the red teaming
  work approaches that.
thread: independent verifiability of a trust score
premise_checked: opinion: her message describes her own framework and asks a method question, so there is no external claim to check
sources_read: none: no link, paper or attachment in either message, 2026-11-10
---

## Reply, paste as is

Then we agree on the hard part, which is that the issuer can't be in the loop at the moment the check runs.

Here's what I test for, in the order these usually fail.

First, whether a customer can recompute the artefact from what they were handed, with a hash and a byte count, without asking us anything.

Second, whether a negative control exists. A check that passes when it should fail isn't a check at all, and breaking the input on purpose is the quickest way to learn whether somebody has one.

Third, whether the thing tested was reachable by the person the claim is aimed at. My sharpest finding this month was a component that passed every test it had and couldn't be invoked by any outside client. The proof was real, and the capability didn't yet exist.

Probabilistic systems add a fourth test, and it's the one most reports skip. A rate needs its denominator, and a rerun needs the same inputs, or the second result measures the sampler rather than the system.

## Why it is short

She is answering a question rather than defending a position, and she asked a method question in good faith. Four short tests give her something to use against her own score tomorrow, and no pitch follows them. Anything longer reads as a lecture from a stranger who joined the network yesterday.
