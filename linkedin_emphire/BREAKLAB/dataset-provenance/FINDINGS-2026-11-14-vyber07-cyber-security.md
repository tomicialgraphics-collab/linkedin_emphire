# Findings: Vyber07/cyber-security, read 14 November 2026

Everything below is taken from the dataset page as published, including the parts that only appear once access is granted. Nothing in the repository was downloaded, opened or executed. The file tree was not pulled, so the byte figures here are the card's own and the audit in `report.json` is pending that step.

## The short version

A 20,702-download dataset, with nine models fine-tuned on it, whose description contradicts itself five times about its own size, whose files are a fifth unusable by the card's own count, whose licence cannot cover what is inside it, and two of whose files the platform has flagged as unsafe. None of that is a claim about whether the content is any good. Whether anyone read it before publishing is the question it answers.

## 1. Five figures for one quantity

| Where it appears | What it says |
| --- | --- |
| Card overview | 16 GB |
| Card statistics table | ~95 GB |
| File listing, total file size | 95 GB |
| Dataset metadata header | under 1K |
| Dataset viewer | 1 row, 1 split (`test`) |

The last two are the platform's own parsing, not the uploader's prose. The viewer shows a single row because the single visible record is one nested object of reference material, and the metadata reports the size class it inferred from that. Those two agree with each other and disagree with every sentence the uploader wrote.

Six times between the smallest uploader claim and the largest. That is not a rounding difference and it is not a disagreement about units. What this is, is a page written in sections, at different times, by somebody who never compared them.

## 2. A fifth of the repository does not parse

507 files, 394 of them valid JSON, by the card's own count. Which 113 are not, or what they are, or why, goes unsaid. The viewer's failure to render anything beyond one row is consistent with that: the platform tried to load 507 files, got 394, and showed what it could.

For anyone writing a loader, this is the first hour of the job rather than a footnote. A glob over the repository returns 507 paths and throws on the 395th usable one, and the exception names a file, not a cause.

## 3. Two files the platform flagged as unsafe

Above the card, in the platform's own chrome: "This dataset has 2 files scanned as unsafe." That banner is the only sentence on the page not written by the uploader.

Nothing in the card mentions it, names the two files, or says what tripped the scan. Whatever it was, a pipeline that clones the repository wholesale inherits it, and the 20,702 downloads suggest a lot of wholesale cloning.

This is the single strongest reason not to clone for analysis. A file listing is all the audit in this folder needs, and a listing cannot hurt you. A clone needs the files, which can.

## 4. The licence cannot cover the contents

The card says Apache 2.0. The same card says the content comes from HackTheBox, TryHackMe, PortSwigger Web Security Academy, SANS and VulnHub, among others.

Three of those prohibit redistribution in terms that leave no room: PortSwigger's 7.4 and 7.7 (personal use only, no commercial use or sharing without a licence), Hack The Box's 11.2 and 11.4(a) (a personal licence for use within the Services, no copying or distribution), and TryHackMe's 3.1 (personal use only, no copying or aggregation for any commercial purpose). The clause texts and URLs are in `UPSTREAM-LICENCES.md`.

MITRE ATT&CK is the one source here that does permit commercial use, and it attaches a condition: every copy must reproduce the copyright designation and the licence text. The required sentence does not appear in the card or anywhere visible on the page.

So the Apache 2.0 line is not a licence over this content. What that line does is label a container whose contents belong to other people, four of whose terms it contradicts.

Nine models have been fine-tuned on it. That is nine models whose training data provenance nobody upstream of them can vouch for, published by people who read a line that said Apache 2.0.

## 5. "PhD-level" is a field, not a standard

Records carry `"level": "PhD"` and `"task_type": "phd_level_reference"`. These are strings inside the metadata the uploader wrote about their own files. There is no external body that grades a JSON record as doctoral, and the phrase appears twice in the card's own description of itself ("most comprehensive cybersecurity knowledge base ever assembled", "PhD-level depth").

This is the least important finding and the most predictive. A page that grades its own homework in a metadata field is a page whose other numbers were not checked either. The five sizes are the same habit.

## What this does not establish

Nothing here establishes that the content is inaccurate, stolen in a legal sense, or dangerous. Copyright standing is a legal question and this is not legal advice; it is a reading of published terms.

Nor does any of this establish the real byte count. That needs the file tree, which is one API call and is the next step in `RUNBOOK.md`.

Whether the nine downstream models are compromised stays open. What closes is narrower: whoever trained them had no more information than a card that contradicts itself, and no way to check.

## What would change the verdict

A file tree that sums to 95 GB would remove one of the five contradictions and leave four. A licence grant from each blocked upstream would remove the fourth. Removing the unsafe flag means identifying and deleting those two files. None of that happens in a card, and none of it has.

## Why this is worth writing up rather than tutting at

This is the ordinary state of a popular training corpus: assembled by scraping, labelled by the person who scraped it, licensed by wishful thinking, and consumed at scale. Ten minutes of checking catches it, needs no download, and almost nobody spends them. That is the whole reason it is worth having a tool.
