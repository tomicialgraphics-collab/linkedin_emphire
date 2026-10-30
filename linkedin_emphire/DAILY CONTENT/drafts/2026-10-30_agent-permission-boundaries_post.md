# 2026-10-30 Agent permission boundaries post (personal feed)

Source: owner's 10-30 request, informed by Tanya Janca's 10-30
agent-permissions post and episode, captured as engagement entry 11 in
`ENGAGEMENT/published_comments/2026-10-30_to_2026-10-30_verbatim.md`.
Episode link was read in full before the comment and post work.

## HEADLINE
Permission is not implied by the prompt

## SUBHEADLINE
Let agents move quickly inside a safe workspace. Put approval at the point of consequence.

## POST (paste-ready, 274w / 1627c, DRAFTED)
Gates: 2 contractions; no dash separators; no banned terms; hashtags on
last line only (3 targeted). No link.

An AI agent should not inherit permissions from the goal you gave it.

“Build me an app” is not the same as “run it, connect it to a service, publish it, and schedule it.” Those are different actions, with different consequences.

The useful question isn't only what the agent was asked to do. It’s what it can do without another person’s approval.

I’d check the permissions in stages:

Can it read files beyond the project it is working on?
Can it execute code, install packages, or change the environment?
Can it reach a network or send data to an external service?
Can it create something that persists after the session, like a scheduled task?
Can it publish, deploy, or affect someone else?

Writing code in a disposable workspace is a different risk from running that code on your machine. Suggesting an API is different from sending data to it. Preparing a deployment is different from making it public. Keep those actions separate, and make the boundary visible before the agent reaches it.

This doesn't mean asking for approval after every small step. That trains people to click through. Let the agent move quickly inside a safe workspace. Require a person to decide when it crosses into another system, exposes data, or creates a lasting change.

The prompt describes the task. The permission set defines the possible side effects. If the two are treated as the same thing, a helpful agent can do much more than anyone intended.

Autonomy should save us from micromanaging the work, not from deciding what the system is allowed to do.

Where would you draw the boundary?

#AISecurity #SoftwareEngineering #AIAgents
