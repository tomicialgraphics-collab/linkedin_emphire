# Visual and hook spec

Built from the approved card (the 0.10 percent design) after the owner asked for three things on
2026-11-01: a headline and subheadline on every post, a first line that forces the "see more", and
the words to highlight in the visual.

Read this before designing a card or writing a first line. Every post ships with both.

---

## Part 1: the first line

The first line has one job. Get the click on "see more". Nothing else in the post matters if it
fails, because nothing else is visible.

**Three mechanisms that work. Use one, never none.**

1. **A number that does not belong together with its unit.** "You are auditing 0.10 percent of the
   input." The reader cannot resolve it without the next line.
2. **A contradiction in two clauses.** "Your vendor passed the audit. It never answered the
   question." Each half is ordinary. Together they are impossible.
3. **A cost stated flatly.** "It is cheaper to ship a model than to test one." No adjectives, no
   setup, just the thing that should not be true.

**Hard rules.**

- Under 120 characters, so it finishes before the mobile cut.
- No question as the first line. Questions ask for work; statements create it.
- Headline plus subheadline must both be complete inside 200 characters. That is what shows before
  the cut. If the pair runs past 200, the subheadline is too long, not the headline.
- Never open with "I", "We", or a greeting. Nobody clicks for the writer.
- The blank line is a design element. Put it where you want the cut to land.
- No em dashes, no bold, no emoji as punctuation.

**The test.** Read only the first 120 characters and ask whether a stranger needs the next line to
close the loop. If the first line is a complete, satisfied thought, it is not a hook. Rewrite it.

---

## Part 2: the words to highlight

One boxed phrase per card. Only one. Two boxes means the eye has nothing to land on, which is the
same as having no box.

**The rule: box the quantity or the failure verb. Never the topic.**

In the approved card, the topic is auditing. The box is "0.10 PERCENT". The topic appears three
times in the headline without being highlighted, and the number carries the whole design.

**Selection order, stop at the first that applies.**

1. **A ratio or a count that humiliates the alternative.** 0.10 PERCENT. 45 TOKENS. 275 STATEMENTS.
2. **The verb of the failure.** NEVER ANSWERED. DROPPED. REFUSING. PICKS ONE. Verbs travel further
   than nouns, because a verb implies an actor.
3. **The mechanism.** CONSENSUS FILTER. SELF-GRADED. Only when there is no number and no clean verb.

**The portability test.** If the boxed words could headline a different post by a different writer,
they are wrong. "AI" fails it. "RISK" fails it. "0.10 PERCENT" passes, because it belongs to one
measurement in one context.

**Format.** One to three words. Sits inside a single line, never split across a line break. Never
opens the first line of the headline. Accent fill, reversed or white text, no outline, no shadow.

---

## Part 3: the card layout

Geometry is locked from the approved reference. Only the copy changes.

- Black field, left 70 to 75 percent of the canvas.
- Two vertical bars at the right edge, light blue then navy. These do not move, resize, or change
  colour.
- Real photograph of the owner, right side, cut out, overlapping the bars. No generated face, ever.
- Headline: three lines maximum, two to four words per line, heavy condensed caps, white.
- One boxed phrase, per Part 2.
- Subheadline: one or two lines, all caps, small, letterspaced, carrying the numbers or the stakes.
  This is where the evidence goes, not the slogan.
- Lockup bottom left: name in bold, role in grey. Olusanya Timothy, Software Engineer | AI Safety |
  AI Red Teaming.
- Nothing else. No logo, no icon row, no URL, no stock imagery, no gradient.

---

## Part 4: the three cards in the repo

### Card A: prompt context window

Already designed. Kept as the reference for everything above.

```
HEADLINE   YOU ARE AUDITING
           [0.10 PERCENT]
           OF THE INPUT.

SUB        IN A PUBLISHED AGENT CONTEXT WINDOW, THE OPERATOR'S INSTRUCTION
           IS 45 TOKENS. THE RETRIEVED DOCUMENTS ARE 45,774.
```

**Box:** 0.10 PERCENT. **Why it works:** the number is the argument. The subheadline supplies the
two figures it came from, so the box is arithmetic rather than decoration.

**Do not change it.** Variants that box "45 TOKENS" are weaker, because that figure is already in
the subheadline and boxing it splits the evidence across two places.

### Card B: vendor review

`soc2-model-behaviour`. No number available, so the box goes on the failure verb.

```
HEADLINE   YOUR VENDOR PASSED
           THE AUDIT. IT
           [NEVER ANSWERED].

SUB        A SOC 2 ATTEST THAT CONTROLS EXIST. IT SAYS NOTHING ABOUT WHAT
           THE MODEL DOES WHEN A USER SAYS FORGET YOUR INSTRUCTIONS.
```

**Box:** NEVER ANSWERED. **Why:** the contrast is the whole post, and the contrast is a verb. Boxing
"SOC 2" would highlight the thing everyone already knows.

**Alternative box:** PASSED THE AUDIT, if a lighter card is wanted. Weaker, because it highlights the
side of the contrast the reader already agrees with.

### Card C: value pluralism

`redteam-pluralism`. This one has a number and a verb, so both the headline and the box can carry
weight.

```
HEADLINE   TWO USERS
           ARE BOTH RIGHT.
           YOUR RUBRIC [PICKS ONE].

SUB        ANTHROPIC BUILT A CONSTITUTION FROM 275 PUBLIC STATEMENTS.
           BOTH SIDES OF ONE CONFLICT WERE DROPPED. THE MODEL WITHDREW MORE.
```

**Box:** PICKS ONE. **Why:** it turns a fair-sounding process into an arbitrary one in two words, and
it is the sentence the reader will repeat. The 275 sits in the subheadline, where evidence belongs.

**Alternative box:** 275 STATEMENTS, for a version aimed at a research audience rather than a buyer.

---

## Part 5: checklist before a card ships

- [ ] First line under 120 characters, and incomplete without the next one.
- [ ] Headline plus subheadline complete inside 200 characters.
- [ ] Exactly one box, one to three words, on a single line, not opening line one.
- [ ] The box passes the portability test.
- [ ] Subheadline contains the evidence, headline contains the claim. Neither repeats the other.
- [ ] Real photo, locked bars, name and role lockup.
- [ ] No em dashes anywhere on the card or in the first line.
