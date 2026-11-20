# emphire.ps1 - the pipeline, for Windows PowerShell 5.1.
#
# One command per line. No && in PowerShell 5.1, so do not chain these.
#
#   .\emphire.ps1 start
#   .\emphire.ps1 check linkedin_emphire\VERIFIED_POSTS\2026-11-06_absence-of-a-record\post.md
#   .\emphire.ps1 log linkedin_emphire\CLIENTS\foray-dunin7\2026-11-06\FINDINGS-02-register-entries-v3.md -To "Marvin" -How "Drive link, hash in message"
#   .\emphire.ps1 board
#   .\emphire.ps1 status
#   .\emphire.ps1 audit
#
# Everything forwards to linkedin_emphire/TOOLING/pipeline.py.

param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$Command,

    [Parameter(Position = 1, ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)

$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$tool = Join-Path $here 'linkedin_emphire\TOOLING\pipeline.py'

if (-not (Test-Path $tool)) {
    Write-Host "pipeline.py not found at $tool" -ForegroundColor Red
    Write-Host "Run this script from the repository root, and check the repo is up to date." -ForegroundColor Yellow
    exit 2
}

$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    $python = Get-Command python3 -ErrorAction SilentlyContinue
}
if (-not $python) {
    Write-Host "Python is not on PATH. Install Python 3.9 or newer, then reopen PowerShell." -ForegroundColor Red
    exit 2
}

$arguments = @($tool, $Command) + $Rest
& $python.Source @arguments
exit $LASTEXITCODE
