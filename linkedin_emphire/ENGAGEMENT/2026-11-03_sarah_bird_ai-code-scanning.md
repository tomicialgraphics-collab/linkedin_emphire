# Sarah Bird, AI application scanning: comment

Posted three minutes before capture, so this is the early window where a comment gets seen by the author
and by everyone who arrives afterwards.

## What the post is

Sarah Bird, Chief Product Officer of Responsible AI at Microsoft since February 2019, previously led
responsible AI for the new Bing and for GitHub Copilot, founding researcher in Microsoft FATE, co-founder
of ONNX and Fairlearn, PhD at Berkeley. She is announcing code scanning for AI applications in GitHub
Advanced Security, public preview as of 28 October.

The substance, from the changelog rather than the post: scans run on pull requests alongside CodeQL,
flag code paths where untrusted content can reach a model with access to tools, and cover indirect prompt
injection, sensitive information disclosure and excessive agency. It needs an Advanced Security licence,
it is on github.com only, not GitHub Enterprise Server. No general availability date and no false
positive rate at scale have been published.

## Comment, 115 words, lint clean

The gate is the right place for the architecture question: can untrusted content reach a model that
holds tools. That is decidable from the code path, and it is worth blocking a merge over.

What the code path cannot tell you is whether the model obeys the content once it arrives. That is a
property of the run, so the pipeline finding and the runtime evidence have to point at the same span, or
a closed alert and a fixed vulnerability look identical in the pull request.

Which is also how to judge a suggested fix. Encoding the untrusted input closes the finding. It does not
change whether the model can be steered by it.

## Why this and not something else

The temptation on a launch post is to say the shift left is correct and stop, which is what every other
comment will do. The distinction here is narrower and more useful: a static check resolves a question
about structure, and the failure that matters resolves a question about behaviour. Those are different
questions and they need different evidence.

The last paragraph is the pointed one, and it is pointed without naming their screenshot. The changelog
example shows a prompt injection finding in a travel agent with a suggested fix that base64-encodes the
untrusted input. Encoding is not a mitigation for instruction following. A reviewer who accepts that fix
gets a closed alert and the same vulnerability, which is the exact failure mode the whole argument is
about. Saying it as a general test of any suggested fix keeps it a technical point rather than a review
of their product, and it is harder to dismiss than a direct criticism would be.

## One line that was cut

Tempting fourth paragraph:

> Publishing the false positive rate at scale, even a rough one, would do more for adoption than the
> three risk names do.

It is true and it is his own argument, but it turns a technical comment into a request, and the author
is a product executive who will read a request as an agenda. Keep it for a later post, or for a comment
on someone else's analysis of the launch.

## Order

Post the comment in the first hour while the post is still climbing. Do not mention the review, the
twelve-day run, or breaklab in it. If she replies, the reply is the place to be concrete about the
runtime half, not the first comment.
