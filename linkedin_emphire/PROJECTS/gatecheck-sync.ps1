<#
.SYNOPSIS
  Pull the current gatecheck source straight into your local folder with git,
  verify it, and optionally commit and push it to your own repo.

.DESCRIPTION
  No browser download, no copying files by hand. The script does a sparse,
  shallow clone of the source repository, takes only the gatecheck folder,
  copies it over your working copy, deletes the old baseline (the one that
  was written by the broken run), reinstalls the package, runs the tests and
  runs the demo against both agents.

  Your folder keeps its own .git and .venv. Nothing is deleted except
  .gatecheck, and you can keep that too with -KeepBaseline.

.PARAMETER Path
  Your local gatecheck folder. Defaults to the folder you are in.

.PARAMETER Push
  After a successful verification, git add, commit and push in your repo.

.NOTES
  Run it as a file. Pasting it into an interactive prompt line by line
  breaks on #Requires and on the try/finally blocks.

.EXAMPLE
  cd C:\Users\Timothy\projects\gatecheck
  powershell -ExecutionPolicy Bypass -File .\gatecheck-sync.ps1

.EXAMPLE
  .\gatecheck-sync.ps1 -Path C:\projects\gatecheck -Push
#>
#Requires -Version 5.1
[CmdletBinding()]
param(
    [string]$Path = (Get-Location).Path,
    [string]$Source = "https://github.com/tomicialgraphics-collab/linkedin_emphire.git",
    [string]$Branch = "arena/6511b4f9-linkedin-emphire",
    [string]$SubPath = "linkedin_emphire/PROJECTS/gatecheck",
    [switch]$KeepBaseline,
    [switch]$Push,
    [switch]$SkipTests
)

$ErrorActionPreference = "Stop"

function Step([string]$Text) {
    Write-Host ""
    Write-Host "== $Text" -ForegroundColor Cyan
}

function AssertExit([string]$What) {
    if ($LASTEXITCODE -ne 0) {
        throw "$What failed with exit code $LASTEXITCODE"
    }
}

# 1. Make sure we are pointed at a gatecheck folder and not somewhere else,
#    because the next step copies over whatever is here.
$Path = (Resolve-Path -LiteralPath $Path).Path
$marker = Join-Path $Path "gatecheck/cli.py"
if (-not (Test-Path -LiteralPath $marker)) {
    throw "No gatecheck/cli.py under $Path. Run this from your gatecheck folder or pass -Path."
}

Step "syncing $Branch into $Path"

$tmp = Join-Path ([System.IO.Path]::GetTempPath()) ("gatecheck-sync-" + [guid]::NewGuid().ToString("N").Substring(0, 8))
$src = Join-Path $tmp "src"

try {
    # 2. Shallow, sparse clone. Only the gatecheck folder comes down,
    #    so this stays small even though the source repo is not.
    New-Item -ItemType Directory -Path $tmp -Force | Out-Null
    $cloneArgs = @("clone", "--depth", "1", "--filter=blob:none", "--sparse", "--branch", $Branch, $Source, $src)
    Step "git clone"
    & git @cloneArgs
    AssertExit "git clone"

    Step "git sparse-checkout set $SubPath"
    & git -C $src sparse-checkout set $SubPath
    AssertExit "git sparse-checkout"

    $rev = (& git -C $src rev-parse --short HEAD).Trim()
    $subject = (& git -C $src log -1 --pretty=%s).Trim()
    Write-Host "source commit $rev  $subject"

    $from = Join-Path $src $SubPath
    if (-not (Test-Path -LiteralPath $from)) {
        throw "The source repo has no $SubPath at $Branch."
    }

    # 3. Copy over the top level of the source folder. -Force picks up
    #    .gitignore, .gitattributes and .github, which a plain glob skips.
    Step "copying files"
    Get-ChildItem -LiteralPath $from -Force | ForEach-Object {
        Copy-Item -LiteralPath $_.FullName -Destination $Path -Recurse -Force
        Write-Host ("  " + $_.Name)
    }
}
finally {
    if (Test-Path -LiteralPath $tmp) {
        Remove-Item -LiteralPath $tmp -Recurse -Force -ErrorAction SilentlyContinue
    }
}

# 4. The baseline your broken run wrote holds zero findings. Keeping it is
#    what made seven real findings look fixed, so it goes.
$baseline = Join-Path $Path ".gatecheck"
if (Test-Path -LiteralPath $baseline) {
    if ($KeepBaseline) {
        Write-Host ""
        Write-Host "kept $baseline as asked. If it was written by a run that found nothing, delete it." -ForegroundColor Yellow
    }
    else {
        Remove-Item -LiteralPath $baseline -Recurse -Force
        Write-Host ""
        Write-Host "removed $baseline (old baseline and run artifacts)" -ForegroundColor Yellow
    }
}

# 5. Use the venv the folder already has, if any.
$python = Join-Path $Path ".venv/Scripts/python.exe"
if (-not (Test-Path -LiteralPath $python)) {
    $python = "python"
}
Write-Host "python: $python"

