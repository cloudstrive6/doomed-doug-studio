# 016 decisions (creative director)

## 2026-10-12: script gate
- Inputs: `script.md` (draft 2 plus the E1 kicker fix), `script_review.md` (round 2: FAIL on E1 only, with "passes once fix 1 is applied, confirm the changed line only"), `facts.md`.
- **E1 confirmed fixed.** Line 366 now reads "The lowest ground on any continent is down here, under the ice, and part of it slopes the wrong way." That is limited to the sourced claim (deepest point on land, retrograde bed on one flank, Brancato 2020) and matches the closing line. Optional fix 2 is applied too ("Nobody should ever trust a cave this comfortable.", 8 words).
- **Order: as briefed.** Vostok is item 10 (3,766 m, death 138), and Denman is the boss (meter 4,000, "more than four kilometers", Thompson et al. 2023 citing BedMachine). The meter is monotonic from 0 to 4,000 m, and every value has a source or a stated basis in the header comment. The Blood Falls 400 m flash is limited to the twist shot.
- I spot-checked facts.md against the lines that matter most: five storeys, 1.5-2 Myr, "at least twice as salty", the Manhattan cavity, farthest-south fish, Whillans 1.8 m / 52 km² / "as crowded as a lake or the ocean", the Ellsworth 300 m link failure and "up to a million years", Fuji and the East African Rift density, the Vostok 15-25 Myr range and Kennicutt's warning, and "only trenches go deeper". Every claim is sourced and attributed where it is contested (Erebus DNA "not proof", Vostok age range, Denman "an estimate", "Doomsday" as a media nickname).
- Would I click and keep watching? Yes. "It isn't blood" lands at about 0:19, the first death comes at about 1:05, and the twists get stronger as the ice gets thicker. The best beats are "Somebody was.", "The ceiling got a closer look at Doug." and the Ellsworth hole closing behind the crew. There is no climate sermon (one attributed number each for Thwaites and Denman), no penguins or cute wildlife, and no safety or medical advice.
- Policy: clean. Blood Falls is rust and says so. Mercer's remains are tiny shells. Every death is crush, freeze or flood, cartoon only.

**Non-blocking notes for downstream (director / art director / titler):**
1. **Three ice-encasement deaths** (134 sponge frost block, 137 Ellsworth borehole column, 138 Vostok mid-wave pillar) all end with "the cap on top". Give them different silhouettes so they don't read as a repeat: 134 is a squat seated block with frost, 137 is a tall thin column inside the borehole walls, and 138 is a splashing wave shape frozen mid-surge. Vostok must not echo 012's amber "preserved" variant. Keep Doug a cartoon X-eyes shape inside opaque blue ice, not a visible body.
2. **Boss continuity:** in the death shot the cap stays on the canyon floor, and in the closing shot the rope comes up with the cap on its end. The director should add a beat where the empty rope end drops and snags the cap (or cut straight to the cap on the hook) so the two shots agree.
3. **Title:** "Every Layer" sits next to 001's "Every Layer of the Ocean". The titler checks this against the feed, as the brief asks, and may lead with the T2 alternate if the two would appear side by side.
4. The callback to 004 ("The last time Doug was in Antarctica, he stood on top of it.") is the only callback. Don't add a 012 crevasse callback in the visuals.

SCRIPT: APPROVED

