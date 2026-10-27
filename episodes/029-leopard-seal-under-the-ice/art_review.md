# 029-leopard-seal-under-the-ice: art review (assets)

## Round 2: APPROVED (art director, 2026-10-27)

## Verdict: PASS. All 37 assets are APPROVED and art is signed off for the assets.

I re-reviewed the six round-2 redraws from `assets/previews/029-leopard-seal-under-the-ice-assets-fixes.png`,
`-seal-mouths.png` and `-jaw-diagram-s161.png`. I also rendered the real keyframes that use them: s021, s079, s080, s105,
s155, s161-s164, s169 and s172-s174.

| Fix | Asset | Round 2 |
|---|---|---|
| 1 | `leopard_seal_gape` | APPROVED. Both jaws are outlined with rounded tips, and the concave mouth edge sits behind them, so the head no longer reads as sliced. In s105 at 1.3 it reads as menacing, not gory |
| 1 | `leopard_seal_open` | APPROVED. Same fix, and it matches `_gape` and the hero design. The small nub teeth stay non-graphic for s135 |
| 2 | `leopard_seal_jaw_diagram` | APPROVED. The back of the skull is closed and rounded, with no cut edge. The canines are clearly the longest teeth (about 1.6x the cheek teeth). The interlock zone is clear, and the s163 ring and s169 arrows still land on the sieve |
| 3 | `leopard_seal_canine` | APPROVED. It is slim and sabre-curved with a plain tan root, so it reads as a fang at 1.4 in s174 |
| 4 | `boat_fender_bitten` | APPROVED. Two diagonal crescent punctures with jagged rims, and no face read at 0.6 (s079) or 1.6 (s080). No red |
| 5 | `explorer_1916_rifle` | APPROVED. Carried across the chest at about 70 degrees with the muzzle above the back shoulder, so it is not aimed. No flash (s021) |

### Shotlist check against the moved canines (canines now at local x +270..+384, tips y -58 / +100)
- **s174**: no change needed. It uses the standalone `leopard_seal_canine` (600, 540, 1.4) plus `leopard_seal`, and does not
  use the jaw diagram, so it has no coordinates tied to the canine position. The FANGS wordart sits clear above the tooth.
- **s162**: I fixed this myself in `shotlist.json`. The dashed leader line from the interlock (978, 544) to the zoom
  circle ran straight through both canines, and the SHARP POINTS wordart (1500, 620) overlapped the upper canine tip and
  the chin. Changes:
  - The line now runs (978, 544) -> (1090, 420) -> (1380, 420), above the lower canine tip.
  - The wordart moved to (1560, 660). Its right edge is about 1800, which is inside the safe area.
  - `validate shotlist` passes and the re-rendered keyframe is clean.
- s155, s161, s163, s164, s169, s172 and s173: no overlays touch the canines, so no change.

### Minor, no action required
- The diagram's upper-canine gum reads a little like a pink cap at 1.1. This is acceptable for a textbook diagram, and the
  illustrator can soften it if there is time.
- The director's note on s064 (`thumbs_up` inside `penguin_costume`) from round 1 still stands.

## Next
The assets are signed off. Keyframe review happens at `art_approved` after the director renders the full contact sheets.

---

## Round 1 (superseded by round 2 above)

Art director, 2026-10-27. Reviewed the 37 new assets in `asset_requests.md` from the three preview sheets
(`assets/previews/029-leopard-seal-under-the-ice-assets-{seal,2,3}.png`). I also rendered three test scenes: the seal family on
ice `#dff4ff` and surface water `#3a9ad9` next to Doug at shot scale, the worn props on Doug (stand / thumbs_up), and
`leopard_seal_jaw_diagram` at its s161 placement (860, 520, 1.1).

## Verdict: FAIL (round 1). 32 APPROVED, 5 need fixes (all to the illustrator)

### Leopard seal design: SIGNED OFF (brief section 7)
The core design is approved and locked for the family. It has a long, slim, snake-like body, a slate `#5f6670` back fading to a
silver `#c9ced4` belly and dark irregular spots that are densest on the throat and shoulders. The head is long, flat and reptilian.
It has a small dark eye under a heavy brow, a grin line that runs back past the eye and no ear flaps. It reads as menacing, never
cute, and nothing about it looks like a kids' mascot. `leopard_seal`, `leopard_seal_hauled_out` and `leopard_seal_head_rising`
are clearly the same animal at every scale I tested (0.7 to 1.1). The fixes below cover only the open-mouth variants and the two
diagram pieces. They do not change the head, palette or spots.

