## 2026-10-14 · Script gate (creative director)
- Screener round 3: PASS, no required fixes (script_review.md).
- **Why approved:**
  - The opener names "The Boom." at word 26, and the twist lands at about 0:35.
  - Every item has a clean one-line twist (radiator, gardener, the dad, the commute, same toe). The thesis "He came to the bird." pays off the field guide.
  - The first death lands at about 3:36. Death 150 gets no bit.
  - The human deaths sit on a sober card with no names, ages or injuries, and there is no safety advice anywhere.
  - The kid-appeal countermeasures held: the chicks are background-only and the raptor comparison is said once, as science.
  - I'd click and keep watching.
- **CD edit:** I added "The cars are winning." (4 words) after the transport-department line in The Road. This is the screener's rule 9 advisory. Total: 2,935 to 2,939 spoken words. The Road: 262 to 266.
- **Carry-forward to the director, illustrator and art director (not blocking):**
  1. Thumbnail proposal B labels: use "32 Hz" (southern) or "23 Hz" (dwarf), never "23 Hz" next to a southern bird. The brief predates the fact check.
  2. The Quills adds new assets: the wing quills close-up, a double-shaft feather, and the wing-claw X-ray. These go in asset_requests.md.
  3. The closing seedling must read as "planted", not as a bathroom joke. If it doesn't, the art director falls back to the cap by the footprints.
  4. Screener advisory for the next brief: sentence average 15-16 words and Flesch 66-70 from draft 1.
- Series bible: the counter and the 018 log row are updated.

SCRIPT: APPROVED

## 2026-10-14 · Shotlist (director)
- 265 shots. All 2,939 spoken words are covered, in order. Max 30 words per shot, and Doug appears in 90% of shots (ghost included). There are 11 chapters, and the section headers "HARMLESS." / "DANGEROUS." / "DEADLY." are white cards with `topbar: false`.
- Ramp: the forest backdrop gets one step darker per item on the severity axis (bright rainforest green, then shade green, river brown-green, dusk, near-dark and near-black). Diagrams are cream (Harmless), pale sage (Dangerous) and dark slate `#1e2622` (Deadly). WordArt uses the green-ground override everywhere on forest backdrops.
- Counter: 147 → 148 (s070 Plum), 149 (s138 Dad), 150 (s159 Swim, no bit), 151 (s184 Sprint), 152 (s208 First Pet), 153 (s230 Toe) and 154 (s257 Kick).
- **Needs art-director approval (one-off capless Doug):** s047 shows Doug with `gear: ["cap_off"]` holding `doug_cap` out over the casque for shade ("offered the bird his cap"). The cap stays in frame, and s048 puts it back on.
- The two human deaths (s240-s245) are on a sober card: plain `#0d0d0f`, white/grey text only, no Doug, no counter, no caption bar, and no names, ages or injuries. The claw never touches Doug: every death is a dust cloud, a splash or a cut-away.
- Chicks stay small (scale 0.28-0.55) and in the background or in diagrams. There is no close-up hero chick.
- Foot close-ups (`cassowary_foot`) only appear on diagram cards. In forest shots the whole bird is shown, so a lone leg never reads as severed.
- Closing: `seedling_cap` (s261, s262, s265). The fallback is `doug_cap` beside the footprint line, as asset_requests.md describes.
- Shorts: short01 The Quills (s106-s116, wing claw), short02 The Swim (s148-s159, Bingil Bay sea swim), short03 The Toe (s218-s226, "It's the same toe."). Each has a hook line and is about 42-52 s.

## 2026-10-14 · Asset gate (art director)
- All 40 new assets are APPROVED (art_review.md). The AD fixed three in the library: the `cassowary_head` casque no longer reads as a hat, the `cassowary_swallow_cap` lump is blue + Doug-red instead of the bruise purples, and the `seedling_cap` seed-husk lumps are removed (dung read). `seedling_cap` reads as planted, so the fallback is not used.
- **Capless upright Doug one-off approved: s047** (`gear: ["cap_off"]`, the cap is held out over the casque for shade, back on in s048). It is not a precedent. Placement fix routed to the director (cap in hand, scale 0.7).

- **Keyframe round 1, s135 white Doug (director, engine fix):** the auto-contrast ink check in `studio/paint.py`
  sampled one pixel above Doug's hip; on s135 it landed on a dark ground-spray speckle and flipped him to white ink on
  the mid-green Dad background. Fixed by `_bg_is_dark()` (median luma of a 9x9 sample grid), used for both Doug and
  `auto_ink` crude humans. s135 also gets an explicit `"ink": "#000000"`. s143 beam tilt (advisory) skipped: the
  `balance_scale` asset is one piece and has no tilt option.

