# 034 Every Bison Reason: visual review

## Round 1: pre-render keyframes (visual screener, 2026-11-01)

**Note on inputs.** `build/contact/` held only `sheet_01.png`, because a partial `keyframes --shots` run wipes every sheet and
rebuilds only the shots it rendered. The shotlist had also been edited (s207 icon discs) after the last full render. So I
re-ran `python -m studio keyframes 034-every-bison-reason` on the current shotlist: 209 keyframes, sheets 01-18. Every tile was
viewed, and the suspect shots were checked at full size.

### What works
- Doug is on-model in every shot (red cap, white head): the wolf costume (s020-s024) and referee shirt (s003, s195-s200) keep
  the cap and face readable. He reads on snow, grass, dusk orange and the death-beat black.
- Death counter: 267 -> 274. That is seven deaths (s025, s071, s092, s111, s131, s153, s201) and it matches the seven icons in s207.
  The new cream discs behind the s207 icons fix the art director's note B. The icons now read on the dark slate.
- Text: no misspellings, nothing cropped, no labels on top of drawings. Calendar months follow the ramp.
- Chalkboard tallies in s140 come to 25. The dot grid in s062 shows 12 of 25. The fortnight grid in s144 is correct.
- Gore and policy: all deaths are cartoon (cap on the ground, ghost Doug). There is no blood. The real calf death (s085-s086) is
  a plain grey silhouette card with no figures. The hump cutaway (s032-s033) is a clean textbook diagram (pink band, ivory
  spines, no blood), so it is acceptable. Nothing reads as a kids' show: the calf is never cute or close-up (decision 5c is followed).
- Planned beats that look deliberate and are fine: the empty riverbank in s087-s088, the calf silhouette on the scale in s080, and
  the sober card in s124-s127.
- Variety is good overall, with many locations and diagram cards. The only run of 4 or more near-identical frames is the sober card,
  which is deliberate (see fix 4).

### Required fixes
1. **s105: broken clock (director).** The three `clock` assets are rotated 0/120/240 to show time passing. Rotating the whole
   asset also rotates the numerals, so the final frame shows 3 at the top, 6 on the right, 12 on the left and 9 at the bottom.
   Change: set `rotate: 0` on all three clock elements (or keep one clock) and show the passing time with the hand only, for
   example a red `arrow`/`line` hand from (480,470) that pops in at three angles with `appear` 0, 0.3 and 0.55. Do not rotate the face.
2. **s113, s116, s117, s194: "visitors" read as lollipops or cotton buds (director).** Each visitor is a white circle on a single line,
   with no arms or legs. In s113 the narration subject is "the visitors", and at 1080p they read as a row of lollipops, not people.
   Change: swap each circle+line pair for the library `stick_man_plain` at about 0.3 scale, keeping the same x positions. Use about 8-10
   figures instead of 17 so they don't merge into a fence. Keep `appear` 0.3 in s113.

### Minor fixes (do these in the same pass)
3. **s061: the TOSS panel is just an arrow (director).** BUTT and HOOK both show the bison head, but TOSS has no bison and nothing
   being tossed, while the narration says "throws the person into the air". Change: add `bison_head_icon` at (1340,690) scale 1.0,
   plus a tiny `stick_man_plain` (about 0.18, rotated about 30) at the arrow tip near (1380,500).
4. **s127: the card line doesn't match the narration (director).** The narration is "The bison did not come to them", but the new line
   is "PARK RULE: 23 M". Change: make the new line `THE BISON DID NOT MOVE`, or move "PARK RULE: 23 M" to the next shot that mentions
   the rule. This also gives the 4-shot card a fresh reason to change on its last beat.
5. **s203: the push-in is too weak to show the sticky note (director).** The keyframe matches s202. Change: camera `zoom_in`
   to the PLANT EATER note at about (800,560), with `zoom` 1.8 (it is 1.1 now), so "all it says is plant eater" lands on the note.
6. **s032 (and s033): arrow tails start inside the label boxes (director).** The MUSCLE arrow starts on the "E" and the LONG BONES
   arrow starts on the "S". Change: start each arrow at the label's lower edge (MUSCLE from about (720,425), LONG BONES from about
   (1440,355) in frame coordinates) so no letters are crossed.

