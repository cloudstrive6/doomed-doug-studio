# 048 decisions

## 2026-11-15, creative director: brief
- Picked #110 false killer whale (top of `topics`, 9.5; confirmed as 048 in the 11-15 memo Decisions, item 3). Playlist `animals`; no "Doug" in the title.
- Axis: distance to Doug (about 1 km to 0 m), 9 items, bands "Their fight." / "Their dinner." / "Their family." / "Doug's share.". Boss: The Offer (Kona 1984).
- 021 constraint applied: the offer is staged in the water with a tuna's momentum, never a fish dropped into a boat; no MENU.
- Title-delivery gate: the offering must be sourced to Baird/Cascadia or a primary account before script approval; the ideas.md "Marine Mammal Science" note was not confirmed for the offering and is corrected.
- Series bible: death counter header corrected from 356 to 362 (047 had added 6 in the log but not in the header). 048 starts at 362.

## 2026-11-15, creative director: script approval (draft 2)
**APPROVED.** Screener PASS (draft 2 re-screen: facts 0, hook 9/10, structure 8, voice 8, policy 0, 2,043 words, about 10.5 min).
- Title promise: both halves are delivered and sourced. "Hunts like an orca" is shown in The Sperm Whales, The Swordfish and The Share ("the orca half of this story"). "Offers its kill to humans" is shown in The Share, The Swimmer (BC/WA salmon) and The Offer (Kona 1984), all sourced to Baird/Cascadia. The title gate in the brief is cleared.
- Opening: the first sentence is concrete (dolphins vs. sperm whales ten times their weight). The promise comes at about 0:05 and is delivered at The Offer; "more than thirty kilos" is safe because the accounts say 34 and 45 kg. "The Sperm Whales." lands at words 33-35 and the twist at about word 114.
- Escalation: the distance axis runs monotonic on the date cards, 1 km to 0 m. The Beach is a sober dip, which is accepted.
- Gags: they match the brief. Deaths are 363-368, "Doug did not agree to this." appears once, the costume gag twice, "hi friends?" once and "for me?" once. The field guide arc, DOUG'S PLATE and the cap share are all there. The outro follows the new rule. There are no 021 reuses and no fish in a boat.
- Accepted deviations: item 2 became The Dolphin Friends (no sourced dolphin-eating) and item 3 became The Swordfish (Lanai 2024 photo). Titler and graphic designer: use the new chapter names.
- Downstream notes (not script changes):
  1. Editor: keep the measured WPM at or below 200 so narration stays at 10:00 or more. Add Lanai (lah-NAH-ee) to the lexicon, and check Galápagos and Mar del Plata.
  2. Director: cut the swordfish death before contact. Draw no unhurt or smiling sperm whales and no wounds. Keep "for me?" and the cap pass deadpan, with no hearts.
  3. Director/editor: The Share's twist and The Swimmer's first sentence both state that false killer whales offer fish to people. Pace The Swimmer's opening fast (a single shot, no hold) so it plays as a reminder and not as news.
  4. Titler: keep both halves of the title; no "Doug" in it (041-043 test); no OctoLab wording.
- Series bible: the counter header is now 368 and the 048 log row has been added.

## 2026-11-15, director: shotlist
- 186 shots (s001 thumbnail + 185), narration matches the approved script word for word (2,043 words), 9 chapters, Doug in 72% of shots,
  no static stretch over ~4.3 s at 195 wpm. 15 new drawings requested in `asset_requests.md`.
- HUD on every shot except the sober cards and the outro: DOUG DEATHS at (1590, 162), `dougs_plate` at (1180, 166) scale 0.42 (empty
  until s182, then a small tuna), and a TO DOUG meter (size-28 label at (1622, 238) with `false_killer_whale_fin` at 0.16) carrying the
  date-card distances: ABOUT 1 KM / 500 M / 200 M / 100 M / 50 M / 20 M / 10 M (beach, from the brief) / 5 M / 0 M.
- Colour ramp: one water step darker per item (`#3a9ad9` -> `#14365e`), no depth-zone hexes except the two dive diagrams (s059-s060,
  s094) where the zones are the point. The Beach and the boss use the regional-ramp dusk sky.
- CD notes applied: the swordfish never touches Doug (s067 bill-first with ~300 px clear, cut to s068 death); no wounds, blood or
  stranded whales anywhere; "for me?" and the cap pass are deadpan with no hearts; DOUG'S PLATE stays empty until s182 (SERVED stamp).
  The Swimmer's first sentence is one shot with `pause_after` 0.05 and no hold.
