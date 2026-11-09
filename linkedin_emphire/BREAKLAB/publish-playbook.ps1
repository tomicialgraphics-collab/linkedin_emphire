# publish-playbook.ps1
# Publishes the AI Red Team Playbook to https://github.com/Teamthy/Ai-Red-Team-Playbook
#
# Before running: download ai-red-team-playbook-1.0.0.zip from the workspace. It can land
# in Documents or Downloads, so this script searches your home folder for it.
#
# Run with:  powershell -ExecutionPolicy Bypass -File .\publish-playbook.ps1
# Windows PowerShell 5.1 compatible. No chained operators, no ternary, nothing newer than 5.1.

$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "AI Red Team Playbook, publish script" -ForegroundColor Cyan
Write-Host "-----------------------------------"

# 1. Find the zip anywhere under the home folder.
$zip = Get-ChildItem -Path $HOME -Recurse -Filter "ai-red-team-playbook-*.zip" -ErrorAction SilentlyContinue |
       Sort-Object LastWriteTime -Descending |
       Select-Object -First 1

if ($null -eq $zip) {
    Write-Host "Could not find ai-red-team-playbook-*.zip anywhere under $HOME." -ForegroundColor Red
    Write-Host "Download it from the workspace first, then run this again."
    exit 1
}

Write-Host "Using zip: $($zip.FullName)"

# 2. Unpack it somewhere clean.
$work = Join-Path $HOME "playbook-build"
if (Test-Path $work) { Remove-Item $work -Recurse -Force }
Expand-Archive -Path $zip.FullName -DestinationPath $work -Force
Write-Host "Unpacked to: $work"

# 3. Clone the empty repository. A warning about an empty repository here is expected.
$repo = Join-Path $HOME "Ai-Red-Team-Playbook"
if (Test-Path $repo) { Remove-Item $repo -Recurse -Force }
git clone https://github.com/Teamthy/Ai-Red-Team-Playbook.git $repo

# 4. Copy the playbook in, set the author, commit, push.
Copy-Item -Path "$work\ai-red-team-playbook\*" -Destination $repo -Recurse -Force
Set-Location $repo

git config user.name "Olusanya Timothy"
git config user.email "olusanyatimothy54@gmail.com"

git add -A
git commit -m "AI Red Team Playbook 1.0.0: 168 testable classes for AI red teaming"
git push -u origin main

# 5. Check what landed.
Write-Host ""
Write-Host "Done. What is now in the repository:" -ForegroundColor Green
git log --oneline -1
$count = (Get-ChildItem -Recurse -File | Where-Object { $_.FullName -notmatch "\\\.git\\" }).Count
Write-Host "Files committed: $count  (expected 28)"
Write-Host ""
Write-Host "Next, on the repository page:"
Write-Host "  Settings, Social preview, upload an image. This is what the LinkedIn card shows."
Write-Host "  The gear beside About, add topics:"
Write-Host "    ai-security, llm-security, red-teaming, ai-evaluation, prompt-injection, agentic-ai, checklist"
Write-Host "  Set the description:"
Write-Host "    168 testable classes for AI red teaming, with a coverage argument and honest intervals"
