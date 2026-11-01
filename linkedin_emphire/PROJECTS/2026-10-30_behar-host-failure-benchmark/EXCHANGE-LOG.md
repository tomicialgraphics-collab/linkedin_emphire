# The Behar exchange: what was said, what was done, what was checked

Olusanya Timothy, 1 November 2026.

This is the record of the review exchange around the host-failure benchmark, from
the day the audit arrived to the day a pull request was opened on the workspace
repository. It exists because the exchange is now three documents, four patches,
thirteen commits and two repositories, and the reasoning behind each change is
easier to lose than the change itself.

Rule followed throughout: nothing here is a number I did not run, and nothing
here is a claim that a fix does more than it does. Where a thing was expected and
not observed, it says so.

Participants: Behar Dalipi, who reviewed; Olusanya Timothy, who built and
responded. All delivery went through messages the owner sent himself. No email
was sent by the agent, and no credential ever travelled in chat.

---

## 1. What arrived

A twelve-page technical audit of `Teamthy/host-failure-benchmark` at `25cd57f`,
with sixteen findings (HIGH F1 to F5, MEDIUM F6 to F12, LOW F13 to F16), a
claims matrix correction, and three gates: P0 integrity, P1 recovery and
authority, P2 publication.

The audit separates four kinds of finding, and that separation was kept intact in
every reply:

- **R**, reproduced by the reviewer locally: 22 cases, 21 discrepancies, plus one
  control (T03).
- **P**, reported by the package: 38 cases, 37 discrepancies.
- **S**, specification or claims wording.
- **H**, hygiene and harness.

Standing rule from the owner: never restate 37/38 as a failure rate. The audit's
own section 2 says it is not a reliability percentage, and both directions of
restatement are wrong.

## 2. What reproduced

`repro_audit.py` was written with one mode per finding and run against a clean
checkout of `25cd57f`. Six of the seven P0 counterexamples were accepted by the
verifier, including the two that mattered most: a WAL verdict flipped from BLOCK
to ALLOW with a stale signature still verifying clean, and seven deleted host
journals still totalling a pass. One was worse than reported: T14 did not just
clear a named gap, it also cleared it in the verifier's own recomputation.

Two claims of my own were withdrawn rather than defended: the note called the
store an independent issuer of identifiers when it accepts an id from the caller,
and it said nine scenarios where the suite runs eight.

One correction went the other way. T08 as described in the report did not behave
that way: changing only the WAL timestamp made `B.wal` fail and `B` hold, the
reverse of the report's line. The substance of F2 stood; the regression test had
to be written against what actually happens.

## 3. The exchange, in order

| when | who | what |
| --- | --- | --- |
| before 1 Nov | reviewer | audit of `25cd57f`, sixteen findings, three gates |
| 1 Nov, morning | builder | reproduced the findings, wrote response v1.0, sent the reply that conceded the P0s and re-stated the T08 reading |
| 1 Nov, morning | builder | P0 patch: signature checks, unverified records cannot resolve gaps, constants compared, timestamp bound to the host counter step, manifest v2, verifier never raises |
| 1 Nov, 5:30 PM | reviewer | T08 was two different intervention points, not one; both are consistent with the implementation and test different properties; asks for both in the suite and the report; restates the F2 concern |
| 1 Nov, evening | builder | split `f2` into `f2a` and `f2b`, each asserting what must fail and what must not; fixed the second Windows portability bug; response v1.1 with the two-row table on the first page |
| 1 Nov, evening | owner | pushed `p0-authenticated-recovery`, merged it to `main` (`fc912cd`) |
| 1 Nov, night | builder | P1: the four remaining items, three probes, four new counterexamples; response v1.2 with F6 as a question rather than a silent change |
| 1 Nov, night | owner | applied P1 on `main` (`41013f0`), ran the suite on Windows, found two defects by mistyping a path |
| 1 Nov, night | builder | P1.1: the verifier answers a path that is not a run, and stops calling two absent directories identical; both become tests (`df0cf5a`) |
| 1 Nov, 6:45 PM | reviewer | will reproduce the updated tests independently before the phase is called validated; will share findings |

## 4. T08, the one that needed both of us

The disagreement was real and neither description was wrong. We were changing the
write-ahead log at two different moments.

| intervention point | what agrees | what fails | property being tested |
| --- | --- | --- | --- |
| before the store replays | recovered record and WAL | `B` | the timestamp is bound to the host journal |
| after replay completes | nothing | `B.wal` | two files agree with each other |

