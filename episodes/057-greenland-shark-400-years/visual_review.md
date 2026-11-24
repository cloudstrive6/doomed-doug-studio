# Visual review: 057-greenland-shark-400-years

## Round 1 (pre-render, keyframes): 2026-11-24

Source: `build/contact/sheet_01..18.png` (fresh full render, s001 to s208 + endslate), spot-checked at full size in
`build/keyframes/`. s001 thumbnail placeholder ignored as instructed.

**VERDICT: FAIL**

Overall this is strong. Doug is on-model in every shot (red cap, white head) and readable on every background. The
deaths are all cartoon (cap floats up, ghost Doug, a silhouette sub, the ice tipping) with no gore. Stomach contents are
black silhouettes inside a cutaway, and the shark in the net is fine. Nothing reads as a kids' show. Most shots make
their subject obvious within 1 second, the HUD counter runs correctly from 414 to 420 with SHARK AGE tracking the
chapters, and the "FOUND INSIDE" list gag (s094-s096, then s110 PICNIC) and the TV ending (s205-s206) work well. It fails
on one blank-looking death frame, several cases of text colliding with drawings or lines, two garbled
"shark line-ups", one prop too small to read, and three runs of near-identical compositions.

### Required fixes

1. **s204 (director)**: The death keyframe is plain black with only the HUD showing. Under the death blackout, only
   elements with `appear` draw, and the only one here is the 420 label. The result reads as a dropped or black frame, and
   QC's black-frame check may flag it. This is the episode's last death, the payoff of the cake promise in s003. Add
   `appear` elements the way s021 and s183 do: the cap rising on a dashed line, plus the cake (or one lit candle)
   sinking toward a faint shark silhouette.
2. **s185, s187, s188 (director)**: The big wordart sits across the shark's back. "THE OLDEST" and "~392 YEARS" overlap
   the dorsal fins and the body outline (confirmed at full size on s187). Move the wordart up into clear water (y of
   about 150-180), or drop the shark to y of about 700 and scale it to about 0.9.
3. **s185-s188 (director, variety)**: There are 4 consecutive near-identical frames: the same giant side-view shark with
   the copepod eye and tiny Doug at lower left. Keep s186 (the 502 CM measure). Recompose s187 as a close-up on the eye
   with the copepod and "~392 YEARS" beside it, or as a pull-back. s188's "± 120" can then reuse the s187 layout.
4. **s061-s065 (director, variety)**: There are 5 consecutive frames with the same ice-hole and tape-measure layout and
   the same camera. Make s064 ("grew less than a centimeter") an underwater close-up of the shark's nose against the tape,
   with a tiny red tick showing under 1 cm. Keep s063 and s065 wide.
5. **s115-s120 (director, variety)**: There are 6 near-identical frames: grey meat slab centre-left, Doug right, beige
   background (the s117 chapter card is the same layout too). Recompose s116 ("The shark has a plan for that too") as
   the shark's face with a smug look and a warning sign. Recompose s119 as a big labelled close-up (UREA / TMAO tags on
   the slab, Doug off-frame or tiny). Keep s118 and s120.
6. **s192, s193 (director)**: The three largest sharks overlap nose-to-tail into a single merged blob (confirmed at full
   size), so this doesn't read as "sharks sorted by size". Space them out: shrink the large ones, or stagger them on two
   rows so no outlines touch. In s193 the red "BORN BEFORE" box then wraps cleanly separate shapes.
7. **s043 (director)**: The "WELCOME" text is drawn unrotated and spills off both sides of the tipped-over sign. Either
   rotate the text with the sign or make the sign wider so the word fits inside it.
8. **s053, s054 (director)**: The vertical divider line runs through the "4 CM A YEAR" label, over the R. Move the
   label left by about 80 px, or end the divider below the label. In s054 the "4X FASTER" wordart sits under the shark,
   so it reads as "the shark is 4x faster". Move it to the fingernail side (left), under the nail.
9. **s028 (illustrator, director)**: "37 CM" is shown over a ruler marked 0-30, and the pup spans only about 20 of those
   units. The scale contradicts the number. Either relabel the ruler ticks so the pup spans 0-37 (ruler to 40), or drop
   the numbers from the ruler.
10. **s137 (illustrator, director)**: The hákarl cube is a tiny toothpick cube tucked under Doug's cap brim. Nobody will
    see "one cube" at video size. Put a large cube (about 80 px) on a small plate on the counter, with the red arrow
    pointing at it, and Doug beside it with an uneasy look.
11. **s046 (director)**: The `calendar_page_flying` asset at (1100, 300), scale 0.45, sits right after "DECADES." at
    the size of a stray glyph. It reads as an artifact. Scale it to about 1.0 and move it to the open sky on the right
    (x of about 1500), or remove it.
