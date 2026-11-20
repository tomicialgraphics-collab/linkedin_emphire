---
deliverable: comment
id: 2026-11-08_adi-rashkes-queen-of-hearts-vishing-ctf
date: 2026-11-08
audience: public
status: ready
approved: no
warm: yes
profile_checked: 2026-11-08. LinkedIn profile fetch returns 403, so read from cached profile copy, accelerator listing and her own recent posts. Adi Rashkes, co-founder and CEO of SottoAI, continuous adversarial testing for voice AI agents, out of stealth in 2026 as a Deepgram partner, based in Tel Aviv, previously backend at Transmit Security and Mend.io, Reichman University. She writes about the move from cascaded pipelines (speech to text, LLM, text to speech) to native speech to speech, and argues security for voice agents has to be built for voice rather than text filtering. Second degree.
thread: her post announcing the Queen of Hearts Call Center, a vishing CTF for BSidesTLV on 11.11.26, where callers ring AI characters who were told never to share their secrets, and have to talk them into it
verified: BSidesTLV's own announcement of the CTF matches hers on format, date and location. The Social Engineering Community village vishing format is established at DEF CON, including the John Henry competition where AI bots cold-called humans, so the flip to humans calling bots is genuinely new rather than a rename.
---

# Comment on Adi Rashkes's vishing CTF post, 8 November 2026

## Why this one

Voice AI security is the same problem as the rest of this week's work with a microphone attached: an agent is told what
it must not do, and someone tries to make it. She runs adversarial testing for exactly that, so the comment has to be
useful to a person who does this professionally, not encouraging.

She has already made the argument that matters on her own feed, that security for voice agents is not text filtering. So
the comment does not repeat it. It goes at the measurement design, which is a live decision four days before the event
and is the kind of thing a founder can act on immediately.

## Comment

One design suggestion before Wednesday, from someone who spends his weeks on refusal records: score the attempts, not
just the outcomes.

Secret out or not is a binary, and a binary collected at an event is a leaderboard. What carries over into a product is
the middle: the caller who got the bot to hint, to contradict something it had already confirmed, to change its tone.
Each is a crack that never reached the secret, and a CTF can measure them for free while everyone is already on the
phone.

The other half is the bot's own account of the call. If it can't name the instruction it was under and the point where
it bent, the only thing you can score is the leak.

## What not to say

No congratulations-only comment. No pitch for SottoAI's own testing, and nothing that reads as offering a service under
someone else's event announcement. No claim about AI vishing being unbeatable or beaten, because the honest position is
that it depends on the guardrail and nobody has published a comparison.

## Held for a reply

The voice-specific version: in speech to speech there is no clean text boundary for a filter to sit on, and a partial
disclosure ("I can't share that, but the code starts with a four") is a leak with no matching log line. That is her own
argument and she is better placed to make it than I am, so it stays out unless she opens it.

Second held beat: publish the aggregate afterwards, even if it is ugly. A CTF that only produces anecdotes wastes the
run, and a table of attempts by outcome would be cited for a year.
