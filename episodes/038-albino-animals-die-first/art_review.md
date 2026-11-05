# 038 art review: assets + keyframes (art director, 2026-11-05)

**Verdict: FAIL** (one blocking asset fix: the deer read as rabbits). Everything else passes. I already fixed
and re-rendered the shotlist items the director flagged (see "Fixed by AD"). Once the illustrator redraws the deer,
re-render s072-s093 and this becomes a PASS. A second full review is not needed; the AD only re-checks those shots.

Checked: assets/previews/038-albino-animals-die-first-assets-1/2/3.png (36 assets) and all 185 keyframes
(contact sheet_01..16, s001 placeholder ignored), plus full-size crops of s003, s004, s052, s070, s085, s089, s114, s141, s144.

## Gore / kid-appeal (main risks): OK
- No blood anywhere. The deaths are the standard field-guide card plus ghost Doug with X eyes (s026, s069, s092,
  s114, s133, s156, s180). The s070 red shape is Doug's cap in the grass, and the s182-184 cap floating is the same gag. The
  sunburn beat (s024-s028) shows the gorilla suit going pink, then red, then collapsing. It is cartoon only, with no burned-skin detail.
- Predators reveal as silhouettes with red rim/glow first (herons s004/s158, lioness s048, cat s108, hawk s128,
  coyotes s085, now rimmed). None of them are shown attacking or with prey in their mouths.
- Kid-appeal: the animals are cute by nature (squirrel, hatchlings, songbird). They stay acceptable because the
  framing is adult (deaths, inbreeding, "hi friend?" then death). The one real kid-appeal risk is the deer costume
  (s089-s091). It reads as a **bunny suit** on Doug, a kids'-show image, which is fix 1.

## Blocking fix (route to illustrator)
1. **white_deer, albino_deer, white_deer_costume: the ears read as rabbit ears.** The ears are long, narrow,
   upright and pink-lined, the head is small and round, and there is no muzzle length. This shows in s072-s093 (about 20 shots), worst in s078/s082/s084
   (close-ups) and s089-s091 (Doug in the costume looks like an Easter bunny).
   Redraw: white-tailed doe ears **set out sideways in a wide V**, broad leaf/oval shape, about 1/2 the current
   length, with a grey-white inner (pink only on albino_deer, and only a thin inner line). Make the head **longer and more wedge-shaped**,
   with a dark nose tip and a dark eye with a small light ring. Make the neck a little thicker and keep the white flag tail. Optional: one small
   spike-antler buck in the herd shots for instant "deer". Apply the same ear and head shape to white_deer_costume's hood.
   Keep names and anchors unchanged so the shotlist does not need edits. Re-preview, then re-render s072-s093.

## Fixed by AD (shotlist, re-rendered, verified)
2. s002-s004 "TIME LEFT:" was blank. Changed to "TIME LEFT: ?". s005 now says "TIME LEFT: DECADES" on the
   spoken "Decades.", so the counter fills in on the beat and matches s006 onward.
3. s003/s004 tiny Doug on dark swamp. Doug + hatchling costume went from scale 0.2 to 0.34, and the glow from r120 to r190. I removed the
   water-mask rect (at the new size it showed as a dark box over the glow). He now reads clearly (auto-white ink on dark).
4. s052 empty left half. Added snowflake_face + "1: ALBINO" on the left, and the right wordart is now "2: LEUCISTIC". This matches
   "the second kind of white animal" and sets up the s055 comparison. Doug moved to the bottom-left corner.
5. s085 coyotes cut at edges. Moved them to x 330 / 1590 (fully in frame) with the standard red rim.
6. s114 death-card text touched the page curl. Moved it to the middle of the right page (y 520/568).
7. s141 "-2 DAYS" was wider than the calendar. Size 40 changed to 28, and it now sits inside the page.
8. s144 bare perch. Removed the brown pole. The gull now swoops in over the hatchlings (x 1180, y 560).

## Advisory (director, non-blocking)
9. s160, s161, s165, s167, s171: tiny Doug stands on the far hill line and reads as floating in the dark sky. Prefer the
   near bank, lower-left (y ~ 950), as in s176-s179.
10. Layout runs: s040-s042 (red 500 m circle) and s043-s045 (zone + costume) are each 3 in a row with the same
    composition. That is allowed, but consider a push-in or a different camera on s041 or s044.
11. white_hatchling_costume_crouch and _cower are almost identical in the preview. That is fine where they are used, but they
    can't carry a pose change on their own. Pair them with a Doug expression change.

## Assets (all others APPROVED)
snowflake_gorilla, snowflake_face, gorilla_icon, white_gorilla_suit (+pink, +red), white_humpback, white_humpback_carcass,
white_whale_costume, ranger_megaphone, white_lioness, white_lioness_face, optic_nerve_diagram, coyote, white_squirrel,
white_squirrel_costume, street_sign_blank, flight_feather_dark, flight_feather_white_worn, white_sneakers, white_duck,
albino_songbird, hawk_flying, white_bird_costume, turtle_hatchling, white_turtle_hatchling, white_turtle_costume,
ghost_crab, white_alligator_hatchling, alligator_hatchling, white_alligator, river_otter, white_hatchling_costume
(+crouch, +cower), field_guide_white_animals. They follow the two-tier rule (shaded, layered creatures vs crude Doug),
stay on-palette, use bold outlines, and read at contact-sheet size. The white-on-white subjects keep a grey shading pass, so they hold
on cream backgrounds.

## Keyframe consistency: PASS (pending fix 1)
- Doug is on-model in every shot: red cap is always visible (ghost included), ink is auto-white on dark swamp/night/death cards, and
  expressions come from the fixed set.
- Caption bar is present on all segment frames, and the item names match. The deaths counter steps correctly
  294 → 301, and TIME LEFT escalates (DECADES → YEARS → ? → ABOUT A DAY).
- Zone colours stay consistent within each item (gorilla cream/tan, whale sky/ocean, lion savanna, deer olive forest, squirrel
  street, bird dusk orange, turtle night beach, alligator black swamp). Escalation darkens toward the swamp finale.
- Text is legible and inside the safe area. There is good layout variety (maps, diagrams, dot grids, split screens, scales,
  silhouettes, death cards).
