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
