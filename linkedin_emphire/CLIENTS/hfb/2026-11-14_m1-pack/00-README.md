---
deliverable: doc
id: 2026-11-14_m1-pack-readme
date: 2026-11-15
audience: collaborator
status: ready
approved: no
contents: 02 baseline failure, 03 the change, 01 environment, 04 classification log, 05 hashes, the two cases of 15 November
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
| carrying the change | same commit plus `03-change/patch.diff` | `bench/store.py` | `b987cc49e186d9281ce86eca76a940319107002d4c5bc05d2ce362f7acc70085` |

The patch applies to `bench/store.py` only. Nothing else in the tree is modified. Patch
`14997eac...` in `05-SHA256SUMS.txt`. This is the 15 November rebuild: the 14 November patch and
the `ead1b552...` hash it produced are superseded, and both are replaced rather than amended.

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
| 4. classification log | `04-classification-log.md` | all twenty-two suite checks before and after, the exact artifact difference, and the two cases |
| 5. the diff against the hash it applies to | `03-change/patch.diff` + `02-baseline-failure/revision.txt` | the diff and the two hashes of the file it changes |
| 6. the two cases | `02-baseline-failure/two-cases.log` | the missing-terminator and unknown-state cases on the pinned revision, exit 2 |
| | `03-change/two-cases.log` | the same two cases on the changed tree, exit 0 |
| | `*/two-cases.json` | the same results as data, per restart |

Also here: `harness/probe_conflict_crash.py` (the cut probe), `harness/probe_two_cases.py` (the
probe for the two cases below, sha256 `286982e7...`), `01-environment.sh` and
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

## The two cases from 15 November

Both are in `harness/probe_two_cases.py`, and both run against each revision. Neither is
described in prose here without a file that reproduces it.

### Case A: a record whose bytes are whole and whose terminator is missing

The conflict journal is cut back by one byte, the final newline. The record is complete JSON and
its digest verifies, so it is readable. What the file does not say is that the write finished.

| restart | pinned revision | changed tree |
|---|---|---|
| 1 | conflict named, then the journal is rewritten: sha256 `1c67c5...` becomes `ff4172...` | named gap, journal unchanged |
| 2 | action reported conflicted, conflict **not** nameable; file rewritten again to `f2f59b...` | the same named gap, journal unchanged |
| 5 | action reported conflicted, conflict **not** nameable | the same named gap, journal unchanged |

The mechanism, which the 15 November message got wrong in one place and corrected in the pack:
the first restart reads the unterminated record and names the conflict from it. The loss happens
on that same start-up, in the `boot` append, which finds an unclean tail, truncates the record
into `store.jsonl.quarantine-N.bin` and rewrites the journal. Restart 2 opens a clean file with
no conflict record in it. So the gap is not a sequence number that the store withheld; it is
the quarantined byte range, and that is what the changed tree names:

```
journal gap: unterminated record of 328 bytes at byte 1335, store_seq 5, kind conflict,
withheld and not indexed; file left as found
```

The changed tree does not cut it, does not index it, does not append a boot record over it, and
refuses any write while the gap stands, because the write would have to cut the tail to land.
The journal therefore carries the same sha256, `573a5554...`, at restarts 1, 2, 3, 4 and 5.

### Case B: a write that failed and a rollback that failed

The batch write reaches half a line and fails. The rollback that would have restored the file
fails too. The process cannot say whether those bytes will survive, so it does not say:

```
{"ok": false, "durable": "unknown", "disk_state": "unknown", "reason": "rollback-failed",
 "error": "journal write failed (...) and the rollback was refused by the failpoint: the
 record's state on disk is unknown"}
```

`durable` now has three values. `true` means the bytes are on disk and the record is in the
index. `false` means nothing was persisted and memory was not touched. `unknown` means neither
claim is available, and it never renders as a pass or collapses into `false`.

On the pinned revision the state cannot even be produced: the failpoint command does not exist
there, and the nearest thing it can say about a refused write is `durable: false`, which is a
claim it is not entitled to make in the unknown case. Evidence: `*/two-cases.json`.

What the restart finds in Case B is reported and not predicted: the changed tree recovers one
verdict, quarantines the half-batch and names the quarantine bytes and hash in a `repair` record.
The probe asserts that the restart names what it found, either the conflict or the quarantine,
and records which of the two happened instead of asserting the one that is convenient.

## What this pack does not claim

**It is a cut, not a power loss.** The probe simulates the crash by truncating the journal at a
line boundary. That is deterministic and replayable, and it is a model of what a crash between
two writes leaves, not a measurement of a device under power loss. No claim here rests on
hardware behaviour.

**It does not re-run the fifty verdicts.** The suite's twenty-two checks were run at both
revisions. That is all the suite does, and all this pack repeats.

**The two cases are modelled, not raced.** Case A inserts one missing byte and Case B inserts a
failure through a failpoint command this patch adds. Neither is a power loss on a device. The
failpoint is scaffolding, it is named as scaffolding in the code, and nothing in the changed
behaviour depends on it existing.

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

python3 harness/probe_conflict_crash.py --repo .    # expect exit 2, two failing cuts
python3 harness/probe_two_cases.py   --repo .    # expect exit 2, both cases fail
python3 run.py && python3 verify.py artifacts/<run> # expect exit 0, every check holds

git apply 03-change/patch.diff
sha256sum bench/store.py            # expect ead1b552...
python3 harness/probe_conflict_crash.py --repo .    # expect exit 0, every cut holds
python3 harness/probe_two_cases.py   --repo .    # expect exit 0, both cases hold
python3 run.py && python3 verify.py artifacts/<run> # expect exit 0, every check holds
```

Both probes take `--repo`, so they are run from this pack's own `harness/` directory against a
checkout rather than copied into it. `rebuild.sh` runs the whole sequence against two checkouts
and refuses to write a pack if any probe returns the wrong answer.
