---
deliverable: comment
id: 2026-11-07_marin-ivezic-quantum-finance-pqc
date: 2026-11-07
audience: public
status: ready
approved: no
warm: no
profile_checked: 2026-11-07 via pqcframework.org, his PostQuantum about page and the published Universal v1.1 framework PDF. Marin Ivezic, CEO of Applied Quantum, previously a Fortune Global 500 CISO and CTO and a Big 4 partner. His eight-phase PQC migration framework is open under CC BY and puts discovery and cryptographic inventory first, with the CBOM profile layered on CycloneDX, so anything the comment says must be beyond "inventory matters", because he wrote the framework that says it. PostQuantum.com has a stated million monthly readers. Audience is security and finance leadership.
thread: his post arguing that quantum will not reach Wall Street for years, measured against Goldman Sachs resource estimates, and that the attention belongs on the cryptographic migration banks have to finish
---

# Comment on Marin Ivezic's quantum-finance post, 7 November 2026

## What the post argues

Derivative pricing by amplitude estimation needs roughly 4,700 logical qubits and 10^9 T gates at around 45 MHz
throughput to match classical Monte Carlo, against feasibility estimates near 10 kHz for logical clock rates, a gap
of about three orders of magnitude. A quadratic speedup also has to beat a bank running pricing across ten thousand
H100s, which parallelise in a way a single coherent circuit cannot. His closing point is that the marketing gap
diverts research budget and attention away from the cryptographic migration banks actually have to finish.

That closing point is the opening for a comment, because he has already written the framework that says migration
starts with inventory. Telling him inventory matters would be returning his own work to him. The useful addition is
the narrower question of how a bank knows the inventory is complete.

## Draft, paste as a comment

The last paragraph is where the real damage is, and your framework already puts discovery first for the same reason.

What is worth adding is how a bank knows the inventory is complete. A crypto register is an existence test: the
entries in it are correctly described. It says nothing about the service that went live outside the process last
quarter. A completeness test starts from a population the bank already counts for another reason, the change
calendar, the certificate estate, the vendor list, and asks which items have no entry. Different sampling frames,
different failures.

There is a trap in phase one worth naming. An inventory gets cleaner as coverage falls, because whatever routes
around the process stops appearing in it.

The reconciliation is what tells you discovery is finished. Nothing else does.

## Why this shape

- Credits the framework by not restating it. He wrote eight phases with discovery first; the comment starts where
  his phase one stops asking questions.
- The existence versus completeness distinction is the audit profession's own vocabulary, so a finance audience
  reads it as competent rather than academic.
- The trap sentence is the one worth quoting: an inventory improving while coverage falls is the failure nobody
  reports, because every metric inside the register looks better.
- Last line is a claim about completion criteria, which is the thing every migration programme argues about and
  almost none writes down.
- No link, no numbers of mine, and no reference to any of my own work.

## Posting notes

- Post while it is fresh. He writes for practitioners and replies to substantive comments, and his readers are the
  security leadership who commission this work.
- If he answers that the CBOM profile already handles completeness, the reply is that a CBOM describes what was
  discovered, so the frame is still the register, and the reconciliation has to start outside it.
- Nothing about clients or the review work here.