12. **s030 (director)**: The "THE ONLY ONE" wordart runs into Doug's head. Move Doug to x of about 1750 or shift the
    wordart left.
13. **s027, s015 (director)**: "10 PUPS" sits on the shark's dorsal outline. Lift it about 40 px. In s015,
    "100+ YEARS" starts on top of the eyeball's pupil. Shift it right or down so it clears the eye diagram.
14. **s167 (illustrator)**: The `heart_monitor` asset reads as a microwave or oven panel, because its screen is blank.
    Draw a slow, flat heartbeat trace (one small blip) on the screen in green, so that "SLOW METABOLISM" reads in 1
    second.
15. **s131 (director)**: The "2014" tag covers the masthead, so it reads "THE DAILY N". The narration says "government
    release", not a newspaper. Swap the newspaper for the plain document asset used in s026/s029 with a "2014" tag (or
    an "ICELAND GOV." label), and keep the flag.

### Minor (fix if cheap)

- **s022, s090 (director)**: The ghost Doug wears his cap and a second loose cap floats right above him, so there are
  two caps in one frame. Drop the floating `doug_cap` from these post-death shots. The death shots themselves (s021,
  s089) can keep it.
- **s203 (director)**: "brought the edge of the ice down" shows only faint crack lines. Tilt the ice slab under Doug and
  the cake a little (as in s089) so the collapse reads before the cut to black.
- **s194 (director)**: The red arrow runs through the T of "THE LOW END". Start the arrow above the wordart.
- **s101 (illustrator)**: The whale-meat chunk reads as a rock or a dead seal. Add a small "WHALE MEAT" label.
- **s158 (director)**: The shark's tail is cropped at the right frame edge. Pull it in about 60 px unless the crop is
  meant as "entering".
- **s013 (director)**: The "WESTERN GREENLAND" label sits under the eyeball diagram, so it reads as a label for the
  eye. Move it next to the document or a map inset.
- **Contact caption, s124 (editor, advisory)**: The contact-sheet caption font shows "hákarl" as "h?karl" (missing
  glyph). The on-frame wordart HÁKARL renders correctly. Confirm the burned-in subtitle font has the á glyph before the
  final render.

### Checked and fine

The chapter cards (s005, s024, s047, s067, s093, s117, s142, s163, s185) are legible. There are no spelling errors on
screen ("TRIMETHYLAMINE OXIDE", "HÁKARL", "CONGRATU-/LATIONS" all correct). The maps are readable, with Svalbard and
Iceland circled. The squid-bait camera, the snail race, the seal napping vertically (s084) and the bomb-pulse curve
(s191) are recognisable. The 28-shark grid counts out correctly (7x4). The endslate's Subscribe circle and video box are
clear.

## Round 2 (pre-render, keyframes): 2026-11-24

Source: fresh `build/contact/sheet_01..18.png` and `build/keyframes/` (regenerated 18:06). I checked every shot changed
since round 1 (s003, s013, s015, s022, s027, s028, s030, s043, s046, s053, s054, s064, s090, s094-s096, s101, s110, s116,
s119, s120, s131, s137, s158, s167, s168, s185, s187, s188, s192-s194, s203, s204), plus their neighbours, for
regressions. The s001 thumbnail placeholder was ignored as instructed.

**VERDICT: PASS**

### Required fixes from round 1

1. s204: Fixed. The cap now rises on a dashed line and the lit cake sinks toward a faint shark outline on black, with the
   420 counter showing. It reads as a death, not a dropped frame.
2. s185, s187, s188: Fixed. "THE OLDEST", "~392 YEARS" and "± 120" now sit in clear water above the shark.
3. s185-s188 variety: Fixed. s185 and s186 are full side views. s187 and s188 are a head close-up with the copepod, and
   in s187 a red arrow points from the wordart to the eye.
4. s061-s065 variety: Fixed. s064 is an underwater nose close-up against a yellow tape, with a red under-1 cm tick.
5. s115-s120 variety: Fixed. s116 is the shark's face front-on with a warning sign and "A PLAN". s119 is a large slab
   with UREA and TRIMETHYLAMINE OXIDE callouts and Doug small. s120 is Doug holding tongs at a big warning sign.
6. s192, s193: Fixed. The five sharks are spaced out with no outlines touching, and the green and red boxes wrap
   separate shapes.
