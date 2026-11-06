# P2 remediation scope, v0.1

A proposal for review, 6 November 2026. Nothing in this document is implemented. It sets out what I
propose to change for each of S1 to S5, how each row will be shown to close, and what will be kept
so that the closure can be checked without taking my word for it.

**Prepared for:** Behar Dalipi, whose review conditions of 5 November are incorporated below.

**The register this responds to:** `FINDINGS-REGISTER.md`, 13,294 bytes, SHA-256
`4413420b45d9312630b1b0e394cb8a09481a5be665135ded1ec4c693156c5c03`, at commit
`fbef78e752f3c6edf3a3e8dffcc1f94ae0dc0e3a`, tag `p2-register-2026-11-04`. That file is not touched by
this proposal. The rows move only in a later revision with its own hash.

**Code baseline:** `006d7ee` on `main` of the benchmark, applied from the patch whose SHA-256 is
`96d3e59aa016a534dcb694506ed954b624c1667ea783797b78d80a1169895e09`.

---

## 1. The closure rule, restated with the evidence it now requires

Unchanged: a row is closed only when a mode in `audit/regressions.py` fails without the fix.

Added, from your P2 closure discipline. Every closed row carries an evidence pack at
`evidence/p2/<row>/` containing:

| file | what it holds |
| --- | --- |
| `baseline.log` | the mode run against the baseline revision, failing, with exit code |
| `postfix.log` | the same mode run against the fix, passing, with exit code |
| `classification.log` | the full mode table before and after, so the change can be seen not to touch other rows |
| `revision.txt` | commit SHA of the fix, the patch SHA-256, and the baseline SHA |
| `env.txt` | Python version, OS, filesystem type of `TMPDIR`, and whether the run had the optional utilities |

Two rules follow from that, and I would rather state them than assume them. **A milestone finishing
is not a row closing.** M1 below finishing means S1 and S2 have modes written; the rows close only
when those modes fail on the baseline and pass on the fix, and the evidence pack says so. **S4 does
not close on anyone's schedule.** It closes when its condition is established on a filesystem that
permits it, and not before.

## 2. S1. Persistence and acknowledgement semantics

**What the code does now.** `Store.cmd_verdict` in `bench/store.py` writes the verdict record, then,
where the verdict conflicts with an earlier one, writes a second record for the conflict. If the
second write raises, `Store.handle` returns `{"ok": false, "durable": false}`. By then the first
record is on disk. The reply denies durability and is silent about which bytes are there.

**What changes.**

1. **Atomicity first.** The verdict and its conflict record are written as one append where the
   conflict applies, so the window between them disappears. One append, one `fsync`, one outcome. If
   the framing cannot carry both without changing the record schema, the two stay separate and step 2
   carries the whole burden, and I will say which of the two happened.
2. **Three states, named in the reply, never inferred.** The reply replaces bare `durable: false`
   with a state that reports what was established, not what was hoped:

| state | established how | what the reply may say |
| --- | --- | --- |
| `persisted` | every record in the request passed `fsync` before the reply was sent | `durable: true`, with `store_seq` for each record |
| `nothing_written` | the append raised, the rollback truncate returned, the length re-read equals the pre-attempt length, and the truncate's `fsync` returned | `durable: false`, `persistence: "nothing_written"` |
| `partial` | some of the request's records are on disk and at least one is not | `durable: false`, `persistence: "partial"`, `records_written: [...]` |
| `indeterminate` | the append raised and the rollback could not be confirmed, or the process died before it could be | `durable: false`, `persistence: "indeterminate"` |

`partial` is the state S1 in the register describes, and it is not a synonym for failure. It says
which records are on disk, which is the only way a caller can act.

**How it is shown to close.** A new mode `s1`:

1. Fresh journal, one verified verdict written and `fsync`ed.
2. Injected failure on the conflict append, using the existing failpoint mechanism extended to
   `conflict`.
3. The reply must carry `durable: false`, `persistence: "partial"`, and a `records_written` entry
   naming the first verdict's `store_seq`.
4. The journal file is read immediately afterwards: exactly one verdict record for that action id,
   no conflict record.
5. The store is restarted on that journal. The boot record's `replayed_records` must equal the number
   of records the reply named, `reconcile` must still name the gap, and no conflict may appear that
   the reply did not claim.

Step 3 fails on the baseline, which is the closure evidence. Steps 4 and 5 are the restart half you
asked for: immediacy and recovery are checked separately, because they can disagree.

**Question for you.** Is `partial` with a record list the shape you want, or would you rather any
request that is not wholly durable report `indeterminate` regardless of what is known? I propose the
former because it is more informative, and it is your call.

## 3. S2. Repair provenance

**What the code does now.** `Journal._cut_damaged_tail` in `bench/store.py` copies an unterminated
tail into `<journal>.quarantine-N.bin`, and records `file`, `bytes`, `sha256` and `ranges` in memory.
It writes no journal record. The start-up path in `main()` does write a `repair` record, which is why
the same cut is announced after a restart and silent during a run.

**What changes.** The runtime cut writes a `repair` record before the append that triggered it
proceeds, carrying the fields the start-up path already writes (`discarded_bytes`, `replayed_records`,
`quarantine`, `quarantine_bytes`, `quarantine_sha256`) plus the byte range from `ranges`, and a
`source` field distinguishing `runtime_cut` from `startup_repair`. The record is `fsync`ed. If that
append fails, the request that triggered the cut returns `persistence: "indeterminate"` with
`repair_record: "not_written"`, and `state` reports the same until a later repair record exists.
Silence is not permitted in either direction: not claiming a repair that did not happen, and not
completing a cut without saying so.

