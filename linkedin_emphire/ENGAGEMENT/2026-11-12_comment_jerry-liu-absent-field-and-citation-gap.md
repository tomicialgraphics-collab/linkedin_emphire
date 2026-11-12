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

Two rows I would want beside the headline, and both are cheap to add to a benchmark already curated at this scale.

The first is fields that are genuinely absent. Completeness rewards a filled field, so on a document where the purchase order number does not exist, the safe answer scores worse than the plausible one. Reporting that slice separately, field absent and a value returned anyway, would separate the systems that know what they do not have from the systems that guess fluently.

The second follows Joel's line about evidence an auditor can check, because that is where the citation gap decides it. Word and page F1 is the right unit, and the number an auditor needs is the share of extracted values carrying no citation at all. Near misses belong beside it: a citation pointing at the right page and the wrong line reads as evidence and is not.

Ahmad's template holdout and Ramkrushna's correction rate complete the picture. Of the lot, the absent-field row is the one a buyer would act on, because it is the failure that costs money quietly.

## Why these two rows

Both are additions to metrics the paper already reports rather than replacements for them, which is the only kind of comment that survives the author reading it. Neither criticises the corpus, the curation, or the vendor position, because on the evidence in the paper all three are stronger than most work of this kind.

The absent-field row matters because completeness and accuracy pull opposite ways on exactly the documents that reach production. The citation gap matters because a grounding average can be high while a meaningful share of values carry no source at all, and the average hides that the way an average always does.
