---
deliverable: dm
id: 2026-11-13_dm_kuldeep-patil-scope-and-price
date: 2026-11-13
audience: client
status: ready
approved: yes
warm: yes
profile_checked: >-
  Kuldeep Patil replied at 17:54 on 13 November. He wants to run the four scenarios against an isolated n8n simulation with
  synthetic data and no exposure of the core implementation, document what happens, and learn which gaps need attention.
  He then asked the commercial question directly: informal technical collaboration or paid security testing, what I would
  need from his side, and how we would work together. He is early stage and is asking for terms, not for reassurance.
premise_checked: >-
  opinion: the price and the scope are decisions taken here, not facts to check. The $1,500 matches the FORAY week already
  drafted in REPLY-14, so the same week does not carry two prices. Nothing is claimed about what the tests will find.
sources_read: >-
  none: the message arrived in full with no link. His earlier message and the four scenarios are in this repository.
---

## Message, paste as is

<!-- gate:body:start -->
Hi Kuldeep,

Paid, and small enough that you can decide it without a committee.

First pass scope: the four scenarios, run against an isolated n8n instance with synthetic invoices and no access to your
core implementation. I write the cases, run them, and record what the gate does. You get a short report per scenario
what I sent, what the gate decided, and a verdict of pass, fail or unknown, the raw requests as files you can re-run
yourself, and a one page order of what to fix first.

One week from the moment the environment is reachable. $1,500 fixed for all four. If you would rather start smaller,
$600 covers the two I think matter most, approval binding and splitting, in the same format, and we can decide about
the rest once you have read it.

What I need from your side: the n8n instance or a snapshot I can run, the invoice schema and the policy config, and the
ability to stop the policy service mid request. Thirty minutes on a call at each end. An NDA is fine, and I don't need
your source.

Invoice on delivery, seven days to pay. I am not asking for equity and I am not proposing a retainer. What I keep is the
right to describe the method in general, never your implementation or your findings.

If that works, send the environment and I can start on 16 November.
<!-- gate:body:end -->

## What not to say

No hourly rate, no estimate range and no "it depends". No free first pass, which would price the work at zero and teach
him that the next one is negotiable. No describing what I expect to find, because a result promised before the test is a
result he cannot trust. Nothing about the playbook or the case study in this message: the terms are the message.

## Why this is worth the slot

He asked the commercial question in as many words, so the answer has to be a number, a scope and a date. The $600 option
exists so that an early stage founder can say yes without a committee, and it covers the two scenarios most likely to
show something, which makes the smaller yes a real test of the work rather than a discount.
