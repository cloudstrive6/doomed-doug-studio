# Visual review: 007-every-time-earth-froze

## Round 1: pre-render keyframes (2026-10-05)

Scope: all 276 keyframes (contact sheets 01-23, plus single-frame checks). s001 (thumbnail pending) is excluded as instructed.

VERDICT: FAIL

The episode is in good shape overall. Doug is on-model almost everywhere, the death counter runs correctly (56 -> 65), the deaths are all cartoon (ice blocks, ghosts, a lone cap), there is no gore, and nothing reads as a kids' show. It fails on one engine-level bug that makes Doug invisible in 5 shots, one rendering glitch, and a batch of text collisions and occlusions.

### Blocking fixes

1. **s036, s037, s038, s050, s051: Doug's body is drawn in white and disappears on the ice.** (director, with a note to the art director)
   Doug's stick body and head outline render pure white (#ffffff) against the near-white ice (#f2f6fa). Only the cap and face are visible, so he looks off-model and headless. Cause: auto-contrast in `studio/paint.py` (line ~479) samples a single pixel at `y - 80*scale`, and that pixel lands on a dark arch of `old_london_bridge`, so the engine switches Doug to white ink.
   Fix (director): add `"ink": "#000000"` to the `doug` element in each of these 5 shots, or move Doug so his chest isn't in front of the bridge arches.
   Engine note (art director): make the auto-contrast sample an area average instead of one pixel. Otherwise any Doug standing in front of a dark detail on a light ground will hit this again.
