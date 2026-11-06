# To Marvin: round 3

Two attachments, both hashed. Nothing in this one is a link, so you and I hold the same bytes.

**1. `foray-probe.mjs`**, 11,827 bytes, SHA-256 `c91be299ff59076f0a49f43fd6a4f01e1f98fad7fe478e46b9b2225efecaa326`.

That is the hash you already have, and it is the file you could not find: same build, unchanged. 292 lines, no dependencies, 23 cases. It takes one argument, the verifier folder (the one holding `lib/`, `vectors/`, `test/`, `foray-verifier.mjs`):

```
node foray-probe.mjs <path-to-verifier-folder>
```

One line per case, id, outcome, check, reason. Exit code 0 if it ran, 2 if the folder does not look like a verifier, so a wrong path cannot read as a passing run. Nothing is fetched and nothing outside the folder is read.

Two things in its output that will look wrong and are not.

Three lines beginning `SYNTH extent 0..412` return INVALID with `history record at seq_no 1 is not the anchored transaction`. Those are my own construction, not your code. I add a segment to the header, recompute the anchored value and write it into both canned chain sources; in those three cases I built the extent and did not rebuild the anchor binding, so the anchor check fires before the stream walk is reached. They are superseded by the `SYNTH-C` block, which is the same fixture with the binding rebuilt, and `SYNTH-C` is the group to read.

`SYNTH-D` and `SYNTH-E` name the cases for the two items below. Everything else is a shipped vector with only `context.streamHistory` changed.

**2. `FINDINGS-02-register-entries-v4.md`**, 29,128 bytes, SHA-256 `84fdf1e878bc9b8582e0b1601b6444f4c4f6deb54c750a69d3b6a988c8f04d5b`.

This is the revised register. It carries your corrections, and four changes from the copy you may have: W-01g is renumbered W-04 throughout and recorded as your identifier, not mine; f and h each carry your report against `05267a36a57edf31bae2c2b9390f85df9c899a43` and both are marked pending my run rather than closed; the custody wording point records your change and the 12 cases where it shows; and there is a status table at the head of the open items so the commit, the report and my position sit in one place. If you were sent an earlier draft of this file, its hash began `b0217774` and it is void.

## What your commit should do to the 23 cases

I have not run `05267a36`. This is the expectation, written down before the run so that the run can contradict it.

| case | on `b890d2c` plus patch v0.3 | expected at `05267a36` |
| --- | --- | --- |
| `SYNTH-D`, declared seq 500 outside segment 0..412 | VALID | **INVALID**, your f fix. The only outcome that should change |
| `SYNTH-E`, segment id and `stream_context.stream_id` differ | VALID | VALID, unchanged. W-04 is a ruling, not a repair, so the code should still be silent here |
| the 12 MATERIAL_UNAVAILABLE cases | same outcome, missing range named | same outcome and same range. The reason string should change in its closing clause only, `responsible custodian: FORAY archival node operator` giving way to the stream-history custodian where the context names one |
| the other 9 INVALID and VALID cases | as recorded in the register | identical |

If `SYNTH-D` moves and the other 22 hold, f closes and the custody clause is confirmed. If `SYNTH-D` returns INVALID with a reason that names neither the stream nor the declared position, the outcome is right and the diagnosis is thin, and I would put one line in the reason.

`SYNTH-E` staying VALID is the point of W-04, not a regression. `SYNTH-C` already shows the extent branch working when the identifiers agree, so the ruling you make there has both a working branch to describe and a failure to remove.

## h, which the probe cannot reach

No case exercises h, and the reason is worth keeping: the packet ships five repository vectors and none carries a `stream_context`, so the branch that would have rejected them is unreachable from the packet as shipped. The test, once you want it in the probe: take a `checkpointed_repository` vector that validates, add the `stream_context` and history from `rotated-chain-seam`, leave `anchor.chain_tx_id` at `"unused-for-repository-class"`, and expect VALID before your change and VALID after it, with the anchored extent still compared. Before your change that bundle returns INVALID, `history record at seq_no N is not the anchored transaction`, whatever its history holds. I will add it as a Group C case if you tell me a repository vector and a `stream_context` can be put in one bundle without breaking the vector's own anchoring, or if you send the tree and I can find out.

## To run the rerun against your commit

Send the archive at `05267a36`, or run it yourself and send the 23 lines. Either is fine and the second is faster. What I will not do is report the 23 cases against a commit I have not executed.
