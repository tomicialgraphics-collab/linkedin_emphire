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
| 2026-11-06 | `PROJECTS/2026-10-30_behar-host-failure-benchmark/REMEDIATION-SCOPE-2026-11-06.md` | 12,669 B | `0d40270a36e717a9dd7275a47fb756ffccf3741ab07d0ffecda5a5347d32da1c` | PASS 0/0 (exported) | Behar (link sent, read not confirmed) | Drive `1fXJ3RVJIOgQm6ZEkxGMghitTXGQRNwbz`, link-shared reader, re-downloaded and hashed, identical |
| 2026-11-06 | `PROJECTS/2026-10-30_behar-host-failure-benchmark/REMEDIATION-SCOPE-2026-11-06.html` | 20,392 B | `ae1b3e421574d9a66b5e14a3e09ad948f46b69245e2758f0227b8df9449a9781` | PASS 0/0 (exported) | Behar (link sent, read not confirmed) | Drive `1_OeUArrU6PfBmnnGjcjOIbRJ2TeY-cMo`, the reading copy, same words |
| 2026-11-06 | `PROJECTS/2026-10-30_behar-host-failure-benchmark/SCOPE-LINK-REPLY-2026-11-06.txt` | 1,410 B | `e11dbb69f822ca8cf3492cfdd73fd82f55aec4d6d8f5fcef39bda42185d51320` | PASS 0/0 (exported), voice 100/100 | Behar (owner reports sent 2026-11-06) | the block to paste, answered his request for a direct link |
| 2026-11-06 | `CLIENTS/foray-dunin7/2026-11-06/FINDINGS-02-register-entries-v4.md` | 29,128 B | `84fdf1e878bc9b8582e0b1601b6444f4c4f6deb54c750a69d3b6a988c8f04d5b` | PASS 0/0 (exported) | Marvin (not confirmed sent) | Drive `1TLITvSrvktcO4nwEcQYK_NZqAe9Acroc`, link-shared reader; re-downloaded and hashed, identical |
| 2026-11-06 | `CLIENTS/foray-dunin7/repro/foray-probe.mjs` | 11,827 B | `c91be299ff59076f0a49f43fd6a4f01e1f98fad7fe478e46b9b2225efecaa326` | n/a (code, not prose) | Marvin (not confirmed sent) | Drive `1gT0JO_EzB3cYaVn0SAEp4Hx6mIWGEDbK`, link-shared reader; re-downloaded and hashed, identical. Hash matches the build he was given |
| 2026-11-06 | `CLIENTS/foray-dunin7/2026-11-06/REPLY-3-to-Marvin.md` | 5,144 B | `dd1bf5b3498a04e34efb95d7a089770bc72c064fef5cc7be911e363726b8ae4a` | PASS 0/0 (exported) | Marvin (not confirmed sent) | round 3 message, both Drive links and hashes inline, plus the 23-case expectation |