7. s043: Fixed. "WELCOME" now fits inside the tipped sign.
8. s053, s054: Fixed. The divider no longer crosses "4 CM A YEAR", and "4X FASTER" sits over the fingernail.
9. s028: Fixed. The new ruler runs 0-40 and the pup spans it, so the scale matches 37 CM.
10. s137: Fixed. A large cube sits on a plate on the counter, the red arrow points at it, and Doug stands beside it.
11. s046: Fixed. The calendar page is larger and in the open sky on the right, and no longer reads as an artifact.
12. s030: Fixed. "THE ONLY ONE" clears Doug.
13. s027, s015: Fixed. "10 PUPS" clears the dorsal fin (checked at full size), and "100+ YEARS" clears the eye diagram.
14. s167: Fixed. The monitor shows a green trace with a single blip and reads as a heart monitor.
15. s131: Fixed. It now uses the plain document with a "2014" tag, an "ICELAND GOV." label and the flag.

### Minor items from round 1

All are addressed. s022 and s090 have no floating second cap. s203's ice slab tilts under Doug and the cake. In s194
the arrow sits below "THE LOW END" pointing to 272. s101 has a "WHALE MEAT" label. s158's tail is inside the frame. In
s013 "WESTERN GREENLAND" now labels a map inset.

### New notes (advisory, not blocking)

- s110 (illustrator): The PICNIC row icon in the FOUND INSIDE list is a small black blob that reads as a bag. A tiny
  basket silhouette matching the basket at Doug's feet would land the gag better. Fix only if cheap.
- Carried over (editor): Confirm the burned-in subtitle font has the "á" glyph for "hákarl" before the final render.

No gore, Doug is on-model throughout, and the HUD counter progression is intact. The keyframes are cleared for the
final render. Post-render checks (samples, qc.json, thumbnails A/B/C, Shorts) are still to come.

## Round 3 (thumbnails + final fixes): 2026-11-24

Viewed: `build/thumbnail.png`, `thumbnail_b.png`, `thumbnail_c.png` (1280x720) and their `_small` versions (168x94), plus
keyframes s001, s137 and s098. Titles checked against `metadata.json` packaging candidates 1-3.

**VERDICT: FAIL** (thumbnail B needs a real fix. The rest are small, quick fixes.)

### Keyframes

- s137: Fixed. The cube sits on a plate on the countertop, the red arrow points at it, and Doug stands beside it,
  pointing and sad. It reads in 1 second. One advisory note: the Iceland flag pole has no base and floats on the wall.
- s001: Same art as thumbnail A, so the same notes apply (see fix 3).
- s098: Mostly fine, with one mismatch (fix 4). Doug, the shark, the HUD counter (417) and "HUNDREDS OF METERS" all
  read. The narration says "near-freezing water", but the thermometer shows its stock red fill at about 60% with no
  label, so it reads as warm or normal. s059 ("-2 °C") and s165 ("CLOSE TO FREEZING") label the same drawing. s098
  doesn't.

### Thumbnails

- **A (392 ± 120 YRS, title "Why the Greenland Shark Is the Creepiest Fish Alive")**: Strong. The text is the clear
  focal point and stays legible at 168x94. The dorsal fin coming up through the ice hole says "shark", and the copepod
  streamer on the eye is visible at small size. It's accurate (estimate with its range), has no gore or attack, and
  isn't misleading. Doug and the cake are small at feed size, with the cake a white blob next to the red cap. That's
  acceptable because the number carries it. The candle tips are cut off by the top edge (fix 3).
- **B (HI FRIEND?, title "...Creepiest Eye Parasite Alive")**: Fails on what the title promises. The shark's nostril
  near the snout (about x=1010, y=420) is a dark oval with a brow stroke over it, so it reads as the shark's eye. The
  real eye ring (about x=560, y=325) sits mid-body and the copepod's head covers it. At 168x94 the copepod looks like
  a pale figure stuck on the shark's flank, not a parasite on its eye. The text, Doug (red cap, torch) and policy are
  fine. The copepod's raised arm stays clear of the eye, so there's no eye damage.
- **C (CONGRATULATIONS?, title "...Creepiest Teenager in the Ocean")**: The text reads at feed size, and the shark and
  Doug read clearly. Doug isn't holding the card: it floats about 80 px above his raised hands, and the candle stuck on
  top of the card is odd. At 168x94 the card reads as an open book. The pink background with arms-up Doug is the
  closest of the three to a party look, but the unimpressed shark keeps it adult and deadpan. Acceptable.

All three are original, use the channel's MS Paint style, and have no gore, no realistic violence and no
kids-show framing. None of them is misleading against its title.

### Required fixes

1. **Thumbnail B (graphic designer)**: Make the eye obvious and put the parasite on it. Remove the brow stroke over the
   nostril and shrink it to a thin dark slit, low on the snout tip. Move the eye ring and the copepod forward, toward the
   head (eye about 180-250 px behind the snout, about x=800-850). Make the ring slightly bigger with a visible dark
   pupil, and attach the copepod's head to the ring's lower edge so the pupil still shows. Re-check `_small`: you should
   see "eye, with a white thing hanging off it".
