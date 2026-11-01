# Findings register

Olusanya Timothy, 1 November 2026. Last updated against `Teamthy/host-failure-benchmark`
`main` at `df0cf5a`.

One row per finding. A finding is closed only when a reproduction test exists, a
commit is named, and the regression suite fails without that commit. Anything
short of that stays open, including findings I believe are already fixed.

Status words mean one thing each:

- **open**: reproduced or accepted, no fix
- **fixed**: fix committed, reproduction caught by a named check
- **disputed**: I believe the case tests something outside the stated threat model;
  the reasoning is in the row and the disagreeing evidence is welcome
- **awaiting package**: named in the review of 9:05 PM but not yet read here

## My own three, reproduced before the package arrived

These were found by reading the code against the five areas in the 9:05 PM message,
and each was reproduced on `df0cf5a` with the command shown. They are here first
because a register that starts with the reviewer's findings and not mine would be
the wrong document.

| id | finding | reproduction on `df0cf5a` | commit | status |
| --- | --- | --- | --- | --- |
| R1 | Recovery authenticates by trust: replay takes `state` from the journal instead of recomputing it, so an unsigned record that says `verified` closes a gap after a restart | edit the `state` field of the D-4005 record in `example/run/store.jsonl` to `verified`, reframe it, start the store on that journal, ask `reconcile`: D-4005 is gone from the gaps and `lookup` reports `verified`. The verifier catches it only because it recomputes independently (`reconcile` fails) | none yet | open |
| R2 | An effect is committed on a qualified acknowledgement: the host treats `ok: true` as consent without reading `state`, so the unsigned D' verdict still logs `effect_committed` | `grep effect_committed example/run/host-Dp.jsonl` returns one line, for a record the store replied `state: unverified` to | none yet | open |
| R3 | I/O failure has no answer: a journal that cannot be written raises `PermissionError` inside the handler, prints a traceback, and closes the connection with no reply, instead of answering `ok: false, durable: false` | `chmod 444` the journal of a running store, send `issue`: the client receives an empty reply and the store prints a traceback | none yet | open |

R1 and R2 are in the area of his first and third concerns. R3 is his fourth. None
of the three is covered by a check today: R1 is caught only by the independent
verifier, R2 and R3 are not caught at all.

## The reviewer's areas, before his report is read

| area, as he named it | what I expect it to be | status |
| --- | --- | --- |
| acceptance of improperly authenticated or inconsistently bound evidence during recovery | R1 above, and possibly a second case where the signature verifies but a bound field does not | open, partly reproduced |
| reconciliation of unsigned or conflicting verdicts | conflict handling exists for two differing verdicts; an unsigned record followed by a signed one may still resolve, which needs testing | awaiting package |
| simulated effects proceeding despite unsuccessful store acknowledgements | R2 above | open, reproduced |
| journal durability and recovery under I/O failures | R3 above, and what the repair does when the failure is a partial write rather than a missing one | open, partly reproduced |
| incorrect rejection of otherwise valid evidence following store restart | not reproduced yet; the likely candidate is the conflict rule treating a re-sent identical record with a different field order as a disagreement | awaiting package |

## Carried over, unchanged

| id | finding | status |
| --- | --- | --- |
| F6 | identifiers are chosen by the caller and registered, not minted. Minting changes the scenario table, so it is a question rather than a patch | open, asked 1 November |
| F15 | an idle connection can hold the store | open |
| V1 | the verifier still imports the encoder it checks, so the correlated-oracle problem stays until there is a second encoder | open |
| H1 | no CI matrix. The cross-platform claim is two machines compared by hand | open |
| C1 | `audit/cases/`, the 38-case package, requested 1 November | awaiting package |

## The rule for closing a row

A row moves to **fixed** only when the suite has a mode that fails without the
fix. Two of my three above are orderings and one is an artifact property, so the
reproduction kinds will differ, and the register will say which kind each is,
exactly as `audit/README.md` does for f7 to f11.
