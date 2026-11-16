---
deliverable: comment
id: 2026-11-16_comment_anthony-alcaraz_the-window-you-do-not-control
date: 2026-11-16
audience: public
status: ready
approved: no
warm: no
time_checked: >-
  checked: 2026-11-16 10:13 WAT, read from the system clock before this file was written.
profile_checked: >-
  Anthony Alcaraz, followed, agentic engineering lead at AWS and an O'Reilly author, writing a technical argument with
  five footnotes rather than a general-audience piece. The post is eight minutes old at the time of the paste. The
  register is set by that: the comment argues with the architecture, in his terms, and does not restate the post.
thread: >-
  always-on agents acting between messages, built from an event inbox, timers, memory files, permissions and an outbox.
  The inbox dedupes on the source event ID and runs one worker at a time, but the design is silent on actions a dead
  worker already took. His fix is to key the action with the event ID of the approval, on the grounds that a reused
  Stripe idempotency key returns the saved first response, and to put a durable execution engine under every action.
premise_checked: >-
  checked: the 24-hour figure is his own, stated in his closing line as the window in which a retry gets back the first
  refund rather than making a second. The comment builds on that number as he states it and does not assert anything
  about Stripe behaviour beyond it, nor about Stripe's internals. The second failure mode is argued from his own
  evidence, not from a source the comment introduces.
sources_read: >-
  blocked: no page was opened and none of the five footnotes was followed. The comment stands entirely on the text he
  published, which is detailed enough to argue with.
---

## Comment, paste as is

One gap here: the idempotency guarantee is time-bounded and the agent's sleep isn't.

A key the service forgets after 24 hours covers a retry on the same day. Wake the timer on day three, let the worker die at the wrong moment, and the retry presents a key nobody recognises. Nothing in the five-part design sees it, because the dedupe happened in a table that still holds the event and a service that no longer holds the key.

So the durable record has to be the agent's rather than the provider's. Write the intent and the key before the call, write the outcome after it, and let a retry consult its own journal before it asks Stripe. That takes the load off a window you don't control.

The failure I'd worry about more than the double refund is the acknowledged one that never happened. The call returns, the record of it doesn't land, and the agent now believes the customer was paid. Nothing retries, because nothing says a retry is needed, and the log reads as success for as long as anybody cares to check.

Idempotency makes a repeat safe. It says nothing about whether the original call ever landed.

## Why the time gap and not the dedupe

The inbox design in the post is sound and the idempotency key is the right instrument, so repeating either would add nothing. What both share is an assumption the post's own architecture breaks: that the record of a decision is available when the retry happens.

His closing line states the window honestly, within 24 hours. An always-on agent is defined by sleeping longer than that. The two facts are in the same paragraph and they don't quite meet.

## The failure that costs more

A double refund is a visible error with an angry customer and a refund to reverse. The acknowledged action that never happened is invisible: the customer is silent because nothing arrived, the log says done, and the discovery happens at the month end or never.

That asymmetry is the reason to keep the write-ahead record on the agent's side. It is also the reason the journal itself has to be able to say it does not know, rather than defaulting to the answer that reads as success, which is a separate defect and a common one.

## What this is not

No link, no offer and no mention of the owner's work. He is an author and an architect in the same field, and the only currency in that thread is a sharper argument.

Not a correction of his five-part design, which is offered as one to build. The comment adds the record it assumes.

## If he replies

The question worth having is whether he would put the write-ahead record in the inbox table or beside it, because that decides whether the retry path has one source of truth or two that can disagree. That is his architecture to answer, and an honest answer would be useful to him.
