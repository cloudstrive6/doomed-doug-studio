# 047 Wolverine Snow Climb: Visual Review

## Round 2: pre-render keyframes re-screen (2026-11-14)

Scope: refreshed `build/contact/sheet_*.png` and the full-size `build/keyframes/` for the changed shots s006, s015,
s019, s040, s126, s127, s130, s131, s145, s146, s162, s175, s177, plus the neighbouring runs (s142-s147,
s169-s178). s001 skipped (thumbnail pending). I rendered s162's full 1920x2160 pan canvas and s175 without the
blackout (elements with appear < 0.6) to check the pan start and the pre-cut state.

**VERDICT: PASS**

### Round 1 required fixes: status
1. **s015**: FIXED. "200,000 KR" is fully legible and the string attaches at the tag's eyelet, clear of the text.
   A kit is now on the den pad with the tag tied to it (see advisory A1).
2. **s006**: FIXED. The wolverine (bottom centre-right) and Doug (far right) no longer touch.
3. **s040**: FIXED. "WIDE ENOUGH" sits in open sky, clear of both pine crowns.
4. **s162**: FIXED. On the pan start, `wolverine_climbing` sits on the left face and is unobstructed. The red
   arrow starts beside it and runs up the face to the snowcap. "STRAIGHT UP" is on the right in open sky.
5. **s143-s146 variety**: FIXED. s145 is now a close-up of the den chamber (WARM thermometer inside, Doug + COLD
   on the surface, COLD GROUND below). s146 is a surface view with the FEB - MAY calendar. Only s143/s144 share
   the same section, which is within the limit.
6. **s131**: FIXED. The divider starts below the "THE SNOWSHOES" tag.
7. **s019**: FIXED. The coloured wolverine with the pale side-stripe is used, so the threat reads at once.

Round 1 advisories also resolved: s126/s127/s130 reindeer are now sunk into the crust (with snow-clump rims in
s126/s127). s175 shows the wolverine going over the summit with the paw-print trail, a "OVER" arrow and Doug on
the face, and no cap on the summit. s177 is re-framed closer (big mountain, "363", cap + arrow, ghost Doug), which
breaks up the s176-s178 run.

No new blocking issues. Doug is on-model, the counter steps 362 -> 363 across the s175 cut, there is no gore, and
the tone is not a kids' show.

### Advisory (does not block; fix if time allows)
- A1. **s015** (illustrator): the kit is a solid black silhouette with a tail (ellipses at about 982,952 /
  1040,952), so at a glance it reads as a rat or a shadow, not a wolverine kit. If time allows, draw a pale
  grey-fluffy kit with shut-eye lines, or reuse `wolverine` at scale about 0.18 with closed eyes.
- A2. **s015** (director): the big red `question_mark` at 1660,600 sits on top of the right-hand pine, and Doug
  already has his own small "?". Drop it or move it into open sky above Doug (for example 1560,700).
- A3. **s130** (director): the two break-through crack marks still read as stray "< >" chevrons under the
  reindeer. Replace them with a snow splash or delete them. The sunk reindeer and the SINKS arrow carry the beat
  without them.
- A4. **s145** (director): the `altitude_stake` HUD tip lands right on the den's surface entrance (about x 1405),
  which clutters that spot. Consider moving the cutaway entrance a little left. A small grey triangle (distant
  peak) also pokes above the surface at about x 1000-1150 and looks like a stray shape.
- A5. **s177** (director): the line is "The cap made the summit", but the cap sits about a third of the way down the
  far slope. Moving `doug_cap` up to just over the peak (for example about 760,140, with the arrow re-aimed) would
  make the payoff literal.
- A6. **s162** (editor, check in render): the HUD (deaths label/stake) is in canvas coordinates at the top of
  the 2160 canvas, so it scrolls in during the pan-up rather than staying fixed. Make sure this looks
  intentional in the draft render.
- Round 1 advisories that were not touched (s012, s043/s053, s055, s008, s088) still apply as nice-to-haves.

---

## Round 1: pre-render keyframes (2026-11-14)

VERDICT: FAIL. 7 required fixes (s015, s006, s040, s162, s143-s146 variety, s131, s019) plus advisories. All
were addressed in round 2 (see above).