**How it is shown to close.** A new mode `s2`:

1. Start the store, append a valid record, then leave an unterminated line in the journal while the
   store is running.
2. Append a further valid record, which forces the cut.
3. The journal must contain a `repair` record naming the quarantine file, its byte count, its
   sha256, the cut range `{start, end}`, and `source: "runtime_cut"`, ordered before the record that
   forced the cut.
4. Restart on that journal: the repair record is replayed, and `state` reports the quarantine without
   a second repair record being invented.
5. Force the repair append itself to fail: the request must report `repair_record: "not_written"`,
   and no reply may claim the cut was recorded.

Steps 3 and 5 fail on the baseline, so the mode fails without the fix.

## 4. S3. Regression-runner reliability

The row names four behaviours, so there are four modes, each with its own assertion. All four are
ports of the scenarios in `p2-verification-2026-11-03/` into the shipped runner, so you can re-run
them from the repository rather than from my transcript.

| mode | what is injected | what must be reported |
| --- | --- | --- |
| `s3-state` | `verify.py` raises on import in the copied tree | every affected mode reports NOT-RUN, not MISSED; the runner exits with a distinct code that means "could not classify" |
| `s3-timeout` | a child that never returns | the runner bounds it, reports TIMEOUT for that mode with the bound printed, and other modes are unaffected |
| `s3-progress` | a run long enough to observe | at least one line arrives before the run completes, and `--json` output is byte-identical to the buffered run |
| `s3-preflight` | `bc` removed from `PATH` through a shim | one preflight line names the missing tool and the affected column, printed once, and every classification and exit code is identical to the run with the tool present |

**The constraint you set is the acceptance test.** These changes may not alter substantive pass or
fail classifications. The mode `s3-classification` therefore compares the full table of
`mode -> caught or MISSED` and every mode's `failed` check set, before and after, and fails on any
difference other than the four behaviours above. That is a stronger assertion than "the suite still
passes", because it pins what each existing mode found.

**Question for you.** Is a distinct non-zero exit code for "runner could not classify" acceptable, or
would you rather NOT-RUN stay inside exit 1 with the classification only in the output? I propose a
distinct code so that a wrapper cannot mistake an unclassifiable run for a caught counterexample.

## 5. S4. Stale-report assurance

No code change is proposed, because none is justified until the condition is established. What is
proposed is that the precondition is written down and tested rather than asserted.

Two candidate environments. (i) A filesystem that permits `chattr +i`, on a host or VM rather than
in this container. (ii) A read-only bind mount over the report file.

The test of equivalence is not the flag, it is the failure condition: the verifier is asked to write
or replace the report and cannot, and is then asked to present the report as current. If both
environments reproduce that identically, they are equivalent for this row and the evidence says so.
If only the mount is available and the refusal happens at a different point, the mount result is
evidence for a narrower condition, recorded as such, and S4 stays open.

**Question for you.** Can you supply a host or runner where `chattr +i` succeeds, or would you rather
I record the read-only mount as the narrower condition and leave the row open on that basis?

## 6. S5. Fixture cleanup

**What the code does now.** `run_mode` cleans its own temporary directory in a `finally`. The custom
modes do not: `fresh_copy` in `audit/regressions.py` calls `tempfile.mkdtemp`, returns the tree path,
and drops the work directory. `custom_f20` calls it twice, which is the two copies in the row.

**What changes.** `fresh_copy` returns the work directory as well as the tree and registers it for
removal; the custom modes remove theirs on the way out; a `--keep-fixtures` option keeps them and
prints every retained path, one per line, with the reason. Retention is opt-in, never implicit, and
always named.

**How it is shown to close.** A new mode `s5`:

1. `TMPDIR` set to a fresh directory.
2. `f20`, `f21`, `f22` and the full suite are run.
3. The directory contains no `hfb-*` entry afterwards.
4. With `--keep-fixtures`, the trees remain and each is printed.
5. The mode fails when a leak is deliberately reintroduced in a scratch copy of the runner, which
   proves the assertion is capable of failing.

## 7. Order and milestones

| milestone | rows | why this order |
| --- | --- | --- |
| M1 | S1, S2 | both are integrity claims, both are cheap to state precisely, and both are inside the store rather than the tooling |
| M2 | S3 | runner reliability, not benchmark correctness, and it depends on the classification vocabulary M1 introduces |
| M3 | S5 | housekeeping, no dependency on the other two |
| held | S4 | environment first; no code until the condition is established |

Each milestone ends with the evidence packs and a `classification.log` showing the full mode table
unchanged except where the milestone intended it. The register rows move at the end of a milestone,
in a new revision of `FINDINGS-REGISTER.md` with its own SHA-256, never as an edit to the pinned copy.

## 8. What this scope does not touch

- No change to benchmark scoring, scenario content, or the expected outcome of any existing mode.
- No change to the closure rule, and no row closed on the strength of a patch alone.
- No change to the assurance boundaries recorded in `TECHNICAL-NOTE.md`.
- No claim that S4 can be closed from this environment.

## 9. Open questions, collected

1. S1: is `partial` with a record list the right shape, or should any partially durable request report
   `indeterminate`?
2. S3: distinct exit code for "could not classify", or fold it into exit 1?
3. S4: a host with `chattr +i`, or record the read-only mount as a narrower condition?
4. S5: `--keep-fixtures` as a flag on the runner, or an environment variable so a CI job can set it
   once?

Four answers and I will implement in the order above.
