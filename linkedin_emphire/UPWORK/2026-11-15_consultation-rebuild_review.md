---
deliverable: doc
id: 2026-11-15_consultation-rebuild-review
date: 2026-11-15
time_checked: >-
  checked: 2026-11-15 12:04 WAT, read from the system clock before this file was written.
audience: internal
status: ready
approved: no
premise_checked: >-
  checked: the owner sent six screenshots of the consultation editor, one per step, with no question attached.
  They are the rewrite of the consultation the previous file recommended, so they are reviewed in place and the
  corrected text is supplied as paste blocks with measured counts.
sources_read: >-
  read: the six editor screenshots sent at 12:04 WAT, the services page read at 11:56 WAT, and the position
  taken in the two profile files of 2026-11-15.
---

# The consultation, three fields and one pass from done

## What is already right, and should not be undone

The draft is much better than what is live. The description opens on the outcome rather than on a biography, it names the actual failure modes, and it ends on who the call is for. The two delivery documents, time and cost estimate plus meeting summary, match what the description promises. Delivery in 2 days, minimum notice 1 day, future limit 4 weeks, and a $40 rate for 30 minutes are all reasonable. All six steps in the stepper already carry a tick, so nothing is missing, only unfinished.

Leave the price alone. Leave the documents and the delivery days alone.

## Fix 1: the character counts are inside the client's text

Every requirement and every FAQ carries its own length as literal text:

- "(101 characters)" after the first requirement
- "(142 characters)" after the second
- "(111 characters)" after the third
- the same again in the FAQ block

A client booking this call reads "Feel free to attach relevant docs, code, or diagrams. (142 characters)". It looks like a paste artefact because it is one. The counter on the first requirement also reads 118 of 250 while the label says 101, so the numbers are stale as well as visible. Strip every one of them.

## Fix 2: the three expertise chips

Live selection is Chatbot Development, Cybersecurity & Data Protection, User Testing. Two problems.

**User Testing is the wrong lane.** It puts the card in front of buyers shopping for QA and usability work, which is the population you cannot beat and do not want. Remove it.

**Chatbot Development is a build topic.** Keep it only if you want chatbot builds to keep arriving. The call is a review, so the chips should say review.

Press "Show all" and look for a security-specific topic: penetration testing, security assessment, red teaming or similar. If one exists, spend a slot on it. Add AI & Machine Learning from the visible list either way. Five slots, three used, so there is room.

While the category dropdown is open, read it properly. The live listing is called "Development & IT Consultation", which is the category name word for word, so the name is probably inherited rather than typed. If a more specific AI or cybersecurity consultation category exists, that single change renames and re-files the listing at once.

## Fix 3: the FAQ that opens the door back up

"Is this only for AI security questions ?" has a stray space before the question mark, and the answer starts "Both." to a question that invites yes or no. The wording is not the real issue. The answer volunteers "full-stack architecture, backend design (Go, Node.js, Python)" as an equal line of business, which reverses the narrowing of the last two weeks and prices it at $40. Replace the question and the answer.

Related, in the description: "backend design issues that cause outages or security incidents" invites the same thing. Cut the outages half.

## Fix 4: the availability hours are unknown and they matter more than the copy

The screenshot shows the calendar connected and the booking rules, but not the hours. Two facts to act on. Lagos is UTC+1; US Eastern is six hours behind and Pacific nine. To be bookable by a US founder, the hours that work are roughly 14:00 to 21:00 WAT, which covers the US morning and the European afternoon. If the calendar only offers Lagos office hours, an American client cannot book at all, and none of the copy above will show up as an order. Set the window, then check the connected calendar has no recurring block sitting inside it.

## Fix 5: make every edit in one pass

The services page has an Under Review tab, so an edit can put a live listing back through review, and while it sits there it is not shown to clients. Do all of the above in one sitting, then walk the stepper to the end rather than saving five small changes over a week.

## The paste blocks

Description, 651 of 1,200. It drops the outages clause, adds one proof line from your own benchmark, and ends on an action.

    I'll review your AI feature, API, or agent workflow and flag the real risks before you ship: prompt injection paths, unsafe tool-calling, agent permission gaps, and data exposure through RAG. You leave with a prioritized fix list, rough effort and cost for each item, and a clear call on whether to fix it in-house, brief a team, or bring me on. In a benchmark I built and published, 4 of 6 attack attempts broke the target agent; that is the kind of gap this call finds. Best for founders, PMs, and engineering leads shipping LLM features on a fixed timeline. Bring code, an architecture diagram, or a hostile prompt and we will work through it live.

Check the 4 of 6 against the pack before pasting. If the pack says a different number, the paste takes the pack's number.

Requirements, one per box, mandatory on the first.

    What's the main problem or decision you want to work through on this call?

74 characters.

    What's your current stack, and if AI is involved, which model provider are you using? Attach docs, code, or diagrams if you have them.

134 characters.

    What's your timeline, and what outcome do you need: a go/no-go call, a fix plan, or a second opinion?

101 characters. The em dash is gone, which also removes the one house-style break in the current draft.

FAQ, three questions and answers.

    Will I get anything in writing after the call?

    Yes. Within 2 days you get a written summary of the key points and my recommendations, plus an effort and cost estimate if we discuss follow-on work.

149 characters, and it now matches the 2 day delivery setting.

    Can we review code or an architecture diagram on the call?

    Yes. Attach it when you book and I'll read it before the call, or share your screen and we'll walk through it live.

115 characters.

    Is this only for AI security?

    Mostly, yes. It is built for teams shipping LLM features, agents, or RAG, where the failure mode is a security or reliability gap. If your issue is adjacent, say so in the booking form and I will tell you honestly whether the call is worth your money.

251 characters. The last sentence is the part that earns trust from a founder who has been sold to badly before.

Everything above is copy with a count, not advice to admire. The listing already has 3 views and no orders, so the measure of this rewrite is whether the next 30 days move that number.

Verified at 12:04 WAT on 2026-11-15.
