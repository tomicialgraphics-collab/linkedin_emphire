# Host-Failure Benchmark, Updated Harness Specification

Version: v0.2 (2026-10-30)
Status: consolidated working draft, integrating Behar’s Working Note
v0.1 received 2026-10-30 with the owner’s v0.1 harness specification.
Subject to technical review and mutual approval. Venue-agnostic.
Contributors: Olusanya Timothy, Behar Dalipi (both, from v0.1).
Integration record: Behar’s guarantee and failure-assumption
analysis is integrated into sections 3, 5, 6, and 7. Attribution of
contributions is recorded in section 10.

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
the recovery mechanism; the residual gap; the test case. Each row's
guarantee is conditional on its stated assumptions. A test result
establishes observed behavior under the implemented failure model,
not a guarantee beyond those conditions.

### M1, guard verdict not emitted

- Conditional guarantee: an independently maintained expectation
  register can establish that a recorded action proposal has no
  corresponding preserved guard verdict within a defined decision
  window.
- Detectable: not at decision time; at review only if the expectation
  register exists outside the guard path.
- Must survive: proposal registration, action identity, proposal
  commitment, and sufficient ordering information must be preserved
  independently of the guard's failure domain through the decision
  window.
- Recovery: none. The decision content is lost; only its absence is
  provable.
- Trust assumptions: proposal registration is non-bypassable and the
  external register preserves identity, commitment, and ordering.
- Failure boundary: absence of a verdict does not establish whether
  the guard executed, failed, or was bypassed.
- Residual limitation: missing decision content cannot be reconstructed
  as historical evidence. A later simulation is not a substitute for
  the original decision record.
- Tests: A, with the register present, names the missing verdict; A',
  the same run without the register, does not name the absence.

### M2, verdict emitted but not preserved centrally

- Conditional guarantee: a durably committed local write-ahead record
  can support eventual recovery and replay after temporary audit-store
  failure.
- Detectable: at persistence failure and at replay, when the record
  surfaces with its original decision timestamp.
- Must survive: the record commits before the applicable execution
  boundary into a local write-ahead copy, preserving a replay path.
- Recovery: replay from that copy to the audit store, carrying the T1
  decision timestamp.
- Trust assumptions: local persistence is acknowledged before the
  execution boundary; write ordering, storage durability, record
  identity, and idempotent replay are enforced.
- Failure boundary: recovery depends on survival and integrity of the
  local persistence domain.
- Residual limitation: local durability is not independent
  survivability. The original decision timestamp must be distinguished
  from an independently verified timestamp; carrying T1 through replay
  alone does not establish independent time attestation.
- Test: B, persistence layer unavailable mid-ship, effect withheld,
  replay restores the verdict with its original T1 timestamp.

### M3, host failure before independent ingestion

- Conditional guarantee: an independently preserved proposal
  commitment can establish that a specific proposal was registered
  and its expected decision evidence is missing.
- Detectable: at reconciliation, only when independent issuance,
  commitment, and reconciliation evidence exist.
- Must survive: the action identity and proposal commitment must be
  preserved outside the host failure domain.
- Recovery: no recovery for the original guard decision. The audit
  system can record a named gap with the strength supported by the
  independent evidence.
- Trust assumptions: external issuance, proposal commitment, and
  reconciliation have independently durable records, a defined
  matching mechanism, and bounded completion expectations.
- Failure boundary: issuance of an action ID alone establishes neither
  proposal content nor that the guarded execution path was entered. A
  preserved commitment establishes what was submitted to the witness,
  not whether the guard evaluated it.
- Residual limitation: the original guard decision may be permanently
  lost. Detection of missing evidence is not recovery of decision
  content.
- Tests: C, preserved proposal commitment; C', issuance without
  proposal content; C'', no independent witness.

### M4, preserved but independently unverifiable record

- Conditional guarantee: under the declared cryptographic trust
  assumptions, verification can establish record integrity and bind the
  asserted decision to an action identifier, policy digest, and signing
  key.
- Detectable: at verification, when an independent verifier checks
  the binding.
- Must survive: the binding (signature, policy digest, and ID chain)
  must be part of the record, not an annotation; the relevant policy
  artifact must also be preserved.
- Recovery: none for a record that arrives without the binding; it is
  quarantined as unverified, never treated as verified.
- Trust assumptions: canonical record encoding, secure signature
  verification, trusted key provenance, algorithm integrity, and
  preservation of the relevant policy artifact.
- Failure boundary: successful signature verification does not
  establish correct policy evaluation, lawful institutional
  authorization, or execution of the resulting effect.
- Residual limitation: the verified record proves only claims within
  its authenticated evidence boundary. Decision correctness requires
  independent policy re-evaluation; institutional authorization
  requires external authority evidence; effect execution requires an
  independently verifiable effect receipt.
- Test: D, record arrives, binding is checked, and any missing element
  causes quarantine.

## 4. Test classes and the C family

Two classes, reported separately in the benchmark:

- Class P, persistence and recovery: A, A', B, C, C', C''. Its claims
  are survival, recovery, and naming, with no cryptographic claim.
