---
deliverable: internal
id: 2026-11-20_thread_linkedin-marvin
date: 2026-11-20
audience: internal
status: ready
approved: no
title: The LinkedIn thread with Marvin Percival, 02:22 to 19:01 WAT on 20 November 2026, as pasted by the owner
time_checked: >-
  checked: 2026-11-20 18:48 WAT, read from the system clock in the sandbox before this file was written.
sources_read: >-
  read: the thread as pasted into the session by the owner at about 18:40 WAT on 20 November, plus Marvin's 16:20
  message pasted earlier the same session. Nothing opened. Times are the times LinkedIn showed, in WAT.
---

# Marvin thread, 20 November

What this is: the record of what was actually said on LinkedIn on 20 November, so later sessions read the thread
rather than reconstruct it from drafts. Who it is for: any session working on Ẹ̀rí or on the Marvin relationship.
What to do next: read it before writing to Marvin, and check a draft in `ENGAGEMENT/` against what was really sent.

Three things are withheld from this copy, on purpose, because this repository is public:

- **A credential.** At 04:12 Marvin posted the password of the shared Gmail and Claude account. It is replaced
  below with `[credential withheld]`. It has to be changed, see `ENGAGEMENT/2026-11-20_dm_marvin-the-password-in-the-chat.md`.
- **His family's travel.** Where his wife was flying from and to, and when. Replaced with `[personal, not recorded]`.
- **A deleted message** at 15:01, which LinkedIn shows only as deleted.

The owner's long messages are recorded in full because they are what was sent. Several of them also exist as
drafts in `ENGAGEMENT/2026-11-20_dm_marvin-*.md`; where the two differ, this file is what Marvin received.

## The thread

**02:22 Marvin.** I think we should build the test first, it can be hosted as a test on my MacMini. Any real project
will need to be hosted in Nigeria. It will be holding data that must be in Nigeria.

**02:23 Owner.** no challenge with that

**02:24 Marvin.** I will begin loading files into the repo tomorrow. I will get Claude to organize it properly.

**02:24 Owner.** what should be focus on for now, your ready market fit product or the Eri product for the new market. Then: good

**02:24 Marvin.** ERI

**02:25 Owner.** are you fixing claude for me also. you could sub the claude from your end and just send me login

**02:25 Marvin.** The REQ document

**02:25 Owner.** read through it

**02:26 Marvin.** I will check on how best to manage Claude too. It will all start to make sense tomorrow

**02:27 Owner.** The scoped plan, seven pages, so you have it before Monday. It landed at 7.45 build days, about 60
hours, which is your 6.5 plus 0.95 for the amendments, and I've taken the four weeks out as agreed. It's here and it
opens without an account (Drive link to `2026-11-20_Eri-practice-build-plan.pdf`, the same file as
`CLIENTS/eri/exports/`). Same file I'll have open on the Friday call. If you only read one page, read the third. It is
the order and what each cycle ends with, and it is the part that would be expensive to change after we start. What
I'd like back is a yes, or the document with your cuts on it. everything on page 4 can be argued about while cycles
one and two run.

**02:28 Marvin.** I will review tomorrow

**02:29 Owner.** Okay, thanks

**02:37 Marvin.** NIPOST key: we don't have one yet. Live keys need company verification. We will need to use the
recorded sample responses from the start. I am not sure how else to get around this. I am not sure they will accept a
US company to give an API key to.

**02:44 Owner.** Good, that settles one of the two, and better at two in the morning than at the review.

Three things and then it's off the critical path.

Record the sample, don't write one. If we invent the response shape we'll build against an interface that doesn't
exist and the day the key lands it's a rewrite. Ask them for the schema, the error codes, the rate limit, and whether
valid=false is the only way a lookup fails. A screenshot of one real response is worth more than a day of our
guessing.

Build the switch, not the fixture. One interface with two implementations, sample and live, chosen by a config value.
Half a day now, a config change later, and no rewrite either way.

And no sample on a screen without saying so. I've added it as REQ-052: when the address comes from a recorded sample,
the screen says "sample response, captured on" and the date. Same reason the certificate says what it doesn't prove.
If a reviewer finds out afterwards that the address was a fixture, they stop trusting the rest of the demo, and this
whole product is the habit of not overstating what it knows.

On the US company worry, you're right, and it resolves itself. The key goes to a Nigerian company, and we're
registering one. So this isn't a blocker, it's an argument for doing the registration properly and putting the RC
number in the application.

Monday doesn't move. 001 to 005 are untouched, and 006 to 010 run against the sample.

