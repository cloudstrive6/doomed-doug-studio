# 018 art review: new assets (art director)

Date: 2026-10-14. Scope: all 40 new drawings in `asset_requests.md`, judged from the previews (`assets/previews/018*`)
and from real keyframes rendered in context (s010 s027 s028 s030 s033 s038 s041 s047 s052 s053 s066 s073 s081 s100
s103 s106 s109 s110 s113 s117 s128 s140 s144 s148 s158 s159 s165 s188 s202 s219 s235 s260 s261 s262).

## Verdict: PASS (after the art director's own fixes below). There are 2 composition fixes for the director, and they don't block the asset gate.

### Fixes made directly in the library (not committed)
1. **`cassowary_head` (casque read as a hat).** The casque was a symmetric brown dome with a full black outline across its base,
   so on the hero close-up it read as a brown beanie/acorn sitting *on* the head. In an episode about Doug's cap, that is a real
   confusion. I reshaped it into a taller, back-leaning crest that runs down to the beak base, and replaced the black base line
   with a thin brown junction line, so the casque now grows *out of* the head. Exposed edges keep the 6 px outline.
   Peak moved from (-10,-280) to about (-26,-290). s028's "CASQUE" arrow still lands on it (verified), so no re-aim is needed.
2. **`cassowary_swallow_cap` (lump read as a bruise).** The lump fill was purple `#8a3a7a` with crimson `#c23a52`, which is a bruise
   palette. It is now neck-blue shadow `#2c5fae` with a crisp Doug-red `#e0201b` cap dome (3 px black outline) and a 7 px red brim.
   It reads as "a cap inside the neck", cartoon-clean, with no blood or bruise cue.
3. **`seedling_cap` (bathroom read).** I removed the two purple seed-husk lumps at the stem base. Small dark lumps on a mound at the
   foot of a plant are exactly the dung cue the CD banned. With clean soil, footprints leading in and "PLANTED", it reads as planted at
   phone size (s261/s262). **No fallback is needed. Keep `seedling_cap` for s261/s262/s265.** I updated the description too.

### Illustrator concerns: rulings
- **Casque shapes domed:** fixed on `cassowary_head` (see 1). On the full-body variants the casque is small enough that the dome
  reads correctly as a casque. They are approved as drawn. `casque_cutaway` stays a dome: it's a diagram, and the arrow/labels carry it.
- **Swallowed-cap shape:** fixed (see 2).
- **Thermal outlines on `#1b1b3a`:** approved as drawn. The black outline nearly disappears on the navy background, but the
  silhouette is carried by the fill contrast (`#4a5ad0` body, glowing yellow-white casque on the hot bird). This matches how a
  thermal image looks. The cold casque reads as cold. No change.
- **`seedling_cap` reads as planted:** yes, after fix 3.
- **`cassowary_wing_quills` black-on-black:** approved. On `#e6ead6` (s106-s108) the 4 quills sit against the light background, and only their
  roots touch the feather mass. On `#0d1b2a` as a silhouette (s109), the red glow disc puts the black quills on red, so it reads clearly.

