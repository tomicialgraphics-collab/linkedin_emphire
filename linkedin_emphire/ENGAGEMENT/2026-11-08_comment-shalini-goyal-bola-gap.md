---
deliverable: comment
id: 2026-11-08_shalini-goyal-bola-gap
date: 2026-11-08
audience: public
status: ready
approved: no
warm: no
profile_checked: 2026-11-08 from her headline as supplied. Shalini Goyal, executive director for AI and engineering at JPMorgan, previously Amazon, author, speaker and professor, positioning herself around helping engineers move into AI and high impact roles. No prior interaction on this account.
thread: her post laying out a ten step roadmap for API design, from fundamentals and HTTP through resource design, request shapes, access control with keys and JWT and OAuth and RBAC, validation, databases, performance, docs and testing, deployment and observability, ending by asking which part of API design the reader is currently learning, with a book plug
verified: two technical claims are standard and checkable. Broken object level authorization is the first entry in the OWASP API Security Top 10, and it is a different failure from broken authentication, because a valid credential is presented and the request simply targets a record the caller does not own.
---

# Comment on Shalini Goyal's API roadmap, 8 November 2026

## Why this angle

Her roadmap is thorough and her access control step is where the gap is. Keys, JWT, OAuth, OIDC and RBAC all answer who
the caller is. None of them answer whether this caller may read this record, which is the failure that keeps showing up in
public disclosures, including the border systems work published this month by a researcher whose whole finding was
object-level authorization.

That makes the addition specific and current rather than a general complaint about lists. The post also ends with a
question, so answering it is the natural close and keeps the comment from reading as a correction.

## Comment

One gap worth its own arrow, given how often it is the thing that actually breaks: object-level authorization.

Keys, JWT, OAuth, OIDC and RBAC all answer who the caller is and what role they hold. BOLA asks the other question: may this
caller read this specific record, right now. It sits at the top of the OWASP API list and it survives every mechanism above,
because the token is valid and the request is simply aimed at somebody else's object.

Answering your question, for me it is rate limiting and object-level access control, and the second one is where I keep
finding holes in agent-facing APIs.

## What not to say

No restatement of her ten steps back at her. No comment on the book, positive or otherwise, since a compliment there reads
as a trade and a criticism reads as an ambush. No mention of the specific companies in her headline, and no pitch.

## Held for a later turn

If she replies, the thread worth having is what object-level authorization means when the caller is an agent acting for a
user, because the token belongs to the user and the agent is choosing which objects to ask for. That is a live design
problem in her exact area and it is a better conversation than a list correction.