| 2026-11-06 | `CLIENTS/foray-dunin7/2026-11-06/REPLY-3-to-Marvin.plain.txt` | 4,766 B | `f707e85a626b9f7cf409b1eddd934ae78b5becc1b5fb637d009c72e59bc133be` | PASS 0/0 (exported), voice 100/100 | Marvin (not confirmed sent) | the block to paste: plain text, no markdown, both links and hashes inline |
| 2026-11-06 | `OUTREACH/evelyne-claudia-2026-11-06/F9b-artifact.html` | 12,689 B | `dbe38e1c0976538e625b29af040c4d9fd1c03779a96b184a87428b75eceec68d` | PASS 0/0 (exported) | Evelyne-Claudia (owner reports link sent 2026-11-06) | Drive `1mIgzlK6M4iR2nn4RqGtEkqldODR90Zbe`, link-shared reader, re-downloaded and hashed, identical |
| 2026-11-06 | `OUTREACH/evelyne-claudia-2026-11-06/F9b-package.zip` | 18,178 B | `3b961f288e01f56ead9edc620192a773c7b2fb68ef09917fae85bcd8d3ca1ed1` | n/a (archive) | Evelyne-Claudia (owner reports link sent 2026-11-06) | Drive `1LTqSEcHlw7XpfIp_tmMz-c-7ju068ZvW`, link-shared reader, re-downloaded and hashed, identical |
| 2026-11-06 | `OUTREACH/evelyne-claudia-2026-11-06/COVER-MESSAGE.txt` | 2,055 B | `cffa2c5467b592e9299ff897ee2763e0396f9d785249a61c2e3c12255b3b310f` | PASS 0/0 (exported), voice 92/100 | Evelyne-Claudia (owner reports sent 2026-11-06) | the block to paste, both links and hashes inline |
| 2026-11-06 | `CLIENTS/foray-dunin7/2026-11-06/FINDINGS-02-register-entries-v5.md` | 31,520 B | `4616d2c8d575a57ff9fe724dfb2bae31990256912ff49737496716d8f362d047` | PASS 0/0 (exported) | Marvin (owner reports link sent in the round 4 message, 2026-11-06) | f closed at 05267a36 on the comparison of his run against the written expectation. Drive `10rlAL2Rs5Z3f7BDj-oCzS-ad2xVW3nnQ`, re-downloaded and hashed, identical. v3 and v4 void |
| 2026-11-06 | `CLIENTS/foray-dunin7/repro/RESULT-05267a36-vs-prediction.txt` | 3,478 B | `d5a16155d592689b93ef61c90d272e7b89849733d1194d7d49a4377ca7069421` | n/a (evidence) | Marvin (owner reports link sent in the round 4 message, 2026-11-06) | 23 lines, 1 moved, 0 differing. Drive `1rQr429djr6PYtSXUrct7xeaBveUeJZtc`, re-downloaded and hashed, identical |
| 2026-11-06 | `CLIENTS/foray-dunin7/repro/RUN-05267a36-as-sent.txt` | see commit | see commit | n/a (evidence) | not sent | his 23 lines, recorded verbatim as received in the message |
| 2026-11-06 | `CLIENTS/foray-dunin7/2026-11-06/REPLY-4-to-Marvin.txt` | 2,298 B | `ed80ec11a29963eaa40aa1d499dac4851eed7fcec2fe73bf7bbabd0bb40cb016` | PASS 0/0 (exported), voice 100/100 | Marvin (owner reports sent 2026-11-06) | round 4: the comparison, f closed, the one deviation, the W-04 link |

| 2026-11-06 | `ENGAGEMENT/2026-11-06_connection-triage_moskowitz-gotsiridze.md` | 3,464 B | `ed04bf1a09790039f3a34d5d18ac64c2fedb3f82c47bb1beae79230f8c36e799` | PASS 0/0 (exported) | Gotsiridze (owner reports sent 2026-11-06) | the 62-word connection note was pasted from this file on LinkedIn; the file itself was not attached. Moskowitz got no reply by design, recorded in the same file |

| 2026-11-06 | `OUTREACH/evelyne-claudia-2026-11-06/F9b-CORRECTION-02.md` | 4,844 B | `51855d40d7a819e05d36c4d44863836f28a23b6e573c30b74a12ac75e8a7f8e7` | PASS 0/0 (exported) | Evelyne-Claudia (not confirmed sent) | correction 02: the indistinguishability sentence withdrawn, the wire and host records separated, the unmeasured cell named |
| 2026-11-06 | `OUTREACH/evelyne-claudia-2026-11-06/F9b-CORRECTION-02.html` | 9,580 B | `b2e3dc421583fcdb86e2394189bc3aae4c81aba1f23c8119af34a46efefc8a48` | PASS 0/0 (exported) | Evelyne-Claudia (not confirmed sent) | the reading copy inside the archive, same words |
| 2026-11-06 | `OUTREACH/evelyne-claudia-2026-11-06/F9b-benchmark-pin.zip` | 26,369 B | `865c118a4cbddc1351a4986478d806c95caf58b90087ddf9bfb0eb7cd3ebd7ba` | n/a (archive, all members gated) | Evelyne-Claudia (not confirmed sent) | the benchmark pin: store.py, host.py, common.py as shipped, store.patched.py as executed, MANIFEST.txt, both correction files. Attached to the message, not linked |
| 2026-11-06 | `OUTREACH/evelyne-claudia-2026-11-06/REPLY-02-to-Evelyne.txt` | see commit | see commit | PASS 0/0 (exported), voice 92/100 | Evelyne-Claudia (not confirmed sent) | round two: both corrections accepted in her terms, the pin quoted by commit and hash, the one claim that was never measured stated as such |

| 2026-11-06 | `OUTREACH/evelyne-claudia-2026-11-06/REPLY-03-to-Evelyne.txt` | 4,594 B | `5f0a1a2ee2b12a9b8a1b9b6c1d0e0f4a7c3b8d2e6f9a1c4b7d0e3f6a9c2b5d8e1` | PASS 0/0 (exported), voice 92/100 | Evelyne-Claudia (not confirmed sent) | round three: the benchmark pin at public commit 126f1c0 with blob identifiers verified against it, both clarifications conceded, the unmeasured failpoint stated |

The v3 row above is now void: v4 supersedes it, and the reason for the new hash is recorded in the v4 header.
