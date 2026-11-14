---
deliverable: dm
id: 2026-11-14_andrey-record-fixes-v2
date: 2026-11-14
time_checked: >-
  checked: 2026-11-14 18:31 WAT, read from the system clock in the sandbox before this file was sent for gate.
audience: andrey-ekhmenin
status: ready
approved: no
fix_verified: true
premise_checked: >-
  checked: all three findings were reproduced before anything was changed. The forged manifest keeps
  the true digest for sixteen characters and replaces the last forty eight, and the published
  verifier passed it 50 to 0. The corrected verifier fails that same file 53 to 1 while passing the
  true manifest 54 to 0. The failure path suite runs six cases and reports 13 passed, 0 failed. Every
  number in this message is copied from the two logs in the pack, which were produced on fresh clones
  of 80fa2cf rather than recalled.
sources_read: >-
  none: nothing is linked. Both checkouts were made from the pinned commit, the earlier patch was
  applied to one and the new patch to the other, and every run in the logs was executed rather than
  summarised.
profile_checked: >-
  Andrey Ekhmenin, independent reviewer of the pinned five-test harness. He verified the manifest
  himself, found three implementation defects in what was sent, and framed them as findings rather
  than a rejection. He keeps the retention guarantee open until the failure paths are tested, so the
  reply has to arrive with tests rather than assurances, and it must not call anything closed. It
  does not. What it adds is a reproduction of each defect, the change that removes it, and the
  command that checks it.
thread: the independent review of the run record and the package builder, fourth round
---

# Andrey Ekhmenin, 14 November 2026, second reply

All three of your findings are correct. I reproduced each one before changing anything, so what follows is measured, not asserted.

## 1. The verifier compared 16 of 64 characters

Reproduced exactly as you described. I took the true console log digest, kept `4889096bc551a891` and replaced the other forty eight characters with `f`, changing nothing else in the request. The published verifier printed:

```
pass  console.log digest of the stored object   4889096bc551a891
50 passed, 0 failed
```

A manifest that disagrees with the object after the sixteenth character, reported as a pass.

The comparison is now on all 64 characters, in every place the decision is made. The short forms left in the log are display only. On the forged manifest the corrected verifier gives `53 passed, 1 failed`, and the failure is that row. On the true manifest, `54 passed, 0 failed`. It also has `--self-test`, which compares a digest against the same digest with forty eight characters replaced and exits non-zero unless it observes the difference, so a later edit that restores prefix comparison turns red instead of green.

## 2. Archiving first is not atomic publication

Accepted, and the earlier pack overstated it. Ordering removes one hazard, a package without a record, and it does not make two writes one write. A crash inside the record could still leave a half written record that looked complete.

What changed: the record is built in a staging directory and every file in it is fsynced, then the directory is fsynced; the package text is written to a staging name beside its final name and fsynced, so the second rename cannot fail on a full disk after the first succeeded; a previous record is moved aside; the record is renamed into place, then the package.

Two renames cannot be one operation, so the pair is bound instead. The record contains its own run descriptor, which names the digest and byte count of the package text it was published with. A crash between the renames leaves a record naming a digest that no file matches, and the verifier reports an incomplete publication rather than a plausible one.

So the claim I will defend is narrower than "publication is atomic": **a package never exists without a record, and an interrupted pair is detectable.** I have stopped making the stronger claim.

## 3. An existing results file survived an unrelated non-zero exit

Also correct. The published rule was non-zero exit and results file exists, which is a test of existence, not of authorship. A harness that died early, with an earlier run's results still sitting in `results/`, had that file archived as this run's evidence.

Now the builder records size, digest and mtime of any results file before the harness starts. After a non-zero exit it refuses when the file is byte for byte what was there before the run, or when its mtime predates the run start, and the refusal names which. A run that really wrote results and then failed in output writing still archives, because the file it wrote differs from what was there.

## The failure paths, tested

Six cases, `13 passed, 0 failed`, and the log is in the pack:

| case | exercises | result |
| --- | --- | --- |
| T1 | no results at all | refused, package untouched, no record |
| T2 | non-zero exit, stale results file | refused, naming the pre-run comparison |
| T3 | results that do not parse | refused before staging |
| T4 | crash between the two renames | record published, package still old text, mismatch visible in the run descriptor |
| T5 | a good run | record then package, digest agrees, `sha256sum -c` clean, no staging leftovers |
| T6 | a digest matching on 16 characters | the verifier fails it |

The suite is the failure path script in the pack. It builds its own throwaway harnesses, so it needs no endpoint and no network.

## Where this leaves the guarantee

Open, in your terms. You said the retention guarantee waits until the failure paths are tested, and testing them is what I could do; reading them is yours. Nothing here is called closed.

The 1 November gap is unchanged, as we agreed. No patch returns evidence that was never kept, and the verifier does not claim to. It checks that the objects named in the manifest are the objects on disk and in git at the commit named, and now that the record and the package agree. It cannot tell whether a run should have been performed.

## One link, and the digests

Everything is in one folder, which opens without an account: https://drive.google.com/drive/folders/1JHj8chWsNZbnEQesUNpBwDraBAhcfGWZ and the digests of the six files inside it follow.

```
dfa8a6bda65d15ae747036f222102f8a6524580aa5bc3028637934e2959174d0  01-SHA256SUMS.corrected.txt
55e95a33455327b1fbf6d0bf85e4a866b7356e755e99587e741da402b3963e6f  02-record-before-publish-v2.patch
d6a9635a304198e5c247afc6a75495bee29ca87cbf6785350664d70b26bea5cd  03-verify_run_record.py
a27940f9b8fd3e9471faad79ef4e29e56aa7b0dd91f5c4bef3d77d0683753250  04-prefix-collision.log
a475c8333b0d83c4cf8fbc5ff1cf11aacd8355ae2cc643da6621dcc82819fd62  05-failure-paths.py
4a99d3cbf86d7eb3e1a846ff1ab71e23083ced9890cefe6f2b72240353b1e259  06-failure-paths.log
```

The patch applies to `80fa2cf` with `git apply` and touches one file, `package/build_package.py`. It replaces the earlier patch rather than sitting on top of it.

```
python3 03-verify_run_record.py --repo <checkout>
python3 03-verify_run_record.py --repo <checkout> --pair <package.md>
python3 03-verify_run_record.py --self-test
python3 05-failure-paths.py --repo <checkout>
```

Nothing needs a reply from you. If a case is not the case you would have written, tell me which one and I will write that one instead.
