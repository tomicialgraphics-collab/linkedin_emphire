---
deliverable: comment
id: 2026-11-20_comment_rakesh-gohel-the-gap-in-due-diligence
date: 2026-11-20
audience: outbound
status: ready
approved: no
recipient: Rakesh Gohel, AI Agent Report, public post
premise: >-
  The newsletter closes the Anthropic story by telling enterprises to base vendor decisions on disclosures rather than the
  stock chart, and separately reports AWS isolating every agent session in its own micro virtual machine with a separate
  identity, access policy and audit trail. This comment takes the advice seriously and finishes it: disclosures describe
  the company, while the question a buyer actually has to answer is what an agent did on a given day under whose
  authority, and isolation does not produce that. It ends on the design decision that separates a record from a log.
time_checked: >-
  checked: 2026-11-20 14:46 WAT, read from the system clock before this file was written. The post is stamped 1h before
  the thread was pasted, so this arrives inside the first two hours.
profile_checked: >-
  Rakesh Gohel, whose own headline is agent governance and evidence infrastructure for regulated AI, and who writes a
  weekly report for people running agents in businesses. The comment does not explain his own subject back to him. It
  takes the one place where his advice stops short and continues it, which is the only kind of reply that lands with
  someone who writes for a living.
premise_checked: >-
  checked: both facts used are from the post as pasted, not from memory. The due diligence sentence is his, in the Why It
  Matters under the Anthropic story. The microVM sentence, with identity, access policy and audit trail, is his, under
  the AgentCore story. No figure from the newsletter is repeated: not the price, not the market capitalisation, not the
  context window, not the 14 per cent. The claim about writing the record in the system that enforces the limit is the
  owner's design opinion and is stated as one.
sources_read: >-
  read: none: nothing attached. The post and its comments as pasted.
---

## Comment, paste as is

<!-- gate:body:start -->
Due diligence is the right frame, and the disclosures stop one step short of the question a buyer has to answer.

Financials, risk factors and governance tell you about the company. None of them tell you what an agent did on a given afternoon, under whose authority, and whether it stayed inside the limits it was given. That evidence lives in the agent's own record or it does not exist.

Which makes the AgentCore story and the due diligence story the same story with a gap in the middle. Isolation stops a session reaching what it should not. It does not produce anything an auditor can open afterwards and check without trusting the operator.

The teams doing this properly decide one thing early, and it is not a vendor choice. The record of what an agent was allowed to do is written by the same system that enforces the limit, and it can be checked by someone outside the building. Everything short of that is a log.
<!-- gate:body:end -->
