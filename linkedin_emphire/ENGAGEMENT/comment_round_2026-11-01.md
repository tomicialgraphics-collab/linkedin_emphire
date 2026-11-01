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

## Entry 4: Brij Kishore Pandey, AWS MCP server for re:Invent

**Surface:** Brij Kishore Pandey, 46 minutes old, sponsored by AWS. 738K on LinkedIn, 294K on
Instagram, a newsletter with 250K AI builders. He is using the AWS MCP server for re:Invent to
plan sessions, lists the constraints his agent has to hold, shows his prompt, and ends on a real
question: what should an agent have to show you before it is allowed to cancel anything.

**My read without a comment:** large reach, an AI-architecture audience, and a direct question
about action-taking agents. This is the best-targeted surface of the four today, because the
question is our subject and he asked it.

**What not to do:** do not attack AWS on a sponsored post, and do not re-explain his own prompt
back to him. He already has approval before action and readback after action, which is more than
most production agents ship with.

**Where the gap is:** approval is granted to a plan, and the plan changes as soon as the first
reservation fails. His own observation about per-session success is the proof. Approval for an
intent is not approval for the concrete call.

**Second gap, larger:** session titles and descriptions are written by strangers and arrive in the
same context that decides what to cancel. That is the only genuinely red-teamable surface in the
post, and it is worth flagging to an AI architect without making it a criticism of AWS.

### Draft: QUESTIONING, 110 words, gate 100/100

> The readback after acting is the part most teams skip, so it's good you put it in the prompt.
>
> On cancelling: it should have to clear a higher bar than reserving did. The exact session, the
> consequence, that the seat goes to someone else the moment the call lands, and what changed
> since I approved. Approval covers the plan you showed me. If the plan moved after I'd said yes,
> my yes expired.
>
> One more test for Vegas. Session titles and descriptions are written by strangers, and they land
> in the same context that decides what to cancel. Write a description that reads like an
> instruction and watch what happens.

**The memorable line:** if the plan moved after I said yes, my yes expired. It answers his
question with a principle rather than a checklist, and it is the sentence a builder will carry
into their own agent.

**Why the second point is worth the last paragraph.** It is the difference between a comment that
agrees with him and a comment that shows what we do. It also costs him nothing to test before
Vegas, and if he reports back, that is a conversation with a 738K audience.

**Careful note:** he does not say the catalogue is adversarial, and I do not claim it is. The
suggestion is a test, not an accusation, and it is framed that way on purpose because the post is
sponsored.

**Not used:** the drumbeat angle. I could have written a fifth version of "verification is weaker
than it looks." The cancellation bar is a different argument, and the injection test is the one
this audience will actually run.

## Entry 5: Brad Wolfe, measure the unit cost not the hours

**Surface:** Brad Wolfe, 1st degree, seven hours old. AI strategy and capital allocation CFO, 80+
M&A, three NASDAQ CFO seats, AI committee and audit committee chair. The post is a chain: hours
saved, capacity released, a management decision, a financial outcome. He argues most business
cases measure the first step and report the last, and gives a PE roll-up case where back-office
cost per unit went from $247 to $202 over twelve months while the company grew 400%. He ends on
"what unit would your back office be measured on?"

**Relationship note:** this is the second time he has been in front of us. On 10-31 he replied to
the 2B comment within three minutes, and the 56-word reply drafted for him then is STILL UNSENT.
If that reply has not gone out, send it before commenting here. Answering a second post from a
1st-degree contact while his earlier reply sits unanswered reads as scatter.

**Why this one matters more than the reach numbers suggest:** he builds the business case that a
buyer takes to a board. If our point about measurement lands with him, it lands upstream of a
security budget, which is the hardest place to reach from a red-teamer's account.

**His frame is right and there is one column missing.** He is careful, he refuses surveys and
hours estimates, and he insists the decision be made before the tool goes in. All correct. What
the table does not carry is how often the work came back.

### Draft: OUTSTANDING, 116 words, gate 100/100

> Agreed on the chain, and the decision in the middle is the step that gets skipped.
>
> One addition for a roll-up: put the return rate in the same table. Cost per unit says what the
> work costs, not how often the work came back. When AI takes the first pass, exceptions don't
> fail loudly, they queue for a person, and the rework lands in a different line item a quarter
> later. In a document-heavy back office that can eat the savings quietly.
>
> Same standard you set for hours, no survey and no estimate. Count the items that had to be
> redone.
>
> $247 to $202 is the number. The rework count is what tells you it holds.

**Why it should land with him specifically.** The argument is in his own language, not ours. It is
about the denominator, not about model behaviour, and it uses the standard he set himself: no
survey, no estimate, count something. A red-teamer telling a CFO about rework rates is credible
only if the rework is described as a cost line, which is what the draft does.

**The memorable line:** cost per unit tells you what the work costs, not how often the work came
back. It also does not contradict his post, which matters, because he is a 1st-degree contact who
has been generous with his time.

**Deliberately absent:** no mention of security, risk, or AI failure modes. There is a version of
this comment that pivots to our subject and it would be worse. He asked about cost per unit, so
the whole comment stays on cost per unit.

**Numbers:** his, quoted back, not new ones. Nothing invented.

## Entry 6: Ashwini Mathur, reply on my own human-in-the-loop post

**Surface:** a reply to my post of the same day, on the line that the human in the loop is not
the safeguard, a human with time to read and standing to say no is. Post shows 437 impressions,
1 reaction.

**Their line, verbatim:** "Yes, the mere logistics of staying human is pushing us away from
staying human."

**My read without a comment:** this is the reply you want on that post, because it takes the
argument somewhere I did not. The post said the safeguard is time and standing. Ashwini says the
administration of that safeguard is itself what pushes people out of it. That is a better
sentence than mine and the reply should say so by building on it, not by complimenting it.

**Draft A: AGREEMENT WITH A TURN, 67 words, voice_lint clean**

> Agreed, and the logistics are the tell. When a review queue is the bottleneck, the cheap fix is
> a wider queue rather than a shorter one: more items per hour, the same twenty seconds each. The
> question I would put to any system like that is whether a reviewer can refuse something and have
> the refusal stick. If not, the human is a name on a diagram.

**Draft B: SHORTER, 48 words, voice_lint clean**

> Which is why the queue gets widened before it gets shortened. More items per hour is cheaper to
> buy than fewer items, so the count rises and the time per item does not. Staying human stops
> being something you are and becomes something you are given time for.

**Why A over B for this thread.** A ends on a test a reader can apply the next morning, which is
what the post already does. B is better writing and worse as a reply, because it closes the
thought instead of handing it back.

**The memorable line:** the human is a name on a diagram.

**Note on the thread.** His sentence deserves a like of its own. Do not stack a second comment
after this one, and do not turn it into a post: the same idea on my own feed two days running
reads as a theme rather than a reply.
