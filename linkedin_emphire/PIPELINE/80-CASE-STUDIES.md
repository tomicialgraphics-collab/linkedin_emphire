---
deliverable: doc
id: 80-case-studies
date: 2026-11-10
audience: internal
status: ready
---

# Case studies, and the permission ladder

The strongest artefacts in this repo are client engagements: the FORAY register with its reopened
finding, and the file-hash recomputation for Evelyne-Claudia. Two people can see them. That is correct
until the client says otherwise (R19), and the point of this system is that the ask gets made early and
the page gets written while the work is fresh.

## Where a case study lives

`CLIENTS/<client>/CASE-STUDY-<n>_<slug>.md`, one file per milestone, indexed in
`STATE/CASE-STUDY-INDEX.md`. It is written for a reader who has never met the client and never will:
a hiring manager, a prospect, or somebody deciding whether to book a call.

## The permission ladder, in front matter

| value | means | what it permits |
| --- | --- | --- |
| `permission: not-requested` | the ask has not been made | drafting only, never sharing |
| `permission: requested: <date>` | asked, waiting | drafting only |
| `permission: granted: <date, <how>>` | in writing, an email or a message that says yes | sharing, in the form they approved |
| `permission: granted-anonymous:` | yes, without their name | sharing, client unnamed |

The gate blocks any case study with `status: ready` or later whose permission is not `granted`. A draft
is allowed at `not-requested`, because the draft is what you ask them to approve: nobody should be
asked to approve a page that does not exist yet. Write it, then ask.

## What a case study contains, in this order

1. **The situation in three sentences**, no client name unless permitted, no industry detail that
   identifies them.
2. **What was tested**, in the terms the client used, with the version and the surface (R35).
3. **What was found**, including anything that was wrong first and corrected. A case study that has no
   correction in it reads as marketing, and the audiences this is for can tell.
4. **What changed**, which is the only section a buyer reads closely.
5. **The artefact**, by hash and size, so the claim is checkable without the file being public.
6. **What could not be established**, in one short paragraph. This is the section that makes the other
   five believable.

## De-identification, before the ask

Names, roles, employer, contract value, dates precise enough to identify a tender, and any screenshot
with a header in it. Remove all six before the page is shown to the client, so the version they approve
is the version that can travel.

## The ask, once, early

One message, at the first milestone, not at the end of the engagement: the page exists, here it is,
may I show it de-identified, and here is exactly what I would remove. A client who is asked at the end
has already stopped thinking about the work. A client asked at the first milestone is still pleased
with it.
