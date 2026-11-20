---
deliverable: post
id: 2026-11-16_repost_eva-benn_the-ticket-authorised-it
date: 2026-11-16
audience: public
status: ready
approved: no
surface: repost-with-thought, share to own feed
reposts: >-
  Eva Benn's Security Mondays episode with Aaron Stanley, posted 16 November 2026, the software-factory conversation.
headline: A software factory does not fail at the code. It fails at the ticket that authorised it.
subheadline: Commits went from 1.4 billion a month to 7.38 billion in five months, and controls sit downstream of a ticket.
box: WHO ASKED
box_alt: THE TICKET
headline_alt: >-
  The failure is in the ticket, not in the code. Every guardrail you build reads work that has already been accepted.
headline_alt2: >-
  When an agent picks up a ticket, a customer's wish and a product decision look identical. Provenance is what tells them apart.
template: T1
visual_link: https://drive.google.com/file/d/1kRYEyevlHu4BRPLFdLpgHAzMte6A0Hz3/view
hashtags: ["#AISecurity", "#AIEngineering", "#AIGovernance", "#AIEvals"]
time_checked: >-
  checked: 2026-11-16 23:08 WAT, read from the system clock before the first draft of this file.
profile_checked: >-
  Eva Benn, followed, running Security Mondays, 230K+ audience, ex-Microsoft, posts weekly with a named practitioner.
  The episode is three hours old. There is a comment of ours already under it from 22:50 tonight, and the internal
  method ladder says a repost replaces a comment on the same surface rather than stacking with it, so this is the
  owner's deliberate exception and it is recorded here as one.
premise_checked: >-
  checked: the commit figures are quoted from the episode's own introduction, not recomputed, and the burrito example
  and the line about the spec being the only human artifact are Aaron Stanley's, restated in the owner's words. Nothing
  is claimed about dbt Labs, Twilio or Eva's audience numbers.
sources_read: >-
  read: the full transcript pasted with the post, all twelve chapters. No page opened and no link followed. The one
  figure used is the pair GitHub published, as read on the recording.
---

## Post, paste this

<!-- gate:body:start -->
A software factory does not fail at the code. It fails at the ticket that authorised it.

GitHub commits went from 1.4 billion a month in April to 7.38 billion by September, and every control built for that speed sits downstream of a ticket somebody wrote.

Eva Benn's conversation with Aaron Stanley is the most useful hour I have heard on what that does to AppSec. The part I keep returning to is the burrito. A customer's wish arrives through a feedback form, becomes a ticket, and by the time an agent picks it up it is indistinguishable from a product decision. Same fields, same queue, same authority.

A sandbox, a gateway, an injected policy: none of them can tell you who was entitled to ask. They all operate on work that has already been accepted as work.

So authenticate at intake rather than at the gate. The spec is the only thing a human still writes, and its provenance is the part worth protecting.

#AISecurity #AIEngineering #AIGovernance #AIEvals

<!-- gate:body:end -->

## Why a repost of this one

Two of hers went up today and both are worth a comment, which is what they got. This is the one that carries a line usable on the owner's own feed without the reader having watched anything: the failure happens at the ticket, not the code.

It also reaches the right room. Her audience is AppSec leaders and practitioners, which is the buyer for the check-behind-the-review register, and a repost puts that frame in front of people who never open a comment thread.

## The conflict this records

The method ladder in the engagement notes says a repost replaces a comment on the same surface and never stacks with it. A comment of ours is already under this episode from 22:50, so this is a deliberate exception taken on the owner's instruction, and it is written down here so it is not later read as an oversight.

The mitigation is that the repost carries a different argument from the comment. The comment was about where authority is lost; the repost is about what a control can and cannot read, which stands alone for somebody who never sees the thread.

## The card

Rendered from the house template at 23:16 WAT, three lines: A FACTORY / FAILS AT THE / TICKET. 1080x1350, his own photograph, his name in the header and on the tag, the yellow follow pill. The renderer is `ASSETS/brand/make_card.sh`, which takes copy and never a design decision.

Uploaded to Drive: `1kRYEyevlHu4BRPLFdLpgHAzMte6A0Hz3`, md5 `8a52be39c0c2d52d76fd28cfeb59c644`, 669,236 bytes, in the 16 November post folder.

## If it lands

The reply to watch for is somebody asking what a provenance field would contain, because that is the question the post invites and the answer is where the work starts. Request class is easy. Naming the person who could authorise it is the part organisations have never had to write down.
