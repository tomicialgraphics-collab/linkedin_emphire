# Run the evidence package

Step by step, from nothing to a filled package. Windows PowerShell first, because that is the
machine. macOS and Linux commands differ only in `python` versus `python3`.

Everything below was tested end to end on 2026-11-01 against a stub endpoint, so the plumbing is
known good. Your model is the only untested piece.

---

## Fastest path: one command

```
python linkedin_emphire/OUTREACH/run_local.py
```

It finds the endpoint on the usual ports, lists the models, checks the one dependency and installs
it if missing, runs the five tests, and fills the package. It asks before spending the run unless
you add `--yes`.

Override what it guesses:

```
python linkedin_emphire/OUTREACH/run_local.py --base-url http://localhost:1234/v1 --model qwen2.5-7b
python linkedin_emphire/OUTREACH/run_local.py --base-url https://api.groq.com/openai/v1 --api-key <key>
```

Tested end to end on 2026-11-01 against a local endpoint, including the branch where nothing is
running: it lists the ports it tried, tells you how to start a server, and exits without touching
the package. A log lands in `OUTREACH/run_<timestamp>.log` and is git-ignored.

The rest of this file is the same procedure by hand, for when something needs looking at.

## What it takes

- Python 3.9 or newer
- `openai`, one package
- An endpoint: Ollama, LM Studio, or any hosted key
- About 5 minutes on a hosted model, longer on a local one.

---

## 1. Install the dependency

```
python -m pip install openai
```

Use whichever `python` you will run the script with. If you use a virtual environment, activate it
first, because the script and the suite must see the same interpreter.

Check it took:

```
python -c "import openai; print(openai.__version__)"
```

## 2. Start the endpoint

**Ollama**

```
ollama serve
ollama list
```

`ollama list` shows what you have. If it is empty, pull something:

```
ollama pull llama3.1:8b
```

Base URL `http://localhost:11434/v1`. Model id is whatever `ollama list` shows. API key can be the
word `ollama`; local endpoints ignore it.

**LM Studio**

Load a model, open the Developer tab, Start Server. Default port is 1234. Base URL
`http://localhost:1234/v1`, model id is the one shown in the server panel, key `lmstudio`.

**Hosted**

Base URL from the provider's docs, usually ending in `/v1`, plus your real key. Costs a few cents.

## 3. Check the endpoint answers

```
curl http://localhost:11434/v1/models
```

You want a JSON list with your model in it. If this returns nothing, stop here. Nothing downstream
will work and the error will be less clear.

## 4. Run it

From the repo root, one command:

```
python linkedin_emphire/OUTREACH/build_evidence_package.py --model llama3.1:8b --base-url http://localhost:11434/v1 --api-key ollama
```

What happens, in order:

1. Checks `openai` is installed and the endpoint answers. Fails with a readable message if either is
   wrong, before doing any work.
2. Clones the suite at the pinned commit `d95a57e`, or uses your existing clone if you pass
   `--suite`.
3. Runs all five tests. Fourteen model calls at minimum, more if the tool test loops.
4. Writes the run into section 2.3 and section 4 of
   `OUTREACH/2026-11-01_andrey_evidence_package.md`.

Nothing is invented. If the run fails and writes no results, the package is left exactly as it was,
and the script exits with the tail of the error.

## 5. Read section 4 and add your verdicts

Every flagged response is printed verbatim, with the detector's reason. Beside each one, write what
you actually saw:

- `confirmed. Key is in the third line.`
- `false positive. Detector matched "address" while the model was refusing to give one.`

That is the part that cannot be automated, and it is the part he is actually assessing.

## 6. Send it

Reply A from the applications file, since the run is now attached. Attach the markdown or paste it.

---

## If there is no endpoint today

Send reply B with the package as it stands and say plainly that the run follows. Section 4 already
says the run is not attached and why. Do not send reply A over an empty section.

---

## Troubleshooting

| What you see | What it means | What to do |
|---|---|---|
| `No module named openai` | The script's interpreter is not the one you installed into | `python -m pip install openai` using the same `python` |
| `Nothing answered at http://.../v1/models` | Server not running, wrong port, or missing `/v1` | Start the server, check the port, keep `/v1` on the end |
| `model not found` | Model id mismatch | Copy the exact id from `/v1/models` |
| Long silence after `[run]` | Local models are slow | Wait. Fourteen calls on an 8B model takes minutes |
| `KeyError: 'Test 1 - prompt injection'` | Known bug in the suite, see below | The script handles it and carries on |

---

## Known bug in the suite

At the pinned commit, `python redteam.py` finishes the run, writes `results.json`, then crashes while
writing `results.md`. Traceback ends in `KeyError: 'Test 1 - prompt injection'`.

Cause, in `write_outputs()`:

```
for tname, key, hasprompt in [("Test 1 - prompt injection", "test1", "prompt"), ...]:
    for x in results[tname]:        # wrong: the dict is keyed test1, not by display name
```

Fix, one word:

```
    for x in results[key]:
```

Verified on 2026-11-01: with that change the suite exits 0 and writes both files. Build script
already tolerates the crash, so the package does not depend on the fix. Fix it in the suite repo
when you have a minute, then re-pin both the package and the script to the new commit.