### Optional (non-blocking)
- s166 (illustrator): the dog on the rug has pointed ears and a closed-eye smile, so it reads a little like a cat. A longer snout
  or floppier ear would make "picture a dog" instant.
- s156 / s177 (director): "THE RUT." is used as the season card at s156, then chapter "THE WALLOW" follows, then chapter "THE RUT" at
  s177. This is fine because the narration says it, but the topbar jump RUT -> WALLOW -> RUT is a little confusing on a scrub.

### Still pending (not part of this verdict)
- s001 shows "(thumbnail pending)". The thumbnail is also the opening image, so screen s001 and the three thumbnails in the
  post-render round once the graphic designer delivers them.

VERDICT: FAIL
Required: fix 1 (s105 clock) and fix 2 (visitor figures in s113/s116/s117/s194). Fixes 3-6 are minor and should go in the same pass.
After the changes, run the full `python -m studio keyframes 034-every-bison-reason`, not `--shots`, which deletes the other sheets.

## Round 2: pre-render keyframes after director fixes (visual screener, 2026-11-01)

**Inputs.** Full rerender `build/contact/sheet_01..18` (209 shots + endslate), every tile viewed, suspect shots checked at
full size from `build/keyframes/`. Camera end-frames for s009, s021, s107 and s203 judged from `/tmp/patch034/cam.png`
(render_still + camera_rect at u=1, s009 at u=0). I re-rendered trial crops of s021 and s107 at other zoom levels to confirm the fixes below.

### Round 1 fixes: status
1. s105 clock: FIXED. The face is upright (12 at top, 3 right, 6 bottom, 9 left) and a red hand shows time passing.
2. s113, s116, s117, s194 visitors: FIXED. They are now 8-10 stick figures with arms and legs, and they read as people.
3. s061 TOSS panel: MOSTLY FIXED. The bison head and a tossed figure are now there, but see minor fix A.
4. s127 card: FIXED. The last line is "THE BISON DID NOT MOVE".
5. s203 push-in: FIXED. At the end of the zoom (1.75) the PLANT EATER note is big and centred, and it lands on "plant eater".
6. s032 arrows: FIXED. Both arrows start below their labels, and no letters are crossed.

### Camera shots
- s009: fine. The "?" over the black wolves is visible and the HUD is intact.
- s203: fine (see above).
- s021 and s107: at the end of the zoom, the in-scene HUD is cut by the top edge of the frame. In s021 the calendar icon and "JAN"
  are sliced in half and the death counter is gone. In s107 only a sliver of the calendar/"JUN" box shows at the very top.
  It reads as a glitch on the held frame (see minor fix B).

### Rest of the episode
- No new problems. Doug is on-model everywhere. The counter runs 267 -> 274 with seven deaths. Text is clean. There is no gore.
  Variety is unchanged from round 1 (good).
- The optional notes from round 1 (s166 dog reads a little cat-like; RUT -> WALLOW -> RUT topbar) still apply and are still optional.

### Minor fixes (non-blocking, apply before the final render)
A. **s061 (director): the tossed figure sits on the panel border and the arrow goes through the bison's face.** The `stick_man_plain`
   at (1380,500) has its head poking above the top edge of the TOSS box (y=450), and the arrow at x=1360 runs straight up through the
   bison_head_icon at (1340,690). Change: move `bison_head_icon` to (1300,690). Move the arrow to `from` [1420,690] and `to` [1420,580],
   so it rises off the horns beside the face. Move `stick_man_plain` to (1440,560) at scale 0.2 and keep rotate 30, so it sits inside
   the box above the arrowhead.
B. **s021 and s107 (director): the zoom end-frames slice the calendar/counter HUD.**
   - s021: set camera `zoom` 1.35 (it is 1.25 now) and keep x 1260, y 760. I rendered this: the HUD leaves the frame cleanly, and
     "12", "13" and Doug in the costume all stay fully in frame. Do not go to 1.4, because that crops the "12" label at the left edge.
   - s107: set camera `zoom` 1.4 (it is 1.3 now). I rendered this: the HUD leaves the frame cleanly, and the bison and "!" are centred.
     Doug leaves the frame, which is fine for "until it does".

### Still pending (post-render round)
- s001 "(thumbnail pending)", the three thumbnails, the final-video samples/qc.json, and the Shorts.

