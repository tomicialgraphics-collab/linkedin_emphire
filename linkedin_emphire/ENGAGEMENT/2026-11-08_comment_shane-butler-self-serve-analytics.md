---
deliverable: comment
id: 2026-11-08_shane-butler-self-serve-analytics
date: 2026-11-08
audience: public
status: ready
approved: no
warm: yes
profile_checked: 2026-11-08. LinkedIn fetch returns 403, so read from his own site and course pages. Shane Butler, co-founder of AI Analyst Lab. Ten or more years in product data science, causal inference and measurement, with roles at Stripe, Nextdoor, AppFolio, Ontra and PwC, and previously led evaluation strategy for AI product development in legal tech. Co-host of the Data Neighbor podcast and co-teaches Agentic Analytics on Maven. He sells analytical independence for product teams, which makes him a peer on evaluation rather than a general audience.
thread: his post about a CEO handing the whole company AI access to the warehouse with no guidance, promo for the podcast returning Thursday and a free lecture on Tuesday about how data teams are managing the change
verified: the podcast is the Data Neighbor Podcast and it is his, the free lecture is real and linked in his post, and the AI Analyst product is his own open source work per his headline. Nothing in the comment depends on those details, which is deliberate, since a comment under a promo should not read as a review of the promo.
---

# Comment on Shane Butler's post, 8 November 2026

## Why this one

He teaches product teams to analyse their own data, so he is not asking whether self-serve access is good. He is asking
what separates the teams doing it well from the ones doing it badly, which is the question his Thursday episode answers.

That means the comment has to bring the failure mode his framing leaves out. Everybody expects bad SQL. The thing that
actually costs a quarter is definition drift: the agent picks a plausible definition of a metric and the answer never says
which one, so five people are all correct and the meeting cannot resolve anything.

## Comment

The chaos usually isn't bad SQL. It's five people asking for active users and the agent quietly picking five definitions,
none of which are visible in the answer. Everyone is right, and the meeting is unresolvable.

Two things make that survivable. The answer carries the query it ran and the metric definition it used, by name and
version, not just the SQL. And a number quoted on Tuesday can still be re-run next month after three schema changes, or
it's a rumour with a chart attached.

None of that is prompt engineering. It's the discipline warehouses have always needed, arriving faster.

## What not to say

No plug for the Tuesday lecture back at him, since he linked it himself and it would read as being helpful in the way a
leaflet is helpful. No "what are the teams doing right" question, because that is his episode and asking it pre-empts it.
No mention of agents refusing things, which has been the theme all week and does not belong under a data team post.

## Held for a later exchange

His evaluation background is the interesting overlap, not the analytics. If he replies, the question worth asking is how
he evaluates an analyst agent when the ground truth itself is a definition somebody chose, which is a harder eval problem
than accuracy and it is the one his course would have to answer.
