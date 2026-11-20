# update-hfb-readme.ps1
# Adds the review attribution, approved by Behar Dalipi on 20 November 2026, to the
# README of the Host-Failure Benchmark repository, then commits it.
#
# Run it from PowerShell in the folder that holds the clone, or point it at the clone:
#
#   .\update-hfb-readme.ps1 -RepoPath C:\code\host-failure-benchmark -DryRun
#   .\update-hfb-readme.ps1 -RepoPath C:\code\host-failure-benchmark
#   .\update-hfb-readme.ps1 -RepoPath C:\code\host-failure-benchmark -Push
#
# -DryRun  makes the edit, shows the diff, then puts the file back. Nothing is committed.
# (default) makes the edit and commits it locally, and prints the commit SHA.
# -Push    also pushes main to origin.
#
# The script refuses to run if the folder is not the benchmark repository, if you are not on
# main, if the working tree is dirty, or if it cannot find the paragraph it is meant to edit.
# It never forces anything and never rewrites history.

[CmdletBinding()]
param(
  [string]$RepoPath = ".",
  [switch]$DryRun,
  [switch]$Push
)

$ErrorActionPreference = "Stop"

function Stop-Here {
  param([string]$Message)
  Write-Host ""
  Write-Host "STOP: $Message" -ForegroundColor Red
  exit 1
}

# The approved wording. Do not edit these two strings without the reviewer's approval.
$paragraph = @'
Version 3 of this benchmark, held at dab7483e (the SHA-256 prefix of the version 3 ZIP), was reviewed by Behar Dalipi, a research collaborator who coordinated two rounds of AI-assisted technical review. Every finding he raised is answered in the register, either by the patch that closes it or by the reason it stays open; the corrections and the verdicts are mine. His contribution is verification and adversarial testing, and expressly not an endorsement of the benchmark. The results cover the modes tested, and other filesystems and concurrent writers are unverified.
'@

$coauthor = @'
Behar Dalipi is also a co-author of the benchmark suite. The review described above concerned Olusanya Timothy's implementation. The contribution record identifies his authorship and review contributions.
'@

$commitMessage = "README: record the review of version 3 and Behar Dalipi's co-authorship (approved 20 Nov 2026)"

# ---- pre-flight ----------------------------------------------------------------

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
  Stop-Here "git is not on PATH in this shell. Open a new PowerShell window or install Git for Windows."
}

if (-not (Test-Path $RepoPath)) { Stop-Here "No such folder: $RepoPath" }
$RepoPath = (Resolve-Path $RepoPath).Path
Push-Location $RepoPath

if (-not (Test-Path (Join-Path $RepoPath ".git"))) {
  Stop-Here "$RepoPath is not a git repository. Point -RepoPath at the clone of host-failure-benchmark."
}

$remote = git remote get-url origin 2>$null
if ($LASTEXITCODE -ne 0 -or -not $remote) { Stop-Here "This clone has no origin remote." }
if ($remote -notmatch "host-failure-benchmark") {
  Stop-Here "origin points at $remote, which is not host-failure-benchmark. Refusing to touch it."
}

$branch = git rev-parse --abbrev-ref HEAD
if ($branch -ne "main") {
  Stop-Here "You are on '$branch'. Switch to main first: git checkout main"
}

$dirty = git status --porcelain
if ($dirty) {
  Stop-Here "The working tree has uncommitted changes. Commit or stash them first, so this change is alone in the diff."
}

Write-Host "Fast-forwarding main from origin..."
git pull --ff-only origin main
if ($LASTEXITCODE -ne 0) { Stop-Here "Could not fast-forward main. Sort that out before editing." }

if (-not (Test-Path (Join-Path $RepoPath "README.md"))) { Stop-Here "There is no README.md in $RepoPath" }

# ---- the edit -------------------------------------------------------------------

$readmePath = Join-Path $RepoPath "README.md"
$text = [System.IO.File]::ReadAllText($readmePath)

$newline = "`n"
if ($text.Contains("`r`n")) { $newline = "`r`n" }

if ($text.Contains("Behar Dalipi is also a co-author of the benchmark suite")) {
  Stop-Here "The clarification is already in the README. Nothing to do."
}

if ($text.Contains("was reviewed independently by Behar Dalipi")) {
  Write-Host "Found the earlier wording. Applying both of the reviewer's changes."
  $text = $text.Replace("was reviewed independently by Behar Dalipi", "was reviewed by Behar Dalipi")
  $endOfParagraph = "other filesystems and concurrent writers are unverified."
  if (-not $text.Contains($endOfParagraph)) {
    Stop-Here "Found the attribution but not the end of it. Open README.md and check it by hand."
  }
  $text = $text.Replace($endOfParagraph, $endOfParagraph + $newline + $newline + $coauthor)
}
else {
  Write-Host "Attribution not present yet. Inserting the approved text."
  $opening = "what can still be known afterwards?"
  if (-not $text.Contains($opening)) {
    Stop-Here "Could not find the opening paragraph to insert after. Open README.md and check it by hand."
  }
  $block = $paragraph + $newline + $newline + $coauthor
  $text = $text.Replace($opening, $opening + $newline + $newline + $block)
}

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText($readmePath, $text, $utf8NoBom)

# Verify before showing anything as done.
$check = [System.IO.File]::ReadAllText($readmePath)
if (-not $check.Contains("was reviewed by Behar Dalipi"))      { Stop-Here "The edit did not apply. README.md is unchanged in content." }
if (-not $check.Contains("is also a co-author of the benchmark suite")) { Stop-Here "The clarification did not apply. README.md is unchanged in content." }
if ($check.Contains("reviewed independently by"))              { Stop-Here "The old wording is still there. README.md is unchanged in content." }

Write-Host ""
Write-Host "Diff:" -ForegroundColor Cyan
git --no-pager diff -- README.md

if ($DryRun) {
  git checkout -- README.md
  Write-Host ""
  Write-Host "Dry run complete. The file has been put back, nothing was committed and nothing was pushed." -ForegroundColor Yellow
  exit 0
}

# ---- commit ---------------------------------------------------------------------

git add README.md
git commit -m $commitMessage
if ($LASTEXITCODE -ne 0) { Stop-Here "The commit failed. The edit is still in the working tree." }

$sha = (git rev-parse HEAD).Trim()

if ($Push) {
  git push origin main
  if ($LASTEXITCODE -ne 0) { Stop-Here "The commit is made but the push failed. Run: git push origin main" }
  Write-Host ""
  Write-Host "Pushed to main." -ForegroundColor Green
}
else {
  Write-Host ""
  Write-Host "Committed locally, not pushed. To publish: git push origin main"
}

Write-Host ""
Write-Host "Commit: $sha" -ForegroundColor Green
Write-Host ""
Write-Host "Send Behar Dalipi two things: the README page, and the commit above."
Write-Host "The commit is not the ZIP hash. The ZIP hash is dab7483e and it stays out of this message."