VERDICT: PASS
Both required fixes from round 1 are in, along with minor fixes 4-6. Fix 3 is mostly done. Minor fixes A and B take one line each. Apply them before
`render --final`. They do not need a full keyframe re-screen: a still of s061 and a camera end-frame of s021/s107 (the cam.py method)
is enough.

## Round 3: check of the round 2 minor fixes before the final render (visual screener, 2026-11-01)

**Inputs.** I rendered the current `shotlist.json` with `render_still`, with all elements visible (t=None). The zoom shots got
camera-aware end-frames: `camera_rect` at u=0 and u=1, then `fit_frame` at 1920x1080 (the cam.py method). s040 and s061 got full
stills. I checked crops at 2x. Files are in `/tmp/vs034/`.

The director used a different fix from the one I asked for. s021, s107 and s203 are now `zoom_in` 1.1, anchored at (960,491), not my
1.35/1.4. At u=1 the crop rect is (87, 0, 1833, 982). The top edge stays at y=0, so the top-right HUD never leaves the frame and
is never cut. This fixes the problem behind minor fix B another way: the HUD now stays in, where my fix pushed it out. It also
keeps the push within the style bible's 10% limit. I accept this fix.

### Shots
- **s021: PASS.** On the held end-frame, "DOUG DEATHS: 267" and the calendar with "JAN" are whole. The box's right edge is about 20 px
  from the frame edge. Nothing is sliced. All 12 wolves, the "12" and "13" cards, and Doug in the wolf costume (red cap, white head)
  are fully in frame.
- **s107: PASS.** On the end-frame, "DOUG DEATHS: 270" and "JUN" are whole. The confused Doug (left), the grazing bison and the red "!"
  are all in frame. The bison is the clear subject on "until it does."
- **s203: PASS.** The 1.1 push is much softer than the old 1.75. The new red ring around the yellow PLANT EATER note gives it a clear
  focal point within a second. The ring stays on the left page, and "AMERICAN BISON" above it is not crossed. The HUD with "274" and
  the red "RUT" is whole. The ring sits over the coffee stain, which is harmless.
- **s040: PASS.** The red strike-through crosses both words of "ANGRY? HUNTING?" at mid-cap height, and all the text stays readable.
  It appears at 0.45, after "not hunting you", and then BUSY lands. It overshoots the box's right edge by about 2 px, which is
  not visible at viewing size.
- **s061: PASS (fix A applied as written).** The tossed `stick_man_plain` now sits fully inside the TOSS box, above the arrowhead.
  The arrow rises beside the bison's face, not through it. Butt, hook and toss read left to right. Cosmetic note only: the TOSS
  bison's flat base rests on the panel's bottom border, while in the BUTT and HOOK panels it floats mid-panel. It reads as standing
  on the panel floor, so no change is needed.

### Still pending (post-render round)
- s001 "(thumbnail pending)", all three thumbnails and their `_small` versions, `build/samples/*.png` and `qc.json` from final.mp4,
  and the Shorts (previews, frames, cliffhanger end cards).

VERDICT: PASS
All five shots are cleared for `render --final`. No further keyframe changes are needed.

## Round 4: thumbnails A, B and C (visual screener, 2026-11-01)

**Inputs.** `build/thumbnail.png` (A, from `thumbnail.json`), `build/thumbnail_b.png` (`thumbnail_test_b.json`),
`build/thumbnail_c.png` (`thumbnail_test_c.json`), all 1280x720, plus their `_small.png` at 168x94. I viewed the smalls at 1x and
at 3x nearest-neighbour, and made zoom crops of B's Doug and C's HUMP tile (`/tmp/vs034t/`). I checked them against the title
"Every Reason the Bison Is Yellowstone's Most Terrifying Animal", the four alts and the `thumbnail_brief` bans.

**Brief bans (all variants).** No variant uses a title or alt word: IT'S BEHIND YOU, REFEREE, SPEED, HUMP, SNOWPLOW, WALLOW,
JAM and RUT are all clean. None has a distance number (23 M / 25 YARDS), safety wording, a calf, a real person or a horn
touching Doug. Doug is on-model (red cap, white head) in all three.

### A (hero, also s001): PASS
- At 168x94 the focal point is clear: a huge charging bull fills the left two-thirds, and tiny red-capped Doug smiles into a
  selfie stick on the right. "IT'S BEHIND YOU" is readable in the feed. The words are tight but whole, with no clipping at
  either edge.
