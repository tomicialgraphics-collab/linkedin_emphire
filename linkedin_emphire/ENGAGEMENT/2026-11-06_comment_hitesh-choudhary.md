---
deliverable: comment
id: 2026-11-06_hitesh-choudhary-twil-8b
date: 2026-11-06
audience: public
status: ready
approved: no
warm: no
profile_checked: 2026-11-06, Peerlist resume, X profile and the explainx instructor list. Hitesh Choudhary, full time YouTuber since leaving corporate, founder of Chai aur Code and of LCO (acquired), ex-CTO at iNeuron, Senior Director at PW, two channels over 1M and 700k, teaches web and AI in Hindi and English. His audience is learners who run things on their own laptops, and his own posts close on a Hinglish line.
thread: his post on webAI open-sourcing TwIL-8B, an 8.8B reasoning model built on IBM Granite 4.2 8B, non-commercial licence, Q4 GGUF about 5 GB, 128K context, with the two flavours balanced and verbose
---

# Comment on Hitesh Choudhary's TwIL-8B post, 6 November 2026

He did the two things a model post usually skips: he said the benchmark scores are the vendor's own,
and he said the licence is non-commercial. His closer is a joke about RAM. The comment should be
useful to the people who will actually run the command he gave, and it should not lecture him about
benchmarks, because he already flagged their provenance.

## Draft, paste as a comment

Good on you for flagging the licence and saying the scores are theirs. Rarer than it should be in these
posts.

For anyone running the 10 minute test, two things worth doing with it.

Run the same bug through balanced and verbose and compare the traces, not the scores. If verbose
spends 20k tokens reaching the same patch, the extra thinking bought confidence, not accuracy. A
longer trace is not more work.

Then put one fact 30k tokens deep and ask for it back on the Q4 and on the bf16. Quantisation tends to
cost long context recall before it costs a maths step, so the small copy can feel fine in the demo and
be weaker at the one job the 128K window exists for.

Your RAM line is the honest bit. Five gig of weights plus the KV cache at 40K is where the laptop
gives up, not the model.

The card says what it can do. The quant says what it kept.

## Why this shape

- He flagged the vendor numbers himself, so the comment does not repeat the warning. It gives his
  audience something to run instead.
- Two tests, both cheap, both on the model he shipped in the post. Nothing needs a second machine.
- The trace comparison is the point an evaluation engineer can make and a tutorial audience can still
  act on. It also quietly answers his closing question about small local versus big hosted: the
  question is not size, it is what the quantisation kept.
- The RAM paragraph meets his own joke on the merits without imitating his register. Never write
  Hinglish back at him.
- Ends on a statement. No question, no link, no offer.

## Posting notes

- Comment inside the first hour. This is a high volume account and the early comments are the ones
  that get read.
- If he replies, the follow-up is one line, not a second essay.
- Nothing about clients, the benchmark or the review work. This thread is about a model on a laptop.
