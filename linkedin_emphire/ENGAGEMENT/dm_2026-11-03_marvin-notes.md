# FORAY review notes, DM from Marvin Percival, 3 November

## Who he is

Sent the DM at 12:08 today, first degree. DUNIN7, Norwalk. He holds an earlier granted patent,
US 7,330,851, on data security through the removal of elements of a database table, filed 2004 and granted
2008, assigned to Eaglehawk. The FORAY site names a pending application, US 63/980,193. The headline mentions
Kaspathon 2026 top ten and patent pending. This is not someone new to the problem, so the reply is direct and
treats him as a peer.

## What the site actually says, read rather than skimmed

- FORAY is a protocol for tamper-evident transaction evidence: a record is hashed, bound with fresh random
  proof material into a 32-byte commitment, and anchored to a chain. The reference implementation anchors to
  Kaspa. Records never leave the enterprise; the chain holds commitments only; verification needs the record
  and its proof material.
- The grammar is four components: Arrangements, Accruals, Anticipations, Actions. FORAY from 4A.
- The wire is flat and F-coded, F1 to F29, with a published catalog. Prose names and the `foray_*` implementer
  register are compiled to F-codes at emission and never appear in hashed bytes.
- Version discipline is explicit and strong: wire 4.3 is current, 4.2 is superseded but permanently accepted
  and judged as 4.2, 4.1 and 4.0 are converted through a deterministic chain and judged at 4.2, and an
  implementation that raises a legacy record to 4.3 in order to judge it is non-conformant. Records carry
  their own wire version in `schema_version`.
- Sections are marked PROTOCOL INVARIANT or DEPLOYMENT POLICY, which is the distinction most protocol pages
  blur.
- The trust model is stated in its own page and does not overclaim: an anchor proves who asserted what and
  when, and that the assertion has not changed since. A false record must be born false.
- Adoption argument is pull, not push: buyers write the requirement into procurement terms and vendors
  implement. Conformance is testable by design, and the site invites the reader to test the claims.

## The observation in the reply, and why it is the one worth making

Everything above covers integrity of records that exist. It does not cover completeness, and completeness is
the assertion that fails audits: unrecorded liabilities, side letters, payments that never reached a system.
Omission leaves no broken hash. A per-lane expected count or a per-source sequence commitment would make a gap
visible in the same way a tampered record is visible.

## Held back for a second message, not the first

The specification is published as open, and there is a pending patent. Implementers need an explicit
royalty-free patent grant, the way W3C and OWFa agreements do it, or "open" is a claim their lawyers will not
support. Ask about that once he answers the completeness question, not in the same breath, because two hard
questions at once reads as an interrogation.

## Optional move that would earn more than the message

The site invites the test: give it to an AI and ask whether the claims hold. A 20 minute run of the same
experiment done properly, meaning re-serialise a valid record with different key order and whitespace and see
whether verification still passes, would show whether the serialisation law is enforced or merely described.
Reporting that result back is evidence, and evidence is the currency in this conversation.

## What is actually there, checked on the proofs page

Two demonstration records, both anchored to Kaspa mainnet on 24 July 2026, with the Kaspa transaction id
published for each, the leaf salt published by design, the lane named, and a stated body hash. Record A is a
fabricated accounts-payable settlement carrying a realistic source-system mapping, TranID through PmtTerms,
across the F catalog. There is a custody sheet, a body sidecar, a verifier specification at v0.4 with a
class A section for commitment recomputation, and an offline conformance suite with an ANCHOR family.

So the implementation is real and checkable. What is absent is any named customer, pilot or auditor. The
exhibits are demonstration records built to be checked, not evidence of a deployment.

## Where the value sits for this side

1. Independent verification, done and reported. Two commands reproduce the body hash; the salt and lane
   reproduce the commitment against the on-chain payload. That takes minutes and it is the one thing a
   protocol with no third party needs most.
2. An adversarial review of the specification: completeness, replay across lanes and windows, salt custody,
   the migration chain's edge cases. Bounded scope, written output, his name on nothing until he approves.
3. The agent column. His own site puts multi-agent safety next, with Stele for identity and GRANTHA for
   containment. A threat model for evidence emitted by an agent, covering omission, replay and
   mis-attribution of a commitment, is the contribution this side is actually equipped to make.
4. Content afterwards. A post describing a protocol that held under checking is unusual, and it fits the
   existing voice far better than an opinion about protocols in general.

## What not to do

- Do not take an advisory title or equity before there is a paying customer. One inventor, a pending
  application and two demo anchors is a pre-adoption protocol.
- Do not hand over the network. Not until something has been verified independently.
- Do not spend more than an evening before he answers the completeness question. The answer reveals whether
  he has thought about the failure that matters to auditors.
