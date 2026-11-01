I published a benchmark that still has eight open defects in it. That is the part worth reading.

It tests what a system does when the host underneath it fails. The write that landed but was never acknowledged. The clock that moved backwards mid-transaction. The lease that expired while the process still believed it held the lock. Nineteen ways for the layer below you to lie, and nineteen checks that tell you whether your code noticed.

Where it stands this week, in public:

→ One suite at thirteen of thirteen, another at three of three.
→ A documentation conformance check at twenty-two of thirty-six. It fails because the docs promise behaviour the code does not implement, which is a finding about the product, not the test.
→ Twelve of thirteen negative cases. The thirteenth is a real gap and it is on the list.
→ Eight defects open, each with an id and a failing test that reproduces it.

None of that reads like a selling point, and it is the most honest thing in the repository.

A benchmark that reports a clean number and no register is telling you about the confidence of its author, not the coverage of its instrument. The register is where the instrument stops. Anyone running these checks against their own system needs to know which failures are mine and which are theirs, and the only way to know is to write mine down first.

The rule I work to: every number ships with the command that reproduces it. If I cannot give you the command, I do not give you the number.

This is not a standard. Standards get agreed. This is a test I wrote and published so that other people can disagree with it in writing, with the code in front of them.

A benchmark that cannot fail in public is not measuring anything.

#SoftwareEngineering #DistributedSystems #Testing

The repository and the findings register are in the first comment.