- The text clears the top of the hump by a few px with no overlap. The horn tip and the nose are about 60 px from Doug. It shows
  the threat without contact.
- It is honest. The video's selfie-stick beat (script line 264) and the s001 open match it. It complements the title, since the
  title names the animal and the picture shows the peril. It has no gore and no nursery tone.
- Cropping: the bull's rump bleeds off the left edge on purpose. The head, hump, beard and front legs are whole.

### B (rut / REFEREE): PASS
- At 168x94 the striped shirt and red cap pop dead centre between two dark bulls. It reads as "Doug is about to be crushed" in
  under a second. REFEREE is big and fully legible.
- The whistle is at Doug's mouth and his shock face reads. Both horns stay clear of Doug's body. It matches the payoff promised
  at 0:10 and the rut beat (script lines 26 and 400), so it is not misleading.
- Cosmetic, no change needed: Doug's arms are thin lines that mostly hide behind the shirt, and the two brown motion arcs in the
  top corners (about x200-310 and x1045-1120, y130-210) read as faint noise at feed size. Neither hurts the read.

### C (6-tile list control): FAIL
1. **HUMP tile (`thumbnail_test_c.json` elements[1], `fill` `#ff5a3c`). Route: graphic designer.** The `bison_hump_cutaway` puts a
   pink muscle band with ivory spines on a red-orange tile. Full size, it is a clean diagram (cleared for s032-s033 in round 1).
   At 168x94, though, the pink patch on red reads as an open wound on the bull's back. It is the brightest, most eye-catching
   spot in the grid, and the thumbnail is the surface that gets the strictest advertiser review. Fix: change the tile `fill` to a
   cool colour that no other tile uses, e.g. `#9b5de5` (purple). Keep the asset as it is. Then re-render `thumbnail_c.png` and
   `_small`. The red tile is the only problem: with a cool background the pink reads as a diagram, not an injury.
- Everything else passes. All six labels (Comic Neue Bold on white bands) are readable at 168x94 and none is cropped. Every
  drawing is recognisable: charge, snow, legs-up wallow on brown dirt, car jam, locked bulls. Doug appears small in JAM only,
  which is acceptable for the approved 032-style list control. Advisory, no change needed: the legs-up WALLOW pose could read as a
  dead bison at feed size. The dirt patch under it carries the meaning, and it is not gore.

VERDICT: FAIL (A: PASS, B: PASS, C: FAIL, 1 fix)
A and B are cleared for upload and the Studio A/B test. C must have fix 1 before it enters the test. Re-screening C needs only
the new `thumbnail_c_small.png`.

## Round 5: thumbnails A, B and C re-check (visual screener, 2026-11-01)

**Inputs.** `build/thumbnail.png`, `thumbnail_b.png` and `thumbnail_c.png` (1280x720, rendered 18:35) and their `_small.png`
(168x94), viewed at 1x and 3x nearest-neighbour, with zoom crops of A's hindquarters and C's WALLOW tile (`/tmp/vs034r2/`).
Checked against the title, the four alts, the `thumbnail_brief` bans and the script. This round I also judged each one as the
creative director would: would I click it, and is it honest?

**Brief bans (all variants).** The text is clean: IT'S BEHIND YOU, REFEREE, WOLVES, SNOWPLOW, SPEED, WALLOW, JAM and RUT use
no title or alt word. There are no distance numbers, no safety wording, no calf, no real people and no horn touching Doug. Doug
is on-model wherever he appears.

### A (hero, also s001): PASS
- **Does it read as a charge? Yes.** The head is down below the shoulder line, the near foreleg reaches far forward and the
  hind leg drives back, so the bull is mid-stride. The tail is raised (cropped at the top-left edge) and three speed lines trail
  off the back on the correct (rear) side. Dust puffs sit at the hooves. At 168x94 the pose alone carries the motion: it reads
  as "lunging at him", not "grazing". The dust is faint at feed size, but it isn't needed.
- The single focal point is clear. A huge dark bull fills the left two-thirds, and tiny white-headed, red-capped Doug smiles
  into the selfie stick at right. That contrast makes the joke in under a second. The nose is about 40-50 px from Doug and the
  horn about 90 px, so the threat is close but there is no contact.
