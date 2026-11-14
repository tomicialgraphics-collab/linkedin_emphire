---
deliverable: doc
id: 2026-11-14_m1-pack-readme
date: 2026-11-14
audience: collaborator
status: ready
approved: no
contents: 02 baseline failure, 03 the change, 01 environment, 04 classification log, 05 hashes
---
# M1 pack: one property, two revisions, and what the change does not touch

This pack answers one question, on one file, at one revision.

**The question.** The conflict path wrote two records: the second verdict, and then the record
that names the conflict between the two verdicts. It wrote them in two appends with an fsync
between them. A crash between those two writes leaves a store that reports an action as
conflicted with nothing on disk that names the conflict. This pack shows that state, shows the
state after the change, and shows that the change moved nothing else.

## The property

> A store that reports an action as conflicted must be able to name the conflict, meaning a
> preserved record carrying both sequence numbers of the two verdicts that disagree.

## The two revisions

| | revision | file | sha256 of that file |
|---|---|---|---|
| baseline | `126f1c00dfae18b30456a8dc698ac906ca7ddb0e` | `bench/store.py` | `99f25cab23b3dea0f6f739a96fae23bc25bbc3d0a0db96e801ac7d701ae1f982` |
| carrying the change | same commit plus `03-change/patch.diff` | `bench/store.py` | `ead1b552be700468168a784533750941fbc83fe23f938709a972c7f1d2867df7` |

The patch applies to `bench/store.py` only. Nothing else in the tree is modified. Patch
`836b30b5...` in `05-SHA256SUMS.txt`.

## What is in each folder

| item | file | what it is |
|---|---|---|
| 1. baseline failure | `02-baseline-failure/probe.log` | the probe on the pinned revision, exit 2, two named failing cuts |
| | `02-baseline-failure/probe.json` | the same result as data |
| | `02-baseline-failure/revision.txt` | revision, file hashes, patch hash |
| 2. the change | `03-change/patch.diff` | the diff, against the file hash above |
| | `03-change/probe.log` | the probe on the patched tree, exit 0, every cut holds |
| | `03-change/probe.json` | the same result as data |
| 3. environment | `01-environment.txt` | interpreter, modules, binaries, determinism |
| 4. classification log | `04-classification-log.md` | all twenty-two suite checks before and after, and the exact artifact difference |
| 5. the diff against the hash it applies to | `03-change/patch.diff` + `02-baseline-failure/revision.txt` | the diff and the two hashes of the file it changes |

Also here: `harness/probe_conflict_crash.py` (the probe itself), `01-environment.sh` and
`rebuild.sh` (both regenerate their outputs), `make_zip.sh` (builds the delivery zip
deterministically, so the zip has a hash worth printing), `05-SHA256SUMS.txt`.

## What the probe does, exactly

It runs one real conflict through a real store process over the store's own socket protocol:
issue, verdict ALLOW, verdict BLOCK. It then takes the journal that conflict produced and cuts
it at every line boundary. Each cut is a place where a crash between two fsyncs could have
stopped the file. Every cut image is handed to a fresh store process, and that store is asked
whether the action is conflicted and whether the conflict is named.

On the baseline, two of the five cuts fail, and both are named.

`line-4` at byte 1277 is the boundary between the two writes: two verdict records survive, the
conflict record does not. The recovered store reports the action as `conflicted` and returns
`conflict: null`. That is the failure this milestone is about, and it is reachable by a crash
landing anywhere in the window between the two fsyncs.

`mid-final-line` at byte 1412 cuts inside the conflict record's own write. The same thing
happens for the same reason: the two verdicts are durable, the record that names their
disagreement is not.

On the patched tree all five cuts hold. The two that failed now withhold the incomplete batch
instead of indexing half of it, so the store reports one verdict and no conflict, and says on
start-up that a batch was withheld. There is no cut on the patched tree that reports a conflict
it cannot name.

## What this pack does not claim

**It is a cut, not a power loss.** The probe simulates the crash by truncating the journal at a
line boundary. That is deterministic and replayable, and it is a model of what a crash between
two writes leaves, not a measurement of a device under power loss. No claim here rests on
hardware behaviour.

**It does not re-run the fifty verdicts.** The suite's twenty-two checks were run at both
revisions. That is all the suite does, and all this pack repeats.

**S1 is not the whole milestone.** This pack covers the conflict path only. S3 (a distinct exit
code for could-not-classify), S4 (read-only mount as the narrower condition) and S5 (fixtures
kept by an explicit flag) are not in it and are not claimed. S4 stays open on its own schedule.

**Nothing here is pushed.** The patch is a diff against a hash. Applying it is your decision in
your repository, and the published register is yours to move.

## Reproduction

```
git clone https://github.com/Teamthy/host-failure-benchmark && cd host-failure-benchmark
git checkout 126f1c00dfae18b30456a8dc698ac906ca7ddb0e
sha256sum bench/store.py            # expect 99f25cab...

python3 harness/probe_conflict_crash.py --repo .    # expect exit 2, one failing cut
python3 run.py && python3 verify.py artifacts/<run> # expect exit 0, every check holds

git apply 03-change/patch.diff
sha256sum bench/store.py            # expect ead1b552...
python3 harness/probe_conflict_crash.py --repo .    # expect exit 0, every cut holds
python3 run.py && python3 verify.py artifacts/<run> # expect exit 0, every check holds
```

`rebuild.sh` runs that sequence against two checkouts and refuses to write a pack if either
probe returns the wrong answer.
