# Host-Failure Benchmark, Updated Harness Specification

Version: v0.1 (2026-10-30)
Status: working document, consolidated from the matrix skeleton (R5)
and the refinements agreed 2026-10-30. Venue-agnostic.
Contributors: Olusanya Timothy, Behar Dalipi (both, from v0.1).
Companion to: the guarantee and failure-assumption analysis (Behar),
which writes against the rows in section 3 and the distinctions in
section 5.

---

## 1. Invariants

The harness is two local processes: the host and the audit store.

- No model, no externally sourced key, no network. Deterministic end
  to end.
- Class V uses a deterministic key pair generated in-process from a
  fixed seed, so nothing external enters the run and the result is
  fully reproducible. This supports reproducible functional
  verification. It is not evidence of production-grade key security
  or institutional trust, and the note states that in the same
  sentence as the Class V claim.
- Every assertion is written as claim plus counterclaim, so a failure
  is a named mismatch, not a color.
- The verify step re-derives each assertion from the stored raw
  outputs, so a stranger can re-run the check without trusting the
  run that produced it.
- The whole suite runs in under thirty minutes from a fresh machine
  with nothing installed beyond the shipped code.

## 2. Phases (the T0-T6 trace)

T0 proposal, T1 guard verdict, T2 local commit, T3 ship, T4 effect,
T5 recovery, T6 verification. Each test case kills or fails the run
at one phase and asserts what the other process sees afterwards.

## 3. Failure matrix (four rows, five columns)

Columns: when the failure becomes detectable; what must survive what;
the recovery mechanism; the residual gap; the test case.

### M1, the verdict is not emitted
- Detectable: never at decision time; at review time only if an
  expectation register exists outside the guard path.
- Survives: the expectation of the verdict must survive outside the
  guard path, so the absence can be named.
- Recovery: none. The decision is lost and only its absence is
  provable.
- Residual: the decision itself, lost forever.
- Test case: A, the register present, the missing verdict is named;
  A', the same run without the register, and the absence is not
  named.

### M2, the verdict is emitted but not preserved
- Detectable: at the persistence failure, and at replay, when the
  record surfaces with its original decision timestamp.
- Survives: the record must commit before the effect, into the local
  write-ahead copy, so a replay path exists.
- Recovery: the replay from that copy to the audit store, carrying
  the T1 timestamp.
- Residual: the window in which the record exists in exactly one
  place.
- Test case: B, the persistence layer down mid-ship, the effect
  withheld, the replay lands the verdict with its original timestamp.

### M3, the host dies before ingestion
- Detectable: at reconciliation only, and only if the ID commitment
  was established independently of the host.
- Survives: the name of the action must survive the host.
- Recovery: none for the decision content; the audit system records
  a named gap with provenance.
- Residual: the decision content, lost; the provable remainder is the
  action's existence and the failure of its verification.
- Test case: the C family (section 4).

### M4, the record is preserved but not independently verifiable
- Detectable: at verification time, when a third party checks the
  binding.
- Survives: the binding (signature, policy hash, ID chain) must be
  part of the record, not an annotation.
- Recovery: none for a record that arrives without it; it is
  quarantined as unverified, never treated as verified.
- Residual: a preserved record that cannot be distinguished from the
  host's claim.
- Test case: D, the record arrives, the binding is checked, the
  missing element is the quarantine.

## 4. Test classes and the C family

Two classes, reported separately in the benchmark:

- Class P, persistence and recovery: A, A', B, C, C', C''. Its claims
  are survival, recovery, and naming, with no cryptographic claim.
- Class V, verification: D and the binding check. Its claim is that
  the binding verifies against the keys it is given. The note states
  that this does not prove the keys are institutional.

The C family, one host death at T3 under three levels of out-of-band
witness:

- C, the complete pair: an issuer-issued ID plus the independently
  preserved commitment to the action descriptor. Result: a named gap
  with content. Action X was proposed; its verdict was never
  independently recorded.
- C', issuance only: the issuer-issued ID, no preserved commitment to
  the descriptor. Result: a named gap without content. An ID was
  issued and never resolved; the content is unknown.
