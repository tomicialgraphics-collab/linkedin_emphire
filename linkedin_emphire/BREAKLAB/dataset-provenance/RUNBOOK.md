# Runbook: auditing a gated dataset without cloning it

Written for PowerShell 5.1 on Windows, because that is the machine this is going to run on. No `&&` anywhere; each step is a line you can paste on its own.

## Why this does not start with a clone

Four reasons, in the order they can hurt you.

**Size.** The card claims 95 GB in two places and 16 GB in another. The machine this was written on has 19 GB free. A clone either fails halfway or fills a disk that other work depends on, and the failure mode is a partial repository that looks complete.

**Executable artefacts.** The platform's own scanner flags two files in this repository as unsafe. A clone fetches them. The audit needs none of them, because every question it answers can be answered from a listing of paths and sizes.

**Licence.** If the material cannot be redistributed, then a copy in Drive or a private repository is a copy you have to destroy on request. Making one before you know the answer is the wrong order.

**GitHub will not take it anyway.** A single file over 100 MB is rejected outright, and this repository is described as gigabytes per folder.

So: pull the inventory, audit the inventory, then decide whether to fetch any content at all.

## Step 1. Get the file tree

You need a Hugging Face token with read access, because the dataset is gated and you have already been granted access on your account.

```powershell
$env:HF_TOKEN = "hf_xxxxxxxxxxxxxxxxxxxxx"
$h = @{ Authorization = "Bearer $env:HF_TOKEN" }
$u = "https://huggingface.co/api/datasets/Vyber07/cyber-security/tree/main?recursive=true"
$tree = Invoke-RestMethod -Uri $u -Headers $h
$tree.Count
$tree | ConvertTo-Json -Depth 8 | Set-Content -Encoding UTF8 tree.json
```

`$tree.Count` should print the number of files, and the card says 507. If it prints 1,000 the response was paginated and you need the next page from the `Link` header before the audit means anything.

This costs a few hundred kilobytes and no content.

## Step 2. Run the audit

```powershell
python audit.py --tree tree.json --dataset "Vyber07/cyber-security" --claim "16 GB" --claim "95 GB" --claim "< 1K" --out report.md --json report.json
```

The exit code is 1 when something blocks, which is what you want in a pipeline. Read `report.md`; it is written for a person.

## Step 3. Record the two flagged files

The banner says two files were scanned as unsafe but does not name them in the page text. Open the repository's **Files and versions** tab, use the scan filter if it is shown, and write the paths into `unsafe.txt`, one per line:

```powershell
# unsafe.txt, one path per line, taken by hand from the Files tab
python audit.py --tree tree.json --unsafe unsafe.txt --out report.md
```

Do not guess which ones they are from the extension. The flag comes from the platform's scanner and belongs to specific files.

## Step 4. If you need content, take a slice

Only for reading, only in a scratch directory, and only `.json`:

```powershell
cd $env:TEMP
pip install -U "huggingface_hub[cli]"
$env:HF_HOME = "$env:TEMP\hfscratch"
huggingface-cli download Vyber07/cyber-security --repo-type dataset --include "red-team/*.json" --local-dir .\slice --token $env:HF_TOKEN
```

Then verify what arrived before opening it:

```powershell
Get-ChildItem .\slice -Recurse -File | ForEach-Object { $_.FullName + " " + $_.Length }
Get-FileHash .\slice\red-team\*.json -Algorithm SHA256
```

`oid` in the tree JSON is the git blob hash, not the SHA-256 of the file. For LFS objects the tree carries `lfs.sha256`, which is the hash you compare against. Comparing an `oid` to a `Get-FileHash` result will mismatch and that mismatch means nothing.

## Step 5. When you are done

```powershell
Remove-Item -Recurse -Force .\slice
Remove-Item Env:\HF_TOKEN
```

If the licence verdict is blocked, leaving the slice on disk is a copy of material you have no right to redistribute, sitting in a folder you will forget about.

## What the audit will not tell you

It will not tell you whether the content is good, correct, current or safe. It answers five questions and none of them is about quality:

1. Does the repository agree with the card about its own size.
2. How many files are usable and what are the rest.
3. Where the content came from and whether that source permits redistribution.
4. Whether the repository carries artefacts that execute on load.
5. Whether it holds material that also serves as an evaluation set.

A dataset can pass all five and still be worthless. None of the five can be answered after a model is trained on it, which is why they are asked first.
