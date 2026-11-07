# Engagement drafts, 4 November 2026, evening feed

One comment per post. Order is by value of the thread, not by feed order.

## 1. Daniel Miessler, agent inventory (2h)

Most teams can list what they deployed. The part that fails is proving the list is complete, and that is a different question. An inventory you maintain yourself can only prove what somebody remembered to add. It stays accurate on the day it is written and quietly stops being complete about six months later, and nothing about it looks wrong in between.

What I would want an auditor holding is a record that cannot shrink without saying so. Registration at the point of creation, plus something anchored periodically that shows the shape of the list at a date. Then the question becomes which of the two moved, the inventory or the thing it inventories.

## 2. Rock Lambros, Adversary Brains and the missing attribution field (6h)

Putting the constraint in the schema rather than in a policy is the part worth stealing. A policy is read by people who already agree with it. A schema is enforced by a parser that has no opinion.

The test I would apply to any framework like this: can a well-meaning analyst record the forbidden thing anyway. If they can, it is a policy wearing a schema's clothes.

The retirement rule is the one I would watch. A brain that never confirms should be retired, but "never" needs a defined interval or the retirement becomes the same judgment call the schema was meant to prevent.

## 3. Sam Illingworth, AI-induced disempowerment (11h)

The number that should worry a review function is the 15 percent. Influence that leaves no trace in the written reasoning means the document is not evidence of independent judgment, and it will read exactly like one.

So the convergence test inverts. Several people reaching the same answer is evidence only if they got there separately, and after this study you cannot assume that from the output. You have to look for the same defaults appearing across people who never spoke to each other.

That is checkable in an organisation. Nobody currently checks it because the artefacts look clean.

## 4. Nathan Hamiel, Black Hat India keynote (6h)

The skills point is the one I would underline. The gap is rarely ignorance of how models work. It is teams putting agents into production faster than they can describe what the agent is allowed to touch, and then discovering the description was the only control.

A security correction rather than an apocalypse is the right frame, and it is also the harder sell, because a correction does not fund itself. The work is boring and it happens before anything goes wrong, which is the same week nobody has budget for.

## 5. Brad Wolfe, you removed an occasion (19h)

The 248 of 250 figure is the trap, and it is structural. Any control measured by how often it changes the answer will look like noise, because by construction it mostly does not change the answer. The case for keeping it can never be made out of its own output.

Which is why the two-year entry test is the right instrument. It looks outside the step, at what the step caused, and that is the only place the evidence was ever going to be.

Worth adding: after the tie-out goes, nothing replaces the schedule. The comparison was the point, not the reconciliation.

## 6. Reply to Shanee Moret's two comments (21h)

Thank you for saying it plainly, twice, which is more than most people bother to do. I am taking the thirty days seriously and starting this week.

The part I am still working out is what to put on camera that is not a repeat of the feed. My material is mostly what breaks when agents are given real access, and that is easier to show than to say, so I will show it.

One question before I start. Do you want the first videos rough on purpose, or does a bad first video cost more than a late one?

## 7. Jerry Liu, OCRia-1 (12m)

I will read the appendix for one thing in particular, how it behaves when it fails rather than how often it succeeds.

In a document pipeline the aggregate accuracy is the least useful number, because the errors are not evenly spread. Tables and forms fail differently from prose, and a cell read confidently and wrongly travels into a figure somebody signs. What matters downstream is whether the parser can output "I could not read this region" with the same conviction it outputs everything else.

If there is a per-element confidence calibration or a refusal rate in the report, that is the section I would send a production team to. Accuracy per class tells you what to expect. A refusal path tells you what to trust.

## 8. Greg Isenberg, the agent stack (24m)

The most load-bearing lines here are the ones where the agent reports on itself. The nightly log is written by the agent whose day it describes. The 1-10 judge is a model that can be talked out of an 8. The new skill is written by the agent that just got it wrong.

That is not a reason to drop any of it. It is a reason to know which controls are evidence and which are testimony.

A cheap test: take one agent, remove its ability to write its own log for a week, and see what still gets logged. Whatever survives that is the part you actually control. The rest is a well-run rumour mill that happens to be right most days.

## 9. NVIDIA DSX OS, AI factory operations (unspecified author)

One operational view is the right goal and the hardest claim to test. Discovery tells you what exists. It cannot tell you what exists and was not discovered, and at rack level that is the failure that hurts, because a node nobody inventoried still draws power and still accepts work.

The agentic part is where I would want the detail. An agent that can provision, drain or quarantine a node is holding a credential that used to belong to a person with a phone call and a manager. What matters is whether its actions land in the same record as the human ones, and whether that record can be shown to be complete rather than merely continuous.

Shorter version: one operational view is the right goal. The question is whether it can tell you what it failed to see, because a node nobody discovered still draws power.

## 10. Dr. Sasha Luccioni, data centre backlash at the polls (36m)

The ballot fights will turn on definitions, and there are three where a defensible choice can still mislead.

