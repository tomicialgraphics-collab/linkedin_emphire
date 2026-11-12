---
deliverable: comment
id: 2026-11-11_comment_rock-lambros-the-version-string-lied
date: 2026-11-12
audience: public, under Rock Lambros' post
status: ready
approved: no
warm: no
profile_checked: 2026-11-12 from the post and public sources. Rock Lambros runs RockCyber, is an OWASP GenAI Security Project contributor alongside Scott Clinton and John Sotiropoulos, and posts under #PROMPT2PWN for the Zenity Labs and NahamSec event. His own lines here: the cooldown's documented default is 0, "your protection against a trojan that was up for 11 hours was a zero", and "tell me again how mature your software supply chain program is". He wrote in March that skill marketplaces are npm before lockfiles.
thread: supply chain, auto-update, and what a laptop has to be able to answer afterwards
premise_checked: checked: the Cursor marketplace extension incident, against Cursor's own security notice and Phorion and StepSecurity analysis, 2026-11-12. Live 29 October 2026 from 2:27am to 1:35pm Pacific, versions 2.1.312 and 2.1.313 for Windows and macOS, up to 5,000 users, svc-telemetry key in authorized_keys, reverse tunnel to 134.209.82.225, persistence by LaunchAgent and scheduled task, 2.1.313 reporting itself internally as 2.1.312.
sources_read: read: Cursor's notice as quoted by Help Net Security, the Hardware Busters write-up, the StepSecurity analysis summary, and the daily.dev and implicator pieces, all 2026-11-12. The two claims I use are the internal version string and the environment variable names, both of which appear in more than one account.
---

## Comment, paste as is

The detail I would move to the top: 2.1.313 reported itself internally as 2.1.312. The bump existed only in the repackaged manifest, so for the eleven hours that mattered, any inventory that asked the extension what version it was got a true-looking answer that was wrong.

That turns your cooldown point inside out, correctly. A cooldown protects the next install and says nothing about the laptop in front of you. The question that laptop has to answer is what code actually ran, from which bundle, and when it started. Hash the bundle rather than trusting the version string, and keep that record somewhere the developer's machine does not control.

The other detail worth naming: the payload took the names of up to forty environment variables, not their values. That reads like restraint and is a map, so rotating the values leaves the attacker's inventory of where the credentials live fully intact.

No cooldown protects a fleet you cannot inventory. That is the maturity question, and most programmes answer it on the pipeline and fail it on the laptop.

## Why this one, out of the batch

Every other security post in the feed is either a repost, an event notice or a warning without an artefact. This one has a specific mechanism, two vendor statements and a clean defensive call to action, and its weakest point is the one the author cannot fix himself: a policy for future installs sits beside an unanswerable question about past ones.

The version string detail is the contribution. It is in the reporting, nobody in the thread will have pulled it out, and it is the difference between an inventory that can be wrong and one that can be checked.

## What the other posts got

Skipped as reposts under R39: Hamel Husain on LightTable, Harrison Chase, Michael Bargury, Iyinoluwa Aboyeji, Sara Hooker, Amanda Minnich, Scott Clinton, Ads Dawson, Dr. Rumman Chowdhury's paper promotions, Blossom Affia, Bolaji Adebayo, Haoma Worgwu.

Skipped as out of lane: Hormozi, Patrick Bet-David, Kieran Drew, Tiago Forte, Ruben Hassid, Lenny Rachitsky, Brad Wolfe's finance posts, Dario Melo's robots.

Held, not skipped: Dr. Rumman Chowdhury's own IVO post is the best audience in the batch and it is a crowded thread, and Tarique Smith's evidence book is the closest thing to this account's own thesis. Both are worth a comment on a day when the supply chain story is not live.