Both are in `audit/regressions.py` as `f2a` and `f2b`. `f2a` requires `B` to fail
and `B.wal` to hold. `f2b` requires `B.wal` to fail; after the P0 patch it also
fails `B`, because the record's signature no longer covers its bytes, which is an
independent reason rather than a change of position.

F2's substance is untouched: agreement between a log and a store on one
filesystem, written by one process, is consistency and not attestation. What the
patch adds is narrower and is stated that way in the sentence where the result is
reported: a decision timestamp must match a counter step the host journal
contains, which is a bound, not a witness.

## 5. P0, what it changed

- WAL records and recovered verdicts are signature-checked, at ingest and in the
  verifier. A record that does not verify stays visible and cannot resolve a gap,
  in `recompute_gaps` as well as in the store.
- Actor and policy hash are compared against the constants in `bench/common.py`,
  and the decision timestamp is bound to a counter step in the host journal.
- `run.py` writes a versioned manifest naming every required artifact, and
  per-scenario event chains, so a deleted journal fails completeness rather than
  reading as a scenario with nothing to say.
- The verifier stops raising on an unreadable artifact and reports an explicit
  unreadable state.

Checks went from 14 to 16. `example/run` was regenerated, because verdict
records now carry a state and the manifest is version 2. The old example failing
the new checks is the correct outcome; the reverse would be the problem.

## 6. P1, the four items and the one left open

| finding | what changed | check |
| --- | --- | --- |
| F11 | the store journals a record before indexing it; a refused write returns `ok: false, durable: false` and memory is untouched | `journal-first` |
| F7 | a repair copies the bytes it removes to a quarantine file and records that file's length and sha256 in the repair record | `repair-quarantine` |
| F9 (state half) | two verdicts that disagree become a named conflict carrying both sequence numbers; the action stays unresolved | `conflict` |
| F10 | a reply counts only if it succeeded and names the action that was asked about | `reply-checked` |

Three probes make those properties checkable without corrupting the main record:
`probe-durability` forces a journal that refuses a verdict write, `probe-repair`
tears a journal mid-record, and `probe-reply` points a host at
`bench/stub_store.py`, a fixture that answers every request correctly and
confirms the wrong action.

F6 was not changed, deliberately. If the store mints every identifier, C'' and A'
stop being possible for any action the host can name, because naming it is
registering it. Those two rows are the silence cases and the strongest thing in
the table. Recasting them is a change to the scenario table, not a bug fix, so it
is written up as a question to the reviewer instead of shipped inside a patch.

Checks 16 to 20 (12 class P, 2 class V, 6 meta). Mutations 9 to 10. Counterexamples
8 to 12. Two of the four new counterexamples restore the old code rather than
damaging an artifact, because F10 and F11 are orderings inside a process and no
artifact can carry that bug.

## 7. P1.1, two defects of my own

Found by the owner's first Windows run of P1, through a mistyped path:

1. `verify.py` pointed at a directory that does not exist printed a failed check
   and then raised `FileNotFoundError` while trying to write its report, after the
   P0 notes had promised the verifier never raises.
2. `verify.py run-a run-b`, given two directories that were both absent, reported
   `determinism holds`. Absent compared to absent is a match, so two runs that did
   not exist were called identical.

The second is the same defect class as a missing artifact passing a completeness
check, committed by the program that exists to catch exactly that. Both are fixed
and both are tests: `challenge.py` now requires a path that is not a run to be
refused with exit 2 and no traceback, and requires a comparison to fail when
either side is missing an artifact. Neither changed any result, because every
number came from a run that existed.

## 8. What has been checked, where

| commit | Linux 3.11.2 | Windows 11, 3.14.5 |
| --- | --- | --- |
| `25cd57f` (reviewed) | 14 checks, 6 of 7 counterexamples accepted | not run by me |
| `3b6b781` P0 | 16 checks, 9 mutations, 7 of 7 | 16 checks, 9 mutations |
| `9194c61` P0.1 | 16 checks, 9 mutations, 8 of 8 | 8 of 8 after the runner fixes |
| `41013f0` P1 | 20 checks, 10 mutations, 12 of 12, byte-identical repeats | 20 checks, 12 of 12 |
| `df0cf5a` P1.1 | 20 checks, 10 mutations + 2 input checks, 12 of 12 | 20 checks, 10 + 2, 12 of 12, missing path refused |

Every figure above was produced by a command that was run. Where a platform has
not been run, the row says so. The Linux byte-identical comparison has no Windows
counterpart yet: the Windows verdicts are single runs.

## 9. Delivery mechanics, because they cost more than they should

- The reviewer receives documents through the owner, as HTML attachments. He has
  the repository itself.
- Raw links are pinned to a commit, never to a branch, so a downloaded file and a
  described file cannot drift apart.
