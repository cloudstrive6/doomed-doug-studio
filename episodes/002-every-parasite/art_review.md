# Art review: 002 Every Parasite

Reviewer: art director.

- **Round 1 (assets)**: 53 new library drawings. 48 approved, 5 sent back (see the history at the end).
- **Round 2 (this review)**: a re-check of the 5 fixed drawings, plus all 247 keyframes in `build/contact/sheet_01..21`
  (commit 196c074), with full-size spot checks from `build/keyframes/`.

Checked against: `channel/art_bible.md`, style bible section 7 (Art Director rules 1-9), and the brief's gore/kid-appeal
watch.

## Round 3 (keyframe re-check, commit 29042fe): FAIL, 2 small composition fixes (director)

I re-checked the 25 re-rendered shots in `build/contact/sheet_01..03`, with full-size checks of s015, s087, s099, s148,
s170 and s179.

Resolved:
- Fix 1 (s014, s015, s062): all the WordArt now sits on the cream sky and reads at phone size. In s015, "GROOMS" and
  "A FEW MINUTES" don't touch (there is a gap of about 15 px).
- Fix 2 (s066, s243, s247, plus the s241-s246 set): the moon and sun are at (1720,330), clear of the counter, and the
  sun no longer jumps between shots of the set.
- Fix 3 (s100): "CAT" is fully readable, and the rat and heart sit below and right of it.
- Fix 4 (s179): "LATRINE" is above the box, and the raccoon's mask is clear.
- Fix 5 (s178): the egg cloud reads at a glance, so "MILLIONS" lands.
- Fix 6 (s170): hopeful Doug and the mosquito under a red X give the frame a subject, and it no longer repeats s171.
- Advisory s148: the stray stroke is gone, and the glowing trypanosome silhouette reads.

Doug is on-model with his cap visible in every shot, the zone colours are unchanged, and gore watch is clean.

Required fixes (route to the director):
1. **s087: the death counter now clips the songbird's head.** The sun moved correctly, but the bird silhouette at
   (1180,260), scale 0.9, has its head and beak under the "DOUG DEATHS: 11" box (about x 1268-1693, y 130-200). This
   is the same collision as fix 2, and the counter zone is reserved. Move the `songbird` to `x 1200, y 380` and keep
   its scale and glow, so the head clears the box by about 100 px and the tail stays off the top leaf. Don't move the
   counter.
2. **s099, s100: the WordArt now sits on the pen's top edge.** "LOST THEIR FEAR" and "DRAWN TO IT" are at y 170 and
   their bottoms touch the pen border at y 200, so the outline merges with the 7 px line. Set both `wordart` to
   `y 135`. That leaves about 20 px of clearance above (under the caption bar) and below (above the pen).

Re-render only `--shots s087,s099,s100`. The other 22 shots in this round are approved.

## Round 2 verdict: FAIL (assets PASS; 6 keyframe composition fixes, all routed to the director)

The episode is close. Style is consistent across all 11 chapters. Doug is on-model in every shot, and his cap is visible
everywhere, including ghost Doug, the costumes, the lilo, the hammock and the floating cap. Each chapter keeps its own
background family, and the value ramp darkens on the reveal/death beats. Gore watch is clean. Layout variety is good:
maps, pens, body outlines, timelines, dish, bar charts, split day/night and scenic sets rotate, and nowhere do I see the
same composition five times in a row. The six fixes below are all collisions or beats that don't read. None of them
needs a new drawing.

## Part 1: fixed assets re-check: PASS (all 5)

Previews used: `assets/previews/002-every-parasite-assets-fixes.png`, `-assets-fixes-checks.png` (white / night navy /
silhouette / small-scale + cap tests), `-costumes-fixes-on-doug.png`.

| Asset | Verdict | Notes |
|---|---|---|
| field_cricket | PASS | The big striped jumping femur now rises above the back line, and the spiny tibia folds down to the ground in a clear inverted V. Wings lie flat. The SIL reads as a cricket at 2.0, and so does the small version. |
| cricket_costume | PASS | Both sides now have proper inverted-V jumping legs. The brown tibias with light spine ticks hold up on `#1b2a4a` (checked in s064/s065 at full size). The wing cape reads. Doug's cap and face stay clear. |
| raccoon | PASS | Legs are tapered, the hind heel bend shows, and the paws are dark rounded mitts. Body, mask and tail are unchanged. The cap sits correctly on the head in s191. |
| blood_flukes | PASS | Now a proper ~210-degree C, ends curling in, with the darker female in the groove and the suckers at the front. It reads as a C even at thumbnail size (s110, s118, s119 at 2.0). |
| rat_costume | PASS | Pink mitten paws with toe ticks sit at sleeve cuffs. The hood now wraps both sides of the face and no longer reads as headphones. |

## Part 2: keyframes: required fixes (route all to the director)

