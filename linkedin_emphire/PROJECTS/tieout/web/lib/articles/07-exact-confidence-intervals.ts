const body = `
## The number you report is the number you can defend

An eval run of fourteen items that passes thirteen produces a point estimate of 0.9286. Most reports stop there, or append a Wilson interval, and call it rigor. At n=14, the normal approximation those intervals rely on is not just rough, it is the wrong tool. The exact answer for a binomial proportion is the Clopper-Pearson interval, and this harness computes it in the code, with no statistics dependency, before the bundle closes.

For 13 of 14, the exact 95 percent interval is [0.661316, 0.998193].

Read the lower bound. Thirteen of fourteen is not "93 percent, give or take a little". It is consistent with a true pass rate as low as 66 percent. That is not pessimism. That is what the data supports.

## How it is computed

The lower endpoint solves P(X >= 13 | p = L, n = 14) = alpha/2, and the upper endpoint solves P(X <= 13 | p = U, n = 14) = alpha/2, with alpha = 0.05. The implementation is bisection on the binomial CDF, built from math.comb, which is exact integer arithmetic. No scipy, no sampling, no approximation. The test suite pins the result with reference vectors: 0 of 10 gives [0, 0.3085], and 13 of 14 gives [0.6613, 0.9982] to four places.

Because the interval is computed before the bundle is sealed, it lives in the manifest. The site reads it from there, the diff endpoint reads it from there, and a stranger recomputing from the raw events gets the same numbers from the same integer arithmetic. The interval is not commentary on the result. It is part of the record.

## What it changes about small evals

Small evals are where agent evaluation actually happens: suites are expensive, and a family with eight items is common, not pathological. The F2 family's 4 of 8 carries the interval [0.157, 0.843] in its manifest, and the site displays the width next to the number. An interval that wide is a statement: this family is a direction, not a measurement.

The discipline this enforces is simple. Report the count, the point estimate, and the exact interval, in that order. If your interval is too wide to act on, the honest next step is more items, not more decimal places.
`;

export { body };
