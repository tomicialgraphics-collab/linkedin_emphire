---
deliverable: dm
id: 2026-11-14_dm_sebastien-favre-draft-40-wording
date: 2026-11-14
time_checked: >-
  checked: 2026-11-14 18:32 WAT, read from the system clock in the sandbox before this file was sent for gate.
audience: vendor
status: ready
approved: no
warm: yes
profile_checked: >-
  Sébastien Favre runs the evidence repository and opened the draft pull request himself, on 14 November
  at 10:45, to credit a contribution he was not obliged to credit. He merges only with approval, which
  makes the reply a decision rather than an acknowledgement, and he sent a recommendation at 10:48 in
  the same hour. He reads carefully enough that a vague yes would be read as a rubber stamp.
premise_checked: >-
  checked: the pull request could not be opened from here. The repository returns 404 without access, so
  nothing in this message claims to have read its wording. What the message does instead is name the
  three things the wording has to carry and give an approval that is conditional on them, which is the
  only honest form of approval available without reading the text. The substance it relies on is
  Timothy's own written position of 14 November and his recorded re-run at version 1.3.0, both already
  in the thread.
sources_read: >-
  read: Timothy's message of 14 November, in which he records that his patches changed a contract rather
  than repairing a defect, and the exchange in which he states that the exit code is the only channel an
  automated caller reads and that a default returning zero on NOT TESTED is fail-open for that caller.
  The pull request itself was not read, and the message says so.
---

## DM, paste this

<!-- gate:body:start -->
I tried to open the draft and got a 404, so I have not read the wording, and I am not going to approve text I have not seen. What I can do is tell you what it has to carry, and approve it the moment it does.

Three things.

First, Timothy's patches changed a contract. They did not repair a defect, and he said so himself before anyone else did. A pull request that calls it a fix would be quietly upgrading his work into something it is not, and the interesting part of what he did was noticing the difference.

Second, his position on the exit code is his, and it is worth stating in his words rather than smoothing into consensus: the exit code is the only channel an automated caller reads, so a default that returns zero on NOT TESTED is fail-open for that caller. If the pull request argues for putting the strict flag in the first paragraph of the attestation docs, that argument should sit under his name, not the repository's.

Third, credit is not endorsement. Nothing in it should suggest the review closed, validated, or signed off on the corpus. It credited a contribution, which is a smaller and more defensible claim, and the smaller claim is the one that survives being questioned later.

If the body already does those three, merge it and no reply is needed. If it does one of them and two would take a sentence each, send me the body and I will approve the edit rather than the intention.

One decision that is yours and not mine: whether the pull request credits Timothy only, or also credits your own re-run at 1.3.0. I would name both, separately, because they are different kinds of work and merging them into one line loses the thing a future reader will want, which is who did what.

On the recommendation, thank you. I am not going to trade one back to keep the ledger level. If I write one it will be because the work earned it, and it has, so it will not be a formality when it comes.

You asked for approval and you have it, on the three conditions above. That is a yes with a shape, which is the only kind worth sending you.
<!-- gate:body:end -->
