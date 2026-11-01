# Red-team evidence pack

Four files in one folder. Nothing here depends on any other project.

`run_it.py` is the one you run. `build_package.py` runs the harness and fills the document.
`package.md` is the evidence document, and it gets filled in place. `replies.md` holds the two
versions of the message to send with it.

## Requirements

- Python 3.9 or newer
- An OpenAI-compatible endpoint: Ollama, LM Studio, or a hosted key
- Internet, once, to clone the harness

## Run it

```
python run_it.py
```

It finds the endpoint. It lists the models. It installs the one Python package it needs if that is
missing. Then it runs the five tests and writes the results into `package.md`.

Override what it guesses:

```
python run_it.py --base-url http://localhost:1234/v1 --model qwen2.5-7b
python run_it.py --base-url https://api.groq.com/openai/v1 --api-key <key>
python run_it.py --yes
```

Nothing running yet:

```
ollama serve
ollama pull llama3.1:8b
```

Expect around fourteen model calls. That is a few minutes on a local 8B, under a minute hosted. A log
lands beside the scripts, so a failure can be sent rather than described.

## After it runs

1. Open `package.md`, section 4.
2. Beside every flagged response, write `confirmed` or `false positive`, in your words, with the
   reason. `replies.md` shows the shape.
3. Send `package.md` with reply A from `replies.md`.

No run today? Send `package.md` as it stands with reply B. Section 4 says plainly that the run is
not attached and why. Never send A over an empty section.

## What is in `package.md`

- The limits, first, so it cannot be read past its scope
- The exact inputs, verified against the harness source
- What counts as a break, fixed before any run
- The sample bot under test
- The run: model, endpoint, per-test flags, rates with sample sizes, every flagged response verbatim

Every number in it comes from the run. None of it is estimated.

## Known bug in the harness

`python redteam.py` finishes, writes `results.json`, then crashes writing `results.md` with
`KeyError: 'Test 1 - prompt injection'`. The loop reads `results[tname]` where the dict is keyed
`test1`. `build_package.py` tolerates the crash and records it. One-word fix in the harness:

```
    for x in results[key]:
```
