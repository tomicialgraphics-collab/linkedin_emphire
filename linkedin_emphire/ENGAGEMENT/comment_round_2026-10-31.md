# Comment round, 2026-10-31 (feed paste, 1d window)

Built against `comment_surfaces.md` (protocol 1-10), `voice_dna.txt` COMMENT MODES,
and the 10-26 ceiling/spacing guardrails. One thesis across the round: the record,
not the intent. Every draft ends on a statement.

**Ceiling math for today:** 4 replies owed + 2 new comments (2A Tanya, 2B Brad late capture) = 6 actions, inside the base 8. Only one is OUTSTANDING, so the 2-a-day cap holds. Replies are exempt from
the 60-minute rule on active threads. That leaves headroom but I would not spend it,
for the reason in the last section.

---

## 1. Replies owed (do these first, they outrank any new comment)

Method ladder rule 1: a reply owed beats a fresh surface, every time.

### 1A. Brad Wolfe, mention on the fractional-owner post (1d)

He wrote: ending the engagement should not end the hold, so write it so a hold stays
until the board or its named delegate releases it, and termination triggers notice
listing every open hold.

**INTERACTIVE, 60 words**

```
Agreed, and the register is what makes it stick. A hold living
in a conversation ends when the conversation does.

Each needs a row: what's held, who raised it, what would
release it, who signs that release. Termination can't clear it
quietly, because the notice carries the open rows.

Undefined release authority is where holds and agent
permissions fail alike.
```

Why: he mentioned you by name on a 45-comment thread, which is a distribution
event, not a courtesy. The reply gives the mechanism he did not name, which keeps
you as the person who supplies the artifact rather than the agreement. It also
closes the loop back to your own thesis in the last line, on his surface, his
vocabulary.

### 1B. Mike Dabydeen, on your own permissions post (1d)

He argued the check has to live in the signer, with a hash of the canonical request
(asset, amount, destination, nonce), and the approved call and the executed call
should hash the same, once.

**INTERACTIVE, 60 words**

```
You're right that it has to fail at the signer, and the nonce
is what makes the approval single-use.

One addition: the hash binds the content of the request, not
the authority behind it. Bind the approver's identity and the
tool version into the same digest. Otherwise yesterday's
approval still verifies against today's call, on a tool that
changed underneath.
```

### 1C. Araiz Khan, on your own permissions post (1d)

He agreed the permission set matters as much as the prompt, and would keep agents
autonomous inside a sandbox with gates around anything reaching outside it.

**INTERACTIVE, 64 words**

```
Agreed, and the sandbox line is the one doing the work. Inside it the
agent can be as autonomous as it likes. The moment it crosses out,
the question stops being what it was asked and becomes what it can
reach without a person.

That's why I keep the two lists apart. The gate only counts if it
sits somewhere the agent can't reach.
```

### 1D. Hitesh Choudhary, reply on his comment (1d)

He said: record what you can actually verify, the model ID for an API and the file
hash for open weights. 11 comments, 35 reactions, and this is a creator with real
reach in your ICP.

**INTERACTIVE, 52 words**

```
Thanks Hitesh. The API case is the awkward one, because there's
nothing to hash. The best you get is the alias, the date, and the
exact response set you tested against, so a behaviour change is
provable instead of arguable.

That's the version of a pin an API can honestly give you.
```

---

## 2. New comments (tier 1-2, in lane)

### 2A. Tanya Janca, "what is your agent ACTUALLY allowed to do" (16h)

Tier 1, 1st degree, named-human security publication, dead center of the lane.
Her post asks the question your whole frame answers, and it ends by asking what
technically prevents the thing. Best fit in the paste.

**Note before sending:** `comment_surfaces.md` says this surface already holds two
carried drafts (119w PHP2Shell, 129w threat-modeling). This would be the third. The
protocol lets you pick which goes first, so either send this instead of one of them
or hold it. It is the strongest of the three on lane fit, weaker on timing, since
both of those drafts are now stale and this one is 16 hours old.

**OUTSTANDING, 119 words**

```
The list is right, and the question at the end is the one that
gets skipped. If the answer is a prompt, you have a
description, not a control. The prompt says what you'd like.
The permission set says what happens on the model's bad day.

The surprise is the second hop. Nobody grants an agent the
payment system. They grant it a deployment tool holding a
credential that reaches the payment system, and every step
looks sensible.

So I test the set that exists, not the one described. Give it
a task with no reason to touch a restricted resource and watch
whether it reaches.

An agent's permissions are a threat model written once and
never read again.
```

