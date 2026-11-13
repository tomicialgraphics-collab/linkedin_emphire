---
deliverable: doc
id: offer-implementation-checklist
date: 2026-11-13
audience: owner
status: draft
---

# Implementing the six levers, in the order that pays first

Total time: about 45 minutes of clicking, plus one message at the end of the next contract. Nothing here needs a decision
from anyone else. Every field named below is one that exists on the live catalog screen today.

## Baseline, taken before anything changes (2 minutes)

Write these down before the first edit, or the fourteen day read is worthless:

| Number | Value on 13 November |
|---|---|
| Red team listing views | 6 |
| Chatbot listing views | 5 |
| Orders, both listings | 0 |
| Consultation listing views | 0 |
| Proposals sent | 0 |
| Price asked in a DM | not yet counted, start counting today |

## Step 1. Red team listing, Pricing step, the three tier descriptions (5 minutes)

Upwork gives each tier a custom title of 30 characters and a custom description of 80. The titles stay as they are. Only
the descriptions change, because each one currently describes the deliverable and none describes the outcome.

| Tier | Custom description (character count) |
|---|---|
| Starter, $150 | `15 injection attempts and a one-page findings report, 3 days` (60) |
| Standard, $600 | `Four-layer test of one AI feature, reproducible findings, 7 days` (64) |
| Advanced, $1,500 | `Full test, the fixes applied, and a verification re-test, 14 days` (65) |

## Step 2. Red team listing, Add-ons (3 minutes)

- Delete the 14 day re-test add-on if it is priced at a token amount. It becomes part of what is included, not a line item.
  A one dollar premium tells the buyer the most useful thing you send is worth a dollar.
- Keep rush delivery at $75.
- Add the executive summary at $100 if it is not there. It is the most bought premium in this category, because the buyer
  is not the person who has to approve the invoice.

## Step 3. Red team listing, the project description (10 minutes)

Replace the description with this. It opens with the outcome, then the proof, then the guarantee, then the limit, then
the queue.

```
Find out what your AI feature does when someone who is not your user talks to it.

Most AI security reports fail in the same three places. The finding cannot be reproduced because the model revision moved
or the prompt was edited, the rate is quoted without a denominator, and the classes nobody tested are left off the page. I
run the test backwards from those three failures.

What you get at every tier: the prompt, the model revision and the date for each finding, so you can run it yourself and
get the same result. A page showing what was not tested, with a written reason for every skipped class. A recorded
walkthrough so somebody who was not on the call can follow it, and a one page summary written for whoever signs off.

Every finding is reproducible or it is not a finding. If any finding cannot be reproduced from what I give you, I strike it
and replace it with a new test at no charge, and if there is nothing left to replace it with, you get the money back.

One thing I will not guarantee: that a system is safe. Nobody can guarantee that, and anyone who does is selling you a
certificate rather than a test.

Two four-layer tests a week, because each one takes three days of my own time and I do the work myself. If the calendar is
full when you book, you get the next available date before you pay.

The verification re-test 14 days after you ship the fixes is included, not sold separately.
```

## Step 4. Red team listing, FAQ (5 minutes)

Three questions, written the way a buyer asks them. This is where the guarantee and the scarcity live a second time, in
the place a cautious buyer actually reads.

**Q: What if a finding does not reproduce on my side?**
A: Send me the prompt and the revision you ran it on. If it does not reproduce, I strike it from the report, replace it
with a new test at no charge, and if there is nothing left to replace it with, you get the money back.

**Q: How many of these do you run at once?**
A: Two a week. Each four-layer test takes three days and I run every one myself, so the calendar is the limit. You get the
date before you pay, and I tell you if it slips.

**Q: What is not included?**
A: A guarantee of safety, load testing, and testing of a system you do not own or have written permission to test. Those
three are out because none of them can be delivered honestly.

## Step 5. Chatbot listing, description and the one dollar add-on (10 minutes)

Delete the one dollar re-test add-on. Keep the $150 integration add-on. Then replace the description:

```
Your agent gets tested by someone who did not build it, before your users test it for you.

You get a working build and the suite that proves it still works: regression tests derived from the failures we find, run
before each release, so version four does not undo version two.

The build and the test are one job, not two. Every feature I ship arrives with the test that would catch it breaking.

If the build does not pass the acceptance tests we write together at the start, the final milestone is not released, and I
will tell you that in the first message rather than after the work.

Prefer to see the testing before you pay for a build? The red team test on my profile does exactly that.
```

## Step 6. Consultation listing (2 minutes)

Two changes. Price at $85 for 45 minutes if it is currently under $50, and add one line to the end of the description:

```
If the call does not leave you with a written list you can act on this week, tell me inside 24 hours and it is refunded.
```

## Step 7. The retainer, sold at the end of the first contract rather than as a new listing (1 minute, twice)

A new catalog item has to be reviewed and approved, and a "monthly service" is the kind of thing Upwork's catalog review
pushes back on. The retainer does not need a listing. It needs one message, sent in the contract room on the day the first
report is accepted:

```
The report is delivered and I have nothing outstanding on my side.

Two things. If it did what you needed, closing the contract as job completed successfully helps me more than anything
else you could do here.

The second thing is the one nobody does and everybody needs. Prompt edits and model upgrades bring findings back and
create new ones, and you cannot see that from inside a release checklist. I run the same four-layer test once a month on
the current revision and send the delta: what is new, what came back, what is closed. Three months, $600, as a separate
contract so your first one closes clean. Tell me the date you want the first run and I will send it.
```

That is the whole back end: same work, no new customer, no connect, no proposal.

## Step 8. The checklist mechanic on the next post (1 minute, then hand made)

In the **first comment** of the next post, never the body:

```
I have the 168-class checklist as a one page PDF, filled in for your system if you tell me what it does. Comment "checklist" or message me and I will send it.
```

Then four touches, by hand, per person:

| Day | Message |
|---|---|
| 0 | the PDF, plus one line: "the page that comes back empty most often is permission drift" |
| 3 | one finding from a real test, no ask |
| 7 | "the page for your setup is missing [class]. worth a look before you ship." |
| 12 | "if you want it done properly, the three day scan is $150 and the link is on my profile" |

## Step 9. Close the loop (2 minutes on 27 November)

Read four numbers only: catalog views, DMs received, proposals sent, closed contracts. If views rise and DMs do not, the
first line of the description is wrong. If DMs rise and closes do not, the guarantee or the price is wrong. Change that
one thing, not everything.

## If a field refuses the text

The tier descriptions are hard limited at 80 characters and the paste above fits. If the long description field will not
take the whole block, cut the paragraph starting "One thing I will not guarantee", because the same sentence is already in
the FAQ, and the guarantee survives in two places without it.