- LinkedIn accepts PDF, DOCX, TXT, HTML and images, not Markdown, not `.patch`,
  not `.zip`. Hence `.patch.txt` copies for the earlier exchanges.
- PowerShell treats a bare URL as a command, and treats a placeholder in angle
  brackets as a URI it cannot parse. Both were learned by breaking a run.
- The patch file from an earlier exchange was committed to the benchmark
  repository by accident. It is removed in P1.1 and `*.patch` is now ignored.

## 10. What is open

For the benchmark:

- F6, store-minted identifiers: a design question, not a defect. Asked, not
  assumed.
- F15, an idle connection can still hold the store.
- The verifier still imports the encoder it checks, so the correlated-oracle
  problem stays until there is a second encoder.
- No CI matrix. The cross-platform claim is two machines compared by hand.
- `audit/cases/`, the 38-case package, has been requested and not received.
- The review is to be cited as `REVIEW-2026-11-01.md` once P1 lands, which it now
  has.
- Author order and venue stay open until finalisation, as agreed from the first
  commit.

For the claims:

- Defensible: this local, deterministic benchmark shows how prior commitment and
  later reconciliation distinguish classes of missing decision evidence under
  scripted process failure, and its verifier rejects a set of counterexamples it
  used to accept.
- Not defensible and not claimed anywhere: authenticated recovery, host-loss
  survivability, institutionally authorised effects.

## 11. What the reviewer is doing next

His last message says he will reproduce the updated tests independently before
the phase is called validated, and will share anything that needs attention. The
thing to send him is a commit, two commands and the expected numbers, not another
argument. If he finds a third defect in the verifier's input handling, that is
worth more than another green run, and it should arrive as a failing command
rather than a description.

## 12. The differential review, and what running it changed

He sent the full review as text on 1 November, v1.2, and a Drive link to the package. The
package arrived as `HFB_Teste_Diferenciale.zip`, 41,754 bytes, sha256
`b2a39986c4ad238446e9d2a4928e58a35cba2ff7ceed8fda3e357ac14db90ed4`, which is the hash the
review declares. So the file is the file.

The package is 36 outcome tests and 13 input checks, not the "eleven counterexamples" his
earlier message described. His results file marks 23 outcomes as defects; run unchanged against
`df0cf5a` here, the same 23 came out, case for case. On the inputs I got N06, N12 and N13, with
N11 untestable for the same reason it was untestable for him.

The three defects I had found by reading the code were V05, V17 and V19 in his numbering. His
first, third and fourth areas, and the same three cases. That is the useful part of the exchange
so far: two people reading one repository separately found the same defects and neither found
them all.

P2 answers F-01 to F-05 and F-09, with the exceptions V22 and V35 and the dispute at V04. On the
patched tree his package reports 9 defects and 22 documented outcomes. The nine are the ones he
predicted would remain: V04, which I dispute, V23 and V24, which are host-side and out of the
current claim, and V28 to V33, which need signed sequence numbers that do not exist yet.

The modes came after the disposition, because his rule is that a row closes on a mode and not on
a run I did by hand. Seven modes, nineteen in all: f16 and f17 for the state trust and the
binding, f18 for the conflicting verdicts, f19 for the acknowledgement, f21 for the journal I/O,
f20 for the false rejection in both directions, f22 for the runner. Six register rows moved from
patched to closed on the strength of them.

Two things I will not do in the reply. I will not restate his count of 25 deviations as if it
were in his own results file, which shows 24 counting the static case; and I will not call
anything closed. Every patched row in the register stays patched until `audit/regressions.py`
has a mode that fails without the fix. His acceptance rule is the mode, not the run I did by
hand.

The release decision stands as he wrote it. Nothing in P2 supports authenticated recovery,
host-loss survivability, or trusted timestamps, and the note says so next to the results rather
than in a footnote.

## 14. His answer, 1 November, 10:53 PM

He replied to the full response and accepted both disputed points in his own words. V04 "needs a
genuine timestamp divergence to test the intended property", which is the argument made in the
disposition. N13 "should be updated to reflect the revised evidence-preservation mechanism", which
concedes that the check is testing a file that no longer exists rather than the property. He will
read the register and rerun the differential tests against 006d7ee before consolidating a position
on the remaining cases. No asks, no attachments requested, no timeline.

State after this message: eight cases open (V23, V24, V28, V29, V30, V31, V32, V33), V04 settled as
disputed with the test to be re-specified, N13 settled with the register entry to be rewritten. The
reply is in behar-reply.md section 12. The register wording is drafted there and held, not pushed,
until his rerun lands.
