# Correction 05: three qualifications, one of them a defect in my instrument

Evelyne-Claudia Yantony, 7 November 2026, in reply to the v2 archive.

She ran v2, reproduced the refusals, and found three things. The first is a defect in the instrument
rather than in the observation, and it is the one that matters.

## 1. Exact result-file reproduction failed in her examination

Her generated files read `26 calls recorded, 26 distinct replies`. Mine read `25`. Everything else in
her run matched: archive size and hash, both 90-byte replies with the reported hash, the retried replies,
the shared-id run passing every check, the distinct-id run failing the full-record comparison, and the
restart-state differences.

**The cause.** The recorder in v2 stored each reply keyed by `id(parsed)`. CPython reuses object
identities once an object is released, so two parsed replies could land on the same identity, and the
count of distinct keys then depended on how the allocator had behaved. In my run one identity was
reused, which produced 25. In hers it was not, which produced 26. She is right that this is not a
dependable exchange identifier, and right that a sequential identifier retaining the request, the parsed
response and the raw bytes together is the fix.

**What it means for what I claimed.** "The archive reproduces its own result file with the same hash"
was true of my run and false as a property of the artifact. That is the same class of error I said I had
corrected in v2, arriving from a different direction: a claim resting on an instrument whose output was
not deterministic. The claim is withdrawn as stated.

**What changed in v3.** The recorder assigns a sequential exchange number per call and returns a dict
subclass carrying it, so consumers see an ordinary dict and the number survives. Each exchange retains
the request, the parsed reply and the raw bytes under that number. Object identity is measured and
printed in the check detail, and no conclusion rests on it.

**What the evidence now shows.** Three independent runs of the matched configuration produced one
result hash, `d41a3e5546e1a4fe6683604d4bf237dad97da47e9693fead6428a64494beef81`. The identity probe
records 26 calls, 26 exchanges, 26 distinct by identity, zero collisions, on this host. That the two
counts disagree here is the point: the old number was environment-dependent, and the new one is a
sequence.

## 2. Execution provenance was mixed

She is right, and her description of the mechanism is exact. v2 did
`conflict.update(runner.host_cell(...))`, and the same for the verdict cell. `update()` let the host
execution's `journal`, `journal_sha256` and `lookup_after_restart` overwrite the wire execution's. The
acknowledged count was read from the wire execution's replies and the durable-record count from the host
execution's journal, and those are different executions with different journals.

**Her counts, checked against the runs.** The conflict wire execution leaves three verdict records after
its retry. The conflict host execution leaves two. Both verdict executions leave none. v3 reports those
four numbers separately, each attributed to the execution that produced it:

| execution | durable verdict records | acknowledged verdict requests |
|---|---|---|
| conflict-wire | 3 | 1 |
| conflict-host | 2 | not claimed |
| verdict-wire | 0 | 0 |
| verdict-host | 0 | not claimed |

Acknowledged counts appear only where the reply itself was captured. In the host executions the store's
reply to the host's own verdict is not captured by this artifact, so the field is `null` rather than a
number inferred from something else. That is a narrower output than v2's, and it is the honest one.

Restart state is likewise reported four times: `conflicted` for both conflict executions, `null` for
both verdict executions, each with the digest of the journal it was read from.

## 3. The host comparison was narrower than the sentence around it

Agreed. v2 compared every field of three selected event records after filtering, and the sentence spoke
about the host agreeing. v3 makes both claims explicit and separates them:

- **Selected events.** The three records the host logged are identical in full under the shared-action-id
  condition. This is the narrower claim, and it is kept and labelled as such.
- **Whole journals.** These are **not** equal, and they cannot be: the injection exists to stop a verdict
  from landing, so one journal holds two verdict records and the other holds none. v3 states this
  instead of hiding it behind a filter, and reports what the difference is:

| | conflict-host | verdict-host |
|---|---|---|
| records in journal | 6 | 4 |
| verdict records | 2 | 0 |
| replayed on restart | 5 of 5 | 3 of 3 |
| whole journal equal | no | |
| equal apart from what the injection moves | yes | |

The stable part, with the verdict records and the restart boot record removed, is identical. The boot
record's replay count follows the verdict records, so it moves with them and is reported separately
rather than being treated as noise.

## What is claimed now, and what is not

- Under the shared-action-id condition, the two refused replies are the same bytes, 90 bytes,
  `1ca16a0ad93f2650f6163c9fe128ea84ed4297321c598d6c35ed18fbaa3c01c7`, including the newline, and so are
  the retried replies.
- The four executions differ in durable verdict records, 3 and 2 against 0 and 0, and in acknowledged
  verdict requests, 1 against 0, each counted where it was produced.
- Restart state differs, `conflicted` against `null`, in both the wire and host executions.
- The selected host records are identical in full. The whole journals are not, and the difference is
  the injection plus the boot record that counts it.
- With distinct action ids in the two host cells, the journal comparison fails. That run ships beside
  the passing one, because the failure is what licenses the condition.

Not claimed: that any of this reproduces an experiment in its entirety, that exact result-file
reproduction is now established on her machine, or that any of it validates an architecture or
REACHABLE™. A reproducible observation is not a reproducible experiment, and reproducibility alone does
not establish that an architecture is correct. Frozen REACHABLE™ is unchanged.

Reproduction remains hers, and this correction does not upgrade the evidentiary status of the result.

## Files

- `F9b-refusal-pair-v3.py`, 26,488 bytes,
  `698588bb0e5fb4fd305d34c55fb4fe388c77f2531690fd42c37e4151341de580`
- `pair3/result.json`, `d41a3e5546e1a4fe6683604d4bf237dad97da47e9693fead6428a64494beef81`, 12 checks, 0
  failed
- `pair3-unmatched/result.json`, `078b4e39f5a8a2f39f4e7b8c34de5dcd344c4faff0fe07a9a0f27df0cad1b351`,
  12 checks, 2 failed (H2 and H3)
- `RESULT-refusal-pair-v3.txt` and `RESULT-refusal-pair-v3-unmatched.txt`, the transcripts of both runs
- `EXPECTATION-v3.md`, what a correct run of this archive produces, written before the run
- `RUN-v3.txt`, how to run it
