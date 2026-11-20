---
deliverable: comment
id: 2026-11-12_reply_tim-zlomke-score-the-refusal-not-the-outcome
date: 2026-11-12
audience: public reply to Tim Zlomke in this account's own post thread
status: ready
approved: no
warm: yes
profile_checked: 2026-11-12 from his two replies and the lineage page he linked earlier. Tim Zlomke works on runtime AI governance, founded Moral Clarity AI and is managing partner of Neurovia Dynamics, and describes his framework as T zero to delta N to T n. Second exchange today: he accepted the age-versus-change distinction, said Harmonic already examines freshness in other bounded controls, refused to designate a new examination before checking existing coverage, and closed warmly. The reply therefore does not push for a new specimen, which would be asking him to spend work to prove something he has already conceded, and gives him the criterion that makes the existing coverage scoreable instead.
thread: whether authority evidence that ages out is handled as a failure mode distinct from authority that changes
premise_checked: checked: his claim that freshness and expiration are already examined in other bounded controls is taken as stated, because the examination records for those controls were not published in the lineage page that he linked earlier today and there is nothing to read. The reply does not dispute it and does not depend on it: it applies equally to a control that exists and to one that would have to be built.
sources_read: none: his reply carries no link. The lineage page and its persistence record were read earlier today for the first reply and are recorded in `2026-11-12_reply_tim-zlomke-age-rather-than-change.md`, along with the reason the manifest could not be recomputed here.
---

## Reply, paste as is

Then I would not ask for BS-006 either. Point the freshness controls you already have at the ageing specimen and score them on one thing: does the refusal name the age and the window it was judged against, or does it just say the evidence was not acceptable?

A control that rejects stale evidence but records only "refused" cannot tell anyone afterwards whether it judged the age or failed to parse a field, and those two outcomes look identical from outside.

There is a variable hiding in it that is worth fixing before you run: which clock. If the window is measured against the receiver's own time rather than the timestamp carried by the evidence, a drifted clock turns stale into fresh, and the specimen passes for the wrong reason.

## Why this reply rather than a push

He conceded the point and then said he would not designate a new examination before checking what already exists. That is the correct order, and asking him to constitute a BS-006 anyway would be asking him to spend work to prove something he has already agreed with.

So the reply moves from the specimen to the acceptance criterion, which is the thing that survives whether or not existing coverage turns out to exist. If the control is already there, the criterion tells him how to read it. If it is not, the criterion is the specification for the next one.

The clock point is the part I would keep. Freshness is a comparison against a clock, and the interesting question is whose. A receiver that measures age against its own time is measuring its own drift, and a system can pass a staleness test while being wrong about every timestamp it holds.

## What I am not doing

No third restatement of the paired-control argument. No asking for the freshness examination records, which are his to publish and not mine to demand. Nothing about BS numbers as if they were mine to assign, which was his point and it was a fair one.

## If he replies

Under R38 a reply is owed the same day. If he says the freshness control already records the judged window, the follow-up is the clock: which timestamp the comparison used, and what happens when it disagrees with the evidence. One question, not a framework.