## Per asset

| # | Asset | Verdict |
|---|---|---|
| 1 | `leopard_seal` | APPROVED (hero design, see above) |
| 2 | `leopard_seal_head_rising` | APPROVED. The ripple ring reads as emerging, not as a cut neck |
| 3 | `leopard_seal_hauled_out` | APPROVED |
| 4 | `leopard_seal_gape` | **FIX 1** |
| 5 | `leopard_seal_open` | **FIX 1** |
| 6 | `leopard_seal_jaw_diagram` | **FIX 2** |
| 7 | `leopard_seal_canine` | **FIX 3** |
| 8 | `boat_fender_bitten` | **FIX 4** |
| 9 | `explorer_1916_rifle` | **FIX 5** |
| 10 | `adelie_penguin` | APPROVED. The white eye ring is the real field mark, not a cute eye. A row at 0.34 reads |
| 11 | `adelie_penguin_swimming` | APPROVED. Alive and darting. The pink trailing feet read as feet, not as injury |
| 12 | `fur_seal_pup` | APPROVED |
| 13 | `crabeater_seal` | APPROVED. Pale scar stripes, never red |
| 14 | `krill_cloud` | APPROVED |
| 15 | `zodiac_boat` | APPROVED |
| 16 | `zodiac_boat_wrapped` | APPROVED. Reads as armoured |
| 17 | `zodiac_boat_wrecked` | APPROVED |
| 18 | `inflatable_dinghy` | APPROVED |
| 19 | `inflatable_dinghy_swamped` | APPROVED |
| 20 | `music_note` | APPROVED. Reads at 0.3 on blue |
| 21 | `photographer_diver` | APPROVED (`auto_ink`, no cap, camera clear of the head) |
| 22 | `quad_bike_rider` | APPROVED (`auto_ink`, generic, not a likeness) |
| 23 | `explorer_1916` | APPROVED (`auto_ink`, no cap) |
| 24 | `explorer_1916_skis` | APPROVED |
| 25 | `doug_skis` | APPROVED (checked under Doug, thumbs_up) |
| 26 | `penguin_costume` | APPROVED. Head, face and cap fully visible (see the director note) |
| 27 | `penguin_costume_flat` | APPROVED |
| 28 | `marina_pontoon` | APPROVED |
| 29 | `canvas_tent` | APPROVED |
| 30 | `new_zealand_map` | APPROVED |
| 31 | `bowling_lane` | APPROVED |
| 32 | `blubber_stove_pot` | APPROVED. No meat visible |
| 33 | `cinema_seat` | APPROVED |
| 34 | `endurance_wreck` | APPROVED |
| 35 | `selfie_stick_phone` | APPROVED |
| 36 | `pasta_strainer` | APPROVED |
| 37 | `vacuum_cleaner` | APPROVED |

## Required fixes (illustrator)

1. **`leopard_seal_gape` and `leopard_seal_open`: the mouth front edge.** The `#7a0d0d` mouth fill runs straight out to a flat,
   unoutlined edge between the jaw tips. The front of the head reads as sliced off, with a red block where the snout should be.
   On `_gape` the upper jaw tip has no closing outline either. This matters most in s178, where `_open` sits at scale 1.4 with no
   Doug, and in s105, where `_gape` is at 1.3. Fix it like this:
   - Close both jaws with their own black lip outlines, with the upper and lower jaw tips each finished as a rounded snout or chin.
   - Pull the mouth interior back from the tips, so its front boundary is a concave curve with a black line that sits behind the
     line between the tips. The background shows through the gap at the very front.
   - Keep `#7a0d0d`, the pink tongue on `_gape` and the existing tooth count.
   - On `_open` the teeth may stay as they are. The request asked for "a few nubs", so you may trim them to 3-4 per jaw, but this
     is optional.
   - Keep the same bboxes, anchors and mouth centres: `_gape` mouth at (+260, -280), `_open` gap at x +300..+410, y -45..+45.
2. **`leopard_seal_jaw_diagram`: the flat cut edge and the canines.**
   - The back of the head ends in a straight vertical edge with a dashed grey line. At the shotlist placements (860, 520, 1.1 in
     s161-s169, and 0.7 in s155/s172/s173) that edge lands mid-frame at about x 365. It reads as a severed head. This breaks the
     art bible's open-jaw cut-edge rule (from 027). Replace it with a closed, rounded back of the skull or neck outline, so the
     head ends in a curve with no flat edge. Keep the width at about 900.
   - The two canines at about (+310..+378) are no taller than the cheek teeth, so s174 (the canine card) has nothing to point
     back to. Make the upper and lower canines clearly the longest teeth: about 1.6x the cheek-tooth height, curved and pointed.
   - Leave the interlock zone at (+80, +40) clear of other detail, exactly as it is now.