2. **Thumbnail C (graphic designer)**: Put the card in Doug's hands. Lower it so its bottom edge sits on both raised
   hands (about y=480-500), or raise his hands to meet it. Either drop the floating candle or stand it on a cake held in
   one hand. If you keep it, add a big "150" on the card face so it reads as a birthday or coming-of-age card at feed
   size instead of a book.
3. **Thumbnail A / s001 (graphic designer)**: The candle flames on the cake's top tier are cut off by the top edge (62
   non-background pixels in row 0 at 1920 px). Move the Doug + cake group down about 30 px, or scale it to 0.95, so the
   tallest flame clears the edge by at least 10 px. Both the thumbnail and the s001 keyframe use this art.
4. **s098 (director)**: Label the cold. Add a white bold label "NEAR 0 °C" (size about 40, appear 0.55) under the
   thermometer at about x=1600, y=780. This matches s059 and s165. Optionally, add a white rect over the upper part of
   the red column so the fill sits at the bulb.

### Advisory (not blocking)

- s137 (illustrator): Give the flag pole a small wall bracket or a base on the counter.
- Packaging (graphic designer): A is the strongest of the three at feed size. Keep it as the primary.

## Round 4 (rebuilt thumbnails + s001/s098): 2026-11-24

Viewed: `build/thumbnail.png` (A, HI FRIEND?), `thumbnail_b.png` (B, 392 ± 120 YRS), `thumbnail_c.png`
(C, CONGRATULATIONS? ~150), all three `_small` versions (168x94), and keyframes s001 and s098. Pairings checked against
`metadata.json` packaging candidates 1-3 (A = "...Has the Creepiest Eye Parasite Alive", B = "Why the Greenland Shark
Is the Creepiest Fish Alive", C = "...Creepiest Teenager in the Ocean").

**VERDICT: PASS**

### Round 3 fixes re-checked

1. **Eye parasite thumbnail (Round 3 fix 1, now A)**: Fixed. The thumbnail was rebuilt as a close-up of the snout with
   one large eye ring and a dark pupil about 200 px behind the snout. The copepod's head attaches to the lower edge of
   the ring with the pupil still visible, its arm is raised in a wave, and its two egg-sac streamers hang down. The
   nostril no longer reads as an eye. At 168x94 it reads as "eye, with a white thing hanging off it". Doug (red cap, torch
   beam lighting the eye) is right of the snout and reads at feed size. There's no eye damage, bite or attack. HI
   FRIEND? is legible and is the clear focal point together with the eye.
2. **C card (Round 3 fix 2)**: Fixed. Doug's hands now hold the card at its top corners, the floating candle is gone,
   and the card face shows a large "~150" that's legible at 168x94. The shark (with its lidded, unimpressed eye) and the
   text both read.
3. **Candle flames cut off (Round 3 fix 3, now B)**: Fixed. The new B art (head-on shark under the ice, Doug on the
   ice holding the candle-covered cake) has no art in row 0. The tallest flame tip is at about y=18 at 1280 px, with
   only faint glow specks at y=8. "392 / ± 120 / YRS" is the clear focal point at feed size, the copepod streamer on the
   shark's left eye is visible, and it's accurate (estimate with its range).
4. **s098 (Round 3 fix 4)**: Fixed. "NEAR 0 °C" now sits under the thermometer, matching s059 and s165. The narration
   ("near-freezing water"), the shark, Doug, "HUNDREDS OF METERS" and the HUD (417, SHARK AGE ~100) all match.
5. **s001**: Uses the new HI FRIEND? art at 1920x1080. Nothing is cropped, Doug's free hand is raised in a wave, and it
   works as the opening image for "Some sharks under the Arctic ice right now".

All three thumbnails are original MS Paint style. None has gore, realistic violence or kids-show framing, and none is
misleading against its paired title.

### Advisory (not blocking)

- B (graphic designer): At 168x94 the head-on shark, with its downturned mouth line and wide-set eyes, reads more like
  a generic grumpy big fish than a shark. The number carries the thumbnail, so this is fine. If there's a future
  revision, a hint of gill slits or a slightly more pointed snout would help.
- C (graphic designer): Doug's legs run off the bottom edge under the card. This is acceptable since the head, cap and
  card carry him.
- s098 (director): The thermometer's red fill still sits at about 60%. The label resolves it. Dropping the fill to the
  bulb would be a nice extra.
- s137 (illustrator): The Round 3 note about the flag pole bracket still stands if it hasn't been addressed.
