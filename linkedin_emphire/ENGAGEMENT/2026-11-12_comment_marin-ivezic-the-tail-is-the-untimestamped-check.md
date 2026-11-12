---
deliverable: comment
id: 2026-11-12_comment_marin-ivezic-the-tail-is-the-untimestamped-check
date: 2026-11-12
audience: public, under Marin Ivezic's post
status: ready
approved: no
warm: no
profile_checked: 2026-11-12 from the post, the blog link and the author note on the article. Marin Ivezic is CEO of Applied Quantum, runs QuantumAcademy.com for training and certification, and writes at PostQuantum.com. His profile line and the article's author note both say former Fortune Global 500 CISO and CTO and a Big 4 partner. The comment says nothing about him beyond that, and nothing about the series as a whole, only Part 1 which was read.
thread: post-quantum migration, and which signatures the break can actually rewrite
premise_checked: checked: the post's claims against Part 1 of the series at postquantum.com, 2026-11-12. Shor breaks RSA, finite-field Diffie-Hellman and elliptic-curve signatures and key exchange; AES survives, preferably at 256 bits; SHA-2, SHA-3 and HMAC survive with margin; Mosca's inequality is x+y>z with all three as estimates and only the first two under the reader's control. The comment builds on his own sentence that trusted timestamps, transparency logs and append-only records still prove what existed before the break, so a bare signature check is the exposed case.
sources_read: read: the whole of Part 1, all three chunks, on 2026-11-12, plus the short link, which passed through a LinkedIn interstitial and landed on the same article. The article is long, dated May 2021 and updated July 2026, so its NIST 2024 standards dates and its Mosca wording were read rather than assumed. No other link is attached to the post.
---

## Comment, paste as is

Your last paragraph is where I'd put the effort, and I would not sort it by asset criticality. What sets the tail on a signing key is the last check of something it signed that carries no trusted timestamp, because that is the check the break can rewrite. Firmware on a device that verifies a signature and nothing else is the case that runs to 2034. The same key, where every release it signed is timestamped, is a much shorter problem.

The two cases tend to sit on the same row of the register, because the record says which key signed what and not whether the verifier on the other end consults a timestamp.

Asking for that distinction is cheap, and the answer belongs in writing: usually a handful of devices in the field doing bare signature checks that nobody owns. Nobody wants that list. It is also the only one of the two you can fix this quarter.

## Why this one

The post is the opening of an eleven part series, so a comment that summarises it back adds nothing. What it does not do is turn its own distinction into a sort order. He is precise that timestamps, transparency logs and append-only records still prove what existed before the break, and that bare signature verification is where the exposure sits. That sentence is the useful part, because it means the migration order is not the asset register.

A test I would apply to any post-quantum plan: for each signing key, find the last verification of something it signed that no timestamp protects. That date is the one that has to beat the machine. A key that signed every release for a decade is a short problem if every one of those releases carries a trusted timestamp and a long one if a single fielded device checks the signature alone.

It is also the column an inventory usually lacks, which is why the two cases end up with the same priority in the same spreadsheet.

## Not a repeat of the 7 November comment

There is already a comment to him in this folder, on his quantum-finance post, which argued that a crypto register is an existence test and that completeness needs reconciliation against a population counted elsewhere. That one was about whether the inventory is complete. This one takes completeness as given and asks what column the inventory is missing, which is a different question and one his own article raises by pointing at timestamps.

If he answers that his framework's discovery phase already captures verifier behaviour, the reply is that a CBOM describes the algorithm and the key, not the code path on the device that decides whether to look at a timestamp.

## What I left out

Harvest-now-decrypt-later is already his, and better stated there than I would manage. The Mosca estimate argument, that z is unknowable and y is usually guessed, is true and is the obvious comment on any post-quantum thread; it stays out because he says as much himself in the article and the point is not new to his readers.

No link, no pitch, nothing about his course or his consulting practice. One idea about ordering, which is the part a reader can act on before the next part lands.
