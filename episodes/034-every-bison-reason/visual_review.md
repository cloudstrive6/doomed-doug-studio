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
