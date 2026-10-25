# Truefolio in-app runbook, A1-A6 (operational)

Companion to item 6b in the 10-25 verbatim. Follow top to bottom;
each step = find, do, capture, if-not-found. Total budget 30-45 min.
Phone or laptop works; laptop is easier for the incognito checks.

## 0. Before you start (2 min)

- Use ONE real brokerage account you're comfortable connecting
  read-only. The Plaid scope is investments only (verified on their
  public page), so the app cannot trade or move money. Still: do NOT
  connect a bank account if given the option, do NOT enable push
  notifications, do NOT export or share anything you didn't intend.
- Capture rules for everything below:
  - percentages, UI labels, screen order, timings = fine to capture
  - real dollar balances, brokerage name/logo, account numbers =
    NOT fine. If a screen shows a real balance, do not screenshot it;
    write "dollar amount present: yes/no, which screen".
  - screenshots are for scope text, settings UI, and the public
    (percentage-only) view only.
- If a control is missing, log "not found" and move on. Missing
  controls are data, not a failure.
- Cleanup last (step 7): set profile private / disconnect the
  brokerage / or delete the account if you don't want it standing.

## A1. Onboarding + link (5 min)

- Install from the App Store (id6809170313) or Google Play
  (package app.truefolio), or try the web app if the marketing
  site gives an app URL.
- Note sign-in options offered (email / Google / Apple). Pick any.
- Time it: start a timer at first screen, stop at first portfolio
  data on screen.
- At the Plaid link screen: screenshot the scope/permission text
  Plaid shows (the "allows access to..." wording). This is your
  A2 evidence.
- Capture: sign-in options, number of screens, data asked at each
  step (name? email only? country?), timer result, the Plaid
  permission wording.

## A2. Scope confirmation (3 min)

- On the same Plaid permission screen, check the wording:
  - should read: view investment accounts, positions, balances,
    transactions
  - must NOT read: trade, transfer, deposit, withdraw, edit
  - anything trade/transfer-adjacent = finding, screenshot it.
- If there's a "connect another account" option later, note which
  account types it offers (brokerage only? banks too?) and what
  Plaid scope the bank option would request.
- Capture: the scope wording, account types offered.

## A3. Display-layer test (10 min)

This is the one that tests "others see percentages, never your
dollar amounts."

- Settings or Profile: find sharing / visibility / public profile /
  leaderboard. Screenshot the settings UI itself (it shows what's
  controllable, which is part of the audit).
- Set the profile to public, or join the leaderboard, whatever the
  mechanism is.
- Now view it as a visitor. Do NOT use your logged-in session:
  - copy your public/share profile link if one exists
  - open it in an incognito/private window (laptop), or ask no one
    and just use the share link in incognito
  - if there's a leaderboard page, open that in incognito too.
- On the public view, check every surface: profile header,
  holdings/allocation block, performance block, leaderboard row.
  Zoom in. The check is binary: any dollar-denominated figure
  anywhere = finding. "Dollar amount present: yes/no + which
  screen" is the record; the amount itself is not needed.
- Capture: incognito screenshots of the public view (they should be
  percentage-only; that is the proof), a list of the surfaces
  checked, the binary yes/no per surface.
- Also note: is the public view a URL others could find? Is it
  opt-in or opt-out? (default state at creation = a finding
  either way if surprising)

## A4. TWR cross-check vs your broker (10 min)

- In the app: find the performance / TWR / Skill Score page.
  Record the periods it shows (1M / 3M / 6M / 1Y / since
  inception) and the number for each.
- At your brokerage: pull the same account's own time-weighted
  returns for the same periods (most brokers have a performance
  report; if not, monthly account returns + your deposit dates is
  the fallback).
- Compare period by period. Expected: small differences (their
  disclaimer admits closing prices can differ slightly from broker
  figures). Material differences (bigger than rounding/timing) =
  finding; record the period, the app number, the broker number,
  and the delta as percentages only.
- Capture: a 2-column table, app vs broker, per period, deltas.
  Percentages only.

## A5. Deposit-strip test (10 min)

Their headline claim: "adding cash cannot flatter the number."
Test it on your own account.

- Find the month in your history with the largest deposit (or
  withdrawal).
- In the app: find that month's sub-period return if the app shows
  monthly/sub-period TWR. The check: that month's TWR should
  reflect the pre-deposit portfolio's market return, not the
  deposit size. If you deposited on day 1 and the market rose ~2%
  that month, the app should show ~+2%, not the diluted/boosted
  arithmetic return.
- If the app only shows an aggregate since-inception number with no
  monthly breakdown: that is itself the finding. Log exactly:
  "no sub-period view; stripping cannot be verified in-app; the
  same gap exists on the public sample page (+15.92% with no
  cash flows shown)."
- If your account has no significant cash flows: log "insufficient
  cash-flow history; test not executable" and keep the sample-page
  gap as the documented instance. Either way the report has
  something true to say.
- Capture: the month chosen, what the app does/doesn't show for it,
  the result or the limitation, in one paragraph.

## A6. Controls audit (5 min)

- Settings, one pass. Screenshot the settings list (safe).
- Check presence of: profile visibility toggle, brokerage
  disconnect, data export, notifications control, delete account,
  delete profile.
- For delete: does it exist in-app? What does the confirm dialog
  say? (Their policy promises self-service deletion + 30-day
  restore; the app should match. If deletion is "email support"
  only, that's a mismatch vs their own policy.)
- Do NOT actually delete anything unless you're done with the
  account.
- Capture: the settings list screenshot, one line per control:
  present / absent / what it says.

## 7. Cleanup (2 min)

- Profile back to private (or disconnect the brokerage, or delete
  the account if you chose that path).
- You're done. Paste the capture into item 6b's template in the
  10-25 verbatim (or just paste everything here in chat and it gets
  logged) and I write the full review + the follow-up to Hod.
