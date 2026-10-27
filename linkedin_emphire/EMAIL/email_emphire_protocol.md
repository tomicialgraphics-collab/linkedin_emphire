# EMAIL EMPIRE PROTOCOL (division charter, living doc)
# The inbox is the only channel in this campaign you own.
# LinkedIn can throttle it, reformat it, or leave it. The list survives all of that.

DIVISION: EMAIL (sibling of LINKEDIN, OUTREACH, ENGAGEMENT)
ESTABLISHED: 2026-10-27
MAGNET: the free single-agent verification receipt (two a month, real)
STAGE: 1 of 3 (capture + value, zero offer)
PLAYBOOK LINK: LINKEDIN/sell_like_crazy_5k_playbook_2026-10-25.md,
section 3, the line "OPEN DECISION: build an owned email capture for
the HVCO". That decision is now made (owner, 2026-10-27: staged build,
free single-agent verification receipt as the magnet, no platform yet).
This division is the owned channel underneath LANTERN 1 to 6. The
Lanterns bring people. The list keeps them.

## RULES (non-negotiable)

R1 CONSENT BEFORE CONTACT. Three capture points only, all
consent-based, same logic as the no-cold-DM rule in LINKEDIN:
  1. Agent Gate DM reply (LANTERN 3, step 3 context)
  2. Article 50 / article one-pager (end-of-article line + reply CTA)
  3. Warm comment reply (only where the conversation already
     touched a number or a claim)
Copy for all three lives in EMAIL/magnet_verification_receipt.md.
A reply is the consent. Never: cold email to a scraped address,
bought lists, a "newsletter pitch" to someone who never engaged.
Every contact is logged in the CONTACTS LOG below with: date, name,
source, consent timestamp, the exact consent line used, tier
(decision-maker or practitioner room).

R2 NO OFFER BEFORE THE GATE. Stage 1 emails never mention the Agent
Gate, the price, or the slots. The only CTAs allowed: reply (a reply
is consent for the next step), read, run. Stage 2 copy exists but is
HELD in EMAIL/sequence_02_offer.md. Gate = 100+ contacts AND 2+
receipts delivered AND 1+ receipt reply, then the owner says GO.

R3 NO DASH PUNCTUATION. No em dash, no en dash, no spaced hyphen as a
sentence separator, in any email, subject line, or footer. Use
commas, colons, periods, parentheses. Hyphens inside compound words
(re-runnable, 48-hour, one-page, decision-maker) are unaffected.

R4 BANNED WORDS APPLY. banned_words.txt at repo root. No delve, no
leverage, no unlock, no robust, no streamline, no harness, no
navigate, no landscape, no elevate, no comprehensive, no "it's worth
noting", no "in today's world". If a banned word is the only word
that fits, the sentence is rewritten, not the word swapped.

R5 MOTIF BUDGET. The brand motifs (re-run, receipt, claim not a
result) are allowed at max 1 to 2 uses per email, and they must vary
across the sequence. A sequence where every email lands on the same
line is a template, and templates get unsubscribed.

R6 ONE IDEA, ONE CTA. Every email carries one idea and at most one
CTA. The CTA is a reply, a read, or a run. No email ends with a
method. E1 to E2 are method-first (the receipt is the method, that
is the proof). E3 to E5 are consequence-first (forcing functions,
dated triggers, the decision room). E6 is the qualifier.

R7 TWO REGISTERS APPLY. Same rule as the LINKEDIN division: classify
before writing. PRACTITIONER room gets method-first. DECISION-MAKER
room gets consequence-first, names the forcing function (board,
insurer, questionnaire, diligence, the 2 December marking grace,
2027 Annex III), method only as a one-sentence answer to "how would
you know?", closes on the decision or the date. The sequence arc is
built so both rooms get their register in the right email.

R8 REAL SCARCITY ONLY. Two receipts a month is real (it is the
delivery capacity). Two Agent Gate slots a month is real (same
reason). No fake countdowns, no invented deadlines, no "last chance".
If the limit is not real, it is not in the email.

R9 EVERY EMAIL CARRIES THE FOOTER. Sender identity, what this note
is, the source line (why they are on it), the one-click unsubscribe,
Lagos address and timezone. No footer, no send.

R10 RECORD SENDS ONLY AFTER THE OWNER SAYS SENT. Same discipline as
the LINKEDIN log: DRAFTED until sent, SENT on the owner's word,
OPENED/REPLIED on data. Nothing is marked delivered from hope.

## STAGES

STAGE 1 (NOW): capture + magnet + E1 to E6 + the standing weekly
teardown note. Zero offer. Goal: a list that replies.

STAGE 2 (GATED): the first offer email (Agent Gate). Copy is
DRAFTED and HELD in EMAIL/sequence_02_offer.md. The gate, restated:
100+ contacts, 2+ receipts delivered, 1+ receipt reply, owner GO.
One offer email, one follow-up. Then the list returns to value only
for 14 days before any second offer touch.