Push-Location -LiteralPath $Path
try {
    Step "pip install -e .[dev]"
    & $python -m pip install -q -e ".[dev]"
    AssertExit "pip install"

    if (-not $SkipTests) {
        Step "pytest"
        & $python -m pytest -q
        AssertExit "pytest (expected 41 passed, 2 skipped with no engines installed)"

        # 6. Exit 2 on the vulnerable agent is the correct answer. Exit 0
        #    would mean the gate had gone back to lying.
        Step "demo 1 of 4: vulnerable agent, nothing recorded yet"
        & $python -m gatecheck run --demo vulnerable --out .gatecheck/runs/sync-1
        $vulnerable = $LASTEXITCODE
        Write-Host "exit code $vulnerable (expect 2 = blocked, 7 findings)"
        if ($vulnerable -ne 2) {
            Write-Host "expected 2. Read the output above before trusting this copy." -ForegroundColor Yellow
        }

        # 7. Record today's state. Exit 2 again is correct: the run is
        #    blocked, and those seven findings become what you accepted.
        Step "demo 2 of 4: record those seven as the baseline"
        & $python -m gatecheck run --demo vulnerable --out .gatecheck/runs/sync-2 --update-baseline
        $recorded = $LASTEXITCODE
        Write-Host "exit code $recorded (expect 2, and a line saying baseline updated)"
        if (-not (Test-Path -LiteralPath (Join-Path $Path ".gatecheck/baseline.json"))) {
            Write-Host "no baseline was written. The gate only refuses when a tool did not run." -ForegroundColor Yellow
        }

        # 8. Now a pass means something: the findings are gone, not unseen.
        Step "demo 3 of 4: hardened agent against that baseline"
        & $python -m gatecheck run --demo fixed --out .gatecheck/runs/sync-3
        $fixed = $LASTEXITCODE
        Write-Host "exit code $fixed (expect 0, and 7 fixed)"
        if ($fixed -ne 0) {
            Write-Host "expected 0." -ForegroundColor Yellow
        }

        # 9. The same broken agent, unchanged, must not be news any more.
        Step "demo 4 of 4: vulnerable agent again, same baseline"
        & $python -m gatecheck run --demo vulnerable --out .gatecheck/runs/sync-4
        $again = $LASTEXITCODE
        Write-Host "exit code $again (expect 0, 7 findings, 0 new)"
        if ($again -ne 0) {
            Write-Host "expected 0. Known findings should stop blocking." -ForegroundColor Yellow
        }
    }
}
finally {
    if (Test-Path -LiteralPath $tmp) {
        Remove-Item -LiteralPath $tmp -Recurse -Force -ErrorAction SilentlyContinue
    }
}

# 4. The baseline your broken run wrote holds zero findings. Keeping it is
#    what made seven real findings look fixed, so it goes.
$baseline = Join-Path $Path ".gatecheck"
if (Test-Path -LiteralPath $baseline) {
    if ($KeepBaseline) {
        Write-Host ""
        Write-Host "kept $baseline as asked. If it was written by a run that found nothing, delete it." -ForegroundColor Yellow
    }
    else {
        Remove-Item -LiteralPath $baseline -Recurse -Force
        Write-Host ""
        Write-Host "removed $baseline (old baseline and run artifacts)" -ForegroundColor Yellow
    }
}

# 5. Use the venv the folder already has, if any.
$python = Join-Path $Path ".venv/Scripts/python.exe"
if (-not (Test-Path -LiteralPath $python)) {
    $python = "python"
}
Write-Host "python: $python"

Push-Location -LiteralPath $Path
try {
    Step "pip install -e .[dev]"
    & $python -m pip install -q -e ".[dev]"
    AssertExit "pip install"

    if (-not $SkipTests) {
        Step "pytest"
        & $python -m pytest -q
        AssertExit "pytest (expected 42 passed, 1 skipped)"

        # 6. The demo. Exit 2 on the vulnerable agent is the correct answer,
        #    exit 0 would mean the gate went back to lying.
        Step "demo: vulnerable agent"
        & $python -m gatecheck run --demo vulnerable --out .gatecheck/runs/sync-vulnerable
        $vulnerable = $LASTEXITCODE
        Write-Host "exit code $vulnerable (2 = blocked with 7 findings, which is right)"
        if ($vulnerable -ne 2) {
            Write-Host "expected 2. Read the output above before trusting this copy." -ForegroundColor Yellow
        }

        Step "demo: hardened agent"
        & $python -m gatecheck run --demo fixed --out .gatecheck/runs/sync-fixed
        $fixed = $LASTEXITCODE
        Write-Host "exit code $fixed (0 = the seven findings are gone)"
        if ($fixed -ne 0) {
            Write-Host "expected 0." -ForegroundColor Yellow
        }
    }
}
finally {
    Pop-Location
}

# 7. Put it in your repo, if you asked for that.
if ($Push) {
    Step "git add / commit / push"
    if (-not (Test-Path -LiteralPath (Join-Path $Path ".git"))) {
        Write-Host "$Path is not a git repo, skipping." -ForegroundColor Yellow
    }
    else {
        & git -C $Path add -A
        AssertExit "git add"
        $pending = (& git -C $Path status --porcelain) -join ""
        if ([string]::IsNullOrWhiteSpace($pending)) {
            Write-Host "nothing to commit, your repo already matches $rev"
        }
        else {
            & git -C $Path commit -q -m "gatecheck 0.1.1: a run that reaches no engine is an error, not a pass"
            AssertExit "git commit"
            & git -C $Path push
            AssertExit "git push"
            Write-Host "pushed $rev to origin"
        }
    }
}

Step "done"
Write-Host "source: $rev"
Write-Host "folder: $Path"
Write-Host ""
Write-Host "next:"
Write-Host "  .\.venv\Scripts\Activate.ps1"
Write-Host "  python -m gatecheck run --demo vulnerable --update-baseline   # record today's state"
Write-Host "  python -m gatecheck run --demo fixed"
