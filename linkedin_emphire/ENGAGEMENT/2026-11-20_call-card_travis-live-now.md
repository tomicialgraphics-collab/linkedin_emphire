---
deliverable: internal
id: 2026-11-20_call-card_travis-live-now
date: 2026-11-20
audience: internal
status: ready
title: Call card, Travis Miragliotta, twenty minutes, three parts
sources_read: >-
  read: the demo run sheet of 18 November, the run record of 14 November, and the thread. No page opened.
---

# Travis, live. Twenty minutes.

He has been waiting since 00:16 and he is in the room. Join, say hello, share one terminal at 20pt or bigger, and keep this open on the other screen.

## 0:00 to 0:40, frame it

"I've got twenty minutes and three parts: five showing you a verifier that could not fail, ten on what that means for a number you have to defend to somebody who didn't build it, five on where it breaks in your work. Stop me whenever."

Then ask, before typing: "Whose number are we using in the middle, a client's or your own?"

## 0:40 to 5:00, the failure, live

```
cd CLIENTS/redteam-five-tests/2026-11-14_run-record-fix-v2
sed -n 24,29p 04-prefix-collision.log
sed -n 67,69p 04-prefix-collision.log
```

On screen the digest is sixteen characters where the true one is sixty-four, and the suite says 50 passed, 0 failed.

Say: "That number on the right is the whole suite agreeing with a check that compared a quarter of the hash."

Then the same input, fixed:

```
sed -n 212,215p 04-prefix-collision.log
sed -n 257,260p 04-prefix-collision.log
```

53 passed, 1 failed, same input, same machine, one row.

## 5:00 to 6:00, the one that looks wrong

```
python3 03-verify_run_record.py --self-test
```

It prints a failure in about a tenth of a second and exits zero. Say plainly: "This is designed to fail. A check that cannot fail isn't a check, so the self-test fails on purpose and passes only when it does. If someone puts the short comparison back, this turns red."

Then the limit, in one sentence: "It proves the objects in the manifest are the objects on disk at the commit named. It can't tell you whether a run should have happened at all, and it doesn't claim to."

## 6:00 to 16:00, his number

Three questions, and let him talk.

"What number do you put in front of someone else that has to survive being re-run?"
"Who re-runs it, and what do they need in order to?"
"What would have to change for you to distrust it?"

Then the only claim you need: "Every number I hand over ships with the command that reproduces it and one line saying what it can't see. That's not rigour, it's the cheapest way to be believed twice."

## 16:00 to 20:00, where it breaks in his work

Ask, do not tell: "Where does the evidence give way before the model does, in what you're doing now?"

His likely answer is that the number is fine but nobody can reproduce it, or that the model was right and the data was stale. Both lead to the same place: the artefact is the claim.

Close: "I'll send you the run record and the command. If you want to try it on one of your numbers, that's an hour of work and I'll do the first one free so you can see whether it holds."

## If it goes wrong

Do not debug on screen. Open the log ranges and say the live run carries the same evidence. If he asks for the fifty-four check run against a live checkout, say the checkout isn't in this room and offer it as a follow-up.

## Do not

Do not pitch the vault, the product, or the red-team retainer. Do not name a price. Do not claim a client. Do not let it run past twenty-five minutes.

## After

Within the hour: the run record, the command, and the limit line in one short message. Nothing else.
