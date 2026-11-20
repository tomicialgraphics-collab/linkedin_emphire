# download-playbook.ps1
# Downloads ai-red-team-playbook-1.0.0.zip into the root of your home folder.
#
# Run from any PowerShell window:
#   powershell -ExecutionPolicy Bypass -File .\download-playbook.ps1
#
# Different folder:
#   powershell -ExecutionPolicy Bypass -File .\download-playbook.ps1 -Destination "C:\Work"
#
# Windows PowerShell 5.1 compatible. No chained operators, nothing newer than 5.1.
# The zip is 64,420 bytes and its SHA256 is checked after download, so a truncated
# or corrupted file fails here rather than halfway through the publish script.

param(
    [string]$Destination = $HOME
)

$ErrorActionPreference = "Stop"

# Two addresses for the same file. The first is pinned to the exact commit, so it cannot
# change under you. The second follows the branch, which is easier to update but can move.
$urls        = @(
    "https://raw.githubusercontent.com/tomicialgraphics-collab/linkedin_emphire/f3a7457ba4ae06f46ce6ac675493d2c3ab2853a1/linkedin_emphire/BREAKLAB/ai-red-team-playbook-1.0.0.zip",
    "https://raw.githubusercontent.com/tomicialgraphics-collab/linkedin_emphire/arena/2d8b05cd-linkedin-emphire/linkedin_emphire/BREAKLAB/ai-red-team-playbook-1.0.0.zip"
)
$fileName    = "ai-red-team-playbook-1.0.0.zip"
$expectedLen = 64420
$expectedSha = "7b4d1554d7c1c4ad66d5ab2c7d76f9e48030a34f88b2d1b1ad069314e79bbb52"

Write-Host ""
Write-Host "Downloading the AI Red Team Playbook" -ForegroundColor Cyan
Write-Host "------------------------------------"

# Older PowerShell defaults to TLS 1.0, which GitHub rejects.
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

if (-not (Test-Path $Destination)) {
    New-Item -ItemType Directory -Path $Destination -Force | Out-Null
}

$target = Join-Path $Destination $fileName
if (Test-Path $target) {
    Remove-Item $target -Force
}

Write-Host "Target: $target"
Write-Host ""

$downloaded = $false
foreach ($url in $urls) {
    Write-Host "Trying: $url"
    try {
        Invoke-WebRequest -Uri $url -OutFile $target -UseBasicParsing -TimeoutSec 120
        $downloaded = $true
        Write-Host "Fetched from that address." -ForegroundColor Green
        break
    }
    catch {
        Write-Host "  no: $($_.Exception.Message)" -ForegroundColor Yellow
    }
}

if (-not $downloaded) {
    Write-Host ""
    Write-Host "Download failed from every address." -ForegroundColor Red
    Write-Host ""
    Write-Host "Three things worth trying:" -ForegroundColor Yellow
    Write-Host "  1. Open the repository, find the file, and copy the raw link from there."
    Write-Host "  2. If curl works and PowerShell does not, run:"
    Write-Host "       curl.exe -L -o `"$target`" `"$($urls[0])`""
    Write-Host "  3. If the repository is private for you, the raw link needs a token, so"
    Write-Host "     download it from the workspace instead and skip this script."
    exit 1
}

# Check it is the file we meant, not an error page saved with a zip extension.
$size = (Get-Item $target).Length
if ($size -ne $expectedLen) {
    Write-Host "Wrong size: $size bytes, expected $expectedLen." -ForegroundColor Red
    Write-Host "The download is incomplete or the URL returned something else. Deleting it."
    Remove-Item $target -Force
    exit 1
}

$hash = (Get-FileHash -Path $target -Algorithm SHA256).Hash.ToLower()
if ($hash -ne $expectedSha) {
    Write-Host "Hash mismatch." -ForegroundColor Red
    Write-Host "  got:      $hash"
    Write-Host "  expected: $expectedSha"
    exit 1
}

Write-Host ""
Write-Host "Done." -ForegroundColor Green
Write-Host "  File:   $target"
Write-Host "  Size:   $size bytes"
Write-Host "  SHA256: $hash"
Write-Host ""
Write-Host "Next, if you are publishing it:" -ForegroundColor Cyan
Write-Host "  powershell -ExecutionPolicy Bypass -File .\publish-playbook.ps1"
Write-Host ""
Write-Host "The publish script searches your home folder for this zip, so it will be found"
Write-Host "wherever this put it."
