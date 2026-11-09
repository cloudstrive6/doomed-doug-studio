# 041-grizzly-wont-fight: visual review

## Round 1: pre-render keyframes + thumbnails (2026-11-09)

Scope: contact sheets 01-17 (s001-s194 + endslate); individual keyframes s004, s016, s017, s057, s079, s085, s114, s115, s140;
thumbnails A/B/C at 1280x720 and 168x94. The keyframes were rendered before the art director's in-progress, uncommitted
shotlist.json edits, so re-render (`keyframes --shots`) and re-check any shot those edits touch.

VERDICT: FAIL

Generally solid: Doug is on-model and readable in every shot. The death cards are cartoon only, with no gore. The tone is adult, the counter runs 315 to 322 correctly, the bear's-cost tag updates per chapter, and the chapter titles are spelled right. The fixes below are blockers (B) or should-fix (S).

### Fixes

1. **B - s016, s017 (illustrator + director).** The pizza-table drawing is garbled. The 12 people are two overlapping rows of 6 squeezed *under* the tabletop, so they read as 6 two-headed figures. In s017 the box removal leaves a rectangular hole in the tablecloth, a floating strip of box lid hangs above the table, and the knives disappear. Fix: seat 6 people on each side of the table, both rows visible, every head above the table edge. Keep the knives in s017. Remove the box cleanly so the table and cloth are intact. Also "GO FIRST??" has a doubled "?" (wordart "?" plus a red "?"); keep only one.
2. **B - s090, s091, s093 (director).** The picture contradicts the narration. Every `moose_icon` has antlers, so these shots show bears killing *bulls*, but the section's point (s094-s096) is that the kills are cows and the bulls get left alone. Fix: use an antlerless (cow) moose icon. In s093, use 28 antlerless and 4 antlered icons to match "almost nine in ten were female". Ask the illustrator for a `moose_cow_icon` if none exists.
3. **B - s085, s086 (illustrator / director).** The moose "front leg" is a free-floating limb with a jagged, torn-looking top. With Doug grimacing beside it, it reads as a severed leg, which is too close to the dismemberment rule. Fix: show the whole bull moose with the front leg highlighted (red circle or arrow plus the FRONT LEGS label), or crop the frame so the leg runs off the top edge into a body.
4. **S - s057 (director).** The bear forearm ends in mid-air at x≈1700 with a flat cut edge, so it reads as a detached limb. Fix: extend the arm past the right frame edge (x ≥ 1940).
5. **S - s115 (illustrator).** The "bison calf" is a tiny orange blob that reads as a dog or piglet. Fix: draw a recognisable calf (reddish-tan, small hump, short legs) at about 2x scale, or put it next to a cow bison for context.
6. **S - s114 (director).** The calendar text "MARCH" is clipped by both sides of the calendar page. Fix: reduce the font size to fit, as APRIL fits at the same size in s115, or widen the page.
7. **S - s186-s189 (director), variety.** Four near-identical compositions in a row: the same orange trail background, bear on the right, Doug on the left, wordart in the sky. s183 and s184 also use it, with only s185 breaking the run. Fix: change at least s187 or s188. For example, push in to a close-up of Doug's offended face for s188 ("OFFENDED"), or show the bear's rear view disappearing into the trees for s187.
8. **S - s172, s174-s177 (director), variety.** Five near-identical US-map frames (s173 changes only the background). Fix: give s174/s175 a different treatment, for example the 50,000 → 700-800 drop as a bar or bear-icon count, or zoom the map in on the two remaining populations for s176/s177.
9. **S - s004, s077 (illustrator, `price_tag` asset).** The tag's grommet hole sits on top of the first letter ("D" of DINNER, "B" of BONES). Fix: add left padding to the tag text, or move the grommet left so it clears the text. FACE, CUBS and LIFE also sit close to it.
10. **Minor - s103, s104 (director).** The carcass is the pale generic elk carcass, but the narration is about bison. Use a dark-brown bison carcass (humped outline) so it reads as bison.
11. **Minor - s165 (director).** "The tiger is the one animal here that hunts the bear" is shown with a bear alone on a trail. Add the tiger (or its silhouette) stalking at the frame edge.
12. **Minor - s126, s130 (director).** These are cub-killing shots with no cubs on screen. The red arrow in s126 points from the male to an adult bear. Add a cub (behind the mother) as the arrow target. No contact, keep it implied.
13. **Minor - s121, s122, s128, s138 (director).** Doug's feet stand in the river band. Raise Doug to y ≈ 1000 or above the waterline.
14. **Minor - s134, s135 (director).** The "ABOUT 780 M" label covers the second house, and the map border runs under the DOUG DEATHS counter. Move the label right or below the line, and shrink the border to x ≤ 1340.
15. **Minor - s018/s019 (director).** Same split-panel composition twice in a row. Acceptable, but consider reframing s019 as a single wide shot of the bear walking off with the carcass past the wolves.

### Thumbnails (graphic designer): PASS with notes
- **A "NOT WORTH IT"** (bear + tiger + Doug): the strongest of the three. Readable at 168x94, the threat is obvious, and it matches the title. Notes: Doug's cap brim touches the tiger's nose (tangent), so move Doug about 30 px left. The tiger's white cheek ruff has a spiky outline that at feed size reads like a cone collar or an open jaw; soften it.
- **B "TOO COSTLY"** (porcupine-suit Doug + porcupine + bear): readable. The quill-suit Doug and the porcupine merge into one brown mass at feed size. Separate them with about 40 px of background.
- **C "IT FEARS US?"**: readable, one focal point. The bear's snout is slightly cropped at the left edge, which is fine. It shows a heart bubble instead of the planned "hi friend?" bubble, which is fine and reads better small.
- None of the three is misleading against "Why a 300 kg Grizzly Still Won't Try to Kill These Animals".

### Checked OK
- Death cards s026, s074, s100, s120, s144 (wordless beat), s164, s190: cartoon only, no blood, cap gag present.
- s185 polar bear is the established 031 callback ("the last bear came for him on purpose"), consistent with the series bible.
- s066 (cougar deaths) and s021 (cubs): silhouettes only, sober and not graphic.
- Endslate: arrow points to the video slot and the subscribe circle is clear.

Post-render checks (samples, qc.json, shorts) are still to come; nothing was rendered yet.
