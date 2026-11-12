---
deliverable: comment
id: 2026-11-12_comment_rock-lambros-verdict-and-effect
date: 2026-11-12
audience: Rock Lambros, comment on his Application Security Podcast post about agent runtime control
status: ready
approved: no
warm: no
profile_checked: 2026-11-12 from the post as pasted. Rock Lambros works on securing agentic AI at Zenity, sits on the OWASP GenAI and Agentic AI work, and posts as a practitioner who builds and breaks rather than as a vendor announcing. The post ends with "go break it, and file issues", which is an invitation a comment can accept directly. He and I exchanged once before on environment variables and rotation, and that premise is spent, so this comment takes the runtime-control thread instead.
thread: who tells an agent no, whether the check lives outside the agent, and what a kill switch actually stops
premise_checked: checked: the Agent Control Standard is real and public, with a reference implementation and open issues, and two things in its own documentation carry this comment. First, the Guardian answers with five dispositions, allow, deny, modify, ask and defer, and the hooks cover tool calls, memory, planning transitions and subagent invocation. Second, the reference repository states plainly that the Guardian's default failure posture is proceed, that a Guardian which crashes, hangs or is unreachable stops governing silently while the host proceeds, and that the operator has to set a failure mode to deny to fail closed. The comment quotes none of the post's own figures back at him.
sources_read: read: the Agent Control Standard site and its reference repository documentation on hooks, dispositions and failure posture. The three lnk.in links, the episode, the OWASP Top 10 for LLM Applications 2026 and Apostol Vassilev's paper, are interstitials rather than sources and were not followed; the standard's own repository and site were read instead, which is where the claim in this comment is checkable.
---

## Comment, paste as is

You asked for people to break it, so here are the places I'd start, and both are about the gap between a verdict and an effect.

That gap is lanes. A deny at the hook is only as strong as the enumeration of ways an action reaches the thing it changes. A spawned shell, or a subagent holding its own credentials, and the verdict is advisory. Your gas plant comparison is right about this and is also the warning, because a trip valve works by being physically in series with the flow. Software routes around what is in series with it.

The other is the default you already name in the repository: a Guardian that is unreachable proceeds. Fail-open is the posture that turns the standard into a prompt with better formatting, and if the host cannot tell a Guardian that will answer from one that has died, the deny path is decoration.

Your kill switch question is the same question one layer down. The first thing I would write down is what the subagent inherits.
