import glob, json, os, sys, tempfile
sys.path.insert(0, os.path.join(sys.argv[1], "bench"))
import store as S

work = tempfile.mkdtemp(prefix="m1f-torn-")
journal = os.path.join(work, "store.jsonl")
real_open = S.open if hasattr(S, "open") else open
out = {}

s = S.Store(S.Journal(journal))
s.handle({"cmd": "issue", "action_id": "T-1"})
s.handle({"cmd": "verdict", "record": {"action_id": "T-1", "verdict": "BLOCK", "signature": None}})

with open(journal, "ab") as fh:
    fh.write(b'{"kind": "verdict", "action_id": "T-1", "sto')
out["bytes_before_recovery"] = len(open(journal, "rb").read())

s2 = S.Store(S.Journal(journal))
out["bytes_after_recovery"] = len(open(journal, "rb").read())
out["discarded"] = s南京 = None
out["discarded"] = s2.journal.discarded
q = s2.journal.quarantine
out["quarantine"] = q and {k: q[k] for k in ("file", "bytes", "sha256")}
out["gap"] = s2.journal.gap
out["quarantine_files"] = sorted(os.path.basename(p) for p in glob.glob(os.path.join(work, "*.bin")))


def failing_open(path, mode="r", *a, **k):
    if str(path) == journal and mode.startswith("a"):
        raise OSError(5, "Input/output error")
    return real_open(path, mode, *a, **k)


S.open = failing_open
reply = s2.handle({"cmd": "verdict", "record": {"action_id": "T-1", "verdict": "ALLOW", "signature": None}})
S.open = real_open
out["retry_reply"] = {k: reply.get(k) for k in ("ok", "durable", "disk_state", "error")}
out["bytes_after_retry"] = len(open(journal, "rb").read())
print(json.dumps(out, indent=1, default=str))
