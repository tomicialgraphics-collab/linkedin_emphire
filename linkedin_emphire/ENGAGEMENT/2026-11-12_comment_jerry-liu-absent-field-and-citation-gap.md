---
deliverable: comment
id: 2026-11-12_comment_jerry-liu-absent-field-and-citation-gap
date: 2026-11-12
audience: public, under Jerry Liu's post
status: ready
approved: no
warm: no
profile_checked: 2026-11-12 from the post and public sources. Jerry Liu is co-founder and CEO of LlamaIndex. The post moves the company from framework to applied research lab for document OCR, names ParseBench, ExtractBench and ExtractBench Pro as its own benchmarks, OCRia-1 as its model, and closes on the research page. The existing thread already carries three substantive comments: Ahmad Abbous on holding out whole templates, M.T. Ramkrushna on abstention and correction rate, and Dr. Joel He on evidence an auditor can check.
thread: document extraction benchmarks, and which failures the headline scores hide
premise_checked: checked: the ExtractBench design, against the paper abstract on arXiv, version 2 of 5 August 2026, 2026-11-12. It scores value F1, record completeness at scale, word and page level grounding F1, and measured cost, over 4,869 pages across 370 documents, eight domains and 67 document types. I did not open the ParseBench or ExtractBench Pro papers and make no claim about them.
sources_read: read: the llamaindex.ai research page, the ExtractBench abstract and its stated metrics, and the five comments under the post, all 2026-11-12. The linked short address resolved to the research page; no paper PDF was downloaded.
---

## Comment, paste as is

Completeness is the number I'd poke at, given what it does on the documents that actually matter. Where the purchase order number doesn't exist, a model that invents one scores better than a model that returns nothing, and the invented value arrives with no warning attached to it.

I don't think you can weight your way out of that, and it isn't a criticism of the corpus. What I'd want is the row on its own: field absent, value returned anyway. You already have to mark absence to score completeness, so it shouldn't cost a new annotation pass.

Same reason I'd take a no-citation count beside the grounding average. A citation at the right page and the wrong line passes the score and fails the auditor.

Publish that and I'll stop asking every vendor for a pilot before I believe anything they tell me about supplier invoices.

## Why it is written this way

The first draft of this had a frame: "two rows I would want beside the headline", then "the first is", then "the second follows Joel's line". The owner read it and said it sounded generated. It did. The tells were the list scaffolding, the mirrored clause about systems that know what they do not have against systems that guess fluently, and a closing aphorism about failure that costs money quietly.

What replaced it starts inside the problem, uses contractions, admits a limit ("you can't weight your way out of that"), and ends on something a person would actually say to a vendor. One idea carries it, with the citation point as an aside rather than a second item on a list. Shorter, and it sounds like somebody who has read supplier invoices.
