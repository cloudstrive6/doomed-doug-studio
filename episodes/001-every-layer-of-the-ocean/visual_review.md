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

## Round 2: pre-render keyframes + thumbnail (2026-09-29)

I re-checked every shot whose scene changed since Round 1 (60 shots, diffed against `1706d59`) at full resolution in
`build/keyframes/`, plus the regenerated contact sheets, `build/thumbnail.png` (1280x720) and
`build/thumbnail_small.png` (320x180).

**VERDICT: PASS**

### Round 1 fixes: all resolved
- **1. s213:** the new `thumbs_up_hand` reads instantly as a thumbs-up. It has a fist with knuckles, a nail and a
  blue cuff, and the car sits on the thumbnail. The phallic read is gone.
- **2. s001:** the real thumbnail is rendered natively at 1920x1080. Every label sits inside the frame, there is no
  cropping and no pixelation.
- **3. s176:** the belly-up swallower now sits on the surface line at the end of the pan, with its stomach and "GAS"
  both readable.
- **4. s114:** the blanking rect is gone. The full barreleye now has a dashed outline around the dome and a "?".
- **5. s060:** the scientist and Doug are outside the tank.
- **6. s050 and s051:** in s050 Doug is on the sofa, so the sofa joke lands. In s051 he stands with a `gritted`
  expression.
- **7. s150:** Doug swims toward the lure at a readable size.
- **8. s182:** Doug is alive (not a ghost) and watches the whale.
- **9 and 10. s088 and s089:** the sub is at the Ogasawara circle and "JULY 2012" is above the map. The "~1,000 km"
  label sits beside the circle near Tokyo, off Australia.
- **11. s107:** "NOSTRILS" has a red arrow to the dark spots.
- **12. s156:** "SHARED BLOOD" has an arrow to the attached male.
- **13 to 17. s005, s009, s189, s101, s241:**
  - s005: the title is clear of Doug.
  - s009: the float is uncropped.
  - s189: the bus and "SHAG CARPET" are separated.
  - s101: a medium shot shows the squid leaving right, with Doug readable.
  - s241: the gravestone is uncropped.
- **18. s239 to s245:** the run is now varied. s240 is a porthole close-up with "great.", s244 is a wide shot with a
  small sub and a depth line.
- **19. Text overlaps:** s010, s015, s017, s023, s027, s068, s080, s144 and s212 are all clean.
- **21. s036 and s037:** the fish and Doug are clear of the coral.
- **Other changed shots are fine.** s038, s039, s059, s097 to s099, s113, s131, s133 to s143, s146, s147, s151, s154,
  s159 to s161, s186, s210, s225 and s236 are on-model and legible, with no gore and no new collisions.

### Thumbnail
- **Readable at 320x180.** The depth pyramid goes from bright to near-black. All 10 labels stay legible and every
  creature reads: man o' war, bobbit worm, giant squid, barreleye, anglerfish, black swallower, zombie worms,
  plastic bag and snailfish.
- **Doug is visible.** He has the red cap and a shocked face on the right. He is small, as the brief asks, but still
  visible.
- **It fits the title.** It complements "How Doug Would Die in Every Layer of the Ocean" without repeating any title
  word, and it isn't misleading: every tile is a chapter subject.

### Non-blocking notes (optional polish, not required to pass)
1. **s156 (director):** the attached male is only about 60 px, and the red X over him reads as "dead" more than
   "fused". Optionally scale him up to about 2x and drop the X. The narration covers "eyes stop working" anyway.
2. **s197 and s198 (illustrator):** carried over from Round 1, item 20. The ice block is still a flat pale rectangle
   and could use rounded corners, a bevel and crack lines.
3. **Thumbnail (graphic designer):** Doug could be about 20% larger and tilted or sinking beside the pyramid to sell
   the "Doug + threat" read at feed size. It is fine as is.

Next visual gate: post-render (`build/samples/*.png`, `build/qc.json`).

## Round 3: post-render (2026-09-29)

**VERDICT: PASS**

Inputs checked: `build/final.mp4` (1920x1080, 60 fps, 1034.6 s, has audio), `build/qc.json` (no problems, 34 samples),
all 34 `build/samples/f_*.png` (one frame every 30 s, at t = 15 s, 45 s, 75 s and so on), `build/thumbnail.png`,
`build/thumbnail_small.png` and `metadata.json`. I also ran my own check at 2 fps over the whole video: blackdetect
(0.5 s, pix_th 0.05) and freezedetect (12 s). Neither found anything.

### Samples
- **No black, blank, torn or glitched frames.** The chapter label box is present and spelled right in every sample,
  from PORTUGUESE MAN O' WAR through CHALLENGER DEEP, and matches `chapters.txt`.
- **Doug is on-model everywhere he appears.** He has the red cap and white head in f_001, f_002, f_004 to f_007,
  f_008, f_009, f_014, f_016 to f_018, f_020, f_022, f_025 to f_028 and f_031, plus the porthole shot in f_033. He
  reads against every background, including the near-black hadal trench. His ghost form (f_003, f_011, f_031) and
  the death counter (f_011 "DOUG DEATHS: 3", end card "DOUG DEATHS: 7") display correctly.
- **The pictures match the narration** at each timestamp I checked against `timing.json`:
  - f_001 / s006: party balloon.
  - f_009 / s070: Humboldt squid, 50 kg and 1.5 m.
  - f_021 / s153: anglerfish lure.
  - f_026 / s177: the 2004 map.
  - f_029 / s206: THE WALL at 8,200 to 8,400 m.
  - f_030 / s213: car on a thumb, for pressure.
  - f_034 / s233: amphipod and 1930s to 1970s pollution.
- **Sparse samples are mid-reveal, not errors.** I checked the full-resolution frames at the end of each shot:
  - f_007 / s055: the fish halves and "CUT IN TWO" appear at 0.75. The halves are pink cartoon cross-sections with
    no blood, so they are acceptable.
  - f_013 / s097: the X, the sperm whale and "SPERM WHALES" appear at 0.57 and 0.86.
  - f_024 / s171: the swallower fills up, and the mackerel gets an X.
- **Policy is clean.** No gore, only cartoon deaths, and the tone is adult-coded with no nursery framing.
- **Variety is good.** Across 34 samples, no run of near-identical compositions.

### Thumbnail and package
- **Readable at 320x180.** The labels and tiles are legible and the depth gradient is clear. It complements "How Doug
  Would Die in Every Layer of the Ocean" and is not misleading, since every tile is a chapter subject.
- **The description is ready.** It keeps `{{CHAPTERS}}`, which `studio/youtube.py` fills at upload.

### Advisory (non-blocking, future episodes)
1. **Director:** s055 holds Doug alone on an empty blue frame for about 3.7 s before the fish halves appear (appear
   0.75). Pull reveals earlier (0.4 to 0.5) or put a placeholder subject in frame so the first second is never
   empty. The same pattern shows at the start of s097.
2. **Graphic designer:** Doug is still small at feed size. Next time, make him about 20% larger or overlap him with
   the pyramid edge.
