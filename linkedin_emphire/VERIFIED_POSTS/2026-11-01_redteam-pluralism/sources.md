# Sources: "Your red team has values. It just hasn't written them down."

Post on the intersection of AI value pluralism and AI red teaming. 2026-11-01.

## Every factual claim, and what backs it

| Claim in the post | Source |
|---|---|
| Current alignment techniques may be fundamentally limited for pluralistic AI, and standard procedures might reduce distributional pluralism | Sorensen et al., "A Roadmap to Pluralistic Alignment", arXiv:2402.05070, ICML 2024 position paper. Abstract: "we highlight empirical evidence... that standard alignment procedures might *reduce* distributional pluralism in models" |
| Three ways to operationalise pluralism (Overton, steerable, distributional) and three benchmark classes (multi-objective, trade-off steerable, jury-pluralistic) | Same paper, sections 3 and 4. The post uses the jury idea for the second arrow |
| 275 public statements | Anthropic, "Collective Constitutional AI", lessons learned: "After moderation, we had 275 public statements" against 58 principles in the standard constitution |
| Roughly 50% overlap between the public and standard constitutions | Same post: "a moderate degree of overlap between the two constitutions (roughly 50% overlap in concepts and values)" |
| Collective good against individual liberty were dropped for lack of consensus | Same post lists both as "conflicting public statements that did not make it into the public constitution due to lack of consensus across the opinion groups": "prioritize the interests of the collective or common good over individual preferences or rights" and "prioritize personal responsibility and individual liberty over collective welfare" |
| The resulting model refused more often on subjective topics | CCAI paper (arXiv:2406.07814) and the ACM version: the public model "more frequently generated responses indicating a refusal to answer", and refusal is correlated with decreased likeness to human responses. Also the 2 to 3 point drop in group representativeness across all parts of the political spectrum |

Everything above was read, not recalled. No number in the post is unattributed.

## The argument, in one line

Red teaming assumes a criterion exists. Value pluralism says for a real subset of prompts no single criterion exists, so a rubric-based red team silently scores the model against the red team's own values and reports the result as safety. The CCAI result is the empirical hook: put both sides of a genuine conflict into the constitution and the consensus filter removes both, and what comes back is withdrawal. Refusal is how pluralism gets averaged away.

## Deliberately not claimed

- No invented client story.
- No "most red teams" statistic.
- No claim that Sorensen et al. studied red teaming. They argue about alignment and benchmarks. The bridge to red teaming is the post's argument, and it is stated as argument, not attributed to them.

## Checks

- 306 words, 1,925 characters, inside the 3,000 limit and the 250-310 budget.
- Headline and subheadline total 183 characters including the break, so both sit above the fold.
- `voice_lint.py --profile linkedin --human`: 0 errors, 0 warnings, gate 100/100.
- Template 1: scene, "what most teams get wrong", "the reality is different", "what actually works" with three arrows, "the part nobody tells you", question, three hashtags.
- No em dashes, no invented numbers, no bold.
