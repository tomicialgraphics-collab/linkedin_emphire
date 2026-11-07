# Legacy posts

Twenty-five posts in this folder were written before the front-matter contract existed. They are
frozen. They are not re-gated, they are not rewritten in bulk, and they cannot be reposted or quoted
in a new package without being brought under the contract first.

## Why not convert them all at once

Because the contract asks for things those posts never had. A headline pair, a boxed phrase, verified
hashtags, a named template. Inventing those after the fact would put a number in a file that no longer
matches what was published, and R06 is about exactly that. The post went out as it went out.

## The rule

Touch a legacy post for any reason, and it comes under contract in the same commit:

```bash
python3 linkedin_emphire/TOOLING/pipeline.py adopt linkedin_emphire/VERIFIED_POSTS/<folder>/post.md --type doc --audience public
```

Then fill in the keys the gate asks for, run `pipeline.py check`, and record the change in the session
log. One post at a time, when it is actually being used.

## The ones that already have a contract

- `2026-11-06_absence-of-a-record/post.md`, the reference implementation. Front matter, gate body
  markers, headline pair plus two alternatives, box and alternative box, four verified hashtags, first
  comment, posting notes, gate 100/100 with zero blocking rows.

Read that file before writing the next post. It is the shape.
