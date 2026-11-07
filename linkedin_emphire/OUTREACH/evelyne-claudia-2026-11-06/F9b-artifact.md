# F9b. A refused conflict write is reported as a refused verdict write

One bounded case, one file. Each claim is measured by `F9b-conflict-write.py` in this folder, or
labelled as read from the code. No verdict words of yours are used.

**The case. One store command writes two records. The second is the annotation. If it is refused, the
reply tells the host that the first, durable write did not happen.**

## The mechanism

`cmd_verdict` appends the verdict record, fsynced, then, when a different verdict already exists for
that action id, appends a conflict record naming both sequence numbers and the rule. Both appends sit
inside one `try` whose handler returns one reply for the whole command. So a refusal of the
annotative write is reported as a refusal of the durable write before it, and the reply loses the
action id it is about.

## Injection

The benchmark ships a failpoint that refuses records of kind `verdict` before any bytes are written. I
copied the benchmark, widened the selector in the copy to `verdict or conflict`, and ran four cells:
control and injected, each through the wire so the reply is captured verbatim, and each with the real
host process so the effect decision is the host's own. The copy is patched. The source is not.

| | control, write accepted | injected, annotation refused |
| --- | --- | --- |
| reply to the second verdict | `ok: true, stored: true, state: "conflicted", conflict: true, conflict_seq: 6` | `ok: false, durable: false` |
| journal | seq 4 verdict BLOCK, seq 5 verdict ALLOW, seq 6 conflict (`first_seq 4, second_seq 5`, rule text) | seq 4 verdict BLOCK, seq 5 verdict ALLOW, no conflict record |
| after a restart | `verdict_state: "conflicted"`, conflict entry present | `verdict_state: "conflicted"`, `conflict: null` |
| host events | `wal_commit`, `reply_rejected`, `effect_withheld` | the same three, the same reason |
| host's stated problem | `store did not resolve the verdict: state='conflicted' (conflict=True)` | `store refused: ...`, `reply names None, the request was 'F9-0004'`, `stored=None`, `state=None` |

Fifteen assertions, all met. Expected is the left column, observed is both.

## Three findings, each bounded

**1. The reply is false about durability.** Two verdict records, each fsynced before the refusal, sit
on disk when the reply says nothing is durable. Both frame digests recompute.

**2. The event class collapses.** A governance condition, two signed verdicts that disagree, reaches
the host as a storage failure. The remedies differ: one sends an operator to a disk, the other sends a
human to two decisions.

**3. The annotation is lost, the finding is not.** The rule text and the two sequence links are gone.
The state is not, because replay recomputes `conflicted` from the two differing verdicts alone.

## Your two corrections, applied

**Governing effect was not contradicted.** I wrote that earlier and withdraw it. The host emits the
same three events with the same reason in both worlds. What is contradicted is the store's account of
its own disk, not the host's conduct.

**Indistinguishability has a scope.** The two worlds are identical only to an observer holding the
reply and the host journal. An observer holding the journal sees two verdict records. One holding the
store's memory before the failure already reads `conflicted`.

That correction reaches further than the first. Because the state is recomputable, any reader with the
journal distinguishes the worlds, so my stronger claim, that two worlds become identical and stay
identical, does not hold. What survives is narrower: the reply states a falsehood about durability,
and the reply is what the host must act on.

## What the false statement invites

A client told its write did not land retries it. The same record sent again is refused in the same
words and appends a third verdict, duplicate of the second, still with no conflict record. Measured.
The control reply does not invite that, because it says `stored: true`.

Honesty note: retrying the control reply also appends, so this path is not idempotent in either world.
Non-idempotence is a separate property and this case does not establish it. What it establishes is
that the reply invites the retry while denying the write.

## Limits

- A failpoint, not a disk error. Same path, same exception, synthetic trigger. No real `ENOSPC`.
- The annotation is refused before any bytes are written. A partial conflict write, and the repair
  after a torn journal, are different cases and are not measured here.
- One store, one action id, loopback, fixed keys, deterministic clock. No concurrency, no production
  keys, no live traffic. Nothing here speaks to a deployed system.
- The host is measured, not judged. It says nothing about a host that reads `ok` alone.
- Read, not run: on a real write error the reply names no record kind. I did not force that path.
- To close: a reply naming which write failed and what is already durable, and a check that a refused
  annotation cannot change the class of the outcome.

## Files, hashes, reproduction

| file | size | SHA-256 |
| --- | --- | --- |
| `F9b-conflict-write.py` | 17,594 B | `991e9eec09c291bf0179b6677577c5929b688df0b2b2c10fea2cc163d669e891` |
| `RUN.txt`, the run above verbatim | 1,753 B | `682a3aaa4f3fec788cf0247b19e245b873037b8958a37259081623139a1cff09` |
| `run/result.json`, every reply, journal and host event | 31,435 B | `e5216e9c3a651f10e3830a036cd56e6719c3582f5385a1b5f67c168e823a3d7b` |
| `bench/store.py` as shipped | | `99f25cab23b3dea0f6f739a96fae23bc25bbc3d0a0db96e801ac7d701ae1f982` |
| `bench/store.py` in the copied tree, patched | | `a57d8bf7df51538c46d502b3c25697f1b1eae5bb2c1ed8453875a25726dd1add` |

```
python3 F9b-conflict-write.py --bench <path to host-failure-benchmark> --out ./run
```

Exits 0 when the fifteen assertions hold, 2 when the world differs from this page, and prints which
one failed. The patch, applied to the copy only:

```
-        if self.failpoint == "verdict" and record.get("kind") == "verdict":
+        if (self.failpoint in ("verdict", "conflict")
+                and self.failpoint == record.get("kind")):
```
