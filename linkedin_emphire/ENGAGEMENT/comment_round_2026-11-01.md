# Comment round: 2026-11-01

Second live round. Round one is `comment_round_2026-10-31.md` and stays open for the Brad
Wolfe reply and the al neitsch comment.

## Entry 1: AI News World, Dario Amodei on per-model profitability

**Surface:** AI News World company page, posted roughly 20 minutes before the paste. Their post
summarises Amodei's example: a model costs $100M and earns $200M, the lab spends $1B training
the next one, then $10B after that. They note he called the numbers hypothetical.

**My read without a comment:** the claim is real and fairly summarised. It is a business story,
not a security artifact, so the ladder does not skip it. There is one angle here that belongs to
this account and nobody else in that comment section will take it.

**Verified:** the example comes from Amodei on the Cheeky Pint podcast with John Collison. He
walks it year by year: a $100M model earns $200M, $1B goes into the next run, that one earns $2B,
$10B into the next. Company-level losses of $100M, then $800M, then $8B. He calls it a
"cartoonish" example and says the numbers are not Anthropic's actual finances. Multiple
transcripts agree on the arithmetic, so the post's version is fair.

### Draft: QUESTIONING, 118 words, gate 100/100

> Fair reframe, and he does flag that the numbers are a cartoon. The part that isn't: every
> cycle the training run gets ten times bigger, and the testing budget doesn't move with it.
>
> Capability is what sells seats, so a lab can defend $10 billion on it. Evaluation stays a
> rounding error against capex, and the buyer carries the difference when the model ships
> before anyone finished testing it.
>
> Ask a vendor, in writing, what fraction of their last model's cost went into testing it.
> That answer says more about your exposure than any benchmark page does.
>
> It is cheaper to ship a model than to test one, and that gap is widening faster than the
> models are.

**Why this angle.** Everyone else in that thread will argue about whether the accounting is
honest or whether the bubble is real. Both are already taken. The move is to accept the reframe
and then point at what it leaves out, which is that none of that tenfold increase is earmarked
for testing. Concede first, then the turn.

**The memorable line:** cheaper to ship a model than to test one. It is the same critique as the
vendor-review post, aimed at the supply side instead of the buyer, so it reads as a consistent
position rather than a new complaint.

**Not used, on purpose:** any claim about what Anthropic actually spends on evaluations. There is
no source for that, and the whole point of Amodei's caveat is that the numbers are a thought
experiment. The draft stays inside the hypothetical he set up.

**Ending:** a statement, not a question, per the comment rule. The ask sits in the third
paragraph, in writing, so the last line can land.

**Timing:** the post is fresh. Anything after a few hours competes with the thread's own noise.
No link, no tag, no pitch.

## Entry 2: Hitesh Choudhary, Stageshow skill for coding agents

**Surface:** Hitesh Choudhary, 40 minutes old at paste. 1M and 700k YouTube channels, dev
audience, one of the largest engineering feeds on the platform. Post promotes Benji Taylor's
open-sourced Stageshow skill, with the install command `npx skills add benjitaylor/skills
--skill stageshow`, and asks whether an agent should be making landing page visuals.

**My read without a comment:** he is not ICP. Nobody in this thread is buying a security review.
The value here is reach and positioning only: a sharp comment in front of a dev audience that
sizes in the tens of thousands, from an account that otherwise talks to CISOs.

**Angle considered and dropped:** that a skill which fabricates convincing product UI makes
screenshots worthless as evidence in a security review. True, and I have made that argument twice
already this week. Three versions of "your evidence is weaker than you think" in five days is a
drumbeat, and a dev feed will read the third one as a man with one point.

**Angle kept:** the install command is the security surface. A skill is third-party instructions
that your agent reads inside its own context before it does anything. That is a dependency, and
the normal habit for dependencies is to read them before the first run.

### Draft: INTERACTIVE, 58 words, gate 100/100

> Agreed on instructions over bigger models. Good example of it here.
>
> The part I would add: a skill is a stranger's instructions sitting inside your agent's context,
> so that install command is a dependency. Same review you would give a package, before the first
> run rather than after.
>
> The mockup is the benefit. The review is the cost.

**Why short.** Big feed, generalist audience, and the post already asks a question. Short travels
further here than a 118-word version, and the last line is the only thing that needs to survive
the scroll.

**Tone check.** He opens with Hindi and a joke, and the post is genuinely enthusiastic. Opening
with agreement and ending on a line rather than a warning keeps this from reading as a man
telling a dev educator his business.

**Timing.** Forty minutes old. Comment now or not at all. His threads do not stay quiet.

## Entry 3: Naveen Reddy, LLM observability at 5 billion spans a day

**Surface:** Naveen Reddy, building roundz.ai, SDE3 at Amazon. Forty minutes old. Four real
engineering lessons: metadata versus payload separation, never blocking the request path, treating
LLM judges as systems, gating on confidence intervals. Ends on a question, and the links are
`lnkd.in`, so the full breakdown is unreadable to us and we do not cite it.

**My read without a comment:** he is not a buyer and he is not exactly ICP. He is building the
observability and eval layer, which is the layer this account red-teams from the outside. That
makes him a peer, a possible referral, and a possible channel, not a lead. Worth a comment anyway,
because the post is genuinely good and the audience is practitioners who will judge us on whether
we add something.

**What not to do:** do not restate his points back at him, and do not correct him. He is right on
all four. There is no error in this post to find.

**Where the gap is:** every check he describes answers a question about correctness on collected
traffic. None of it covers a user who is writing text to influence the grader. His judge lesson
calibrates the judge against human labels, which is the right instinct, and it assumes both the
judge and the human were looking at honest input.

### Draft: QUESTIONING, 117 words, gate 100/100

> Strong set, and the judge lesson is the one I would push hardest on.
>
> Kappa against human labels measures agreement on the traffic you collected. It says nothing
> about a user who'd write their prompt to make the judge pass. Grade on user-supplied text and
> the score is attacker-authored, then the gate approves it with a clean interval around a
> corrupted label.
>
> Calibration is necessary and it isn't adversarial coverage. Two ways in: hold out a set of
> judge-targeting inputs and measure how often the verdict flips, and require an exact check to
> pass before any judge verdict can gate a release.
>
> Your judge is a product with its own failure modes. Give it a red team.

**Why this angle.** It is the only thing in his four lessons that has a hole in it, and the hole
is exactly our subject. It also lands as an addition rather than a correction, because the first
line concedes that his instinct was right and the third line says calibration is necessary.

**The memorable line:** the score is attacker-authored and the gate approves it with a clean
interval around a corrupted label. Confidence intervals on corrupted labels is the sentence a
practitioner will remember, because it is a failure they can picture in their own pipeline.

**Risk accepted:** this is the third comment in two days built on an unverified assumption about
how something is measured. Here it is narrower, since he names the method himself, kappa on human
labels, and the argument is only about what that method covers. Still worth noting if the pattern
continues.

**Not used:** his `lnkd.in` links are unreadable, so nothing in the comment depends on the article.
