---
deliverable: dm
id: 2026-11-13_dm_sebastien-favre-declined-write-up-instead
date: 2026-11-13
audience: vendor
status: ready
approved: yes
warm: yes
profile_checked: >-
  Sébastien Favre declined the paid proposal at 18:36 on 13 November. He has funded NeoMundi's development himself, the
  project runs on independent researchers and contributors, and he is no longer in a position to finance external audits.
  He thanked us for the work already shared and was explicit that he respects its value. This is a budget answer, not a
  judgement of the work, so the reply takes it at face value and does not re-pitch, discount or argue.
premise_checked: >-
  checked: the two findings offered for the write-up are the ones reproduced on 13 November from the public repository,
  the exit 0 on an attestation whose signature was never checked, and the corpus degrading to five failures on a stock
  Python without cryptography. Both were reproduced from the fixtures named in the earlier message and can be reproduced
  by anyone with the repository.
sources_read: >-
  read: his message in full. The repository was read and run earlier on 13 November and is the source of both findings.
---

## Message, paste as is

<!-- gate:body:start -->
Sébastien, that's a clear answer and an honourable reason, so there's nothing to argue with. Thank you for saying it
plainly instead of going quiet, which is what usually happens at this stage.

One thing I'd like to do, and it costs you nothing. I'd write the two failure-path findings up as a short public piece,
the exit code and the silent dependency, with the fixtures and the exact commands so anyone can reproduce them. You'd
read it before it goes anywhere, you'd be named, and you'd have the right of reply inside the piece. It's useful to your
project because both are fixable in an afternoon, and useful to me because a review that ends in a fixed defect is the
only kind worth writing about.

If that's unwelcome, say so and I'll drop it and leave the repository alone.

Two patches in the meantime if you want them, as suggestions rather than a report: return a non-zero code when a required
check comes back NOT TESTED, and refuse to run the corpus at all when cryptography is missing instead of degrading
quietly.

And if funding turns up later, the week at $1,500 stands as offered. I'd rather tell you that once than pretend the work
is free in the meantime.

Timothy
<!-- gate:body:end -->

## What not to say

No discount, no lower counter-offer, no "let's find a way", and no suggestion that he take it to a funder or a sponsor on
my behalf. No complaint about the outcome and no hint that the free first pass was an invoice arriving later. Nothing
about the case study, which he already has.

## Why this is worth sending

He said no for a reason that has nothing to do with the quality of the work, so the relationship is worth more kept than
argued. The write-up converts a declined proposal into a public artefact with his name and his reply in it, which is the
next case study, and the two patches cost twenty minutes while proving the findings were not theatrical.
