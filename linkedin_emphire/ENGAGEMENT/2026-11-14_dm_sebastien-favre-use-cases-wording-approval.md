---
deliverable: dm
id: 2026-11-14_dm_sebastien-favre-use-cases-wording-approval
date: 2026-11-14
time_checked: >-
  checked: 2026-11-14 19:12 WAT, read from the system clock in the sandbox before this file was sent for gate.
audience: vendor
status: ready
approved: no
warm: yes
profile_checked: >-
  Sébastien Favre publishes under his own name and asks for wording approval before taking the pending
  markers off. He has now answered two sets of proposed text in one evening and changed both where asked,
  so the reply can be a line edit rather than a negotiation. He is the one who will be asked to defend
  the page later, which is why the limits section matters more than the credit section.
premise_checked: >-
  checked: the Use Cases page was opened and read, not taken on description. The section is headed
  Independent Evidence Reviews, the entry is titled Conformance corpus and CLI verification contract and
  marked proposed, and the text credits the dependency-diagnostics finding, keeps the strict-mode
  discovery with NeoMundi's release notes, distinguishes the exit-code question from a defect fix, records
  the rerun as being on release 1.3.0 rather than on a branch, and states that the Rust toolchain was not
  exercised. The three points asked for on 14 November are present. The commit history shows the entry
  arrived through a pull request titled as a proposal for approval, which matches what he says.
sources_read: >-
  read: the Independent Evidence Reviews section of the public use-cases repository and its commit list,
  on 14 November 2026. Not read: the private engine repository, so the merge commit quoted in the entry is
  his reference and not one I have verified.
---

## DM, paste this

<!-- gate:body:start -->
I read it this time, which I couldn't do with the pull request, so this is a review rather than a thank you.

The paragraph is accurate, and it's accurate in the places where accuracy costs something. "Incomplete verification and failed verification are distinct states" followed by "not a defect fix attributed to the reviewer" is the right call: it credits the question and refuses the claim. "The strict-mode coverage gap was already recorded in NeoMundi release notes. Timothy located it in those notes and relayed the flag" is the sentence I asked for, and the note that I didn't exercise the Rust toolchain is the caveat I'd have added myself.

Three edits before you take the pending markers off.

One, my name. This page says Olusanya Timothy and the recommendation says Timothy Olusanya. My profile displays the first, so make the two public pages agree, whichever you settle on.

Two, keep the dependency finding specific. "Misleading dependency diagnostics" is fair, and the clause after it already says the useful part: an optional dependency absent from the environment reported as a regression rather than a missing prerequisite. That clause is the finding. Don't let a later edit shorten it away.

Three, when you drop the pending markers, leave the limits exactly as written. "Does not imply that Timothy closed, validated, certified or signed off on the corpus, or endorsed NeoMundi" is the sentence that makes the rest of the entry safe to publish, and it's the one I'd check first if I were a reader.

That's approval on those three. I'll cite the page as a description of the review, not as an endorsement, and anyone who asks me for evidence gets the open items.

One thing I can't verify and won't pretend to: the merge commit quoted in the entry. The engine repository is private to you, so that reference is yours. It reads as precise, which is the right instinct, and it's the kind of precise that only you can check.

Thank you for building the page rather than just saying you would.
<!-- gate:body:end -->
