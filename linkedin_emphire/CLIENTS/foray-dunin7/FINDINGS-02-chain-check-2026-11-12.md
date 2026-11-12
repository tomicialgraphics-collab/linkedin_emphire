---
deliverable: doc
id: findings-02-chain-check-2026-11-12
date: 2026-11-12
audience: internal
status: draft
client: FORAY (Dunin7)
---

# Chain check of the three anchors, 12 November 2026

Why this exists: the reply to Marvin makes four claims about the public chain, and a claim about a chain
should be re-runnable by somebody who does not trust this file. Every value below came from the public
Kaspa API at `api.kaspa.org/transactions/<id>` on 2026-11-12, with no repository, no verifier and no
custody material. Anyone with a browser can repeat it.

## Payload against the anchored value in the v10 status record

| batch | transaction | payload returned | anchored value in v10 | block time (UTC) |
| --- | --- | --- | --- | --- |
| 1, seq_no 0 to 2 | `6ca065b965716a58097d0671a2308874b3aeb15a551e8fe7dd76c23e4214e684` | `3b8f2d15a1bf6426a57704e5307075511ef220c32d18480d7db3fad94a67ea2e` | same | 2026-11-10 12:20:15.128 |
| 2, seq_no 3 to 5 | `17f8ce56028053ec84644a39e4bd98917fd0ac7fde8d005878281c809f3738cb` | `32a656672d6b4aed6130793e25bf2689ffd2db061ff98645666c1b27fac4424f` | same | 2026-11-10 15:17:42.986 |
| 3, seq_no 6 to 8, Tier-2 aggregate | `6944db124ca819ec355713a1556640ae80843316394d56c1b72f495e11c03c12` | `9ca34d90aee5a0237125d9906f9e3b12e5e0733e86264f4a95f69caa1724cfb3` | same | 2026-11-12 16:28:25.637 |

Each payload is 64 hex characters, so 32 bytes, and nothing else is carried. All three transactions report
`is_accepted: true`. The block times come from the `block_time` field, not from `accepting_block_time`,
which is 145 to 1836 ms later depending on the transaction.

## The lineage observation

- Batch 2's input names `6ca065b9…4214e684` as its previous outpoint, so batches 1 and 2 are joined at the
  transaction level as well as by the header chain in item 11.
- Batch 3's input names `a4edda51ff38165b9f8754c2a52274f0898575245b7357c9fb878c20f62a6d63`, which is
  neither of the earlier transactions. Batches 2 and 3 are therefore not joined by spend.
- All three pay the same output address, `kaspa:qr2kfwx69r8t5tmwrcny2wte07wx5ywnewa4l2c0wu4zjwlpgejax8rsacjwn`,
  which is consistent with one operator and is not evidence of one stream.

What follows: the public chain supports three anchors, each committing the published value, each with a
block time. It does not support the extent of seq_no 0 to 8 on its own, because the third anchor's
membership in the stream lives in the client header inside the aggregate leaf, and the payload is the
aggregate root rather than the header. The header is recoverable from the proof bundle, not from the chain.
This is consistent with v0.13 section 10 item 12, which states the single-leaf limit; it is a separate
observation, that a browser user cannot join the third anchor even in principle.

## Not checked here

The 157 byte client header, its SHA-256 `4e9100e1…`, the parent salt, the inclusion paths, and the
`prev_header_hash` linkage all come from custody material that is not public. The verifier's VALID,
MATERIAL_UNAVAILABLE and INVALID results were not reproduced: no repository access and no verifier.
Amendment v0.26 could not be opened, since the raw path returns 404 and the repository requires a login.
