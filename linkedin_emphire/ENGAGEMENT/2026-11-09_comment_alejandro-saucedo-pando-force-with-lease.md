---
deliverable: comment
id: 2026-11-09_comment_alejandro-saucedo-pando-force-with-lease
date: 2026-11-09
audience: Alejandro Saucedo post on OpenAI's Pando Git backend
status: ready
approved: no
warm: no
profile_checked: >-
  Alejandro Saucedo, AI and tech executive at Zalando, advisor to the UN, EU and ACM, runs The ML Engineer newsletter at
  70k+ subscribers, already following him. His post is a summary of OpenAI's "Scaling Git for OpenAI" work, framed as
  agents pushing old frameworks to their limits. He is praising the engineering and is right to.
thread: agent-scale infrastructure
---

## Why not the throughput

Every comment under this will be about ten weeks, or a petabyte on a handful of cores, or agents writing the implementation.
None of that needs saying again and none of it is his to defend. The one thing in the post he did not foreground is the
sentence in the upstream fixes, and it is the sentence that matters to anyone about to copy the design.

## What the sources establish

OpenAI's post states openly that it gives up a repository-wide point-in-time snapshot of refs and that users and agents are
agnostic to the global ordering of ref updates. Per-ref serializability is kept; reads across branches can see different
points in time. Pando advertises only a designated trunk branch on feature-branch pushes to keep ref advertisement
constant-size. Among the fixes contributed back to Git is "explicit haves", which lets clients use `--force-with-lease`
against trunk-only packs.

That last item is the tell. `--force-with-lease` is the check that stops a forced push from destroying a commit someone else
pushed in the meantime, and it works by comparing against the tip the client last saw. Advertise only trunk and the client
has no fresh tip to compare against.

## Comment, paste as is

The line I would frame is buried in the upstream fixes: explicit haves, so a client can use --force-with-lease against a trunk-only pack.

That restores a safety property the ref advertisement shortcut removed. When the server advertises only trunk, a client pushing a feature branch has no fresh view of that branch's tip, and the lease check, which is the last thing between a forced push and someone else's commit, loses the value it verifies against. They put it back on purpose. Right call, and the most transferable part of the whole post.

Throughput trades are easy to copy. The safety property you dissolve on the way is the part nobody notices until it matters.

## What not to say

No "agents cannot be trusted to write a storage system" and no implication that OpenAI shipped something unsafe. They found
it, restored it and upstreamed it, which is the behaviour worth praising. The comment adds the part his summary skipped, in
his own lane, without correcting him.

## Skip reason for the rest of the feed

Nothing else in this paste. One comment, one post, no follow-up.
