---
deliverable: comment
id: 2026-11-08_salman-lakhani-fallback-attribution
date: 2026-11-08
audience: public
status: ready
approved: no
warm: no
profile_checked: 2026-11-08 from his headline and post. Salman Lakhani, data and AI governance leader working in master and reference data, stewardship and data quality, fifteen or more years across financial services and healthcare, founder of LLCreativity. He writes analytical posts with a stated read and one or two concrete actions, and closes with a question to readers, which is the opening the comment uses.
thread: his post on Anthropic paying 3.4 billion dollars for 1.7 gigawatts of Caterpillar generators by taking over OnePWR's place in the delivery queue, his read that a company paying to jump an equipment queue is telling you its capacity plan is a forecast rather than a promise, and his two actions: measure peak tokens per minute against your real ceiling, and put one fallback model behind a flag with real traffic
verified: the deal is as he describes it. The Financial Times reported it on 8 November, Reuters and others note they could not independently confirm it, and a Piper Sandler transaction listing corroborates a 3.4 billion dollar sale of OnePWR's power generation platform to an unnamed frontier AI lab in September. Anthropic did not buy the company. The comment asserts none of this, since he has already stated it correctly.
---

# Comment on Salman Lakhani's fallback post, 8 November 2026

## Why this one

His post ends with a direct question to readers, which makes it the one post in the feed that is actively asking for an
answer rather than collecting agreement. He is also a governance person rather than an infrastructure one, so the useful
addition is not more about generators. It is about what the fallback does to the evidence.

The point is his own frame applied one step further. A capacity plan is a forecast. A fallback model is also a forecast,
and the difference is that the fallback silently becomes fact, with nothing downstream knowing which system produced the
answer it is reading.

## Comment

Tested, and the part that made it worth doing was the record rather than the reroute.

Once the flag flips, two different systems are producing one indistinguishable stream of answers, and nothing downstream
knows which one it got. So the same half hour should settle two things: every response carries which model produced it,
and the switch logs when it flipped and why.

Otherwise the question nobody can answer in March is the one your post is really about. The capacity was a forecast, the
fallback was too, and the only evidence of which one you got is somebody's memory of a flag.

## What not to say

No restating the acquisition details, which he has already got right, and no doubt about the FT report, since it is
unconfirmed but well sourced and questioning it in his comments adds nothing. No claim about what Anthropic should have
done. No mention of my own work.

## Held for a second turn

If he replies, the sharper version is in his own post already and he may not have noticed it: Anthropic's amended filing
lists on-site gas generation as exposing it to fuel price volatility outside its control, which is the same sentence as his
forecast point, written by the company itself. That is a good follow-up and a bad opening, because it would make the
comment about Anthropic instead of about him.
