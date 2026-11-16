---
deliverable: post
id: 2026-11-16_unknown-state
date: 2026-11-16
time_checked: >-
  checked: 2026-11-16 07:54 WAT, read from the system clock in the sandbox before this file was sent for gate.
audience: public
status: ready
approved: no
warm: no
template: T1
first_comment: FIRST_COMMENT.md
headline: The write came back acknowledged. The number it was given was already on disk.
headline_alt: "A journal with three states is one state short."
headline_alt2: It could not look, so it said there was nothing to see.
subheadline: "The missing state is not an error. It is unknown."
box: not an error
box_alt: say you couldn't look
hashtags: "#AIEngineering #AISecurity #AIEvaluation #AIRedTeam"
visual_link: https://drive.google.com/file/d/1nT9waE6dYOYppR2nRngh56SXqFw4xgKO/view?usp=drivesdk
visual_file: Drive 1nT9waE6dYOYppR2nRngh56SXqFw4xgKO, folder 1FUGSl1zRxMNt4cdq68kappFt59IQVOKo, 1080x1350, md5 c5a00503d05a25da6f116bd41da08886, 676,303 B, public reader, checked against Drive after upload
visual_note: 1080x1350 reference layout, photograph in the header, cut-out portrait at the desk, yellow pill and name tag, name Olusanya Timothy, rendered from ASSETS/brand/make_card.sh with UNKNOWN / IS A STATE / NOT AN ERROR. Drawn by the card renderer rather than VISUAL/post_visual.py, whose carousel template prints a monogram where the photograph belongs and adds a verification badge the account does not have.
premise_checked: >-
  checked: the defect is the one reproduced on the host-failure benchmark on 15 November and fixed the same night. An
  EIO injected into the recovery read was caught by the resync as "size unchanged", the following write was
  acknowledged, and it reused a sequence number a record already held. The fix raises an unknown state on a failed
  recovery read, refuses the write, and returns durable unknown. The conflict pointing at the wrong record is the
  second, separate finding from the same review and is named in the post only as the symptom that surfaces later.
  No figure in the post is estimated and none is quoted from anyone else.
sources_read: >-
  read: the M1d pack logs in CLIENTS/hfb/2026-11-15_m1d-pack, both the failing and the passing f23 run, and the
  review that reported the case. Nothing outside the repository is quoted. No page was opened and no link sits in the
  body; the playbook link belongs in the first comment, as on every post until the repository reaches a thousand stars.
profile_checked: >-
  Nobody is named, no client is described, and no repository is identified. The subject is the author's own code and
  its own failure, which is the only authority a reader can check without trusting the author.
---

## Post, paste this

<!-- gate:body:start -->
The write came back acknowledged. The number it was given was already on disk.

A recovery read hit an I/O error. The code caught it, compared the size it could read against the size it expected, found them equal, and decided there was nothing to recover. Then it took the next write and handed it a sequence number that a record already held.

Nothing raised. The call returned success. Two records now share a number, and the first sign of it is a conflict raised later, pointing at the wrong one.

The I/O error isn't the bug. Disks do that. The bug is that the function had no way to say "I could not look", so it said "there is nothing to see". From inside the code those are one branch. From outside they are opposite claims about the same disk.

The fix is not clever. A failed recovery read raises unknown, the write gets refused, and the caller receives durable: unknown instead of a yes. Most journals carry 3 states: acknowledged, failed, never attempted. The 4th is the one that matters here. Without it, the code spends one of the other 3 on a case it cannot describe, and it does that silently.

There is no rate to quote for this. It was found once, by somebody who was looking for exactly this, and reproduced once here. A percentage built on two runs would be the same lie in a smaller font.

Every unknown your system can't express becomes a yes it can't support.

#AIEngineering #AISecurity #AIEvaluation #AIRedTeam
<!-- gate:body:end -->
