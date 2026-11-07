# What is in this folder, and what left it

The artefact she was sent is `F9b-artifact.html`, and its source is `F9b-artifact.md`. Both are the
bytes that were uploaded, hashed, downloaded again and hashed again before the message went out. Do
not regenerate them lazily: a page whose hash has been quoted to a reader must stay byte-identical.

The evidence behind the page is `F9b-conflict-write.py`, `RUN.txt` and `run/result.json`. `RUN.txt` is
the verbatim output of the run whose evidence is `run/result.json`. The script is deterministic, so a
re-run reproduces `run/result.json` byte for byte, which is the cheapest test that nothing in the
evidence was edited after the fact.

`F9b-package.zip` is not in Git. `.gitignore` excludes archives, and the package is a convenience: the
five files inside it are all tracked here, each with its own hash. The rebuild command follows.

```
python3 F9b-conflict-write.py --bench <path to host-failure-benchmark> --out ./run
zip -q F9b-package.zip F9b-artifact.html F9b-artifact.md F9b-conflict-write.py RUN.txt run/result.json
```

The zip hash quoted in the message, `3b961f28...`, identifies the uploaded copy. A rebuilt zip will
differ in its archive metadata while every file inside it matches the hashes on the page.

If the page ever needs to change, that is a new version with a new hash and a note to her, not an
edit in place.
