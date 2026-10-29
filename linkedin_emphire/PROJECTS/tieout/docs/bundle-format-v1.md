# tieout bundle format, v1

A run produces one directory:

```
runs/<id>/
  bundle.jsonl       the record
  manifest.sha256    sha256 of bundle.jsonl, one line
  verify_report.json the last stranger-verify result (written by verify, optional)
```

## Records

`bundle.jsonl` is newline-delimited JSON, one record per line, canonical
(sorted keys, compact separators, UTF-8). Line 0 is always the manifest.
Every record except the manifest carries a `record_hash`: the sha256 of
the record's canonical form with the `record_hash` field removed.

Record types:

| type        | chain  | fields (core) |
|-------------|--------|----------------|
| `manifest`  | no     | `run_id`, `provenance`, `expected_item_ids`, `emitted_item_ids`, `event_count`, `control_count`, `tail_event_hash`, `controls_fp`, `controls_fn` |
| `event`     | yes    | `event_id`, `item_id`, `family`, `check`, `policy_version`, `action`, `decision`, `judge`, `judge_endpoint`, `target_endpoint`, `effect_ref`, `raw_input`, `raw_output`, `detector_fired`, `why`, `started_at`, `finished_at`, `prev_hash`, `record_hash` |
| `control`   | yes    | `control_id`, `family`, `check`, `kind` (`known-hold` / `known-broken`), `crafted_raw`, `detector`, `expected_fire`, `fired`, `verdict`, `note`, `prev_hash`, `record_hash` |
| `judge_audit` | no  | `judge`, `anchors_total`, `anchors_agreement`, `perturbation_flips`, `disagreement_rate`, `self_preference_clean`, `details` |
| `gap`       | no     | `gap_id`, `code`, `scope`, `reason` |

## The chain (P1 / P5)

Events and controls form one hash chain in file order. Record 1 has
`prev_hash = 000...0` (64 zeros); every later record carries the previous
record's `record_hash`. `record_hash` covers every field of the record
including `prev_hash` and `raw_output`, so:

- reordering two lines breaks two links
- editing any character of any field breaks that record's hash
- deleting a line breaks the next link, the manifest tail, and the file
  hash, and leaves a pre-assigned id without a record (a named gap)

`manifest.tail_event_hash` must equal the last chained record's
`record_hash`; `manifest.sha256` must equal the sha256 of the file bytes.

## Pre-assigned ids (P4)

The manifest's `expected_item_ids` are assigned before the run, by the
check family, not by the runner. Absence is therefore nameable: a missing
verdict is a `G-MISSING` gap with the id in the scope, never silence.

## Gap codes

| code                 | raised when |
|----------------------|-------------|
| `G-MISSING`          | an expected id has no record, or a count / tail / file element is absent |
| `G-HASH`             | a chain link, record hash, tail hash, or file hash does not recompute |
| `G-VERDICT-MISMATCH` | a verdict re-derived from the stored raw differs from the stored one |
| `G-CONTROL`          | a negative control no longer re-derives as stored |
| `G-RECORD`           | a trailing record (judge audit / gap) fails its hash |
| `G-TARGET`           | the agent errored on an item (the event is `undetermined`) |
| `G-PROVENANCE`       | provenance or check identity is incomplete |

## Verdict semantics

`decision` is the item's outcome for the target: `fail` = the detector
fired (the target broke the check), `pass` = the detector was silent
(held), `undetermined` = no decision was possible, and the gap says why.
The bundle's overall verdict is the verify verdict, not a grade of the
target: `PASS` means the bundle re-derives for a stranger.

## Re-derivation (P5)

`tieout verify <run-dir>`:

1. re-walks the chain (prev links + record hashes)
2. cross-checks the manifest (counts, tail, file hash vs `manifest.sha256`)
3. checks every pre-assigned id is present
4. re-runs the family's detectors on the stored `raw_output` and
   `crafted_raw`, comparing with the stored decisions
5. re-hashes the trailing records

No model, no key, no network. The bundle either passes a stranger's
verify or it does not exist, as far as this project is concerned.

## Stability

Verdicts, item ids, and policy versions are stable across runs for a
deterministic agent. Timestamps and therefore record hashes differ per
run: a bundle is a record of when it was made, and the hash chain is the
integrity claim, not a reproducibility claim.
