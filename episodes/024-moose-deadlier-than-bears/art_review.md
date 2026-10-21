# 024-moose-deadlier-than-bears: art review (assets)

**Verdict: FAIL (1 redraw). 35 assets APPROVED, 1 APPROVED after an art-director fix, 1 needs a redraw.**
Keyframes are not reviewed yet; that review comes later as a separate pass.

Checked against `asset_requests.md` and the house rules (detailed tier vs crude Doug, thick outline, flat fills with interior shading, on-palette, bold silhouette, readable small, no gore). Previews checked: `assets/previews/024-moose-deadlier-than-bears-moose-assets(-detail).png`, `024-moose-deadlier-than-bears-assets-b(-detail).png`, `024-assets-a.png`, `024-assets-b.png`, plus single re-renders on white. I also compared side by side with the library `moose` and `grizzly_bear` drawings.

## Moose batch
| Asset | Verdict | Notes |
|---|---|---|
| moose_warning | APPROVED | Swaps cleanly with `moose`: hump crest spiky, brow lowered, menacing. |
| moose_head_on | APPROVED (AD fix) | The mouth line curved up into a smile, which breaks the brief's "no smile" rule and matters on the thumbnail hero. **Fixed by AD**: element 32 is now a slight downturn. Everything else is strong. |
| moose_cow | APPROVED | Same animal, no antlers, reads at small size. |
| moose_cow_rearing | APPROVED | Silhouette reads as rearing, with the hooves forward at the top. Suitable for the s128 black/red-rim use. |
| moose_calf | APPROVED | Gangly knobbly legs, not cute. |
| moose_charging | APPROVED | Head down, gallop and speed strokes. The antler tips sit front-top, so the flipped pair will lock. |
| moose_velvet | APPROVED | Velvet stubs read as soft and half-grown, with no blood. |
| moose_antler_rack | APPROVED | Full span, palmate, small stub, no skull. |
| moose_head_surfacing | APPROVED | The ears are a little tall and horse-like, but the drooping muzzle, weed and ripples carry the read. Optional polish only. |
| moose_submerged | APPROVED | Blue-shifted palette, bubbles and weed. |
| moose_nose_cutaway | APPROVED | Clear diagram with pink passage and valves, no gore. Nostrils are at (+122,+134)/(+224,+134), within tolerance of the request. |
| moose_in_apple_tree | APPROVED | Moose reads in the crown with dangling legs and falling apples, and has no drunk cues. |
| locked_antlers_ice | **NEEDS FIX** | See fix 1. |
| moose_track | APPROVED | Cloven print with dewclaws, correct length. |
| moose_icon | APPROVED | Still reads as a moose at thumbnail scale. |

## Bears
| Asset | Verdict | Notes |
|---|---|---|
| grizzly_running | APPROVED | Matches `grizzly_bear` palette and claws. It is a sprawling gallop but reads as running, with a closed mouth. |
| grizzly_sleeping | APPROVED | Curled up with closed lids, calm. |
| grizzly_cub | APPROVED | Round but not cute (small eye, no smile). |
| brown_bear_swimming | APPROVED | Head and hump above water, wake visible, muted body below. |
| black_bear | APPROVED | Reads on white, navy and water thanks to the grey-blue highlights and brown muzzle. |

## Props, places, maps
| Asset | Verdict | Notes |
|---|---|---|
| bear_moose_scoreboard | APPROVED | Matches the chalkboard look. Header, divider and underline are correct and the columns are empty. |
| apple | APPROVED | |
| apple_tree | APPROVED | Reads on navy. |
| willow_bush | APPROVED | Dense enough to hide the cow, and does not read as a pine. |
| paddleboard | APPROVED | |
| snow_shovel | APPROVED | |
| cardboard_antlers | APPROVED | Cap brim, face and eyes stay clear. |
| cardboard_antlers_flat | APPROVED | |
| locomotive | APPROVED | Horn and headlight are where the shotlist expects them. No logos. |
| moose_crossing_sign | APPROVED | |
| small_car_driving | APPROVED | Front side window is an open cut-out (x 0..100, y -163..-112). |
| fire_engine | APPROVED | No text or logos. |
| hand_saw | APPROVED | |
| lake_superior_map | APPROVED | Isle Royale pops in yellow. |
| newfoundland_map | APPROVED | Geographically correct, but the dots moved. See fix 2 (director). |
| anchorage_map | APPROVED | Three valleys open toward the city grid. |
| stadium | APPROVED | No logos. |

