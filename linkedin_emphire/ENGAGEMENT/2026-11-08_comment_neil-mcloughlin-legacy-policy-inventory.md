---
deliverable: comment
id: 2026-11-08_neil-mcloughlin-legacy-policy-inventory
date: 2026-11-08
audience: public
status: ready
approved: no
warm: no
profile_checked: 2026-11-08 from his headline and public work. Neil McLoughlin, principal technical account manager at Nerdio, Microsoft MVP, author and co-author of a book on Azure Virtual Desktop, working across Windows 365, Intune, Azure and end user computing. He writes specific operational alerts rather than opinion, and he ends this one with a direct question.
thread: his post warning that the User settings blade for Cloud PC is becoming legacy and cannot take new policies, that the local admin toggle now lives in Cloud PC configurations, that the most recently created policy wins when users sit in more than one, that scripts adding people to the local admin group may be overridden, and recommending an export and deliberate rebuild rather than a copy and paste
verified: everything specific in the post is his, and nothing in the comment restates or disputes it. The comment talks about the consequence of two mechanisms writing the same state, which follows from his third point rather than adding a new claim about Intune.
---

# Comment on Neil McLoughlin's Intune migration post, 8 November 2026

## Why this angle

Off-lane for this account, on purpose. He writes operational alerts and most of his commenters will either thank him or ask
which tenants are affected. Neither is useful.

His third point is the one with a second life. A policy and a script both writing local admin membership means last writer
wins, and the loser leaves no record of having been overridden. That is the same failure this account spends its weeks on in
a different technology, so it can be said here in his terms without any pivot at all.

## Comment

The bit that will bite in six months is number three. Two mechanisms writing the same state, policy and script, means
whoever runs last wins, and the loser leaves no line saying it was overridden. That is how local admin quietly comes back
after somebody removed it.

So the inventory is worth more than a list of policies. One record per person: who has local admin, why, which mechanism
granted it, and when it was last checked. When the next blade gets renamed, the rebuild starts from intent instead of from
whatever the previous export happened to capture.

And to your question: if the honest answer is nobody, that is already the finding.

## What not to say

No technical correction, since the post is accurate and specific. No thanks-for-sharing. No statement about what Microsoft
should have done. No mention of AI, agents or my own work, which would be the most obvious off-topic pivot in the feed
today.

## Held for a later turn

If he replies, the natural question is whether the new Cloud PC configurations expose an audit trail per change, since that
decides whether the next migration is a rebuild from intent or another export of whatever was left behind. That is a
practical answer he may already have.