2. **s238: a white rectangle glitch cuts the horizon.** (director)
   The masking `rect` (x 250, y 500, w 300, h 330, fill #eef4fb) that hides the walking Doug also paints over the snow-line outline, leaving a visible blank notch left of the pond.
   Fix: drop the mask rect. Hide the walking Doug with a timing or `disappear` mechanism instead, or limit the rect to the sky above the horizon (bottom edge above y≈800 at that x).
3. **s120 and s125: the gold medal and red ribbon cover Bretz's face.** (director)
   Fix: move the medal down to his chest, about 60 px lower so it sits below the head circle. The face needs to read as a person receiving an award.
4. **s118: the "J HARLEN BRETZ" label is cut by the "FLOOD!" bubble, so it reads "HARLEN BRETZ".** (director)
   Fix: move the speech bubble left or down (for example x≈380) so it doesn't touch the label, or move the label to the right of Bretz.
5. **s114: Doug's head and cap cover the "NN" of "CHANNELED SCABLANDS".** (director)
   Fix: drop Doug by about 120 px so he stands on the canyon rim (y≈300 in tile terms, the ground line), or raise the wordart.
6. **s040, s054, s055: "PRINTED ON THE THAMES" runs past the card's inner border on both sides (the "P" and "S" are clipped by the frame).** (director, or illustrator if the text is baked into `printed_card`)
   Fix: reduce that line's text size by about 20% (or scale the card up about 15%) so it fits inside the red inner border with margin.
7. **s088: the "NORTH ATLANTIC" label spills out of the map and touches the right edge of the frame.** (director)
   Fix: move the label inside the map, over the Atlantic just right of the arrow head (x≈1600), or shorten it to "ATLANTIC".
8. **s214: Doug is lying horizontally in mid-air in the orange sky with no context.** He reads as flying or glitched. (director)
   Fix: put him floating on the water surface (feet at y≈300), or stand him on the limestone band. Otherwise remove him from the shot.
9. **s223: three stacked date tags ("717 TO 660 MILLION YEARS AGO", plus "660 MILLION YEARS AGO" floating above the time machine's own "717 MILLION YEARS AGO" tag).** It reads as a duplicated-label bug. (director)
   Fix: remove the floating "660 MILLION YEARS AGO" tag. Keep the main range label and the time-machine tag.
10. **s147, s172, s195: tree canopies sit on top of the DOUG DEATHS counter and the FROZEN badge.** (director)
    Fix: move the top-right trees left or down (canopy top below y≈200, or x < 1550) so the counter and badge are clear.
11. **s110: Doug floats about 100 px above the ice dam near the top edge of the frame, and the "TO" in "NOT BUILT TO LAST" overlaps the warning sign.** (director)
    Fix: seat Doug on top of the dam (feet at the dam's top edge, y≈360) and move the warning sign about 60 px down, clear of the wordart.
12. **s044 and s046: the wordart ("A BRIDGE", "HEAD START") and the red "?" are printed over the houses on the bridge.** Legibility is poor at speed. (director)
    Fix: move the wordart down into the open water or ice area (y≈1250-1350 equivalent, under the arches), and move the "?" next to Doug.
13. **s071: the tsunami is a single thin white arc and isn't recognisable as a wave.** (director, or illustrator if a new asset is needed)
    Fix: reuse the wave drawing from s078 (the blue curling wave), scaled down, approaching the coast from the left.
14. **s189: the wordart says just "CLOSE TO", a meaningless fragment.** (director)
    Fix: change it to "CLOSE TO SNOWBALL" (or "ALMOST FROZEN") and give it the same outlined wordart style as the rest of the episode. It is currently plain flat green.

### Should fix (non-blocking; do with the round above)

15. **s062, s073, s134, s059: green wordart ("DOGGERLAND", "DROWNED SLOWLY", "DRY", "HILLS, RIVERS") sits over green land and the map frame, so contrast is low.** (director) Move each to open blue sea inside the map or to the sky outside the map frame. s019 "BOTH SIDES", s090 "SLOW DOWN", s127 "PEAK" and s258 "HURONIAN" straddle the map's bottom border too. They are readable but cleaner if lifted about 40 px.
16. **s024: the sunscreen bottle hovers in mid-air beside Doug's hip.** (director) Put it in his hand or on the snow.
17. **s185: the tree crown is hidden behind the chapter tag at the top edge, so it reads as a bare pole.** (director) Lower the tree by about 120 px so the canopy shows under the tag.
18. **s142: the "mine" bubble's tail points at the CHICAGO flag, not Doug.** (director) Move the bubble left or retarget the tail to Doug's head.
19. **s003: the red "?" touches the "D" of "DID NOT AGREE".** (director) Move the "?" up by about 30 px.
20. **s060, s061, s133, s137: Doug floats a little above the ground or slope (25-60 px).** (director) Drop him so his feet sit on the line.
21. **Variety: s062-s065 are 4 consecutive near-identical North Sea map shots with Doug in the same spot, and s238-s244 are 7 consecutive near-identical pond shots (Doug and algae in the same pond).** (director) In s063 or s064, punch in on the shrinking island. In the pond run, change the framing on at least 2 shots (for example a close-up of Doug and the algae for s239 or s243, or a wide shot with the ice sheet for s242).
22. **s104 and s105: the "Pacific Northwest" map is a plain green rectangle with rivers and no state lines or coastline cues, so "IDAHO" and "CANADA" are hard to place.** (director; illustrator if a new map asset is wanted) Use the North America map asset from s129, cropped in, or add state outlines.

### Checked and OK
- Doug on-model (red cap, white head) in every shot except fix 1. Ghost Dougs and frozen-in-ice deaths are clearly cartoon.
- No gore, blood or realistic violence. The tone is adult-deadpan, not nursery.
- Spelling of all on-screen text is correct (Tambora, Sumbawa, Storegga, Meganeura, Kirschvink, Laurentide, Huronian, Sturtian, Marinoan, octopetala).
- Chapter tags, title cards and death counter progression (56 -> 57 at s026, 58 s079, 59 s100, 60 s123, 61 s144, 62 s170, 63 s194, 64 s219, 65 s271) are consistent with the narration.
- s213 uses white-ink Doug on a dark brown background on purpose. It is readable, so no change needed.
