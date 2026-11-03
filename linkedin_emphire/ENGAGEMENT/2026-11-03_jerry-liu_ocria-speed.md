# Jerry Liu, OCRia-1 10x: comment

## Who he is

Co-founder and CEO of LlamaIndex, Princeton, previously Uber, Quora, Two Sigma, Apple. The detail that
matters here: before LlamaIndex he was at Robust Intelligence, the AI risk company, where he led
engineering for an AI firewall that vetted data before it entered a model. He is not a stranger to
security and evaluation language, so a comment about test design is in his own register rather than
adjacent to it.

## What the post says, and one trap

OCRia-1 was released 22 October as a 4B document-parsing model, a fine-tune of Qwen3.5-4B, claiming 87.4
on ParseBench and 83.5 on olmOCR-bench with 92.9 on tables. This post is the serving optimisation: 285
to 2800 tokens per second on one B200, built from quantization, DFlash2 speculative decoding, kernel
fusion, vLLM changes and seventeen other items.

**The trap.** The technical report measures single-stream decoding at about 4,700 tokens per second with
time to first token excluded, and about 3,000 end to end at the median. The post's 2800 and the report's
4,700 are different measurement bases, not a contradiction. Do not quote either number back at him as if
they disagree, because that is the fastest way to look like someone who did not read the report.

## Comment, 81 words, lint clean

The 10x changes the evaluation, not only the cost. At 2800 tokens per second you can afford invariance
tests that used to be too expensive to run: the same page recompressed, rotated a degree, re-rendered at
another DPI, parsed twice. Identical output every time is a real claim about the parser reading the
document instead of the artifact.

A single score against a fixed transcript cannot see that class of failure. Cheap inference is what makes
the test that can affordable.

## Why this one is worth posting

It takes his number seriously and then puts it to a use he did not claim. An invariance test is a
metamorphic test: the same document under transformations that should not change the interpretation. If
the output moves, the parser is reading the artifact. That is a real and cheap failure class for document
parsing, it is the same argument this account makes about checks everywhere, and the speed improvement is
precisely what makes it affordable at scale. It is a compliment to the work that is not a compliment to
the post.

No criticism of ParseBench, even though a company publishing a benchmark it owns is the exact structure
this account has spent a week criticising elsewhere. He built the firewall product at Robust Intelligence.
He knows. Saying it here buys nothing and costs the thread.

## Where this sits among today's six drafts

Post two, hold the rest. In order of what actually serves the November goal:

1. **Sarah Bird.** Time-sensitive and the closest to the lane. Her post was minutes old when captured.
2. **Jerry Liu.** Technical, credible, and the audience is enterprise document AI, which is a buyer
   audience rather than a follower audience.
3. **Hamel Husain.** Warm, and the same subject as this one. Do not post both in the same hour.
4. **Neil Sahota.** Good thread, governance audience, low commercial value.
5. **Rock Lambros.** Warm repeat surface, keep for tomorrow.
6. **Allie Miller.** Reach only, and the author has already mocked her comment section.
