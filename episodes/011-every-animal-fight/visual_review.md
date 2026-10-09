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

## Round 2: re-keyed shots (2026-10-09)

Scope: the 20 re-rendered shots on `build/contact/sheet_01..02.png` (s025, s026, s028, s052, s055, s083, s123, s137, s146, s154, s189,
s207, s208, s209, s217, s232, s264, s266, s275, s277), with full-res checks of s025, s028, s052, s123, s137, s154, s189, s208, s232, s275 and s277.
I also checked continuity against `shotlist.json` (s024-s027 Doug gear and goose asset; s274-s279 narration).

VERDICT: FAIL

All of the round-1 fixes landed. Two small new defects in re-keyed shots block the pass: a text collision (s154) and a stray line on Doug in the new
s232 close-up. Each one is a one-element shotlist edit. Re-key s154 and s232 only.

### Round-1 fixes: verified
- **1. s025/s026 goose continuity: fixed.** Doug has `cap_off` and the goose is `canada_goose_cap` in s024, s025 and s026. The cap returns at the s027 chapter
  card. s025 is down to 2 labels (POND on the pond, DIGNITY + LAST WORD). The goose's cap is small at 1080p but it reads as red on the head, and it matches s021-s024.
- **2. s208 label collision: fixed.** The 27 FATAL box bottom is at about y 703 and Doug's cap top at about y 745, so they are clear.
- **3a. s274-s278 variety: fixed.** s275 is now a head-and-ears close-up that fills the frame, with small Doug bottom-left and white sound arcs going toward the elephant.
  "Listened very carefully" reads in 1 s. s277 is a tighter two-shot: large smiling Doug, a green tick over him, and the elephant at 1.1 scale. It reads as
  "Doug really is harmless: correct", which sets up "It did not matter" (s278) and the s279 death. The run is now wide / close / wide / two-shot / wide.
- **3b. s230-s233 variety: fixed.** s232 is a 2.6x push-in on the bear's head with tiny shocked Doug left, so it breaks the run. See fix 2 below for one new problem.
- **4. s028: fixed.** The cat sits at the bottom-left of the card, well clear of "MOST CONFIDENT".
- **5. s083: fixed.** There is one label, "MOOSE + ELK + BISON", over the moose.
- **6. s052: fixed.** The red arrow tip stops about 25 px above the red figure's head and reads as a pointer.
- **7. s266: fixed.** The high-pitch red wave is now above the black MEN wave, with an up arrow between them that agrees with "PITCH UP".
- **8. s137: fixed.** The 27 KG suitcase rides on the chimp's back.
- **9. s217: fixed.** The threat aura behind the silhouette is now a sparse grey speckle and no longer reads as red spray.
- **Art-director shots, also clean:** s055 (FEMALE / MALE 2x, 2 labels), s123 (bag tipped on the ground, seeds spilling, label upright), s146 (blue dots,
  10th chimp unmarked, nothing reads as blood), s189 (cream diagram, croc and car on separate baselines, 6 M line clear, about 150 px gap), s209 (about 100 px of
  sand between snout and Doug), s264 (BOYS clear of the sun), s207 (2 labels plus map, clean).
- **Policy:** no gore and no kids-show tone in any re-keyed shot. The s232 bear is a neutral side-on head with no open mouth.

### Required fixes
1. **s154 (director): cap over the citation.** The `doug_cap` asset at (800, 745) sits on the white "PNAS 2017" card and covers the "NA" of "PNAS". This was
   present in round 1 and I missed it. It is text overlapped by a drawing. Change: move the cap onto the log next to the card, at about x 960, y 790
   (scale 0.35, sitting on the log top), or move the card to x 520 and keep the cap where it is. Check that no part of the cap touches the card.
2. **s232 (director): stray line on Doug.** The ice-crack line `[[200, 820], [420, 812]]` starts exactly at Doug's cap brim (Doug is at x 170, scale 0.4).
   It reads as a long pole sticking out of his cap or face. Change: delete that line, or move it to `[[330, 960], [560, 952]]`, clear of Doug.

### Recommended (not blocking)
3. **s232 (illustrator/director):** at 2.6x the `polar_bear` asset shows two artefacts: the near foreleg's black outline pokes above the chest line as a
   small spike (about x 1355, y 810), and the grey far-leg stroke crosses the body diagonally (about x 1565,670 to 1460,960) like a crease. At this
   scale it reads as a stray line. Moving the bear will not hide it, because the spike sits mid-frame. The fix is in the asset: the illustrator
   ends the foreleg outline at the chest line. The grey stroke can stay. It is invisible at the asset's normal 0.85 scale, so this does not block s232.
4. **s277 (director, optional):** the green tick at (494-626, 400-520) floats in the sky band. It would tie to Doug more clearly about 60 px lower, nearer his head.

Routing: fixes 1-2 go to the director (re-key s154 and s232). Fix 3 is optional and goes to the illustrator (`polar_bear` asset). Fix 4 is optional and goes to the director. In round 3 I will re-screen only s154 and s232.

## Round 3: re-keyed shots (2026-10-09)

Scope: full-res `build/keyframes/s154.png`, `s232.png` and `s277.png` (rendered 09:36, same time as commit 051581f), with a zoomed crop of the s232
foreleg. I also checked the shared `polar_bear` asset edit by re-keying ep 008 s195, s198, s208, s214 and s220 (scales 0.3 to 1.0), with a zoomed crop
of the s198 chest/foreleg joint.

VERDICT: PASS

### Round-2 fixes: verified
- **1. s154 cap over citation: fixed.** `doug_cap` now sits on the log top at about x 925-995, y 778-802. That leaves about 35 px of clear log between the
  cap and the right edge of the "PNAS 2017" card, and "PNAS 2017" reads in full.
- **2. s232 stray line: fixed.** The ice-crack line at Doug's cap brim is gone. Doug (shocked, cap on, on-model) stands alone at the left with clean space
  around him. The close-up still breaks the s230-s233 run, and "THE HUNGRY ONE" reads in 1 s.
- **3. s232 foreleg spike (optional): fixed.** The new chest fill patch hides the foreleg outline, so it now starts at the chest line. Only a ~5 px
  square end-cap is visible at about x 1352, y 855, and it is not noticeable at 1080p. The grey far-leg stroke is unchanged, as allowed in round 2. The one
  short pale ice-crack line left of the leg (about x 1250-1345, y 900) reads as ice, not as a stray stroke.
- **4. s277 tick (optional): fixed.** The green tick moved down 60 px (bottom at about y 585). It now sits just above and right of Doug's cap (top at about
  y 655), so it clearly belongs to him. It overlaps the edge of the sun a little, which is fine.

### Shared asset check (ep 008)
- The `polar_bear` edit does not break anything in ep 008. In s195, s198, s208, s214 (two bears, 0.9 and 0.7) and s220 (0.3), the chest/foreleg joint is
  clean, with no gaps, holes, or fill showing past the outline. The silhouette, radio collar (s208) and -22% comparison (s214) are unchanged. Re-keying ep 008
  is not needed. If it has already rendered, the new asset only removes a hidden spike.

### Policy
- No gore and no kids-show tone in the three shots.

Routing: none. Keyframes for 011 are cleared for render from the visual side. The post-render screen (samples, qc.json, thumbnail, shorts) follows the build.