## 2026-10-12: art + package gate
- Inputs: `visual_review.md` (round 3 PASS, 274 keyframes, 23 contact sheets), `art_review.md` (assets: all 43 APPROVED; keyframes round 3: 4 director fixes), `shotlist.json`, `metadata.json`, thumbnails A and B with `build/thumb_compare_168.png`.
- **Art-director round-3 fixes verified in the shotlist:** SEA LEVEL is at x 330 and the s261 camera ends at [1008,500,1.1]. LIFTS OFF AND FLOATS is at y 320 (s263). LOWEST GROUND and UNDER THE ICE are at (600,540) and (600,620) (s266). All 16 counter safe-area camera centres match the art director's table exactly. The keyframes and contact sheets were re-rendered after the last shotlist save (18:04 → 18:05). I looked at s263 and s266 at full size: the labels are clear of the outlines and the arrow is continuous. `python -m studio validate` returns OK.
- **Thumbnail: A wins and stays in `thumbnail.json`.** No file swap. Reasons:
  1. At 168 px, A sells the promise of the title "at Every Depth": six subjects stacked down a column that darkens, with the cap at the bottom. It is the proven archetype B grid (the style bible's depth gradient), and it doubles as the s001 opening image, as the brief requires.
  2. B ("4 KM DOWN", Doug over a red-glow canyon) is clean, but there is only one idea in it and nothing to discover. A dark canyon could belong to any topic, and nothing in it says Antarctica or what is down there. That makes it weaker on curiosity than A, which has six named things to look at.
  3. Every label in A is backed by the script and facts.md (for example, the "see-through fish" is sourced at line 124 of the script), and none of them repeat a word from the title or alt titles.
  B stays in `thumbnail_b.json` as the YouTube Test & Compare variant. Run it as a test, not as the primary.
- **Package:** The title "What Dying at Every Depth Under Antarctica Would Be Like" (T1, 56 chars) delivers what it promises: Doug dies at 9 of 11 depth stops, down to more than 4 km. It is not a noun swap of 001, and the titler's side-by-side reasoning is accepted. The description is factual and lists sources, with the AI-use and cartoon disclaimers. Playlist is `places`. Not made for kids. No gore: the deaths are opaque ice and cartoon X-eyes, and Blood Falls is shown as rust.
- Non-blocking for the editor/director (optional, only if it costs nothing): clip the Denman glow and the volcano ash speckles in thumbnail A to their own bands. Also note the advisories on s036, s075, s120 and s138. Post-render screening is still required.

ART + PACKAGE: APPROVED
- 2026-10-12: scripted in 2 screener rounds (fact fixes, Denman/Vostok order resolved with sourced >4000 m), art 3 rounds + 1 safe-area fix pass (camera-move counter overflow; keyframe renderer skips 1080p camera moves so reviewers must render end frames). Engine: clamped font size >=1 in paint.py. Risks: Lake Vostok/Denman hedges, minor notes s036/s075/s120.

## 2026-10-12: final package gate
- Inputs: `metadata.json`, `build/thumbnail.png` (A), `build/chapters.txt`, `build/timing.json`, `build/qc.json` (914.5 s, `problems: []`), `build/samples` f_001-f_002, `script.md` opening, `visual_review.md` post-render (main FAIL on s248 only; Shorts PASS), and the s248 shotlist diff.
- **Title kept:** "What Dying at Every Depth Under Antarctica Would Be Like". None of the alternates is clearly stronger. "Every Layer" lands next to 001. "How Doug Would Die" repeats the openings of 001 and 003. "Creepiest Things" underpromises on the death format. "Why ... Deadlier" is the weakest curiosity frame of the four. The title delivers what it promises: 9 deaths over 11 depth stops down to more than 4 km.
- **Thumbnail A:** the six-band ice column reads at feed size. The red cap at the top and the dropped cap at the bottom bookend the episode, and every label is a chapter. The labels share no words with the title. I would click it.
- **Chapters/description:** every chapter matches the spoken header shot in `timing.json`. Blood Falls is at 13.4 s, Mercer at 495.7 s (8:15), Vostok at 731.5 s (12:11) and Denman at 813.5 s (13:33). The first chapter is at 0:00, the intro is at least 10 s, and there are 12 chapters. The s248 label move changes no timing, so the chapters hold for the re-render. The description includes the sources plus the AI-use and cartoon disclaimers, with no medical or safety advice.
- **First 60 s:** "Blood Falls" is the 33rd word (spoken at 13.4 s), "It isn't blood" plays at 24.8 s and the first death comes at about 65 s. The thumbnail is the opening image. Narration runs at 194 wpm overall. Samples f_001 and f_002 are clean: the meter flashes 400 m only on the twist shot and the outflow reads as a rust stain. The pacing would keep me watching.
- **s248 fix verified in `shotlist.json`:** DENMAN GLACIER x 600 → 720, with y, size and appear unchanged. This was the screener's only required fix.
- Condition (operational, not creative): the upload may go only from the queued `render --final` output (`.rerender=final`), after `qc` passes and a frame check at s248 (about 825 s) shows "SEA LEVEL" whole. The current `build/final.mp4` still has the overlap and must not be uploaded. The Shorts need no re-render.
- Series bible: the death total is now 139 (16 episodes) and the 016 log row is set to final-approved.

FINAL: APPROVED
- 2026-10-12: post-render main FAIL (s248 label overlap, fixed x720); re-render queued; stage left unchanged pending round 2. Shorts PASS.
FINAL: APPROVED

- 2026-10-12 round 2: QC exit 0 (problems: []), visual screener main PASS + shorts PASS (s248 SEA LEVEL / DENMAN GLACIER clear at 825 s). Creative director's conditional package approval (frame check at s248) is now satisfied; stage set to qc_passed.
FINAL: APPROVED
