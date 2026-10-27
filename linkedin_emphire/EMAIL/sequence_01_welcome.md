# SEQUENCE 01: welcome + value (stage 1, zero offer)
# E1 to E6, paste-ready. Per protocol R2: no Agent Gate, no price,
# no slots anywhere in this file. CTAs are reply / read / run only.
# All copy: dash-free (R3), banned-word clean (R4), motif budget
# 1 to 2 per email (R5), one idea one CTA (R6).
# P-group (R11): plain text, subject 1 to 20 chars lowercase, and
# at send time the body's first line is merged to "{first name},
# {their context}." (R14). Onboarding only; the weekly spine (W)
# is the standing send, template in the protocol.

FOOTER (R9, on every send, source line varies per contact):
  Timothy Olusanya
  AI red teaming. Breaking AI products before users do.
  Lagos, Nigeria (UTC+1)
  This note goes out because you asked for it on {source}.
  Unsubscribe: one click, gone, no hard feelings.

============================================================
E1 (T0)  SUBJECT: the receipt
Purpose: deliver the sample receipt, schedule the personal one,
open the reply line. Register: method-first (the receipt is the
proof). Motifs: receipt x3 (the subject of the email), re-run x1.
============================================================

{IF personal receipt scheduled, first line: "Your receipt is
scheduled. It lands within 48 hours, and it will be about your
agent, not a sample. While you wait, read the sample below. It is
the format."}

Here is a sample receipt. Everything I send is this shape.

RECEIPT
Date: 22 Oct 2026
Target: the PHP parser (every PHP app that parses untrusted requests)

CLAIM: the parser treats untrusted input as data. Your
validation, your framework, your auth, those are the layers that
keep untrusted input out of your logic.

RESULT: two 9.2 remote code execution bugs (CVE-2026-109618,
CVE-2026-109619), reachable while PHP is parsing the request,
before a line of your code runs. Emergency patch is out: 8.2.35,
8.3.36, 8.4.27, 8.5.12. On 8.1 or older there is no official
release at all.

METHOD: the exploit tooling is public. Attempt signals were
logged by Amazon and Cloudflare days before the patch. If you run
PHP, check the runtime version now. If it is not one of those
four, patch or move, then re-check the patch held.

HONEST LINE: no confirmed breach as of the patch. CISA has not
listed it as known-exploited. The public exploits reportedly do
not work on a default install. The window between attempted and
confirmed is the dangerous one.

The one line this teaches: your check has to reach the layer you
do not own.

If you want a receipt on your own agent, reply with one flow:
what it touches, what it does, one edge case you are not sure
about. I can run two a month, free.

{footer}

============================================================
E2 (T+3)  SUBJECT: how to read it
Purpose: make the format stick. The method line is the
differentiator. Register: method-first. Motifs: re-run x1,
claim/result x2 (the concept, not the catchphrase).
============================================================

Quick one, on the format.

Four lines. The claim is what the number says. The result is what
the re-run showed. The method is how anyone, including you, can
disagree with me using my own setup. The honest line is what the
result does not prove.

The method line is the one that matters.

A number without a method is an opinion with a decimal point.
The claim is free. Anyone can write it. The result is earned.
Someone ran it, logged the fingerprint, model, seed, temperature,
prompt version, date, and left the setup where a skeptic can pick
it up.

That is the whole difference a receipt exists to show.

Read the last two notes with that lens. The claim is the easy
part.

{footer}

============================================================
E3 (T+7)  SUBJECT: a number
Purpose: the live teardown. Source: the owner's own D2 group post
(490 unauthenticated public MCP servers, posted, "MCP is a good
protocol. The protocol is not the threat. The unauthenticated
default is."). Public, verified, no consent gate. Register:
method-first with a consequence line at the end. Motifs: re-run
x2.
============================================================

This week's number.

CLAIM: MCP servers are authenticated by default. The protocol
ships auth, so the deployments are auth'd.

RESULT: a scan of the public MCP ecosystem found roughly 490
public servers with no authentication at all. The protocol is not
the threat. The unauthenticated default is.

METHOD: the scan is logged, and the source is in the comments of
the post this came from. Run it any time. Auth posture changes,
and a second scan will differ.

HONEST LINE: no confirmed breach in the set. A scan is a snapshot
of the public surface, not a statement about the private one.

Why it matters this week: an agent with no auth in front of it is
not a demo. It is an endpoint. And endpoints get found.

If there is a number you are quietly afraid of, reply with it. I
will tell you if it is re-runnable, and if I can get to it this
month.

{footer}

============================================================
E4 (T+14)  SUBJECT: run this
Purpose: the DIY path. The five-tests repo, public, built to be
run by the owner of the agent. Register: method-first. Motifs:
re-run x1, receipt x1.
============================================================

One idea this week, and it is yours to do, not mine.

The five tests are public. They are the same five I run on a paid
engagement, built to be run by the person who owns the agent, not
just by me. github.com/Teamthy/ai-redteam-five-tests. The report
template is inside, so the output looks like a receipt: claim,
result, method, honest line.

If you have an engineer and an afternoon, run them on the agent
that touches real data.

Two outcomes, both useful. It breaks. Now you know, on your
timeline, before the other side does. It holds. Now you have a
document with a fingerprint that says so, and that document is
worth more in a diligence room than any demo you could show.

If you would rather someone else run it, that is what the reply
line is for.

{footer}

============================================================
E5 (T+21)  SUBJECT: when it's yours
Purpose: the consequence email. Decision-maker register, no ask,
no method, closes on the date. Facts used (verified): Art 50 live
2 Aug 2026, marking grace closes 2 Dec 2026, Annex III applies
2 Dec 2027, penalties to EUR 35M or 7 percent.
============================================================

A claim is cheap to make. It is not cheap to own.

The vendor ships a number. Ninety-nine percent reduction. Fully
tested. The number is theirs to make, and it is yours to defend.
The board will not ask who produced the claim. It will ask what
you did with it. The insurer will not ask whether the vendor is
credible. It will ask what the check was. The other side of your
questionnaire will not take the vendor's number as your answer.

So there is a moment, once, where the claim stops being a
marketing asset and starts being a liability. It is the first
room where someone can re-run it. The board. The auditor. The
diligence call. The incident review.

That room has a date. In the EU the Article 50 marking grace
closes 2 December, and Annex III applies from 2 December 2027. In
a deal it is the questionnaire deadline. In a launch it is the
day the agent touches real money.

If one of those dates is in your calendar, the check is not a
nice to have. It is the only document that changes what that room
says.

{footer}

============================================================
E6 (T+28)  SUBJECT: one question
Purpose: the qualifier. Sorts the list into two lanes: keep the
notes (tested it) vs the personal receipt (tested a demo).
Register: direct, no register shift. Motifs: receipt x1.
============================================================

One question, and the honest answer is the useful one.

Which is closer to true about the agent you run: we tested it, or
we tested a demo of it?

If it is the first, keep the notes coming. They are for you. If
it is the second, reply with one flow: what it touches, what it
does, one edge case you are not sure about. I can run two
receipts a month, free, and yours would take one of the two.

Either way, keep the question. The next person who asks it of you
will not be me.

{footer}

============================================================
W (weekly, the spine)  SUBJECT: one number
The personalized verified research (protocol R13, R14). One number
a week, verified by the owner running the re-run. Full template in
the protocol (merged first line, per-room framing, the four lines,
the honest line, the teaser, the P.S., the footer). No CTA unless
the number is re-runnable by the reader, then the CTA is "run it".
If no number passes the gate this week, the honest week email goes
out instead (short, true, cadence kept).
============================================================

## SEQUENCE STATE

E1 DRAFTED (both variants: list opt-in + personal receipt
scheduled)
E2 DRAFTED
E3 DRAFTED (source verified: owner's own D2 post, public)
E4 DRAFTED (repo verified: github.com/Teamthy/ai-redteam-five-tests)
E5 DRAFTED (all dates verified, see purpose line)
E6 DRAFTED
W TEMPLATE (in protocol)

First send: after platform setup (protocol, platform section) and
the first consented capture (CONTACTS LOG). Nothing is sent from
this file until the owner says sent (R10).

Last updated: 2026-10-27 (sequence drafted)
