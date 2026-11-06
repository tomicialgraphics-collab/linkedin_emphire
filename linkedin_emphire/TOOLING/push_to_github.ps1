#Requires -Version 5.1
<#
.SYNOPSIS
    Applies sandbox commits (from a .bundle file) and pushes the LinkedIn Empire repo to GitHub.

.DESCRIPTION
    Run this on your Windows machine. It will:
      1. Check for git (installs if missing via winget)
      2. Ask for your GitHub Personal Access Token (or use stored credentials)
      3. Clone the repo if you don't have it, or fetch/pull if you do
      4. Pull in the 4 sandbox commits from the .bundle file
      5. Push everything to https://github.com/Teamthy/linkedin_emphire.git (main branch)

.NOTES
    You need TWO files in the same folder as this script:
      • push_to_github.ps1    (this script)
      • linkedin-empire-commits.bundle   (the bundle file from the sandbox)

    If you don't have a GitHub Personal Access Token yet:
      https://github.com/settings/tokens → "Generate new token (classic)"
      Scopes needed: repo  (full control of private repos)
      Copy the token — you only see it once.
#>

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# ── CONFIG ──────────────────────────────────────────────────────────
$RepoUrl      = "https://github.com/Teamthy/linkedin_emphire.git"
$RepoFolder   = "linkedin_emphire"                # local folder name
$BundleFile   = "linkedin-empire-commits.bundle"  # must be next to this script
$Branch       = "main"
$GitName      = "Olusanya Timothy"
$GitEmail     = "olusanyatimothy54@gmail.com"
# ────────────────────────────────────────────────────────────────────

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  LINKEDIN EMPIRE — PUSH TO GITHUB"           -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# ── STEP 0: Make sure we're in the right directory ─────────────────
$ScriptDir = $PSScriptRoot
if (-not $ScriptDir) { $ScriptDir = Get-Location }
Set-Location $ScriptDir
Write-Host "[*] Working in: $ScriptDir" -ForegroundColor Gray

# ── STEP 1: Check for git ──────────────────────────────────────────
Write-Host "[1/7] Checking for git..." -ForegroundColor Yellow
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "    Git not found. Installing via winget..." -ForegroundColor DarkYellow
    winget install --id Git.Git -e --source winget --accept-package-agreements --accept-source-agreements | Out-Null
    # Refresh PATH so git is available in this session
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
}
Write-Host "    Git found: $((git --version 2>&1))" -ForegroundColor Green

# ── STEP 2: Check the bundle file exists ───────────────────────────
Write-Host "[2/7] Checking for bundle file..." -ForegroundColor Yellow
$BundlePath = Join-Path $ScriptDir $BundleFile
if (-not (Test-Path $BundlePath)) {
    Write-Host ""
    Write-Host "ERROR: $BundleFile not found in $ScriptDir" -ForegroundColor Red
    Write-Host "Make sure both push_to_github.ps1 and $BundleFile are in the same folder." -ForegroundColor Red
    exit 1
}
Write-Host "    Bundle found: $BundleFile" -ForegroundColor Green

# ── STEP 3: Get GitHub credentials ────────────────────────────────
Write-Host "[3/7] Setting up GitHub credentials..." -ForegroundColor Yellow

# Check if there's already a stored credential
Write-Host "    Checking for existing GitHub credentials..." -ForegroundColor Gray
$StoredCred = git config --global credential.helper 2>$null
if (-not $StoredCred) {
    # Enable Windows Credential Manager (built into Windows, stores creds securely)
    Write-Host "    Enabling Windows Credential Manager for git..." -ForegroundColor DarkYellow
    git config --global credential.helper manager-core 2>$null
}

$Pat = $env:GITHUB_PAT
if (-not $Pat) {
    Write-Host ""
    Write-Host "    ┌──────────────────────────────────────────────────────┐" -ForegroundColor DarkCyan
    Write-Host "    │  GITHUB PERSONAL ACCESS TOKEN REQUIRED                │" -ForegroundColor DarkCyan
    Write-Host "    │                                                        │" -ForegroundColor DarkCyan
    Write-Host "    │  If you have one, paste it here.                      │" -ForegroundColor DarkCyan
    Write-Host "    │  If not, create one at:                               │" -ForegroundColor DarkCyan
    Write-Host "    │  https://github.com/settings/tokens                   │" -ForegroundColor DarkCyan
    Write-Host "    │  (scopes: 'repo' — that's all you need)               │" -ForegroundColor DarkCyan
    Write-Host "    │                                                        │" -ForegroundColor DarkCyan
    Write-Host "    │  Tip: next time set `$env:GITHUB_PAT='your_token'      │" -ForegroundColor DarkCyan
    Write-Host "    │  before running to skip this prompt.                  │" -ForegroundColor DarkCyan
    Write-Host "    └──────────────────────────────────────────────────────┘" -ForegroundColor DarkCyan
    Write-Host ""
    $PatSec = Read-Host "    Paste your GitHub PAT (input is hidden)" -AsSecureString
    $BSTR   = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($PatSec)
    $Pat    = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)
}

if (-not $Pat -or $Pat.Length -lt 10) {
    Write-Host "    ERROR: No PAT provided or token looks too short." -ForegroundColor Red
    exit 1
}