- The text is whole, readable at 168x94 and clears the hump. Cropping is deliberate: the rump and tail bleed off the left
  edge, and the head, hump, beard and forelegs are whole. No stray lines.
- **Click test: yes.** The dramatic irony ("he doesn't know") is the strongest hook of the three. It pairs well with the
  title: the title names the animal and the picture shows why. The selfie beat is in the video, so it is honest.

### B (rut / REFEREE): PASS (unchanged from round 4)
- The striped shirt, red cap and shock face sit dead centre between two mirrored bulls in a dust cloud. REFEREE is big and
  legible. It is honest (the 0:10 payoff promise and the rut beat). Cosmetic only, no change: the two thin brown arcs in the top
  corners are faint noise at feed size.
- **Click test: yes.** It is a strong "what is he doing there" image and a good challenger to A.

### C (6-tile list control, rebuilt): PASS
- Round 4's fix 1 is resolved by the rebuild. The HUMP tile and its pink muscle band are gone, so nothing in the grid reads as
  a wound. The tiles now run WOLVES / SNOWPLOW / SPEED over WALLOW / JAM / RUT, with six distinct background colours (pale blue,
  lilac, yellow, teal, green, orange) and no repeats.
- All six labels are readable at 168x94 and none is cropped. All six match script items (The Wolves, The Snowplow, The Speed,
  The Wallow, The Jam, The Rut), so the grid is honest.
- **Does the wallow read as a live bull? Yes.** It is lying down with its legs tucked under it, not legs-up, and its head is
  raised with horns up and an open, alert eye. It sits on a dirt patch inside a speckled dust cloud. Nothing suggests death:
  no X eyes, no tongue, no belly-up pose. At 168x94 it is the softest tile (a brown lump with a head on the right, and the dust
  speckle mostly washes into the teal), but it reads as "resting bison", not a carcass. Advisory only, no change required: if
  the designer touches C again, a few bolder dust puffs or a tilted, mid-roll body would make "wallow" more active.
- Other tiles: the WOLVES line-up reads as grey wolves with tiny Doug at the back. SNOWPLOW's snow-capped head is clear, SPEED's
  raised tail and lunge are clear, JAM's red car against the bull is the brightest read, and RUT's locked heads are clear.
- **Click test: yes, for list-format viewers.** It promises a variety of reasons, and that fits "Every Reason" well. It is
  weaker than A at a glance because it has no single focal point, which is expected of the list control.

VERDICT: PASS (A: PASS, B: PASS, C: PASS)
All three variants are cleared for upload and the Studio A/B/C test, with A as the lead. **Creative-director-level approval is
recommended:** A reads as a charge and is the strongest click, B is a strong challenger, and C's wallow reads as a live bull.
No packaging fixes are outstanding. Still pending for the post-render round: `build/samples/*.png`, `qc.json` and the Shorts.

## Post-render review (2026-11-01)
Inputs viewed: `build/samples/f_001`-`f_023.png` (640x360, every 30 s across final.mp4), extra 1080p grabs around 6:26-6:34,
`build/qc.json`, `build/thumbnail.png` plus all three `_small` versions, `metadata.json`, `shorts.json`,
`build/shorts/short0{1,2,3}_preview.png` and 10 frames from each Short mp4 (4 from the body, 6 from the last ~8 s), with
full-res crops of the three end-card silhouettes. Nothing was re-rendered.

