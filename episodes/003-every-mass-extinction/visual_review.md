# Visual review: 003-every-mass-extinction

## Round 1: pre-render keyframes (2026-10-01)

Scope: all 249 keyframes in `build/contact/sheet_01..21.png`, checked against the narration in `shotlist.json`. I also opened full-size
keyframes for s047, s058, s071, s098, s106, s116 and s130.

VERDICT: FAIL

### What works
- Picture matches narration on almost every shot, and each act has a clear colour zone (moss blue, reef teal, ozone grey,
  Siberia maroon, hot-tub red, purple ocean, Pangaea yellow-green, Deccan grey, Chicxulub sky blue).
- The death counter goes 18 > 19 (s025) > 20 (s047) > 21 (s071) > 22 (s110) > 23 (s132) > 24 (s152) > 25 (s198) > 26 (s220) > 27 (s246).
  The survivals in s091 (stays 21) and s177 (stays 24) are correct, and the count matches the series bible (18 at the end of 002).
- No gore. All deaths are cartoon: X eyes plus a ghost. The heart in s151 and the "good moss" bubble are deadpan rather than
  nursery-style, so I see no made-for-kids risk.
- Doug is on-model (red cap, white head) everywhere except the death pose (fix 1). The red head in s089-s091 is the sunburn joke and
  reads as intended. Doug's limbs switch to white on dark backgrounds, so he stays readable.
- No spelling errors found. Title cards, labels and the caption bar are legible.

### Required fixes

1. **Death pose looks like a disembodied head. Shots: s047, s071, s110, s152, s198, s220.** Route: art director, then director.
   `pose: "lie"` with `rotate: -90` draws a head split half red / half white, with the visor sticking straight up. The torso and limbs
   collapse into a fan of thin lines coming out of the head. At contact-sheet size the payoff shot of every death reads as a "head with
   whiskers", not as Doug lying flat. I tested it: `lie` without rotate draws him standing, so the director cannot fix this from the
   shotlist. Art director: add a proper lying pose with the cap still reading as a cap. For example: body horizontal, arms and legs
   splayed, head turned to camera with the cap tipped off beside it. Director: then swap these six shots to that pose and drop the `rotate`.
   Interim option if the art director can't extend the rig in time: use the series-bible gag "red cap floating alone after a death",
   plus the ghost, and leave the body off-screen.

2. **s130, s131: the towel sits over Doug's mouth like a gag.** Route: director.
   `head_towel` is at y=630 while Doug is at y=508. s132 is correct because there the towel y equals the Doug y. Set `head_towel.y` to 508
   in s130 and s131 so the towel sits on top of the cap, matching the narration "a little towel on his head".

3. **s024: the wordart "FREEZE A PLANET" (x=1240, y=360) overlaps the "good moss" speech bubble.** Route: director.
   Move the wordart to about x=1380, y=230, or shrink it to size 72, so it clears the bubble's right edge (~x=880).

4. **s196, s197: the wordart "BLEND IN" / "VERY SERIOUSLY" (x=860, y=250) is printed over Doug's head and cap.** Route: director.
   Move the wordart to the right half, about x=1400, y=250, clear of the ammonites, or move Doug down and left.

5. **s116: the wordart "BRUTAL" (x=800, y=560) covers the conodont tooth drawing it is about.** Route: director.
   Move it out of the circle, e.g. x=1500, y=200, size 110, above the thermometer.

6. **s224, and s201: the asteroid is a black silhouette that reads as a hole or stain, not a rock.** Route: director.
   In s224 it is a black silhouette on a near-black background (#0b0b18) with a red haze, so the key subject is not obvious in 1 second.
   Set `silhouette: false` so the real asteroid drawing shows, as in s225. Alternatively, keep the silhouette but use a lighter sky.
   In s201 the small black blob on blue is equally unreadable. Use the plain asteroid drawing there too.

7. **s058: the red X at upper left crosses out nearly invisible pale bubbles on the cream background.** Route: director.
   As it stands, the X looks like a stray mark. Add an "O2" label like the one in s054, or recolour the bubbles dark blue.

8. **s233: the thermometer (x=1600, y=480) is drawn on top of the sauropod's head, and it shows a warm reading for "cooled".**
   Route: director. Move it into clear sky, about x=1450, y=330, and show it falling (low level, or the red down arrow used in s183).

9. **s150: Doug sits half behind the Lystrosaurus with the leaf across his face, so it reads like the animal is eating him.**
   Route: director. "Befriends ... ignores him" needs a gap. Move Doug to about x=450 and put the leaf in his outstretched hand
   (about x=560, y=620), so he is offering it to an animal that is not looking at him.

10. **s145: the speech bubble's tail points at the horizon (tail [320,560]), not at the scientist.** Route: director.
    The scientist also stands inside the purple sea. Point the tail at the scientist's head, about [300,720], and stand him on a
    short land strip or move him to the shoreline.

11. **Variety: s049-s054 are six near-identical shots.** Route: director.
    All six use the same reef backdrop and framing (only the label and the sky colour change), and s056 repeats it again. Recompose
    at least two of them. For example: s051 as a wide panorama or map showing the reef spread, and s052 as a close camera push on
    the stromatoporoid and coral so the labels have room.

12. **Variety: s101-s104 are four near-identical strata cross-sections.** Route: director.
    Change s103 to a close-up of a burning coal seam with flames, and s104 to a pull-back to the surface with gas plumes rising into
    the sky.

13. **s001 shows the "(thumbnail pending)" placeholder.** Route: graphic designer.
    The opening image is the thumbnail, so it must be delivered and the keyframe re-rendered before the final render.

### Should fix (minor polish, not blocking on its own)
- s047: the clock is rotated, so the numerals read 6/9/3/12 in the wrong places. Keep the clock upright and move the hands instead.
  The flippers also stand upright, detached from Doug; lay them by his feet. (director)
- Text crossing outlines: "SUPERCONTINENT" over the globe edge (s027), "NO REAL ROOTS" touching the ice cube (s025), "NOWHERE TO HIDE"
  across the sea/fresh-water divider (s084), "MADE IT" across the ozone line (s091), "PANGAEA SPLITS" with the red rift through the
  title (s154), "PANGAEA" (s155), "GREEN SULFUR BACTERIA" over the circle edge (s140), "DISAPPEARED" over the coastline (s193),
  "SHOOK THE PLANET" over the shock rings (s211). Nudge each 40-80 px clear. (director)
- s210: stray "- - - -" dashes under the timeline, not connected to anything. Remove them or draw a proper span bracket. (director)
- s098: the map is cropped off at the left and bottom with a blue band above it, and the Siberian lava is only a faint red speckle.
  Frame the map fully and add a solid lava patch over Siberia. (director)
- s122: "chalky algae" are plain white circles with X's, which are hard to recognise. A small coccolith (plated sphere) drawing would
  read better. (illustrator)
- s228, s229: the four coloured bars have no labels. Add the extinction names so "thousands of years" vs "1 day" lands. (director)

### Round 1 routing summary
- Art director: 1
- Director: 1-12, plus the minor items
- Graphic designer: 13
- Illustrator: s122 (optional)

Re-run `python -m studio keyframes 003-every-mass-extinction --shots s001,s024,s047,s049,s050,s051,s052,s053,s054,s058,s071,s101,s102,s103,s104,s110,s116,s130,s131,s145,s150,s152,s196,s197,s198,s201,s220,s224,s233`
and send the new sheets back for round 2.
