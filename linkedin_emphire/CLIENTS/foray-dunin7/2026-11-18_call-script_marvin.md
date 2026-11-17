---
deliverable: doc
id: 2026-11-18_call-foray-marvin
date: 2026-11-18
audience: internal
status: ready
approved: no
client: FORAY (Dunin7)
time_checked: >-
  checked: 2026-11-17 23:44 WAT, read from the system clock before this file was written. The call is 18 November at
  14:00 WAT, which is 08:00 on the US east coast, and both times are checked against that reading.
premise_checked: >-
  checked: every figure below is taken from this client's own record in this workspace, not from memory. The three
  anchor times, the register revision and its hash, the verifier versions, the 66 of 66 suite run and the 91 against
  121 vector discrepancy are all in the version 5 case study and the register addendum. Nothing about his systems is
  asserted beyond what those documents state.
sources_read: >-
  read: the version 5 case study, the register addendum v8, replies 9, 10, 14, 17 and 18, and the state notes for this
  client. No external page was opened, so nothing here depends on a source outside his own record.
---

# Call script, Marvin Percival, 18 November 2026

14:00 WAT, 08:00 his time. Fifty minutes of substance, five of buffer. No slides, nothing for him to prepare, and
nothing sent to him beforehand.

## Before the hour, five minutes of preparation at my end

- Open the register at revision 7, `b9af6973`, and read the status lines for W-04 and W-01h. **The script assumes
  both are open. If W-01h has closed since 6 November, drop it and give W-04 the whole segment.**
- Open version 5 of the case study, so a quote can be read from the page rather than recalled.
- Have the three anchor times in front of me: 10 November 12:20:15 and 15:17:42 UTC, 12 November 16:28:25 UTC.

## 0:00 to 2:00, open

Thanks for the hour, and for reading the correction as the small thing it was.

The shape, in one breath: two items still open on the register, then what version 5 changed and what it deliberately
did not, then the question I actually want his view on. Nothing to prepare.

Then stop talking and let him set the temperature. He asked for a chat, so the first two minutes belong to him.

## 2:00 to 12:00, the two open items

Say the frame first: every numbered item closed in code or in text, and two are open in the only sense that matters,
which is that neither was closed by a test in his record.

**W-04, the mapping.** The rule that maps my probe onto the new vector family is in the specification. What is not
in the record is a re-run of the probe against it, so the closure is textual: the rule exists, and the test of the
rule is outstanding in the record rather than settled by it. That distinction is his, stated in his record before I
asked for it, and I am keeping it rather than tidying it away.

Ask him, and mean it: whether he wants the probe re-run or whether the textual closure is enough for his purposes.
Both are legitimate answers. One of them is a piece of work and the other one is a sentence in the register.

**W-01h, the sentinel.** The repository-anchored sentinel is read and never run: the branch that would exercise it
does not execute on any packet the suite produces. So the item records a path that exists and has never been taken,
which is the same shape as the finding that started this review.

Do not score it. Say what it would take to close it, which is one packet built for the purpose, and leave the
decision with him.

Keep this segment to ten minutes even if he wants to expand it. The third segment is the reason for the call.

## 12:00 to 22:00, version 5, and what it refused to do

**What changed:** the title, five weeks to ten days, and nothing else. His first message was 3 November at 12:08;
the post went up on 13 November. The same sentence in the post was corrected the same day. Version 4 stays exactly
as he cleared it, and version 5 opens with a short section saying what changed and why.

**What it deliberately did not do,** and this is the part worth the minutes:

- No edit in place, even though an edit would have been invisible and cheaper.
- No change to a finding, a count, a hash, or the section where I was wrong first. That section stays where he put
  it, at his instruction.
- No promotion of the two recorded limits into passing items. The anchored extent still proves order and not
  content, and the reachable path is still covered by vectors rather than by an anchor.
- No claim that the review established anything after 12 November. The three anchors were found by the project, and
  the page says so.

The one sentence to say out loud: a document that hides its own revisions is the failure this page describes, so
the correction had to be visible even though visible costs more.

## 22:00 to 45:00, the question

Frame it as a design question and hand it to him without a recommendation attached, because his answer is the point
of the hour.

A defect register has a natural life while the protocol is moving. Every item is either open or closed against a
revision, and the register is doing work the whole time. Once the protocol stops moving, the register has three
possible futures and they cost different things.

- **Freeze it.** Version it, hash it, publish it as a historical record. Cheap, honest, and it keeps the case study
  standing on something checkable.
- **Turn it into a conformance suite.** Every closed item becomes a check a future revision can be run against, so
  the register stops being my document about his work and becomes a regression net his own team runs. This is the
  expensive one and the only one that keeps paying after I am gone.
- **Keep it live.** Re-run against each new revision and report deltas. That is a standing arrangement, and it only
  works if there is an owner who will accept findings, which is a different question from whether there is a
  budget.

Then the question I actually want answered: which of those does a protocol that has stopped moving need, given that
the person who wrote the specification is also the person who would be audited by it.

Shut up and take notes. Do not fill the silence, and do not argue for the conformance suite even if it is the one I
would pick.

## 45:00 to 52:00, close

Say what goes in writing and when: a one-page note recording the two rulings, whatever they are, and nothing else.

Ask one closing question, which is the useful one for any future work between us: in six months, what would he want
the register to have been for.

## 52:00 to 57:00, buffer

His questions. If he asks what the W-04 re-run would take, the answer is one sentence: a week, a fixed fee, a
written result with the probe and its logs attached, and one revision included. The number goes in writing after
the call, not on it.

## Five things not to do

- Do not say five weeks. It was ten days and he corrected it himself.
- Do not say he has not re-run the probe. Say his record does not show a re-run, which is what the record says and
  is the wording his own document uses.
- Do not re-send the case study. He has read it twice and corrected it twice.
- Do not soften W-01h into a suggestion. It is an item on a register and it either closes or it does not.
- Do not raise the price beyond that one sentence, and do not put it in the note afterwards unless he asked what it
  would take.

## If the conversation goes somewhere else

**If he opens with the dataset:** one line, already agreed: it is not his content, I answered it as though it were,
the findings stand and the aim was wrong, and it is closed.

**If he asks what the review was worth:** the honest answer is that it made a claim reachable rather than
withdrawn, and the record that proves it now exists rather than being promised. Nothing about fees.

**If he offers an introduction:** take it, ask what the person is working on, and do not pitch. The next step after
an introduction is a message, not a deck.