Stele is the other one, and it's now the only thing left that can stop week one. If it can't mount this week, say so
today and we agree the development-only session in writing instead.

ERI it is. I'll stop bringing the other one up unless you want it compared properly, and if you do, give me its name
in writing and I'll put the two on one page against three questions. Who pays first, who signs, and what proves it
worked.

Now distribution, because that's the real worry and I've been answering it sideways.

ERI doesn't distribute to buyers. Buyers are the free end. It distributes through issuers, one at a time, starting
with the surveyor who already lost an argument about which version of a plan was current. He has a reason to care
before we sell him anything.

The mechanism is the free check. Every buyer who checks and gets no record is a lead that we hand to an agency, and
the agency has a reason to open an account on the day it happens. That is the only part of this that spreads without
money, and it is also why checking stays free and registering is paid.

What decides it is not the build and it is not the register either. It is who pays first. We agreed the buyer does
not and the agency does, and I still don't have a number for the moment of sale. Until that number exists,
distribution is a story I can tell well and cannot test.

Two things to withdraw from my own messages. Forget the Claude login. Sharing an account is against their terms and
it breaks the day you change a password, so either put me on a seat or send the money and I'll pay for my own. The
second is simpler and I can start Monday either way.

And on the repository, before you load anything: it is still public, so make it private first. Then load the
requirement document, the amendments and the plan. Nothing from a client, nothing real, no keys.

Mac Mini is fine for the test. One condition, which is that I can reach it from outside your network for the Friday
reviews, so it needs a tunnel or an address that survives a router restart. You're right that real data has to sit in
Nigeria, and that is a reason the company is Nigerian rather than a detail we deal with later.

Review it tomorrow. Monday morning I test the anchor regardless, because that result is worth having whether or not
the plan is agreed.

**02:47 Marvin.** The build is a test, not necessarily a product

**02:49 Marvin.** I am sending a request to NIPOST (with a screenshot)

**03:00 Owner.** Good, While you're in there, add two questions so we don't need a second round trip. What they need
to verify a Nigerian company, since our RC number may not exist yet when they answer. And whether there are test
postcodes or a sandbox, or whether every lookup from day one is a live one.

Agreed on test rather than product, with one condition. A test has to settle something specific or it quietly
becomes a smaller product. So here are the three things I think it settles, and then we can argue about them.

That anchoring returns something a stranger can open without us in the room. That a stranger with a file and no
account gets a straight answer, including a straight no. And that the two of us can run a cycle at this pace without
either of us going quiet for a week.

If those aren't the three you want, name yours and I'll build to them instead of mine.

**03:02 Marvin.** I think the REQ file covers all your questions and more. The NIPOST request is in, so we just have to
wait and see what they say

**03:03 Marvin.** "And that the two of us can run a cycle at this pace without either of us going quiet for a week."
If this happens, we have failed

**03:05 Owner.** Fair, and mostly right. The file does cover the mechanics, which is why it was worth writing as
requirements instead of a plan.

Two places it doesn't, and one of them is yours.

The fourth answer. REQ-035 tells a checker whether their file matches a sealed item inside one evidence file. Nothing
in the document says what a person sees when their paper matches nothing anywhere. That's your own argument from the
call, that it has to read as an ordinary answer and not as bad news, and it's the first screen of the demo rather
than the last, because on day one the register is empty and every check returns it.

Second, the pace thing isn't a requirement and I put it in the wrong list. It's an operating condition, not a
criterion, so it belongs in how we work and not in your numbering. My mistake.

NIPOST, fine. Waiting costs us nothing now that the sample is the path, so Monday doesn't depend on their reply.

I'll put the fourth answer into the redline as REQ-053, which is about ten minutes of work and one sentence of copy,
and send it with the rest over the weekend.

**03:10 Owner.** Agreed, and it's the only one of the three that a commit can't fix later.

So the rule should be easy to keep rather than noble. Silence isn't the failure. Silence nobody flags is. If either of
us is losing a week, we say so before it happens, with a date for when we're back, and the other one doesn't read it
as a warning sign.

You've spent the small hours on NIPOST paperwork for something you've just described as not necessarily a product.

That's the part I noticed.

im so eager to work with you and learn from your wealth of experience.

**03:13 Marvin.** First draft (attached `Eri-Test-Mockups-v0_1.pdf`, 2 MB)

**03:21 Owner.** Read all nine pages twice. The placeholders are the best thing in it. No invented postcode, no
invented transaction id, a QR that says it does not scan, and the issuing office left open. Most design packs are full
of numbers that turn out to be fiction.

Listing the five states you haven't drawn is the same instinct, and it's why I can read this in ten minutes instead of
an hour.

