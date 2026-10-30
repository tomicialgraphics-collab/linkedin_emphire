# Behar Dalipi, host-failure benchmark thread (DM)

Working thread: benchmark of host-failure modes for decision-record
systems. Co-authored: owner + Behar. Thread-scoped rules (standing):
no repository reference of ANY kind in this DM while the build is
incomplete (link ships with the first runnable harness); the generic
noun "repository" only when answering his explicit governance
questions; no reference to the portfolio project. Earlier rounds
(R1-R4, incl. the T0-T6 trace and the CALL R5 failure-mode matrix) are
in session history, not yet captured in a workspace file.

Division of work (agreed, R5+): owner sends the completed test-case
column and the first runnable harness (code and tests together); Behar
sends the guarantee and failure-assumption columns with the evidence-
to-effect binding notes. License: MIT (code), CC BY 4.0 (note),
proposed by owner, not yet confirmed by Behar in writing. Authorship:
joint, both names; author order per the contribution record (owner) /
mutually approved based on substantive contributions alongside the
manuscript and venue (Behar, 10-30).

---

## 2026-10-30 capture (owner paste, messages 3:35 PM -> 7:07 PM)

### Owner, 3:35 PM (SENT)

Your question on the locally assigned ID is the right one to answer
first, because it changes the design of the host-failure test. The
matrix skeleton and the harness specification are in this message, in
full. The implementation you asked to examine ships with the harness:
the first runnable version I send carries the code and the tests
together, and you run both, so the examination is the run.

You are correct that a locally assigned action ID cannot independently
establish that a missing action existed. The ID is minted on the host,
so the name of the gap dies with the host that named it, and the audit
system cannot distinguish an action that existed and was lost from an
action that never was. The named gap requires the name to have been
witnessed out of band. The fix is to move the minting authority.
Option one: the audit system issues the ID range. The host requests an
ID commitment before proposing the action, and the issuer's own record
is the independent witness that an action with that ID was proposed; it
requires no trust in the host. Option two: the host publishes a hash
commitment of the ID plus the action descriptor at proposal time, and
the full record arrives at decision time. I would take option one as
the default for high-consequence classes, and keep option two for
classes where the round trip to the issuer is not affordable. That
turns your host failure into a pair of tests: with issuance, the audit
system records a named gap with provenance, the action existed, its
verdict was never independently recorded, which is the incident;
without it, the same host death is silent, and the negative control
asserts exactly that silence. The control demonstrates your point
rather than merely covering it.

The matrix skeleton, four rows, five columns: when the failure becomes
detectable, what must survive what, the recovery mechanism, the
residual gap, the test case.

M1, the verdict is not emitted. Detectable never at decision time, at
review time only if an expectation register exists outside the guard
path. The expectation of the verdict must survive outside the guard
path, so the absence can be named. There is no recovery; the decision
is lost and only its absence is provable. The residual is the decision
itself, lost forever. Test A, the register present, the missing
verdict is named; A' is the same run without the register, and the
absence is not named.

M2, the verdict is emitted but not preserved. Detectable at the
persistence failure, and at replay, when the record surfaces with its
original decision timestamp. The record must commit before the effect,
into the local write-ahead copy, so a replay path exists. Recovery is
the replay from that copy to the audit store, carrying the T1
timestamp. The residual is the window in which the record exists in
exactly one place. Test B, the persistence layer down mid-ship, the
effect withheld, the replay lands the verdict with its original
timestamp.

M3, the host dies before ingestion. Detectable at reconciliation only,
and only if the ID commitment was established independently of the
host. The name of the action must survive the host. There is no
recovery for the decision content; the audit system records a named
gap with provenance. The residual is the decision content, lost; the
provable remainder is the action's existence and the failure of its
verification. Test C, the host killed mid-replay with an issuer-issued
ID, the audit system records the named gap; C' is the same death with a
locally assigned ID, and the control asserts the silence.

M4, the record is preserved but not independently verifiable.
Detectable at verification time, when a third party checks the
binding. The binding, signature, policy hash, ID chain, must be part of
the record, not an annotation. There is no recovery for a record that
arrives without it; it is quarantined as unverified, never treated as
verified. The residual is a preserved record that cannot be
distinguished from the host's claim. Test D, the record arrives, the
binding is checked, the missing element is the quarantine.

