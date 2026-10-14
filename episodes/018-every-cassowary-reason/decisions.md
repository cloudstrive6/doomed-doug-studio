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