# Build authenticated URL (embeds PAT so push/pull doesn't prompt)
$AuthUrl = $RepoUrl -replace "https://", "https://oauth2:$Pat@"

# ── STEP 4: Clone or open existing repo ───────────────────────────
Write-Host "[4/7] Preparing local repo..." -ForegroundColor Yellow
$RepoPath = Join-Path $ScriptDir $RepoFolder

if (-not (Test-Path $RepoPath)) {
    Write-Host "    Cloning repo into: $RepoPath" -ForegroundColor DarkYellow
    git clone $AuthUrl $RepoPath 2>&1 | ForEach-Object { Write-Host "    $_" -ForegroundColor Gray }
    Set-Location $RepoPath
} else {
    Write-Host "    Repo already exists at: $RepoPath" -ForegroundColor DarkYellow
    Set-Location $RepoPath
    Write-Host "    Fetching latest from origin..." -ForegroundColor Gray
    git fetch $AuthUrl $Branch 2>&1 | ForEach-Object { Write-Host "    $_" -ForegroundColor Gray }
    git checkout $Branch 2>&1 | ForEach-Object { Write-Host "    $_" -ForegroundColor Gray }
    git pull $AuthUrl $Branch 2>&1 | ForEach-Object { Write-Host "    $_" -ForegroundColor Gray }
}

# Set git identity if not set
if (-not (git config user.name))  { git config user.name  $GitName }
if (-not (git config user.email)) { git config user.email $GitEmail }

# ── STEP 5: Verify the bundle is compatible ───────────────────────
Write-Host "[5/7] Verifying bundle against local repo..." -ForegroundColor Yellow
$VerifyOutput = git bundle verify $BundlePath 2>&1
$VerifyExit = $LASTEXITCODE
$VerifyOutput | ForEach-Object { Write-Host "    $_" -ForegroundColor Gray }

if ($VerifyExit -ne 0) {
    Write-Host ""
    Write-Host "ERROR: Bundle verification failed." -ForegroundColor Red
    Write-Host "This usually means your local repo is not in sync with origin." -ForegroundColor Red
    Write-Host "Try deleting the $RepoFolder and running this script again (fresh clone)." -ForegroundColor Red
    exit 1
}

# ── STEP 6: Pull in the sandbox commits from the bundle ────────────
Write-Host "[6/7] Applying sandbox commits from bundle..." -ForegroundColor Yellow

# Fetch the bundle into a temporary branch
$TempBranch = "bundle-import-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
git fetch $BundlePath HEAD:refs/heads/$TempBranch 2>&1 | ForEach-Object { Write-Host "    $_" -ForegroundColor Gray }

# Check if we're already up to date (idempotent — safe to re-run)
$MergeBase = git merge-base $Branch $TempBranch
$BundleTip = git rev-parse $TempBranch
$CurrentTip = git rev-parse $Branch

if ($MergeBase -eq $BundleTip) {
    Write-Host "    Bundle commits already applied — nothing new to merge." -ForegroundColor Green
} elseif ($MergeBase -eq $CurrentTip) {
    # We can fast-forward (cleanest path)
    Write-Host "    Fast-forwarding $Branch to include bundle commits..." -ForegroundColor DarkYellow
    git merge --ff-only $TempBranch 2>&1 | ForEach-Object { Write-Host "    $_" -ForegroundColor Gray }
} else {
    # Local has diverged — do a proper merge (shouldn't happen often)
    Write-Host "    Merging bundle commits into local $Branch..." -ForegroundColor DarkYellow
    git merge $TempBranch --no-edit 2>&1 | ForEach-Object { Write-Host "    $_" -ForegroundColor Gray }
}

# Clean up the temp branch
git branch -D $TempBranch 2>&1 | Out-Null

Write-Host ""
Write-Host "    Commits now in local repo:" -ForegroundColor Green
git log --oneline -8 | ForEach-Object { Write-Host "      $_" -ForegroundColor Green }

# ── STEP 7: Push to GitHub ─────────────────────────────────────────
Write-Host ""
Write-Host "[7/7] Pushing to GitHub..." -ForegroundColor Yellow
git push $AuthUrl $Branch 2>&1 | ForEach-Object {
    if ($_ -match "error|fatal|rejected") {
        Write-Host "    $_" -ForegroundColor Red
    } elseif ($_ -match "->|Everything up-to-date") {
        Write-Host "    $_" -ForegroundColor Green
    } else {
        Write-Host "    $_" -ForegroundColor Gray
    }
}

# ── DONE ───────────────────────────────────────────────────────────
Write-Host ""
Write-Host "============================================" -ForegroundColor Green
Write-Host "  ✅  PUSH COMPLETE"                          -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host ""
Write-Host "Check https://github.com/Teamthy/linkedin_emphire to confirm." -ForegroundColor White
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "  1. Verify the VERIFIED_POSTS/ folder shows both Post #1 and Post #2" -ForegroundColor White
Write-Host "  2. Check inspiration_library.txt and the _RAW.txt are both there" -ForegroundColor White
Write-Host "  3. Schedule Post #2 for Friday 7PM WAT or Saturday 10AM WAT" -ForegroundColor White
Write-Host ""
