# Steve Higgins provider-failover DM, 2026-10-30

## INPUT (verbatim from owner paste)

- **[Olusanya Timothy](https://www.linkedin.com/in/ACoAAFVrvC4BQf66VerIn0wpyEPPd_akPxxKhfA)** 9:46 AM
  -
  -
  -

  hi steve

  A chatbot digital twin with automatic LLM provider failover is the interesting part of what you build, every provider switch changes the system that answers underneath the same prompt, and the model version in the logs stops being a single fact. Do you log which provider actually answered each turn, or is that the part of the system that only shows up when it fails?
- **Today**Steve Higgins sent the following messages at 9:40 AM

  **[View Steve’s profile](https://www.linkedin.com/in/ACoAAAS_NuUBGLz0--bTApdgw0iw64GmiXOL5XY)**

  **[Steve Higgins](https://www.linkedin.com/in/ACoAAAS_NuUBGLz0--bTApdgw0iw64GmiXOL5XY)** 9:40 AM
  -
  -
  -

  Hi Olusanya,

  Thanks for your comments.
  This was a simple low budget demo, using entry level accounts with LLM providers. It is read only, and doesn't log anything.
  I agree this would be important for a more complex app.

## DISCUSS

- Steve replies to the owner’s question about per-turn provider logging.
  He clarifies this is a low-budget, read-only demo using entry-level
  provider accounts and currently has no logging. He agrees logging
  would matter in a more complex application.
- This is a warm new-connection practitioner conversation. The owner’s
  earlier message has been sent; this is the first substantive reply
  from Steve captured in the record.

## THOUGHT

- Acknowledge the project scope instead of arguing that a demo needs
  production telemetry. Suggest one minimal, useful record only if the
  app grows: provider and model per turn, so failover is observable.
  Ask one open but bounded question about whether he intends to expand
  the demo.
- No pitch or link. No promise of help or assumption that he is
  building a production service.

## DELIVERABLE

DRAFTED, not sent. 55 words / 314 characters. 0 contractions; 0
en/em dashes; 0 banned terms.

Thanks, that clarifies it. For a low-budget, read-only demo, no logging
is a reasonable tradeoff. If you extend it, even a small per-turn
record of the provider and model that answered would make failover
visible when something goes wrong. Is that something you might add as
the app grows, or is it staying a demo?
