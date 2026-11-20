---
deliverable: dm
id: 2026-11-12_reply_martina-brazelton-who-can-act-on-it
date: 2026-11-12
audience: Martina Brazelton, direct message, existing thread
status: ready
approved: no
warm: yes
profile_checked: 2026-11-12 from the thread. Martina Brazelton works on Anchored Autonomy, which she describes as testing the reliability of decisions themselves and the conditions under which a decision counts as reliable. This is an ongoing exchange rather than a cold approach: she replied to the four-test message sent on 5 November, picked out the reachability point as the one she liked, and asked a direct question at the end. The reply answers that question and does not restart the thread.
thread: what a system should be accounting for, and how to find the variable nobody modelled, prompted by her Pizza Hut case
premise_checked: checked: the Pizza Hut matter is real and is a filed suit, not a rumour. Chaac Pizza Northeast, 111 locations across New York, New Jersey, Maryland, Washington DC and Pennsylvania, filed in the Business Court of Texas on 6 May 2026 against Pizza Hut and Yum, seeking at least 100 million, case 26-BC01A-0037. The complaint says Dragontail gave DoorDash Dashers visibility into kitchen timing, that drivers waited up to fifteen minutes to batch orders, that rack time had been under five minutes before the rollout, and that New York City same-store sales growth went from positive 10.19 percent to negative 9.78 percent. Every one of those is an allegation in a complaint and the reply says "the complaint's own detail", which keeps it there.
sources_read: none: she pasted no link. The Pizza Hut facts were checked against Business Insider, ppc.land and two further trade write-ups covering the same filing.
---

## Reply, paste as is

I remember it, and I don't think the missing variable in that one was temperature. Your case's own detail is that the system showed Dashers when pizzas were coming out of the oven, and they started waiting up to fifteen minutes to batch. Rack time had been under five minutes. Nobody had modelled a party whose incentive is earnings per hour rather than delivery speed.

Which gives me the first thing I ask about any system now. For every signal it publishes, who can act on it, and what do they gain by acting? A timing feed handed to a driver isn't neutral information. It's an input to somebody else's optimisation, and when their objective isn't yours, the system is quietly working for the other side of the transaction.

There's a slower method, and it's watching people rather than software. The batching was the requirement written in behaviour before anyone wrote it down. The workaround a human invents is usually the spec they were never given, and it shows up first in support tickets, manual overrides and the thing an operator checks by hand every morning.

It catches it after people have already compensated, which is the limit. The earlier version is asking what someone checks by feel, because anyone who has run a shift keeps that list and rarely thinks to hand it over.

## Why this answers her question rather than agreeing with it

Her question is the good one: how do you find what the builders never knew was missing. The tempting answer is "test for temperature", which is just restating her example. The reply takes the same case and finds a different missing thing in it, which is the incentive of the party who received the signal.

That distinction matters to her work because it is a class, not an instance. Temperature is a domain fact somebody could have listed. A third party's objective function is a structural omission, and it is invisible from inside the model no matter how much testing happens there.

The second method is the one I actually use and the one nobody writes about: the workaround is the requirement. Drivers batching, operators keeping a spreadsheet, engineers with a manual override in a wrapper script. All of those are the system's missing specification, expressed in behaviour, and they appear before the incident rather than after it.

## What I left out

The four-test framework from the earlier message. She has read it and quoted it back; repeating it would make the reply a recital.

The 10.19 to negative 9.78 sales swing and the 111 locations. They are striking and they are her case, not the point of my answer, and a message that replies to a question with a better set of figures than she brought is doing something other than answering.

No link, no offer of a call, nothing about my own work beyond the method.

## If she replies

The place this goes is her Anchored Autonomy question of what conditions a decision needs. The next useful thing I could say is that a condition nobody wrote down cannot be anchored, and the workaround is the only place it shows up before it fails, which would make the post-incident review the wrong place to start collecting conditions.
