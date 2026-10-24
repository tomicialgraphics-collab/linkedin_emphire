# COMMENT SURFACES — TRACKED LIST

Source of picks for the daily comment round (empire_pipeline Stage 2,
Step 2.1). Built from the owner's network read 2026-10-23 (684
followers, 468 following). This is a menu, not a quota: pick
8 fresh (up to 12 under the extension guardrails, protocol 1)
posts across tiers per day.

## Protocol (per 2026-10-23 analytics + feed data)
1. 8 comment actions per day base, extendable to 12, hard
   ceiling 12. Spaced across the day, never a burst. The
   10-23 event (14-16 actions in about an hour) was a
   clustering risk, not a count risk, and no throttling was
   observed, so the 10-24 expansion raises the ceiling and
   keeps the anti-clustering guardrails. Extension guardrails
   (ALL must hold on a 9-12 day):
   a. Max 2 actions per hour, 60+ minutes between new
      comments (replies exempt on an active thread)
   b. At least 4 actions on tier 1-2 surfaces or
      thread-partner replies (quality floor)
   c. At least 2 actions are INTERACTIVE replies
   d. Never more than 3 actions in any 2-hour window
   The cap counts SHIPPED actions on real surfaces. Weak,
   out-of-lane, and company-page surfaces are skipped
   regardless of headroom; headroom is not a license to fill.
   REVIEW TRIGGER (10-30 weekly snapshot): if a 10-12 day is
   followed by a comment-impression drop against the
   reply-tier baseline (Paolo reply 3,722 class), log a
   throttling signal and revert to the base 8 until the next
   90-day check.
2. A comment action = a comment OR a follow-up reply. Follow-up replies
   are first-class: threads compound (Paolo Perrone thread: main + 2
   replies; the reply alone hit 3,722 impressions).
3. Fresh posts only (same day or yesterday). Stale posts do not push.
4. Tier 1 first (reach), tier 2 for home-turf authority, tier 3 as
   spice.
5. One thesis (the check frame) across all tiers, different surface
   each time. No two comments in the same 24h may reuse the same
   closing line.
6. If an author replies (supportive or hostile), the reply is a
   scheduled action the same day. Hostile reply protocol: do not
   defend, serve the verifiable claim, invite the re-run (reference:
   the 10-23 Filip R. exchange on the Endrit banks thread).
7. Pick the mode before drafting (ENGAGEMENT/voice_dna.txt
   COMMENT MODES, 10-24 fine-tune): OUTSTANDING for tier 1-2 main
   comments (90-120w, one memorable line), QUESTIONING when the
   post has a checkable claim or number (90-120w, lead with the
   line that does not hold), HUMAN for personal and community
   posts (20-80w, frame invisible), INTERACTIVE for replies
   (15-60w, question allowed there only). Max 2 OUTSTANDING a day.
8. Run the slop detector before every post (voice_dna.txt PART 10,
   THE HUMAN GATE): 0 em dashes, 1-4 natural contractions (never
   in the first line), inside the mode budget and under the post's
   length, argument test passed (one line a hostile reader could
   argue with), no CATEGORY 7 openers or closers, at most one
   specific earned compliment after the first line (the author
   must be able to point at the line; in HUMAN mode it is the
   payload), uneven paragraphs, no bullets, flat ending. 10-24
   context: Jada
   Balster's post shows the market now complains out loud about
   the exact shape this gate removes.
9. SOURCE RULE (10-24, owner standing instruction: always read
   the read-more link before commenting). If the post carries a
   read-more, article, paper, or report link, fetch and read the
   full source before drafting. Comment on what the source
   actually says; cite specifics (numbers, conditions, p-values,
   design details) to the source, not the post body; the comment's
   added value is often the one finding the post omitted. If the
   source cannot be fetched, say so in the tone notes and draft
   from the post body only, marked UNVERIFIED-SOURCE.