### 2B. Brad Wolfe, "most payment fraud does not create a vendor, it changes one" (21m, late capture)

Thread partner, 1st degree, 60-comment class author. His beat is finance and yours is
evals, but this post is about who can change a control record, which is your ground.
Commercial author (`wolfepacks.com`, daily cadence, tags collaborators), so the rule
is value that stands on its own with no pitch.

**QUESTIONING, 116 words**

```
The four controls are right, and the callback is the one that
stops the money. It has one hole, one field over.

Control 1 trusts a phone number already on file. That number
lives in the vendor master beside the bank detail, and whoever
can change the account can often change the contact too. Then
you call the attacker back, they confirm the change, and the
control works as designed.

So the contact record needs its own change control, held
separately from the billing record. Two fields, two controls.
Right now only one of them is defended.

Who can change the account isn't the question. It's who can
change the number you'll call to confirm it.
```

Why this angle and not another: the approval-binding argument is already spent in the
Mike Dabydeen reply (1B), and the hold-register argument is spent in 1A. Control 1 is
the only one of his four that a second field change defeats, and nobody in his comment
thread has said it. It also answers his closing question by replacing it, which is the
strongest position on a post that ends on an open question.

Protocol 5 check: same thesis as 1C (the control has to sit somewhere the actor cannot
reach it), different surface, closing line distinct. That is what "one thesis, different
surface" asks for, not a violation. All seven closings in this round are unique.

---

## 3. Ranked and held, with the reason

| Surface | Age | Why it is held |
|---|---|---|
| **~~Rock Lambros~~**, 200-character approval / MCPTox | 1h | **Promoted to 3A, source read, ready to send.** Was held on the DFM dedupe and the unfetchable links. `cxbom.org` and spec 0.3.1 both read now, so the draft cites their own ledger. |
| **Sam Illingworth**, accuracy claims without denominators | 1d | Dead center on methodology and he is following you, but you commented on his Nature paper post 1d ago. Two consecutive Sam touches reads as a fan, not a peer. Send tomorrow. Draft below. |
| **Amjad Masad**, Agent Habitat / broker adds the credential | 23h | Tier 1 and in lane (credential never enters context is the correct pattern). Held because this is the third Replit touch and the earlier partner-program post was already skipped as commercial. Tomorrow's first pick, not today's second. |
| **Jerry Liu**, 61% perfect extraction on ExtractBench Pro | 18h | Tier 1, checkable number, and it pairs perfectly with the Sam draft. But two number-critique comments in one day is a single note played twice. Hold behind Sam. |
| **Daniel Miessler**, 1,500 commands/hour | 15h | In lane, body is too thin to add to without the link, and `lnkd.in` will not fetch. Skip unless you read the linked piece. |
| **Neil Sahota**, election chatbots, 22% wrong district | 13h | Adjacent, not core, and a broadcast-media post. Tier 3 spice at best. |
| **Amanda Minnich / Craig Nelson / Tim Schulz** (Microsoft AIRT) | 21h | You have already applied to that team and commented on the hiring post. Commenting again on the team's reposts while an application is open reads as pressure. Watch, do not engage. |
| **Chinasa T. Okolo** repost, **Hamel Husain** repost, **Sara Hooker** repost | 1d | Congrats and promo surfaces. React, do not comment. |
| **Blossom Affia** (x6), **Bolaji Adebayo**, **Kieran Drew**, **Ruben Hassid**, **Tiago Forte**, **Alex Hormozi**, **Alex Banks**, **Luís Rodrigues**, **Endrit Restelica**, **Iyinoluwa Aboyeji** (x8) | 1d | Out of lane, creator-economy or engagement-bait. The Aboyeji block is Talent Nation funding news, which is Nigerian-tech distribution rather than evals. One thoughtful repost would beat six comments, but not this week. |

---

## 4. Held drafts

### Rock Lambros, 200-character approval / MCPTox (1h)  -- SOURCE READ, ready to send

**Source status: VERIFIED** against `cxbom.org` and specification 0.3.1, both fetched and
read in full. The `lnkd.in` links are redirects and will not resolve from here, and the
MCPTox study was not read, so nothing below cites MCPTox. Every number in the draft comes
from their published reference session ledger, not from the post body.

**QUESTIONING, 120 words**

