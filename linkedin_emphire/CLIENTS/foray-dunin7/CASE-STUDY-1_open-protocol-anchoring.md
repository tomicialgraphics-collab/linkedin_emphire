---
deliverable: doc
id: case-study-1-foray-anchoring
date: 2026-11-12
audience: client
status: ready for client read
permission: granted
permission_note: granted 2026-11-12, named, on the condition he reads it before anyone else. He has since confirmed the naming and asked for the draft. Read-first still applies.
client: FORAY (Dunin7)
---

# Five weeks of a claim that was true and not yet reachable

Version 1 was written on 10 November. Three things in it are no longer true, and they are marked in the page
rather than edited away, because a document that hides its own revisions is the failure it describes.

## The situation, in three sentences

An open protocol project was preparing to describe its anchoring and verification story as complete. The author
had built the segment code, the serialiser and the test vectors, and could demonstrate a byte match between
producer and verifier on his own machine. Two things stood between that demonstration and the claim: whether a
holder could reach the code path, and whether anything had ever been anchored on the network that a walk could
read.

## What was reviewed

The producer and verifier as published at the revision the author pinned, the conformance packet, the vector
files, and the specification text beside them. Every claim in the register was checked against one of those
four surfaces and cited to a file and a line, because a review that cannot be re-run from its own citations is
an opinion.

## What the register found

Five findings, of which one was the load-bearing one.

The producer serialised every batch header through the route that carries no segments, and both the batch
accumulator and the Tier-2 aggregator used it. The full segments serialiser existed and was tested. On the
surface the author tested, producer and verifier agreed byte for byte.

What the review added was a reachability question rather than a truth question. The segment path was real, and
no outside client could invoke it: every lane an outside client could register bound to the aggregate. The proof
was correct and the capability was not yet a capability. That distinction moved the finding from "the code is
wrong" to "the claim is ahead of the surface", which is the finding the author accepted and reopened against
his own test.

## What was wrong first, and was corrected

My register opened with a comparison that counted a test file's vectors as evidence of coverage. The author
showed it counted a command he had not run, and the sentence was withdrawn rather than softened. A second
claim, that a specific subsystem was closed, lost its heading and became a registered item instead. A third
correction was mine alone: two commits were named without saying which was which.

Four corrections across seven revisions, three of them prompted by the author, one found by re-reading my own
text. The register carries a revision history for exactly this reason: a reviewer who reports only the
corrections he was forced into is not keeping a record.

## What has changed in the project since

The project closed every item on the register, and closed them in the text as well as in the code, which is the
rarer half. The verifier specification has moved from v0.10 to v0.14 and each revision names the finding it
answers. A correction raised in the last exchange, that one amendment sentence still described the segments
serialiser as unbuilt after it had been built, is closed in both places: Batch Anchoring Amendment v0.26
corrects the sentence, keeps the old wording visible as superseded, and points at the verifier rule; the
specification now points at v0.26 instead of promising a revision that already exists.

## The absence that stopped being an absence

Version 1 of this page ended with the one thing review could not establish: whether a non-zero segment range had
ever been anchored on the public network, since no transaction identifier existed for one, and the absence of a
record is not a record of absence.

That question was answered inside two days, by the project rather than by the review. On 10 November a header
carrying a non-zero segment range was anchored through a client lane, and on 12 November a Tier-2 aggregate
carrying such a header was anchored as well. Three anchors now sit on Kaspa mainnet, at 12:20:15 and 15:17:42
UTC on 10 November and 16:28:25 UTC on 12 November, and each payload is the anchored value and nothing else.

The second transaction spends the first one's output. The third does not: its input is an earlier transaction,
and all three pay one address, which is consistent and is not lineage. The join of the third is inside the
client header within the aggregate leaf, and that is not in the payload. So a holder with a browser can check
each anchor and its block time, and the extent from sequence 0 to 8 is checked with the proof bundle.

This is the outcome the page argued for. The claim was not withdrawn; it was made reachable, and the record
that proves it now exists rather than being promised.

## What is still not established

The live Tier-2 aggregate has one leaf, so the path from the client header to the aggregate root is empty on
chain. A path with sibling hashes is covered by vectors and by the verifier's own tests, not yet by an anchor.

The producer takes the sequence number and the previous transaction hash from the request. It does not read them
out of the record body, and neither does the verifier. The extent proves what was committed and in what order.
It does not prove that the numbers match anything inside the records, and the specification says so.

The verifier's own test suite passes in full, 66 of 66, and that figure is not the conformance vector count.
The specification's table of vector families totals 91 across seven families, and its own note records that the
suite it describes runs 121 vectors in nine families at wire 4.3. A conformance claim has to name the suite
version it was run against, and both numbers are in the text for anyone who wants to check which one is being
used.

## The artefact

The register, revision seven, 34,757 bytes, SHA-256 beginning `b9af6973`, delivered to the author with a
v6-to-v7 patch that applies cleanly and a negative control showing an already-patched tree refusing every hunk.
The author holds the earlier revision and its hash, which is why version six was frozen rather than edited.

## What this is worth to a reader

Not a protocol review. A demonstration that the sentence a team is most confident about is often the one never
tested from the position of the person the sentence is meant to convince.

## Naming, and what it costs

He accepted the point that naming him does not protect anonymity: his name plus his published work makes the
project findable by anyone who wants to find it, so a removal list stops doing its real work at the moment the
name goes in. He chose to be named anyway, which is his call to make and not mine.

The section on where I was wrong first stays in, at his instruction and for the obvious reason.
