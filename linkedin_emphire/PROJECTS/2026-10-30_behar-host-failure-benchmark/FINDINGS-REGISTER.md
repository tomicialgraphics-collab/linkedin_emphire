# Findings register

Olusanya Timothy, 1 November 2026. Last updated against `Teamthy/host-failure-benchmark` `main`
at `df0cf5a`, with patch P2 applied on top (see `P2-DIFFERENTIAL-FIXES.patch.txt`, sha256
`1737a13c06d0b55af9f45405572c5ec2b9647d9b5e35524d2ef18f5a5ada646c`).

One row per finding. A row is **closed** only when a mode in `audit/regressions.py` fails
without the fix. Until then the row stays in this file, whatever the patch does, and the status
says exactly how far it has got. That rule has not changed since the first version of this
register, and it is the reason no row below says closed.

Status words mean one thing each:

- **open**: reproduced or accepted, no fix in any tree I control
- **patched**: fix written and verified against the reviewer's own case, which now behaves as
  documented; the in-repo mode that would close the row is not written yet
- **disputed**: I believe the case does not test the property it names, or tests something
  outside the stated threat model; the reasoning is in the row and the evidence is in
  `evidence/2026-11-01/`
- **scope**: nothing to patch; the claim is narrowed and the narrowing is written in
  `TECHNICAL-NOTE.md`
- **closed**: patched, and a mode fails without it

## Where the numbers come from

The reviewer shipped 36 outcome tests and 13 input checks. Re-run unchanged against `df0cf5a`,
his own results file marks 23 outcomes as defects and 9 as documented. Against P2 it marks 9 as
defects and 22 as documented. The per-case table, with the disposition of every one of the 49
cases, is `DISPOSITION-2026-11-01.md`. Every count in this register comes from that table.

## My own three, found before the package arrived

All three were reproduced on `df0cf5a` by hand, and all three turned out to be cases in his
package: R1 is V05, R2 is V17, R3 is V19. Each now behaves as documented under P2.

| id | finding | his case | fix | status |
| --- | --- | --- | --- | --- |
| R1 | Recovery authenticated by trust: replay took `state` from the journal row instead of recomputing it, so an unsigned record that says `verified` closed a gap after a restart | V05, V06 | store recomputes state from the record bytes and the id the row is filed under, through one `bound_state()` in `bench/common.py` that the store and the verifier both import | patched |
| R2 | An effect committed on a qualified acknowledgement: the host read `ok: true` without reading `state`, so the unsigned D' verdict still logged `effect_committed` | V15, V16, V17, V18 | a verdict reply must say `stored: true` and `state: "verified"`; anything else, including a closed connection, withholds the effect and names the reason | patched |
| R3 | I/O failure had no answer: a journal that could not be written raised inside the handler, printed a traceback and closed the connection with no reply | V19, V20, V21 | a failed append cuts the file back to its previous length and the store answers `ok: false, durable: false`; a damaged tail is quarantined before the next append; repair keeps the records that follow damage | patched |

## His findings, as F-numbered in the review

| id | finding | cases | fix | status |
| --- | --- | --- | --- | --- |
| F-01 | journal state and action-ID binding | V05, V06 | as R1 | patched |
| F-02 | conflicting verdicts and verifier self-consistency | V12, V13 | check `D` refuses to report a record verified while the same journal lists its action as an unresolved gap | patched |
| F-03 | acknowledgement and effect admission | V15-V18 | as R2 | patched |
| F-04 | durable journal I/O, torn writes | V19-V22 | as R3 for V19-V21; V22 stays open: the failpoint still refuses before any byte is written, so only damage tests tearing | patched, V22 open |
| F-05 | false rejection after a routine restart | V26 | `B` binds the recovered verdict to the epoch it landed in, not to the last boot record in the file | patched |
| F-06 | host loss and proof of crash | V23, V24 | none. No independently recorded kill receipt, no named host-disk-loss test, and nothing in the suite authenticates that the host died | scope |
| F-07 | completeness of earlier evidence | V28-V33 | none. Nothing signs the sequence or checkpoints the journal, so a deletion or a rewrite inside framed records still verifies | open |
| F-08 | timestamp semantics and the shared fixture key | V02, V04 | `B.decision` compares the recovered verdict and rule with the guard decision the host logged; V04 is disputed: its mutation writes the value the field already holds, and the re-signed record is byte-identical to the WAL | patched, V04 disputed |
| F-09 | runner trustworthiness | V35, N06, N11-N13 | `verify.py run run` is refused; `challenge.py` writes nothing into the evidence directory, derives its absent path, and fingerprints the directory to prove it is unchanged | patched; V35 not testable here, N13 needs his check rewritten |
| F-10 | idle connection blocks the store; client-selected ids | V36, F6 | none | open |

## Disputed, with the evidence beside it

| case | why |
| --- | --- |
| V04 | Replay step and decision step are both 2 in this run, so `record["decision_ts"] = self.clock.step + 1` rewrites the field with the value it already held, and re-signing produces identical bytes. `evidence/2026-11-01/v04-inert-proof.log` prints `record_identical_to_wal=True` for his exact mutation and `B=fails, B.wal=fails, exit=1` for the same mutation with the clocks five steps apart. `B.wal` compared the stored timestamp with the WAL before P2 as well. |
| N13 | His check requires `challenge.py` to leave a passing report in the directory it was pointed at. I removed that behaviour, so the file it opens no longer exists and the check raises. The property is now asserted by the tool, every run, in its last line. |

## Carried over, unchanged

| id | finding | status |
| --- | --- | --- |
| F6 | identifiers are chosen by the caller and registered, not minted. Minting changes the scenario table, so it is a question rather than a patch | open, asked 1 November |
| F15 | an idle connection can hold the store | open |
| V1 | the verifier still imports the encoder it checks, so the correlated-oracle problem stays until there is a second encoder | open |
| H1 | no CI matrix. The cross-platform claim is two machines compared by hand | open |

## What closes the patched rows

One `audit/regressions.py` mode each, in the same three kinds the file already uses: an
after-run artifact mutation for F-02, a before-run code revert for F-01 and F-03, and a
store-level case for F-04, which needs a journal that refuses a write rather than a run that
contains one. The acceptance rule for each is his: the mode must reject the original
counterexample and the benign run must still verify. The second half is already measured: P2
leaves `run.py` plus `verify.py` at 13 of 13 Class P and 2 of 2 Class V, two runs byte-identical,
and `challenge.py` catching every mutation it names.
