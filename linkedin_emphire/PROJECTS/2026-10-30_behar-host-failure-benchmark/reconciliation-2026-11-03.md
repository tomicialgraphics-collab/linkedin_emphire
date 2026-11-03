# P2 reconciliation, 3 November: reply to the consolidated review

He sent `HFB_P2_Audit.pdf` at 8:54 AM with an archive link at 8:56, and asked for the specific findings
to be reconciled against the shared register before the P2 record is finalised.

## What the review actually establishes

He accepts: baseline Class P 13/13 and Class V 3/3, the nineteen-mode regression campaigns, and the main
P2 repairs (verdict binding, effect withholding, I/O refusal, benign restart). V04 becomes scope with the
synthetic skew kept as a test asset, and N13 is replaced by the directory inventory and digest criterion.
Both match what the register already proposes.

He keeps open V23, V24 and V28 to V33 as assurance boundaries rather than defects, adds five supplemental
findings (S1 to S5), and raises six documentation items.

## The finding that matters most

Three of his documentation items are correct against the published snapshot and already fixed in a tree
that was never pushed. Checked against `main` rather than from memory:

| Item | On `main` | In the working tree |
| --- | --- | --- |
| README Class V count | "Two checks" | "Three checks" |
| Register attribution | No mention of the reviewer at all | Full attribution section, roles separated |
| Evidence paths cited by the register | Do not resolve | Eight logs exist, unpublished |

So his DOC-1, DOC-2 and DOC-4 are not disagreements, they are a publication gap, and calling it anything
else would be dishonest. Corrections that exist only on the author's disk are not corrections.

## The work, in order

1. Publish the reconciliation commit: counts, attribution, `audit/evidence/2026-11-01/` with hashes.
   Bundle ready at `linkedin_emphire/PUBLISH/hfb-p2-reconciliation-2026-11-03/`, instructions in its
   `APPLY.md`.
2. Reproduce S1 to S5 against the pinned source before accepting or disputing any of them. Reproduction is
   the acceptance test and it is his own rule.
3. Row-level dispositions in his four categories: verified, reproduced, limitation, unreconciled.
4. Decide DOC-6 with him: the note says it has not been reviewed by the second author, and there is now a
   review record to cite, while author order and venue stay unsettled until finalisation.

## The reply

Behar,

Received, and the container is the right one: a technical reconciliation against a fixed commit, not an
assessment of the project. I am treating the memo as the working record for P2 and the register as the
place the reconciliation lands.

Three of your documentation items are correct against the published snapshot, and already corrected in a
tree I have not pushed. `README.md` on `main` still says Class V is two checks, because `D'.effect` took
Class V from 2 of 2 to 3 of 3 and the sentence did not move with it. The register on `main` does not name
you at all, and the disposition names you once in passing and separates nothing. The register cites
`evidence/2026-11-01/` and at least one log by name, and neither resolves anywhere public. I fetched both
documents from `main` to check this rather than trusting my own notes, so I am not disputing any of it.

That is your DOC-4 in its general form, and the fault is mine. A correction that exists only on my disk is
not a correction.

The next commit publishes, in one revision: the corrected counts in `README.md` and `TECHNICAL-NOTE.md`,
the attributed register and disposition, and `audit/evidence/2026-11-01/` with eight logs and a hash
manifest, so every cited path resolves at that sha. I will send you the sha and the manifest, not a link
to a branch.

On the focal cases I am adopting your dispositions and your wording. V04 as scope, with the synthetic
skew kept as a test asset and external time provenance expressly disclaimed. N13 replaced by the inventory
and digest criterion, with the self-test that plants a file, and the acceptance condition stated as
inventory and digest equality rather than a universal total of 18.

On the residuals I accept the distinction you are drawing: V23, V24, V29 and V33 are boundaries of what
the test can attest, not defects to be fixed, and none of them will be described as survivability or as
independent time attestation in the publication wording. On V28, V30, V31 and V32 I accept that your P09
shows four low-cost consistency checks with no false positive in the benign control, and I accept the
limit you put on them, which is that they do not hold against an actor who rewrites every correlated
artifact.

The five supplemental findings I am neither disputing nor accepting yet. Reproducing them is the
acceptance test, so they stay in an unreconciled state in the register until I have run your setup against
the pinned source. My expectation, which is not a finding: S1 and S3 will reproduce, S2 in part, S4 and S5
as described.

Two requests. Send the archive as a file with its hash rather than the Drive link, since a link that can
be edited later is the moving target DOC-4 warns about, and I would rather cite a digest. And send the
exact commands and fixtures behind S1 to S5, because I want to reproduce your setup rather than an
approximation of it.

Target: the publication commit this week, then a register revision with one row per item in your four
categories, so you are reviewing a diff rather than prose.

Olusanya

## Do not

- Do not concede a finding that has not been reproduced, and do not dispute one either. "Unreconciled" is
  a real state and it is the honest one.
- Do not promise a date for the architecture-level items (V23, V24, V29, V33). They are scope, not
  backlog.
- Do not let the register and the disposition drift apart again. Both get published in the same commit,
  and every evidence path in either one resolves at that sha.