- C'', locally assigned ID: the ID is minted on the host. Result:
  silence. The control asserts exactly that silence.

Validity condition: in C'' the undetectability must hold. If the
harness can see the gap it is testing, the benchmark measures the
harness, not the system.

The strength of the named gap (content, no content, silence) is a
reported dimension of the benchmark, not a binary.

## 5. The two distinctions (built into guarantees and limitations)

### 5.1 Issuance is not proposal
An independently issued action ID does not, by itself, prove that the
corresponding action was proposed. Issuance proves that the host
requested to propose an action; the independently preserved
commitment to the proposal content is the second witness. For the
high-consequence class the complete default is the pair. The
commitment binds the descriptor as of proposal time, so a modified
action is a new proposal that requires its own commitment.

Guarantee scope: an ID alone witnesses a request; only the pair
witnesses a proposal.
Limitation: without the preserved commitment, the benchmark can name
the gap but cannot state what was proposed.

### 5.2 The binding is not the decision
A cryptographic signature plus policy hash plus ID chain proves
integrity and provenance of the decision record: which guard decided,
under which policy version, on which action. It does not prove:

- correct policy enforcement, because the guard logic itself is
  outside the signature,
- institutional authorization, because key management and mandate are
  institutional facts that the record cannot contain,
- execution of the effect, because the record asserts the effect, and
  the effect stands or falls on its own independently verifiable
  trace.

The guarantee statement is scoped to one sentence: the record is
what it claims to be, from who it claims, under which policy version.

Limitations, each with the mechanism that would bring it inside:
independent re-evaluation of the decision against the recorded policy
(correctness); the key-management record (authorization); a second
binding chain from the system-of-record receipt (effect execution,
out of scope for this note).

## 6. Where the guarantee analysis lands (for the second column)

- Evidence of ID issuance versus evidence of an actual proposal: M3,
  the C family, and section 5.1.
- Local durability versus independent survivability: M2's residual
  (the window in which the record exists in exactly one place) read
  against M3 (the record does not survive at all).
- Detection of missing evidence versus recovery of lost decision
  content: M1 (absence provable, content not), M2 (content returns
  with its original timestamp), M3 (existence and failed
  verification remain provable).
- Cryptographic provenance versus policy correctness, institutional
  authorization, and verified execution: M4, and section 5.2.

Each guarantee states its trust assumptions, failure boundaries, and
residual limitations against the row it belongs to.

## 7. Reporting

Per run, per row, per class: verdict stability; naming (gap named or
unnamed); gap strength (C / C' / C''); recovery (replay landed with
the T1 timestamp, or not); verification (binding verified, or
quarantined). Class P and Class V are reported separately, and the
limitations state what each covers.

## 8. Governance (agreed, recorded here from day one)

- Contribution record: per file and per claim, timestamped, kept with
  the note.
- Authorship: joint, both names on the first page. Author order: the
  contribution record is the substantive basis; the mutual approval
  at finalization, alongside the manuscript and the venue, is the
  form it takes.
- Licensing: MIT for the harness code, CC BY 4.0 for the note
  (proposed by Olusanya; confirm in the contribution record).
- Publication: venue-agnostic; both authors approve the final text
  and the venue before any submission; no third-party content enters
  the note without permission.
- Repository: one shared repository, both contributors as
  maintainers. The direct link arrives with the first runnable
  version; until then the document versions are exchanged in the
  thread with a version line.

## 9. Division of work

- Olusanya: this updated test specification (section 4, this
  document); the first runnable harness, code and tests together, so
  the examination is the run.
- Behar: the guarantee and failure-assumption columns for the four
  rows, built around the four bullets of section 6 and the
  methodological point, since they seed the limitations section.

## 10. Version line

v0.1 (2026-10-30): consolidated from the R5 matrix skeleton and the
2026-10-30 refinements: the P/V class split, the C, C', C'' family,
the two distinctions as sections 5.1 and 5.2, the methodological
point on deterministic keys, and the governance record of section 8.
