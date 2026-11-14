---
deliverable: email
id: 2026-11-14_email_aithos-status-bump
date: 2026-11-14
time_checked: >-
  checked: 2026-11-14 23:08 WAT, read from the system clock in the sandbox before this file was sent for gate.
audience: outbound
status: ready
approved: no
warm: yes
profile_checked: "Aithos Research Foundation, Amsterdam, a Dutch ANBI. The published contact page lists nadia@aithos.org for general inquiries and collaborations, daan@aithos.org for research partnerships, and info@aithos.org as the start of a conversation. It does not list hiring@aithos.org anywhere. The vacancy page, read today, is struck through and marked closed, and its application line reads 'email your resume and a brief motivation letter to by 31 October' with no address in it at all."
premise_checked: >-
  checked: the vacancy page was fetched and read at 23:05 WAT on 14 November. It says applications closed on 31 October, that the team would review in the first week of November, and that shortlisted candidates would get a 30 minute screen, a three hour take-home and a 60 minute technical. The page is now headed 'Open Vacancy: Research Engineer (closed)'. Five working days have passed since the end of the advertised review week.
sources_read: >-
  read: aithos.org/vacancies/research-engineer/ (closed, process and dates above), aithos.org/contact/ (the three addresses), the LinkedIn posts by their own team inviting questions on the role. The connected Gmail is tomicialgraphics@gmail.com and holds nothing from aithos.org in any folder including spam, but the application went from olusanyatimothy54@gmail.com, so that mailbox cannot confirm or deny receipt.
---

## The email

**To:** info@aithos.org
**Subject:** Follow-up, Application, Research Engineer, Olusanya Timothy (31 Oct)
**Attach:** `RESUME/Timothy_Olusanya_Aithos_Research_Engineer.pdf`

<!-- gate:body:start -->
Hello,

I applied for the Research Engineer role on 31 October under the subject "Application, Research Engineer, Olusanya Timothy". The vacancy page has since closed and I have heard nothing either way, so this is a status question and not a chase.

One practical detail. The application line on that page had no address in it when I read it, so I sent to hiring@aithos.org. If that inbox is not one you monitor, this is the first copy you have received, and the resume is attached again.

One thing has changed since I applied. I found a verifier of mine comparing the first sixteen characters of every SHA-256 instead of all sixty-four, so a forged manifest passed all fifty checks. It now fails unless it can prove it rejects a digest that matches on a prefix. That is the failure your role description is written against, a number that traces back to nothing.

Either answer helps: whether my application was among those reviewed in the first week of November, and whether the role is filled.

Olusanya Timothy
olusanyatimothy54@gmail.com · +234 812 786 8211
<!-- gate:body:end -->

## What the repo held, and what was wrong with it

**What it held.** `APPLICATIONS/2026-10-31_aithos_research-engineer_send-package/` (letter 527 words, `.eml` built and round-trip verified, resume PDF, `build_eml.py`) and `SENT.md`, which records the send as 31 October to hiring@aithos.org from olusanyatimothy54@gmail.com, and states the rule: one bump only, 14 November, short, warm, referencing the original subject.

**What was blank.** Every row of the reply tracker after "Application sent": auto-acknowledgement, human reply, screen proposed, screen held, take-home, technical round, outcome. The time sent is also a blank, and the checklist of which variant of the letter actually went out was never ticked. So the record establishes that something was sent and not one fact about what came back.

**What the record did not know.** The vacancy is closed, and the address the application went to does not appear on Aithos's own contact page. Those two facts were not in the repo, because nobody had opened the page again since 31 October.

## Why info@ and not hiring@ again

The bump is one message. Sent to hiring@aithos.org it repeats the send that has already produced eleven days of silence from an address nobody can point to on the site. Sent to info@aithos.org it arrives where the site says a conversation starts, it is forwardable to whoever runs hiring, and it carries the information that makes the original loss plausible. It also asks a question that has a factual answer, which is the kind of email a small foundation answers.

**Not dania@ or daan@ directly.** Daan Henselmans is the Research Director and the right person substantively, but a first contact to a director about a closed round reads as bypassing a process. If info@ answers with nothing useful, that address is the escalation, and it is one message, not two.

## If they answer closed

Take the answer and ask for the next opening in the same sentence. The 16-of-64 material is the strongest thing to leave behind either way, and the Playbook link belongs in a follow-up only if they ask what else you have built. Do not offer the take-home unsolicited a second time; the letter already did.