3. **`leopard_seal_canine`: shape.** It is straight, symmetrical and banded, so at 1.4-1.6 it reads as an ice-cream cone or a
   corn kernel, not a fang. Redraw it as a long, slim, **curved** tooth:
   - The crown curves back like a sabre, with the tip at y -150 bent toward one side.
   - Shade `#f4ecd8` with grey on the inside curve.
   - Give the root half a duller tan with no horizontal bands, so nothing looks like a waffle cone. A single faint line at the
     gum line is fine.
   - Keep it about 110 x 300 with a centre anchor.
4. **`boat_fender_bitten`: the holes read as a face.** The two dark chevrons stacked on the white band look like a pair of
   frowning eyebrows, so the fender reads as a face at 0.6 (s079) and at 1.6 (s080). Draw them as clear punctures instead:
   - Two small dark-filled crescent or oval holes **side by side on a slight diagonal**, the spacing of a bite. Do not stack them
     vertically.
   - Give each one a jagged pale rim and a short wrinkle or dent line, so the vinyl reads as punctured and soft.
   - No red.
5. **`explorer_1916_rifle`: the rifle angle.** The rifle is held out in front of the face at about 40 degrees, so it reads as
   aimed forward and up. The brief's policy note asks for it carried *across the chest, muzzle up*. Rotate it to about 70
   degrees, with the butt at the front hip and the muzzle beside the back shoulder, above head height. Keep both hands on it and
   no flash.

## Director notes (no change needed for asset sign-off)
- s064 uses `thumbs_up` with `penguin_costume`. The costume hides the arm, so only a lone thumb pops out next to the hood, which
  reads as odd. Prefer `stand` (or `wave` if the gesture matters) for that shot, or accept the floating thumb knowingly.
- `leopard_seal_jaw_diagram`: keep wordart and the red ring off the canines once fix 2 lands, because s174 calls back to them.

## Next
The illustrator redraws items 4-8 (fixes 1-5), re-runs `python -m studio asset-preview` for those five, and pings me for round 2.
The 32 approved assets need no further review. `_gape` is bottom-anchored and about 390 tall, so the default preview cell
crops its head. Preview it at `--scale 0.6` or on a scene canvas.

---

# Keyframes + thumbnails, round 1 (art director, 2026-10-27)

## Verdict: FAIL. Style, palette and Doug are consistent; layout variety and the thumbnails' water colour are not.

I reviewed all 23 contact sheets (264 shots plus the endslate), checked the suspect shots at full frame, and looked at
the three thumbnails at full size and at feed size.

**Passes:**
- The two-tier look holds in every shot.
- Doug's red cap is visible in every Doug shot, including the ghosts and the costume deaths (s067, s210). The cap stays in frame on
  every death beat (s031, s124, s179/s180, s210, s257-s263).
- Sea and sub-ice water are `#3a9ad9` everywhere in the body of the video.
- Item title cards are red. The Snorkeller uses the white sober title, following the 027 Legend precedent.
- Death counter values are correct: 234 to 240.
- There is no gore. The open mouths use `#7a0d0d`, and no penguin is shown being caught.

## Fixed myself (shotlist re-rendered, `validate shotlist` OK)
1. **s002**: the red speckle glow on the cream 1916 floe read as blood spatter next to the skier. I changed it to the dull purple
   `#5e4670`, per the art bible's rule for tan and brown grounds.
2. **s099, s182**: the red silhouette rim also traced the asset's water drips and ripple rings. That produced red "drips" hanging
   from the jaw and red rings in the water, which read as blood. I added an engine flag `"silhouette_keep": true`
   (`studio/paint.py`, `_silhouette`): when it is set, an element keeps its own colour inside a silhouette and is skipped by the
   rim pass. I tagged the drips and ripples in `leopard_seal_head_rising.json` with it. This is metadata only, and the asset's normal
   look is unchanged. The rim now hugs only the head.
3. **s071**: the THE VISITOR title sat on the skyline. Its glyphs crossed the building tops (skylines count as land, per the 027
   treeline rule). I moved it to (880, 235) at size 120. It is now clear of the buildings and its right edge stays under x 1280,
   outside the counter zone.
