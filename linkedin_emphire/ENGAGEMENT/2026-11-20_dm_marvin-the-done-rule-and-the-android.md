---
deliverable: dm
id: 2026-11-20_dm_marvin-the-done-rule-and-the-android
date: 2026-11-20
audience: outbound
status: ready
approved: no
recipient: Marvin Percival
premise: >-
  Marvin chose the second reading of the phone gate at 4:51 PM, supplied the exact wording, asked for it on a docs branch
  tonight, and asked whether the owner has an Android phone to test on. This reply accepts his wording unchanged, offers
  one optional sentence that names why the fallback is safe, and answers the device question with the one part the owner
  has to supply.
time_checked: >-
  checked: 2026-11-20 16:54 WAT, read from the system clock before this file was written. His message is stamped 4:51 PM
  in the thread as pasted.
profile_checked: >-
  Marvin Percival, who answered a blocking question within the hour and wrote the replacement himself, which means the
  reply should use his sentences rather than improve them. He has also taken the iPhone side, so the Android question is
  about coverage, not about commitment.
premise_checked: >-
  checked: his two sentences are quoted from his message of 4:51 PM. The claim about the approval rule is read from the
  instructions file, which already requires a second person to merge every pull request. The observation about emulators is
  an opinion about testing, labelled as one, and the answer on whether an Android handset exists is left to the owner
  because it is a fact only he knows.
sources_read: >-
  read: CLAUDE.md of DUNIN7/eri-test as pasted at 16:42 on 20 November. No page opened.
---

## Message, paste as is, after choosing the Android answer

<!-- gate:body:start -->
The second one, and your wording is better than mine because it names the features rather than the screens. It goes in as a docs branch now and the pull request will be waiting for you.

One sentence I would add under it, and strike it if you disagree: that the second sentence only holds because every pull request needs the other person's approval. Without that rule, done when the tests pass lets one person write a test, watch it pass and call the requirement finished, which is the exact failure this product is about.

On the Android: [I have one and can test on it / I do not have one yet, so tell me how you want to handle it].

I would not count an emulator as a phone for that rule. The camera, the location and the install behave differently on one, and those are the parts of this app most likely to break.
<!-- gate:body:end -->
