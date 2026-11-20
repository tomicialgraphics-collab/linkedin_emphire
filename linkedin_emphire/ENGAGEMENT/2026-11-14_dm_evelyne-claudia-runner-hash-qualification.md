---
deliverable: dm
id: 2026-11-14_dm_evelyne-claudia-runner-hash-qualification
date: 2026-11-14
time_checked: >-
  checked: 2026-11-14 21:08 WAT, read from the system clock in the sandbox before this file was sent for gate.
audience: peer
status: ready
approved: no
profile_checked: "Evelyne-Claudia Yantony replied at 9:52 PM accepting the pin and the hashes, correcting my terminology and raising one technical qualification about the patch guard. She is an examiner working to a written standard, so the reply has to answer her point in her terms and concede it if the bytes support her."
premise_checked: >-
  checked: the claim about the guard was tested against the runner in the repository rather than remembered.
  F9b-conflict-write.py is 17,594 bytes and hashes to 991e9eec09c291bf0179b6677577c5929b688df0b2b2c10fea2cc163d669e891, which
  is the hash quoted to her. It calls sha256_file on the store before and after the patch, writes both into
  the result, and compares neither against a constant. Its only refusal is a missing anchor line. Her
  qualification therefore stands and the earlier sentence was broader than the code.
sources_read: >-
  read: the runner source in OUTREACH/evelyne-claudia-2026-11-06, and the message history in this thread.
  Nothing was run and no archive was opened.
---

## DM, paste this

<!-- gate:body:start -->
Evelyne-Claudia,

The qualification is right, and I checked it against the bytes rather than against my memory of them, because I had described the guard as stronger than it is.

The runner you hold, 17,594 bytes, SHA-256 991e9eec and the rest of it as given, hashes the store module before the patch and after it and writes both digests into the result. It compares neither of them to anything. Its only refusal is the anchor line: if the failpoint line has moved, it stops. So the sentence I wrote, that it cannot patch a version it does not recognise, is true of the line and not of the file. A store module edited anywhere else would pass that check, and the claim should have been narrower.

There are two ways to close it and I would rather you had both.

The whole-file check you ask for does exist in the artifact, just later than the patch. The result file carries the pre-patch digest under patched_store_sha256_before, so a source file that is not the one this case names puts a different value in the output, and the output's own hash moves with it. Compare the run's result against e5216e9c and the file check has happened, at the end rather than the start. That is a weaker design than yours and it is one command.

The stronger design is the second runner, which refuses before it measures anything. If you want that one for the comparison, say so and it goes out with its own hash.

Terminology, retained as you put it: two different signed verdict records where the host cells both carry BLOCK, and a disagreement in the verdict value for the wire pair at sequences 4 and 5. The correction note keeps that language wherever the two comparisons sit side by side.

On validation, the phrase is gone from the page and not only from the letter. It was never mine to give.

The genuine verdict-write refusal is the next cell, and I agree it is a new run rather than an argument, with the five surfaces named separately: the refused operation, the durable records, the reply, the host diagnostics and the replayed state.

Reproduction is still outstanding and it stays yours.

Olusanya
<!-- gate:body:end -->
