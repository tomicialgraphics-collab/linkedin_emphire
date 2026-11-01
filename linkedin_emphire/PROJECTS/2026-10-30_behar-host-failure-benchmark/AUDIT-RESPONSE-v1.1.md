# Response to the technical audit, version 1.1

Olusanya Timothy. 1 November 2026.

Supersedes version 1.0. What changed since then: the T08 disagreement is
settled, and the P0 patch exists and is tested on two platforms. Everything
version 1.0 said about the other findings stands.

Reviewed: `Teamthy/host-failure-benchmark` at `25cd57f`. Patch: P0 against that
commit, applied to a clean clone, checkable with three commands.

## 1. T08, settled

You are right, and the reason is instructive. We were changing the write-ahead
log at two different moments and both of us described what we saw correctly.

| intervention point | what agrees | what fails | property being tested |
| --- | --- | --- | --- |
| before the store replays | recovered record and WAL | `B` | the timestamp is bound to the host journal |
| after replay completes | nothing | `B.wal` | two files agree with each other |

Changing the log before the store restarts makes the recovered record carry the
altered value, so the pair is self-consistent and the failure lands on the
binding between the timestamp and the counter step the host journal records.
Changing it afterwards leaves the store holding the original value, so the
failure lands on agreement between the files. Same edit, different moment,
different check, and neither is redundant.

Both are now in `audit/regressions.py` as `f2a` and `f2b`. `f2a` requires `B`
to fail and `B.wal` to hold. `f2b` requires `B.wal` to fail. One addition: with
the P0 patch, `f2b` also fails `B`, because the log record's signature no
longer covers its bytes, which is an independent reason and a small
improvement rather than a change of position.

The F2 substance is untouched by any of this, and the patch does not pretend
otherwise. Agreement between a log and a store on the same filesystem, written
by the same process, is consistency and not attestation. What the patch adds
is narrower: a timestamp now has to match a counter step the host journal
contains, so a record cannot carry a decision time the host has no evidence of.
That is a bound, not a witness, and the note says so in the sentence where the
result is reported.

## 2. The P0 patch

Applied to a clean clone at `25cd57f`, with the counterexamples shipped as
tests rather than described.

| change | finding |
| --- | --- |
| WAL records and recovered verdicts are signature-checked, at ingest and in the verifier. An unverified record stays visible and cannot resolve a gap, in `recompute_gaps` as well as in the store | F1, F3, F9 |
| Actor and policy hash compared against the constants in `bench/common.py`; the decision timestamp bound to a counter step in the host journal | F8, F14, F2 |
| A versioned manifest naming every required artifact, and per-scenario event chains, so a deleted journal fails | F5 |
| The verifier never raises; an unreadable artifact produces a report with an explicit unreadable state | F13 |
| Two claims corrected and one phrase: identifiers are registered rather than issued, the suite runs eight scenarios, row M3 is a deliberate exit | F6, F16, F4 |

## 3. What the patch is tested against

`audit/regressions.py`, eight modes, named after the findings:

| mode | at `25cd57f` | with the patch |
| --- | --- | --- |
| f1 WAL verdict flipped, stale signature | accepted | `B` |
| f2a WAL timestamp changed before replay, re-signed | `B` | `B`, `B.wal` holds |
| f2b WAL timestamp changed after replay | `B.wal` | `B.wal` and `B` |
| f3 unsigned verdict, reframed | gap erased | gap stays named |
| f5 seven host journals deleted | accepted | `artifacts-complete` |
| f8 actor and policy rewritten, re-signed | accepted | `D` |
| f13 host journal cut mid-line | traceback | `artifacts-parse`, report written |
| f14 timestamp set to an epoch value, re-signed | accepted | `D` |

Four of these left verification reporting that every check held. Six were
accepted at `25cd57f` in total; all eight are caught now.

On Windows 11 with Python 3.14.5, from a clean clone: 16 of 16 checks hold, 9
of 9 built-in mutations are caught, 8 of 8 counterexamples are caught. The same
on Linux, plus two consecutive runs byte-identical file by file.

Two things will look like regressions and are not. The check count went from 14
to 16. And `example/run` is regenerated, because verdict records now carry a
state and the manifest is version 2; the old example fails the new checks,
which is the correct outcome and would be a problem if it passed.

## 4. What the patch does not fix

Unchanged from version 1.0, and listed in the patch notes under P1 and P2:

- memory updated before the journal append in one path (F11)
- repair that truncates without keeping the discarded bytes (F7)
- duplicate verdicts still resolving to whichever record a component reads
  first (F9's state half)
- the host not validating the store's reply before logging an effect (F10)
- identifiers still chosen by the caller (F6; renamed, not minted)
- an idle socket still able to block the store (F15)
- the verifier still importing the encoder it checks, smaller than before but
  the correlated-oracle problem stays until there is a second encoder
- no CI matrix, so the cross-platform evidence is two runs and not a pipeline

## 5. Claims and publication

The sentence I would stand behind, and the one I would not:

Defensible now: this local, deterministic benchmark shows how prior commitment
and later reconciliation distinguish classes of missing decision evidence under
scripted process failure, and its verifier rejects a set of counterexamples
that it used to accept.

Not defensible, before P1 lands, and not claimed anywhere in the patch:
authenticated recovery, host-loss survivability, institutionally authorised
effects. I accept your decision rule in section 7.1 without qualification.

## 6. Two requests, unchanged

1. Put the 38-case package into the repository as `audit/cases/`, with its own
   runner, next to `audit/regressions.py`. The two sets belong together and
   every fixed finding should keep a test that can fail again.
2. Let me cite the review in the note, as `REVIEW-2026-11-01.md`, once P1
   lands. A demonstration with a review attached is worth more than one
   without.

Author order and venue stay open until the patch cycle is done, as we agreed.
