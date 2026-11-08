# What a correct run of this archive produces

Written before the run, so that a result which differs is visible rather than explained afterwards.

## Matched configuration

Command: `python3 F9b-refusal-pair-v3.py --bench . --out ./pair3 --match-host-id`

- Twelve checks, none marked FAIL, exit code 0.
- Result file SHA-256 `d41a3e5546e1a4fe6683604d4bf237dad97da47e9693fead6428a64494beef81`.
- Both refused replies: 90 bytes,
  `1ca16a0ad93f2650f6163c9fe128ea84ed4297321c598d6c35ed18fbaa3c01c7`, trailing newline present.
- Retried replies: equal to each other in bytes.
- 26 calls, 26 sequential exchanges.
- Durable verdict records: conflict-wire 3, conflict-host 2, verdict-wire 0, verdict-host 0.
- Acknowledged verdict requests: conflict-wire 1, verdict-wire 0, the two host executions report null.
- Restart state: `conflicted` for both conflict executions, `null` for both verdict executions.
- Whole host journals not equal; equal apart from the verdict records and the restart boot record.
- Replayed on restart: 5 of 5 and 3 of 3.
- Selected host events: identical in full.

## Distinct-action-id configuration

Command: `python3 F9b-refusal-pair-v3.py --bench . --out ./pair3-unmatched`

- Twelve checks, exactly two marked FAIL, H2 and H3, exit code 1.
- Result file SHA-256 `078b4e39f5a8a2f39f4e7b8c34de5dcd344c4faff0fe07a9a0f27df0cad1b351`.

## What would count as a failure of the artifact rather than of the experiment

- Two runs of the same configuration producing different result hashes.
- A result file containing an absolute path, a temporary directory name or a process identifier.
- A check passing while its detail contradicts it.
- Any count attributed to an execution that did not produce it.
