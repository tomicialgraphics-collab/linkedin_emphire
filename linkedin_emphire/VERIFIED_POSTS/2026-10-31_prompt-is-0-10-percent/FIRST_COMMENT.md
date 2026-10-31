# First comment on today's post

Post: `post.md` (311 words). Headline: "You are auditing 0.10 percent of the input."

Post the first comment yourself, **within 20 minutes of publishing**, then reply to every response
inside the first hour. Your last three posts died at 26, 76 and 27 impressions with no comment on
them, and a post with no early comments has no reason to be shown to anyone else.

## Recommended: preempt the objection

**122 words, voice lint clean, human gate 100/100**

```
The fair objection to this post is that one session is not a distribution. Correct, and it isn't the claim.

The claim is structural. Whatever the distribution turns out to be, the operator's instruction is the smallest component by construction, because instructions arrive in a sentence and retrieved documents arrive in bulk. You don't need a sample to know which side the weight sits on.

What a sample buys you is the ratio in your own stack, and that number is worth having. Dump one session, count the tokens by source, and see how much of what your agent read was written by you.

Most teams can't answer that, and it is the first question I'd put to any vendor selling oversight.
```

**Why this one.** The post has exactly one obvious line of attack: a single session proves nothing
about the distribution. Every careful reader who disagrees will reach for it, and if you answer it
first the thread has somewhere to go other than your defence. It also splits the claim into what is
structural (the instruction is the smallest component by construction) and what needs measurement
(the ratio in a given stack), which is the honest split and the one a research reader will respect.

## Alternative: the how-to

**113 words, voice lint clean, human gate 100/100**

```
If you want to run this on your own agent, you don't need anything fancy. Take one session, list every component that entered the context window, and tag each one by who wrote it.

You're looking for two numbers: the token share you authored, and the token share that arrived from a tool result, a retrieved document or somebody else's tool definition.

In the session I wrote about, the second number was 99.1 percent.

The useful question after that is not how to shrink it. It's which of those components a person ever read before it went in. For most pipelines the answer is the instruction, and the instruction is the 0.10 percent.
```

Use this one if you would rather the thread be practical than argumentative. It gives a reader a
task, which pulls in the people who lurk rather than comment, and it points back at the post's own
number without repeating the argument.

Do not post both. Two comments from the author on one post reads as filling the room.

## What to avoid in the thread

- Do not re-explain the post. Anyone commenting has read it.
- Do not thank people for engaging. Answer the substance or let it sit.
- If someone produces a real session of their own, that is the best outcome available today. Ask
  what their share was, then leave it alone.
- If someone says the numbers are from a vendor's own record and therefore marketing, agree, and
  point at the caveat already in the post: one session, not a study, not evaluated in production.