- Class V, verification: D and the binding check. Its claim is that
  the binding verifies against the keys it is given. The note states
  that this does not prove production-grade key security or
  institutional trust.

The C family, one host death at T3 under three levels of out-of-band
witness:

- C, the complete pair: an issuer-issued ID plus the independently
  preserved commitment to the action descriptor. Result: a named gap
  with content. Action X’s proposal descriptor was independently
  registered; its guard verdict was never independently recorded.
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
commitment binds the descriptor as of registration time, so a modified
action requires its own commitment.

Guarantee scope: an ID alone witnesses a request; the pair witnesses
that the specified proposal descriptor was independently registered.
It does not prove that the guarded execution path was entered or that
the guard evaluated it.
Limitation: without the preserved commitment, the benchmark can name
the gap but cannot state what proposal content was registered.

### 5.2 The binding is not the decision

Under the declared cryptographic assumptions, verification establishes
record integrity and binds the asserted decision to the action ID,
policy digest, and signing key. It does not establish that the policy
was applied correctly, that the key had institutional authority, or
that the resulting effect actually executed.

The scoped Class V claim is limited to what the cryptographic check
establishes against the keys and artifacts supplied to it. A verified
binding is not, by itself, proof of a trusted guard identity. That
identity depends on key provenance and its authorized relationship to
the guard.

Limitations and the additional evidence that would address them:
independent re-evaluation against the recorded policy (decision
correctness); external authority and key-management records
(institutional authorization); an independently verifiable
system-of-record receipt (effect execution, out of scope for this
note).

## 6. Guarantee-analysis alignment

Behar’s four distinctions map directly to the matrix:

- Evidence of ID issuance versus evidence of an actual proposal: M3,
  the C family, and section 5.1.
- Local durability versus independent survivability: M2's residual
  (the window in which the record exists in exactly one place) read
  against M3 (the record does not survive the host failure).
- Detection of missing evidence versus recovery of lost decision
  content: M1 (absence may be provable, content is not), M2 (content
  can return from the local copy with its original T1 timestamp), M3
  (proposal evidence and missing decision evidence may remain provable,
  while the original guard decision is not recovered).
- Cryptographic provenance versus policy correctness, institutional
  authorization, and verified execution: M4, section 5.2, and the
  stated trust assumptions and residual limitations.

Each guarantee identifies its preconditions, evidence, failure
boundary, and residual uncertainty against its matrix row. Results
must distinguish directly observed behavior from claims conditional
on untested assumptions.

## 7. Cross-cutting methodological conditions

1. Class P tests persistence, survival, recovery, and detection of
   missing evidence.
2. Class V tests functional cryptographic verification using
   reproducible test keys. It makes no production-grade key-security
   or institutional-trust claim.
3. Each assertion identifies its preconditions, expected evidence,
   counterexample, and residual uncertainty.
4. A test establishes a guarantee only within its declared failure
   model.
5. Evidence preservation, decision correctness, institutional
   legitimacy, and effect execution remain separate claims.
6. Proposed acceptance criterion: every matrix row has at least one
   reproducible positive or negative test demonstrating the stated
   guarantee or its limitation. Report observed behavior separately
   from guarantees that depend on untested assumptions.

## 8. Reporting

Per run, per row, per class: verdict stability; naming (gap named or
unnamed); gap strength (C / C' / C''); recovery (replay landed with
the T1 timestamp, or not); verification (binding verified, or
quarantined). Class P and Class V are reported separately, and the
limitations state what each covers.

## 9. Governance (agreed, recorded here from day one)

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

## 10. Division of work

- Olusanya: integrate and maintain this updated test specification;
  implement the first runnable harness, code and tests together, so
  the examination is the run.
- Behar: the guarantee and failure-assumption analysis for the four
  rows, supplied in Working Note v0.1 and integrated into this version;
  Behar reviews the integration and identifies any changes needed.

## 11. Open point and version line

Point closed 2026-11-01, 1:27 PM, by Behar Dalipi: "Class P preserves
the original T1 timestamp through replay without independently
establishing its accuracy or authenticity as the actual decision time.
The distinction between a source-asserted timestamp and an
independently verified timestamp should remain explicit in the
specification and benchmark results." Nothing on this point blocks
implementation.

Reading as confirmed: M2 preserves the original T1 decision timestamp
through replay. That timestamp is source-asserted. The specification
makes no independent time-attestation claim, and neither does the
benchmark: the suite reports a decision-time field that the host wrote
before the ship failed, and separately reports that no mechanism in the
suite can establish that field as the true moment of decision.

v0.2 (2026-10-30): integrates Behar's Working Note v0.1, received
10:16 AM, into the owner’s harness specification v0.1. Adds conditional
guarantees, trust assumptions, failure boundaries, and residual
limitations for M1-M4; sharpens C/C'/C''; separates the original T1
timestamp from independent time attestation; adds proposed acceptance
criteria and observed-behavior reporting. Draft for technical review
and mutual approval, not yet agreed as final.
