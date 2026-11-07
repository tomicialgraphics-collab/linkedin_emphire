The check passed because the file it reads was empty.

A job runs every morning and confirms nothing went out twice. It reads the send log, compares the day's drafts against it, reports zero duplicates. Clean run, every day, for as long as the write has been failing.

The log is empty. An empty log contains no duplicates.

Nothing is wrong with the reader. It's correct. Nothing asserts that its input exists, and every check downstream of missing data returns the answer that looks like success. A check that can pass on empty input isn't a check. It's a formality.

Where I keep meeting it, in AI systems:

They dedupe against a log nobody confirmed grew.

They run the eval suite against a fixture set that loaded zero cases and reported a hundred percent pass.

They confirm every claim was grounded, on an empty retrieval set.

They report no anomalies, because the feed stopped two days ago.

Same shape every time. Your reader is fine, the thing it reads is missing, and the first party to notice is the user.

What works is cheap and boring:

→ Assert the substrate, not only the output. Compare the count before and after the write and fail when it didn't move.

→ Make absence loud. Zero rows, zero cases, zero retrieved spans is an error and never a pass.

→ When you can't prove it either way, say so. An unevaluated check and a passing check must never print the same word.

The part nobody tells you:

Almost every green dashboard I've looked into turns out to be a dashboard about an empty set. Green is the default state of a system with nothing in it.

What does your pipeline print when the input is empty?

#AIEngineering #AISecurity #AIEvaluation
