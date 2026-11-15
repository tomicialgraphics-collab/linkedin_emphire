---
deliverable: doc
id: 2026-11-15_upwork-daily-filter
date: 2026-11-15
time_checked: >-
  checked: 2026-11-15 10:44 WAT, read from the system clock before this file was opened for gate.
audience: internal
status: ready
approved: no
premise_checked: >-
  checked: every search string and URL in this file was run against upwork.com between 10:37 and 10:44 WAT on 15
  November 2026, and the counts beside each one are what that search returned. The filter parameters were tested
  individually. One of them failed the test and is named as failed rather than quietly dropped.
sources_read: >-
  read: eleven public job searches on upwork.com with their facet counts, and the seventeen postings coded in
  2026-11-15_job-feed-corpus_seventeen-posts.md.
---

# The daily filter: five saved searches, tested

## How to load them

Paste the URL into a browser where you are signed in as yourself. Set nothing else. Then use the save control on the
results page so it appears in your saved searches, and leave notifications on for it. If your view calls that control
something other than "Save search", it is the only save affordance on the page.

Do not type the strings into the search box by hand and do not add quotes or `AND` or `OR`. Boolean strings are
executed as literal words here, which is how `no AI policy` once returned SEO writers. The URLs below carry the plain
terms and nothing else.

## The five

| # | name | exact string | URL to paste | filters | returned at 10:44 WAT |
|---|---|---|---|---|---|
| 1 | Money | `penetration test` | `https://www.upwork.com/nx/search/jobs/?q=penetration%20test&contractor_tier=3&t=1&sort=recency` | Expert, Fixed-Price, Newest first | 10 |
| 2 | Lane | `AI security` | `https://www.upwork.com/nx/search/jobs/?q=AI%20security&contractor_tier=3&sort=recency` | Expert, Newest first, hourly and fixed together | 112 |
| 3 | Precise | `prompt injection` | `https://www.upwork.com/nx/search/jobs/?q=prompt%20injection&sort=recency` | Newest first, all levels | 6 |
| 4 | Standard | `OWASP` | `https://www.upwork.com/nx/search/jobs/?q=OWASP&sort=recency` | Newest first, all levels | 7 |
| 5 | Adjacent | `MCP server` | `https://www.upwork.com/nx/search/jobs/?q=MCP%20server&contractor_tier=3&sort=recency` | Expert, Newest first | 11 |

Search 1 is the one that pays. It is the only filter that returns fixed-price, expert-level, report-shaped work in
volume: of the 10 it carried, five sat in the $1K to $5K band and three above $5K, and four came from clients who have
never hired. Those are the $2,000 and $2,500 report-plus-retest buyers.

Search 2 is the market. It is too broad to read whole, which is why it is sorted newest: you check the top ten and
close the tab. Expert and fixed-price together would leave 31, so the type filter stays off on this one.

Search 3 and search 4 are small on purpose. Between them they carry the buyers who already know what they want, which
is the cheapest conversation on the platform.

Search 5 catches the agent-security work that never uses the word security in the title: OAuth, per-tool permissions,
audit logging and field masking are all inside those scopes.

## Settings that matter, and one that does not work

Sort by newest on all five. Any other order buries the post you can still be first on.

Leave the budget filters empty. Five of the seventeen postings I coded published no number at all, and a minimum
filter silently deletes them.

**Do not use the client-history URL parameter.** I tested `client_hires=1` expecting the 62 no-hire clients in AI
security and got 16 unrelated postings: a trucking app and a website rebuild. The query broke rather than filtered.
Set that filter in the interface on the card instead, by reading the client's hire count, which is visible without
opening the post.

## When to run them

Upwork's own hire pages state that the average time from a job post to its first proposal is three hours. The buyers in
this set are mostly US-based, so their posting day starts around 13:00 WAT. Run the five at **13:30 WAT**, then again
at **19:30 WAT** for the west-coast tail. Ten minutes, both times together. A run at 07:00 WAT is reading the previous
day's posts.

## The four questions on every card

Answer them in order and stop at the first no.

1. Does it ask for a document? Findings, report, audit, assessment, review. If it only asks for a build, skip.
2. Does it name a stack that includes an LLM, an agent, RAG or MCP? If it is web pentesting with no AI surface, it is
   someone else's job at someone else's price.
3. Has the client hired before? A no-hire client is not a warning here; a third of this market has never hired. But a
   client with 10+ hires and one review-free proposal is a different conversation, and worth the extra paragraph.
4. Is the budget inside the band, or unpublished and plausible? Unpublished is normal. A published $5 to $30 an hour
   is a no.

## What to stop running

`red teaming` returns 16 postings and most of them are a Red Hat advertisement, a Google Ads consultant matched on
"red flags", an accounting firm and a chemist. `LLM red team`, `jailbreak` and `eval harness` return zero. The
plain string `red team` was not measured on its own, and its results would be dominated by the same colour match. `LLM evaluation` and `AI
evaluation` are real but gated: the money at the top of that lane requires US residency and the bottom is annotation
at $5 to $30. Keep them out of the morning.

## The one number to watch

Sends, not views. The filter is worth nothing if it produces reading. Two sends a week from search 1 and one from
searches 3 and 4 is the target, and anything beyond that is volume for its own sake. With 84 Connects left, a send
that is a genuine fit is the only kind worth making.
