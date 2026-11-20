---
deliverable: internal
id: 2026-11-20_review_eri-test-mockups-v0-1
date: 2026-11-20
audience: internal
status: ready
title: Review of Eri Test Mockups v0.1, nine pages, thirteen screens
sources_read: >-
  read: Eri-Test-Mockups-v0_1.pdf, nine pages, text extracted and every page rendered and looked at. No page opened.
---

# What it is

Marvin's design companion, dated 19 November, thirteen screens across three parts: the verifier's flow, what others
see, and the four results. It cites the v0.4 amendments by number and adopts REQ-046 and REQ-014 explicitly.

# What is genuinely good, in order

1. **Nothing fake is presented as real.** `[POSTCODE]`, `[TX ID]`, `[BLOCK TIME]`, `[ISSUING OFFICE]`, invented
   fingerprints marked as invented, a QR code that says it does not scan. A design pack that refuses to invent a
   postcode because nobody has seen one is a pack written by someone who intends to be believed.
2. **Every screen carries a "check in the test" box** that restates an acceptance criterion. The design and the
   requirements are wired together, which means an argument about a picture can be settled by a criterion.
3. **The five undrawn states are listed rather than omitted.** REQ-047, 048, 049, 050 and the REQ-014 caption are named
   as missing from v0.1 and promised for v0.2. That is the honest way to hand over a first version.
4. **Badge colour is doubled with words.** "Colours differ in lightness as well as hue, and every badge carries words."
   That is the difference between a design that survives a photocopier and one that does not.
5. **The disclaimer is locked against the brand file.** A licensee can rename the product and cannot delete the sentence
   saying what it does not prove.

# The four things to change before v0.2

## 1. "Nothing has been changed since" becomes false on the second seal

Screen 9 says the page holds exactly what was sealed on 19 November, "Nothing has been changed since." REQ-030 allows new
items to be added and sealed in a second batch, so the first time that happens the sentence is untrue on the page that
matters most.

Change: make the panel per batch. *"Three items sealed on 19 Nov 2026 at 11:20 WAT. Nothing sealed at that time has changed
since."* If later batches exist, a second line lists them with their own anchor references. The claim then stays true
for the life of the file.

## 2. Green with a tick reads as approval

The panel is green with a tick and says "All 3 items match". The sentence that stops it being read as approval, that
this says nothing about ownership or title, is at the foot of the page in small grey.

Change: move that sentence up beside the badge, in the reading order, before the item list. Keep green for the narrow fact
it earns, which is that the sealed batch is unchanged, and let the ownership denial sit at the same weight as the claim.

## 3. Part 3 is a different product surface

The four results are drawn on a **postcode check**, which belongs to the register. The prototype's public check (REQ-034
to REQ-036) is a **file check**, reached by QR or link. Both are right, and they are not the same screen.

This matters because only one of them is inside the forty-five. Either cycle four builds a postcode check, which means
requirements that do not exist yet, or Part 3 is labelled as the register rather than the prototype and stays a design
asset. REQ-053, the fourth answer, needs to say which page it lives on before it is built.

## 4. The name is spelled two ways in one document

The header says Ẹ̀rí. The brand configuration field says Ẹrí. The brand field is the value the whole application reads,
so this is not a typo in a picture, it is two different products depending on which page loads.

Change: one string, in the brand file, and every screen renders it.

# The Yoruba pass

Screen 11 carries six strings the owner must correct, by his own standing rule that he is the speaker and no one else
is. The ones that need attention, with the English they are translating:

| On screen | English | Note |
| --- | --- | --- |
| Gbogbo nǹkan mẹ́ta bá a mu | All 3 items match | Consider "bá ara wọn mu", which is the usual construction for things agreeing |
| Ohun tí ò wà níbi ni ohun tí a fi édíidì ní 19 Nov 2026, 11:20 | What this page holds is exactly what was sealed on 19 Nov | "édíidì" is a loanword where a Yoruba verb would read better, and the sentence needs the tone marks checked throughout |
| Kóòdù NIPOST | Postcode | Decide whether the interface borrows "kóòdù" or names it in Yoruba |
| Olùṣàyẹ̀wò ẹ̀rí sí i | Attested by verifier | Reads oddly; a verb construction such as "fọwọ́ sí i" is the obvious candidate |
| Àwòrán olùṣàyẹ̀wò ẹ̀rí sí i | Image, attested by verifier | Same as above |
| Ọjọ́ tí a ṣe àyẹ̀wò | Checked | Fine, but the date format under it should match the English screen exactly |

None of this is a criticism of the design. Screen 11 correctly says the strings are unchecked and assigns the pass.

# What to ask for in v0.2

The five undrawn states, the per-batch seal wording, the disclaimer moved up, and one spelling of the name. Nothing
else. Everything else in the pack can be built as drawn.
