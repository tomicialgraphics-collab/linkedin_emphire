# Banner and headline wording, 3 November

Four complete sets. Each is a unit: banner headline, banner subheadline, the headline field, the alt text,
and the first line of the About. The field and the banner must not say the same sentence twice, because
both appear on the same screen.

## The one rule that decides all of it

The field headline appears everywhere: search, suggestions, next to every comment. The banner appears in
only one place, the profile page itself. So the field has to work alone, and the banner has to reward the
click. Anyone landing from a comment already knows his name; the banner's job is to say the lane and the
standard in three seconds, not to repeat his title.

Never put his name in the banner. It is six inches above it. Never put "Software Engineer" in it either,
because that is the word that makes him look like everyone else in the feed.

## Set A. The green dashboard. Recommended.

Banner headline, 45 characters, set at 50 point over two lines:

```
Most AI failures ship
with a green dashboard.
```

Banner subheadline, 81 characters, two lines:

```
Red teaming and evaluations that end in a
reproducible finding, not a screenshot.
```

Headline field, 87 characters:

```
AI security and evals. I red team agents before they get keys, and publish what breaks.
```

Alt text, 107 characters:

```
Most AI failures ship with a green dashboard. Red teaming and evaluations ending in a reproducible finding.
```

About first line, unchanged: `I trained as a Medical Laboratory Scientist. Now I break AI systems on
purpose.`

Why this one. The headline is a claim about the industry, not about him, which is what makes it readable
twice. The subheadline is the method and it contains the one phrase that separates him from a hundred
other red-teamers: not a screenshot. The field carries the identity and the searchable words. Nothing is
said twice.

## Set B. Benchmarks. For a research audience.

Banner headline, 36 characters:

```
I find the failures
benchmarks miss.
```

Banner subheadline, 84 characters:

```
Red teaming and reproducible evaluation for
agents with tools, data and permissions.
```

Headline field, 95 characters:

```
AI security and evals. Red teaming, reproducible findings, and defect registers for benchmarks.
```

Alt text: `I find the failures benchmarks miss. Red teaming and reproducible evaluation for agents with tools and permissions.`

Why this one. It is the closest to a research identity, so it is the set to use while the NVIDIA
conversation is live. The cost is that "benchmarks" is narrower than what he does, and it invites the
question of which benchmarks.

## Set C. For clients.

Banner headline, 84 characters over three lines:

```
Your agent has tools, data
and permissions. I test what
happens when someone pushes.
```

Banner subheadline, 80 characters:

```
Before launch, not after. A second pair of
eyes on the checks you already trust.
```

Small green line under it: `DM me   ·   Lagos, Nigeria`

Headline field, 85 characters:

```
I test AI agents before launch. Red teaming, evaluations, and findings you can rerun.
```

Why this one. It is the only set that asks for the work. Use it when paid engagements are the priority and
the job search is not, and do not run it while a research role is in flight, because it reads as a vendor.

## Set D. The quiet one.

Banner headline, 27 characters: `AI security and evaluations`

Banner subheadline, 74 characters:

```
Agents, retrieval, tool permissions.
Findings published with the evidence.
```

Headline field, 65 characters: `AI security and evaluations. Agents, retrieval, tool permissions.`

Why this one. It is the only set that will not embarrass him in three years. It is also the only one that
gives a reader nothing to remember, which matters if the profile has to work without him posting every
day. Take it only if he intends to stop posting.

## The other things the banner needs

- **Alt text.** LinkedIn accepts it on the banner and almost nobody fills it in. Paste the line from the
  set he picks. It is read by screen readers and it is indexed.
- **Straight punctuation only.** No em dashes, no curly quotes, no ellipsis characters. The renders use
  straight apostrophes and that has to survive any editing he does.
- **Size.** 1584 by 396. Text sits right of centre so the circular photo in the bottom left does not cover
  it.
- **No hashtags, no emoji, no follower counts, no client names, no numbers that need a footnote.** A banner
  is not a CV and cannot carry evidence.
- **One URL at most, and only if it is short enough to retype.** Better to leave it out and let the
  Featured section carry the links.
- **Do not put a photo of himself in it.** He is already in the photo.

## Renders

`ASSETS/profile-2026-11-03/banner_A_green-dashboard.png`
`ASSETS/profile-2026-11-03/banner_B_benchmarks-miss.png`
`ASSETS/profile-2026-11-03/banner_C_your-agent.png`
`ASSETS/profile-2026-11-03/banner_D_quiet.png`

Regenerate any of them with `ASSETS/profile-2026-11-03/render.sh`. Change a word, run the script, and the
line breaks are already correct at that size.
