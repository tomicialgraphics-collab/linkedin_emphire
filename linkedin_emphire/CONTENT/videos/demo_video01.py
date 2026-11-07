import hashlib

def h(s):
    return hashlib.sha256(s.encode()).hexdigest()[:12]

def rec(seq, prev, body):
    return {"seq": seq, "prev": prev, "body": body, "hash": h("%d|%s|%s" % (seq, prev, body))}

def check(history):
    seen = set()
    for i, r in enumerate(history):
        if r["seq"] in seen:
            return "INVALID  duplicate slot at %d" % r["seq"]
        seen.add(r["seq"])
        if i and r["prev"] != history[i - 1]["hash"]:
            return "INVALID  broken chain at %d" % r["seq"]
    return "VALID"

r1 = rec(1, "0" * 12, "payment A")
r2 = rec(2, r1["hash"], "payment B")
r3 = rec(3, r2["hash"], "payment C")
r4 = rec(4, r3["hash"], "payment D")
r5 = rec(5, r4["hash"], "payment E")

inserted = rec(3, r2["hash"], "payment C  (backdated)")

clean = [r1, r2, r3, r4, r5]
tampered = [r1, r2, r3, inserted, r4, r5]

print("as written              :", check(clean))
print("with the insert         :", check(tampered))
print("insert removed          :", check([r1, r2, r3, r4, r5]))
print("history emptied         :", check([]))
print()
print("four inputs, and the last two print the same word as the first.")