Three notes, in the order they would cost us.

Screen nine says nothing has been changed since. That's true today and false the first time we seal a second batch,
which REQ-030 allows. Make it per batch: three items sealed on this date, nothing sealed at that time has changed
since, and a later batch appears as its own line. Then the sentence stays true for the life of the file.

The green panel with a tick reads as approval, and the sentence that stops it being read that way is at the foot in
small grey. Put that sentence beside the badge, before the item list. Keep the green for the one narrow thing it
earns, which is that this batch is unchanged.

Part three is bigger than it looks. The four results are drawn on a postcode check, which is the register. Our public
check page is a file check, reached by QR. Both are right, and they are not the same screen, and only one of them is
inside the forty-five. I'll write the requirement that says which, before anyone builds either.

The Yoruba is mine. I'll do the pass this evening, including whether "bá a mu" wants to be "bá ara wọn mu" and the two
places where "olùṣàyẹ̀wò ẹ̀rí sí i" reads oddly.

**03:23 Marvin.** I think I will put the files up on the repo and let you modify

**03:24 Owner.** we can get this done as fast and clean as possible. should i hold for the claude or should start
building the test case while we wait for response from NIPOST

**03:25 Marvin.** I will send the claude subscription to your bank in the morning

**03:31 Owner.** Thank you. Sending it to my bank rather than a card on an account is the right call, and I'll send you
the receipt so it sits on the company's books from day one.

Since you didn't ask for this, here it is anyway.

You wrote a requirements document where every line has an acceptance test a stranger could run. Most people write
down what they want. You wrote down how we will know, which is a much harder thing to do and the reason I could answer
you in an hour instead of a week.

Then you drew thirteen screens and left brackets where the truth is not known yet, and listed the five you had not
drawn. In one pack you did the thing this whole product is about, which is refusing to say more than you can support.

And you spent three in the morning on NIPOST paperwork for something you keep describing as only a test. I have met a
lot of people who talk well about rigour. You did it quietly, at three, without an audience.

i really do appreciate every effort youre putting into this

**03:32 Owner.** if i may ask whats your macmini config

**03:34 Marvin.** It is a MacMini M4 with 24Gb and 256Gb

**03:35 Owner.** oh wow, that works well

**03:36 Marvin.** Just asked my wife to send you $40 for 2mths of Claude

**04:12 Marvin.** PW = `[credential withheld]`. GMAIL account id is in WhatsApp

**04:16 Owner.** im in already

**04:21 Owner.** are you making it now

**04:25 Owner.** no need for the 40$ again from your wife in my account only if ill use for coffee or get better cellular
bandwidth. all expenses will be paid from immediate revenues

**08:25 Owner.** Hello are you there

**12:29 Owner.** i had to seat and draft out my career plans for next year this morning do you mind i share with you for
a review and hear your opinion about it or we just focus on the project at hand

**12:30 Marvin.** Share, happy to look

**12:31 Owner.** alright i will share the doc with you, im compiling it. hope you got enough rest

**12:31 Marvin.** Yes, thanks.

**12:36 to 12:42.** `[personal, not recorded]`: a short exchange about his wife's travel. He confirmed he had told her
about the owner.

**12:42 Owner.** so what are you up to today

**12:43 Marvin.** I am going to prepare docs and put in repo. Finish Stele recovery logic

**12:44 Owner.** also figuring out how the test case architect would be properly build and design here. Then, quoting
his own 04:25 message: what about the claude

**12:46 Marvin.** I could try and set it up here using the new Gmail

**12:46 Owner.** alright

**12:47 Marvin.** If that works, you can then simply use it with the Gmail ID

**12:48 Owner.** yes that works. just make the subscription on the gmail and i will access it from here

**13:16 Marvin.** You should be able to sign in using Google account (with a screenshot)

**13:22 Owner.** ohh im in already (with a screenshot)

**13:34 Owner.** ive not used it before im figuring out how to use it. i just connected my github to it

**13:35 Marvin.** I am currently looking at the Team plan requirements and benefits

**13:41 Marvin.** I think we can function well with a shared repo for now. I may set up a repo separately today for the
project, get Claude to manage it. Claude already manages repos for me so is used to how I operate. Will see how it
goes, we can always change if we don't like it

**14:01 Owner.** yes, and one of them rather than two. There is an empty Eri-OS under my account that I made, If you set
up the project one, I will delete that and we work in yours.

Three things I would want set before code goes in, and all three take minutes.

Private. Not for the code, for what will end up in it: names, postcodes, addresses, whatever the first test collects.

