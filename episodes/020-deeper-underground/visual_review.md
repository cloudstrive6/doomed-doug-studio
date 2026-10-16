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

## Round 5: post-render (final.mp4 samples, thumbnail, Shorts)

### Main video
I looked at all 32 sample frames (f_001 to f_032) and at qc.json (duration 968.8 s, `problems: []`).
- There are no black, blank, frozen or glitched frames. The chapter header, DOUG DEATHS and DOUG DEPTH sit in the same place on every frame. Deaths go 161 to 169 and depth goes 18 m, 489 m, 1,300 m, 2,209 m, 2,400 m, 2,800 m, 4,000 m, 12,262 m, 35 km, 660 km, 2,890 km, 6,371 km, so both only ever go up.
- f_001 is a split screen (the Black Sea map next to the MOVILE CAVE title card). I pulled frames at 14 s and 15.5 s and it holds steady with the BLACK SEA label appearing, so it is a deliberate layout and not a stuck transition.
- Doug is on-model in every frame where he appears. All text is legible and nothing is cropped. There is no gore: the death at f_016 is cartoon X-eyes beside a houseplant and rug. Nothing has a kids-show tone. Settings change every one or two samples, so there is no stale run.

### Thumbnail
thumbnail.png is an Earth wedge with eight bands, each holding one subject, from the centipede down to the glowing core, with Doug at the top edge. At 168x94 (thumbnail_small.png) the wedge, the colour going from brown to white-hot, Doug's red cap and all eight labels still read. None of the labels use title words. It fits "Why the Ground Gets Deadlier the Deeper Doug Goes" and does not mislead. One minor note: the Mponeng mine-cage icon is tiny at feed size, but this does not block.

VERDICT (main): PASS

### Shorts
- **short01 (40.6 s): pass.** The title is readable and the subtitles are legible. The Movile cave, centipede and jar are not cut off at the sides. It pays off "sealed 2.5 million years". The outro teases "the king of the cave" without showing it. The end card has a cave_centipede silhouette whose legs and antennae are clearly recognisable, with "???", "WHO IS THE KING OF THIS CAVE?", and the arrow pointing down.
- **short03 (45.9 s): pass.** It pays off the 12 km / 0.2% title (the Earth vs 12 km "< 1 MM" frame). The outro teases "something of his on a string" without naming it. The end card shows a doug_cap silhouette that is recognisable as a cap, matching "WHAT WENT DOWN INSTEAD OF DOUG?". The arrow points down.
- **short02 (36.6 s): FAIL, unrecognisable tease silhouette.** The clip and the outro are fine (it pays off the tasted water, then teases the lonely bacterium 2.8 km down). On the end card, though, `tease_asset: "microbe"` is only about 96 px wide in the library. `_tease_card` caps the scale at 3.0, so it renders as a roughly 290 px dark blob, and the 150 px "???" wordart covers almost all of it. A viewer sees a small red-rimmed smudge behind "???", not a bacterium. Even uncovered, a plain rod with a tail would be hard to recognise as a silhouette.

VERDICT (shorts): FAIL

### Fixes
1. **short02 (director, `shorts.json` only):** Re-target the cliffhanger to something whose silhouette is recognisable and that the Short does not show. Use the Mponeng lift cage:
   - `tease_from`: `"s165"` and `tease_asset`: `"mine_cage"`
   - `outro`: "Further down is the deepest mine on Earth, where a steel cage full of workers drops two kilometers in three minutes. Doug got in. It's linked below."
   - `end_card`: "WHAT WAITS AT THE BOTTOM FOR DOUG?" (7 words)
   - Update `description` to match, ending with "the full episode shows what waits at the bottom of the deepest mine on Earth."
   - Then re-render only short02 and check the preview: the cage silhouette (a box with bars and a cable) must read, and "???" must not hide it.
   - Alternative if the bacterium tease is kept: the end-card silhouette needs an engine change (offset the "???" off the silhouette, or a larger microbe drawing). That is outside shotlist/scene edits, so take it to the art director, not the director.

The main video and thumbnail can go ahead. Only short02 has to be redone.
