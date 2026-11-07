# Restructure of the P2 verification upload

The 42 files Behar supplied arrived flat at the repository root at `ec6e46f`, next to `verify.py`, `run.py`
and `bench/`. That puts an independent reviewer's fixtures inside the maintainer's tree at the top level,
and it overwrites a recorded artifact the moment anyone re-runs a probe.

The target layout is built and tested here. Owner runs the commands, because the GitHub token in this
sandbox has read-only access to `Teamthy/host-failure-benchmark`.

## Target layout

```
review/2026-11-03_p2-verification/
  README.md                  what this is, the digest gap, how to run it
  MANIFEST.sha256            hashes of all 42 delivered files
  scripts/                   p2probes.py, runner_checks.sh, runner_extra.sh, extra_checks.py,
                             v2lib.py, v2tests.py, v3fixes.py, build_matrix.py
  recorded/                  the review's own outputs, byte for byte, including
                             p2probes.delivered.json
  results-2026-11-03/        RESULTS.md and the six logs from tonight's run
```

## What was verified here

- All 42 files moved with `git mv`, so history follows them.
- `p2probes.py` still finds its library and still writes `p2probes.json` next to itself, now inside
  `scripts/`, which is gitignored so a re-run cannot overwrite the delivered capture.
- S1 and S2 re-ran from `scripts/` and produced the same observations as before the move.
- `MANIFEST.sha256` has 42 rows and was generated from the delivered bytes, which a move does not change.

## The sequence, PowerShell 5.1

```
cd C:\path\to\host-failure-benchmark
git pull
$R = "review/2026-11-03_p2-verification"
New-Item -ItemType Directory -Force "$R\scripts", "$R\recorded", "$R\results-2026-11-03\logs" | Out-Null
git mv p2probes.py "$R/scripts/"
git mv v2lib.py "$R/scripts/"
git mv v2tests.py "$R/scripts/"
git mv v3fixes.py "$R/scripts/"
git mv build_matrix.py "$R/scripts/"
git mv extra_checks.py "$R/scripts/"
git mv runner_checks.sh "$R/scripts/"
git mv runner_extra.sh "$R/scripts/"
git mv p2probes.json "$R/recorded/p2probes.delivered.json"
git mv p2-results-matrix.json "$R/recorded/"
git mv p2-results-matrix.csv "$R/recorded/"
git mv v2results.json "$R/recorded/"
Get-ChildItem -Filter *.out | ForEach-Object { git mv $_.Name "$R/recorded/" }
Get-ChildItem -Filter *.log | ForEach-Object { git mv $_.Name "$R/recorded/" }
```

Then the four new files, fetched from the copy kept in this repository:

```
$B = "https://raw.githubusercontent.com/tomicialgraphics-collab/linkedin_emphire/arena/70379866-linkedin-emphire/linkedin_emphire/PROJECTS/2026-10-30_behar-host-failure-benchmark/p2-verification-2026-11-03"
Invoke-WebRequest "$B/README.md" -OutFile "$R/README.md"
Invoke-WebRequest "$B/MANIFEST.sha256" -OutFile "$R/MANIFEST.sha256"
Invoke-WebRequest "$B/MANIFEST-delivered.sha256" -OutFile "$R/MANIFEST-delivered.sha256"
Invoke-WebRequest "$B/RESULTS.md" -OutFile "$R/results-2026-11-03/RESULTS.md"
foreach ($f in "s1-p08","s2-p07","s3-runner_checks","s3-runner_extra","s4-n11-run","s5-f20") { Invoke-WebRequest "$B/logs/$f.log" -OutFile "$R/results-2026-11-03/logs/$f.log" }
Add-Content .gitignore "review/2026-11-03_p2-verification/scripts/p2probes.json"
git add -A
git commit -m "review: restructure the P2 verification kit and add the S1-S5 reproduction results"
git push
```

## Check the manifest before committing

```
Get-Content "$R/MANIFEST.sha256" | ForEach-Object { $h,$p = $_ -split '\s+',2; $c = (Get-FileHash "$R/$p" -Algorithm SHA256).Hash.ToLower(); if ($c -ne $h) { "MISMATCH $p" } }
```

No output means all 42 hashes match. Anything printed is a file that did not survive the move intact.

## Why this matters beyond tidiness

A reviewer's fixtures sitting at the maintainer's root is the kind of contamination that makes a later
reproduction ambiguous, because "the checkout" now contains the audit kit as well as the subject. Under
`review/`, the source tree at `006d7ee` stays exactly what it claims to be, and the kit is a thing you
point at rather than a thing that is inside.

The `p2probes.json` rename matters more than it looks. `p2probes.py` writes its JSON next to itself. Left as
delivered, the first re-run silently replaces the review's recorded capture with the operator's new one,
and the two are then indistinguishable in the history. That is the failure this account spends its time
reviewing, and it is worth not committing it in the tidy-up.
