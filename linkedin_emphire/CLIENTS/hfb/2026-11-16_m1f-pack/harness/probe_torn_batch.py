import glob, hashlib, json, os, sys, tempfile
sys.path.insert(0, os.path.join(sys.argv[1], "bench"))
import store as S

work = tempfile.mkdtemp(prefix="m1e-case-")
journal = os.path.join(work, "store.jsonl")
real_open = S.open if hasattr(S, "open") else open
out = {}


class ShortWrite:
    """A file that stops one byte before the end of the write, then fails.

    The batch reaches the disk whole apart from its final terminator, which is the crash the
    reviewer injected: everything arrived, the file never said so.
    """

    def __init__(self, fh):
        self.fh = fh

    def write(self, data):
        self.fh.write(data[:-1] if data.endswith("\n") else data[: max(1, len(data) // 2)])
        raise OSError("injected: the write stopped one byte short")

    def __enter__(self):
        return self

    def __exit__(self, *a):
        self.fh.close()
        return False


def short_open(path, mode="r", *a, **k):
    fh = real_open(path, mode, *a, **k)
    if mode.startswith("a") and str(path) == journal:
        return ShortWrite(fh)
    return fh


s = S.Store(S.Journal(journal))
s.handle({"cmd": "issue", "action_id": "H-1"})
a = {"action_id": "H-1", "verdict": "BLOCK", "signature": None}
b = {"action_id": "H-1", "verdict": "ALLOW", "signature": None}
s.handle({"cmd": "verdict", "record": a})

before_bytes = open(journal, "rb").read()
s.journal.failpoint = "rollback"
S.open = short_open
crash = s.handle({"cmd": "verdict", "record": b})
S.open = real_open
s.journal.failpoint = ""
out["crash_reply"] = {k: crash.get(k) for k in ("ok", "durable", "disk_state", "reason")}

torn = open(journal, "rb").read()
out["torn_tail_bytes"] = len(torn) - len(before_bytes)
out["torn_tail_sha"] = hashlib.sha256(torn[len(before_bytes):]).hexdigest()

retry = s.handle({"cmd": "verdict", "record": b})
out["retry_reply"] = {k: retry.get(k) for k in ("ok", "durable", "disk_state", "error")}

after = open(journal, "rb").read()
out["journal_after_retry_bytes"] = len(after)
out["journal_intact"] = after == torn
out["tail_still_present"] = after.endswith(torn[len(before_bytes):])
out["quarantine_files"] = sorted(os.path.basename(p) for p in glob.glob(os.path.join(work, "*.bin")))
out["quarantine"] = (s.journal.quarantine or {}).get("file")

s2 = S.Store(S.Journal(journal))
out["gap_after_restart"] = s2.journal.gap and {
    k: s2.journal.gap[k] for k in ("store_seq", "kind", "bytes")}
accepted = s2.handle({"cmd": "issue", "action_id": "H-9"})
out["write_after_restart"] = {k: accepted.get(k) for k in ("ok", "durable", "error")}
print(json.dumps(out, indent=1, default=str))
