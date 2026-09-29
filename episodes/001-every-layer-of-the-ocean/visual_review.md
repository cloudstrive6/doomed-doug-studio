# Visual review: 001-every-layer-of-the-ocean

## Round 1: pre-render keyframes (2026-09-29)

I reviewed all 245 keyframes on the 21 contact sheets in `build/contact/`, and opened the suspect shots in
`build/keyframes/` at full resolution. Keyframes are the final state of each shot, so for pans (`pan_up` and
`pan_down`) they show the last frame.

**VERDICT: FAIL**

### What passes
- **Doug is on-model everywhere.** He has the red cap and white head in every shot, and his auto white ink reads on
  every dark zone. The squid costume follows the art director's upright-pose rule.
- **The death counter is consistent.** It runs 1 (s021), 2 (s043), 3 (s084), 4 (s160), 5 (s179), 6 (s197) and
  7 (s218), and s243 shows exactly 7 gravestones.
- **Every death is cartoon only.** Ghost Doug, X eyes, a flattened Doug, a cap floating up, and his head in the
  anglerfish's mouth, all with no blood. s055 (fish cut in two) shows a pink cross-section with no blood, which is
  acceptable. None of it has a nursery or kids'-show tone.
- **Topbars and creature cards are legible and spelled right.** I checked Vampyroteuthis infernalis,
  Izu-Ogasawara, Piccard + Walsh, Vescovo and Monterey Canyon.
- **Creatures are recognisable.** The man o' war, cone snail, bobbit worm, the squids, barreleye, vampire squid,
  anglerfish, black swallower, Osedax, snailfish and Trieste all read clearly.
- **Zone palette progression works.** It goes sunlight, twilight, midnight, abyss, hadal.

### Required fixes

**Blocking**

1. **s213 (illustrator + director): risky, unrecognisable drawing.** The "thumb" is a flesh-coloured upright
   rectangle with a rounded ellipse cap (a raw `rect` and `ellipse`, no asset). With a car parked on top it does not
   read as a thumb, and to an adult audience it can read as phallic. That is an advertiser-friendliness risk.
   - **Illustrator:** draw a proper `thumbs_up_hand` asset: a fist with knuckles, the thumb pointing up with a
     visible nail, and a wrist or sleeve cuff.
   - **Director:** replace the rect and ellipse with it, keeping the car parked on the thumbnail.
2. **s001 (graphic designer): opening image is the director's placeholder thumbnail** (`thumbnail.json` still has
   the `_draft` placeholder note).
   - The "ANGLERFISH / BLACK SWALLOWER" label is cropped off the left edge ("GLERFISH", "ALLOWER").
   - The "MAN O' WAR" label overlaps the man o' war drawing.
   - "HUMBOLDT" labels a tier that also holds the giant squid, barreleye and vampire squid.
   - It is rendered at 1280x720 and upscaled with nearest-neighbour, so it is visibly pixelated beside every other
     shot.
   - **Fix:** replace it with the real thumbnail design at 1920x1080, with every label inside the central 90%.
3. **s176 (director): key subject never in frame.** The camera is `pan_up`, but `black_swallower_full` sits static
   at y=1200. As the camera rises the fish slides out of the bottom, and the last frame shows only a sliver of its
   stomach under "GAS".
   - **Fix:** put the floating, belly-up swallower near the surface (about y=480, straddling the 540 band line) so
     the pan ends on it.
   - Or make the shot static with the fish centred.
