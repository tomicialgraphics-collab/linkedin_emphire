---
deliverable: comment
id: 2026-11-12_comment_elena-bobkova-the-credentials-nobody-owns
date: 2026-11-12
audience: public, under Elena Bobkova's post, first degree connection
status: ready
approved: no
warm: no
profile_checked: 2026-11-12 from the post itself. Elena Bobkova is a first degree connection, a J.D. and LL.M., works in AI governance and cybersecurity as a lead auditor, teaches as professor of practice in law and compliance, and uses her farm as an AI security case study. She spoke on the second day of Genworth's annual AI risk summit for the second year running and says so in the post. The comment says nothing about her beyond that, and makes no claim about the talk itself, which was not published.
thread: her talk on the leading cause of security incidents in 2026 and 2027, with an open invitation to guess in the comments
premise_checked: opinion: the post reports a talk and asks readers to guess its conclusion, so there is no external claim to verify. Her three hints are the whole brief, that the cause is only indirectly about AI, that its scale is massive, and that even the top 5% of organisations in that discipline struggle with it. The comment is a guess offered against those hints and says so.
sources_read: read: the Genworth company page she tags, 2026-11-12, which returns a public record only, insurance, a thousand to five thousand staff, NYSE GNW, and nothing about the summit. The tagged people are individuals thanked by name and their profiles were not opened, because the comment makes no claim about any of them. No article, deck or write-up of the talk is attached, so the guess rests on the hints in the post rather than on anything she presented.
---

## Comment, paste as is

My guess, before the reveal: the credentials nobody owns. Service accounts, API keys, OAuth grants, and now the ones minted so an agent can act.

Each of those got created to solve a problem that week. Almost none has a retirement event, because access reviews are built around people, and people at least resign. A token doesn't.

That fits your hints for me. It is only indirectly about AI until the agent needs to do something, and the cheapest way to let it do something is another credential. The scale isn't a breach scale, it is a count nobody has: the number of ways into the environment that no human logs in with. And the top 5% wobble on it for a reason that isn't effort. Their reviews ask who has access. Nothing asks what can authenticate.

If that isn't the answer, I would still like to know it. My runner-up is unpatched systems with no owner, and from the outside the two look identical.

## Why this guess

She asks for guesses, so the comment has to commit rather than hedge. The guess is non-human identity because it is the only candidate that satisfies all three hints without strain. It is indirect to AI in the sense that the credentials predate the agents, and the agents inherit them. Its scale is not measured in incidents, which is why nobody quotes it, but in the number of authenticating paths in an estate. And a mature access review programme can be excellent and still miss it, because the review asks a person's manager to confirm a person's access.

The line about what the review does not ask is the one worth reading twice. It is the reason the top 5% is a hint rather than a boast: effort is not the missing ingredient, and neither is tooling they already own.

## The other candidates, and why they lose

Shadow AI is the obvious one and it is too directly about AI to fit her hint. Third-party and vendor risk has the right scale and the wrong shape, because it is well covered in audit and she would not call it a thing nobody talks about. Unpatched legacy systems fit the hints and are the runner-up, named in the last line so a wrong guess still lands somewhere. Misconfiguration fits the scale and not the maturity hint, since it is the one thing a top decile programme does measure.

## If she replies

Under R38 a reply is owed within the day. If she says the answer is agent credentials specifically, the follow-up is the offboarding question: what event retires a credential that no person ever held. If she says third-party or supply chain, concede the guess and ask which of her audit cases made the scale visible, since that is the part a reader cannot get from the slide.

No link, no pitch, no mention of the farm or the memes. She invited an answer to a technical question and the comment is only that.