The harness specification: two local processes, the host and the audit
store. No model, no key, no network, deterministic end to end. The
phases are the T0-T6 trace from round four: proposal, guard verdict,
local commit, ship, effect, recovery, verification. One test per row:
A and A' on M1, B on M2, C and C' on M3, D on M4. Every assertion is
written as claim plus counterclaim, so a failure is a named mismatch,
not a color. The verify step re-derives each assertion from the stored
raw outputs, so a stranger can re-run the check without trusting the
run that produced it. One validity condition: in C', the
undetectability must hold, because if the harness can see the gap it
is testing, the benchmark measures the harness, not the system. The
whole suite must run in under thirty minutes from a fresh machine with
nothing installed beyond the shipped code.

On the arrangements: the note is written venue-agnostic, a short
technical note, the benchmark, the reproducible tests, so the venue
can be chosen after the substance is settled. On licensing, I propose
MIT for the harness code and CC BY 4.0 for the note, unless you prefer
otherwise.

When you are ready: you send the guarantee and failure-assumption
columns with the evidence-to-effect binding notes, and I send the
completed test-case column and the first runnable version of the
harness.

### Behar, 3:55 PM (SENT)

Hi Olusanya,

Thank you for the detailed matrix skeleton and harness specification.
I think we now have a workable foundation for a genuinely useful
technical contribution.

I agree with the four failure modes and the proposed division of
responsibilities.

I would make two distinctions explicit in the guarantee analysis.

First, an independently issued action ID does not, by itself, prove
that the corresponding action was proposed. That requires an
independently preserved commitment to the proposal itself.

Second, a cryptographic signature and policy hash can establish
important properties of record integrity and provenance, but they do
not independently prove correct policy enforcement, institutional
authorization, or the execution of the resulting effect.

These distinctions should be reflected in both the guarantees and the
limitations of the benchmark.

I also suggest distinguishing tests of persistence and recovery from
tests of actual cryptographic verification, particularly given the
proposed key-free harness.

I am comfortable proceeding with the initial technical note and the
agreed division of work. Before substantial development, let's confirm
the author order, contribution records, repository arrangements, and
publication permissions.

Please share the direct repository link when available.

Best regards,
Behar

### Owner, 5:58 PM (SENT)

The two distinctions are correct, and they are the two places where
the guarantee analysis would otherwise overclaim. They belong in both
the guarantees and the limitations, as you say, and they change the
test family, which I will send with the updated specification. I will
take them in order, then the test-class point, then the governance
items you listed.

On the ID: agreed, and the refinement is that issuance and commitment
are two different witnesses. Issuance of an ID proves that the host
requested to propose an action. It does not prove what was proposed.
The independently preserved commitment to the proposal content is the
second witness, and for the high-consequence class the complete
default is the pair: issuer-issued ID plus the preserved commitment to
the descriptor. Issuance alone gives a weaker named gap: an ID was
issued and never resolved, content unknown. The complete pair gives
the full named gap: action X was proposed, its verdict was never
independently recorded. One corollary follows: the commitment binds
the descriptor as of proposal time, so a modified action is a new
proposal that requires its own commitment. This splits the host-
failure test into three: C, the complete pair, a named gap with
content; C', issuance only, a named gap without content; C'', what the
current specification calls C', the locally assigned ID, silence. The
strength of the named gap becomes a reported dimension of the
benchmark, not a binary.

On the binding: agreed, and the limit is exactly what you named. The
signature plus policy hash plus ID chain proves integrity and
provenance of the decision record: which guard decided, under which
policy version, on which action. It does not prove that the decision
was correct against that policy, because the guard logic itself is
outside the signature. It does not prove institutional authorization,
because key management and mandate are institutional facts that the
record cannot contain. It does not prove that the effect was executed,
because the record asserts the effect, and the effect stands or falls
on its own independently verifiable trace. So the guarantee statement
in your column should be scoped to one sentence: the record is what it
claims to be, from who it claims, under which policy version.
Correctness, authorization, and effect execution go into the
limitations, each with the mechanism that would bring it inside:
independent re-evaluation of the decision against the recorded policy
for correctness, the key-management record for authorization, and a
second binding chain from the system-of-record receipt for the effect.
The last one is the natural extension and out of scope for this note.

On separating the test classes: agreed, and the key-free line refines
as follows. The harness stays model-free and network-free. The
verification tests use a deterministic key pair generated in-process
from a fixed seed, so nothing external enters the run and the result
is fully reproducible. The specification labels two classes. Class P,
persistence and recovery: A, A', B, C, C', C''. Its claims are
survival, recovery, and naming, with no cryptographic claim. Class V,
verification: D and the binding check. Its claim is that the binding
verifies against the keys it is given, and the note states that this
does not prove the keys are institutional, which is your second
distinction applied to the test itself. The two classes are reported
separately in the benchmark, and the limitations state what each
covers.