## Numbered fixes
1. **locked_antlers_ice: redraw (illustrator).** The four antler halves read as clubs or spoons on thin stalks, not as moose palmate racks. The scratched "X" in the middle reads as a mark on the drawing, not as interlocked tines. Redraw as two **broad palmate paddles per rack**, in the same shape language and colours as `moose_antler_rack` (#d9c49a, wide paddles with tines along the rim, short beam). The two racks should meet in the centre with the inner paddles **overlapping**, and the tines should interleave visibly (draw the front rack's tines over the back rack's paddle; no cross-hatch X). Keep the snow caps, the ice line at y=0 and the crack ring. Nothing should appear below the ice. bbox x -350..350, y -260..0. Shots s189 and s190.
2. **newfoundland_map dots (director, composition).** The Gander Bay dot is at (+168,-41) and the Howley dot is at (-121,-9). The request asked for Gander Bay at (+235,-306). Re-place the moose icons and labels in s251–s255 against the real dot positions so they don't float in the sea.
3. Optional, not blocking: moose_head_surfacing could have broader, leaf-shaped ears angled outward so it reads less like a horse at small size.

AD change made: `assets/library/moose_head_on.json` element 32 (mouth curve) changed from an upturned to a slightly downturned line. Re-previewed and verified.

---

# Keyframes round 1 (art director, 2026-10-21)

**Verdict: FAIL.** 280 frames reviewed (24 contact sheets, s001-s279 + endslate), plus full-res re-checks of s189, s190, s196.
The style is consistent: one Doug on-model in every shot (cap visible on ghost Doug too), detailed-tier animals vs crude humans,
zone palettes hold per chapter (meadow green, lake blue, night navy for The Apples, snow grey-blue, rut amber, night road for The Highway),
counter and scoreboard tick correctly (195 to 203; BEAR 5 / MOOSE 11), and there is no gore. The FAIL is for a set of
composition defects (things covering the content they point at, floating or detached objects, and one six-card static run). None of them need
new art except where noted. Most fixes are single-element moves for the **director**.

## Asset re-checks from the asset pass
- **Fix 1 `locked_antlers_ice` (s189, s190): APPROVED.** The redraw now reads as two moose racks. It has broad palmate paddles in the
  `moose_antler_rack` colours, rim tines with snow caps, the inner paddles overlap, there is no cross-hatch X, nothing shows below the ice and
  there is no skull or gore. It reads at contact-sheet size.
- **Fix 2 `newfoundland_map` dots (s251-s255): RESOLVED.** The Gander Bay and Howley moose icons sit on the real dots, and none are in the sea.
- AD addition: new Doug pose **`crouch`** (`studio/doug.py`, documented in `channel/art_bible.md` and `docs/SCENE_SCHEMA.md`). It is a low squat
  with the front hand out, with the same hip y as `stand`. I verified it with `python -m studio art`. Used by fix 12.

## Required fixes (director unless noted)
1. **Narrator hand hides the scoreboard.** In every scoreboard shot the white glove sits on the MOOSE header and the tally it has just added,
   so the tick the shot is about can't be read: s020 (the first MOOSE tick is completely under the palm), s047, s065, s096, s118 ("MOOS"),
   s141, s167, s191, s214, s238, s269 (s018/s019 are borderline, so fix them the same way for consistency). Move the hand down and right so the
   fingertips stop just right of the newest tick, below the header line (about 60-80 px lower and 60 px right of the current pose
   at board scale), so that "BEAR | MOOSE" and every tick stay fully visible.
2. **Square shorelines.** In s028, s029 and s037 the land is a hard vertical rectangle edge against the lake, in a different olive (#8f9a5a-ish) from the
   meadow green used everywhere else. Replace it with a curved or diagonal shore `poly` (meadow green, with a thin sand strip) so it reads as a
   lake edge and not a rendering seam.
3. **Moose standing on an invisible floor in deep water.** s032 and s035 have a second horizontal line under the surface. In s035 the bull
   stands on that line in open water with all four legs drawn, and the paddleboard rides the lower line instead of the surface. Remove the
   duplicate line. Draw the water `rect` **after** the moose from the surface down (wading: legs hidden, back and head above the water), and
   put the paddleboard on the real surface line.
4. **Doug standing on the lakebed with no gear.** In s044, s045 and s048, Doug stands on the bottom next to the moose/hoop, but s043 and s046
   have him on the paddleboard. Put him on the board at the surface in all three (continuity), or add `gear: ["scuba"]` if you want him down
   there (and then keep it consistent across s043-s048).
5. **s047: Doug stands on open water and the scoreboard floats in the lake.** Put Doug on the paddleboard, and put the board on the far shore
   strip (or raise it so its legs meet the tree line).
6. **Labels colliding with content.**
   - s009: "UP TO ABOUT 2 M AT THE SHOULDER" butts against the DOUG DEATHS box. Move it left or down (x ≤ 1500 right edge).
   - s044, s046: "18 FT? UNMEASURED" sits on the hoop backboard. Move it up about 70 px or to the left of the dashed line.
   - s106: "NPS: SAME" covers Doug's head. Move Doug down/right or stack the label under "ABOUT 56 KM/H" further left.
   - s236: the red circle cuts through the "0" in "KILLED: 0". Widen the ellipse (rx about 140, ry about 50) so the whole line sits inside it.
7. **s010: Doug overlaps the moose's front legs and bell.** He is the height reference and reads as stuck inside the moose. Move him to
   clear ground between the moose and the door (around x 1250).
8. **s080: Doug's head pokes out of the neighbour's front door** (he isn't in this beat). Remove him or stand him clear of the house.
9. **Detached speed lines.** In s105, s106 and s110 the three black `line` speed strokes float over the trees at the far left, well behind the moose
   (the moose was moved, but the lines weren't). Delete them, because `moose_charging` already has its own speed strokes, or re-anchor them just
   behind its rump.
10. **s100: the crossed-out RIP DOUG tombstone hangs in the tree crown over the moose's legs.** Put it on the ground (left of the trunk), or
    inside a narrator thought bubble.
11. **s121: `doormat` under the moose's front hooves** reads as a stray plank, because nothing in the narration sets it up. Remove it.
12. **s071: the narration says Doug "crouched down to introduce himself", but he stands waving.** Use `pose: "crouch"` (new), with the
    same x/y and facing toward the calf, and point the speech-bubble tail at the new head position (about 45 px lower at scale 0.4).
13. **Den mound floating in sky.** In s150, s152, s153 and s165 the den trapezoid sits on plain sky with no ground under it. Add the snow
    ground band (white #f4f8fb `rect` + black ground line) at the mound's base.
14. **s166: three labels on screen (AWAKE / HUNGRY / EXHAUSTED)** breaks style bible §7 AD rule 4 (max 2). Use one label,
    "AWAKE, HUNGRY, EXHAUSTED", or build them in so only two are ever up at once (drop AWAKE when EXHAUSTED pops).
15. **s204: the locomotive floats in mid-air.** Add the rail line and snow strip under it (copy them from s198), or drop it to the ground row.
16. **s056: "MAY - JUNE" spills past both edges of the calendar page.** Use a smaller size (about 26) or "MAY-JUN".
17. **Caption bar missing (style bible §7 AD rule 3, "must").** s146-s148 (inside The Hooves) and s258-s263 (inside The Highway)
    have `topbar: false`. Keep these sober cards **without** the death counter and scoreboard (that is correct for real deaths), but
    turn the caption bar back on (`topbar: true`) so the chapter strip stays continuous. s004, s124 and s220 are the spoken band
    headers before the first chapter name, so they are fine without it.
18. **s258-s263: six near-identical dark text cards in a row (about 40 s).** This breaks the "no same composition 5 times in a row" rule. Keep it
    sober (no Doug, no gags, no counter) but give it a quiet drawn anchor and two layouts:
    s258-s260 should show the empty night road (as in s248, with the moose silhouette removed) and the moose-crossing sign, with the text in the upper third.
    s261-s263 should show a moose and a deer side by side, large (moose_icon about 0.6, deer about 0.5, so both are at least 150 px tall). The current
    icons in s261 are about 40 px and can't be read.
19. **s225: the wolf icon sits on the map's top frame, half outside the map.** Place it inside the map on the ice between the Canadian
    shore and the island, at the end of the red dashed path.

## Recommended (non-blocking; director's call)
20. **Same-layout runs:** s207-s210 (four side-on locomotives in a row) could use a `zoom_in` on the cab/whistle for s208-s209.
    s211-s213 (three identical track perspectives) could add a slow push-in on s213 as the headlight grows. s022-s024, s109-s111 and
    s130-s131 are acceptable because something new pops in each shot.
21. **Doug parked in the bottom-right corner:** 60 shots put him at x ≥ 1700, y ≥ 900, scale 0.4 (e.g. s006, s007, s009, s054, s060,
    s062, s065, s084, s086, s096, s105, s159, s176, s181, s182, s184, s198, s222, s231, s250-s252, s264, s266). These are all legal, but
    in about 1 shot in 4 he looks like a watermark. Bring him into the scene (left side, or next to the subject) in at least every other shot of a run.
22. **s015:** the big blank white card with only the source line for the whole shot reads as a failed render. Either pop the claim text in at
    appear ≈ 0.7, or show only a small "ALASKA DEPT. OF FISH AND GAME" label without the empty card.
23. **s146-s148:** s148 adds nothing new, so this is a possible >6 s static stretch for QC (editor will flag). A small quiet addition (a
    campus building outline, low contrast) on s148 would avoid it.
24. **s196:** the `moss_patch` under the flattened cardboard antlers reads as a salad at small size. A plain trampled-grass tuft or no patch would read better.
25. **s172/s173:** the field guide overlaps the house front. Slide it about 80 px left/down so it sits on the snow.
26. s033/s036/s042-s048 swap the antlered bull (s032, s035) for the antlerless `moose_submerged`. That is acceptable because the asset was
    approved that way, but the illustrator could add short antler stubs later for continuity (optional, no re-render needed now).

## Routing
- **Director:** fixes 1-19 (all composition or shotlist edits; fix 12 uses the new `crouch` pose), plus the optional 20-26.
- **Illustrator:** nothing required. Optional item 26, and asset-pass item 3 (moose_head_surfacing ears) remains optional.
- Re-review: send only the changed shots (`python -m studio keyframes 024-moose-deadlier-than-bears --shots ...`), and I'll re-check them against this list.

---

# Keyframes round 2 (art director, 2026-10-21)

**Verdict: PASS.** I re-reviewed all 24 contact sheets (s001-s279 + endslate) after the re-render, plus the three thumbnails.
All 19 required fixes from round 1 are in, and the re-render introduced no new defects. Style, Doug on-model, zone palettes,
counter (195 to 203) and scoreboard (BEAR 5 / MOOSE 11) are all still consistent, and nothing is gory.

## Round-1 fixes verified
1. Scoreboard hand: RESOLVED. In s018-s020, s047, s065, s096, s118, s141, s167, s191, s214, s238 and s269 the glove sits below and right of the newest tick, and "BEAR | MOOSE" plus every tick can be read.
2. Shorelines s028/s029/s037: RESOLVED. The shore is now diagonal with a sand strip.
3. s032/s035 invisible floor: RESOLVED. There is a single surface line, the board sits on the surface and the bull no longer stands on a mid-water line.
4. s043-s048 Doug continuity: RESOLVED. He is on the paddleboard at the surface throughout.
5. s047: RESOLVED. Doug is on the board and the scoreboard sits on the far shore.
6. Labels: RESOLVED. s009 label clear of the counter, s044/s046 off the backboard, s106 "NPS: SAME" clear of Doug, s236 ellipse encloses "KILLED: 0".
7. s010: RESOLVED. Doug stands clear between the moose and the door.
8. s080: RESOLVED. Doug is out of the door.
9. s105/s106/s110 speed lines: RESOLVED. They are anchored behind the moose.
10. s100 tombstone: RESOLVED. It is on the ground.
11. s121 doormat: RESOLVED. Removed.
12. s071 crouch: RESOLVED. The new pose reads and the bubble tail points at the head.
13. Den mounds s150/s152/s153/s165: RESOLVED. They now have a snow ground band.
14. s166: RESOLVED. It uses one label, "AWAKE, HUNGRY, EXHAUSTED".
15. s204 locomotive: RESOLVED. It sits on rails with a snow strip.
16. s056: RESOLVED. "MAY-JUN" fits the page.
17. Caption bar s146-s148 and s258-s263: RESOLVED. The bar is on, and the counter and scoreboard stay off for the real-death cards.
18. s258-s263 static run: RESOLVED. s258-s260 show the night road and crossing sign, and s261-s263 show a large moose vs deer, all kept sober.
19. s225 wolf: RESOLVED. It is inside the map, on the ice.
Optional items also done: s015 now has a "?" on the card, s148 has a quiet campus and moose silhouette, s196 has no salad patch, and s172/s173 have the guide on the snow.

## Still open (non-blocking, carry to next episode)
- s211-s213 are still three identical track perspectives. Only the headlight grows, which is acceptable but flat, so the editor could add a push-in on s213.
- Doug is still parked bottom-right in many info shots (e.g. s249-s252, s105, s159). Next episode, bring him into the scene more often.

## Thumbnails (art pass; CD approval separate)
- **A hero (`thumbnail.png`): APPROVED, my first pick.** The head-on moose glare fills the frame, "WRONG ANIMAL" is heavy and readable at 168 px, and the small bear plus screaming Doug set up the twist. The downturned mouth fix holds. It is the one I'd click.
- **B peril (`thumbnail_b.png`): APPROVED, strong second.** The charging bull plus fleeing Doug on flat amber reads instantly at feed size, and "35 MPH" matches the script's 56 km/h. It is clickable, but less unexpected than A.
- **C grid (`thumbnail_c.png`): APPROVED, weakest.** It is clean and on-grammar, but at 168 px the six cells become small brown shapes on colour. Use it as a test variant only.
