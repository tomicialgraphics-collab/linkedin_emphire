# DM to Evelyne-Claudia Yantony, 6 November 2026

LinkedIn message, reply to her 7:49 AM Thursday message. No attachment offered yet; the one-page
artifact is offered and sent only if she says yes.

---

Evelyne-Claudia,

Straight answer first: evidentiary insufficiency, most of the time. Implementation failure second. Architectural absence third, and when it is real it is unmistakable.

The reason is close to something you said in another form. Authority is asserted at design time and almost never made falsifiable at run time, so the same symptom, a handler with no effect on execution, arrives with three possible causes and nothing in the alert path separates them. The category gets settled by what remains provable afterwards, not by what was observed at the moment.

A bounded example from my own work, offered under your rule that correspondence permits comparison and does not transfer proof. I built a failure benchmark around a decision store and a host that acts on its verdicts. One case: the store writes a decision, and writes a second record when two conflicting decisions exist for one action id. We inject a failure into the second write. The reply to the host then reports that nothing was durable, which in that code is the same claim as nothing having been written, while the first decision is on disk and fsynced.

In your five transitions: Invocation evidenced, Receipt evidenced, Consumption evidenced, Governing effect contradicted by the system's own account, Consequence unrecorded. Implementation failure with an evidentiary consequence, and its worst property is that it makes two worlds identical. A correction that failed and a correction that succeeded without a record look the same to any observer afterwards.

The architectural case is narrower than it sounds. What makes it architectural is not a missing mechanism but authority placed where it cannot reach. In the same benchmark the authority to withhold the effect sits in the host, and the store can only refuse to acknowledge. A store that refuses is not an effect withheld, and the natural implementation puts the refusal in the store, where it has no reach over the action. I had to put the withholding in the host's effect path and test it there. That one does not improve with better logging, which is how you recognise it.

One question, because it is the transition I can least evidence anywhere: in the PaySim pilot, how do you establish that the consequence changed because of the intervention rather than for another reason? A suppressed-intervention rerun on the same seed, a matched pair, or a different construction? Consequence is where I am usually left with correlation and no way to say more.

If a one-page artifact would help, I will send the benchmark case as a file with its reproduction command, its hashes, and its limits stated the way you state yours. I would not import your verdict words into it.
