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
