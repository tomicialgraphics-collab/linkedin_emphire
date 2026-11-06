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
| 2026-11-06 | `CLIENTS/foray-dunin7/2026-11-06/FINDINGS-02-register-entries-v4.md` | 29,128 B | `84fdf1e878bc9b8582e0b1601b6444f4c4f6deb54c750a69d3b6a988c8f04d5b` | PASS 0/0 (exported) | Marvin (not confirmed sent) | to be attached with the round 3 reply |
| 2026-11-06 | `CLIENTS/foray-dunin7/repro/foray-probe.mjs` | 11,827 B | `c91be299ff59076f0a49f43fd6a4f01e1f98fad7fe478e46b9b2225efecaa326` | n/a (code, not prose) | Marvin (not confirmed sent) | re-sent at his request; hash matches the build he was given |
| 2026-11-06 | `CLIENTS/foray-dunin7/2026-11-06/REPLY-3-to-Marvin.md` | 4,839 B | `b42c668bf69bafe5deb6583eb486f943b808eaf710821637ea90a88e39aafd2a` | PASS 0/0 (exported) | Marvin (not confirmed sent) | round 3 message, carries both attachments and the 23-case expectation |

The v3 row above is now void: v4 supersedes it, and the reason for the new hash is recorded in the v4 header.
