# Visual review: 011-every-animal-fight

## Round 1: pre-render keyframes (2026-10-09)

Scope: `shotlist.json` (285 shots), `build/contact/sheet_01..24.png`. s001 shows "(thumbnail pending)", which is expected at this stage and not counted against the episode.

VERDICT: FAIL

Three required fixes, all small: one continuity break that undercuts a narrated payoff, one label collision, and two runs of near-identical frames. Everything else is clean. Drawings are recognisable, Doug is on-model throughout (red cap, white head, readable on every background including the night wolf set and the dark-red elephant set), the counter is correct (93 -> 94 kangaroo, 95 wolf, 96 cassowary, 97 chimp, 98 croc, 99 polar bear, 100 elephant; goose, cat and gorilla survived), all on-screen text is spelled correctly and inside frame, and the chapter labels and title cards are consistent.

### Policy checks
- **Gore / violence:** pass. Every death is shown as the dust cloud, then X-eyes Doug lying flat with his cap knocked off, plus ghost Doug (s072, s098-099, s124-125, s153, s213, s242-243, s279). There is no blood. The open mouths (gorilla s166/s171-175, polar bear s218/s221, croc s192-195) have plain red or tan interiors with no blood. The 2022 kangaroo death (s068) is a map dot, the Maasai spearing (s258) is shown as arrows meeting at a waterhole with no spear, the chimp killings (s145-149) are flat silhouettes, and the seal in s234 is whole.
- **Kids-show tone:** pass. The "hi friend?" bubbles are naive in a deadpan way, not nursery. There are no baby-style framings, mascots or sing-song text.
- **Gorilla walk-away (s177-s184):** pass. It does not read as survival advice. Doug's chest beat is framed as pathetic ("tap tap" on a cardboard box, s178). The verdict in the guide is MAYBE, not a tick (s181). The narrator's pre-drawn death page (s182) and the gorilla's own "~~~ = SMALL" judgement (s183) make it clear the gorilla chose to leave, and that Doug did nothing right. No frame shows a "DO THIS" style instruction.
- **Cat-bite bar (s043-s044):** pass. The 3-cell bar with 1 red cell plus "1 in 3 -> HOSPITAL" reads correctly in 1 s. "3 YEARS" sits above it, and "FIGHT" is crossed out in s044. There is no wound, blood or bite imagery, and Doug's bandage (s039) reads as a wrapped hand at full size.

### Required fixes
1. **s025, s026 (director): goose continuity.** In s021-s024 the goose walks off wearing Doug's cap (`canada_goose_cap`) and Doug sits with `cap_off`. In s025-s026 Doug is suddenly wearing the cap again and the goose is bare (`canada_goose`). That contradicts the narration "the goose kept the pond, the dignity and the last word ... a clean sweep". Change: in both shots set Doug `gear: ["cap_off"]` and swap the asset to `canada_goose_cap`. Keep it on the pond and keep the labels. The cap can come back at the s027 House Cat chapter card as it does now.
2. **s208 (director): label collision.** Doug's cap overlaps the bottom-right corner of the red "27 FATAL" box. Change: move Doug about 120 px right and down, or move the "87 ATTACKS" / "27 FATAL" stack up and left about 60 px, so they don't touch.
3. **s274-s278 and s230-s233 (director): variety.** These are two runs of 4 or more near-identical compositions.
   - **s274-s278 (elephant ending):** five shots in a row use the same layout: same frontal elephant at x1300, small Doug left, sunset left. Only the bubble or label changes. Change: make s275 ("listened very carefully") a close-up of the elephant's head and ear with sound arcs, with Doug small at the edge. Make s277 ("It was right.") a tighter two-shot or a low angle. Then keep s276 and s278 in the current wide layout, so the s278 -> s279 death cut still lands.
   - **s230-s233 (polar bear, "worst part" beat):** four shots in a row put Doug left and the side-view bear right on the same ice horizon. Change: make s232 ("the hungry one") a close-up of the bear's head, or show the bear with the empty FOOD meter from s231 enlarged, or just push in on the bear. Then s233 can keep the wide shot with the crossed-out "DEFENDING".

### Recommended (not blocking)
4. **s028 (director):** the cat's ear clips the "M" of "MOST CONFIDENT". Move the cat about 40 px down or move the text about 30 px right.
5. **s083 (director/illustrator):** the ELK, BISON and MOOSE labels float, but only the moose is drawn. Either point each label at an animal (add the existing library elk/bison if there are any) or keep only MOOSE plus a "+ ELK, BISON" line.
6. **s052 (director):** the red down-pointer lands right on the red figure's head and reads a little like a spike through it. Stop the arrow about 20 px above the head, or use a bracket or ring instead.
7. **s266 (director):** the red arrow points down from the low-frequency wave to the high-frequency wave under the heading "PITCH UP". At a glance it reads as "pitch down". Use a sideways arrow, or put the high-pitch wave above the original wave.
8. **s137 (director):** the 27 KG suitcase floats above the chimp, whose arms are down. Give the chimp a lifting pose if the asset has one, or place the suitcase in its hands or on its back. s136 works because Doug's arms are up.
9. **s217 (art director, optional):** the red-speckle threat aura behind the bear silhouette is denser than the cassowary's (s103). It is fine at full size, but at small size it could read as a red spray. Consider dropping its density or tinting it toward grey-red.

Routing: fixes 1-4 and 6-8 go to the director (shotlist edits, then re-key s025, s026, s028, s052, s137, s208, s230-s233, s266, s274-s278). Fix 5 goes to the director, plus the illustrator only if new assets are wanted. Fix 9 goes to the art director. Re-screen only the re-keyed shots in round 2.
