---
deliverable: internal
id: 2026-11-20_call-card_travis-windows-demo
date: 2026-11-20
audience: internal
status: ready
title: Travis demo, Windows PowerShell 5.1, no sed
sources_read: >-
  read: 04-prefix-collision.log in this workspace, checked line by line for the patterns below. No page opened.
---

# The same demo on Windows

The call card assumed a Unix shell. He is in PowerShell 5.1 at `C:\WINDOWS\system32`, so `sed` does not exist and the working directory is not the repo.

Say this first, once, and then move: "The commands I gave you were for a Unix shell. Same file, same evidence, I'll print it with PowerShell."

## 1. Find the record and go there (one line, paste whole)

```powershell
$f = Get-ChildItem $HOME -Filter 04-prefix-collision.log -Recurse -ErrorAction SilentlyContinue | Select-Object -First 1; if ($f) { cd $f.DirectoryName; $f.FullName } else { "NOT FOUND under $HOME" }
```

## 2. The failure, from the recorded run

```powershell
Select-String -Path .\04-prefix-collision.log -Pattern "digest of the stored object"
```

The first rows show the sixteen-character digest `4889096bc551a891` marked `pass`.

```powershell
Select-String -Path .\04-prefix-collision.log -Pattern "passed, .*failed"
```

Shows `50 passed, 0 failed` twice, then `54 passed, 0 failed`, then `53 passed, 1 failed`.

Say over it: "Sixteen characters where the true digest is sixty-four, and the suite agrees with it. Same file, later in the run, the same row fails."

## 3. The corrected comparison, isolated

```powershell
Select-String -Path .\04-prefix-collision.log -Pattern "digest of the stored object" | Select-Object -Last 2
Select-String -Path .\04-prefix-collision.log -Pattern "passed, .*failed" | Select-Object -Last 1
```

On screen: `got 4889096bc551a89116ee8e83..., manifest says 4889096bc551a891ffffffff...` and `53 passed, 1 failed`.

## 4. The check that is designed to fail

```powershell
py .\03-verify_run_record.py --self-test; $LASTEXITCODE
```

If `py` is not there, use `python`. Expect the FAIL line about prefix collision, then `self-test: 0 passed, 1 failed`, then `0` as the exit code.

Say: "It fails on purpose and exits zero only when it fails. That is the whole point, and it is why this looks like a wrong result."

## If the folder is not on this machine

Do not search the whole disk on a call. Say the record lives on the machine you build on, offer it as an email within the hour, and move to the ten minutes on his number. Do not narrate the problem past one sentence.