4. **s074, s077, s078, s083**: Doug stood on the pier post at x 500, so the post's outlines ran through his torso. I moved him to x 590,
   on clear deck in front of the second hull.
5. **s094-s096**: in "waist deep", the `stand` arms under the head read as two short legs, so it looked like a head on legs. I
   changed the pose to `hands_hips` so the elbows read as arms at the waterline.
6. **s101, s102**: the photo board's top-right corner (1360, 180) butted against the counter box. I shifted the whole board, with
   the photo, pin, GRIN wordart and WARNING SIGN note, 80 px left, so the right edge is at 1280.
7. **s105**: the ENORMOUS GAPE wordart reached x 1320 at y 185-250, inside the counter zone. I moved it to (880, 300).
8. **s252-s256**: upside-down Doug at 0.5 with `mask` had his eyes covered by the mask and the cap covering half his head, so he
   read as a red-and-white ball or bobber. I removed `mask` (no other under-ice Doug wears one) and raised the scale to 0.6 (group
   y 290). His eyes now read, and the cap hanging below matches the 017 upside-down convention.

Note for whoever re-renders: `keyframes --shots` rewrites `build/contact` with only the listed shots. I rebuilt the full 23-sheet
set from the existing keyframes afterwards.

## Required fixes: director (layout variety, no more than 4 shots in a row with the same composition, per the 028 rule)
1. **s010-s022 (13 shots)**: the 1916 framed panel is on the left with Doug on the right. Only the panel's contents change. Turn
   2-3 of these into full-frame sepia shots that keep the "1916" tag:
   - s017 "tracked his shadow": a full-width under-ice view of the seal looking up at the shadow.
   - s019/s020 floor/window: a full-frame split, with the skier on top and the seal below.
   - s012 ENORMOUS: a scale beat.
2. **s037-s041 (5)**: the same penguin-row edge shot five times. Make s040 or s041 a different view, either from below the ice
   edge or a close-up of the strip.
3. **s084-s091 (8)**: the NZ map is on the left with a prop on the right every time. Make s086 (public reports) and s088 (216 seals)
   full-frame (a phone or hotline card, and a lineup of seals), so the map shots are not consecutive.
4. **s109-s113 (5)**: Palmer Station is the same wide shot five times. Make s110 or s112 a close-up of a seal biting a pontoon.
5. **s129-s139 (11)**: diver, seal and Doug are in the same underwater layout. s134 already has an inset. Also break s131/s132
   (Paul Nicklen, 2006), for example with a magazine-cover card, and s135 with a close-up of the head over the camera.
6. **s148-s152 (5)**: Doug and the seal in the same mid-water frame. Make s152 ("and frankly, so are we") a different shot.
7. **s199-s210 (12)**: the pack-ice crabeater scene is the backdrop for all twelve shots. Break it twice: s203 (escaped when young)
   as a framed flashback, and s204/s205 as a stat or close-up card.
8. **s212-s224 (13 sober cards)**: keep them sober, with no Doug, no counter and no joke, but vary 2-3 of them using the 027
   sober-card palette. For example, a muted map of the Antarctic Peninsula with a Rothera marker (`#2a3440` sea, `#4a5a48` land) for
   s215, and a closed dive-log book with the four tally marks for s220/s221. The text position also jumps between centre (s214-s216)
   and top (s217-s219). Pick one.
9. **s249-s256 (8)**: the same under-ice frame. Break s253 or s254 with a close-up of the singing seal or a rival-male card for
   "to a rival male".

## Required fixes: graphic designer (thumbnails)
10. **All three variants use navy water** (`#0b2a55`): under the sea ice in A and in C's Song tile, and at the surface in B. This
    breaks the art-bible rule that water under sea ice, and at any surface scene, is `#3a9ad9`, never a deeper ramp colour for
    "cold". It matters most for **A**, because A is also s001: the video opens on navy and then cuts to `#3a9ad9` at s003. Use
    `#3a9ad9` with `#6fc1ee` speckle. The seal's grey and the black-outlined white text still read on it.
11. **B (CORNERED)**: Doug is about 45% of the frame height and co-stars with the seal. Style bible 7.10 allows Doug only as a
    small scale figure. Shrink him to about half that size, or keep B only as a logged deliberate test.
12. **C (2x2 tiles)**: this is off-spec for Archetype A, which needs 6-12 tiles with the bold label *under* each tile. If C goes to
    A/B testing as a deliberate 4-tile control, log that in `decisions.md`. Otherwise use 6-8 chapter tiles with labels underneath
    (skip The Snorkeller).
