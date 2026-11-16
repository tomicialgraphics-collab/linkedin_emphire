---
deliverable: dm
id: 2026-11-16_dm_behar_the-tree-the-log-cannot-name
date: 2026-11-16
audience: direct
status: ready
approved: no
warm: yes
time_checked: >-
  checked: 2026-11-16 22:58 WAT, read from the system clock before this file was written.
profile_checked: >-
  Behar Dalipi, messages at 22:48 and 22:51 on 16 November. He confirmed the zip hash, reproduced f23, f24 and f25
  from the patches including the 44 bytes and the failed append, and agreed the recovery status belongs to a future
  revision. He found that 02-previous-change/revision.txt carries the M1d hashes under an M1e label, asked which
  checkout produced the f25 log beside it, and then said he had found the base commit and patches himself and needs
  only that one clarification for now.
premise: >-
  He is right about the hashes, and the question behind them cannot be answered from the log: f25 produces identical
  output on M1d, M1e and M1f, verified by running it on all three rebuilt trees. Two further defects surfaced while
  checking, and the tree he asked for is supplied as a snapshot so the full rerun needs no patch chain.
sources_read: >-
  read: his two messages, the M1f pack in full, the M1e and M1d packs, and four runs made on this machine on 16
  November against rebuilt trees: f25 on M1d, M1e and M1f, and the full twenty-two mode run plus verify on M1f.
premise_checked: >-
  checked: every hash quoted was computed here from a tree rebuilt from the packs, not copied from a record. The M1e
  tree was rebuilt as base then M1d patch then M1e patch and hashes to 9070f970 and 1c246c61; the M1f tree as base
  then M1d patch then M1f patch and hashes to 0989c8db, 490de706 and ae147a28. The Drive md5s were read back from the
  upload responses and match the local md5s.
---

## DM, paste this

You're right, and it's worse than one wrong line.

`02-previous-change/revision.txt` now carries the M1e hashes: `bench/store.py` 9070f970, `audit/regressions.py` 1c246c61, and the README at b20b4a87, which was correct all along because it never changed between the base tree and M1e. The two wrong values were M1d's. The old values are named in the file rather than quietly overwritten.

On which checkout produced `02-previous-change/f25.log`: the log can't tell you, and that's the real finding. **f25 gives byte-identical output on M1d, M1e and M1f.** I rebuilt all three trees from the packs and ran it on each. Same 44 bytes, same 341 to 297, same gap None, all three logs hashing to `c4e4f2b2`. The torn-line path is untouched by every revision in this chain, so f25 documents behaviour and separates nothing; f24 is the mode that separates M1e from M1d. The pack shouldn't have implied the f25 record identified a tree, and the readme's line about the two revision files meaning the trees cannot be confused is now gone.

Checking your find turned up two more. The patch in `03-this-change` is a diff from M1d, not from M1e, which is why applying M1e then M1f is rejected; base then M1d then M1f reproduces the tree exactly. And no code line changed: `bench/store.py` still differs from M1e only in the module docstring, seven lines.

For the full rerun, here is the tree rather than a chain, so nothing has to be assembled:

**Tree snapshot:** https://drive.google.com/file/d/15qwQ05eL4oH_-_6pkmzeOhFKN7ThKKxY/view
sha256 `c8a56695c4a47ae8ddb7a54efcabc11e900ae435fac3b6683ae9d0e84b894687`, md5 `af8493038f5aecf5db1f73ec20a7668c`, 39 files, with a revision record at the root carrying the three hashes and the chain.

I ran all twenty-two modes, then run, then verify on that exact tree before zipping it: 22 caught, 0 missed, `VERDICT: every check holds`.

**Corrected pack:** https://drive.google.com/file/d/1Jdbq9Wo2s4cyTKuBG74bDdviux-uC0mv/view
sha256 `f7e3e1808711d0cebd85714684aa439ca9484bf1fba569c177a07832531fc167`, md5 `701f7cbded6c926ca573d14ca580842a`, 23 files, with a correction note naming all three defects and `06-f25-tree-check/` holding the runs behind the claim.

If you'd rather f25's description said plainly that it documents the limit and separates no revision, that's a one-line change and I'll put it in the next revision rather than this one.

## Why the answer is the defect and not the log

He asked a fair question and the honest answer is that the artefact cannot answer it. Three trees, one output hash. A log that is identical across every revision it sits beside is a record of behaviour, not of provenance, and dressing it as provenance is what produced the wrong line above it.

Saying that plainly is worth more than picking the tree I believe produced it, because the belief cannot be checked and he would be right not to accept it.

## Why the tree snapshot and not a chain

He has already found the patches, and the chain is now known to be base, M1d, M1f rather than base, M1e, M1f. Rather than ask him to trust a corrected instruction, the snapshot removes the assembly step: unzip, hash three files, run three commands.

It is also the artefact that answers the larger question under his message, which is whether the thing he would merge is the thing that was tested. A tree he can hash and run is a stronger answer than a commit nobody can point at.

## Why no apology paragraph

The correction is in the pack, in the readme and in the message, each saying what was wrong and what it is now. A paragraph about how it happened adds nothing he can use, and he has a full rerun to do tonight.
