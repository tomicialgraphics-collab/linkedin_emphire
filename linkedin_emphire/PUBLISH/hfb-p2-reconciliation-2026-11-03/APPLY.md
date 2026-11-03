# Apply this to Teamthy/host-failure-benchmark, then push one commit

Prepared 3 November 2026, in answer to Behar Dalipi's consolidated P2 review. Everything here already
exists in a working tree; none of it is published. The review found that gap and it is correct.

## Where each file goes

| File in this bundle | Destination in the repository |
| --- | --- |
| `README.md` | `README.md` |
| `TECHNICAL-NOTE.md` | `TECHNICAL-NOTE.md` |
| `audit/FINDINGS-REGISTER.md` | `audit/FINDINGS-REGISTER.md` |
| `audit/DISPOSITION-2026-11-01.md` | `audit/DISPOSITION-2026-11-01.md` |
| `audit/evidence/2026-11-01/*.log` | `audit/evidence/2026-11-01/`, new folder |
| `SHA256SUMS.txt` | `SHA256SUMS-2026-11-03.txt` at the repository root |

## What changes, in the reviewer's own categories

**DOC-1, documentation counts.** `README.md` on main says Class V is two checks. It is three, because
`D'.effect` took Class V from 2 of 2 to 3 of 3. The bundled copy says three, and `TECHNICAL-NOTE.md`
matches.

**Attribution.** The register on main does not name the reviewer at all. The bundled register carries the
attribution section: reviewer and author roles separated, the sentence that no row is an endorsement, and
the note that the section was added on 1 November at the reviewer's request. The disposition names him
once in passing and separates nothing; the bundled copy is the same file with the register's attribution
referenced rather than repeated.

**DOC-4, evidence paths.** The register cites `evidence/2026-11-01/` and at least one log by name, and
neither resolved anywhere public. The bundled evidence folder contains eight logs and a hash manifest, so
every cited path resolves at this revision.

## Commands, PowerShell 5.1, one per line

```
cd C:\path\to\host-failure-benchmark
```

```
git pull
```

Copy the files in, keeping the folder shape. If the bundle is unzipped at `C:\review\hfb-p2`:

```
Copy-Item C:\review\hfb-p2\README.md . -Force
```

```
Copy-Item C:\review\hfb-p2\TECHNICAL-NOTE.md . -Force
```

```
Copy-Item C:\review\hfb-p2\audit\FINDINGS-REGISTER.md audit\ -Force
```

```
Copy-Item C:\review\hfb-p2\audit\DISPOSITION-2026-11-01.md audit\ -Force
```

```
mkdir audit\evidence\2026-11-01
```

```
Copy-Item C:\review\hfb-p2\audit\evidence\2026-11-01\* audit\evidence\2026-11-01\ -Force
```

Then check before committing:

```
Select-String -Path README.md -Pattern "Three checks"
```

```
Select-String -Path audit\FINDINGS-REGISTER.md -Pattern "## Attribution"
```

```
Get-ChildItem audit\evidence\2026-11-01
```

Expect eight logs, a match on "Three checks", and a match on "## Attribution".

```
git add -A
```

```
git commit -m "Reconcile the published record with the P2 review: counts, attribution, evidence"
```

```
git push
```

Then record the new commit sha. That sha is what goes in the reply, not a link.

## Do not

- Do not describe the attribution as verified until this commit is pushed and the files are read at that
  sha. The review's point is precisely that a private confirmation is not a published revision.
- Do not edit the register's finding rows in this commit. This commit reconciles documentation, evidence
  and attribution. Row-level dispositions follow in the next commit, after the supplemental findings are
  reproduced.