```
The 200 characters are a rendering problem, not a detector
problem. In your own reference session the fetch definition is
357 tokens. Two hundred characters is about fifty tokens, so
the summary covers a seventh of a definition under one percent
of the context window. Nobody is being spared a long read.

The proxy holds the full text and the record holds its digest,
so show all of it, and on a re-listing, the diff. The delta is
where the rug pull lives.

Then measure the reviewer, which is the number you don't have.
Seed known-bad definitions at a rate you know and report how
many a human caught, sample size attached.

An approval nobody has measured is a click.
```

**The finding the post omits.** Their own reference session ledger publishes the numbers
that answer the 200-character complaint. The `fetch` tool definition is **357 tokens**,
which is **0.77%** of a **46,205** token context window and is flagged **TRUST INVERSION**.
Two hundred characters is roughly fifty tokens, so the approval summary renders about a
seventh of a definition that is itself under one percent of the window. If he is proposing
to publish more of the review surface, the arithmetic says the whole thing costs a scroll.
That is a stronger argument for his position than the flaw he is conceding.

The draft also separates the two cases he runs together: a re-listing has a digest to diff
against, and the delta is small; a definition malicious on day one has no delta, which is
exactly why his sentence about approval being the only defence is right. That concession
then earns the ask in the last paragraph.

**Dedupe:** confirm the 155w Dual-Failure draft from 10-29 is posted or dropped before
sending. If it went out, this is the second Rock action in two days, which the 10-28 like
already bought room for. If it hasn't gone out, publish that one first or drop it, and do
not run two live Rock drafts.

### Sam Illingworth (send tomorrow)

**QUESTIONING, 120 words**

```
The denominator is what kills most accuracy claims, and the
confidence interval is the honest version of the question. Ten
errors across twelve thousand pieces isn't a rate, it's a range, and
the deck always shows the point in the middle of it.

I'd add a fourth question, because the interval only covers
sampling. What was the set, and can I rerun it? A tight interval
around one domain is precise about the wrong population, and it does
not survive contact with another.

The clean results are the tell. No failures in 89 tests reads like a
pass and means the test has not been near the failure yet.

A rate with no denominator is a claim wearing a number.
```

---

## 5. Two things the paste says that the protocol does not cover

**The comment engine is working. The post engine is not.** Your own posts are at 76,
26 and 27 impressions. Your comments are at 5,808, 1,176, 346 and 363, and the
phantom-permissions comment on the Brad Wolfe thread is in a 45-comment room where
he then mentioned you by name. You are being distributed through other people's
audiences and not through your own. That is the opposite of the usual failure, and
it means the fix is not more comments, it is fewer of them and one post a week
built to carry the frame instead of answering someone else's. Worth a strategy
session rather than a slot in this round.

**"Harness" is on your own banned list.** `banned_words.txt` lists it as AI slop
("use instead: test suite, rig, framework"). It is also the word you use in your
resume, your Aithos letter, and half your comments, including the one in this feed
("an open-source harness with five reproducible failure checks"). One of the two is
wrong. My read: the ban was written for LinkedIn voice, where "harness" does read
as tooling jargon, but it is the precise term for your artifact and the recruiters
reading it know the word. Keep it in technical documents, avoid it in posts, and
add a note to `banned_words.txt` so the next session does not re-litigate this.
Every draft here avoids it, which is why none of them say the word.

---

## 2B RESULT: posted, and the author replied

2B went live at ~4 impressions, 1 reaction. **Brad Wolfe replied 3 minutes into it**, which is
the thread signal that matters and not the impression count. He extended it past what the draft
argued:

> "They rarely change both on the same day. The contact changes first, quietly, and the bank
> request comes a few weeks later, when the callback reaches them. So beyond separate control on
> each field, the sequence is worth watching. Any bank change within 90 days of a contact change
> gets called on the number from before the contact change, and someone outside AP signs it off.
> The pair is the signal, even when each change looks routine on its own."

He moved the frame from "two fields, two controls" to "the pair is a signal over time", which is
better than the draft. Protocol rule 6 applies: an author reply is a scheduled action the same
day. The reply below concedes that and attacks the one thing his fix leaves open.

**INTERACTIVE, 56 words**

```
Right. The pairing is what most systems can't see. Two logs, two readers, and nobody looks at the pair.

One caution on 90 days. A fixed window becomes a target, and anyone who knows the rule just waits it out. Key the callback to the pre-change number with no expiry, and the waiting stops helping them.
```

