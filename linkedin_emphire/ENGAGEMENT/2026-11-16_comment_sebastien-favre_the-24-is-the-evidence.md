---
deliverable: comment
id: 2026-11-16_comment_sebastien-favre_the-24-is-the-evidence
date: 2026-11-16
time_checked: >-
  checked: 2026-11-16 10:01 WAT, read from the system clock before this file was written.
audience: public
status: ready
approved: no
warm: yes
profile_checked: >-
  Sebastien Favre, first degree, founder of NeoMundi, working on turning AI behaviour into auditable evidence. The owner
  is named on NeoMundi's public use-cases page as an independent reviewer and holds a published recommendation from him,
  so this is a peer comment under a post that invites scrutiny rather than a cold approach. The post thanks Mark Mocnaj
  for an interoperability pilot and quotes Mocnaj's own account of it.
thread: >-
  the OGS and NeoMundi interoperability pilot, five synthetic payloads, three limited-use outcomes, one hold, one
  refusal to admit an observation as a claim, and five corrected receipts. The evidence layer adds 19 matching artifact
  hashes, reproduction of the five-case replay, byte-identical output after newline normalisation, and four ingestion
  anomalies corrected to take the adapter from 24 of 28 to 28 of 28. Mocnaj's own text states the boundaries: synthetic
  observations, no production integration, no independent validation of the governance judgments.
premise_checked: >-
  checked: every figure in this comment, 24, 28, 19 and 5, is taken from the quoted post and used as the author states
  it. Nothing is claimed about the private engine repository, which remains unreadable from this account, and no claim
  is made that the pilot was reviewed here. The one suggestion in the last paragraph is framed as a question to a second
  reader, not as a finding.
sources_read: >-
  blocked: no page was opened for this comment. The post and the quoted text are the whole of the source material. The
  earlier NeoMundi verification work in CLIENTS/neomundi and the thread of 14 November were re-read so that nothing here
  contradicts what has already been published about the relationship.
---

## Comment, paste as is

Twenty-eight of twenty-eight is the least interesting number in that pilot. Twenty-four is the interesting one.

An adapter that lands on 28 first time tells you nothing about the scoring. One that publishes 24, names the four ingestion anomalies, corrects them and then reaches 28 has shown you the instrument working, and that history is what makes the endpoint worth reading.

The stability case is the same lesson pointed the other way. Deterministic replay proves the output repeats. Repeating is not the same as being true, and most dashboards collapse the two into one green tick. Keeping them apart while still publishing the number is the harder thing, and the more useful one.

The line about what the evidence does and does not demonstrate is the part other pilots will copy badly. Writing the boundary down before anyone asks for it is rare, and it's why the numbers above survive contact.

One question I'd put to a second reader: the normalisation rule behind the byte-identical claim. Four anomalies in an adapter is a clean result. A rule that rewrites the input is where a fifth sits quietly.

## Why this rather than congratulations

The post is a thank you, and every reply under it will be another one. A thank you under a thank you adds nothing to Favre and less to the record.

What the comment does is read the evidence the way the post asks to be read. It picks the two properties that the pilot actually demonstrates, that the correction history is visible and that stability and truth were kept apart, and it says why those matter more than the final score. Then it offers the next place to look, which is the only thing a reviewer can usefully add to a result they did not produce.

## The reviewer position

The owner is named publicly on this repository as an independent reviewer, and the recommendation published on 14 November records challenging the handling of the exit-code contract. That history is the reason this comment can ask a question about normalisation without it reading as an attack: it is the same posture, applied to a different artifact, and Favre has taken every such point so far.

It also rules out two things. No credit is claimed for any part of this pilot, because none of it was the owner's work. No praise is heaped on it either, because a reviewer who only praises stops being read as a reviewer.

## What is not here

No link, no offer, no mention of price or availability. The commercial conversation with him is in writing elsewhere and is not advanced by a comment under a public post.

No claim about the private engine repository, which is still unreadable from this account, and no assertion that the pilot was checked here.

## If he replies

The question worth having is whether the normalisation rule is documented in the public repository or lives in the replay code, because those are two different claims about reproducibility. One is a specification. The other is a behaviour you have to read the source to find.
