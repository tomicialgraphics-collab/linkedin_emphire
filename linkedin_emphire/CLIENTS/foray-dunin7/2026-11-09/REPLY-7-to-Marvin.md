Marvin,

The file checks out, and further than you claimed.

Version 7 is 34,757 bytes, SHA-256 b9af6973854d2b27998e6f8775c8e44c791f77888c5a0fd4daeedfa6c9568bce, md5 a2a8e8508ade04c3f83068e263111c92. Drive reports the same size and the same md5, and it also reports the same SHA-256, so the check available to a reader is stronger than the one you wrote.

I did not have to take either number on trust. I reproduced the file. Version 6 at c3888fbf, with the register patch applied, produced exactly 34,757 bytes with byte-identical content to the copy you linked, same SHA-256 and same md5. c3888fbf is confirmed against the version 6 file I hold. The patch id 70e9aec1 I cannot confirm, because it lives in a repository I cannot reach, but the patch in my possession reproduces your bytes exactly, so your claim that the two routes agree is true as far as I can test it.

The acknowledgement is right, and I checked the page rather than the message. Independent reviewer, named for two things and no others, the class A verification of Record A from published material alone and the stream-walk findings, not an auditor, not a security audit, not an endorsement, no implication of affiliation, and W-01c with you. Nothing needs changing.

On the two design decisions.

The producer holding no stream registry: accepted, and for the reason you give. A per-client registry is a volume ledger under another name, and your custody model forbids it. Put the consequence in the text, though, because it is now load-bearing. With the producer stateless, the anchored extent is the only thing between a reordered or dropped batch and a clean verification. Until one segment is anchored for real, that check has only ever run against constructed vectors. §10 item 6 says so, and §10 is where a reader arrives last. Move one sentence of it into §4.4.

Tier-2 refusal: fine, provided the refusal is a named finding and not a silence. Which code does it return, and is there a vector for it?

One thing I found while checking the page, and it belongs to the same class as the entries in the register. The document's own thesis is that verification requires no access to DUNIN7. The eight commits it cites as evidence sit in a repository that returns 404 to anyone outside today. DUNIN7's three public repositories are doneinseven, dunin7-site and stele, and the account's last public push was 19 July. So a reader is asked to take the citations on trust, which is the specific thing this specification exists to remove. Two ways out, and I would take the first: make the repository public. If it cannot be, cite the vector names and the derivation in the document and drop the commit ids.

I will re-run the probes against v0.9 and the live worker, with the group C, D and E fixtures using the derived segment id rather than the stream name. I will send only what reproduces, and the register will carry the version it was run against.

The public statement goes up this week, in exactly the terms you agreed: I reviewed FORAY v0.4, findings from that review were adopted in code and in the specification, nothing about internal documents, and it is a review rather than an audit or an endorsement. I will also say plainly that v0.9 is current and that my probes have not been re-run against it, because a reader deserves to know which version my name is attached to.

Timothy
