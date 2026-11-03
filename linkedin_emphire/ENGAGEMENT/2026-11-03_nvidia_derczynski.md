# NVIDIA, Senior Research Scientist, AI Security: Leon Derczynski's post

## What the post actually is

Leon Derczynski, Security and AI at NVIDIA, professor at ITU Copenhagen, founder of garak, chair of ACL
SIGSEC. He posted five hours ago with the link in the first comment. The role is on the Agentic
Cybersecurity Research team, job 893398261143, requisition JR2028502.

**The window.** Posted 30 October 2026, applications accepted at least until 3 November 2026, which is
today. "At least until" means it can run longer, but it is being treated as today.

**The bar.** Master's or PhD in computer science, computer engineering, data science or a related field,
or equivalent experience. Five or more years in machine learning, cybersecurity or closely related
fields. Shown programming expertise. Knowledge of AI and conventional software weaknesses and how to
mitigate them. In-depth understanding of generative AI workflows.

**What makes a candidate stand out.** Cross-functional delivery. Discovered CVEs and built successful
tooling. Adversarial machine learning. Secure development practice. Ability to build human-friendly
resources.

**Pay.** Level 3: 168,000 to 264,500 USD. Level 4: 192,000 to 304,750 USD. Level 5: 224,000 to 356,500.
Equity and benefits on top.

**Location.** United States, including Santa Clara, or elsewhere. "Elsewhere" is doing a lot of work in
that sentence and it has not been defined.

## The honest read on fit

The two stand-out bullets are his record almost word for word. Built successful tooling: breaklab, a
deterministic red-team tool that produces a verdict against the app's own evidence and the exact span
that broke. Ability to build human-friendly resources: twelve days of run notes, a twelve-model
benchmark, a published review of someone else's suite with a defect register and a fix order.

The bar that is genuinely in the way is five or more years in ML or security, and the degree. Equivalent
experience is written into the posting, but a hiring manager reading a form will apply the years filter
before reading the evidence. That is an argument for applying with the artifacts in front of him, not
against applying.

The specific advantage here is that the team's stated work is exposing novel weaknesses and publishing
the results in peer-reviewed venues. His twelve-day run found that the benchmark itself was the weak
point, and he published that. That is the same instinct the role is asking for, applied one level up.

## The blocker: fix this before linking anything

`Teamthy/My-Breaking-lab` is public, last pushed 12 October, and `config/example_target.yaml` still reads
`name: ncd-guideline-tutor`. So does `config/example_sse_target.yaml`. That is the client identifier the
standing rule says must never appear in public, and it has been sitting there for three weeks.

Do not put that repo in an application, a DM or a comment until it is renamed. Two edits:

```
name: example-chat-target
name: example-chat-target-stream
```

The repo is public and searchable, so this is not theoretical. Either rename the two fields and push, or
leave the repo out of the application entirely and describe the work in words.

## The comment, 87 words, lint clean

garak settled the part that used to be hard: producing a large, systematic set of probes is now a
distribution problem, not a research one.

What still stops teams is everything after a probe trips. Deciding whether it is a real failure, naming
the exact span that broke, and showing a second person that the same input fails the same way on their
build.

The detector is rarely the bottleneck. Reproducibility and attribution are, and both are unglamorous
enough that most tooling leaves them to the user.

It does not say "I am applying". It says the thing that makes the application obvious to the person who
reads it, on the timeline of a comment that will be seen before the form is.

## The direct message, 104 words, lint clean

Leon, I saw the Senior Research Scientist post. I work on the half that comes after the probe trips:
deterministic red-team checks that fail CI on the exact span that broke, and a twelve-day run of
eighteen models through a security benchmark where I published the defects I found in the benchmark
rather than the scores.

One thing I would rather ask now than waste your time on: I am in Lagos, so I would want to know what
"or elsewhere" means for this team before I apply. If it means remote inside the US, tell me and I will
not take the slot.

The location question is the whole point of sending this rather than just applying. He can answer it in
one line, and it decides whether the application is worth an hour.

## Order

1. Rename the two config fields, or decide to leave the repo out. Do not skip this.
2. Comment on the post. It takes a minute and puts the argument under his own post.
3. Send the message. The location answer gates everything else.
4. If the answer is workable, apply today with breaklab first, the review second, and the run third.

Do not name the Aithos application, the Arcezia review or any client inside the application. The
review of the benchmark can be described without naming Behar.
