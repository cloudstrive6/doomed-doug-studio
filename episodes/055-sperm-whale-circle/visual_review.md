# Visual review: 055-sperm-whale-circle

## Round 1: keyframes (pre-render), 2026-11-22

Scope: all 203 shots in `build/keyframes/` (re-tiled locally; `build/contact/sheet_01.png` holds only s152, so the
contact sheet is stale or partial and must be regenerated for the full episode). s001 shows "thumbnail pending",
which is expected at this stage.

VERDICT: FAIL

### What passes
- **Gore:** clean. The kill (s190-s191) is a broken ring and a dashed empty slot. The injured survivors (s193-s195)
  are drawn as a thinning ring on black, with no wounds and no blood. All six Doug deaths (s044, s065, s085, s129,
  s149, s198) are cartoon beats: a cap left behind, X-eyes, a splash. There is no realistic violence.
- **Kid appeal:** acceptable. The school buses (s098), daisy (s089-s093), day-care rota (s035-s040) and "toddler"
  car (s036) all illustrate the narrator's metaphors in flat MS Paint style. None of them use nursery framing.
  The dark ending (s192-s200) keeps the adult tone.
- **Doug:** on-model throughout (red cap, white head, whale costume). He reads against every background,
  including the navy ring shots. The counter runs 402→408 with no gaps, and s106 "405 deaths" matches it.
- **Pictures match the narration** in nearly every shot. Maps are labelled correctly (Caribbean, Galápagos,
  Gulf of Mexico, BC/Alaska). There is no spelling error in on-screen text.

### Required fixes
1. **s058 (illustrator):** The "NURSERY" sign text is clipped by the bottom edge of the board, so the lower half of
   the letters is cut off. Enlarge the board or shrink/raise the text so it sits fully inside.
2. **s098 (director):** The "NOSE TO NOSE" caption overlaps the lower-right school bus. Move the caption to the
   lower-left empty area, or below the ring, with clear space around it.
3. **s176 (illustrator/director):** The location circle sits on the Southern California / Baja coast. The narration
   says "about 130 km off central California". Move the circle north to the Monterey/Big Sur latitude and offshore
   into the ocean.
4. **s198 (director):** The frame is fully black except for the HUD. It will read as a dropout and may trip the
   black-frame QC. Keep the dark tone but add a subject, for example the empty ring outline with the cap alone in
   the centre, or a fading ring of dashed slots.
5. **s125-s127 (illustrator/director):** The two whales meeting nose-to-nose fuse into one two-tailed creature at
   normal viewing size. Add a visible gap or a slight vertical offset so they read as two whales. The "HELPING"
   sign on Doug is about 10 px text and unreadable. Make the sign about 2.5x larger or drop it.
6. **Variety: runs of 4 or more near-identical top-down ring compositions (director).** The premise is the ring,
   but these runs are long enough to go stale. Break each run with at least one different framing, such as a
   water-level side view, a close-up of one whale or a fin, a ship/binocular POV, or a slow push-in:
   - **s099-s102:** ring with Doug on the right, four in a row. Make s099 a close-up of Doug's "?" face, or
     s102 a side view of whales shoulder to shoulder.
   - **s104-s109:** ring with Doug in the centre (s104, s105, s106, s108 and s109 are near-identical). Make
     s105 a ring-closing animation or a low side view, and s108 a close-up of Doug in the middle looking outward.
   - **s156-s162:** ring with orcas off to the right, seven in a row. Turn s159 ("attacked straight away") into
     a tight close-up of the pair with fins converging, and s161 into the ship POV (reuse the s155 ship).
   - **s164-s169:** ring with orcas, six in a row. Make s166 "NEVER" a close-up of a single adult whale's eye
     or head.
   - **s178-s182:** ring counts, five in a row. Make s180 ("about a dozen") the binocular/ship view with
     fins on the horizon, then return to the top-down view for s181-s182.
   - **s186-s191:** ring, six in a row. Make s187 ("Nobody saw a calf") a water-level side view with the
     empty gap in the middle, or a single close-up.
7. **Contact sheets (editor):** Regenerate `build/contact/sheet_*.png` for all 203 shots after the fixes, so the
   next round reviews the real sheets.

### Notes (no change required)
- The minimap changes per chapter: blank in Ch1, "THE RING" dots later, and an Americas map in "The Other
  Hunters". This is intentional. Check that the Ch1 empty minimap (s004-s022) is deliberate and not a
  missing layer.
- s063 and s073: the ear icon is small but readable at 1080p.
- s203 "410?" is a subscribe CTA, not a withheld-payoff "???" card. The ending pays off the title (s003 setup →
  s188-s200).