- Otherwise the thumbnails are fine. All three read at feed size, the text is not in the title, and there is no gore. The seal's
  mouth is closed in A and B, and C's Head tile uses the approved gape.

## Next
The director breaks runs 1-9 and re-renders. The graphic designer fixes 10-12 and re-renders s001 together with `thumbnail`. I
re-check only the changed shots in round 2.

---

# Keyframes + thumbnails, round 2 (art director, 2026-10-27)

## Verdict: PASS

I re-rendered the full keyframe set from the current `shotlist.json` (265 frames, 23 sheets) and reviewed all of it. Some round-1
keyframes on disk were stale (18:16). I also checked the three thumbnails at full size and the suspect shots at full frame.

### Round-1 director fixes (layout variety): all done
1. **s010-s022**: s012 (ENORMOUS scale beat) and s015-s020 (shadow and floor/window, under-ice cross-section) are now full-frame
   sepia with the 1916 tag. The longest framed run is now 2 shots. s022 shows Wild, the BANG and the seal, with no wound.
2. **s037-s041**: s041 is a below-the-edge cross-section with penguins diving through the red strip.
3. **s084-s091**: s086 (three phones with SEAL! bubbles) and s088 (216-seal lineup) break the map run.
4. **s109-s113**: s110 is a close-up of a seal biting the zodiac pontoon.
5. **s129-s139**: s131/s132 use the magazine-cover card, and s135 and s138 are push-ins.
6. **s148-s152**: s152 is a close-up of Doug with the seal cropping in.
7. **s199-s210**: s203 is a framed YEARS EARLIER flashback, and s204/s205 are stat cards on cream.
8. **s212-s224**: s215 is the muted Peninsula map (`#2a3440` / `#4a5a48`) with the Rothera marker, and s220/s221 show the dive-log
   book with four tallies. The text sits at y 440 on every card. s224 is the new REPUTATION card.
9. **s249-s256**: s253 is a close-up of the singing seal.
- The recommended items also landed: KRILL sign on s179, MAYBE struck through on s258, grey-tan beach on s182-s188 (the pups read),
  and no red ripple rings on s099/s182.

### Round-1 graphic-designer fixes: all done
10. A and B use `#3a9ad9` water with `#6fc1ee` speckle. In A the seal now sits clearly under the floe, below Doug's shadow, and s001
    matches.
11. In B, Doug is about a quarter of the frame height, a small scale figure.
12. C is a 3x2 grid of 6 tiles with labels under them (Archetype A spec), and The Snorkeller is not used.

### Fixed myself this round (`validate shotlist` OK, full set and thumbnails re-rendered)
1. **s110**: the zoom group sat at x -1940 at 2x, which left a 20 px white strip down the right edge of the frame. I moved it to
   x -1920.
2. **s115**: the GUIDELINES wordart touched the checklist card's right border. I moved it to (1580, 430), clear of the card and the
   counter.
3. **s016**: the EXPEDITION ACCOUNTS book's top-right corner was 20 px under the counter box, inside the counter zone. I moved it to
   (1250, 300). The label is unchanged.
4. **Thumbnail C, Sieve tile**: the fill was `#1d6fb8`, a deeper blue than the art bible allows. I changed it to `#3a9ad9`, which
   matches s176-s180.

### Checked and fine
- Doug is on-model with his red cap in every Doug shot. The costume deaths (s067, s210) and the upside-down shots (s254-s256) keep
  the cap and eyes readable.
- Counter: 234 to 240. The Snorkeller block (s212-s224) has no Doug and no counter.
- There is no gore. Open mouths use `#7a0d0d`, and no penguin is ever shown caught.
- Zone colours: open and sub-ice water is `#3a9ad9`, and the 1916 cross-sections use the sepia `#7f9ea3`. The Visitor marina uses
  the regional harbour step `#2f7fbf` across the whole item (unchanged since round 1). This is consistent, and it is not a "cold"
  borrow.

### Non-blocking (illustrator, if time allows)
- The `leopard_seal_jaw_diagram` sieve head (s155, s161-s164, s169, s172-s173) is still the plain pale-grey diagram. Adding the
  spot pattern, darker dorsal shading and whisker dots (visual screener rec. 10) would tie it to the hero head better.
- The s064 floating thumb in `penguin_costume` stands, as accepted in round 1.

## Next
Art is approved. The visual screener's round 2 is also PASS, so the stage moves to `art_approved`.
