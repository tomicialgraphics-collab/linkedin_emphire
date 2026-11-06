# Three alternative posts for 4 November 2026

Pick one. Each is standalone and linted.

---

## Option A, the inventory that is only a memory

Slot: 13:30 WAT. Post body:

Every company that runs agents has an inventory of them. Almost every one of those inventories is a memory rather than a record, and the difference only shows up when someone asks for it.

A memory is accurate on the day it is written. It gets updated when somebody remembers, it is checked annually, and it has no way of telling you about the thing that was never added. A record is checked against something outside itself, so it can be found incomplete.

I have watched two versions of the same failure. An agent registered by one team that another team's list had never heard of. A month of activity that exists in a vendor invoice and nowhere in the company's own count.

The question an auditor asks is not "what do you have". It is "how would you know if something you had stopped appearing on this list".

If the honest answer is "someone would probably notice", the inventory is documentation, not control.

---

## Option B, the eval passed and the answer was still wrong

Slot: 13:30 WAT. Post body:

An eval suite tells you that a system agrees with your expectations. It does not tell you the system is right, and the difference grows as the suite gets better.

Two reasons. The expectations were written by the same team that built the thing, so shared assumptions pass silently. And when the scoring is done by a model, you have one model judging another, which is useful for throughput and worthless as independent evidence.

The failure I look for first is not a failing test. It is a suite that has never changed its mind. A test set that has produced the same pass rate for months is either measuring something stable or has stopped being able to see the change.

Before adding cases, add the one that should fail. If nothing fails, the suite is not measuring what you think.

---

## Option C, on being asked to prove nothing happened

Slot: 13:30 WAT. Post body:

The hardest request in AI assurance is not "show me what it did". It is "show me what it did not do".

Every system logs its successes. Very few log their refusals, their blocks, their timeouts, and the requests they declined to serve. So when someone asks whether the agent touched a system it was not supposed to touch, the logs are silent, and silence is read as no.

That is the wrong inference, and it is the one every incident review makes in the first day. The absence of a record is being used as a record of absence.

Proving a negative requires the negative to be recorded when it happens. A blocked action is an event. A refused request is an event. If nothing writes them down, then the only honest answer to "did it happen" is "I cannot tell", and that answer has to be available before it is true.

Log the attempt, not just the outcome.

---

## Which one

Post A if you want to enter the conversation already running under Daniel Miessler's thread about agent inventories. It is the closest to what your ICP is currently arguing about, and it will get read by the people who care about governance rather than tooling.

Post C if you want the one that sounds most like you and is least like anyone else's post today. It is the sharpest of the three, and it is the one a reviewer reading your profile will remember.

Post B is the safest and the least distinctive. Use it another day.
