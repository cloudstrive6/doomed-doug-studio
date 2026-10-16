# Visual review: 020-deeper-underground

## Round 2: keyframes (pre-render) + thumbnail

I re-checked all 26 fresh contact sheets (s001 to s308, s001 included now). I opened the doubtful frames at full size: s090, s229, s273, s275, s303 and s307. I also checked the thumbnail at 1280x720 and at feed size (168x94).

**Round 1 fixes confirmed:** s002/s005 (text clears the planet), s023/s024 (MOVILE tag sits beside the marker), s045, s083 ("SURVIVED" fully readable), s089 (Burj stack clears the HUD), s090 ("DEEPEST CAVE" sits between the passages), s184, s190 (derrick visible), s219 (Doug on the surface strip with the 35 km line), s222, s229, s230, s243, s248, s251, s274, s279, s282, s144, and s262 to s270 (Doug is back in s262 to s265 and s269 to s270, and the heat close-up breaks the globe run). In s307/s308 the AGAIN stamp now sits only on the second Mponeng sticker, and THE MOHO and MOVILE CAVE are fully readable.

**Still good:** Doug is on-model everywhere. All deaths are cartoon only. The death counter goes 161 to 170 and stays consistent. No gore and no kids-show tone. No run of 4 or more near-identical shots is left.

**New problem:** one broken drawing, at s303.

VERDICT: FAIL

### Fixes

1. **s303 (director, composition):** A leftover cream mask polygon covers the left half of dead Doug's head. It is a flat #fff3c0 box, so it shows up as a solid patch against the sprayed background. The polygon is in `scene.elements`, right after the `doug` element: `poly` with points (422,860), (429,790), (625,790), (632,860). Delete that polygon. If it was meant to sink Doug into the floor, use the floor colour (#ffe9a0) and put it below y 860 instead. Dead Doug's whole head, with the X eyes, must be visible. Re-run `keyframes --shots s303`.

That is the only blocking item. Once s303 is fixed, the keyframes pass. No other shot needs a re-check.

### Minor (not blocking, fix if cheap)
- s220: the 4 stacked Everests are still small plain grey triangles (carried over from round 1). Bigger triangles with snowcaps would read as mountains faster.
- s275: the red "?" arrow tip touches Doug's cap brim. Nudge the arrow start about 30 px right.
- s040/s041: "230 KM" and "5 MARATHONS" sit on top of the passage lines. They are readable, but moving them up into plain rock (y about 0.25) would be cleaner.
- s267/s269/s278: the magnetic field lines run through "SHIELD", "WANDER" and "SAFE". They are readable because of the outline, so leave them unless they are being touched anyway.

### Thumbnail (graphic designer): PASS
- At 1280x720 it matches the brief: an Earth wedge with banded strata, one subject per band, 8 chapter labels, and Doug standing at the top edge looking down. It goes with the title "Why the Ground Gets Deadlier the Deeper Doug Goes" without repeating its words, and it isn't misleading (every band is a real chapter).
- At 168x94 the descent wedge, the colour gradient and the pink worm read straight away. Most labels can still be read (Movile Cave, Devil Worm, Oldest Water, Kola Borehole, Hidden Ocean). Doug shows as a red-capped speck.
- Optional improvements: make Doug about 1.5x bigger so he reads as a figure in the feed, not a dot. Give the Inner Core ball a hot orange or white glow so the bottom feels deadlier; right now it is a pale circle. In the middle bands (glass, cage, borehole, pod) the subjects blur into one grey column at feed size, so a little more contrast there would help.

## Round 3: re-check of s303, s221, s268, s184

I opened all four fresh keyframes at full size and zoomed in on dead Doug in s184 and s303.

- **s303: fixed.** The cream cover is gone. Dead Doug's whole head shows, with the X eyes and frown. Only one cap is left, lying beside his head. The flag ("DOUG WAS HERE"), the suitcase, "THE INNER CORE" and DEATHS 170 / DEPTH 6,371 km all read cleanly.
- **s221: pass.** The ocean / 6 KM crust / red Moho line reads straight away and matches "about six kilometers". "MUCH CLOSER" is legible on the mantle. Doug is on-model at the right edge.
- **s268: pass.** The core, the magnetic field loops, the angry Sun, the solar-wind lines bending around the field and the SOLAR WIND label all match the line. Nothing is cropped. The outer field loop passes close to the depth icon but doesn't cover any text.
- **s184: new defect, two caps.** Dead Doug uses `gear: ["cap_off"]`, which already draws his fallen cap behind his head (its red brim pokes out between the suitcase and his head). The scene also adds a separate `doug_cap` asset at (760, 840), which sits on his chest over the arm lines. So the frame shows two caps on one body. This is the same duplicate-cap problem that was just removed from s303.

VERDICT: FAIL

### Fixes

1. **s184 (director, composition):** Delete the `{"type": "asset", "name": "doug_cap", "x": 760, "y": 840, "scale": 0.4}` element. Make the rig's own fallen cap visible by moving the suitcase group about 110 px left: `travel_suitcase` x 538 to 428, the five stickers x -110 each (502/538/574 to 392/428/464), and `again_stamp` x 538.6 to 428.6. Afterwards there must be exactly one cap beside dead Doug's head, and nothing on his chest. Re-run `keyframes --shots s184`.

Once s184 is fixed, the keyframes pass. No other shot needs a re-check.

## Round 4: re-check of s183, s184 (double-cap fix)

I opened both fresh keyframes at full size and zoomed in on dead Doug. The shotlist matches what is drawn: the extra `doug_cap` asset is gone, and the suitcase group has moved left to x 428.

- **s184: fixed.** There is exactly one cap: the rig's own `cap_off` cap lies just left of dead Doug's head, between the suitcase and the head. His chest and arm lines are clear. The suitcase, its stickers and the AGAIN stamp sit together without touching Doug. The ghost Doug (upper left, with the usual cap), WORKPLACE / OVEN, "PIPE FULL OF ICE", DEATHS 166 and DEPTH 4,000 m all read cleanly. The ice pipe stands between the body and the labels, so the picture matches the line.
- **s183: pass.** The composition is the same as s184: one fallen cap, the heat shimmer above the body, and the second Mponeng sticker plus the AGAIN stamp on the suitcase. The counter goes 165 to 166 and lines up with s184. Nothing is cropped, there are no stray lines, and no gore.

The two shots stay on the same set across the cut, so the s183 to s184 change is only the overlays. That is intended and does not make a run of 4 or more.

VERDICT: PASS

The keyframes pass. The minor items from round 2 (s220, s275, s040/s041, s267/s269/s278) are still optional and do not block.