Water, consumption against withdrawal. A closed loop withdraws and returns nearly all of it, so the same facility is either a rounding error or a town's supply depending on the word on the page.

Electricity, annual average carbon intensity against the marginal hour. A plant running flat load looks good on the first and often poor on the second.

The boundary itself, whether the figure covers the shell, the IT load or the whole campus. That is the difference between a PUE claim and a measurement.

A workable middle ground is going to be built out of those three choices being fixed in public before the numbers arrive.

Caution: keep it on measurement, take no side on the measures themselves.

## 11. Isabel Heineman, Triangle InfoSeCon 2026 (45m)

Your line about shifting the focus from a malicious actor to our own action or inaction is the whole argument, and it deserves saying more often. Most agent incidents I look at are not attacks. They are ordinary permissions applied to something that now acts on its own, at a speed nobody configured for.

In a HIPAA setting that question gets sharper, because an agent touching records is a disclosure path that may never have been written down anywhere.

What I would carry into GRC work from that talk: not what could attack this agent, but what we handed it, and whether it can tell us afterwards what it did with it. An auditor ends up asking both.

## 12. Rachael Bolton, recommendation of Sam Illingworth (47m)

Good recommendation. The part of Sam's work I keep taking into reviews is the 15 percent, because it means the written reasoning cannot be counted as evidence of independent judgment. Influence that leaves no trace in the record is invisible to exactly the process most organisations use to check their own decisions.

For anyone writing about the future of work, that is the quieter story. The tool does not replace the judgement. It supplies the default, the person signs it, and the document afterwards looks like their thinking either way.

## 13. Jamil Jaffer, joining OpenAI as Head of Global Government Cyber (50m)

Congratulations. One question rather than a comment, since you are about to be on the receiving end of it for the next few years.

When a government points an AI system at critical infrastructure, the oversight question that lands first is not whether it works. It is whether anyone can prove afterwards what it did, in a form that survives the vendor's own logs and the passage of a procurement cycle.

That is a different requirement from capability, and it is usually discovered after deployment rather than before.

Is that part of how you are framing the role, or does it sit with the agencies themselves?

Shorter version: congratulations. The question I would expect to follow you into this role is not whether government AI works, but whether anyone can prove afterwards what it did once the vendor's logs are gone.

## 14. Paolo Perrone, OS-style virtual memory for LLM serving (55m)

The interesting consequence is not the 2 to 28x. It is what virtualising the cache does to a boundary that used to be physical. Once one GPU is time sharing several models, a recycled block stops being a performance detail and becomes a disclosure risk, because the memory being handed to the next request may still describe somebody else's prompt.

So the two things I would want from anything claiming to be a drop-in: a stated guarantee about what happens to a block on release, and a counter for blocks reclaimed while still referenced. The second is the one that catches the bad day, where throughput looks excellent and isolation is quietly gone.

Does the implementation expose either?

## 15. Alex Mashrabov, Higgsfield #5 on Ramp (1h)

The interesting line in this is not the ranking. It is the move from a card swipe to a creative budget.

Card spend is one person deciding a tool is worth trying. A budget line is a finance owner deciding it is worth defending, and the questions change with the ownership. Which assets were generated, under what rights, and whether that can be shown a year later if a campaign is challenged.

Everyone in this category meets that question eventually. Being first on spend means meeting it first.

Is it changing the shape of your deals, fewer seats with bigger commitments, or still individuals swiping cards at scale?

## 16. Dr. Rumman Chowdhury, the kitchen table op-ed (2m)

Your critique of the patronising framing has a practical consequence the industry keeps missing. The three in four who do not trust the output get treated as a communications problem, which is why the reassurance campaigns do not work. It is a verification problem.

Nobody at a kitchen table wants to be told the system is fair. They want to see what it did with their information, and to know who answers when it goes wrong. Both of those need a record a person can hold, not a policy saying a record exists somewhere.

Agency without a receipt is a preference, not a right. That is the whole distance between what people are asking for and what is being offered to them.

## 17. Luis Fernando Roquette, the AI insurance market (5m)

That market appears when there is an insurable unit, and the unit is what is missing.

Insurers price events they can locate, bound, and audit after the fact. An agent acting inside a customer's systems leaves a record that the customer wrote, and no underwriter will accept the insured's account of the loss as the account of the loss. That is the same reason you cannot buy cover against your own bookkeeping.

So the precondition is not better guardrails. It is an action record with a custodian outside the party being covered, plus a way for an adjuster to check the record is complete rather than merely present. Smaller and more concrete than what currently gets sold as AI governance.

Are you seeing anyone write this risk yet, or is it exclusions and sub-limits all the way down?

## 18. Lauren Toulson, preferences that do not survive deployment (9h)

Part of what the forced choice measures is friction, not preference. Both options are equally reachable when you ask directly, so what comes out is a ranking of hypotheticals. In a deployment the options are rarely equal. One is the default, the other needs a tool call, a delay, or a permission, and the cheaper one tends to win.

