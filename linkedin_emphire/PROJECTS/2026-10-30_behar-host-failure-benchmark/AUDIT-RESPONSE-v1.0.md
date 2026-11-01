# Response to the technical audit of 1 November 2026

Olusanya Timothy. Version 1.0, 1 November 2026.

Reviewed: `Teamthy/host-failure-benchmark` at commit `25cd57f`, which is the
tip as I write this. The audit was run against a source archive without
`.git`, so it could not see the commit history; the repository has one, five
commits from `5bb8a7c` (2026-11-01) to `25cd57f`. Citations should use the
hash, as the audit says.

I reran the counterexamples rather than accepting them, on Linux, Python
3.11.2, standard library only. The script is in this folder as
`repro_audit.py`, one mode per finding, and it never touches the checkout it
points at: it copies the tree, applies one change, runs the suite and reports
what `verify.py` said.

```
python3 repro_audit.py --repo /path/to/host-failure-benchmark --list
python3 repro_audit.py --repo /path/to/host-failure-benchmark f1
```

## 1. The short version

The audit is right about the things that matter. The P0 findings reproduce,
including the two I would have least wanted to be true: a verdict that was
never signed can replace one that was, and deleting the journals that prove
five scenarios ran leaves a full pass.

I accept the remediation gates. I do not accept that the work is without
value: the parts that survive are the parts the note actually claims, and the
audit says the same thing in its conclusion.

Two of my own published statements are wrong and are withdrawn in the next
commit, not defended:

- "identifiers issued by an independent authority rather than minted where the
  action happens" (`TECHNICAL-NOTE.md`, standard practice section). The store
  accepts an `action_id` chosen by the caller and returns no receipt. It is a
  registration service, not an authority. F6.
- "nine scenarios" in the limitations paragraph of the same note. The suite
  runs eight. The sentences around it say eight. F16, and it is my error, not
  a wording preference.

Three more are accurate but overstated by the artifacts rather than the prose,
and are handled in section 4: the cross-platform claim, the "complete" example
run, and the phrase "killed" for a process that exits itself.

## 2. What I reran, and what came back

Each row is my own run of the audit's change, not a copy of the audit's log.

| mode | change made | `verify.py` verdict |
| --- | --- | --- |
| f1 | WAL verdict flipped BLOCK to ALLOW, signature left stale, then replayed | **every check holds**; the store now serves `ALLOW` for B-2001 and its signature does not verify |
| f2 | WAL `decision_ts` 2 to 7, nothing else touched | 1 check fails: `B.wal` (B holds) |
| f3 | unsigned verdict for C-3003 appended, frame recomputed so replay accepts it | the store's own reconciliation drops C-3003 from its named gaps; `verify.py` fails `reconcile` and `C` |
| f5 | the seven host journals for A, A', C, C', C'', D, D' deleted | **every check holds** |
| f8 | D-4004 actor and policy replaced, record re-signed with the fixture key | **every check holds** |
| f13 | host-B.jsonl cut mid-line, as a crash during an append would leave it | traceback, no `verify-report.json` |
| f14 | D-4004 `decision_ts` set to a Unix epoch value, re-signed, reframed | **every check holds** |

f3 is slightly worse than the audit states. The audit says an unverified
verdict "resolves named gaps". It does, and so does the verifier's own
recomputation: `recompute_gaps` in `verify.py` treats any record with
`kind == "verdict"` as a verdict, with no signature test. So the store and the
verifier agree that the gap is closed, and the disagreement that `reconcile`
would have caught never arises in the honest case. In my run they only
disagreed because I injected the record after `reconciled.json` had been
written.

## 3. One correction to the report

**F2, the T08 line.** The report says that changing the WAL timestamp to 7
leaves `B.wal` holding while B fails. In my run the opposite happens:
`B.wal` fails, because it compares the WAL timestamp against the stored one
and they no longer match, and B still holds. Mode `f2` above is that run.

The substance of F2 is unaffected. The WAL sits on the same filesystem,
written by the same process, with no external witness, so agreement between
the two files is consistency and not attestation. But the regression test
should be written against the behaviour that exists, otherwise it will pass
for the wrong reason and then be defended for the wrong reason.

## 4. Where the finding and the claim differ

These are not disagreements about whether to fix something. They are about
what the fix has to say, and three of them change what the note may claim
before any code moves.