1. **s014, s015, s062: lime-on-lime WordArt. Decision: fix it.** "STOPS WANTING", "GROOMS" and "DRESSED AS A CRICKET"
   sit at y=950 on the lime ground (`#b8e05a`). At full size the dark outline saves them, but in the contact sheet
   (which is roughly phone size) they sink into the grass, and the yellow-to-green gradient is the ground colour.
   Move each `wordart` up onto the cream sky and keep the size:
   - s014: `x 700, y 250` (left of the EXIT door, clear of Doug's antennae).
   - s015: `x 960, y 150`. The "A FEW MINUTES" label at (560,240) stays. Check that the two don't touch, and if they
     do, move the label to `x 480, y 330`.
   - s062: `x 960, y 150` (above the arrow, which starts at about (1100,110). Shorten the arrow start to (1060,150)
     if it touches).
   I have added this as a standing rule in the art bible: no WordArt on green ground or fields.
2. **s066, s087, s243, s247: the death counter overlaps the moon/sun.** The "DOUG DEATHS: N" box (centred at
   1480,165) covers half the moon/sun at about (1600-1650, 170-190), so it looks like a pasting mistake on four
   death beats. Keep the counter where it is (it's the recurring layout) and move the celestial body:
   - s066 moon: `(1720, 330)`, r 60.
   - s087 sun: `(1720, 330)`, r 80. The bird silhouette is further left, so it's clear.
   - s243 and s247 sun: `(1720, 330)`, r 70. Also move the sun in s241/s242/s244/s245/s246 to the same spot, so
     it doesn't jump between shots of one set.
   This is now an art bible rule too: the counter zone is reserved.
3. **s100: the rat hides the "CAT" label.** The whole beat is "infected rats go to the cat corner", but the rat
   (700,330, scale 0.6) now covers the CAT box, so only a "C" shows. Move the rat to `x 760, y 380` so it sits just
   below and right of the label (as in s099), and move the heart to `x 880, y 280`. The CAT label must be fully
   readable.
4. **s179: the "LATRINE" label covers the raccoon's face.** The label is at (950,740), right over the raccoon's
   head. Move it above the right half of the latrine box, to `x 1060, y 640` (clear of the head and below the
   red arrow). Or move the raccoon left to x 700. The raccoon's mask must be visible.
5. **s178: "MILLIONS" has nothing to count.** The egg sprays (`#fff3c4` at 0.08 and `#c9b27a` at 0.03 on
   `#f6d9cf`) are practically invisible, so the right half of the frame is empty and the beat doesn't land.
   Replace them with a dense scatter of the same small cream egg ellipses used in s177 (rx about 14, black 3 px
   outline). Use about 60-80 of them in a loose cloud centred on (1300,600), r about 330, and let them pop in with
   `appear` 0.53. Or bump the spray to a darker `#8a7550` at density 0.25 or more. The eggs have to read at a glance.
6. **s170: empty frame.** It's only "PREVENTED AND CURED" on flat pink, and s171 is another text-only frame straight
   after it. Give s170 a subject: Doug `hopeful` at about (560,820), scale 0.6, plus the `mosquito` at (1350,700),
   scale 0.35, under a red X (`appear` 0.4). Keep the WordArt, moved up to y 250.

## Advisories (not blocking; director's call)

- **s148**: there's an unexplained brown line element from (1100,900) to (1180,700) next to dead Doug. It reads as
  a stray stroke. Remove it, or turn it into something readable.
- **s034**: Doug appears without the ant costume mid-chapter (s033 and s036 have it). If he is meant to be the
  researcher here, that's fine. If not, add `ant_costume` for continuity. The plain-Doug shots in s090/s091 (Doug as
  "people") and s101/s102 are fine as they are.
- **s099, s100, s241**: the WordArt sits right under the caption bar (it nearly touches). It's legible, but dropping
  it about 30 px would let it breathe.
- **s128/s129, s244/s245**: these pairs share a composition. That's acceptable as build-up (the stat card pair and
  the end-card pair), and I'm not asking for a change.

## Resolved from round 1
- s216/s218 amoeba glow: now a strong red halo on `#3d0f18`, so it reads.
- s168/s169 mosquito speck: a red arrow now points at it in both shots, so it reads.
- s064/s065 cricket costume on night navy: reads after asset fix 2.

After the director applies fixes 1-6, re-render only those shots (`python -m studio keyframes 002-every-parasite
--shots s014,s015,s062,s066,s087,s100,s170,s178,s179,s241,s242,s243,s244,s245,s246,s247`) and send them to me for a
quick re-check. The other shots are approved.

---

## History: round 1 asset fixes (all now resolved)
1. field_cricket: add the big jumping hind leg and lay the wings flat. **Fixed.**
2. cricket_costume: add inverted-V legs, brown tibias and a rim highlight for night shots. **Fixed.**
3. raccoon: taper the legs, add a heel bend, use mitt paws. **Fixed.**
4. blood_flukes: curl into a 200-220 degree C. **Fixed.**
5. rat_costume: give the forepaws a paw shape and wrap the hood. **Fixed.**

The round 1 approved list (48 assets) stands unchanged. Director notes from round 1 are listed under "Resolved"
above.