10. PROFILE READ + METHOD LADDER (10-24, owner direction: read
   the author's profile before choosing the move). For every
   pasted surface, read the author's block BEFORE drafting
   anything:
   - Relationship: Following / followed back? degree (1st, 2nd,
     3rd+), mutuals shown in the paste
   - Positioning: headline, what they post about, their tier in
     this file
   - Commercial signals: services page, newsletter, "book a
     call", top-creator badges. Commercial author = value added
     only, never a pitch
   - History: is this a thread partner (see
     published_comments archive)? If yes, replies outrank new
     comments
   - ICP fit: security, research, evals, red team, big tech,
     journalism
   Use only what the paste shows. Any field missing from the
   paste is UNKNOWN, not a guess.
   METHOD LADDER (first match wins):
   1. Thread partner, or a reply is owed → INTERACTIVE reply,
      same day, first-class
   2. ICP profile (security, research, evals, big tech) →
      follow-back if not followed; comment only if the post is
      in lane, otherwise follow-back alone
   3. Tier 1-2, Following, fresh, in lane → comment
      (OUTSTANDING or QUESTIONING)
   4. Tier 1-2, Following, fresh, strongly on brand, and the
      post carries a line worth putting on the owner's own feed
      → repost with thought (40-60w, one bankable line, one
      specific compliment). A repost REPLACES the comment on
      the same surface, it never stacks with it
   5. 2nd or 3rd degree, in lane or ICP-adjacent, fresh
      → comment (HUMAN or OUTSTANDING) or follow-back alone
   6. Weak fit, out of lane, or stale (any degree) → skip,
      log the skip and the reason in this file's refresh
      notes
   POSITIONING FROM THE PROFILE (how the same frame bends):
   - Peer in the same niche: comment is a positioning statement
     for the third party reading the thread, not a message to
     the author; equal footing, differentiate the framing, do
     not mirror theirs
   - Generalist or creator: bring the check as new information,
     one concept they can reuse
   - Commercial author: add value that stands without their
     product; do not feed their CTA

## Tier 1 — big reach (your comment rides into the author's audience)
Chip Huyen, Ethan Mollick, Sebastian Raschka, Eugene Yan, Hamel Husain,
Simon Willison, Jerry Liu (LlamaIndex), Amjad Masad (Replit),
Paolo Perrone (60,500-imp thread origin; keep watching),
Prasad Rao (AWS Principal SA, following, added 10-24 evening)

## Tier 2 — home turf (LLM security / red teaming; this audience hires)
Kai Greshake, Leon Derczynski (garak, NVIDIA), Battista Biggio
(Cagliari), Dustin Farley (Lakera), Pete Bryan (Microsoft AI Red
Team), Clint Gibler (OpenAI), Ian W. (Promptfoo / OpenAI), Joseph
Thacker, Rebecca Huteson, Alex Combessie (Giskard), Keren Katz
(Zenity, OWASP Agentic Top 10), Hyrum Anderson (Abundant Security),
Rock Lambros (Zenity), Tarique Smith (Zero Day Agent),
Nathan Hamiel (Sr Dir Research, AI security, keynote speaker,
following, added 10-24 evening)

## Tier 3 — builder / adjacent layer + active thread partners
Ado Kukic (Claude Code community), Jason Liu (OpenAI DevEx),
Ife Abimbola-Olulesi (Proof), Shehbaz Pathan (RAG / agent memory),
Alex Banks, Sam Illingworth (Slow AI), al neitsch, Endrit
Restelica, Helen Oakley (Zenity), Robinson Miranda, Tanay
Kothari, Salman Lakhani (SIGNAL/NOISE corroboration board;
10-24 confirmed author of the Sweden post, thread partner,
follow-back pending), Chris H., Madhan Vadlamudi, Ned Lowe,
Sudarshan Thorat

## Groups (free distribution; separate from the comment round)
- Group 6773411: the 90-day top performer is a post in this group
  (1,053 imp, VERIFIED_POSTS row 15). Sunday planning decision:
  cross-post the week's strongest standalone, or publish a
  group-native post with a group-specific question close (the
  "Question for this group" pattern worked).

## Skip log (10-24)
- GenAI Works (company page, 11m at paste): Jensen Huang
  Vera Rubin tray, assembly 2h to 5min. Skipped per protocol
  10 rung 6: company/marketing surface (contact-us + UTM
  link), no relationship, not followed, not in tier list,
  out of core lane (infra manufacturing, not the check
  frame), and the day was at the 8/8 action cap. The
  in-lane angle (the constraint is tray-to-serving time,
  not assembly time) is noted in case the owner overrides.
- The AI Colony (company page, 25m at paste): US banks
  blocking third-party AI agents (Axios report, Morgan
  Stanley / BofA / JPM / Wells, credential-sharing gap,
  move to read-only). Skipped per the company-page rule +
  day cap. Topic is on-lane (authorization when the user
  is the credential); held for a person's surface (Endrit
  banks thread territory) or a standalone with the Axios
  source fetched under the source rule. Resolved 10-24
  evening: shipped as a comment on Endrit Restelica's own
  Axios post (published_comments item 7), the
  authenticity-vs-authorization split.
- 10-24 evening feed batch (all rung 6, weak fit or out of
  lane, logged so headroom never fills with them): Tiago
  Forte (annual review / book promo), Patrick Bet-David
  (motivation video, no substance), Blossom Affia (two
  self-reposts, personal brand), Harrison Chase reposting
  Tom Loverro (founder durability, VC), Michael Bargury
  repost (speaker thanks, thin; same event covered by the
  Rock Lambros recap, one surface per event), Kieran Drew
  (mindset), Ruben Hassid (Claude productivity promo,
  weak fit), Endrit Warhound dogs (bio/military),
  Iyinoluwa Aboyeji repost (founder philosophy), job alert
  + event-hosted notifications (not surfaces).
- Exabeam (company page, reposted by Steve Wilson, 1d at
  paste): "Agentic SOC / machine speed" product marketing,
  ow.ly tracked link, hashtag wall, solution-brief CTA.
  Skipped per protocol 10 rung 6 + company-page rule:
  vendor marketing, not a security publication (no
  research, advisory, or technical disclosure to engage),
  no relationship to the company or the reposting author,
  not followed, 1d old. The "keep humans in control" line
  is a vendor claim, not a check; answering a claim with
  positioning on a marketing post is the slop pattern the
  engine avoids. Skipped on quality, not the cap.

## Refresh rules
- On any network or feed paste: add new qualifying surfaces (reach,
  home turf, or active thread partner) with their tier.
- Demote a surface after 3 consecutive comments under ~20 impressions
  or zero replies; log the demotion and why in
  LINKEDIN/performance_tracker.md.
- Follow-back audit each refresh: any thread partner or tier 1-2
  author not followed back gets a follow (10-23 finding: Robinson
  Miranda was a thread partner and not followed back).
- Rebuild the whole list from the network read every 90 days,
  aligned with the 90-day tracker snapshot.

Last refreshed: 2026-10-24 (protocols 7-10 added:
comment modes + slop detector + source rule +
profile read and method ladder, 10-24 humanization
fine-tune; daily cap expanded 8 base / 12 max with
anti-clustering guardrails + 10-30 review trigger)
