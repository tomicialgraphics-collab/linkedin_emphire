---
deliverable: comment
id: 2026-11-12_reply_rock-lambros-rotate-wider-than-the-evidence
date: 2026-11-12
audience: public reply to Rock Lambros in this account's own post thread
status: ready
approved: no
warm: yes
profile_checked: 2026-11-12, and again against the comment written under his post on the same day. Rock Lambros runs RockCyber, is an OWASP GenAI and Agentic AI contributor, and writes as a security practitioner and board adviser. He is replying inside his own field here rather than to a stranger, and he conceded the version string point rather than defending his post, so the reply takes his addition seriously and extends it instead of restating it. Nothing is claimed about him beyond the headline and what he wrote.
thread: what the leaked environment variable names are worth after rotation, and who has to change their setup as a result
premise_checked: checked: the incident facts the exchange rests on were verified on 2026-11-12 for the comment under his post, and nothing new is asserted here. His addition is a claim about consequence rather than a fact, that a list of secret names survives rotation because the next build reads the same environment. The reply accepts it and adds the enumeration problem beside it.
sources_read: none: nothing is attached to his reply. The incident was read and recorded earlier the same day, in the comment file under his post, and no new link is claimed here.
---

## Reply, paste as is

Agreed, and the list is the part that bites. The install record sits on the laptop, and nobody can query every laptop on the day it matters, which is the same reason the version string could not be trusted.

So I would not wait for the list. Rotate for everyone who could have run it rather than everyone you can prove did, and widen that until it is uncomfortable.

Then change the shape while you are in there. A scoped, short lived credential bound to the build identity rather than to the developer's shell means the next build on that laptop needs something the attacker's map cannot reach, and the names stop being worth much even before the rotation finishes.

## Why this reply

He made the point that rotation alone does not finish the cleanup, and he is right. An obvious reply is to agree and stop, which would leave the thread with nothing to act on.

My addition is the population question. His remediation is "for everyone who ran it", and that set is not knowable from the organisation's side: extension install records live on the machines, and the machines are the ones we cannot query. So the practical rule is to act on the population you can bound, an org unit or a team or everyone with the extension allow-listed, rather than the population you can prove. Waiting for evidence is how a credential stays live through a quarter.

His own logic, one step further, is the last part. If the names survive rotation, the fix that ends the cycle is a credential whose value and scope have both changed, so the map points at something that no longer opens anything. Bound to the build identity rather than the developer's shell, because that is the one the next build can present and the attacker cannot.

## Not done here

No restatement of the incident, no second helping of the version string point, and no link. Rock Lambros is the closest security reader this account has and the thread is doing the work on its own.

## Standing item, second time

This is the second text from a comment that has gone out as a post on this account. A first comment under each should carry the AI Red Team Playbook link until a thousand stars, and nothing in either paste shows one. The count stays internal and the comment never asks for a star.