- One-offs to log: field guide name is "FALSE KILLER WHALE" (3 words, wrapped to two lines at size 28 instead of the 2-word rule);
  The Beach uses upright Doug with `cap_off` holding a `doug_cap` (script: "cap in his hands"; exactly one cap in frame); s161 shows the
  narrator's pre-drawn death as a small sketch on a white card (no counter tick; the counter stays 367 until s181).
- Shorts (`shorts.json`, validator OK): short01 s164-s175 The Offer (Kona 1984, ~51 s), short02 s150-s160 The Swimmer (salmon taken
  back, ends "Doug is fine.", ~39 s), short03 s050-s061 The Swordfish (Lanai 2024, ~46 s). Titles are director placeholders because the
  validator requires one; the titler should replace titles and fill descriptions.

## 2026-11-15, creative director: package gate (thumbnails A/B/C)
Viewed build/thumbnail.png, thumbnail_b.png and thumbnail_c.png at 1280x720 and at 168x94 (the *_small.png files), each with
its paired title from metadata.json `packaging.variants`. `package check --dry-run` returns OK. **There is no visual_review.md
for 048 yet**, so this is the creative verdict only. Nothing ships until the visual screener passes all three. Thumbnails were
not edited.

- **A, "IT'S A GIFT" / "False Killer Whales Hunt Like Orcas, Then Hand Us Their Kill": APPROVED (pending screener).** I would
  click it. It reads at feed size: yellow sky, cyan water, a black toothed whale, a bright tuna pointed at a small screaming
  Doug. The open mouth with teeth sells "hunts like an orca", and the tuna held by its tail toward Doug sells "hand us their
  kill". The caption adds tone and does not repeat the title. No blood, no boat (021 rule kept). The bottom-right badge area is
  empty water. Advisory, not a blocker: the tuna is about Doug's height. A 34-45 kg yellowfin is about 1.2-1.4 m, so do not make
  it any bigger.
- **B, "FOR ME?" / "False Killer Whales Kill Like Orcas, Then Offer Humans Tuna": CHANGES.** At 168x94 it is the weakest of the
  three. It is also nearly a mirror of A, so the test would mostly compare background colours.
  1. The dark royal blue background swallows the charcoal whale at feed size. Use a clearly lighter blue (about the cyan in A
     or one step darker), or a two-tone surface and depth split like A, so the whale's silhouette pops.
  2. There is a black stub cut off at the right edge (x about 1270, y about 390), the remains of the tail. Either fit the whole
     fluke in frame or crop the body cleanly with no stray shape.
  3. Make the concept "Doug in peril" so it differs from A. Scale the whale's head up so it fills the right 55-60% of the frame,
     mouth open, stopped about a tuna length from Doug. The upper right is currently about 40% empty blue. Keep Doug at his
     current size with goggles. Bigger whale plus small Doug is the click.
  4. Keep "FOR ME?" bottom-centre, clear of the duration badge (it is clear now).
- **C, "30+ KG TUNA" / "A Dolphin That Hunts Like an Orca Offers Humans Its Kill": CHANGES.** At feed size the tuna is the hero
  and the whale reads as a small grey fish. That undersells "hunts like an orca" and inverts the scale.
  1. Scale. The tuna is about 1.5x Doug's height and as big as the visible whale. Per facts.md the fish is 34-45 kg (about
     1.2-1.4 m, so about 2/3 of Doug) and the whale is up to 6 m and over a tonne. Shrink the tuna to about 2/3 of Doug's height
     and show more of the whale so it is clearly the largest thing in frame. The "30+ KG" must not be paired with a fish that
     looks 200 kg (packaging must not overstate the video).
  2. The concept calls for a tag on the fish, but it is drawn as a floating banner. Run a string from the tag's hole to the
     tuna's tail and tilt the tag a little more, so it reads as a price or luggage tag (the 047 C "200,000" tag grammar).
  3. Show the push: add 2-3 short motion lines behind the tuna, pointed at Doug. The tuna's momentum is the joke of The Offer.
  4. Move Doug up and left so his feet clear the bottom-right duration badge (about x 1130-1270, y 670-710). Right now his feet
     sit in it.
  5. Keep the hot-pink background. It is the most distinct of the three in a feed and fits the saturated-flat archetype.

Next: the graphic designer applies the B and C changes. Then the visual screener reviews all three (feed size, policy, badge
area). Then I re-review B and C. A needs no rework.
