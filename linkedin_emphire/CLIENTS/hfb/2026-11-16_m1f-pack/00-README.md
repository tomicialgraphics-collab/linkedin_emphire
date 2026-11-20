---
deliverable: pack-readme
id: 2026-11-16_m1f-pack-readme
date: 2026-11-16
audience: collaborator
status: ready
approved: no
contents: the documented guarantee, scoped to the complete record, and the torn-line limitation pinned rather than fixed
---

# M1f: what the refusal guarantee covers, and what it does not

Behar's message of 16 November at 21:42 confirmed M1e and asked for one thing before merging: scope
the documented guarantee to the complete record missing its final newline, and record the limit he
found, where recovery quarantines a genuinely torn line before the retry's append open fails and
the reply still says `disk_state: unchanged`.

**No behaviour changed in this revision.** The code that decides anything is byte-identical to M1e
except for the module docstring. What changed is that the claim is now written down at its real
size, and pinned by a mode, so it cannot quietly widen.

## The limitation, reproduced

A journal with a valid verdict, then half a record appended by hand as a crash would leave it:

| step | bytes |
|---|---|
| before recovery | 341 |
| after recovery | **297** (44 torn bytes moved into `store.jsonl.quarantine-1.bin`, sha256 `5e5ded7a…`) |
| after the refused retry | 297 |

The recovery is correct: a torn line is damage, not a gap, and the journal is unusable until it is
quarantined. The retry that follows fails on `open` and answers `ok: false, durable: false,
disk_state: "unchanged"` — which is true of **the retry** and says nothing about the 44 bytes
recovery removed moments earlier.

He is right that this is not covered by the guarantee, and right that it should be recorded rather
than described as if it were.

## What changed

**`bench/store.py`.** The module docstring now carries the scope in four sentences: the guarantee
covers a complete record whose terminator never arrived; a torn line is damage and recovery
quarantines it before any append is attempted; `disk_state: unchanged` on the retry is therefore a
claim about that append and not about the file; and f25 pins both halves.

**`audit/README.md`.** A section, *What the refusal guarantee covers*, states the same thing for a
reviewer, and the mode table now lists f23, f24 and f25. The count in the usage line was stale at
nineteen; it is twenty-two.

**`audit/regressions.py`.** The new mode.

## The new mode: f25

It pins the limitation instead of removing it, and it says so in its own docstring. It asserts four
things:

1. recovery quarantines exactly the torn bytes, whole and named, with the sha256 of what was
   appended by hand;
2. recovery does not call it a gap (`journal_gap` stays None), because it is damage;
3. recovery does change the file, from 341 bytes to 297 — the limitation, asserted so it stays
   visible if somebody later "fixes" it into a gap;
4. the retry that follows changes nothing itself, and its reply is `unchanged`.

**f25 passes on M1e as well as on M1f**, and that is the honest result rather than a weak one: the
behaviour was never broken, the claim about it was too broad. The mode exists so that the scope is
tested where it is stated.

## Why the limit is recorded rather than fixed

The two repairs pull against each other. Recovery has to remove a torn line to produce a journal a
reader can trust. A refusal has to leave the file alone. Both are right, and only one of them can
own the file at the instant the retry arrives.

The alternative, making the reply distinguish "my append changed nothing" from "recovery changed
something before me", is a change to the reply shape that would need its own review. It is written
here as the next thing to do if he wants it, not smuggled into a documentation revision.

## What he can run

```
python3 audit/regressions.py f25          # the limitation, pinned
python3 audit/regressions.py f24          # the case that was fixed, still caught
python3 audit/regressions.py              # all twenty-two, 22 caught, 0 missed
python3 run.py && python3 verify.py artifacts/<run>
```

`03-this-change/` holds those outputs as produced and `02-previous-change/` holds f25 run against
the M1e `bench/store.py` with this change's audit code, since f25 does not exist before this change.
`revision.txt` in each names the file hashes.

## Corrections since first delivery

**`04-CORRECTION.md`.** The reviewer found that `02-previous-change/revision.txt` carried the M1d
hashes under an M1e label. Checked and confirmed, and it is corrected in place. Two further defects
came out of the check: f25 is output-identical on M1d, M1e and M1f, so it identifies no tree, and
the patch in `03-this-change/` is a diff from M1d rather than from M1e.

**The reconstruction chain, stated rather than inferred.** `base 99f25cab` (the tree as reviewed),
then the M1d patch, then `03-this-change/patch.diff`. Applying M1e first and this patch second fails
with rejected hunks, because the M1e guard is already inside this patch. `base → M1d → M1f`
reproduces `0989c8db`, `490de706`, `ae147a28` exactly.

**`06-f25-tree-check/`.** The three f25 runs behind that statement, one per tree, all byte-identical,
with the full twenty-two mode run and the verify verdict produced on the rebuilt M1f tree.
