# Delivery log

Append-only. Every file that leaves this repo gets a row: path, size, SHA-256, gate result, who
received it, and how. A file that is not in this table has not been delivered, whatever the chat says.

`python3 TOOLING/pipeline.py log <path> --to "Name" --how "Drive link, hash in message"` writes the
row and runs the gate in the same command.

The two rows below are the files this repo can already account for from before the log existed. Their
hashes were taken from the working tree on 2026-11-06 and are recorded here so that later sessions do
not have to re-derive them. Neither has been confirmed sent.

| When | File | Size | SHA-256 | Gate | To | How |
|---|---|---|---|---|---|---|
| 2026-11-06 | `CLIENTS/foray-dunin7/2026-11-06/FINDINGS-02-register-entries-v3.md` | 24,373 B | `b0217774fb04989c3a534845c7862e5c6fd97de391847f249430539bb7cef094` | pre-gate | Marvin (not confirmed sent) | Drive upload, hash verified after download |
| 2026-11-06 | `PROJECTS/2026-10-30_behar-host-failure-benchmark/REMEDIATION-SCOPE-2026-11-06.md` | 12,669 B | `0d40270a36e717a9dd7275a47fb756ffccf3741ab07d0ffecda5a5347d32da1c` | pre-gate | Behar (not confirmed sent) | Drive upload, hash verified after download |
