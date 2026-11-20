---
deliverable: run-record-correction
id: 2026-11-14_record-fixes-v2
date: 2026-11-14
time_checked: >-
  checked: 2026-11-14 18:29 WAT, read from the system clock in the sandbox before this file was sent for gate.
audience: reviewer
status: ready
approved: no
premise_checked: >-
  checked: every number in this pack was produced on 14 November 2026 on two fresh clones of
  80fa2cf, one with the earlier patch and one with this one. The prefix collision is reproduced in
  the log rather than described: the published verifier passed a manifest whose console.log row
  was wrong after its sixteenth character, 50 checks to 0. The corrected verifier fails that same
  manifest on exactly that row, 53 to 1, and passes the true one 54 to 0.
sources_read: >-
  read: the three findings in the reviewer's message of 14 November 2026, and the delivered files
  they refer to, which are in this repository and were re-read rather than recalled.
profile_checked: >-
  Andrey Ekhmenin, independent reviewer of the pinned five-test harness. He tests rather than
  reads, and he writes findings as implementation detail with the failing case attached, so the
  reply has to answer with the same currency: a reproduction, a change, and a test he can run. He
  has said plainly that these are implementation findings and not a rejection, and he keeps the
  retention guarantee open until the failure paths are tested. That condition is accepted here
  rather than argued with.
thread: the independent review of the run record and the package builder, third round
---

# Three findings, reproduced and answered

Read the clock before writing this: 2026-11-14, 18:29 WAT, Saturday. All three findings are correct. Two of them are defects that a reader could have been misled by, and the first one is the worst kind, because it is a defect in the tool whose only purpose is to catch defects.

## Finding 1: the verifier compared 16 of 64 characters

Confirmed by construction. Take the true digest for the console log, keep its first sixteen characters, replace the other forty eight with `f`, and leave the request untouched. The published verifier passes it:

```
pass  console.log digest of the stored object   4889096bc551a891
50 passed, 0 failed
```

That is the manifest disagreeing with the object in every character after the sixteenth, and the check reporting a pass. The comparison on the decision path is now `got == want` on the full 64 characters, in all five places it appears. The short strings in the log are display only.

The corrected verifier on the same forged manifest: 53 passed, 1 failed, and the failure is that row. On the true manifest: 54 passed, 0 failed. A `--self-test` mode makes the collision a fixture, so a future edit that restores prefix comparison turns the suite red rather than green.

## Finding 2: ordering is not atomicity

Also confirmed, and the earlier pack overstated it. Writing the record first means a package cannot exist without one, which is a real improvement over the 1 November behaviour, but it is not atomic. A crash inside the record write left a half-written record that looked complete, and a crash between the two writes left a state nobody had described.

What changed:

1. The record is built in a staging directory, and every file in it is fsynced, then the directory is fsynced.
2. The package text is written beside its final name as a staging file and fsynced, so the second rename cannot fail on a full disk after the first has succeeded.
3. Any previous record is moved aside, then the record is renamed into place, then the package. A rename is atomic; a sequence of two is not.
4. Because a pair of renames cannot be one operation, the pair is **bound**: the record contains `RUN.json`, which names the digest and byte count of the exact package text that was about to be published. A crash between the renames leaves a record naming a digest that does not match the file on disk, and the verifier reports that as an incomplete publication.

So the claim is now stated in the direction that holds: **a package never exists without a record, and a pair that was interrupted is detectable rather than plausible.** That is not the same sentence as "publication is atomic", and it is the sentence the code supports.

## Finding 3: an existing results file survived an unrelated non-zero exit

Confirmed in the published patch. The rule was `returncode != 0 and results.json exists`, and existence was doing all the work. A harness that died early, with an earlier run's results still in `results/`, had that file archived as this run's evidence.

What changed: before the harness starts, the builder captures size, digest and mtime of any existing results file. After a non-zero exit it refuses if the file is byte for byte what was there before the run, and refuses if its mtime predates the run start. The refusal names the reason. A run that genuinely wrote results and then crashed in `write_outputs()` still archives, because the file it wrote differs from what was there.

## The failure paths, tested

Six cases, all in `06-failure-paths.log`, 13 checks, 0 failures:

| case | what it exercises | result |
| --- | --- | --- |
| T1 | no results at all | refused, package untouched, no record published |
| T2 | non-zero exit with a stale results file | refused, naming the pre-run comparison |
| T3 | results that do not parse | refused before anything is staged |
| T4 | crash between the two renames | record published, package still the old text, mismatch detectable from RUN.json |
| T5 | a good run | record then package, digest agrees, `sha256sum -c` clean, no staging file left |
| T6 | a digest matching on 16 characters | the verifier fails it |

## What stays open, in his terms

The retention guarantee stays open. He said the improvements are substantial and the guarantee waits for the failure paths to be tested; the tests exist now, and what closes it is his reading of them, not my claim that they pass.

The 1 November gap is unchanged, as agreed. No patch returns evidence that was never kept.

The verifier is not a proof of the repository's history. It checks that the objects named in the manifest are the objects on disk and in git at the commit named, and after this change it checks the pair binding. It cannot tell whether a run should have been performed, and it does not claim to.

## Files

| file | what it is |
| --- | --- |
| `01-SHA256SUMS.corrected.txt` | the corrected manifest, unchanged from the previous pack |
| `02-record-before-publish-v2.patch` | builder change, applies to `80fa2cf`, replaces the earlier patch |
| `03-verify_run_record.py` | full 64 character comparison, pair binding, `--self-test` |
| `04-prefix-collision.log` | the collision reproduced, then fixed, with both checkouts named |
| `05-failure-paths.py` | the six cases, runnable against any checkout with the patch |
| `06-failure-paths.log` | their output, 13 passed, 0 failed |
| `07-SHA256SUMS.txt` | digests of the six files above |

## How to check it

```
python3 03-verify_run_record.py --repo <checkout>            # 54 checks against the record
python3 03-verify_run_record.py --repo <checkout> --pair <package.md>   # plus the binding
python3 03-verify_run_record.py --self-test                  # proves the checker can fail
python3 05-failure-paths.py --repo <checkout>                # the six failure paths
```

No network, standard library only, Python 3.8 or later. The patch applies to `80fa2cf` with `git apply` and touches one file.