**Why the window attack and not the visibility point.** The visibility point is true and he would
agree with it in one line. The window is a real hole in a fix he just proposed, and it generalises
to every control built on a threshold: a rule with a number in it tells the attacker the number.
It also keeps the thread on his ground, which is how a thread partner stays a thread partner.

---

## Surface served late: Ashwini Mathur, "keeping humans human" (18m, edited)

**Profile read.** 1st degree. Executive Director, Onesto Consulting. Services page live, so a
commercial author. No prior history in this file. Post is a 4/5 review of an AI thriller plus a
humanist reflection, ending on "The real challenge may not be keeping humans in the loop. It may
be keeping humans human."

**Ladder verdict: SKIP for pipeline, optional for the relationship.** Rule 2 fails (not ICP:
consulting ED, not security or evals). Rule 3 fails (not tier 1-2 for reach, and the post carries
no checkable claim). What is left is a fresh 1st-degree humanist post with a book link, which
under rule 6 is weak fit. Headroom is not a licence to fill, and this is exactly the surface type
that eats minutes without moving a dollar or a referee.

**Source rule fails.** The review link is `lnkd.in` and does not resolve from here. Any comment
is UNVERIFIED-SOURCE and must come from the post body alone. Do not discuss the book.

**Why a draft is still here.** The closing line is the one place this touches your lane, and a
1st-degree relationship is worth one sentence. This is relationship maintenance, not pipeline.
Send it only if you want the thread warm, and count it against the 8 as a low-value action.

**HUMAN, 79 words**

```
Keeping humans human is the right worry, and there's a duller version of it that shows up as a control failing rather than a culture one.

A person approving five hundred items a day stops reading and starts clicking. The loop still looks closed on the diagram, and everyone can point to the human in it.

The human in the loop isn't the safeguard. A human with time to read the item, and the standing to say no, is.
```

It does not touch the book, does not feed the review link, and stands on its own. The point is the
one already made twice today in different words, which is the risk: three versions of "a human
clicking is not a human checking" in one day is a drumbeat. If both Brad threads are live, skip
this one and save the line.

---

## Surface served late: al neitsch, Just Eat AI food images (21m)

**Profile read.** 1st degree. Founder TNGC, consultant, author, advisor in data and AI engineering
and governance, with a services page. Commercial author. No prior surface history beyond a mention
in the audience follow list.

**Ladder verdict: COMMENT.** Fresh, in lane at the governance end, and it carries a real incident
rather than a reflection. He sells governance advice, so the value here has to stand without
feeding his practice, which it does: the comment is about a public claim a company made, not about
his service.

**Source rule satisfied.** The post names BBC News but carries no URL, so the paste alone was not
enough. Searched and read the BBC piece (2026-10-21, bbc.co.uk/news/articles/crz981p0klvgo) plus
the NDTV write-up. The finding below comes from that, not from the post body.

**The finding the post omitted.** Just Eat said **every image had been manually checked** before it
appeared on the platform. The post argues for "human oversight" as the missing piece. The
oversight was not missing. It ran, and it passed a glass of cola with bacon and egg floating in it,
and a "jacket potato" rendered as a puffy jacket covered in potatoes. This is a different argument
from the rest of today's round: not that reviewers click through at volume, but that the reviewer
was asked the wrong question. A competent-looking image passes "does this look like food" while
failing "is this the dish".

The four failures also share one cause, and it is the one that matters most to your positioning:
soda bread, chip muffin, cheese roll, plain. Regional vocabulary, read literally. That failure class
lands first in markets the model's training data under-represents, which is the Global South argument
you already make, arriving in a UK case.

**QUESTIONING, 118 words**

```
The line missing from most coverage is the one worth stopping on. Just Eat told the BBC that every image had been manually checked before it appeared.

So the check existed, and it passed a glass of cola with bacon and egg floating in it. That isn't a missing control. It's a control that asked the wrong question. A reviewer looking at a competent-looking picture judges whether it resembles food, not whether it is that dish.

And look at what tripped it: soda bread, chip muffin, cheese roll, plain. Every one is local vocabulary read literally.

Ask whether the image contains the noun in the item name. All four fail that. All four pass "does this look plausible".
```

**Why this one is not the drumbeat.** Today already carries three versions of "a human clicking is
not a human checking". This is the first that is about the criterion rather than the volume, it
rests on a public claim the company made, and it is the only one with a cheap test attached that a
reader can apply to their own pipeline. It also does not ask him to agree with you about governance,
which keeps a commercial author out of defensive posture.