Which makes the null result the interesting part. It does not say the model has no preferences. It says the preferences do not survive the shape of the task, and that shape is usually a design decision somebody made without noticing.

The follow-up I would want: make the disfavoured option the default in the deployment context, and see whether the ranking comes back.

## 19. Rock Lambros, the agent wearing an employee's login (12h)

The detail that matters is the clock. The 72 hour reporting window starts at discovery, and discovery is the thing that failed. An agent wearing a person's session means every record of the activity names the person, so the first question in an investigation returns the wrong name.

Separate agent identity fixes attribution from here forward. It does not fix the two months already spent, unless the record can be read backwards to show which sessions were agents. That is a schema question rather than an IAM question: does the session record carry the actor's type, and was it written at the time.

Without that, the honest answer to "how long did it run" is the date somebody noticed.

## 20. Brad Wolfe, the agent needs a row in the delegation of authority (44m)

The row is right and it has one gap an auditor will find. A delegation of authority is written for a person accountable for their own acts. An agent's row also needs what it may do that is not an approval at all.

Reading is an act. An agent with read access to the whole ledger has authority to see everything while approving nothing, and no row in that document will mention it. Same for the systems it can query and the records it can copy.

Authority to act and authority to see are two different limits. Only one of them currently gets written down anywhere.

## 21. Tanya Janca, what permissions should you give an agent (4h)

Permissions versus instructions is the episode in two words. An instruction is advice the model can be talked out of. A permission is a fact about what the runtime will allow, and it holds whether or not the agent agrees with you.

The question that saves the most work is the one you put last. Does this need to be an agent at all. Most of the ones I see did not. They needed a scheduled script with a fixed scope, and the agent arrived because a person wanted one.

Blast radius is decided when the credential is issued, not when the prompt is written.

## 22. Brad Wolfe, definitions across acquisitions (6m)

The line that will get lost is the last one. If the agent cannot tell you which definition is right, neither can the variance it reports, and the number it produces next quarter will look like performance.

The mechanism is the one nobody notices. The moment you pick one definition, every prior period gets re-expressed under it. History is restated silently, so the change in the number is part movement and part definition, with nothing on the page to say which.

Which means the record has to carry the definition, not just the figure. Version, effective from when, who signed it. Then a variance splits into the two halves and somebody can be asked about theirs.

Is the definition stored with the number it produced, or only as the current version? That is what decides whether a variance can ever be explained after the fact.

## 23. Endrit Restelica, should AI pricing be outcome based (6h)

Both halves of that question need the same thing, and it is not a pricing model.

Charging for value means attributing an outcome to a contribution. Refunding for harm means attributing a loss to an action. Neither is possible with what most deployments record, which is the final answer and not the steps, the inputs, or the version of the system that produced it.

So outcome pricing will not arrive everywhere. It will arrive where the vendor can produce a record of what the system did, and stay away from everywhere else, which is a much smaller market than the argument suggests.

Attribution first. Pricing is what happens after somebody can attribute.

## 24. Lauren Toulson, second comment after reading the paper (post is 9h old)

Two lines in the limitations section deserve to be findings.

Kimi is the only model whose reasoning named the country as a reason, and it was excluded for exhausting its reasoning budget before a verdict. That exclusion is not neutral. It removes the one case where deliberation surfaced a country specific judgement, so the null is estimated on the models that reasoned least about the country. If a preference only appears when the model has room to think, the design has removed the condition that would reveal it.

Refusals do something similar. In the A/B tests they carry much of the hierarchy, and in the agentic scenarios no-action is coded as a directional favour. The two instruments treat indecision differently, so part of the gap between the results could be indecision converted into action rather than a preference disappearing.

Kimi with a longer reasoning budget would settle more than a higher epoch count would.

## 25. Dario Melo, humanoids and the 60/40 teleoperation split (35m)

A fourth gap belongs on that list, and it decides whether the other three reach homes at all.

Once a remote operator can take the wheel inside a stranger's house, every incident has two possible actors, and the first question afterwards is who was in control at that second. Video will not answer it. Neither will the robot's own log, because the robot is not the party with an interest in the answer.

Control transfers, operator identity, and what the operator could see while they held it need to be recorded as events, at the time they happen. That is a small amount of telemetry and it is the difference between an incident that ends one vendor and one that ends the category.

## 26. Adrian Lee Sanchez, the AI revenue gap and the accountability bills (8h)

Two things here are usually told as separate stories, the six hundred billion and the accountability bills. They share a cause.

Enterprise AI spend currently arrives as hours saved, tickets closed, drafts produced. None of those is an account. Until the value lands in a line somebody signs, the spend stays a pilot, and pilots do not service depreciation. That is the revenue gap, and it is a measurement problem wearing a demand problem's clothes.

The same absence sits behind the regulation. An accountability act does not ask whether the model is good. It asks what it did and who decided, and the deployer who cannot answer pays for that, not the builder.

Both stories end at the same artefact. Somebody has to be able to show what the system did.