4. **s114 (director): reads as a render glitch.** A `rect` filled with the background colour (#e8e0cc, 320x300)
   blanks out the fish's head and slices the dome in half with a hard edge. It looks like a broken drawing, not
   "nobody saw the whole picture".
   - **Fix:** remove the rect.
   - Instead show the full barreleye with a dashed outline around the dome labelled "?", or cover the head with a
     torn-paper patch that has an outline.
5. **s060 (director): Doug and the scientist are inside the aquarium.** Both stand on the rocks in the water, so the
   shot reads as a layering or position error.
   - **Fix:** move them outside the tank, in front of the glass: scientist at about x=250, Doug at about x=1700,
     both at y≈900. Keep the "?" over the tank.
6. **s050 and s051 (director): Doug sits on nothing in open water.** He uses the `sit` pose floating mid-screen
   (s050: x=1500, y=370), and in s050 the sofa sits empty right beside him.
   - **s050:** seat Doug on the sofa (about x=960, y=430, scale 0.5) so the joke "longer than a sofa, living under
     the floor" lands.
   - **s051:** use `stand` with a `gritted` expression, or seat him on a rock.

**Composition, clarity and accuracy**

7. **s150 (director): invisible Doug.** He is at scale 0.3 in the `lie` pose rotated -90, with a `sleepy`
   expression, at the bottom right. At that size he reads as a red-and-white speck. The pose also looks like a death
   pose ten shots before death 4 (s160).
   - **Fix:** remove him, or put him in `swim1` at scale ≥0.45 drifting toward the lure.
8. **s182 (director): continuity error.** Ghost Doug (`"ghost": true`) floats mid-pan, but Doug is alive here:
   death 5 was s179, and s180 and s181 show him alive.
   - **Fix:** use normal Doug (`float`, `sad`) watching the whale sink, or drop him.
9. **s088 (director): misleading map.** The submersible is parked in the Southern Ocean off South America, while
   the red Ogasawara circle is near Japan.
   - **Fix:** move the sub next to the circle, or drop it. Also move "JULY 2012" off the continents, into the Pacific
     or above the map.
10. **s089 (director): misplaced label.** The "~1,000 km" label sits on Australia.
    - **Fix:** draw a dashed line from Tokyo to the circle and put the label next to that line.
11. **s107 (director): label points at nothing.** "NOSTRILS" floats in empty water to the right with no pointer.
    - **Fix:** move it next to the face at the dark spots, with a red arrow like s105's. Keep the "REAL EYES" arrow.
12. **s156 (director): labels are far from their subjects.** "FUSED" floats at the left, away from the male, and
    "SHARED BLOOD" sits next to the lure.
    - **Fix:** put both labels beside the attached male at the belly, stacked, with one red arrow.
13. **s005 (director): title hides Doug.** The "PORTUGUESE MAN O' WAR" title wordart runs across Doug's cap and the
    top of the float.
    - **Fix:** raise the wordart to y≈120, or lower Doug and the man o' war by about 80 px.
14. **s009 (director): float cropped.** The float is cut off at the top edge and sits behind the topbar label.
    - **Fix:** lower the man o' war by about 120 px or zoom out slightly.
15. **s189 (director): school bus collides with text.** The bus overlaps the topbar label, and "SHAG CARPET" is
    printed over the bus windows.
    - **Fix:** move the bus down and left (about y=380), and move the wordart to the left third, clear of the bus.
16. **s101 (director): Doug hard to see, picture off-script.** Doug is tiny, red cap on the red iris rim, and the
    extreme eye close-up doesn't show "turns and slowly leaves".
    - **Fix:** use a medium shot with the squid swimming off right (red arrow) and Doug at a readable scale, left.
      Keep "SEEN ENOUGH".
17. **s241 (director): cropped gravestone.** The last gravestone (y=3300) is cut by the frame top on the final pan
    frame and collides with the topbar.
    - **Fix:** move it to y≈3500 or remove it.
18. **s239 to s245 (director): variety.** Seven consecutive shots are built around the same centred yellow
    submarine on black. s239, s240, s243, s244 and s245 are near-identical.
    - **Fix:** vary at least two of them, for example:
      - s240: a close-up of Doug's unimpressed face in the porthole with the "great." bubble.
      - s244: a wide shot with the sub small and the depth line.

**Text overlapping drawings (minor, fix in the same pass; all director)**

19. The fixes below are listed by shot.
    - **s010:** "THIRTY METERS" is crossed by the tentacle line and the dashed line. Move the wordart left of the
      tentacle.
    - **s015:** "ONE JOB" is printed over the tentacles. Move it above the float or below the job labels.
    - **s017:** "FLOATING COMMITTEE" overlaps the float, and the "JELLYFISH?" label is covered by tentacle tips.
      Raise the wordart and move the label beside the tentacles.
    - **s023:** "WEEKS LATER" sits on the stranded tentacles. Move it to the sky band.
    - **s027:** "TV REMOTE" runs into the coral. Move it left, over the remote.
    - **s068:** "DIABLO ROJO" is printed over the boat cabin and fishing rod. Raise it above the boat or move it to
      the left.
    - **s080:** "CANNIBALISM" overlaps the bottom row of squid. Move it below the grid, or remove the bottom-right
      row.
    - **s144:** The "MIDNIGHT ZONE" title touches Doug's glow and cap. Lower Doug by about 80 px.
    - **s212:** Both pressure arrows cut through "800x PRESSURE". Start the arrows below the text.

**Optional (not blocking)**

20. **s197 and s198 (illustrator):** Doug's "ice block" is a flat pale rectangle over the ribs and reads like a
    picture-in-picture card. Give it ice cues: rounded corners, a bevel highlight and a couple of crack lines.
21. **s036 and s037 (director):** the fish and Doug overlap the purple coral and are hard to separate. Nudge them
    clear of the coral.

### Routing
- **Director:** fixes 3 to 19 and 21, plus the scene change in fix 1.
- **Illustrator:** the `thumbs_up_hand` asset (fix 1). Optionally the ice block (fix 20).
- **Graphic designer:** the real thumbnail, which replaces the s001 placeholder (fix 2).
- **Art director:** nothing required. The style is consistent across all zones.

After the fixes, re-run `python -m studio keyframes 001-every-layer-of-the-ocean --shots
s001,s005,s009,s010,s015,s017,s023,s027,s050,s051,s060,s068,s080,s088,s089,s101,s107,s114,s144,s150,s156,s176,s182,s189,s212,s213,s240,s241,s244`
and send the result back for Round 2.
