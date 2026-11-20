---
deliverable: comment
id: 2026-11-09_comment_anthony-alcaraz-cost-per-task
date: 2026-11-09
audience: public
status: ready
approved: no
warm: yes
profile_checked: 2026-11-09 from public sources, since LinkedIn profile pages return 403. Anthony Alcaraz is a GTM Agentic Engineering Lead at AWS, co-author of Agentic GraphRAG (O'Reilly), formerly a startup CTO, with AI work at L'Oreal and in the public sector. He runs a well read GraphRAG series and writes dense, cited breakdowns of papers, so the post is his own reading of primary sources rather than a repost. Second degree. The role is go-to-market, which means the technical register of the post is deliberate and the comment should match it rather than pitch anything.
thread: his post decomposing agent cost into three layers, tokens per task set by the prompts and tools, the model layer that picks who answers, and capacity that sets how the bill scales, using Revolut's blended cost falling from $1.49 to $0.49 per million tokens, Airbnb's fine tuned 2B classifier matching frontier accuracy at about one percent of the frontier API bill, and a harness search paper that cut cost per task 42 percent with the model unchanged. He closes by asking for cost per token, token split and tokens per task side by side.
verified: the figures used are his, attributed to his sources, and the comment adds no new number. The two claims it does make are about mechanism: that step count varies with model choice, and that the cost of matching frontier accuracy with a fine tune is carried by the labelled decisions rather than by tokens.
---

# Comment on Anthony Alcaraz's cost-per-task post, 9 November 2026

## Why this angle

The comment section is ninety-six comments of agreement, most of them one sentence restating one of his beats. Nothing there will be remembered.

The post is a decomposition, and decompositions have a habit of hiding the term that moves. His three layers explain what a finished task costs given a fixed definition of the task. Swapping the model is the one intervention on his list that changes the definition, because an agent's step count is a property of the model's planning, not of the work. That is a real gap rather than a quibble, and it sits inside his own frame.

The second beat is the one the meters cannot see: what replaced the token bill when the 2B model matched frontier accuracy. His own source says the answer, labelled decisions, and labels are the asset that decays.

## Comment

The decomposition holds, with one addition that changes the comparison: the model choice moves the denominator as well as the numerator.

A classifier has a clean task boundary, one listing in, one verdict out. An agent doesn't. The same job takes four steps or nine depending on how the model plans, and the cheaper model that fails a little more often spends the difference on retries. So the number to compare across models is steps per completed task, not tokens per task, and the completion rate has to come from the same suite for both.

The other thing the meters miss. The 2B model matched frontier accuracy because it was trained on Airbnb's own labelled decisions, so the recurring cost moved from per token to per relabel. Labels age with the policy they encode, and that bill behaves like capital spending while both meters read it as zero.

## What not to say

No restatement of the three layers, no agreement paragraph, no mention of my own work or of anything for sale, and no question at the end. He asks for numbers in the closing line, so a question would be answered rather than remembered, and the comment should leave him with a term to add rather than a reply to write.

## Held for a later turn

If he replies, the interesting extension is how a fixed threshold on a frozen model behaves once the input distribution moves, since the score lets a team set the cut off and nothing in that arrangement tells them when the cut off has gone stale.
