# Art review: 009 One Night in Every Prehistoric Ocean, round 1 (assets)

Reviewer: art director, 2026-10-08. Scope: the 45 new library assets in `asset_requests.md`. This round does not review keyframes.

I checked them against `channel/art_bible.md` (two-tier rendering, palette, no gore), style bible section 7 (Art Director rules 1-9), and the
director's sizes, anchors and named local points. Sources:
- every `assets/previews/009-*` sheet
- my own inspection renders of each asset at scale 1, on white, on Miocene navy `#0a1630`, and as `silhouette: true` on `#112f4f`, with the measured local bbox and anchor
- side-by-side renders against the library look-alikes (`megalodon` vs `great_white_shark`, `livyatan` vs `sperm_whale`, `time_machine_closed` vs `time_machine`)
- an automated check for `spray` discs that leak outside their shape
- 15 draft keyframes (s034, s052, s100, s109, s116, s124, s126, s129, s132, s189, s198, s228, s230, s253, s254) to see the riskier assets in their real shots

## Verdict: FAIL (1 asset rejected, 44 approved)

## Rejected (route to the illustrator)

1. **`helicoprion`** (B SIL, 7 shots, the item's "where the spiral went" payoff). Three problems:
   (a) The whorl does not read as a spiral. The lower-jaw shape (element 41) and its belly band (42) are drawn *after* the whorl (15-40), so they cover the bottom two thirds of it. At phone size s126 ("like a circular saw") shows only a fringe of cream spikes.
   (b) The head is deeper than the body (top y -156, bottom +144 at x 200-300). The fish reads as a tadpole or sperm whale, which is especially clear in the s109 silhouette. The asset is also 376 tall against the director's 300 box.
   (c) The eye (r25, pupil r11, high thin brow) plus the huge gape makes a goofy "shocked" face. That breaks the brief's "predators look dangerous, no cute faces" rule.
   **Exact fixes** (keep the anchor, the whorl centre (+280,+80) and the toothless upper lip through (+285,-60)):
   1. Move elements 41 and 42 (lower jaw and its pale band) so they come **before** element 15. The whorl then sits on top of the jaw. Raise the whorl disc (15) to r 56 and scale the tooth ring (16-29) and spiral (30-40) by 1.15 about (280,80), so the full spiral of about 3 turns is visible, with the largest teeth at the upper right.
   2. Flatten the head. In the body outline (elements 4 and 14) change (386,-124) to (386,-100), (310,-150) to (310,-118), (200,-156) to (200,-128) and (90,-146) to (90,-124). Lower the back band (5) by the same amounts. Move the first dorsal (1, 2) down by 28. Move spray 7 to y -95. Target height is 300 or less (about y -180..+150 including the fin).
   3. Make the eye match our other predators: r 16, pupil r 8 at (+3,+2) from the eye centre, eye centre at (310,-88). Use a heavy brow line of width 6 from (284,-104) to (334,-98) that overlaps the top of the eye (as on `xiphactinus` and `pliosaurus`). Keep the brow above the lip at y -60.
   4. Re-check the silhouette. It must show a pointed snout and a jaw notch, not a round whale head.

## Approved with non-blocking cleanup (illustrator, next pass; these do not hold the stage)
2. **Spray leaking outside shapes.** These read as dust specks on sky or navy. Pull each spray centre inward or shrink `r` until the disc stays inside its fill:
   - `skateboard` #9 (-60,-50) r20, a smudge above the deck
   - `computer_keyboard` #2 (-150,-40) r40, visible as grey dust above the top-left edge on navy
   - `crt_tv` #14 (-200,-140) r50, above the top-left corner
   - `pickup_truck` #13 (120,-250) r40, above the roof
   - `xiphactinus_fossil` #5 (-100,130) r45, below the slab
   - `livyatan_tooth` #4 (150,10) r40
   - `basilosaurus_leg` #12 (110,-60) r50, visible under the body patch in s253
   - `dorset_cliff` #10/#11 can stay, because they read as crumbling dust

   The sparkles on `time_machine_closed` are intentional and match `time_machine`.
3. **`pickup_truck`**: the wheel bottoms reach y +9, not 0. Raise the wheels and tyres by 9 so the truck doesn't sink into the ground line.
4. **`basilosaurus_leg`**: the rounded body patch reads a little like a loaf. If there is time, give the patch flatter top/bottom edges and extend it to the full x -185..+185 width so it reads as a section of the long body. The leg itself (thigh, knee, ankle, three toes) reads clearly.

## For the director (composition, not assets)
5. **s253**: the `KNEE` arrow lands on the body patch and the `ANKLE` arrow lands on the knee. In the asset the knee is at local (-110,+25), the ankle at (-90,+108) and the toes at (+42,+112..+144). Re-aim the arrows (x scale, plus the asset's x/y).

## Per-asset verdicts
| # | Asset | Verdict | Notes |
|---|---|---|---|
| 1 | `anomalocaris` | APPROVED | Predatory, not a toy. Spined curled arms, stalked eyes and a tail fan all read in the silhouette. Salmon reads on navy. |
| 2 | `skateboard` | APPROVED | Bottom-centre anchor, wheels on y=0. Cleanup 2. |
| 3 | `snorkel` | APPROVED | Matches `snorkel_gear` (blue J, yellow tip, black mouthpiece). Clean J silhouette. |
| 4 | `endoceras` | APPROVED | Long tapering banded cone, tentacles to the right. Clean silhouette. |
| 5 | `endoceras_shell` | APPROVED | Faded, chipped, flat bottom at y +100, dark hollow opening centred about (+434,+5). Reads in s052. |
| 6 | `nautilus` | APPROVED | Tiger stripes, hood, tentacles. Not a predator, so the softer face is fine. |
| 7 | `pickup_truck` | APPROVED | Dark blue crew cab with a flat open bed. Cleanup 2 and 3. |
| 8 | `jaekelopterus` | APPROVED | Dark glossy red-brown, kidney eyes, paddles, telson, toothed claws. Menacing top view with a clean silhouette. |
| 9 | `jaekelopterus_claw` | APPROVED | Stone-coloured toothed pincer, broken lower tip. |
| 10 | `computer_keyboard` | APPROVED | Width matches the claw. Cleanup 2. |
| 11 | `arthropleura` | APPROVED | Legs touch y about +80. Dark plates with pale edges. |
| 12 | `japanese_spider_crab` | APPROVED | Mostly legs, leg tips at the bottom corners, white spots. |
| 13 | `garden_spider` | APPROVED | Reads as a spider icon at small size. |
| 14 | `lobster` | APPROVED | Dark red-brown, claws forward, tail fan. |
| 15 | `dunkleosteus_old` | APPROVED | Same armoured head on a long faded eel body. Reads as "old textbook" next to `dunkleosteus` (s100). |
| 16 | `helicoprion_whorl` | APPROVED | Three-turn spiral, largest teeth at the outer upper right, grey stone disc. |
| 17 | `helicoprion` | **REJECTED** | See fix 1. |
| 18 | `helicoprion_guess_nose` | APPROVED | Sepia old-book look, whorl curls up and back from the snout. Transparent background. |
| 19 | `helicoprion_guess_tail` | APPROVED | Same fish, whorl replaces the tail. |
| 20 | `helicoprion_guess_fin` | APPROVED | Same fish, whorl stands on the dorsal. The trio is clearly a set (s132). |
| 21 | `ratfish` | APPROVED | Mid-tone, green eye, tooth plates, wing pectorals, rat tail. Reads on `#0a1630`. |
| 22 | `cymbospondylus` | APPROVED | Slim with a long toothy snout, clearly not our chunky `ichthyosaur`. Silhouette OK. |
| 23 | `cymbospondylus_skull` | APPROVED | Sclerotic ring, long toothy snout, cream bone. |
| 24 | `pliosaurus` | APPROVED | Big croc head, white teeth on a dark red mouth, angry eye. The neck seam is a little hard but fits the armoured look. |
| 25 | `pliosaur_skull` | APPROVED | Large conical teeth, eye socket. Fits the `dorset_cliff` hollow. |
| 26 | `crt_tv` | APPROVED | Screen measured at centre (-9,-16), 342x264, empty apart from a faint static glow. Cleanup 2. |
| 27 | `dorset_cliff` | APPROVED | Grey/cream bands, cracks, loose rocks. Hollow measured at about x -180..+186, y -178..-28 (centre about (0,-103)), and the skull fits. |
| 28 | `xiphactinus` | APPROVED | Bulldog underbite with fangs, steel back, silver sides. Not cute. Silhouette shows the fangs. |
| 29 | `xiphactinus_fossil` | APPROVED | Gillicus skeleton inside the ribcage at (0,0). Cleanup 2. |
| 30 | `gillicus` | APPROVED | Slim silvery prey fish with a deep head and forked tail. |
| 31 | `interior_seaway_map` | APPROVED | Matches the `world_map` palette and frame. The seaway runs N-S, Kansas at (+20,0) is in the seaway, and the white corner is deliberate Greenland ice. |
| 32 | `tylosaurus` | APPROVED | Pointed snout, teeth, four paddles, downturned fluke, angry eye. Silhouette OK. |
| 33 | `tylosaurus_fossil` | APPROVED | Plesiosaur skeleton (contrasting tan) inside the ribcage at (0,0). |
| 34 | `tylosaurus_mouth` | APPROVED | Symmetric. Throat at (0,-180), and the s230 arrow lands on it. Pterygoid rows read. Cartoon reds, no gore. |
| 35 | `plesiosaur` | APPROVED | Long neck, small head, four flippers, olive-teal. |
| 36 | `basilosaurus` | APPROVED | Very long eel-whale, cheek teeth. Tiny hind legs at (-226..-168, +50..+99) stay visible in the silhouette. Mid-tone on navy. |
| 37 | `basilosaurus_leg` | APPROVED | Knee/ankle/toes clear. Cleanup 2 and 4, director note 5. |
| 38 | `dorudon` | APPROVED | Small toothy early whale with an angry eye. |
| 39 | `livyatan` | APPROVED | Boxy brown head with big interlocking teeth in both jaws. Clearly different from `sperm_whale` (grey, scars, peg teeth). Mid-tone on navy. |
| 40 | `livyatan_tooth` | APPROVED | Banana curve, cream enamel, darker root. Cleanup 2. |
| 41 | `ruler` | APPROVED | Yellow, 0-30 cm, legible ticks. |
| 42 | `megalodon_tooth` | APPROVED | Serrated, dark grey-blue enamel, tan root band. Reads on near-black navy and when rotated. |
| 43 | `megalodon` | APPROVED | Longer and slimmer than `great_white_shark`, with bigger red-mouth teeth and a tall dorsal. Boss-worthy and mid-tone on navy. |
| 44 | `hand_outline` | APPROVED | Traced hand, fingers up, white inside, so it reads on dark too. |
| 45 | `time_machine_closed` | APPROVED | Identical footprint, roof at y -640 and TIME sign as `time_machine`, with the door shut. The tooth at (+63,-326) and the cap on the roof both land correctly. |

## Rejected assets
- `helicoprion`

# Keyframes round 1

Reviewer: art director, 2026-10-08. Scope: all 337 shots on `build/contact/sheet_01..29.png`, full-res `build/keyframes/` for s126 and
s140, and element positions in `shotlist.json` for every shot flagged below. s001 is the thumbnail placeholder (pending, expected).

## Verdict: FAIL (round 1). 12 fixes for the director, touching 24 shots. The rest is strong.

**What works:** the style is consistent across all 12 items. The two tiers hold everywhere (crude Doug, scientists and the child against
detailed, shaded creatures and props). Doug is on-model in every shot: round head, crescent, oval eyes, red cap, snorkel and fins
moving with him, and the ink flips to white on the dark interior (s209) and navy (s256). The era ramp darkens one step per item, from
Cambrian `#7cc6e6` to Miocene `#0a1630`, and lands on near-black navy at the boss. Every item opens on a glowing silhouette and a red
title card. Annotations appear in every item. The night clock reads at a glance (moon, then sun on survival, then pink when frozen on death).
Death beats are cartoon only (X eyes, ghost, splash, floating cap), with no gore. The mouth interiors in s228-s234 are cartoon reds.
Most items vary layouts well: maps, monitors, TV, museum frames, sunset surface beats, the menu chalkboard, ladders and bar charts.

**Asset `helicoprion` (round 2, re-drawn in 18c6135): APPROVED.** The whorl now sits on top of the lower jaw and reads as a toothed saw
(s116, s124-s127, s132; checked full-res on s126). The head is flattened, the snout is pointed with a jaw notch in the s109 silhouette,
and the small eye and heavy brow match `xiphactinus`/`pliosaurus`. That lifts the round-1 asset rejection: all 45 assets are now approved.

## Blocking fixes (director)

1. **s330: no cap on a death beat** (style bible 7.2, art bible "never a death beat with no cap"). The frame is all black apart from the HUD.
   Add `doug_cap` at about (960, 600), scale 0.6, `rotate` 20, so the cap tumbles in the dark. Red on black reads at phone size.
2. **s334: wordart on green grass** (art bible: lime on green disappears). Move THE WHOLE NIGHT into the sky left of the booth, at (380, 640),
   size 60. That keeps it clear of the sun and of the booth's left edge (about x 720).
3. **s191: SHALLOW SEA crosses the map frame and the green land.** Move it into the right margin at (1590, 900), size 60. That keeps it below Doug's feet (about y 630)
   and right edge at 1856 or less.
4. **Labels sitting on a map's bottom frame line** (008 precedent, s155): s166 (ABOUT 155 MILLION YEARS AGO), s189 (ABOUT 85 MILLION YEARS AGO),
   s219 (SAME SEA), s271 (ABOUT 10 MILLION YEARS AGO). Move each one off the frame into the top-left slot used by s032/s140, at about (480, 170),
   size 40-42.
5. **More than 2 keyword labels on screen** (7.4). Merge or drop as follows:
   - **s076**: drop IN WATER (the sea scorpion is already established in water). Keep ON LAND and VERY CLOSE.
   - **s096**: merge STRONG and FAST into one label, "STRONG + FAST", at (900, 330). Keep BOTH.
   - **s110**: merge 1899 and RUSSIA into "RUSSIA, 1899" (the s140 style). Keep ABOUT 280 MILLION YEARS AGO.
   - **s124**: merge 2013 and IDAHO MUSEUM into "IDAHO MUSEUM, 2013" at the old 2013 slot. Keep X-RAY SCANS.
   - **s161**: drop the 1999 box and make the label "LIOPLEURODON, 1999". Keep MONSTER.
   - **s236**: merge NO ARMOR and NO FINS into "NO ARMOR, NO FINS" at (800, 1000). Keep RED HAT and its arrow.
   - **s243**: drop ABOUT 37 MILLION YEARS AGO. It isn't spoken here (the narration is "It is not a lizard,") and s249 carries the date.
   - **s140**: the SKULL, BACKBONE and FLIPPER labels float over bare dirt with no bones drawn (checked full-res). Delete all three. Add
     `cymbospondylus_skull` on the ground between the scientists at (960, 840), scale 0.35, with one label, "SKULL, SPINE, FLIPPER", at (960, 960), size 40.
   - Accepted as furniture (not keyword labels): s002 (CAMBRIAN is the booth's destination sign), measurements in s115/s163/s195/s274,
     the anatomy callouts in s253 (the 007 s243 precedent) and the s336 option list in the outro question.
6. **s035: CHAMBERS appears twice** (boxed label plus wordart). Drop the wordart. Keep the label and its arrow onto the chamber line.
7. **s059: the poster inset enters the counter's column.** The rect runs x 560-1360 from y 160, but the art bible says insets start at y 250 or below, or end at x 1280 or less.
   Set the rect to x 580, w 700 (so it ends at 1280) and move the jaekelopterus, SEA SCORPION! and NOW SHOWING to x 930.
8. **s187: TWO-METER HEAD crosses the pliosaur's front flippers** at y 980. Move it into the clear water at the right, (1450, 450), size 70.
9. **s108: MORE DANGEROUS runs into the Dunkleosteus tail** (about x 1110-1145). Move it to x 660, or keep x 760 at size 76.
10. **s272: UPPER sits about 10 px under the night clock.** Move it to (1450, 370) and re-aim its arrow at the upper teeth.
11. **Endoceras fossil run, s040-s050: same composition 10 times in 11 shots** (horizontal cone mid-frame, Doug at the right, cream). s045-s050
    is 6 in a row, and our limit is 4. Re-stage two of them:
    - **s046 (ESTIMATE)**: a close-up. Put the cone at about 2x, cropped so the dashed tip fills the left half. Tiny Doug stands *on* the shell,
      pointing back at the dashed part. Keep the ESTIMATED label and arrow.
    - **s048 (2025 STUDY)**: use the computer-model layout from s017/s089. Copy the monitor rects from s017 and show the cone on screen with the dashed tip, the
      scientist at the left, and 2025 STUDY plus GENEROUS. Drop the warning triangle (one annotation is enough).
12. **Pliosaur skull run, s172-s176: 5 in a row** of the skull centred on cream with Doug at the right (s167-s169 are the same layout too). Re-stage:
    - **s173 (WEAKNESS)**: put the skull back on the monitor (copy the s170/s171 rects) ("the model found one weakness"), with the warning triangle
      beside the screen.
    - **s176 (BIT HARDER)**: show the live `pliosaurus` in Mesozoic teal `#24797c`, jaws clamped on an `ammonite`, Doug watching small at the right,
      with BIT HARDER below in clear water. No gore. A clamp, not a bite-through.

## Non-blocking advisories
- **A1 (night clock spacing).** Short readings ("10 s", "3 s", "22 min") stay centred at x 1600 while the moon stays at x 1338. That leaves
  a gap of about 100 px (s262-s264, s289-s293, s328-s337 most visibly). If you touch these shots anyway, put the moon at the label's left edge minus 34.
  The format changes (h/min, then min, then s, then SUNRISE, then pink when frozen) follow the brief's downward trend and are intended.
- **A2 (wordart on dark water).** The `#1a1a1a` outline vanishes on navy and teal, so wordart looks flatter there than on cream. Lime on navy
  still reads at phone size. Accepted.
- **A3 (late reveals, accepted).** Helicoprion (s109 to s116), Pliosaurus (s157 to s165), Livyatan (s267 to s272) and Megalodon (s294 to s301)
  show the full body more than 3 beats after the silhouette. Each of these items is *about* the body being unknown or disputed, so the
  in-between shots carry partial evidence (whorl, TV, sperm whale, teeth).
- **A4.** s229-s232 are 4 mouth shots in a row. That is inside the limit, and the annotation changes each beat. Accepted.

## Style bible 7 checks (keyframe level)
- Rule 1 (two tiers): PASS. Rule 2 (cap always visible): **FAIL** at s330 (fix 1). Rule 3 (caption bar): PASS. Section cards (s004, s135, s240)
  and the cold open and outro carry no bar, as intended.
- Rule 4 (labels, max 2): **FAIL** at s076, s096, s110, s124, s140, s161, s236 and s243 (fix 5). The duplicate in s035 is fix 6.
- Rule 5 (annotations): PASS, every item has several. Rule 6 (value ramp): PASS. The era ramp darkens monotonically, and night
  (`#2e5f8a`, s053-s055) and sunset surface beats are lighting devices. Rule 7 (silhouette then reveal): PASS, with the A3 exceptions.
  Rule 8 (no gore): PASS. Rule 9 (photos): not used.

Routing: all 12 fixes go to the **director**. No asset work is needed (`cymbospondylus_skull`, `ammonite` and `pliosaurus` exist, and the monitor is plain rects).
Re-render only the touched shots:
`--shots s035,s046,s048,s059,s076,s096,s108,s110,s124,s140,s161,s166,s173,s176,s187,s189,s191,s219,s236,s243,s271,s272,s330,s334`
and send me the new sheets for round 2.

KEYFRAMES: FAIL (round 1)
