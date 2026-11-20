---
deliverable: pack-readme
id: 2026-11-16_m1e-pack-readme
date: 2026-11-16
audience: collaborator
status: ready
approved: no
contents: the fourth combination, why the refusal was not side-effect free, and the mode that now holds both
---

# M1e: the retry that cut the record it was refusing to append onto

Behar's message of 16 November at 09:18: the three M1d fixes hold, and one combination still
breaks gap preservation. A batch is interrupted immediately before its final newline, the rollback
is forced to fail, and the retry returns `disk_state: unchanged` while moving the final record out
of the journal and into quarantine. After a restart the gap is gone from `state`, and the store
accepts writes again.

All of that reproduced here, byte for byte, and the cause is one step earlier than it looks.

## What happened

`append()` and `append_batch()` already refused to write while a gap stood, and the refusal says
so: *refusing to append until that gap is resolved, and refusing to cut it*.

But the refusal is not the first thing that runs. A write whose rollback was not confirmed calls
`_resync()` first, and `_resync()` did two jobs: re-derive the sequence from the file, and cut the
bytes after the last newline into a quarantine file. When the tail is a torn line, cutting it is
correct. When the tail is a **whole record whose terminator never arrived**, cutting it is the
repair the M1d guard was written to prevent, and it happened before the guard could speak.

So the reply was `ok: false, durable: false, disk_state: "unchanged"` on a file that had just
changed. The withheld record moved to `store.jsonl.quarantine-1.bin`, the journal lost 324 bytes,
and the next start-up had nothing to report because the file no longer ended mid-record.

The reviewer's numbers, reproduced on the revision he holds:

| | M1d, the revision he holds | M1e |
|---|---|---|
| journal after the refused retry | 875 → **551 bytes** | 875 → **875 bytes** |
| withheld record still in journal | no | **yes** |
| quarantine file written by the retry | `store.jsonl.quarantine-1.bin` | **none** |
| gap after restart | **None** | `store_seq 4, conflict, 324 bytes` |
| write after restart | **accepted** | **refused** |

## What changed

One guard, in the place the damage was done.

`_unterminated_tail()` already had the test that distinguishes a gap from damage: the tail parses,
and its digest agrees with its own bytes. That test is now `_gap_from_tail(tail, start)`, a static
method used by both start-up and `_resync()`, so a repair cannot apply a looser test than the one
that reports the gap.

`_resync()` applies it to the tail it is holding, before anything is copied or cut. If the tail is
a whole record, it sets `self.gap` and raises the same refusal the append would have raised. The
file is left exactly as found, and the quarantine is not touched. A torn line still takes the old
path, because a torn line is damage and cutting it is a repair.

The rule the code now follows: **a refusal may not have a side effect.** If the reply says the
file is unchanged, nothing in the path that produced the reply may have written to it.

## The new mode: f24

One case, in a copy of the repository, with the crash arranged in the case rather than in the
store: a file wrapper that writes every byte of the batch except the last, then raises. The
failpoint refuses the subsequent rollback, so the store reaches the state the reviewer described
without any new production code being added to reach it.

It asserts three things:

1. the crash is answered `durable: unknown` (the known state, unchanged from M1d);
2. the refused retry leaves the journal byte-identical, and writes no quarantine file;
3. after a restart the gap is still reported, and a write is still refused while it stands.

On the revision he holds it reports `MISSED` with the numbers above. Here it passes.

## What he can run

```
python3 audit/regressions.py f24          # the mode on its own
python3 audit/regressions.py             # every registered mode
python3 run.py && python3 verify.py artifacts/<run>
```

`03-this-change/` holds all of those outputs as they were produced, `02-previous-change/` holds the
same mode run against the revision he has, and `revision.txt` in each names the two file hashes so
the two trees cannot be confused.
