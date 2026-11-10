---
deliverable: comment
id: 2026-11-09_comment_efi-pylarinou-read-only-and-egress
date: 2026-11-09
audience: Dr. Efi Pylarinou post on Gmail consent granularity
status: ready
approved: no
warm: no
profile_checked: >-
  Dr. Efi Pylarinou, second degree, fintech influencer and keynote speaker, publishes "Agentic AI in FS" to a 40K+ list,
  founder of GrowFin. The post is an open letter to Google about OAuth consent, written from experience: she connected a
  WhatsApp agent to a Gmail account for one job, found all-or-nothing consent, and asked for a user-selectable read-only
  scope. Her closing line is the strongest in it. Martha Boeckenfeld and Michael Borrelli have already agreed with her, so
  the room is warm and agreement adds nothing.
thread: agent consent and least privilege
---

## The angle

Agree, then finish the argument she started, using her own open banking parallel rather than a new frame. In open banking,
seeing an account and moving money are separate licences. Her post covers the first column of the consent screen. The
missing second column is where the data may go once it has been read, and that is the column a prompt injection actually
needs.

Read-only on Gmail closes composing, sending and deleting. It does not touch the note, the sheet, the memory store or the
outbound API call the same agent already holds. That is the observation her readers will not have made, and it costs one
paragraph.

## Comment, paste as is

Your open banking parallel already contains the other half, and it is the half the consent screen leaves out. Viewing an account and moving money need separate licences. Here, reading mail and moving what was read out of the agent are also two permissions, and only the first one is on offer.

That matters because the injection does not need Gmail at all. It needs the agent to have some writable surface, a note, a sheet, a memory store, an outbound API call, and read-only on mail does nothing about any of them.

So the screen needs a second column: read from Gmail, write to nowhere. That is the lock. The one she is asking for is the door.

## What not to say

No agreement paragraph, because Martha and Michael have both already said it and the thread does not need a third. No
"actually" and no correction framing, since she is right about the scope and this adds a column rather than moving her point.
No vendor names, no link, and no mention of the client work.

## Why this is the strongest slot of the batch

Her list is 40 thousand financial services readers, her post is seventeen minutes old, and she has written about prompt
injection in exactly the terms that make this reply land. Second degree, so a comment is the only route, which is also the
cheapest one.