On the governance items before substantial development. Contribution
record from day one, per file and per claim, timestamped, kept with
the note. Author order follows that record at finalization, so the
order is a fact, not a negotiation. Both names, joint authorship, as
agreed. Repository arrangement, confirmed in principle: one shared
repository, both of us as maintainers, MIT for the code, CC BY 4.0 for
the note. The direct repository link arrives with the first runnable
version, as stated. Until then, this thread is the full surface of the
material. Publication permissions: venue-agnostic as stated; both
authors approve the final text and the venue before any submission,
and no third-party content enters the note without permission.

When you are ready: your guarantee and failure-assumption columns with
the two distinctions built in, since they seed the limitations
section. And I send the updated harness specification with the two
test classes labeled and the C, C', C'' family, so the first version
of the harness and the first draft of the note proceed from the same
document.

### Behar, 7:07 PM (SENT)

Hi Olusanya,

Thank you for the detailed refinements. I think we have reached a
sufficiently concrete foundation to move into a structured working
document.

I agree with separating persistence and recovery tests (Class P) from
cryptographic verification tests (Class V), and with distinguishing C,
C', and C'' according to the independently preserved evidence.

For my part, I will structure the guarantee and failure-assumption
analysis around the four failure modes, with particular attention to:

- The distinction between evidence of ID issuance and evidence of an
  actual proposal.
- Local durability versus independent survivability.
- Detection of missing evidence versus recovery of lost decision
  content.
- Cryptographic provenance versus policy correctness, institutional
  authorization, and verified execution.

Each guarantee will explicitly identify its trust assumptions,
failure boundaries, and residual limitations.

One methodological point: deterministic test keys are suitable for
reproducible functional verification, but should not be presented as
evidence of production-grade key security or institutional trust.

I also agree with maintaining contribution records from the outset.
Author order should ultimately be mutually approved based on
substantive contributions, alongside the final manuscript and
publication venue.

I suggest that we now consolidate the matrix and the updated test
specification into a version-controlled working document, with both
contributors clearly identified, before progressing to the runnable
harness.

Best regards,
Behar

---

## Owner reply (R8, DRAFT 10-30, DRAFTED, owner sends when ready)
- CALL: accept the methodological point as the Class V limitation
  (claim and limit in the same sentence); map his four bullets onto
  the matrix rows so his columns have a landing row (issuance vs
  proposal -> M3 C family; local durability vs independent
  survivability -> M2 residual vs M3; detection vs recovery -> M1,
  M2, M3 split; provenance vs correctness/authorization/execution ->
  M4 + scoped guarantee); author order agreed in his form (record =
  substantive basis, mutual approval = the form it takes, formality
  because the record is kept from day one); working document agreed as
  v0.1 with both contributors named on the first page; store timing
  kept (opens with the first runnable version, as stated; thread
  versions with a version line until then, so nothing depends on
  store timing). No repository link, no project reference
  (thread-scoped rule stands).
- COMPANION: the updated harness specification v0.1 is prepared in
  PROJECTS/2026-10-30_behar-host-failure-benchmark/ and goes as a
  standalone document in the thread (the "same document" the harness
  and the note proceed from).

The methodological point is accepted as stated, and it sharpens the
Class V limitation. The deterministic key pair supports reproducible
functional verification, and the note says so in one sentence: Class
V shows that the binding verifies against the keys it is given, and it
states that this is not evidence of production-grade key security or
institutional trust. The claim and its limit in the same sentence, in
the same place.

Your four bullets have rows to land on. Issuance versus actual
proposal is the C, C', C'' family in M3, where the strength of the
named gap is the reported dimension. Local durability versus
independent survivability is M2's residual, the window in which the
record exists in exactly one place, read against M3, where the record
does not survive at all and only the name, or its absence, survives.
Detection of missing evidence versus recovery of lost content splits
across three rows: M1, where the absence is provable and the content
is not; M2, where the content returns with its original timestamp;
M3, where what remains provable is the action's existence and the
failure of its verification. Provenance versus correctness,
authorization, and execution is M4 with the scoped guarantee
statement, and the three limitations each carry the mechanism that
would bring them inside. So the guarantee analysis writes directly
against the matrix rows, and each guarantee states its trust
assumptions, failure boundaries, and residual limitations against the
row it belongs to.

