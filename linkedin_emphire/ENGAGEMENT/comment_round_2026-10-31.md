# Comment round, 2026-10-31 (feed paste, 1d window)

Built against `comment_surfaces.md` (protocol 1-10), `voice_dna.txt` COMMENT MODES,
and the 10-26 ceiling/spacing guardrails. One thesis across the round: the record,
not the intent. Every draft ends on a statement.

**Ceiling math for today:** 4 replies owed + 1 new comment. Replies are exempt from
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

## 2. New comment (one, tier 1, in lane)

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

---

## 3. Ranked and held, with the reason

| Surface | Age | Why it is held |
|---|---|---|
| **Rock Lambros**, 200-character approval / MCPTox | 1h | Highest-fit surface in the paste and he is your strongest thread partner (he liked the 10-28 comment). Held on one condition: the 155w Dual-Failure draft from 10-29 needs to be confirmed as posted or dropped first. Two live Rock drafts at once spends the thread. Also `.lnkd.in` and `cxbom.org` links cannot be fetched from this sandbox, so the source rule fails and any draft is **UNVERIFIED-SOURCE** until you read them. Draft below is ready if the 155w went out more than 24h ago. |
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

### Rock Lambros (send only if the 155w DFM draft is closed)

**QUESTIONING, 107 words, UNVERIFIED-SOURCE**

```
The pin is the right control and most tools skip it, so credit for naming the gap in your product. But the 200 characters aren't the thing I'd fix first.

A pin proves a definition hasn't changed since somebody approved it. It doesn't prove anyone read it. A definition malicious on day one carries a valid pin, and your post says approval is the only defence.

The number you say you haven't measured is worth publishing. Seed known-bad definitions into the approval queue at a rate you know, then report how many a reviewer caught, with the sample size.

An approval nobody has measured is a click.
```

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
