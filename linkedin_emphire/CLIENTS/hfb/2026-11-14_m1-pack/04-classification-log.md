---
deliverable: doc
id: 2026-11-14_m1-classification-log
date: 2026-11-14
audience: collaborator
status: ready
approved: no
contents: twenty-two suite checks at two revisions, the artifact difference, the modes M1 does not touch
---
# Classification log: what the change moves, and what it does not touch

Two runs of the same suite, one on the pinned revision and one on the tree carrying the patch.
Both exit 0 and print `VERDICT: every check holds`. The two verifier outputs were diffed: they
are byte-identical, all thirty lines including the class counts, the M3 gap sentence and the
decision-time sentence. The table below is that output, twice, and it is the whole of it.

## All twenty-two checks

| check | class | pinned revision | with the change |
|---|---|---|---|
| reconcile | meta | holds | holds |
| A | P | holds | holds |
| A' | P | holds | holds |
| B | P | holds | holds |
| B.decision | P | holds | holds |
| B.wal | P | holds | holds |
| B.effect | P | holds | holds |
| C | P | holds | holds |
| C' | P | holds | holds |
| C'' | P | holds | holds |
| D | V | holds | holds |
| D' | V | holds | holds |
| D'.effect | V | holds | holds |
| journal-first | P | holds | holds |
| repair-quarantine | P | holds | holds |
| conflict | P | holds | holds |
| reply-checked | P | holds | holds |
| artifacts-complete | meta | holds | holds |
| scenarios-ran | meta | holds | holds |
| store-records-framed | meta | holds | holds |
| line-endings | meta | holds | holds |
| no-wall-clock | meta | holds | holds |

Class counts at both revisions: P 13 of 13, V 3 of 3. Evidence: `02-baseline-failure/suite-verify.log` and `03-change/suite-verify.log`. Those two
files carry the same sha256 in `05-SHA256SUMS.txt`, `b3f990f4...`, which is the byte-identity
claim provable in one line without trusting this document.

## What M1 does not touch

These are unchanged by the patch, line for line, and are named so that the claim has edges:

| mode | what it would have moved if the patch had reached it |
|---|---|
| A, A' | the expectation path, and the silence when no expectation was registered |
| B, B.decision, B.wal, B.effect | local verdict commit, recovery, and the timestamp the host wrote before the ship |
| C, C', C'' | the M3 named gap: name with content, name only, silence |
| D, D', D'.effect | verification against the key the record carries, and quarantine of a record that does not verify |
| journal-first | a store that cannot journal a verdict does not report it as known |
| repair-quarantine | a repair that shortens a journal keeps the bytes it removed |
| reply-checked | the host logs an effect only when the store's reply names the action asked about |
| reconcile | the store's reconciliation report against what its own journal implies |

## The exact artifact difference

The suite writes 24 artifact files. Comparing the pinned run to the patched run:

- **23 of 24 files byte-identical.** Including `host-*.jsonl`, `wal-B.jsonl`, `reconciled.json`,
  `store-state.json`, `lookups.json`, the three probe directories and the manifests.
- **`port.txt` differs in four places.** These record the ephemeral port each store process bound
  to. They are not evidence about anything and they differ between two runs of the same revision too.
- **`store.jsonl`, the one substantive difference.** Both runs write 18 lines. Sixteen are identical.
  The two that differ are the C-9009 verdict and the C-9009 conflict, and in both cases the only
  difference is one added field:

```
pinned:  {"kind": "verdict",  "action_id": "C-9009", "store_seq": 17, ...}
patched: {"kind": "verdict",  "action_id": "C-9009", "store_seq": 17, "batch": {"id": "c227f34964b1236d", "index": 1, "of": 2}, ...}
pinned:  {"kind": "conflict", "action_id": "C-9009", "store_seq": 18, "second_seq": 17, ...}
patched: {"kind": "conflict", "action_id": "C-9009", "store_seq": 18, "second_seq": 17, "batch": {"id": "c227f34964b1236d", "index": 2, "of": 2}, ...}
```

No field was removed, no sequence number moved, and the conflict record still carries
`first_seq` and `second_seq`, which is why the suite's own `conflict` check still passes without
being edited.

## What the change adds, and where it lives

One method on the journal, `append_batch`: it assigns the next two sequence numbers, marks both
records with a shared batch id that is computed from their content, writes both lines in one
write call, and calls fsync once.

One branch in replay: a batch that arrives with fewer records than its marker declares is
withheld from the index and named. Withheld records still consumed their sequence numbers, so
numbering does not reuse them. The store prints one line when this happens, and appends a
`repair` record naming the withheld batch, its seqs and the rule.

One line in the store's start-up: if records were withheld, say so instead of presenting a
shorter history as the whole one.

## The classification the last exchange settled

V04 inside F-08 is recorded here as **scope**, on the ruling given in the exchange of 14
November, with the reasoning that came with it: the original mutation left the timestamp
unchanged, the synthetic skew was detected by B and B.wal, so what the record establishes is
consistency with the WAL under the tested conditions, and independent timestamp provenance
remains unverified. The published register still reads disputed; this pack does not change it
and does not claim it has. N13 is untouched and undecided, and stays with the code question of
whether the check produces the report it requires.

## What is still not written

S3, S4 and S5 are not in this pack. S4 remains open on its own schedule and nothing here is
offered as evidence about it.