On author order: agreed in the form you stated. The contribution
record, kept from day one per file and per claim, is the substantive
basis, and the mutual approval at finalization, alongside the
manuscript and the venue, is the form it takes. With the record kept
from the start, that approval should be a formality, which is the
reason for keeping the record rather than reconstructing
contributions at the end.

On the working document: agreed, and it starts now as v0.1. The
contents are the matrix with the four rows and five columns, your
guarantee and failure-assumption columns written against the four
bullets, the updated test specification with the P and V classes
labeled and the C, C', C'' family, the two distinctions built into
both the guarantees and the limitations, both contributors named on
the first page, and the contribution record kept with the document.
The version-controlled store opens with the first runnable version,
as stated, and the direct link arrives then; until then each version
is exchanged in this thread with a version line, so the document has
a history from v0.1 and nothing depends on the store's timing.

When you are ready: send your guarantee and failure-assumption
columns for the four rows, built around the four bullets and the
methodological point, since they seed the limitations section. I send
the updated test specification with the class labels and the C family
as the next message, as a standalone document, and the first runnable
version of the harness follows the two, so the note, the tests, and
the code proceed from the same document.

---

## 2026-10-30 next exchange (owner 12:42 AM; Behar 10:16 AM)

### Owner, 12:42 AM (SENT; verbatim from owner paste)

The methodological point is accepted as stated, and it sharpens the
Class V limitation. The deterministic key pair supports reproducible
functional verification, and the note says so in one sentence: Class
V shows that the binding verifies against the keys it is given, and it
states that this is not evidence of production-grade key security or
institutional trust. The claim and its limit in the same sentence, in
the same place.

Your four bullets have rows to land on. Issuance versus actual
proposal is the C, C', C'' family in M3, where the strength of the
named gap is the reported dimension. Local durability versus
independent survivability is M2's residual, the window in which the
record exists in exactly one place, read against M3, where the record
does not survive at all and only the name, or its absence, survives.
Detection of missing evidence versus recovery of lost content splits
across three rows: M1, where the absence is provable and the content
is not; M2, where the content returns with its original timestamp;
M3, where what remains provable is the action's existence and the
failure of its verification. Provenance versus correctness,
authorization, and execution is M4 with the scoped guarantee
statement, and the three limitations each carry the mechanism that
would bring them inside. So the guarantee analysis writes directly
against the matrix rows, and each guarantee states its trust
assumptions, failure boundaries, and residual limitations against the
row it belongs to.

On author order: agreed in the form you stated. The contribution
record, kept from day one per file and per claim, is the substantive
basis, and the mutual approval at finalization, alongside the
manuscript and the venue, is the form it takes. With the record kept
from the start, that approval should be a formality, which is the
reason for keeping the record rather than reconstructing
contributions at the end.

On the working document: agreed, and it starts now as v0.1. The
contents are the matrix with the four rows and five columns, your
guarantee and failure-assumption columns written against the four
bullets, the updated test specification with the P and V classes
labeled and the C, C', C'' family, the two distinctions built into
both the guarantees and the limitations, both contributors named on
the first page, and the contribution record kept with the document.
The version-controlled store opens with the first runnable version,
as stated, and the direct link arrives then; until then each version
is exchanged in this thread with a version line, so the document has
a history from v0.1 and nothing depends on the store's timing.

When you are ready: send your guarantee and failure-assumption
columns for the four rows, built around the four bullets and the
methodological point, since they seed the limitations section. I send
the updated test specification with the class labels and the C family
as the next message, as a standalone document, and the first runnable
version of the harness follows the two, so the note, the tests, and
the code proceed from the same document.

### Behar, 10:16 AM (RECEIVED; verbatim from owner paste)

Working Note v0.1 — Guarantee and Failure-Assumption Analysis

Proposed joint work: Behar Dalipi and Olusanya Timothy
Section draft contributed by: Behar Dalipi
Scope: Decision-time evidence, persistence guarantees, failure assumptions, and independently verifiable governance records.

M1 — Guard Verdict Not Emitted

Conditional guarantee: An independently maintained expectation register can establish that a recorded action proposal has no corresponding preserved guard verdict within a defined decision window.

Trust assumptions: Proposal registration must occur through a non-bypassable mechanism, outside the guard's failure domain. The register must preserve action identity, proposal commitment, and sufficient ordering information.

Failure boundary: The absence of a verdict does not establish whether the guard executed, failed, or was bypassed.

Residual limitation: Missing decision content cannot be reconstructed as historical evidence. A later simulation is not a substitute for the original decision record.

M2 — Verdict Emitted but Not Preserved Centrally

