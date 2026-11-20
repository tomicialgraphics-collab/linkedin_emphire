---
deliverable: dm
id: 2026-11-20_dm_marvin-no-key-so-the-sample-is-the-plan
date: 2026-11-20
audience: outbound
status: ready
approved: no
recipient: Marvin Percival
premise: >-
  Marvin confirmed that there is no NIPOST key, that live keys need company verification, that cycle one will have to
  run on recorded sample responses from the start, and that he doubts a US company would be granted a key. This reply
  takes the sample path as decided rather than as a workaround, makes the sample faithful rather than invented, puts a
  switch behind it instead of a rewrite, adds a requirement that the app says when the address is a sample, and points
  out that the Nigerian company is the answer to the US company problem.
time_checked: >-
  checked: 2026-11-20 02:42 WAT, read from the system clock before this file was written. That is 21:42 on Thursday in
  New York.
profile_checked: >-
  Marvin Percival, who raised a blocker at midnight rather than at the review, and whose instinct was to say he is not
  sure how else to get around it. The reply does not reassure him; it removes the item from the critical path and tells
  him exactly what to ask NIPOST for.
premise_checked: >-
  checked: the claims about what needs a key, and the doubt about a US company, are his, reported at 02:37, and are
  restated as his rather than asserted as fact. Nothing is claimed about NIPOST's actual process, because it has not
  been read. The requirement added here was written into the amendments document before this message was drafted, and
  its cost is in the same arithmetic.
sources_read: >-
  read: his message of 02:37, pasted by the owner, and CLIENTS/eri/ERI-REQ-v0.4-amendments.md in this repository. No web
  page opened.
---

## Message, paste as is

<!-- gate:body:start -->
Good, that settles one of the two, and better at two in the morning than at the review.

Three things and then it's off the critical path.

Record the sample, don't write one. If we invent the response shape we'll build against an interface that doesn't exist and the day the key lands it's a rewrite. Ask them for the schema, the error codes, the rate limit, and whether valid=false is the only way a lookup fails. A screenshot of one real response is worth more than a day of our guessing.

Build the switch, not the fixture. One interface with two implementations, sample and live, chosen by a config value. Half a day now, a config change later, and no rewrite either way.

And no sample on a screen without saying so. I've added it as REQ-052: when the address comes from a recorded sample, the screen says "sample response, captured on" and the date. Same reason the certificate says what it doesn't prove. If a reviewer finds out afterwards that the address was a fixture, they stop trusting the rest of the demo, and this whole product is the habit of not overstating what it knows.

On the US company worry, you're right, and it resolves itself. The key goes to a Nigerian company, and we're registering one. So this isn't a blocker, it's an argument for doing the registration properly and putting the RC number in the application.

Monday doesn't move. 001 to 005 are untouched, and 006 to 010 run against the sample.

Stele is the other one, and it's now the only thing left that can stop week one. If it can't mount this week, say so today and we agree the development-only session in writing instead.
<!-- gate:body:end -->
