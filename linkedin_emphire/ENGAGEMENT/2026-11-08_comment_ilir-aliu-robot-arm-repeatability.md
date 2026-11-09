---
deliverable: comment
id: 2026-11-08_ilir-aliu-robot-arm-repeatability
date: 2026-11-08
audience: public
status: ready
approved: no
warm: no
profile_checked: 2026-11-08 from his headline and site. Ilir Aliu, curator and writer covering AI and robotics stories for 22Astronauts. He does not appear to post his own engineering work, so he is a distributor rather than a practitioner, which limits what a comment can start.
thread: his post on a low-cost six axis robot arm built by James Gullberg, covering modular joints, custom gearboxes, a spherical wrist, firmware and motor control, ROS 2 motion planning, and the gap between simulation and real hardware where friction, backlash and motor limits appear
verified: the build details and the credit are his and are not restated as mine. Nothing in the comment depends on a claim about the project or the robot, only on general behaviour of geared joints, which is stated as a measurement to make rather than a result that exists.
---

# Comment on Ilir Aliu's robot arm post, 8 November 2026

## The judgement

Off-lane. He curates AI and robotics stories rather than building, and his audience is enthusiasts rather than the people
who hire for evaluation work. There is no conversation to start here, only mild reach.

The comment is still worth writing because the one genuinely useful thing to add is small and true: the simulator gap he
names is measurable, and almost nobody publishes the measurements. If the owner posts it, fine. If not, nothing is lost.

## Comment

The sim-to-real line is where these builds earn their keep. Backlash alone costs repeatability that no amount of tuning
recovers, and it stays invisible until you command the same move a hundred times and measure where the tool actually ends
up.

Which is the part worth seeing more of. Not the demo, the first hundred cycles: position error after returning to the same
point, how far the wrist drifts under load, which joint had the most slack out of the box. Cheap to measure with a dial
indicator, and it turns an impressive build into a reference someone else can work from.

## What not to say

No claim about this specific arm's accuracy, since I have not measured it and he has not published it. No correction of
the post, which is a careful and accurate description of an interesting project. No pivot to AI evaluation or agents,
which would be an advert under a robotics post.

## Held for nothing

There is no reply worth engineering here. If he answers, a thank you is enough.