we can have the Main branch protected for both of us, including whatever Claude runs. No force-push, no history
rewrite, no tidying of a commit that a record already points at. An agent that manages repos is useful right up to the
moment it rewrites one we cited.

**15:01 Owner.** `[deleted]`

**15:17 Owner.** there are no task files here in the repo yet

**16:20 Marvin.** The repo is set up and you're in: github.com/DUNIN7/eri-test

I took your three points as the starting rules. It's private, main is protected for everyone (me and Claude
included), no force-push, no history rewrite, merge commits only so every commit keeps its ID, and every pull request
needs one approval from the other person.

Best place to start is the README. It has a short reading order. The one I'd most like your eyes on is
docs/ERI-Standards-v0_1.md. That's how DUNIN7 builds things, split into fixed rules and defaults. The fixed rules
don't move. The defaults are just where we start. If you've got a better way, write it up as a short decision note in
docs/decisions and we'll look at it together. Good ideas there go back into the DUNIN7 standards with your name on
them.

One you might want to look at before Monday: decision 0001 sets the stack to our usual Next.js / TypeScript / Drizzle
/ Vitest instead of the FastAPI server in REQ v0.3. If you'd rather go another way, now's the time to say so, before
any code is written.

Your scoped plan is in docs as the v0.4 draft. When you're ready, put your REQ changes in as a pull request and I'll
review them. CLAUDE.md is set up so your Claude Code and mine follow the same rules, and there's a three-line handoff
note in notes/ for whoever stops work, so we don't trip over each other across the time difference.

I'll be stepping back from day-to-day coding and acting more as architect and reviewer, so the build is yours to
lead. Separately, I'm tidying up a proposal for the company structure and how we go forward together. I'll send it
over in the next week or so, and we can talk it through on a call. Shout if anything doesn't make sense.

**16:49 Owner.** CLAUDE.md says a requirement is done only when its criterion has been seen on the Android phone and
the iPhone. Cycle one is the event table, the revoke, the adapters and the sample path, and most of those never reach
a screen.

Do you mean every requirement, or only the ones whose criterion names a device? If it's the second I'll write that
sentence into CLAUDE.md on a docs branch so the agent reads it tomorrow.

**16:51 Owner.** Good. That is the four rules I asked for plus two I had not thought of, and merge commits only is the
right call, because a rebase rewrites the ID a note later points at.

On decision 0001 I would keep your call. Next.js with Drizzle is one runtime, one deploy and one auth surface on a Mac
mini, and FastAPI beside a Next front end is two of each in exchange for nothing this product needs. Two conditions I
would write into the note, not change the decision for: the NIPOST key and the fingerprint recomputation live in
server code that never reaches the client, and the append-only grant on the event table is enforced in the migration
rather than in the app.

One thing the rules do not cover, and it decides what done means for cycle one. The instructions file says a
requirement is finished only when its criterion has been seen on the Android phone and the iPhone. Half of cycle one
never reaches a screen: the event table, the revoke, the three adapters. Do you mean every requirement, or only the
ones whose criterion names a device? Whichever you pick, I will put the sentence into the instructions file on the
docs branch so the agent reads it on Saturday.

I will read the standards and the v0.4 draft tonight. If that draft is the scoped plan rather than the requirements, I
will put my amendments in beside it in number order instead of creating a second v0.4 that disagrees with the first.

And noted on stepping back. I will bring you decisions and evidence rather than build steps. Send the structure
proposal when it is ready and we will do it on a call rather than in messages.

**16:51 Marvin.** Good catch. The second one. The phone check is for anything a person sees or touches: screens,
camera, mic, location, install, the QR scan. The event table, revoke, adapters and sample path are proven by their
tests, and that's enough.

Something like: "A requirement whose acceptance criterion involves a screen or a device feature is done only when it
has been observed on both the Android phone and the iPhone. Every other requirement is done when its automated tests
pass."

Go ahead and put it in on a docs branch. I'll approve it tonight so it's in main before your agent starts tomorrow.

I've got the iPhone side covered. Do you have an Android phone you can test on? If not, we'll sort one out.

**16:52 Owner.** The repo is in good shape, and the merge-commit rule is the part I'd have missed.

One thing worth sorting while it's small: if the code is the company's asset, it shouldn't sit in either of our
personal accounts. A free GitHub org, both of us as owners, and you transfer eri-test into it. Then it's nobody's
personal repo, and if either of us loses access to an account the work is still there.

Not urgent tonight. If you're happy with it I'll set the org up and send you the four transfer steps.

**17:00 Owner.** yes i use an android phone

**17:13 Marvin.** No rush on the repo. This is a test... Off to the airport...