Conditional guarantee: A durably committed local write-ahead record can support eventual recovery and replay after temporary audit-store failure.

Trust assumptions: Local persistence must be acknowledged before the applicable execution boundary; write ordering, storage durability, record identity, and idempotent replay must be enforced.

Failure boundary: Recovery depends on the survival and integrity of the local persistence domain.

Residual limitation: Local durability is not independent survivability. The original decision timestamp must also be distinguished from an independently verified timestamp.

M3 — Host Failure Before Independent Ingestion

Conditional guarantee: An independently preserved proposal commitment can establish that a specific proposal was registered and that its expected decision evidence is missing.

Trust assumptions: External issuance, proposal commitment, and reconciliation must have independently durable records, a defined matching mechanism, and bounded completion expectations.

Failure boundary: Issuance of an action ID alone establishes neither the proposal content nor that a guard evaluated it. A preserved commitment establishes what was submitted to the witness, not necessarily whether the guarded execution path was entered.

Residual limitation: The original guard decision may be permanently lost. Detection of missing evidence must never be represented as recovery of decision content.

Test distinction: C tests a preserved proposal commitment; C' tests issuance without proposal content; C'' tests the absence of an independent witness.

M4 — Preserved but Independently Unverifiable Record

Conditional guarantee: With appropriate cryptographic trust assumptions, verification can establish record integrity and the binding of an asserted decision to an action identifier, policy digest, and signing key.

Trust assumptions: Canonical record encoding, secure signature verification, trusted key provenance, algorithm integrity, and preservation of the relevant policy artifact are required.

Failure boundary: Successful signature verification does not establish correct policy evaluation, lawful institutional authorization, or actual effect execution.

Residual limitation: The verified record proves only claims within its authenticated evidence boundary. Decision correctness requires independent policy re-evaluation; institutional authorization requires external authority evidence; effect execution requires an independently verifiable effect receipt.

Cross-Cutting Methodological Conditions

1. Class P tests persistence, survival, recovery, and detection of missing evidence.
2. Class V tests functional cryptographic verification using reproducible test keys. It makes no production-grade key-security or institutional-trust claim.
3. Each assertion must identify its preconditions, expected evidence, counterexample, and residual uncertainty.
4. A test may establish a guarantee only within its declared failure model.
5. Evidence preservation, decision correctness, institutional legitimacy, and effect execution must remain separate claims.

Proposed acceptance criterion: Every matrix row must contain at least one reproducible positive or negative test demonstrating the stated guarantee or its limitation. Results must distinguish observed behavior from guarantees that depend on untested assumptions.

Draft v0.1 — subject to technical review, integration, and mutual approval by both contributors.

### DISCUSS

- Behar has now supplied the requested guarantee and failure-
  assumption analysis for M1-M4. The v0.1 harness specification
  already contains the matrix, C family, class split, governance
  decisions, and initial alignment, but Behar's new note adds the
  conditions and limits that need to be explicit per row.
- New precision to integrate: M1's non-bypassable independent
  expectation register; M2's local persistence and idempotent replay
  assumptions plus timestamp-attestation distinction; M3's boundary
  between a preserved proposal commitment and proof the guard was
  entered; M4's crypto assumptions and strict evidence boundary.
- Next step in the thread sequence: send the integrated test
  specification as a standalone v0.2 document, with no repository
  link. First runnable harness follows after this document is reviewed.

### THOUGHT

- Preserve v0.1; produce a separately versioned v0.2 instead of
  silently rewriting the prior baseline.
- Integrate Behar's analysis without turning conditional guarantees
  into unconditional claims. Include a concrete open point: the
  original T1 timestamp survives replay, but replay alone does not
  establish independent time attestation. Ask Behar to confirm that
  this captures his intended distinction before implementation.
- Keep collaboration terms as recorded: mutual approval on final
  authorship/order, license terms still proposed until confirmed.
  The working document may be exchanged as an attachment; do not
  send a repository link before the first runnable harness.

### DELIVERABLE

Prepared `PROJECTS/2026-10-30_behar-host-failure-benchmark/spec-v0.2-integrated-guarantee-analysis.md` as a standalone integrated draft. Not sent. Draft reply:

Behar,

Thank you. I’ve integrated your guarantee and failure-assumption analysis into the updated specification. I kept your distinctions against the four rows and made the guarantees conditional on the assumptions and failure boundaries. I also separated carrying the original T1 timestamp through replay from independently verifying that timestamp. Please review the attached v0.2 and flag any changes, especially that timestamp distinction. Once we agree on it, I’ll move to the runnable harness.