### Per-asset status
| asset | status |
|---|---|
| cassowary_head | APPROVED (AD fix 1) |
| casque_cutaway | APPROVED |
| cassowary_thermal_cold | APPROVED |
| cassowary_thermal_hot | APPROVED |
| cassowary_swallow | APPROVED |
| cassowary_swallow_cap | APPROVED (AD fix 2) |
| cassowary_head_down | APPROVED |
| cassowary_running | APPROVED |
| cassowary_kick | APPROVED (no victim or contact; reads on the dark slate) |
| cassowary_wing_raised | APPROVED |
| cassowary_swimming | APPROVED |
| casque_fin | APPROVED (reads as "fin" in silhouette s158, as a casque in colour s159) |
| cassowary_on_nest | APPROVED |
| cassowary_icon | APPROVED (readable at 0.6 in the Opera House crowd) |
| cassowary_chick | APPROVED (scruffy, striped, beady eye, not cute) |
| cassowary_chick_brown | APPROVED |
| cassowary_double_feather | APPROVED. Optional polish: the side strands curl like fern fronds. Looser, straighter, hair-like strands would sell "hair-like" better. Not blocking. |
| cassowary_wing_quills | APPROVED |
| cassowary_wing_xray | APPROVED (claw pops inside the red ring, matches the x-ray set) |
| piano_keyboard | APPROVED |
| cassowary_plum | APPROVED |
| cassowary_footprint | APPROVED |
| narrator_hand | APPROVED (crude tier, no face) |
| cassowary_sign | APPROVED |
| sydney_opera_house | APPROVED |
| tree_stump | APPROVED |
| cassowary_nest | APPROVED |
| cassowary_egg | APPROVED |
| soccer_ball | APPROVED |
| balance_scale | APPROVED (pan tops line up with the bird and the rice in s144) |
| rice_bag | APPROVED |
| camper | APPROVED (crude tier, on Doug's tier, no cap) |
| rock_shelter | APPROVED |
| eggshell_fragments | APPROVED |
| ancient_person | APPROVED (a plain person, not a caricature) |
| chicken | APPROVED |
| paring_knife | APPROVED (clean steel, no blood) |
| deinonychus_foot | APPROVED (bone reads on `#2c3350` and `#1e2622`) |
| plaster_claw_cast | APPROVED |
| seedling_cap | APPROVED (AD fix 3) |

## s047 cap-off-for-shade: APPROVED as a one-off capless upright Doug, with a placement fix
The beat ("offered the bird his cap for shade") is the joke. The cap stays in frame, and s048 puts it back on. This fits the
capless-upright exception in the art bible, and it is logged in `decisions.md`. It is not a precedent.

## Fixes for the director (composition, not blocking the asset gate)
1. **s047:** the cap floats about 100 px above Doug's hand, so it reads as the cap flying off. Put it *in his hand* at his own size:
   `doug_cap` → `"x": 1000, "y": 546, "scale": 0.7` (was 1010/470/0.45). The rim then rests on his pointing fingertips and
   the dome overhangs the bird's casque like a sunshade. I test-rendered this and it reads clearly. Keep `doug_cap` listed before `cassowary`, so the casque
   draws in front of the brim.
2. **s066:** `narrator_hand` at scale 0.8 covers the right half of Doug's face, and the hand reads bigger than Doug. Scale it to about 0.6
   and move it right/up (about x 790, y 740) so the fingertips stop at his raised hand/plum and his eyes stay clear.
3. Advisory, s260: at bird scale 0.62 the cap lump is about 20 px tall. Consider scale 0.8 or a slow `zoom_in` on the neck
   (lump at local (100,-470), flipped), so the outro gag lands at phone size.

---

# Keyframe review (art director, 2026-10-14): FAIL (6 small fixes, all director/composition)

Scope: all 265 keyframes (`build/contact/sheet_01..23.png`; single frames checked for s135, s216).

**What passes.** The style is consistent across all 11 items. Doug is on-model everywhere except s135 (fix 1). The cap is visible
in every frame where he is alive or a ghost, and s047 stays the logged one-off. Two-tier rendering holds (crude Doug,
scientists and campers; detailed cassowary, foot, casque, x-ray wing, Deinonychus). The background ramp darkens one step
per item (light green Boom/Helmet/Plum, then Road `#8fb07a`, Dad `#789f66`, Sprint brown, First Pet/Toe dark green, Kick
near-black), and diagram cards follow it (cream, then grey-mint, then dark). Silhouette-then-reveal is used at s014, s109,
s137 and s182. Every death is a dust cloud, a splash or a cut-away, so there is no gore. The claw never touches Doug. The real-death
sober cards (s240-s245, `topbar: false`, no Doug, no counter) are the CD-sanctioned exception in `decisions.md` and are
approved as staged. Layout variety is good: forest wides alternate with map, piano, pie chart, scale, timeline, x-ray, split
panel, Opera House and beach builds. Long runs on one background (Road s088-s095, Swim beach s148-s153) are build-up groups
that add an element on every shot, which is allowed.

## Fixes (route: director)
1. **s135:** Doug auto-inks **white** on the Dad mid-green (`#789f66`), so his body lines almost vanish. Add `"ink": "#000000"`
   to the `doug` element.
2. **s216:** the "DAGGER-LIKE" wordart sits on the black feather fringe at the top of the foot (text bottom about y 335, fringe top
   about y 330). Move the wordart to clear dark space at about `"x": 1300, "y": 250`. That keeps it under the counter, above the "TOE 2" label, and off the foot.
3. **s258-s261:** these shots are still The Kick (the coda runs before the outro line "Doug deaths: one hundred and fifty-four"), but they
   have `topbar: false`. Style bible 7.3 requires the caption bar on every segment frame. Restore the "THE KICK" top bar on
   s258, s259, s260 and s261. The outro (s262-s265) can stay bar-free.
4. **s084:** the bare white disc reads as a missing or broken asset for the whole shot, until s085 fills it. Give it content now: put
   a `cassowary` icon (scale about 0.35) or a big "110" text in the centre of the circle, or start the pie with its outline only (thin black ring, `fill` = background).
5. **s190:** the label "18,000 TO 6,000 YEARS OLD" is 5 words (the max is 4). Change it to `"18,000-6,000 YEARS"`.
6. **s041:** the wordart "THE MOST" has no noun, so it reads as a fragment. Change it to `"MOST HEAT"`, which echoes "heat" in the same line.

## Advisory (not blocking)
- s143: the balance beam is level with one pan empty. If the `balance_scale` asset or the scene allows a tilt, let the bird's pan sit lower and level it at s144 when the rice arrives.

Re-run `python -m studio keyframes 018-every-cassowary-reason --shots s041,s084,s135,s190,s216,s258,s259,s260,s261`. If those
frames match the above, the keyframes PASS with no further review round needed for the remaining shots.
