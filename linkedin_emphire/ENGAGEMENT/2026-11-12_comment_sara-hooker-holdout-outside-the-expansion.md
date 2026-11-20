---
deliverable: comment
id: 2026-11-12_comment_sara-hooker-holdout-outside-the-expansion
date: 2026-11-12
audience: public, under Sara Hooker's post
status: ready
approved: no
warm: no
profile_checked: 2026-11-12 from the post and the company site it links to. Sara Hooker describes herself as co-founder of adaption with a PhD in computer science. Her post announces Expand, a feature of Adaptive Data, and links to the adaptionlabs.ai home page. The comment says nothing about her research or her company beyond what the post and that site already say.
thread: synthetic expansion of small seed sets, and what the resulting dataset can and cannot prove
premise_checked: checked: the Expand claim, against the post and the adaptionlabs.ai home and Adaptive Data pages, 2026-11-12. Expand claims to take 10 data points to a 100,000-row training-ready set, optimizes task, domain and general-purpose data in the sample, hands the mix to AutoScientist, and that the data is commercially licensed for training. Its Adaptive Data page describes Invent, Forge, Blueprint and multilingual expansion and publishes no evaluation method, so the comment asks about the holdout rather than asserting that it is wrong.
sources_read: read: adaptionlabs.ai home page and the Adaptive Data page, both 2026-11-12, reached from the website link on the post. A permalink on the adaption company post requires a login and returned 403, so the comment rests on the founder's post and the public site, which carry the same product claims. No other link is attached.
---

## Comment, paste as is

The number I want next to the 100,000 is the score from the model trained on the ten.

Volume is what Expand solves, and that was a real problem to have. Whether the model got better at the task is a different measurement, and the two only agree if the held-out set stayed outside the expansion. When a test row is a sibling of a generated row, the model has effectively seen it, and the gain you're reading is the generator agreeing with itself.

Doing it is unglamorous: keep real data aside, never run it through Expand, and split at the document or the source rather than the row. Ten rows can't seed that test set, so somebody has to hold it back before the project starts.

That ordering is the part I'd argue about, because it is a lot easier to agree to before the 100,000 exists.

## Why this one, and what it is not

Her post is a launch, and a launch thread fills with congratulations and one line of "this changes everything". The useful thing a stranger can add on day one is not admiration, it is the question that decides whether the customer ever gets the benefit they think they bought.

This is a narrow point and not a criticism of the product. Expanding ten rows generates variations of those ten rows. That is what makes it work, and it is also why a randomly split evaluation set will contain siblings of training rows, which turns a generalisation score into a consistency check on the generator. The fix costs nothing at the point of sale and is nearly impossible to retrofit: the client's own rows stay out of the expansion, and the split is drawn at the document or the source.

Two angles I passed over. Provenance, meaning whether generated rows carry the same commercial warranty as the seeds, is a real question but belongs in a contract conversation rather than a comment. Coverage is the other one: ten seeds cannot contain the rare case a client will be judged on. That is the strongest version of my usual argument and it would have made this a second idea, so it is out.

## Why not a reply

Nobody in the thread has asked a question worth answering, and the 18 hidden comments were not read, so there is nothing here that R38 makes owed. One comment, no link, no pitch.
