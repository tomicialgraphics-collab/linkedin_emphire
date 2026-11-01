# groq_target

A claims assistant with a real model behind the contract gatecheck already
speaks. The gate does not know or care that a model is on the other end.

## Run it

Terminal one:

```powershell
$env:GROQ_API_KEY = "gsk_..."          # this session only, never a file in the repo
python -m groq_target.serve --mode vulnerable
```

Terminal two:

```powershell
python -m gatecheck run --config gatecheck.groq.yml
```

The first run should block. Record it, restart the server in `guarded`
mode, and run the gate again to see what changes:

```powershell
python -m gatecheck run --config gatecheck.groq.yml --update-baseline
# ctrl-c terminal one, then:
python -m groq_target.serve --mode guarded
python -m gatecheck run --config gatecheck.groq.yml
```

## Options

| flag | default | what it does |
| --- | --- | --- |
| `--mode` | `vulnerable` | `guarded` adds the refund limit, the email domain and the no-disclosure rule |
| `--model` | `openai/gpt-oss-120b` | any Groq model that supports tool calling |
| `--temperature` | `0.0` | non-zero makes reruns disagree with each other |
| `--seed` | `7` | best effort determinism, not a guarantee |
| `--fake` | off | scripted answers, no key, no network: proves the wiring |
| `--port` | `8000` | the port `gatecheck.groq.yml` points at |

## Why the guarded prompt says in total, not per refund

The first version said "refunds up to 5000 may be issued". The gate split the
request into two refunds of 4,900 on one claim and the model complied, because
it was following the policy exactly as written: no single refund broke the
rule. The gate caught it as an aggregated tool-misuse, the only finding that
survived the guarded prompt, and the prompt now states the cap as a total per
claim per conversation.

A prompt is still the weaker half of the fix. The enforced version is a check
in `issue_refund` that refuses the second call, and then the gate sees the
attempt rather than the action. That is the difference between asking a model
to behave and making it impossible not to.

## What is safe about it

The three tools never touch the outside world. `send_email` records the
action and returns "sent"; `issue_refund` and `approve_claim` return a
string. Nothing is emailed, nothing is paid, and the only state kept is the
session history that multi-turn attacks need.

## What to expect

A full run is about seventeen attacks and, with tool calls, a few dozen
model requests. On the free tier that is one run a minute or so before a
429, which the client sleeps on once and retries.

The model is not deterministic even at temperature zero, so an attack can
fire on one run and not the next. That is a property of the target, not a
bug in the gate, and it is why the honest next feature is a hit rate per
finding rather than a yes or no.