## 2026-10-14 · Thumbnail A/B pick (creative director)
- **A wins** (thumbnail.json, Archetype C hero). Kept as is; thumbnail_b.json stays on file, unused.
- Why: at feed size (320x180), A reads as one clear threat story: the hard-eyed head looking down at tiny red-cap Doug, with the ringed claw between them. B has no Doug (our brand marker). Its RADIATOR tile (pink bird on navy) doesn't read without the video. Its four small panels lose the claw's menace, and its white ground blends into YouTube's feed.
- 2026-10-14: Showrunner run. Script 3 rounds (fact/hook/timing fixes; PASS round 3), keyframes 2 rounds (art-director + visual-screener PASS round 2), thumbnail A. Risks: Flesch ~73 (edge), 50 km/h sourced from encyclopedias, s242/s243 sober-card pop-in text added by editor (ON HIS OWN PROPERTY) re: real 2019 death — verify tone; engine ink-detection fix in studio/paint.py.

## 2026-10-14 · Final package gate (creative director)
- Inputs: visual_review.md round 3 says PASS for the main video and PASS for the shorts. qc.json has no problems (15:11, 2,939 words, 193.6 wpm overall). I checked the thumbnail, metadata.json, chapters.txt, the script opening, keyframes s001-s003 and s240-s245, and frames from final.mp4 at 1/6/11/18/25/35/45/55 s and at 838/845/852 s.
- **Title: kept** as "Every Reason the Cassowary Is the Most Terrifying Bird Alive" (60 chars).
  - It's honest: 11 reasons, and they rise to the toe and the kick. The topic noun reads at feed size, and it pairs with "SAME TOE" without repeating a word.
  - Strongest alt: "The Most Terrifying Bird That Scientists Think People Once Raised". It has more curiosity, but it sells one item out of 11 (The First Pet, at 10:34), so it under-delivers on the promise. It is not clearly stronger, so no swap. It goes on file as the A/B title test candidate if T8 CTR comes in under channel median after 500 impressions or more.
- **Thumbnail (A):** clicks for me.
  - One hard-eyed head, the ringed claw and tiny red-cap Doug make a single threat story. "SAME TOE" is a curiosity gap the video pays off at 11:59.
  - The leg runs off the top edge, so there is no severed read. It matches the opening frame at 0:00-0:02.
- **Description/chapters:**
  - Every claim in the first paragraph is in the script and sourced: 32 Hz, the radiator, about 50 days, the swim, 50 km/h, 18,000 years "may", the inner-toe claw.
  - The 11 chapters run from 0:00, ascending, and match the item order. The disclaimer and AI-use lines are present. "Do not approach wild animals." is a generic disclaimer, not safety advice.
  - The tags are on-topic and the playlist is animals.
- **First 60 s:** retention holds.
  - The thumbnail is the opening image. The "NO" in the field guide plus "MISUNDERSTANDING" sets the gag by about 6 s, and "The Boom." is named by about 8 s.
  - The twist "you might feel this bird before you hear it" lands around 0:35, inside the 45 s rule.
  - The visual changes about every 2-5 s: map, piano build, elephant, forest. The piano labels pop in cleanly.
  - Non-blocking: the 2003-study map frames Australia while the line says Papua New Guinea. PNG is visible at the top edge, so it's acceptable. Next time, centre the map on the place being named.
- **Sober cards s240-s245: tone approved.**
  - Plain white and grey on near-black, with no Doug, counter, topbar, bird, music sting or joke. That is a clean tonal break.
  - The text is restricted to dates, places and neutral facts: STRUCK THE BIRD / RAN / FELL / ON HIS OWN PROPERTY / BRED THE BIRDS / HAD FALLEN. There are no names, ages or injuries.
  - The editor's pop-in "ON HIS OWN PROPERTY" mirrors the narration word for word ("kept on his own property"). It reads as context, not blame or irony, so it stays.
  - The "naturally shy and wary" reset at s246 is respectful and does not undercut the cards.
  - Rule for future episodes: real deaths are never written as a list of what the victim did wrong. Each card gets at most one action line, and no pop-in may land as a punchline beat.
- **Series bible:** no new lore at this gate. The death counter (147 to 154) and the 018 log row were already updated at the script gate.
- Not rendered or uploaded by me. Next step: `python -m studio upload 018-every-cassowary-reason` via the showrunner, scheduled ≥ 18 h out.

FINAL: APPROVED
- 2026-10-14: Showrunner final review. The workflow reported QC exit 1, but qc.json had no problems and a re-run of qc exited 0. Visual screener round 3 PASS (main + shorts). Creative director approved. Advisories (non-blocking): s225/s226 leg fringe, s251 caption over the neck.
