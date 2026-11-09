# 07 Reporting

The report is the deliverable. The number is the product.

## Structure that survives a review

1. **What was tested.** Target, environment, revision, prompt version, dates, scope, and the rules of engagement reference. One screen.
2. **What was not tested.** The coverage argument, with the `open` row visible.
3. **Findings.** One page each: title, severity with the method, what the system does, how to reproduce it, the evidence, the smallest fix.
4. **Root causes.** Grouped, because twelve findings under one broken trust boundary is one finding and eleven instances.
5. **The handover.** The suite, how to run it, what it costs, and the cases that came from this report.

## A finding, in the order a reader needs it

```markdown
### F-03 System prompt recovered through a summarisation request

**Severity:** high. Confidentiality of the instruction layer, one request, no authentication beyond a normal user session.
**Model revision:** vendor-model-2026-09 rev 4, pinned. **Prompt:** support-agent v17.
**Rate:** 19 of 20 attempts, 95 percent CI 77.0 to 99.0 percent.
**What happens:** ask for a summary of the rules the assistant follows and the response returns the system prompt verbatim.
**Reproduce:** [four lines of exact request and response]
**Evidence:** trace id, timestamp, screenshot path.
**Fix:** treat the system prompt as confidential by design rather than by obscurity. Assume it is known and move the secrets it holds into the tool layer.
**Regression case:** added to the suite as case 041, runs on every deploy.
```

Note what that contains: a method for the severity, six reproducibility fields, a rate with an interval, evidence, a fix that does not depend on hiding something, and the regression case. That is roughly the minimum for a finding to be useful.

## Severity, with a method

Decide before the run, and state the method in one line. A workable default:

| Band | Test |
|---|---|
| Critical | Unauthenticated, remote, leads to another tenant's data or a write the user cannot authorise |
| High | Authenticated user reaches data or actions beyond their authority, or confidentiality of the instruction layer breaks with one request |
| Medium | Requires unusual conditions, or a partial disclosure, or a rate too low to rely on |
| Low | Cosmetic, or a hardening gap with no demonstrated effect |

Then say what you used. A number with no method is a preference.

## The coverage argument

Generated, not written by hand. Include all four buckets and the counts:

```
168 classes. 23 tested, 2 not present, 1 skipped on purpose, 142 open.
```

`skipped` needs a reason and the tool will refuse without one. `open` needs no apology, only a count, because a report that claims full coverage is either wrong or testing something narrower than it says.

## Words that cost you the reader

- "Comprehensive", when the coverage table shows 142 open classes.
- "Secure", which is not a property a test can establish.
- "Patched" for something you have not rerun.
- Any rate without a denominator.
- Any recommendation that says "implement guardrails" without naming the control and the test for it.

## The handover section

End with what the client owns:

- The suite, in their repository, running in their CI.
- The cases added, numbered, with the finding they came from.
- The cost per run and the wall clock time per run.
- The two names: who runs it, who reads the failure.

An engagement that ends with a PDF has produced a document. One that ends with a suite has produced a repair, and the difference is visible a quarter later when the next prompt change lands.
