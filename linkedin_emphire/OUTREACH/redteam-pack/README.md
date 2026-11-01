# Red-team evidence pack

Four files in one folder. Nothing here depends on any other project.

`run_it.py` is the one you run. `build_package.py` runs the five tests and fills the document.
`package.md` is the evidence document, and it gets filled in place. `replies.md` holds the two
versions of the message to send with it.

## Requirements

- Python 3.9 or newer.
- An OpenAI-compatible endpoint: Ollama, LM Studio, or a hosted key.
- Internet, once, to clone the five-test suite.

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

## If the endpoint refuses you

Before a run, ask the script one question:

```
python run_it.py --check --base-url https://api.groq.com/openai/v1
```

It asks for the key, hides what you type, makes two calls and prints both answers. It also reports the key length, because a 56 character Groq key arriving as 112 means the paste landed twice. Nothing is written and the package is untouched.

If one model refuses, it tries the next one down the list, so a speech model or a model with unaccepted terms cannot stop the check. There are four answers worth knowing. HTTP 200 on both means the key works and the run will go. HTTP 401 means the key string is wrong, so copy it again from the console. HTTP 403 means the key is real and the request is still refused, which is an entitlement or a network block, not a typo. No connection at all means the base URL is wrong or the server is not running.

## From PowerShell, step by step

Make the folder and go into it:

```powershell
mkdir "$HOME\Desktop\redteam-pack"
cd "$HOME\Desktop\redteam-pack"
```

Save the five files into it, then confirm all five are there:

```powershell
Get-ChildItem
```

Check which Python you have. One of these will answer:

```powershell
python --version
py --version
```

If `python` opens the Microsoft Store instead of printing a version, use `py` everywhere below.

Start the model server in a **second** PowerShell window, because this command holds the window
until you stop it:

```powershell
ollama serve
```

Back in the first window, check that the endpoint answers. Use `curl.exe`, not `curl`, because
PowerShell aliases `curl` to a different command:

```powershell
curl.exe http://localhost:11434/v1/models
```

If no model is listed:

```powershell
ollama pull llama3.1:8b
```

Then run it:

```powershell
python run_it.py
```

or, if your Python is the `py` launcher:

```powershell
py run_it.py
```

A Windows Firewall prompt may appear when Ollama starts. Allow private networks. Nothing leaves the
machine, because both the endpoint and the test inputs are local.

If it stops, the log says where:

```powershell
Get-Content .\run_*.log -Tail 40
```

PowerShell execution policy does not apply here. That setting blocks `.ps1` scripts, and these are
`.py` files run by Python.

## After it runs

1. Open `package.md`, section 4.
2. Beside every flagged response, write `confirmed` or `false positive`, in your words, with the
   reason. `replies.md` shows the shape.
3. Send `package.md` with reply A from `replies.md`.

No run today? Send `package.md` as it stands with reply B. Section 4 says plainly that the run is
not attached and why. Never send A over an empty section.

## Sending it

`package.md` is markdown, and a LinkedIn message accepts PDF, DOCX, TXT or HTML but not `.md`. Convert first.

```
python to_pdf.py
Start-Process .\package.html
```

Print to PDF from the browser and attach `package.pdf`. The print stylesheet sets the margins, so the dialog needs no changes.

## What is in `package.md`

- The limits, first, so it cannot be read past its scope.
- The exact inputs, verified against the source.
- What counts as a break, fixed before any run.
- The sample bot under test.
- The run: model, endpoint, per-test flags, rates with sample sizes, every flagged response verbatim.

Every number in it comes from the run. None of it is estimated.

## Known bug in the upstream runner

`python redteam.py` finishes, writes `results.json`, then crashes writing `results.md` with
`KeyError: 'Test 1 - prompt injection'`. The loop reads `results[tname]` where the dict is keyed
`test1`. `build_package.py` tolerates the crash and records it. One-word fix in the runner:

```
    for x in results[key]:
```
