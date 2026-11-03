# Getting the restructure into Teamthy/host-failure-benchmark

One download, three commands. The zip already contains the finished layout, including all 42 delivered
files, so nothing has to be moved by hand.

## 1. Download

```
https://github.com/tomicialgraphics-collab/linkedin_emphire/raw/arena/70379866-linkedin-emphire/linkedin_emphire/OUTREACH/2026-11-03_behar_send/hfb-p2-review-structure.zip
```

92 KB, 52 files plus 6 directories, sha256 `175724f48b396e83d6a58a2e...`.

## 2. Apply, PowerShell 5.1, one command per line

```
cd C:\path\to\host-failure-benchmark
git pull
Invoke-WebRequest "https://github.com/tomicialgraphics-collab/linkedin_emphire/raw/arena/70379866-linkedin-emphire/linkedin_emphire/OUTREACH/2026-11-03_behar_send/hfb-p2-review-structure.zip" -OutFile hfb-p2-review-structure.zip
Expand-Archive hfb-p2-review-structure.zip -DestinationPath . -Force
Remove-Item hfb-p2-review-structure.zip
git rm -q "*.out" "*.log"
git rm -q p2probes.py v2lib.py v2tests.py v3fixes.py build_matrix.py extra_checks.py runner_checks.sh runner_extra.sh p2probes.json p2-results-matrix.json p2-results-matrix.csv v2results.json
Add-Content .gitignore "review/2026-11-03_p2-verification/scripts/p2probes.json"
git add -A
git commit -m "review: restructure the P2 verification kit and add the S1-S5 reproduction results"
git push
```

## 3. Check it landed

```
git ls-tree -r --name-only HEAD review | Measure-Object -Line
```

Expect 52. Then open `review/2026-11-03_p2-verification/README.md` on GitHub and confirm it renders, and
`results-2026-11-03/RESULTS.md` beside it.

## Why a copy rather than a move

`git rm` plus `git add` looks like a delete and an add, but git detects the renames on commit, so history
follows each file. The bytes are identical: `MANIFEST.sha256` inside the folder was generated from the
delivered copies and verifies 42 of 42 from inside that directory.

## The one thing not to do

Do not clone the `linkedin_emphire` repository into this one. It is a different project and it carries
client work, outreach notes and a LinkedIn archive. The zip above contains only the review folder and
nothing else.
