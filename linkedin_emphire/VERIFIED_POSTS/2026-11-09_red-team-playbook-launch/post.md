---
deliverable: post
id: 2026-11-09_red-team-playbook-launch
date: 2026-11-09
audience: public
status: ready
approved: no
template: T11
headline: The number nobody prints
subheadline: 168 testable classes, and a tool that counts what you did not test.
headline_alt: Every report has a page it leaves out
subheadline_alt2: The classes you skipped are the most honest line in the document.
headline_alt2: 168 classes, 142 open
subheadline_alt2: A checklist that tells on you.
box: 142 OPEN
box_alt: NOT TESTED
hashtags: [#AISecurity, #AIEvaluation, #AIRedTeam, #LLMEvaluation]
slot: 19:00 WAT, Monday 9 November 2026
first_comment: none, the post carries the link
---

I published the checklist I use for AI red teaming. 168 classes. The list is not the useful part.

Here's the problem with every red team list I have read, mine included. A list of attacks is easy to write and impossible to audit. It tells you what somebody thought of. It does not tell you what was covered, on which revision, with what result.

Three ways an engagement fails, and only one of them is finding nothing:

→ The finding cannot be reproduced. The model revision moved, the prompt was edited, nobody wrote the date.

→ The rate is meaningless. Three successes, quoted as a percentage, no denominator, one run.

→ The coverage is unstated. The report lists what was tested and stays quiet about the classes nobody opened.

So I built it backwards from those three. The checklist is a data file. Four small tools work on it, with no dependencies. One refuses a skipped class unless there is a written reason. One puts a Wilson interval on every rate, because 3 of 20 is not "15 percent", it is 5 to 36. One prints the page nobody publishes. The example engagement that ships with it comes out at 23 tested, 2 not present, 1 skipped, 142 open.

That last number is the one I would trust a report for. Anyone can list what they found. The open count says how much of the surface was never looked at, and a report that names it is arguing in good faith.

No checklist certifies an AI system as safe. The input space is language and the behaviour depends on content nobody controls. What a checklist can do is make the gaps countable, and a countable gap is one somebody can close.

It is public, CC BY for the writing and MIT for the code: github.com/Teamthy/Ai-Red-Team-Playbook.

#AISecurity #AIEvaluation #AIRedTeam #LLMEvaluation
