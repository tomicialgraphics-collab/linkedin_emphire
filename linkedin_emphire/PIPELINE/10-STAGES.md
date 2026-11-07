# 10 STAGES

Seven stages, each with an entry condition, an exit condition, and the folder it writes into. The
pipeline is only real if a file cannot skip a stage. The gate is what makes skipping visible.

| Stage | Name | Enter when | Exit only when | Writes into |
|---|---|---|---|---|
| S0 | boot | a session starts | `pipeline.py start` has been run and the read order followed | nothing |
| S1 | intake | a thread, brief, job, client or deadline arrives | the person, the ask and the deadline are written down | `OPPURTUNITIES/`, `ENGAGEMENT/`, `CLIENTS/` |
| S2 | read | the ask is written down | the profile is read, the rules are read, the constraint list is read | `STATE/OPEN-LOOPS.md` |
| S3 | draft | the reading is done | the artefact exists in the contract shape | `VERIFIED_POSTS/`, `ENGAGEMENT/`, `CLIENTS/`, `PROJECTS/` |
| S4 | gate | a draft exists | `pipeline.py check` exits 0, and the manual rules are honestly marked done | nothing |
| S5 | verify | the gate passes | every number traces to a run, every hash matches, every claim is provable | nothing |
| S6 | deliver | the owner approves | `pipeline.py log` has written the row | `STATE/DELIVERY-LOG.md` |
| S7 | log | the file is delivered | session log written and index row added | `SESSION_LOG/`, `VERIFIED_POSTS/INDEX.md` |
| S8 | review | Monday, or a milestone closes | money rows summed, open loops pruned | `PIPELINE.md`, `STATE/OPEN-LOOPS.md` |

---

## S0 boot

Run `pipeline.py start`. It prints the read order, the rule counts and the open loops. If a session
begins writing before this, every later stage inherits the assumption that the rules were known.

## S1 intake

Three questions, answered in writing, before anything else:

1. Who is this for, by name, and what did they actually say or ask?
2. What is the deadline, in WAT, with a date?
3. What does done look like, in one sentence the owner could disagree with?

If the answer to 1 is a company and not a person, the profile read is not done.

## S2 read

The rule the owner has now stated three times: read well before writing. It's the first line of
S2 because it's the one that keeps getting skipped.

- `pipeline.py start` output, end to end.
- The person's profile. Their last three posts, their role, the sentence only they would write.
- The constraints in `context.md` section 7, and the corrections in the current session log.
- The last file delivered to that person, so the new one does not repeat it.

## S3 draft

You draft to the contract, not to taste. A post names its template. A comment names the person and quotes
one thing they said. A review carries the script that produced every number in it.

## S4 gate

```bash
python3 TOOLING/pipeline.py check <path>
```

Blocking failures are fixed, not explained. Warnings are either fixed or justified in the delivery
log row. A manual rule that was not done means the file is not done.

## S5 verify

- Every figure traces to a file, a command, or a run recorded in the delivery log.
- Every hash is written next to the file it belongs to, and re-checked after an upload.
- Claims about other people's code say what was read and what was run, separately.
- A patch is "under test" until the post-fix run exists. Then it is "passes the suite", never "fixed".

## S6 deliver

The owner sends. The agent hashes, logs, and hands over the exact text. If the artefact goes to Drive,
the local file and the Drive copy are both hashed and the two digests are compared before the message
goes out.

## S7 log

`SESSION_LOG/SESSION_LOG_<date>.md` records each instruction, each decision, each artefact with its
path, and the open loops. A post adds its index row. Nothing is closed in the chat alone.

## S8 review

Weekly, or when a milestone closes: sum the money rows in `PIPELINE.md`, prune `OPEN-LOOPS.md`, and
run `pipeline.py audit` to see which files would fail today's gate.