**17:13 to 18:12.** `[personal, not recorded]`: he was collecting his wife. The owner sent his regards and said he would
leave him to his evening.

**18:27 Owner.** Not asking for anything tonight. Flagging while it is fresh.

I put the local database password into a file through the GitHub web editor, so it ended up in a commit on a pull
request instead of on my laptop. Nothing merged, the PR is closed, the password is already changed, and the database
is a Postgres on this machine with no real data in it. The repo is private, so it is small.

The rules say tell you the same day, so I am telling you the same day.

Enjoy the evening. We can decide whether to ask GitHub to purge that PR another time.

**19:01 Marvin.** Thanks for flagging the password straight away. That's exactly how it should go. I had a look: PR 5
only ever had the .env file, it never reached main, and the password's already changed, so as far as I'm concerned it's
closed. No need to ask GitHub to purge anything. That's for secrets that can't be rotated, and this one is dead. Only
lesson I'd take: the GitHub web editor ignores .gitignore, so .env should only ever be edited on the laptop.

PR 4 is approved and merged, so your agent will read the new done rule tomorrow. Small one for next time: bump the
version line at the top of CLAUDE.md when it changes (v0.2 to v0.3).

PR 6 is really good work. Tests written first and seen failing, run twice from an empty database, and the limits named
instead of hidden. You also caught a genuine contradiction in our own rules: F6 says nothing is deleted, DATA-RULES says
demo data goes after 30 days. Good catch.

On the purge door, here's my view. As it stands the purge also deletes the fingerprints and the seals, and DATA-RULES
says those stay. What if we split each event into two parts: the record (kind, seq, fingerprint, seal) that never goes,
with no door at all, and the content (payload, names, recordings) in its own table that's the only thing the purge can
touch? Then F6 holds completely, the privacy rule holds, and anyone can still prove a fingerprint existed on a date long
after the content is gone. That's the whole point of the certificate.

Your call on how to build it, but since it bends a fixed rule, please write it up as decision 0003 so it's on the
record. I'd rather we settle it before PR 6 merges than patch it after.

Your other two questions: agreed on the owner role. The app connects as eri_app, never the owner, and migrations run as
a non-superuser owner. I'll put that in DEPLOYMENT.md. And yes, send the v0.4 amendments as a PR whenever you're ready.

Tiny ones on PR 6, no rush: the commit should start REQ-020/REQ-030 rather than CHORE, and package.json picked up the
README version line as its description.

Last thing: there's a branch called claude/adoring-babbage-jng35n with a phased build plan on it. Is that yours? If so,
open a PR when you want it looked at.

Enjoy your evening.

## What the thread settled

| Settled | When |
| --- | --- |
| Ẹ̀rí is the focus, not the other product | 02:24 |
| The build is a test, hosted on his Mac mini M4 (24 GB, 256 GB); real data later sits in Nigeria | 02:22, 02:47, 03:34 |
| No NIPOST key; cycle one runs on recorded samples, labelled on screen (REQ-052) | 02:37, 02:44 |
| REQ-053, what a checker sees when a file matches nothing anywhere, goes in the v0.4 redline over the weekend | 03:05 |
| Silence is a failure only when nobody flags it first | 03:03, 03:10 |
| The repository of record is `DUNIN7/eri-test`, private, main protected, merge commits only, one approval per pull request | 16:20 |
| Decision 0001 accepted by the owner with two conditions | 16:51 |
| The phone check applies only to screens and device features; everything else is done when its tests pass | 16:51 |
| Marvin tests on iPhone, the owner on Android | 16:51, 17:00 |
| A joint GitHub organisation was proposed; Marvin said no rush | 16:52, 17:13 |
| The database password slip was disclosed the same day | 18:27 |
| PR 5 closed, no purge asked of GitHub: the password is rotated, so it is dead | 19:01 |
| PR 4 merged: the phone check applies only to screens and device features | 19:01 |
| The purge door goes: each event splits into a record that never goes and a content table the purge alone can touch. Written up as decision 0003 before PR 6 merges | 19:01 |
| The app connects as eri_app, never the owner; migrations run as a non-superuser owner. Marvin writes it into DEPLOYMENT.md | 19:01 |

## What it left open

- The shared Gmail and Claude account: the credential sat in a LinkedIn message, and the owner connected GitHub to that
  account at 13:34. Both need undoing. The owner's own 02:44 message said why.
- His company structure proposal, due within the week.
- The price at the moment of sale, still unanswered since 12:18 on the previous thread.
- Whether the Mac mini can be reached from outside his network for the Friday reviews.
