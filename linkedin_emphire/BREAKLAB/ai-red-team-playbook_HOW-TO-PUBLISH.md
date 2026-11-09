---
deliverable: note
id: ai-red-team-playbook-how-to-publish
date: 2026-11-09
audience: internal
status: ready
approved: no
warm: no
thread: how the playbook gets published to Teamthy/Ai-Red-Team-Playbook, and why the push is the one step this workspace cannot complete
verified: the repository exists, is public, is empty, and the workspace account has pull access only. The push attempt returned 403 permission denied, which is recorded below rather than described.
---

# Publishing the playbook to Teamthy/Ai-Red-Team-Playbook

## Where things stand

- Repo exists: `https://github.com/Teamthy/Ai-Red-Team-Playbook`, public, empty, default branch `main`.
- Local source, committed and ready: `/home/user/ai-red-team-playbook`, 28 files, branch `main`, remote `origin` already pointing at the repo, commit author set to `Olusanya Timothy <olusanyatimothy54@gmail.com>` so the public history carries your name and not the retired one.
- Checks green on that copy: validate, render, coverage, wilson.

What stops it:

```
remote: Permission to Teamthy/Ai-Red-Team-Playbook.git denied to tomicialgraphics-collab.
fatal: unable to access ...: The requested URL returned error: 403
```

The workspace account can read the repo and nothing else. That is the whole of the problem, and it is one permission away from solved.

## Route A, fastest: invite the workspace account, then I push

In the repository, Settings, Collaborators, Add people, paste `tomicialgraphics-collab`, role **Write**. No need to accept anything on this side.

Then say so in the chat, and the next turn is:

```bash
cd /home/user/ai-red-team-playbook
git push -u origin main
gh api -X PUT repos/Teamthy/Ai-Red-Team-Playbook/topics \
  -f "names[]=ai-security" -f "names[]=llm-security" -f "names[]=red-teaming" \
  -f "names[]=ai-evaluation" -f "names[]=prompt-injection" -f "names[]=agentic-ai" \
  -f "names[]=checklist"
gh repo edit Teamthy/Ai-Red-Team-Playbook \
  --description "168 testable classes for AI red teaming, with a coverage argument and honest intervals"
```

You can remove the collaborator straight after the push. The commit author is already yours, so nothing in the history changes when it goes.

## Route B: you push in two minutes

The folder is also packaged as `BREAKLAB/ai-red-team-playbook-1.0.0.zip` inside the portfolio repository. Download it, unpack, then:

```powershell
git clone https://github.com/Teamthy/Ai-Red-Team-Playbook.git
Copy-Item -Path .\ai-red-team-playbook\* -Destination .\Ai-Red-Team-Playbook\ -Recurse -Force
cd .\Ai-Red-Team-Playbook
git add -A
git commit -m "AI Red Team Playbook 1.0.0: 168 testable classes"
git push -u origin main
```

Set the author first if the machine is not already configured:

```powershell
git config user.name "Olusanya Timothy"
git config user.email "olusanyatimothy54@gmail.com"
```

## After the first push, whichever route

1. **Social preview.** Settings, then upload an image. GitHub does not take it from a file in the repository, and it is what the LinkedIn Featured card shows.
2. **Topics.** The command above, or the gear icon on the repo page.
3. **Description.** The one-liner above. It becomes the line under the name on the card.
4. **CI.** The workflow should go green on the first run, since it is green here.
5. **Pin it.** Profile, Customize your pins, choose the repo, so it sits above the other work.

## Keeping the two copies in step

`BREAKLAB/ai-red-team-playbook/` in the portfolio repository stays the source of truth, and `/home/user/ai-red-team-playbook` is the publishing copy. After any edit, refresh the publishing copy with:

```bash
cp -a /home/user/linkedin_emphire/linkedin_emphire/BREAKLAB/ai-red-team-playbook/. /home/user/ai-red-team-playbook/
cd /home/user/ai-red-team-playbook
python3 tools/validate.py
python3 tools/render.py
git add -A
git commit -m "update the checklist"
git push
```
