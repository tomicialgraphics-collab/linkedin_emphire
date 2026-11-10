# 50 CONTRACT

Every deliverable carries its own paperwork. The reason is narrow and practical: a file with no front
matter cannot be gated, a file that cannot be gated cannot be trusted, and a file that is not
journalled cannot be proved to exist. The owner has been sent work twice that was not ready. This is
the fix.

---

## 1. Front matter

At the top of every deliverable, between two `---` lines:

```yaml
---
deliverable: post            # post | comment | dm | email | doc | internal
id: 2026-11-06_absence-of-a-record
date: 2026-11-06             # the date the file speaks to, not the date you wrote it
audience: public             # public | client | reviewer | hiring | vendor | internal
status: ready                # draft | ready | sent | posted | superseded | archived
approved: no                 # yes only when the owner has approved a send
---
```

The parser is a small subset of YAML, on purpose, because the repo has no dependencies: `key: value`,
lists as `[a, b]`, comments after `#`. Nothing nested.

### Required for every file

`deliverable`, `id`, `date`, `audience`, `status`.

### Required for a post

`template`, `headline`, `subheadline`, `headline_alt`, `subheadline_alt`, `headline_alt2`,
`subheadline_alt2`, `box`, `box_alt`, `hashtags`.

### Required for a comment or a DM

`profile_checked`, which is the date you read the person's profile and something only they said.
`warm: yes` if a link is allowed.
`sources_read`, from 2026-11-10 on. **Every link a post attaches is opened before the comment is
written** (owner instruction, 2026-11-09: "please always read it"). The line records what happened:

| value | means |
| --- | --- |
| `read: <what it was> <date>` | opened it, and the comment is written against it |
| `none: nothing attached` | there was no link, paper, film, thread or repository to open |
| `blocked: <why>, so <what the comment claims anyway>` | it will not open, with the reason and the consequence |

A post points at something far more often than it looks. A paper, an SSRN version, a film, a waitlist,
a publisher page, another post, a repository. A landing page or a waitlist still counts as read: open
it, say what it turned out to be, and the line reads `read:`. `blocked:` is for material that will not
open at all, and it has to say what the comment claims without it.

There is no "I read the post so the link does not matter". That was the earlier version of this rule
and the owner struck it out on 2026-11-09, the same evening. Working from a summary of a source and
working from the source are different acts, and only one of them can be checked afterwards.

### When the file leaves the repo as it stands

Some artefacts are read by the client or the reviewer exactly as written: a review register, a probe,
a reply. Internal front matter in one of those is noise to the reader and a leak at worst. Those files
carry no front matter and are gated with `--profile exported`:

```
./emphire check <file> --profile exported
```

That profile runs the full text rules, keeps the retired-identity check blocking, and skips the front
matter requirement, because the paperwork for an exported artefact lives in `STATE/DELIVERY-LOG.md`
instead. It is not a way past a rule: R26 and R20 are the only checks it changes, and both because
their evidence is a header the file deliberately does not have.

### Required for a review or a scope

`client`, `private: yes`, and `fix_verified: true` only when the post-fix run is attached.

## 2. File shape, by type

| Type | Where it goes | Ships with |
|---|---|---|
| post | `VERIFIED_POSTS/YYYY-MM-DD_slug/post.md` | `FIRST_COMMENT.md`, `metadata.json`, a row in `INDEX.md` |
| comment | `ENGAGEMENT/drafts_YYYY-MM-DD-feed.md` | one section per post, the person named, the thread linked |
| dm | `ENGAGEMENT/dm_YYYY-MM-DD_person.md` | the person's argument quoted back, once |
| review | `CLIENTS/<client>/<date>/FINDINGS-*.md` | the probe script, the result files, the patch, a SHA-256 |
| scope | `PROJECTS/<date>_<name>/*.md` | the questions you need answered, numbered |
| application | `APPLICATIONS/<date>_<role>/` | the send package, the sent log, a follow-up date |
| internal | `SESSION_LOG/`, `STATE/`, `PIPELINE/` | nothing |

## 3. The post contract, in full

A post is ready when all of these are true, and the gate checks the first nine:

1. `headline` is under 120 characters, is a statement, and is the first line of the body.
2. `headline` plus `subheadline` is inside 200 characters.
3. Two alternative pairs are given, one of them cost-led if the audience is a buyer.
4. `box` is one to three words, does not appear in the headline, and has a `box_alt`.
5. Three to five hashtags, every one in `PIPELINE/registry/hashtags.json`, on the final line.
6. `template` is one of T1 to T14, and it is not the template used the day before.
7. The human gate is 90 or above with zero errors.
8. `FIRST_COMMENT.md` exists and holds one idea, not a summary.
9. A row exists in `VERIFIED_POSTS/INDEX.md` with the date, the slug, the template and the slot.
10. Manual: the box passes the portability test, and the headline is not something any other writer
    in this lane could have written that day.

## 4. What "delivered" means

A file is delivered when `STATE/DELIVERY-LOG.md` has a row with its path, its size, its SHA-256, its
gate verdict, who received it and how. Anything else is a draft, however finished it looks.

## 5. Naming

- Dated folders: `YYYY-MM-DD_slug`, lowercase, hyphens, no spaces.
- Files that go to a person: `FINDINGS-01-topic.md`, `REPLY-to-Name.md`, `SCOPE-YYYY-MM-DD.md`.
- Never two files with the same name in two places. If a file has a `-v2`, the `v1` is deleted or
  moved to `ARCHIVE/`, never left beside it.
