# Arcezia engagement, state 3 November

He wrote at 10:22 AM: "today I am actively reviewing the docs will let you know end of the day with
more clarity."

Read: the three PDFs delivered 1 November are being read today. No question, no objection, and no
decision yet. Reply sent acknowledges and does not chase.

## What is in his hands

- `Arcezia-Action-Gate_Findings_2026-11-01.pdf` (22 KB), the findings record, seven findings, all open.
- `Arcezia_default-state_one-pager_2026-11-01.pdf`, the summary for readers who will not read the record.
- `Arcezia_write-up_DRAFT_not-for-publication.pdf`, marked not for publication until he signs it off.

## Reply sent

> Thanks Praveen, that works.
>
> While you read: the findings report is the record, the one-pager is for people who will not read the
> record, and the write-up is the only one that needs your word, since it stays marked not for
> publication until you sign it off.
>
> Two things usually get raised first. F7, because it is rated low and it is the one where the artifact
> empties a field rather than the workflow making a bad decision. And the fact that all seven findings
> are open, which is deliberate: a finding stops being open when a fix is verified, not when it is
> promised.
>
> End of day is fine. If something is unclear, ask me the specific point and I will answer that rather
> than send the documents again.

130 words, lint clean. No ask, no deadline of our own, no re-send.

## When he comes back, the four answers to have ready

1. **Why F7 is Low.** It corrupts the certificate, not the decision. The severity follows the effect,
   and the effect is a record that cannot be trusted for one field, which is bad and not dangerous.
   The fix is a validation on the token, and it belongs in the same release as F1.
2. **Why everything is open.** Because an open finding is one without a verified fix. Closing on a
   promise would make the report shorter and worth less.
3. **What a fix looks like, in his order.** F1 and F2 first, because they are the two that change what
   the default state permits. F7 rides along with F1. F3 to F6 are triage and operability, and they can
   wait for a second release without weakening the first.
4. **What the write-up claims.** The six sections in the draft, no more: sequence, cheapest path,
   production door, three things it got right, the certificate, and what was not tested. If he wants a
   section removed, remove it rather than soften it.

## Do not

- Do not re-send the documents. He has them.
- Do not ask for a call before he has said what the review found.
- Do not raise the upsell or the fee in this exchange. Wait until the review lands.
