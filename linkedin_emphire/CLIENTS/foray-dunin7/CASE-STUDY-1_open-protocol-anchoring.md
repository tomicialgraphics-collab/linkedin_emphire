---
deliverable: doc
id: case-study-1-foray-anchoring
date: 2026-11-10
audience: internal
status: draft
permission: not-requested
client: FORAY (Dunin7)
---

# CASE STUDY 1: five weeks of a claim that was true and not yet reachable

Draft. Nothing here is shared until the front matter says `granted`. This is the page to put in front
of the author with the removal list, because a client asked to approve a page that does not exist yet
is being asked for a favour rather than for a decision.

## The situation, in three sentences

An open protocol project was preparing to describe its anchoring and verification story as complete. The
author had built the segment code, the serialiser and the test vectors, and could demonstrate a byte
match between producer and verifier on his own machine. Two things stood between that demonstration and
the claim: whether a holder could reach the code path, and whether anything had ever been anchored on
the network that a walk could read.

## What was reviewed

The producer and verifier as published at the revision the author pinned, the conformance packet, the
vector files, and the specification text beside them. Every claim in the register was checked against
one of those four surfaces and cited to a file and a line, because a review that cannot be re-run from
its own citations is an opinion.

## What the register found

Five findings, of which one was the load-bearing one.

The producer serialised every batch header through the route that carries no segments, and both the
batch accumulator and the Tier-2 aggregator used it. The full segments serialiser existed and was
tested. On the surface the author tested, producer and verifier agreed byte for byte.

What the review added was a reachability question rather than a truth question. The segment path was
real, and no outside client could invoke it: every lane an outside client could register bound to the
aggregate. The proof was correct and the capability was not yet a capability. That distinction moved the
finding from "the code is wrong" to "the claim is ahead of the surface", which is the finding the author
accepted and reopened against his own test.

## What was wrong first, and was corrected

My register opened with a comparison that counted a test file's vectors as evidence of coverage. The
author showed it counted a command he had not run, and the sentence was withdrawn rather than softened.
A second claim, that a specific subsystem was closed, lost its heading and became a registered item
instead. A third correction was mine alone: two commits were named without saying which was which.

Four corrections across seven revisions, three of them prompted by the author, one found by re-reading
my own text. The register carries a revision history for exactly this reason: a reviewer who reports
only the corrections he was forced into is not keeping a record.

## What changed

The author adopted stream history as unavailable material in the next specification revision, replaced
commit identifiers with vector names and derivations so a reader without repository access can still
recompute them, and scoped the producer sentence into the section where the claim is made rather than
the section where it is defended. The public statement was narrowed to the version that is current,
with the producer side described as still being completed.

## The artefact

The register, revision seven, 34,757 bytes, SHA-256 beginning `b9af6973`, delivered to the author with a
v6-to-v7 patch that applies cleanly and a negative control showing an already-patched tree refusing
every hunk. The author holds the earlier revision and its hash, which is why version six was frozen
rather than edited.

## What could not be established

Whether a non-zero segment range has ever been anchored on the public network. No transaction
identifier exists for one, and the absence of a record is not a record of absence. The refusal path that
rejects a malformed segment returns a refusal with no finding code and no vector, so it is a response
and not yet an instrument. The verifier groups that do not depend on the producer were unaffected by any
of this and are tested separately.

## What this is worth to a reader

Not a protocol review. A demonstration that the sentence a team is most confident about is often the one
never tested from the position of the person the sentence is meant to convince.
