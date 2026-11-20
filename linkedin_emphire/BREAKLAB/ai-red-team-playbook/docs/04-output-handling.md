# 04 Output handling

Covers `OH-01` to `OH-15`.

## The output is input

Model text leaves the model and becomes someone else's input: a browser, a database, a shell, a mail client, a file name, a log line, another model. The severity of any output-related finding is set by the sink, not by the text.

Draw the sinks before testing. In most systems there are more than the builders think:

- Markdown rendered in a chat UI, which fetches images automatically.
- HTML rendered anywhere, including in an email digest.
- A database, through generated SQL.
- A shell or a runtime, through generated code.
- A downstream API, through generated JSON.
- A file path, a header, a log field, an audit record.
- Another model, which makes it a chain rather than a sink.

## The exfiltration family

The reason this category outranks most others in real engagements is that it needs no jailbreak. A model that will render a link will render a link with data in it.

- **Markdown images.** The browser fetches the URL to render it, and the query string carries whatever the attacker wants to learn. No click required.
- **Link parameters.** Requires a click, so it is a weaker finding, and still a finding.
- **Length and timing.** The size of a refusal, or how long it takes, can leak a little about the content that was refused.
- **Whitespace and formatting.** Low bandwidth, high patience.

Test them where they land, not in the model. A payload that is inert in the API response can be live in the client that renders it.

## Guardrails, judged as classifiers

A guardrail is a classifier, so the whole discipline of adversarial examples applies, plus two problems that are specific to this setting.

**Ordering.** A filter that runs after the tool call is a log line, not a control. Ask where it sits relative to the action, and test with a payload whose effect is irreversible.

**Same context.** If the guardrail is a prompt in the same context as the content it judges, it can be argued with. A model told to ignore instructions and judge the text below will, under enough pressure, judge the text above instead.

Then the ordinary bypasses: encoding, language, length, structured output. And the boring one that catches most teams: the filter inspects prose, the schema field is not prose, and the content arrives anyway.

## Sanitisation is a claim about two strings

Whenever someone says input is sanitised, the question is whether the string that was checked is the string that arrived. Normalisation, encoding, truncation and concatenation all happen somewhere, and the order matters. `OH-12` is the fastest test in the playbook: send a marker, then look at what the model actually received.

## What good looks like

- Output validated against a schema by the consumer, not trusted because the model was asked nicely.
- Rendering that treats model text as untrusted, which usually means no automatic image fetches and no raw HTML.
- A guardrail with a stated position in the flow, before the action it guards.
- A log entry for every tool call with arguments and result, because output handling failures are only diagnosable with the arguments.
