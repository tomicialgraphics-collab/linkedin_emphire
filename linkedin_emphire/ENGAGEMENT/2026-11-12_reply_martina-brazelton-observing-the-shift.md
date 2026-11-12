---
deliverable: dm
id: 2026-11-12_reply_martina-brazelton-observing-the-shift
date: 2026-11-12
audience: Martina Brazelton, direct message, existing thread
status: ready
approved: no
warm: yes
profile_checked: 2026-11-12 from the thread. Third round in an exchange that started with the four-test message on 5 November. She agreed on the incentive mismatch, put her own frame around it (cold pizza as the business failure rather than the system failure), described Anchored Autonomy as making business intent machine-readable, measurable and traceable, and closed with four direct questions about how I test a system that already exists. The reply answers those questions in order and takes her correction seriously rather than defending the previous message.
thread: what a system should account for, who can act on a published signal, and whether people or software is the better sensor
premise_checked: checked: no new link in her message, so nothing new was opened. The Pizza Hut material already in the thread is the filed suit rather than a rumour, and the earlier file records the sourcing (Chaac Pizza Northeast, filed 6 May 2026 in the Business Court of Texas, case 26-BC01A-0037). This reply quotes none of her figures back at her, since she wrote them and does not need them returned.
sources_read: none: she pasted no link in this message.
---

## Reply, paste as is

Observation is part of it, but it isn't where I start, and it's rarely a shift I get.

Where I have site access I take it, because the queue at the pass shows you what the system never recorded. Where I don't, which is most of the time, I ask for the exception reports and for the one thing an operator checks by hand every morning. That list is the requirement written in behaviour before anyone wrote it down, and it costs an hour rather than a day of shadowing.

On whether the system could even sense it, that's an inventory question rather than a code review. Write down every variable the system reads. Write down what the business calls a failure. Anything on the second list and missing from the first can't be found by testing inside the system at all, because the failure sits outside what it observes. Cold pizza was never a monitoring gap. It was never an input.

On preventing the next one I'd push back slightly. You can't anticipate it, so you make the intent testable instead: a number somebody owns, and something that has to happen when it trips. Then the workaround list becomes the regression suite, re-run whenever conditions change, because last time the requirement showed up in behaviour first.

You're right about the split, though. I answer why the system failed. Yours decides whether anyone notices.