### Main video
- qc.json: 689.3 s (11:29), `problems: []`. No black, blank, glitched or frozen samples. The only dark frame is the deliberate
  RECORD stat card (f_013: "YELLOWSTONE, 2000 TO 2015 / 25 PEOPLE HURT BY BISON / ALL WITHIN 6 M / 8 IN 10 HAD WALKED UP TO
  IT"). All four lines are legible.
- Continuity: the topbar runs through the chapters in order (WOLVES, SNOWPLOW, HUMP, CALF, SPEED, RECORD, JAM, WALLOW, RUT).
  The death counter climbs monotonically from 267 to 273, the month badge runs JAN to AUG and then RUT, and every sample has the
  counter and badge. Doug is on-model (red cap, white head) and readable in every frame that has him, including the wolf costume
  (f_003) and the referee shirt (f_021).
- Drawings: wolves, elk, bison bull, cow, calf, cars, scales, the US map and the stopwatch all read in under a second. The hump
  cutaway (f_004, s032/s033) is the textbook diagram cleared in round 1, with arrows starting at the label edges. It is not a wound.
- Text: CHAPTER labels, MUSCLE / LONG BONES, the struck-through "ANGRY? HUNTING?" over BUSY, 12 OF 25, MANY TIMES, 1.5 M,
  BEST VIEW / FINISH LINE, EVERY 2 WEEKS, -90 KG / 1 DOUG and DOUG'S NEXT DEATH are all spelled correctly, uncropped and clear
  of the drawings.
- Policy: cartoon only, with no blood, no gore and no contact shown. The tone is adult and dry, not nursery.
- Variety: consecutive samples change composition, background colour or scale, and there is no run of near-identical frames.
- Advisory only (no change required):
  - s136: the question_mark floats in the sky over the 3rd car, so it does not clearly belong to anyone. If touched, move it
    over Doug's head (about x 1840, y 860).
  - s169: the wallow silhouettes' red outlines double up on the legs and look slightly jittery at 640 px. They read fine at 1080p.

### Thumbnails / packaging
- `thumbnail.png` (A, IT'S BEHIND YOU), the lead, matches the round-5 approval: one focal point (the charging bull), tiny
  red-capped Doug with the selfie stick, and no contact. At 168x94 the text and the joke both read. B (REFEREE) and C (6-tile
  list) at 168x94 are unchanged from round 5 and still read.
- They complement "Every Reason the Bison Is Yellowstone's Most Terrifying Animal" without repeating a title word. They are
  honest: the selfie beat (s129), the referee beat (s197) and all six list tiles are in the video.

VERDICT (main): PASS

### Shorts
| Short | Title payoff | Cliffhanger (outro / end card) | Silhouette | Verdict |
|---|---|---|---|---|
| short01 (34.0 s) "A Bull Bison Plows Snow With Its Face (Up to 900 kg)" | Yes: the head-swing snowplow with the arrow, the hump, and the 900 kg scale vs pianos | "Doug went and stood exactly where the snow used to be" / WHAT DID THAT SWING DO TO DOUG? Specific and unanswered | american_bison_snowplow: head-down hump-and-beard bison, red outline, recognisable | PASS |
| short02 (49.2 s) "This Sofa With a Beard Can Run at 55 km/h" | Yes: SOFA WITH A BEARD wordart with the sofa, 55 KM/H (s097) | "timed one with a stopwatch, standing on the finish line" / WHAT DID DOUG'S STOPWATCH READ? Unanswered (the payoff "finishes before Doug presses start" is s110, outside the clip) | american_bison_charging: raised tail, lunge, recognisable | PASS |
| short03 (35.6 s) "A Bison Bull Can Lose Nearly 90 kg in One Rut" | Yes: the -90 KG scale, 12%, TENDING, the threat and the dust fight | "Doug stepped between them with a whistle to referee" / WHAT HAPPENED WHEN DOUG BLEW THE WHISTLE? Unanswered | american_bison_charging, recognisable | PASS |

- All three: the title is legible, red on the top band. Burned-in subtitles are large and white with an outline. No drawing is
  cut at the sides (the 9:16 crops keep Doug, the bison and the topbar in frame). The end-card arrow points straight down
  between Doug and the silhouette. @DoomedDoug is legible.
- Advisory only (no change required):
  1. short01 title wraps as "...(Up to 900 / kg)", which leaves the unit orphaned on line 3. If the titler revises it, use
     "A 900 kg Bull Bison Plows Snow With Its Face" (fits on 2 lines) **(youtube-titler, shorts.json `title`)**.
  2. short02 shows the s099 "1.5 S" stopwatch (tennis-court time) before asking what Doug's stopwatch read. It does not answer
     the question, because the real answer is "he never pressed start", but a viewer may guess "1.5 s". It is acceptable as a
     red herring.
  3. short02 and short03 use the same `american_bison_charging` end-card silhouette. For variety on back-to-back Shorts, the
     director could set short03 `tease_asset` to `bison_bulls_locked` (in the library), which matches the whistle/referee
     question better. Check that its silhouette still reads before swapping.
  4. The "???" sits across the silhouette's body and the red glow under it. Both read as the channel's standard tease
     treatment, not as blood.

VERDICT (shorts): PASS
