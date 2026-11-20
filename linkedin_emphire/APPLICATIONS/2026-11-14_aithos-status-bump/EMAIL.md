---
deliverable: email
id: 2026-11-14_email_aithos-status-bump
date: 2026-11-14
time_checked: >-
  checked: 2026-11-14 23:15 WAT, read from the system clock in the sandbox before this file was sent for gate.
audience: outbound
status: ready
approved: no
warm: yes
supersedes: >-
  the 23:08 version of this file, which was written from the repo alone and addressed info@aithos.org on the
  assumption that nothing had ever come back. The thread pasted at 23:12 shows an acknowledgement inside 26 hours,
  from a named person, so that premise was wrong and that draft must not be sent.
profile_checked: "Sicco Pier van Gosliga, sicco@aithos.org, is the person who acknowledged the application on 15 October and signs as the Aithos hiring team. He is on the research side of a two-person research team in Amsterdam and is the contact the role was advertised under. He is named in the thread, so the bump replies to him rather than opening a new conversation."
premise_checked: >-
  checked: the thread, pasted in full. Applied Wednesday 14 October at 09:06 WAT. Acknowledged Thursday 15 October
  at 12:08 by Sicco, confirming the CV and motivation letter arrived and that the team would review in the first
  week of November and then reach out with next steps. Owner replied Friday 16 October at 04:51. Nothing since.
  The review week (2 to 8 November) ended four working days before 14 November.
sources_read: >-
  read: the pasted thread (three messages, verbatim dates), aithos.org/vacancies/research-engineer/ (closed to new
  applications, same three-stage process, review week first week of November), aithos.org/contact/. The attached
  resume as sent is 73,004 bytes, `6c3b5e38624d`; the copy in RESUME is a different build at 29,814 bytes,
  `1bc812d1de8b`, so the file in the repo is not the file that went out.
---

## The email

**Reply in the existing thread.** To `sicco@aithos.org`, subject unchanged: "Application, Research Engineer, Olusanya Timothy". Attach nothing.

<!-- gate:body:start -->
Sicco,

Following up on your confirmation of 15 October, where you said the team would reach out once the first week of November review was done. I am asking where things stand, not for a decision, and two lines would be enough.

One thing has changed since my letter, and it is the kind of thing the role is about. A verifier of mine was comparing the first sixteen characters of every SHA-256 instead of all sixty-four, so a forged manifest passed all fifty checks while the suite stayed green. It now fails unless it can prove it rejects a digest that matches on a prefix.

Either way, thank you for the consideration.

Olusanya Timothy
<!-- gate:body:end -->

## Correcting the record, because the repo had it wrong

Four things were recorded wrongly, and each one changes the next move.

**The date.** `SENT.md` says the application went out on 31 October, "before the deadline". It went out on **14 October at 09:06**, seventeen days earlier than recorded. A seventeen-day error in a two-week follow-up rule is the whole rule.

**The acknowledgement.** The reply tracker has "Auto-acknowledgement received" blank and "Human reply" blank. There was a **human acknowledgement in twenty-six hours**, from Sicco, confirming both documents arrived and naming the review window. Silence since then is four working days past a date they set, not eleven days of nothing.

**The address.** The 23:08 draft argued that `hiring@aithos.org` might be an inbox nobody reads, because it is printed nowhere on their site. The thread settles it: it reached the team, and a named person answered from it. Sending to `info@` would have told them that their own confirmation email did not exist.

**The letter.** `letter.txt` is not the text that was sent. The sent version carries different sentences around the harness and the principles paragraph. `SENT.md` asks for the sent text to be pasted at the bottom when the two differ, and it never was.

## Why this bump, in this shape

**It replies, so it does not restart anything.** Same thread, same subject, no attachment. He can read it in five seconds and answer in one.

**It quotes his own commitment.** "Once the first week of November review was done" is his sentence, not an accusation, so the question of lateness never arises.

**It asks for status, not for a decision.** A busy person can answer "still with the panel" without pre-empting an outcome. Asking for a decision invites a no.

**The one new thing is the point of the message.** A verifier that compared sixteen characters of a sixty-four character digest is exactly the failure the role description is written against, and saying it about his own tool is the cheapest possible demonstration of the scientific mindset the listing asks for. It is also the only reason a hiring team re-reads an application it has already read.

## If nothing comes back

One message, and this is it. If there is no answer by **21 November**, the round is over and the next contact is a fresh application when they post the next research engineer role, not another message to this thread.