**F1, F8 and F14 are one defect wearing three coats.** The note already
concedes the underlying weakness: tamper evidence against an adversary holding
the source is listed as not implemented, and the paragraph says the key is a
literal in `common.py` so anything that can rewrite a file can re-sign it.
What the audit adds, and what I had not stated, is that `verify.py` cannot
tell the difference in its output. It prints `VERDICT: every check holds` over
a record whose signer is `nobody` and whose signature is `null`. The
limitation is disclosed; the verdict line contradicts the disclosure. That is
the defect. The cheap half of the fix is not a new witness, it is a verifier
that says "consistent with the fixture key, not authenticated", and a state
per record that can be `verified`, `unverified` or `conflict`.

**F4 and the word "killed".** Row M3 exits with `os._exit(9)`. The host
journal in that scenario records the note `killed before any verdict left the
process`, and the README says one process is "killed on purpose". Both are
wrong for a self-exit, and both are mine to fix. What I will not do is pretend
the failure domain is wider than it is: on one machine, with one filesystem,
loss of the host disk cannot be demonstrated. I propose to declare the
boundary in the note and name the two experiments that would cross it, an
external kill at a barrier and destruction of the host-local filesystem, as
declared out of scope with a stated design, rather than simulate host loss and
call it host loss. If you would rather have them built, they need a second
failure domain, which means a second machine or a container with its own
volume.

**F16, provenance.** The audit could not verify the commit history because the
archive had no `.git`, and its S classification is fair on those materials.
The repository does have history, and `CONTRIBUTION.md` records the first
commit and the basis for each file. For anything published, the citation is a
hash, and I will tag the reviewed commit so the audit's snapshot and the
repository can be tied together.

**F16, "nine vs eight".** You have this one right and it is a real
inconsistency in the note: the scenarios table lists eight, and a later
paragraph says nine. The README's "damages it nine ways" is a different nine
(`challenge.py` has nine mutations) and is correct.

**The 37 of 38.** I am not going to argue with the number and I am not going
to repeat it as a quality figure for the implementation. It is a fraction of
tests selected to produce counterexamples, which the report itself says in
section 2. What I would ask for is the opposite of a defence: put the package
in the repository as a permanent test suite, so every repaired finding keeps a
negative test that can fail again later.

## 5. What I accept, and what will change

Mapped to the gates in section 7 of the audit. Each row is a code change, a
test that must fail before it and pass after it, and a sentence in the note
that the change makes safe to keep.

### P0, integrity

| change | where | test that must fail before, pass after |
| --- | --- | --- |
| Verify the signature on WAL records at ingest and on recovered verdicts in the verifier | `bench/store.py` `cmd_verdict`, `verify.py` class P checks | f1: altered WAL must be rejected or marked unverified, never recovered as `ALLOW` |
| Explicit `verified` / `unverified` / `conflict` state per record, and only `verified` resolves a gap | `bench/store.py`, `verify.py` `recompute_gaps` | f3: an unsigned verdict leaves C-3003 named as a gap |
| Artifact manifest with a version, required files, and a per-scenario event chain check | `run.py`, `verify.py` | f5: deleting a host journal must fail, not pass |
| Verifier never raises: one defensive parse path, `indeterminate` in the report, a report written even when the run is unreadable | `verify.py` | f13: torn host journal gives a report with a documentation status, no traceback |
| Compare `policy_sha` and `decided_by` against the trusted constants already in `common.py` | `verify.py` class V | f8: a rewritten actor or policy must fail |
| Timestamp bounds: `decision_ts` must match a counter step present in the matching host journal | `verify.py` `no-wall-clock` | f14: an epoch value must fail |

The last two are worth calling out as the cheapest fixes in the report and the
most embarrassing to have missed: the expected policy hash and the expected
actor are constants in `bench/common.py`, and `verify.py` never compares
against them.

### P0, scope

Rename the M3 failure to "the host process exits before the verdict leaves
it" everywhere, including the host journal note and the README sentence.
State that host-local disk loss is not modelled. State the three time
distinctions the audit asks for as three separate fields: host counter step,
store arrival order, and whether either is independently attested (it is not).

### P1, recovery

Journal before memory: `apply()` persists before the in-memory index moves,
and an append failure returns a structured error. Repair keeps the original
journal (`store.jsonl.pre-repair-<n>`) and records what it discarded.
Mid-file corruption is an explicit indeterminate result, not a truncation.
Sequence gaps in `store_seq` are checked. Duplicate verdicts become a conflict
state, and the store and verifier agree on which record is authoritative.

