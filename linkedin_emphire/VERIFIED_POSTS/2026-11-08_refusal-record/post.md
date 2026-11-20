---
deliverable: post
id: 2026-11-08_refusal-record
date: 2026-11-08
audience: public
status: ready
approved: no
template: T7
headline: The guard fired. Nobody can find where.
subheadline: A refusal and a failure write the same trace, and only one of them can be reviewed.
headline_alt: A refusal nobody can find is worse than no guard.
subheadline_alt: Two refusals returned the same ninety bytes. Only the durable records told them apart.
headline_alt2: Blocked is not the same as recorded.
subheadline_alt2: Three things every refusal has to leave behind, or the review starts with an argument.
box: NO TRACE
box_alt: REFUSED, UNRECORDED
hashtags: [#AISecurity, #AIEvaluation, #AIGovernance, #AIEngineering]
slot: 13:30 WAT, Sunday 8 November 2026
first_comment: none, the post stands alone
---

Ask your agent for something it is not allowed to do, then go and look for the refusal.

Most systems refuse. Fewer can show, a week later, that they did.

I measured two refusals in a small store this week. They returned identical replies, ninety bytes each, the same hash. Both hosts logged the same three events. Every surface a consumer could read said exactly the same thing. The difference survived in two places only: the durable records, and the state a replay recomputed.

That's the failure worth naming. The guard worked, and the evidence of it nearly didn't exist.

Three things a refusal has to leave behind, or the review starts with an argument:

→ The refusal as an event with its own identity. Not an error line, not a failed status code, its own record with its own sequence number.

→ A named rule, at the version that was in force. A refusal citing a rule that has since been edited is a story.

→ What was withheld, and what the caller was told. Those aren't the same thing, and a reply that says only failed hides both.

Here's where it breaks. If the record is written after the refusal is sent, or by a different process, it can be lost in exactly the case it exists for. It has to come from the thing that refused, before the reply leaves.

A refusal with no trace is worse than no guard, because it lets you believe you have one.

#AISecurity #AIEvaluation #AIGovernance #AIEngineering
