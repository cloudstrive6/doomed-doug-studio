# Visual review: 006-disturbing-deep-sea-discoveries

## Round 1: pre-render keyframes (2026-10-04)

Scope: all 24 contact sheets (s001 to s278), plus full-size keyframes for s018, s025, s038, s041, s063, s065, s092,
s097, s112, s113, s117, s136, s163, s180, s213, s240 and s256. s001 is the thumbnail placeholder; I ignored it as instructed.

### What passes
- **Doug:** on-model everywhere I checked (red cap, white head, snorkel and fins gear consistent). Ghost Doug and the
  dead/flat poses keep the cap, so he always reads.
- **Death counter:** 46, then 47 (s024), 48 (s069), 49 (s091), 50 (s115), 51 (s138), 52 (s161), 53 (s182), 54 (s205),
  55 (s244), 56 (s271). In order, with no skips.
- **Policy:** every death is cartoon only. X-eyes, ghost floats up, cap left behind, RIP headstone. No blood, organs or
  dismemberment. s092, s161, s205 and s271 show a lying body with all limbs attached. Nothing reads as a kids' show:
  animals have no cute faces, the humour is dry, and the speech bubbles are deadpan.
- **Text:** the caption bars, WordArt and labels are spelled right, and nothing is cropped at the frame edge. The depth
  meter is back on s061 and s068, and the surface iceberg beats now read 0 M.
- **Drawings:** recognisable on the whole (hammerhead, pufferfish, squid silhouette, scaly-foot snail, black smoker,
  submersible, inverted Empire State Building and inverted Everest as depth comparisons). Earlier art-review fixes (s149,
  s191, s251, s089) are confirmed in the renders.

### Required fixes (blocking)
1. **s038 (illustrator):** the crossed-out black silhouette (the "alien mystery") is an unreadable bell/blob shape.
   Nobody will see "alien" or "UFO" in it in 1 second. Replace it with a clear flying-saucer silhouette (dome plus disc
   rim plus a short beam) or a grey alien head with big almond eyes, then keep the red X.
2. **s213 (illustrator, then director):** the three "egg case / sponge" guess silhouettes are pure black (#000) on
   abyss navy (#050a1f), so they are nearly invisible and none of them can be identified.
   - Fill them mid-grey (about #5a6070) with a thin light outline, or give them the red guess-glow used in s014 and s032.
   - Make one shape a clear skate egg case (a rectangle with curled corner horns) and one a clear vase sponge.
   - Drop the third shape or make it obvious.
3. **s240 (director / art director):** Doug's body is drawn in white on the cream (#f4ecd8) lab background, so only
   his head and cap show. He looks like a floating head. The element sets `"ink": "#000000"`, but the render ignores
   it. Get the black ink to apply (or render Doug with the dark-background-off line colour, as he appears in
   s149/s214/s259). Also offset him a few px so the divider line does not run straight through his spine, unless the
   "on the fence" gag is wanted, in which case keep it with black ink.
4. **s112 (director):** Doug stands on top of the "~900 M" depth label. His legs disappear behind it and the label box
   cuts him off at the knees. Move Doug to x≈1650, y≈850 (right of the chart, under the red "?"), or anywhere clear of
   the meter column (x < 360).
5. **s018 (director):** the scientist's speech-bubble tail is a long double needle that enters the bubble and runs
   across "LIVE HERE", with a stray tick mark inside the bubble. Shorten the tail so it stops at the bubble edge, and
   anchor it toward the scientist's mask (≈1530, 330) without crossing the text. The same needle-tail habit is milder
   in s113 (crosses the fishing rod) and s180 (points into empty space up-left of Doug, not at his mouth). Re-aim
   both at Doug's head.
6. **s119–s125 (director): variety.** That is seven near-identical frames in a row: the same brine pool, same scale,
   bottom centre, dark navy, with only labels changing. s128–s132 repeats it five more times, with the pool sliding left
   and right. Break the run with at least two compositions:
   - s121 Cordes close-up: a waist-up scientist with the 2014 label and no pool.
   - s124 a macro cross-section: the pool as a heavy layer under seawater, salt particles sinking.
   - s129 a close-up of the warning sign and the gas plume over the pool surface.

### Recommended fixes (non-blocking, do them if time allows)
7. **s064, s065 (director):** Doug, the thermometer and the goldfish float inside the solid rock walls of the
   blue-hole cross-section. Doug reads as buried in rock. Put Doug on the surface (as in s063) or inside the shaft.
   For "LIKE THE CARIBBEAN", the generic goldfish says nothing. Swap it for a small Caribbean map inset with an arrow
   to the hole, or a "CARIBBEAN SEA" sign, and keep the thermometer.
8. **s117 (director):** the chapter WordArt "THE JACUZZI OF DESPAIR" starts flush against the depth meter (the T
   touches it at x≈255). Shrink it to about 90 px, or recentre it at x≈1060, so there is at least 40 px clear of the
   meter. s140 ("THE CHAMPAGNE VENT") is also tight against the meter and crossed by bubble columns. Nudge it right
   or drop the leftmost column behind it.
9. **s256 (director):** the "9,533 M" label sits on top of the left tubeworm cluster (only the red tips poke out), and
   a loose red marker triangle floats beside it. Move the label up to y≈880, left of the Everest tip, so it clears
   the worms, and delete the orphan triangle (or attach it to the tip).
10. **s163, s072, s076, s077, s078, s085, s088, s217 (director):** WordArt crosses drawings. Examples: "SNAIL" runs
    through the black-smoker plume in s163, "LOST CITY"/"PALE TOWERS"/"FIRST LIFE?" through chimney tops, "ANEMONE" and
    the 2 m dashed line through the tentacles in s217. All of it stays legible thanks to the outline, but shift the
    text into open water (usually 60–120 px up or sideways) so the key drawing is clean.
11. **s219–s222 (director):** four near-identical orb-on-rock frames (Doug left, orb centre). The gag continuity
    justifies some of it, but make s221 ("Doug is fine.") a tight two-shot of Doug and the orb, or a push-in camera,
    to break the run.
12. **s273–s278 (director):** six consecutive TV-monitor frames. The progression (cap drifts in, clam closes, heart)
    works as the payoff, but push in on s275 and s276: crop to the clam filling about 60% of the monitor so the
    "clam closes on it" beat reads at phone size.
13. **s125 (director):** the lone red X at the right has no referent. Either attach it to a "MIXING" label or a
    swirl icon ("without mixing"), or remove it. The same applies to the "?"-behind-X in s218 and s222: label it
    (for example, "EGG? SPONGE?") or drop it.

### Routing summary
- **Illustrator:** 1, 2
- **Director:** 2 (layout), 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
- **Art director:** 3 (Doug ink colour on light backgrounds)
- **Graphic designer:** none this round (thumbnail pending)

VERDICT: FAIL. Fix shots s038, s213, s240, s112, s018 and the s119–s125 / s128–s132 variety run, then re-render those
keyframes for round 2.
