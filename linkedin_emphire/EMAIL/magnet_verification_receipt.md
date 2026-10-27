# THE MAGNET: the free single-agent verification receipt
# What we give away for an email address, and every word that gets it.

## WHAT IT IS

One specific agent flow or chatbot. One check. 48 hours. A receipt:
the claim, the result, the method, the honest line. It is the Agent
Gate's 48-hour first finding, given away free, on purpose.

Why this magnet (and not a PDF or a course):
- It is theirs, not generic. A receipt on their agent is the
  highest-value artifact the brand has, and the cost to produce is
  one check with the five-tests repo.
- It filters. Only a person with an agent and skin in the game
  replies with a flow. The list self-selects toward buyers.
- It is the offer in miniature. Whoever gets one has already seen
  the full version's shape. Stage 2 (the Agent Gate email) is not a
  pitch to them, it is a continuation.
- Real scarcity (R8): two receipts a month. That is the delivery
  capacity, not a number.

## THE RECEIPT FORMAT (the artifact itself)

Every receipt, personal or sample, has exactly four lines:

  CLAIM: what the number or the document says
  RESULT: what the re-run showed (the number)
  METHOD: how anyone, including the reader, can disagree with it
          using our setup (the fingerprint: model, seed, temperature,
          prompt version, date, where the source lives)
  HONEST LINE: what the result does not prove

Plus one closing line that is the lesson. That is the whole format.
If a receipt needs a fifth line to make sense, the receipt is wrong.

## THE SAMPLE RECEIPT (what every list opt-in receives, E1)

Source: the owner's own public post, VERIFIED_POSTS/
2026-10-22_php2shell_AREDTEAM_EVENT/post.md (posted 10-22, live,
120 impressions in the 10-26 capture). No third-party consent gate,
fully verified.

  RECEIPT
  Date: 22 Oct 2026
  Target: the PHP parser (every PHP app that parses untrusted requests)

  CLAIM: the parser treats untrusted input as data. Your
    validation, your framework, your auth, those are the layers that
    keep untrusted input out of your logic.

  RESULT: two 9.2 remote code execution bugs (CVE-2026-109618,
    CVE-2026-109619), reachable while PHP is parsing the request,
    before a line of your code runs. Emergency patch is out:
    8.2.35, 8.3.36, 8.4.27, 8.5.12. On 8.1 or older there is no
    official release at all.

  METHOD: the exploit tooling is public. Attempt signals were
    logged by Amazon and Cloudflare days before the patch. If you
    run PHP, check the runtime version now. If it is not one of
    those four, patch or move, then re-check the patch held.

  HONEST LINE: no confirmed breach as of the patch. CISA has not
    listed it as known-exploited. The public exploits reportedly do
    not work on a default install. The window between attempted and
    confirmed is the dangerous one.

  The one line this teaches: your check has to reach the layer you
  do not own.

## THE PERSONAL RECEIPT (spec, what we ask and what we deliver)

ASK (one message, no forms): "one flow: what it touches, what it
does, one edge case you are not sure about." Plus the minimum
access: a staging URL, or an API key for that flow only. No
production credentials without a scope doc. If they cannot give
access in a day, the receipt waits, and the sample stands.

DELIVER (within 48 hours, in writing):
- ONE concrete finding: the failed input, the exact repro, the
  root-cause class, the fix pattern. The Quick Scan spec from the
  playbook: a concrete defect, never a thin "free audit" that is a
  sales call in a coat.
- OR the honest result: "nothing material in this flow, here is
  what I ran." That is a receipt too. A clean receipt is a receipt,
  and it is the most trusted kind.
- Always: the fingerprint (model, seed, temperature, prompt
  version, date) so the result is re-runnable by them.
- Never: the offer, the price, the slots. A personal receipt is a
  stage 1 artifact (R2). The follow-up to a personal receipt is one
  line: "if you ever want the full version of this, the reply line
  works." Then silence.

CAP: two per month. When both are taken, the waitlist gets the
weekly teardowns and the next slot is named by month, not by
countdown (R8).

## CAPTURE COPY (paste-ready, all three points)

VARIANT 1: the Agent Gate DM reply (LANTERN 3, step 3 context)
  "I run these checks, and I send one short note a week when a
  number turns out to be a claim. The re-run is in the same note.
  Your address, one click to leave. Want the first one?"
  (on yes + address):
  "Got it. The first note is a sample receipt: the claim, the
  result, the re-run. If you want one on your own agent, reply to
  that note with one flow. I can run two a month, free."

VARIANT 2: end of Article 50 / article one-pager
  "One line, in case it helps: I send one short note a week, one
  number, the re-run attached. Reply with your email and the first
  one is on its way. One click to leave, any time."

VARIANT 3: warm comment reply (only where a number or claim was
  already discussed in the thread)
  "Short version: I re-run AI numbers for a living, and I send the
  ones that break as a weekly note. Reply if you want the first
  one. One click to leave, any time."

## THE ONE-PAGER (1-page site, BUILD, ~1 hour per the playbook's
## minimal version)

HEADLINE: The claim, the result, the re-run.
SUB: One short note a week. One AI number, re-run, with the method
inside. Free. One click to leave.
BODY (short):
  "I'm Timothy. I break AI products before users do. Every week I
  pick one number, a vendor claim, a benchmark, a 99 percent
  reduction, and I re-run it. The note is four lines: the claim,
  the result, the method, and the honest line about what it does
  not prove. No course. No funnel. One number a week, and two
  people a month get a free receipt on their own agent flow."
OPT-IN FIELD: [ email ]  [ first note ]
FOOTER: Timothy Olusanya, AI red teaming, Lagos, Nigeria (UTC+1),
one-click unsubscribe, the source line on the confirmation email.

STATE: DRAFTED (copy) + BUILD (the page itself is not built yet)

## STATE

MAGNET: DRAFTED (format + sample + spec + copy all above)
PERSONAL RECEIPTS DELIVERED: 0 (cap 2/month, month of 10-27)
WAITLIST: 0

Last updated: 2026-10-27 (magnet drafted)
