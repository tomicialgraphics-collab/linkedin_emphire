# Response to the technical audit, version 1.2

Olusanya Timothy. 1 November 2026.

Supersedes version 1.1. What changed since then: the four P1 items are fixed,
each with a counterexample that fails without it, and the count of things this
patch does not fix has gone from four to one. Everything said about T08 and
about the other findings stands unchanged.

Reviewed: `Teamthy/host-failure-benchmark` at `25cd57f`. Patches: P0 against that
commit and P1 on top of it, both applied to a clean clone and checkable with
three commands.

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

On Windows 11 with Python 3.14.5, from a clean clone: 16 of 16 checks hold and
9 of 9 built-in mutations are caught. On Linux: the same, plus 8 of 8
counterexamples caught and two consecutive runs identical file by file.

The regression script needed two fixes to run on Windows, both in the second
commit and neither of them in a check: it located the run directory by parsing
a path with the platform separator in it, and it took an artifact directory as
proof that the suite had finished, so a run that stopped early failed later on
a missing file rather than on its own cause. It now requires every artifact the
suite writes and reports the run's output when one is missing. That is the kind
of defect the review would have found in my code, so it belongs in the same
message as the rest.

Two things will look like regressions and are not. The check count went from 14
to 16. And `example/run` is regenerated, because verdict records now carry a
state and the manifest is version 2; the old example fails the new checks,
which is the correct outcome and would be a problem if it passed.

## 4. What P1 changed

The four items version 1.1 listed as still open are fixed, in one commit on top
of the P0 branch. Each one has a counterexample that fails without the fix, and
the suite now fails if any of them is reintroduced.

| finding | what changed | check |
| --- | --- | --- |
| F11 | the store journals a record before it indexes it; a journal that refuses a write returns `ok: false, durable: false` and leaves memory untouched | `journal-first` |
| F7 | a repair copies the bytes it removes to a quarantine file and records that file's length and digest in the repair record | `repair-quarantine` |
| F9 (state half) | two verdicts that disagree become a named conflict carrying both sequence numbers; neither resolves the gap | `conflict` |
| F10 | a reply counts only if it succeeded and names the action that was asked about; anything else is rejected and the effect withheld | `reply-checked` |

F7 and F9 are counterexamples that damage the evidence. F10 and F11 are
counterexamples that restore the old code, because those two findings are about
the order a process acts in and no artifact can carry that bug. The suite says
which kind each mode is.

Three probes make those properties checkable without corrupting the main record:
a journal that refuses a verdict write, a journal torn mid-record, and a stub
store that answers every request correctly and confirms the wrong action in its
verdict reply. The stub is the only third process in the suite and it is six
lines of behaviour with no state.

The numbers are now 20 of 20 checks (12 P, 2 V, 6 meta), 10 of 10 mutations, and
12 of 12 counterexamples, with two consecutive runs identical file by file. Six
checks and one mutation were added; the counts are stated per class because the
class P count moving is the result, not the total moving.

One item stays open, and it is a design question rather than a defect.
Identifiers are still chosen by the caller and registered by the store. Minting
them is small in the protocol and large in the scenarios: A' exists to show
silence when nothing was registered, and if the store mints every id, any action
the host can name is one the store already knows. That row would have to be
recast. I would rather ask you than ship a change to the scenario table inside a
bug-fix patch, so it is the single remaining P1 item and it is written as a
question in section 6.

Two further defects were found by the first Windows run of this patch, both in
`verify.py` rather than in the store: pointing it at a directory that is not a
run raised `FileNotFoundError` while writing its report, and comparing two
directories that were both absent reported `determinism holds`. The second is
the same class of defect the review is about, committed by the tool that exists
to catch it, and it is the reason it is now a test: `challenge.py` requires a
path that is not a run to be refused, and requires a comparison to fail when an
artifact is missing from either side. Both are fixed in the third commit.

Unchanged and still open: an idle connection can hold the store (F15); the
verifier still imports the encoder it checks, so the correlated-oracle problem
stays until there is a second encoder; and there is no CI matrix, so the
cross-platform evidence is still two runs compared by hand and not a pipeline.

## 5. Claims and publication

The sentence I would stand behind, and the one I would not:

Defensible now: this local, deterministic benchmark shows how prior commitment
and later reconciliation distinguish classes of missing decision evidence under
scripted process failure, and its verifier rejects a set of counterexamples
that it used to accept.

Not defensible, now or after P2, and not claimed anywhere in the patch:
authenticated recovery, host-loss survivability, institutionally authorised
effects. Fixing the four P1 items makes the verifier harder to fool about what
it has. It does not create a witness outside the machine, and the note keeps
saying so in the sentence where the result is reported. I accept your decision
rule in section 7.1 without qualification.

## 6. Two requests, and one question

1. Put the 38-case package into the repository as `audit/cases/`, with its own
   runner, next to `audit/regressions.py`. The two sets belong together and
   every fixed finding should keep a test that can fail again.
2. Let me cite the review in the note, as `REVIEW-2026-11-01.md`, once P1
   lands. A demonstration with a review attached is worth more than one
   without.

3. On F6, a question rather than a request. If the store mints every identifier,
   the silence case C'' and the no-expectation case A' stop being possible for any
   action the host can name, because naming it is registering it. Which do you
   want: strict minting with those two rows recast, or registration kept and the
   claim kept as narrow as it is now? I have not changed it unilaterally, because
   it edits the table rather than fixing a bug.

Author order and venue stay open until the patch cycle is done, as we agreed.
