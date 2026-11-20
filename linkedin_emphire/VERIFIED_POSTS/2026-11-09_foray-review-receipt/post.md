---
deliverable: post
id: 2026-11-09_foray-review-receipt
date: 2026-11-09
audience: public
status: ready
approved: no
template: T11
headline: What the verifier could not catch
subheadline: Four findings from an outside review, now closed in someone else's specification.
headline_alt: A stranger read the document
subheadline_alt: The independence claim held, except where it cited a repository nobody can open.
headline_alt2: Not an audit, and I will keep saying so
subheadline_alt2: What an outside review of FORAY v0.4 actually produced.
box: 4 CLOSED
box_alt: v0.4 REVIEWED
hashtags: [#AISecurity, #AIEvaluation, #AIGovernance, #SoftwareEngineering]
slot: 09:00 WAT, Tuesday 10 November 2026
first_comment: none, the post carries the link
---

I reviewed someone else's verification system as an outsider. Four findings from that review are now closed in its specification.

FORAY anchors records so that a verifier can check them without asking DUNIN7 for anything. That claim is the product, so I read version 0.4 the way a stranger would, from published material alone, and wrote down what the verifier could not catch.

In the author's own summary: a continuity walk that did not read the stream history it was given, an empty history treated as clean, an anchored extent checked against nothing, and no way for an entity to show that a list of its streams was complete. One of those four he found himself while reproducing my work, and it stays attributed to him.

Each is now a finding code, a section of the specification and a conformance vector at a named commit. One of them started as a suggestion of mine, an anchored inventory of streams, which turns "is this stream continuous" into "is this list complete". He built the harder version, the one that keeps no state on his side.

What I did not do, because the difference matters in this field. Not an audit. Not a penetration test. Not an endorsement, and nothing here implies I work for DUNIN7. I reviewed 0.4; the current document is 0.9, and I have not re-run my probes against it.

The part worth copying is his, not mine. He closed every item in the register, then wrote his own limits down in the same document, including the one that costs him something to admit: no stream segment has been anchored on mainnet yet.

The specification is public at foray.dunin7.com/spec, and it is a better use of your time than my summary of it. Read the limits section first.

#AISecurity #AIEvaluation #AIGovernance #SoftwareEngineering