### P1, authority

Store-minted identifiers, returned with a receipt, or a renamed claim that
says registration. Commitments write-once, with overwrite rejected. A verdict
against an unissued id is either refused or stored as `unissued`. Actor, policy
and descriptor commitment checked against independently held expectations
where the test can hold them.

### P1, harness

`host.transport.call` validates the reply before any effect is logged, and a
negative, malformed or absent reply produces `effect_withheld`. Then an
admission test: the effect boundary is a function that cannot run without a
positive durable receipt.

### P2, hardening

Bounded reads and concurrency in the store, an independent implementation of
canonicalisation and framing for the verifier (the correlated-oracle point in
5.4 is right, and the cheapest version is that `verify.py` stops importing the
machinery it is checking), known-answer vectors, and a CI matrix on Linux and
Windows publishing file digests so the byte-identity claim stops being an
assertion. The f15 idle-socket behaviour gets fixed by the bounded reads; I am
not going to argue the severity either way, since it is a harness.

## 6. What I propose to keep

The four rows, the split of M3 into C, C' and C'', the claim and counterclaim
form for every check, the separation of Class P and Class V, the counter clock
and the determinism it buys, and a verifier that reads no pass flag. None of
these is implicated by the findings. F12 says the built-in mutations are
shallow, which is true and fixable; it does not say the mutation idea is
wrong.

Two sentences in the note need to go regardless of code: the one that calls
the store an independent issuer of identifiers, and the one asserting
byte-identical artifacts across two operating systems without a published
digest to back it.

## 7. Claims matrix

Every guarantee sentence in `README.md` and `TECHNICAL-NOTE.md` gets a row:
the claim, the check id that supports it, the counterexample test that would
refute it, and one of the report's own statuses (R, P, S, H). A claim without
a test is marked as a design goal, not a result. This is the thing that would
have caught F16 without an auditor, and it is the artifact I would want a
reviewer to read first.

## 8. Publication

I accept the decision rule in section 7.1 without qualification. Nothing in
the current draft should be published as authenticated recovery, host-loss
survival, or institutionally governed effects. After P0 and P1 land and the
regression suite runs green, I will send the corrected note and the claims
matrix, and we can decide together whether it is publishable as a
demonstration of the named-gap result or whether it needs another cycle.

The defensible sentence in the meantime is the one in Appendix B of the audit,
with one change: I would say the benchmark "demonstrates how prior commitment
and later reconciliation distinguish classes of missing decision evidence",
and leave authenticated recovery out of the sentence entirely, because it is
not what the suite shows.

## 9. Process, and two requests

Attribution stays as `CONTRIBUTION.md` records it, and author order and venue
stay open until the patch cycle is done, as we agreed.

Two requests:

1. Ship the 38-case package into the repository as `audit/`, with its own
   runner, so every finding fixed here keeps a test that can fail again. I
   would rather the counterexamples live in the code than in a report about
   the code.
2. Keep the audit as a citable document. If you are willing, it goes in as
   `REVIEW-2026-11-01.md` and the note cites it in the limitations section.
   A demonstration with a review attached is worth more than one without, and
   it costs us nothing to say so.

## 10. What I could not check

The package-reported results (P status) I did not rerun, including T12, T13,
T15, T21, T36 and T38. F15 I have not reproduced; I am accepting it on the
code. The Windows half of the byte-identity claim I have run once and cannot
show you a digest trail for, which is the honest state of it and the reason
for the CI matrix above.

## Appendix: reproductions

```
python3 repro_audit.py --repo <checkout> f1     # WAL flip, stale signature
python3 repro_audit.py --repo <checkout> f2     # WAL timestamp only
python3 repro_audit.py --repo <checkout> f3     # unsigned verdict, gap cleared
python3 repro_audit.py --repo <checkout> f5     # seven host journals deleted
python3 repro_audit.py --repo <checkout> f8     # actor and policy rewritten
python3 repro_audit.py --repo <checkout> f13    # torn host journal
python3 repro_audit.py --repo <checkout> f14    # epoch timestamp, re-signed
```

Each mode prints what it changed, `verify.py`'s exit code and verdict line,
the checks that failed, and the specific evidence for the finding. `--keep`
leaves the working copy for inspection. The script is review equipment: it is
not part of the benchmark and it is not proposed for it, except as the seed of
the `audit/` suite in section 9.
