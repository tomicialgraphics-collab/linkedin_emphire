---
deliverable: note
id: ai-red-team-playbook-how-to-publish
date: 2026-11-09
audience: internal
status: ready
approved: no
warm: no
thread: how to publish the standalone playbook repo under the owner's own account, and why it was not created from this workspace
verified: the commands were written against the GitHub CLI interface and match the repository as built. Nothing about the publication state is asserted, since nothing has been published.
---

# Publishing the playbook

This file sits outside `ai-red-team-playbook/` on purpose. It is for you, not for the public repo.

## Why it is not already on GitHub

The GitHub connection in this workspace is authenticated as the retired identity you asked never to show in a deliverable. A public repository created under that account would put the name in the URL, on the Featured card, and in every clone line. So the repo is built, tested and packaged, and the one step left needs your own account.

## Publish in four commands

```bash
cd path/to/ai-red-team-playbook
git init -b main
git add -A
git commit -m "AI Red Team Playbook 1.0.0: 168 testable classes"
```

Then, with the GitHub CLI signed in as your own account:

```bash
gh repo create ai-red-team-playbook --public --source . --push \
  --description "168 testable classes for AI red teaming, with a coverage argument and honest intervals"
```

Without the CLI, create the empty repository in the browser, then:

```bash
git remote add origin https://github.com/YOUR-ACCOUNT/ai-red-team-playbook.git
git push -u origin main
```

## After the first push

1. **Set the social preview.** Repository settings, then upload an image. It is what shows on the Featured card, and GitHub does not take it from a file in the repository.
2. **Add the topics.** `ai-security`, `llm-security`, `red-teaming`, `ai-evaluation`, `prompt-injection`, `agentic-ai`, `checklist`. Topics are how people find it.
3. **Check the CI run.** The workflow validates the checklist, checks the rendered files match, runs the coverage example and the interval tool. It should be green on the first run because it was green here.
4. **Add the description line.** The one in the command above is used as the tagline under the name on the Featured card.

## What to attach on LinkedIn

Featured item, type Link, with the repository URL. Title it `AI Red Team Playbook` and use the description line. If the card shows the README, the first screen is the tagline, the three badges and the thesis, which is the part worth reading.

## Second deliverable, if you want one from the same work

The two reference documents behind this repo live in the private tree: the ranked explanation of why each class sits where it does, and the infrastructure counterpart. Neither belongs in the public repo, since the README has to stay a map rather than an argument. They are for conversations, not for the Featured section.