STAGE 3 (AFTER FIRST EMAIL CLOSE): the case study email
(anonymized per the redaction standard in the playbook) + the
referral question (Tier 0 pattern from the playbook: the specific
ask, the referral question, no generic "forward this").

## SEQUENCE MAP

ID    DAY    SUBJECT                     PURPOSE                  CTA      STATE
E1    T0     the receipt                 sample receipt (PHP2Shell) + personal receipt offer    reply     DRAFTED
E2    T+3    how to read one of these    the four lines, method is the differentiator           none      DRAFTED
E3    T+7    a number I re-ran this week live teardown (490 unauth MCP servers, public)         reply     DRAFTED
E4    T+14   run this on your own agent  the five-tests repo, the DIY path                      run or reply  DRAFTED
E5    T+21   what a claim costs when it is yours  consequence-first, dated triggers, no ask     none      DRAFTED
E6    T+28   one question                the qualifier (tested it vs tested a demo)             reply     DRAFTED
W     weekly after E6  one number, re-run (date)  standing teardown, format below               none      TEMPLATE

Full copy: E1 to E6 in EMAIL/sequence_01_welcome.md. Stage 2 in
EMAIL/sequence_02_offer.md. The magnet and all capture copy in
EMAIL/magnet_verification_receipt.md.

Weekly teardown template (standing after E6):
  SUBJECT: one number, re-run (the date)
  CLAIM: the vendor or benchmark number, one line
  RESULT: what the re-run showed, one to two lines, the number
  METHOD: how to re-run it, the fingerprint, the source
  HONEST LINE: what it does not prove, one line
  (one line: why this week)
  (footer)

## PLATFORM SETUP (free tier, platform-agnostic)

No platform yet (owner, 2026-10-27). Setup order:
1. SENDING DOMAIN. A custom domain or subdomain (notes.yourdomain).
   Never a free mailbox address for a growing list. SPF, DKIM,
   DMARC records set at signup.
2. DOUBLE OPT-IN. ON. The list is foreign-first (foreign_first_pivot
   2026-10-25), so EU contacts are in scope: GDPR. Double opt-in plus
   a stored consent record (R1) is the floor. US: CAN-SPAM
   (identity, address, opt-out honored. Immediate is the practice).
3. HOSTED vs OWNED. Option A, start: a hosted free tier (verify
   current limits at signup, they move. Resend, Brevo, Mailchimp
   class). Fine to 300 to 500 contacts. Option B, the empire
   standard from ~500: listmonk, self-hosted on a $5 VPS. No
   per-recipient cost, full ownership, the email is the asset so the
   infrastructure is owned too. Decide at 300, not at 5,000.
4. WARM-UP. Week 1: 10 to 20 sends/day. Ramp roughly 2x per week to
   100/day. Never blast the free tier on day one. Reputation is the
   channel.
5. UNSUBSCRIBE. One click, immediate, no confirmation step, no
   guilt trip in the goodbye.
6. FOOTER. Per R9, on every send, including the opt-in
   confirmation.

## KPIs (weekly, logged in the KPI table below)

LIST: net new, unsubscribes, gate progress (100 contacts / 2
receipts delivered / 1 receipt reply)
OPEN: percent (warm consent list benchmark 35 to 55. Under 25 after
5 sends = subject problem, rewrite subjects, keep bodies)
REPLY: count and percent (the real conversion metric. A reply moves
the person to a 1:1 lane, DM or email, whichever they chose. The
list is where trust is banked, not where the sale happens)
RECEIPTS: requested, scheduled, delivered
UNSUB: percent per send (over 2 on any send = the note is not
delivering, check teardown quality before the next send)

## KILL / HOLD RULES (SLC discipline, from the playbook)

- 0 replies in 50 touches: HOLD all sends, audit the capture
  sources. A list that does not reply was not consented with a
  reason.
- Open under 20 percent after 5 sends: subject lines are the
  problem. Rewrite, keep the bodies.
- The reply rate is the number. Open rate is vanity here. This list
  is a sales trust list, not a media list.
- Any reply: the person leaves the batch lane and enters 1:1. Never
  run a campaign at someone who has talked to you.

## SEND LOG (newest on top)

10-27  DIVISION-0  EMAIL EMPIRE ESTABLISHED. Staged build (owner
        decision): magnet = free single-agent verification receipt
        (two a month, real), stage 1 = capture + E1 to E6 + weekly
        teardown, stage 2 gate = 100 contacts + 2 receipts
        delivered + 1 receipt reply + owner GO. Platform = none
        yet, setup checklist above. State of all copy: DRAFTED.
        Nothing is sent until the owner confirms platform setup and
        the first consented capture.

## CONTACTS LOG (newest on top, per R1)

(none yet. First entry: date, name, source, consent timestamp,
consent line used, tier)

## KPI TABLE (weekly, newest on top)

(none yet. First row lands after the first week of sends)

Last updated: 2026-10-27 (division established)
