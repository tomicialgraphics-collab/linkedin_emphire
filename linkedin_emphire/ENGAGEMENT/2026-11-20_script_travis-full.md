---
deliverable: internal
id: 2026-11-20_script_travis-full
date: 2026-11-20
audience: internal
status: ready
title: Full call script, Travis Miragliotta, twenty minutes, everything spoken
sources_read: >-
  read: the demo run sheet, 04-prefix-collision.log, and the thread with Travis as pasted. No page opened.
---

# The whole call, in words you can read off

The log is on Drive and the repo is not on this laptop, so the demo is the file, not the terminal. If he asks why, one sentence and move on.

Log: https://drive.google.com/file/d/1m9vdIT2qLAXuDyftNfTuF7RKhrkI80gX/view

## 0:00 to 0:30. Frame

"Travis, thanks for staying with this. Twenty minutes, three parts. Five on a verifier that passed fifty checks and could never fail. Ten on what that means for a number you have to defend to somebody who didn't build it. Five on where it breaks in your work. Stop me whenever."

## 0:30 to 1:00. The honesty line, said once

"I was going to run this live and the tools for it aren't on this machine, so I'm showing you the log instead. Same file I'd have run. If you want the live version, I'll do it on my box another day and you can watch it fail in real time."

## 1:00 to 5:00. The evidence

Open the log. Point at line 27, then line 69.

"Line 27 is a check comparing a digest. The digest it compares is sixteen characters. The real one is sixty-four. Line 69 is the suite's verdict on that: fifty passed, zero failed."

Scroll to 214 and 260.

"Same file, same case, after the fix. Line 214 is the same row, now failing, and you can see why. The value it got is the real sixty-four. What the manifest says is that value with the rest replaced by f's. Line 260 is the suite: fifty-three passed, one failed."

The two sentences to say over it:

"So the instrument was measuring a quarter of the thing and reporting full agreement. Nobody had asked it to fail, so nobody knew."

"A suite that passes everything is telling you about the author's confidence, not about the coverage of the instrument."

## 5:00 to 6:00. The limit

"And this is what the tool is not, because it matters more than what it is. It proves the objects named in the manifest are the objects on disk at the commit named, and that the record and the package are bound to each other. It cannot tell you whether a run should have been performed at all. It doesn't claim to."

"Which is the difference between a tool you can rely on and a tool you have to trust."

## 6:00 to 16:00. His number, ten minutes

Ask one, then shut up. He will fill the space.

"What number do you put in front of someone else that has to survive being re-run?"

Follow-ups, in this order:
"Who re-runs it?"
"What do they need in order to?"
"What would have to change for you to stop believing it?"

Then, once, and only once:

"Every number I hand over ships with the command that reproduces it and one line saying what it can't see. That's not rigour. It's the cheapest way to be believed twice."

If he describes a dashboard or a model, the question is: "and when the number moves, what tells the reader whether the model changed or the data did?"

## 16:00 to 19:00. Where it breaks for him

Ask, don't tell.

"Where does the evidence give way before the model does, in what you're doing now?"

Then reflect one line back, no more:

"So the instrument is fine and the record of what it saw is the weak part."

## 19:00 to 20:00. Close and the ask

"I'll send you the log and the command within the hour. If you want, bring me one number you have to defend and I'll do the first one free, so you can watch whether it holds under a re-run."

"And the thing I still want to know, because it changes nothing about today but everything about what I'd prepare: is that a client's number or one of yours?"

## If he asks these

"How do I know you're not just good at slides?" You don't yet. That's why the first one is free and it's a file you keep, not a meeting you attend.

"What does this cost?" The first one is free. After that it's a fixed fee per number, and I'd rather quote it after I've seen yours than before.

"Can you do this for our whole pipeline?" Probably not yet, and I'd rather tell you that now than in six weeks.

"Are you looking for a job?" No. I'm looking for one or two people whose numbers have to hold up.

## Do not

Do not apologise twice for the terminal. Do not demo anything else. Do not mention the vault, the land product, Marvin, or any price beyond "fixed fee per number". Do not promise a timeline. Do not run past twenty-five minutes.

## After, within the hour

Send the log link, the two line numbers, the limit sentence, and one question: which number he'd like tested first. Nothing else.
