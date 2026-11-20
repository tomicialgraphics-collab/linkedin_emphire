---
deliverable: comment
id: 2026-11-17_comment_tanya-janca_who-held-the-authority
date: 2026-11-17
audience: public
status: ready
approved: no
warm: yes
surface: >-
  Comment under Tanya Janca's post asking who is responsible when an agent reaches someone else's systems without
  authorisation. She names four candidates, the developer, the deploying organisation, the model provider and whoever
  gave the agent its tools, then adds the harder version of the question, that nobody instructed it to do anything wrong.
time_checked: >-
  checked: 2026-11-17 20:00 WAT, read from the system clock before this file was written. Her post was thirty-seven
  minutes old when it arrived here.
profile_checked: >-
  Tanya Janca, secure coding trainer, author and founder, known for AppSec teaching that hands people something they
  can apply on Monday. Her post ends where the engineering begins, so the comment answers the engineering half and
  leaves the legal half alone, which is also the only half I can answer honestly.
premise_checked: >-
  checked: no statute, regulator or case is cited, because none was read today and liability differs by jurisdiction.
  Every claim here is about records and grants inside a system, which is checkable by anyone who has built one. The
  sentence about developers not needing to be lawyers is her own framing, quoted back, and not a legal position.
sources_read: >-
  read: her post in full. Her linked video was not opened, so nothing here describes its contents.
---

## Comment, paste as is

<!-- gate:body:start -->
You're right that developers shouldn't have to become lawyers. The way to keep them out of the argument is to make the record do the arguing.

All four of those parties are answerable in principle. What most agent systems can't do is produce the record that tells you which one applies, and that's an engineering question before it's a legal one.

A log will tell you a credential was used. It rarely tells you whose authority stood behind it, when that authority was granted, or what it was scoped to. Without those three, an investigation is a reconstruction of intent from timestamps, and the answer ends up decided by argument rather than evidence.

On the case where nobody instructed it: there's still a grantor. Nobody hands an agent a set of tools without a person deciding it may reach those systems. So the nearest answerable party is whoever widened the authority, and if the organisation can't name that person, the absence is the finding.

The engineering fix is dull. Record the principal at grant time with the scope and the expiry, and the investigation becomes a lookup.
<!-- gate:body:end -->

## Why it refuses the legal half

Her four candidates are all legal answers, and any of them would be wrong to assert from here without a jurisdiction and a case. The technical answer is the one that changes the outcome, because whichever party ends up answerable still has to prove what happened, and the record is what settles that.

The move is to convert the question from who should be liable to what the system can show about who authorised what. That is a question about software, and it has an answer tonight.

## Why the no-instruction case gets an answer

It reads like the unanswerable version, and it isn't. Authority never appears without somebody granting it, so the trail has a grantor even when the instruction was never written down. Naming that is harder than naming the developer, and it's the honest answer.

The last clause matters most for her audience: where the organisation cannot identify the grantor, that gap is itself a finding, and it is the kind a reviewer writes down.

## Why the fix is stated as dull

Secure coding audiences are tired of being sold frameworks. The fix here is a field in a record and a discipline about writing it, which is the sort of thing her readers can put in a pull request this week. Calling it dull is the point, because dull is what survives a code review.
