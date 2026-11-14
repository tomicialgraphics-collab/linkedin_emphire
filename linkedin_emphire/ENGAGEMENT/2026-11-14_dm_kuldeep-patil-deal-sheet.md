---
deliverable: doc
id: 2026-11-14_kuldeep-patil-deal-sheet
date: 2026-11-14
audience: internal
status: ready
approved: no
premise_checked: >-
  checked: the four-message thread of 14 November was read in full. His 3:21 message asks what I
  would break first, 5:42 answers it with four scenarios, 5:54 accepts the four scenarios inside
  an isolated n8n simulation with synthetic data and asks whether this is informal or paid, and
  6:02 answers paid at 1,000 fixed for four scenarios or 500 for two, one week, invoice on
  delivery. No message from him after that. Nothing here is sent.
sources_read: >-
  read: the pasted thread only. His company is InvisibleAct, described in his own headline as AI
  agent security and runtime authorization. No claim here about his product beyond what he wrote
  in the thread.
---

# Kuldeep Patil, InvisibleAct: what was offered, what must be settled first, and three replies

## Where it stands

| | |
|---|---|
| Who | Kuldeep Patil, founder, InvisibleAct. AI agent security, runtime authorization and enforcement |
| How he arrived | He read a comment on his own post about counting blocks instead of checking whether the block was right, opened the profile, and wrote first |
| What he wanted | What would I break first, in a system that checks an agent's permission before execution |
| What he was given | Four scenarios: metadata and effect disagreeing, approval binding, splitting under a threshold, and the policy service disappearing mid request |
| What he then asked | Informal collaboration or paid engagement, what I would need from him, and how we would work |
| What was offered, 18:02 | Paid. 1,000 fixed for the four scenarios in an isolated n8n instance with synthetic invoices. 500 for approval binding and splitting only. One week from the moment the environment is reachable. Invoice on delivery, seven days to pay. No equity, no retainer. NDA fine, no source needed, method describable in general |
| State now | **Awaiting his environment.** Nothing is owed by us until then and nothing should be sent until he answers |

He is early stage and said so twice. That is the whole shape of the risk: an early-stage founder
who is interested, polite, and has no procurement process to force a decision. The proposal is
written to be decided by one person without a committee, which was the point.

## The one thing that is not settled, and it is the one that decides whether this earns money

**The payment rail is not agreed.** Invoice on delivery is fine for a 1,000 engagement when the
counterparty is easy to invoice. It is not fine when the two sides are in different countries and
there is no deposit, no platform holding the money, and no prior transaction.

This does not need a message today. It needs to be the second sentence of the message that
accepts the environment, before any work starts: which rail, which currency, and which name on
the invoice. If he cannot answer that, the engagement has not started, whatever the calendar says
about 16 November.

The three rails worth offering, in this order: a Wise or Payoneer invoice in USD, then a bank
transfer, then Upwork as a contract if he already has an account and prefers escrow. Not a
crypto wallet, and not "we will sort it after".

## What the 1,000 buys, written so it can be quoted back

**Deliverable, per engagement:** four scenario cases run against his isolated instance, each one
with the request as a file he can re-run, the gate's decision, and a verdict of pass, fail or
unknown. Plus one page ordering what to close first and what each item costs to close. Raw
requests travel with the report.

**Clock:** one week from the moment the environment is reachable and the four prerequisites below
exist. Not from a date on a calendar. If the environment arrives on 18 November, the week starts
on the 18th.

**Unknown is a verdict.** A case that cannot be decided on the evidence produced is recorded as
unknown with the reason, not rounded to pass or fail. This is the one thing in the format that
matters most and the one most likely to be argued about, so it is in the offer rather than in the
report.

**Out of scope, stated now:** his core implementation, his production environment, load or
performance testing, any review of his source, and remediation work. Findings are described;
closing them is a separate decision.

**Price consistency:** the public catalog sells a Red Team Review at 800 for a documented
artifact review. The 1,000 here is above it because it includes a live environment, four authored
cases, and requests he can re-run. The number should not drift below 800 in any negotiation, or
the catalog looks like the expensive option for less work.

## The limitation that must be printed in the report, not discovered by him later

The gate under test is one he built, in a simulator, on synthetic invoices. A finding about it is
a finding about **the simulated gate**. It says a class of bypass exists in that design; it does
not say the production system behaves the same way, in either direction. The first page of the
report carries that sentence, and no line anywhere calls a simulation finding a product finding.

That is also the strongest reason to charge for it: a simulated test that is written down properly
is worth more to him than a production test done informally, because he can hand it to a customer.

## The four prerequisites, before the clock starts

1. The instance is reachable, or a snapshot I can run locally, with the invoice schema and the
   policy configuration in it.
2. Synthetic data only, and a written statement from him that it is synthetic.
3. A documented way to stop the policy service mid request, since scenario four is that scenario.
4. An agreed rail, currency and invoice name.

If any one is missing, the week has not started and the message says which one.

## Three replies, ready

**If he sends the environment.**

```
Kuldeep,

Good, and the isolated simulation is the right first step for both of us. Two things before I start the clock, so neither of us is guessing later.

First, the rail: how do you want to pay the 1,000? A Wise or Payoneer invoice in USD is easiest at my end, a bank transfer works, and if you already run contracts on Upwork I am happy to do it there instead. Tell me which, plus the legal name for the invoice.

Second, the four things I need in the environment: the instance or a snapshot I can run, the invoice schema and the policy config, a documented way to stop the policy service mid request, and your confirmation that the data is synthetic. The week starts when those exist, not on a date.

One thing to be clear about now rather than in the report. What I will be testing is the gate you built in the simulation, so the findings will say what the design does, not what your production system does. That distinction goes on the first page, because it is the difference between a document you can hand a customer and one you cannot.

I will send the cases for your review before I run them, so there are no surprises about what was tried.

Olusanya
```

**If he asks to start smaller.**

```
Kuldeep,

Then take the 500, two scenarios: approval binding and splitting. Those are the two I would expect to land, so you will know within a few days whether the rest is worth buying.

Same format, same week, three cases instead of four, and the same page ordering what to close first. If the two land, the other two are a separate decision later and I will not hold you to it now.

Olusanya
```

**If he says the first message read like a free offer.**

```
Kuldeep,

You are right that it read that way, and that was my wording, not your inference. What I offered there was to tell you which of the four land, which is a sentence, not a test. Running them, recording what the gate actually does, and writing it up so you can act on it is the part I charge for.

The 500 option exists for exactly this reason: two scenarios, so you can see the output before deciding the rest is worth anything.

Olusanya
```

## Calendar

Nothing goes out until he answers. If the environment has not arrived by 18 November, one short
nudge that asks only about the environment and the rail, then nothing further. This is the same
rule as every other row: one nudge, then the ball stays where it is.

If it starts on 16 November, the report is due on the 23rd, which lands inside the 42-day window
and turns the money row from proposed to collected in the same cycle as the catalog work.
