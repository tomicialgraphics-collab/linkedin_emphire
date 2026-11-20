---
deliverable: internal
id: 2026-11-20_connecting-claude-to-the-repo
date: 2026-11-20
audience: internal
status: ready
title: Giving Claude the ERI repository, without giving it the account
time_checked: >-
  checked: 2026-11-20 14:15 WAT, read from the system clock before this file was written.
profile_checked: >-
  Not a per-person deliverable. The steps are written for the owner and can be handed to Marvin unchanged, because the
  same two routes apply to whichever of them installs an agent on the repository of record.
premise_checked: >-
  checked: the connector flow was verified by web search on 20 November, including the three checks Claude itself runs
  (account connected, GitHub App installed, repository status). The Claude Code install command is the published npm
  package and was not executed in this workspace, which has no Node toolchain on the owner's machine to test against, so
  the file tells him what to type and what to expect rather than asserting the output.
sources_read: >-
  read: five write-ups of the Claude GitHub connection flow by web search on 20 November, including Anthropic's own
  documentation page for configuring GitHub access. No page opened directly.
---

# First: don't wire it to a repository that may not survive the week

`Teamthy/Eri-OS` is public, empty, and made before either of you agreed anything. Marvin said on 20 November that he may
stand up a project repository today and let his own agent manage it. Connecting Claude to an empty repository that gets
deleted is twenty minutes of setup and one confused afternoon.

Settle the repository of record first, then attach the agent to that one.

# Route A, local, and the right one for this week

No connector, no GitHub App, no organisation permission. Claude Code runs in the folder you already cloned, uses the git
credentials you already have, and cannot reach any repository you did not clone. Your subscription covers it.

1. Install Node 18 or newer if it is not already there, then install the client: `npm install -g @anthropic-ai/claude-code`
2. In PowerShell, from the clone: `cd "$env:USERPROFILE\Desktop\PROJECTS\<repo>"` then `claude`
3. Sign in when it asks, using the same account the subscription is on.
4. First thing to type, so you know the folder is right rather than assuming: `read README.md and quote the first heading`

What this route gives you that the connector does not: pushes happen with your name on them, the history is yours, and
revoking access is deleting a folder rather than uninstalling an app from an account.

# Route B, the GitHub Integration connector

Use this when you want Claude to read or open pull requests on a repository you have not cloned, and only after the
repository of record is settled.

1. In Claude, open **Customize → Connectors**.
2. Choose **GitHub Integration**, then **Connect**, and sign in with the GitHub account that can reach the repository.
   It does not have to be the same email as your Claude account.
3. In the same panel, click **Install on GitHub** next to the Claude GitHub App. On GitHub, choose the account or
   organisation that owns the repository, and grant **only that repository**, not all of them.
4. Back in the panel, under **Check repository status**, select the repository and confirm all three checks pass: account
   connected, app installed, repository reachable.
5. Test it with a direct file read, not a search, because search does not return private repositories regardless of
   permission: ask it to quote the first heading of the README.

Two things that go wrong and look like something else. A private repository that returns not found while public ones
read fine means the app was installed on the wrong account, not that the connection failed. And a connection that can
read but cannot open a pull request means the GitHub App was authorised but never installed on the repository; those are
two separate acts.

# The rules that apply to either route

**One repository.** Not "all repositories". An agent scoped to everything sees everything, including the repositories
this one has nothing to do with.

**It commits as itself.** The Claude GitHub App has its own identity, which is the point: a commit that cannot be traced
to a person or an agent is exactly the thing ERI exists to argue against. If an agent commits as you, nobody can tell
afterwards whether a person or a script made the change.

**Main is protected for the agent too.** No force-push, no history rewrite, no amending a commit that a record already
points at. Put this in the repository settings rather than in an instruction, because an instruction is a preference and
a branch protection rule is a fact.

**The database rule is unchanged.** `revoke update, delete on event from eri_app` applies to anything that writes,
human or not. An agent that can rewrite an append-only table can destroy the property the product is sold on.

# What to send Marvin

The same four rules, and one sentence on why: he plans to let his agent manage the repository, which is fine until it
tidies a branch that a record points at. Agreed between the two of you, it is a standard. Imposed on him, it is a
restriction.
