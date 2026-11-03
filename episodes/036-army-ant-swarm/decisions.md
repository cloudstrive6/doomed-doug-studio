# 036 Why Army Ants Only Kill What Can't Run Away, Like Doug: decisions

## 2026-11-03, creative director: episode pick
1. **Picked #85 army ants (8.0)**, the top eligible backlog row. Brief: `brief.md`.
2. **Did not pick #84 chimp**, the memo's 036 recommendation. Its gate is 033's early CTR, and 033 doesn't publish until 11-04 17:00Z, so the gate can't be read before production has to start. It moves to 037/038.
3. **Overrode my 035 note ("036 must not be `animals`")** under that note's own exception. Memo 11-02 sections 4-5 recommend animals for 036/037, and every non-`animals` row is gated (prehistoric until 11-06) or weak (#94 duplicates 012).
   The repetition risk we treat as real is four big-mammal T9s in a row. A swarm insect in a rainforest, with a new title shape and a new axis, breaks that run.
4. Stage stays `idea`.

## 2026-11-03, script writer: draft 2 (screener FAIL on draft 1)
1. F1-F4 fixed as the screener asked. Beebe's ring is now "about a century ago", with the label "BRITISH GUIANA" and no year. The kicker is now "the biggest army ant colonies on Earth". The bivouac line is conditioned on cool weather, with the energy saving framed as "scientists think it may". "Built to grip" is cut.
2. Rule 8 is now met in all three items, with sourced scale analogies: the ocellated antbird is about a pencil (17.5-20 cm), a soldier is about two grains of rice (about 12 mm), and the smallest pothole plug is about a sesame seed (3 mm). No waiver is needed for The Soldiers.
3. Line 384 is split into the swelling, then "she does it again every few weeks, for years", then the marked queen. The 557 SPECIES label is moved to the researchers shot. Rettenmeyer, Beebe and Guiana are added to config voice.pronunciations. The Couzin & Franks 2003 row is added to facts.md.
4. The opening is untouched: item 1's name is still at word 35. The script is 2,168 words. "The narrator would like that noted." is left for the creative director. Stage stays `scripted`.

## 2026-11-03, creative director: script approved (draft 3)
1. **Approved.** Screener PASS on draft 3 (facts 0 items, policy 0, hook 8, structure 8, voice 8, 2,163 words, about 11.1 min). The script delivers on the brief: item 1 named at word 35, payoff promise by 0:10, the honesty frame ("a grown person can simply walk away") said once, the boss survival pays off the title, 7 deaths (281-287) with 287 played flat, cartoon-only deaths (cut to black, empty hammock or tent, flat costume), no ants on skin, no "eats everything", and adult-coded jokes ("Doug became infrastructure", "left behind with the losers").
2. **The writer's fact-driven deviations are accepted:** a cold open at 3,000 an hour (no daily figure), a grasshopper instead of a katydid with the twist reversed to fit the source (movement triggers the swarm, and Doug dies by giving a thumbs up), the Soldiers trimmed to sourced claims, and the farmer anecdote cut.
3. **"The narrator would like that noted." has been replaced** (CD line edit, L474) with "The narrator will be reviewing the footage." The series bible lists 011's "He would like that noted." as used-once, so even with a different speaker, using the same tag in the same survival slot reads as a reused bit. The new line keeps the narrator quietly disappointed and is new to the channel. It is +1 word, so the screener doesn't need to re-check it (there's no factual content).
4. Notes for the director and the titler (not blocking): the sign values the script states are 100/50/30/10/0 M, and the director may fill in 200/150 on the earlier items as the brief says. The ants are never cute (brief section 7). No "vs" or "1000" in the packaging. The title must stay honest to "only kill what can't run away".
5. The series bible is updated: counter 287, the 036 log row, and the new used-once lines.

## 2026-11-03, director: shotlist
1. **218 shots.** Narration matches the approved script word for word (2,163 words). Doug appears in 156 of 218 shots (72%), and no shot runs over 45 words. On a 195 wpm estimate, every shot gets a new pop-in at least every 5 s. s001 opens on `scene_ref: thumbnail` with the first 11 words. The thumbnail.json is the graphic designer's, so that validate error is expected until it exists.
2. **Palette: a "distance to the queen" ramp.** The forest gets one step darker per item along the trail: pale green `#dde8cc` at the front, then night `#1b2f4a` for the move, nest dusk `#46523f` / `#3a4535`, and a dawn-orange `#f2a24a` Africa for the boss. Full table in asset_requests.md. The forest skies count as green grounds, so wordart there uses the white-to-yellow override.
3. **DISTANCE TO QUEEN sign:** a size-28 wood-fill `#e8c07a` label under the counter at (1580,238). The values follow the brief's lead (ABOUT 200 M / 200 / 150 / 100 / 50 / 30 / 10 / 0 / 0 / AFRICA), and each change sits on the beat the script stages: 100 M at s088, 50 M at s108, 30 M at s130, 10 M on the empty-tent death s149, and AFRICA at s193 after the big sign is struck through (s192-s193).
4. **Cap logic (one cap per frame):** Doug wears his cap in items 2-7 as usual (cartoon reset per item; the script's own stage directions put it on him there). s166-s168 (finds his cap on the living nest, climbs in) use `gear: ["cap_off"]` on upright Doug, because `doug_cap` is on the nest in the same frame. This is a logged one-off exception (art bible "Capless upright Doug"). At the queen (s187) he has it back on.
5. **Deaths, cartoon only:** 281 is black card + counter + ghost; the cap is carried off as cargo in s027. 282 is the flat costume + cap on black. 283 is `on_back` dead across the logs under the column. 284 is still walking the mill with X eyes. 285 is the empty open tent + cap on the ground. 286 is the nest silhouette on black + ghost, then the cap at the ghost's feet. 287 is played flat: small `on_back` on black. No ants on skin, nothing cut up.
6. **Silhouette-then-reveal:** the soldier (s005 silhouette → s069 colour), the queen (s080/s139 silhouette → s172 colour), the living nest (s152 → s153), the driver-ant queen (s199 → s200) and the driver jaws (s082 teaser → s203).
7. **Shorts (3, all ending on the item's Doug beat, simple end card, no tease):** short01 Death Spiral s117-s129 (Beebe's 1,200 ft ring, Doug dies still walking; hook line on the s111 mill drawing). short02 The Queen s179-s191 (workers choose the queen, Doug left behind with the losers). short03 Driver Ants s205-s213 (20 m an hour, Doug walks away and survives; hook "twenty million workers" on s196).
   Road Crew was the first choice but runs about 56 s with an outro, over the 55 s cap. Titles and descriptions are left for the youtube-titler.
8. **Layout check:** keyframes were rendered with temporary stand-in boxes at the exact requested extents (removed afterwards). Fixed: props, wordart and bubbles in the counter/sign zone (s042, s044, s048, s070, s076, s102, s154, s187, s192, s203, s205), the hanging-nest log crossing the HUD (now x 800, scale 1.15), the egg piles (now drawn eggs instead of spray), the bridge-Doug geometry and the field-guide NO rows (4+3 at 32 units).
   A real keyframe pass is still needed once the 33 drawings exist.

## Keyframe review fixes (director, 2026-11-03)
- **Capless ghost, s169-s170 (logged one-off, visual review item 10):** the ghost Doug wears `gear: ["cap_taken"]`. The real cap is stuck in the bivouac (s166) and comes back out in s170 ("The cap came back out"), so a capped ghost would put two caps in the frame and muddle the punchline. This departs from the art bible's "a ghost Doug keeps his cap as always" for these two shots only.
- s197: New York is built from the library building family (`empire_state_building` + `four/five/six/eight/ten_story_building`) instead of `city_skyline_small` (Darwin, palms). No new asset needed.
- s117-s118 restaged on the top-down dirt card used in s109-s116 (visual review option b). No `army_ant_mill_side` asset needed.
- Distance sign: one format all episode ("DISTANCE TO QUEEN: 200 M"; "ABOUT" dropped in s002-s028).

## 2026-11-03, creative director: thumbnails A/B/C, round 1
Reviewed build/thumbnail.png, thumbnail_b.png and thumbnail_c.png at full size and the *_small.png feed-size versions, against brief section 8 and the title "Why Army Ants Only Kill What Can't Run Away, Like Doug". No visual-screener report on the thumbnails exists yet, so nothing here is final package approval. That waits for a screener PASS on the revised set.

**B (SURROUNDED): approved creatively, no changes.** It is the strongest of the three at feed size: the amber field, one word, a big red-capped Doug and a carpet that reads as a mass of insects even at 168 px. It complements the title rather than repeating it ("can't run away" plus SURROUNDED), and it delivers: Doug stands in the swarm several times in the video. The stump itself is not a scene in the video, but it is a staging device, not a promised event. It is adult-coded enough (nothing cute, no faces on the ants, no "vs" and no count).

**A (DON'T SLEEP): changes required.** The concept is right and it stays the primary and the s001 opening image (the hammock is item 1's death and the boss setup). At feed size, though, the threat and the victim don't meet:
1. Bring the sickle jaw tips to within about 40 px above Doug's head. Right now they end over the left palm (about x 860), about 130 px short of him, so the picture reads as "ant and a man in a hammock" instead of "this is about to happen". Either move the soldier right (x 70 to about 190) or move the hammock and Doug left. Keep DON'T SLEEP clear of the jaws.
2. Doug scale goes from 0.4 to about 0.55, with the hammock scaled to match. At 168 px he is currently a red dot. The cap and closed eyes need to read.
3. Fix the clipped antenna at the top edge (about x 640-700, y 0-20). It shows as a stray black blob at feed size. Keep it fully in frame or crop it cleanly through the shaft.

**C (grid): changes required.**
4. Use the chapter names as labels: SWARM FRONT / DEATH SPIRAL / LIVING NEST / THE QUEEN. "FRONT" on its own means nothing at feed size. "Death Spiral" and "Living Nest" are the curiosity gaps the grid exists to sell. (This overrides the one-word leads in my brief.)
5. Queen tile: at feed size the pale-banded gaster reads as a barrel or a cage, not an abdomen. Narrow the pale bands, or darken them toward the body colour, and make the queen about 15% larger so it reads as one huge ant next to a small Doug.
6. Keep 4 tiles (a deliberate departure from the 6-16 of style bible archetype A, for feed-size legibility) and keep the tile colours as they are.

Next: the graphic designer applies 1-6 and re-renders A and C (and their _small versions). Then the visual-screener checks all three. If it passes, the set goes to Test & Compare with the same title.
- **Art director, round 3:** the s169-s170 capless ghost is **not approved**. Both ghosts wear the cap again (standard ghost grammar, as in s027). s180's zoom was re-aimed so only the winning queen ends in frame. See art_review.md Round 3.

## 2026-11-03, graphic designer: thumbnails round 2 (CD round 1 notes 1-6)
- **A:** soldier moved to x 262, y 356, scale 3.35→3.1. The lowest point of the jaw hook now hangs about 35-40 px above Doug's cap, and the hook tips stay about 35 px clear of DON'T SLEEP. Doug is 0.4→0.55 and the hammock 0.55→0.76, re-seated at (1030,630). The hammock is now drawn before the soldier so the jaws pass in front of the left palm. The antenna club is fully in frame (about 15 px from the top edge).
- **C:** labels are now SWARM FRONT / DEATH SPIRAL / LIVING NEST / THE QUEEN. The queen is an inline `group` copy of `army_ant_queen` (the library file is unchanged), with the pale gaster membrane `#efe2c0`→`#a8643f` and scale 0.66→0.76. Doug moved to x 1205. 4 tiles, colours unchanged.
- B unchanged. All three re-rendered and checked at 168x94. Next: the visual-screener.

## 2026-11-03, creative director: thumbnails A/C, round 2
Re-reviewed build/thumbnail.png and thumbnail_c.png at full size and at 168 px (*_small.png). B stays approved as is.

**A (DON'T SLEEP): approved creatively.** Notes 1-3 are all met. The jaw hook now hangs right over the hammock, so at feed size it reads as "this is about to happen". Doug at 0.55 reads (red cap, white head, closed eyes). The antenna is in frame, and DON'T SLEEP is clear of the jaws. It stays the primary and the s001 opening image.

**C (grid): one last small round, queen tile only.** Note 4 (chapter labels) is met, and the other three tiles are good. Note 5 is not met. Darkening the membrane made it worse: the gaster is still a near-circle split by vertical bands into plank-like panels, so at 168 px it reads as a wooden barrel lying on its side, not as an abdomen. Doug is still a sliver at the tile edge. Changes:
1. Gaster shape: make it an elongated oval, about 1.8-2:1 (wider than tall), not a circle. Keep the left end at about the current x, and narrow it vertically so the top sits about 30 px below the tile's label bar.
2. Gaster fill: one body colour (the same red-brown as the thorax, as in the library queen's plates) with **3-4 thin pale membrane bands at most** (#efe2c0 is fine again, at 6-10 px each), running across the oval and following its curve. No rectangular panel or plank pattern. The 4-6 band "slat" look is what makes it a barrel.
3. Doug: scale 0.24→about 0.30, placed at about x 1215, feet on the same baseline as the queen's legs, shock face toward her. If the queen has to shrink about 5% to fit both, that's fine. The size contrast still sells "one huge ant".
4. Leave everything else as it is.

This is the last CD round on C. If 1-3 are applied, C is approved without another CD look, subject to the visual-screener. If the queen still reads as a barrel to the screener at 168 px, C is dropped from Test & Compare and A/B run as a two-way test. Next: the graphic designer fixes the C queen tile, then the visual-screener checks A, B and C (package approval needs that PASS).

- 2026-11-03 showrunner: packaged. Rounds: script 3 (2 screener FAILs on facts, PASS draft 3), art assets 2 (feet chain redraw), keyframes 3 (art-director + visual-screener), thumbnails 3 (A/B/C all PASS). Risks: kid-appeal of ant topic (no faces, no "vs"); animals playlist is the 4th big-animal slot in a row; tool bug: `keyframes --shots` wipes contact sheets (rebuild with full run).

## 2026-11-03, visual-screener: post-render QA (round 5)
VERDICT (main): PASS
VERDICT (shorts): PASS

## 2026-11-03, creative director: final package approval
Reviewed: title and alt_titles, build/thumbnail.png (A), the metadata.json description, build/chapters.txt, the script opening and samples f_001-f_003. Gates: QC passed (698.5 s, no problems) and visual-screener round 5 PASS (main and shorts).
1. **Title: kept as "Why Army Ants Only Kill What Can't Run Away, Like Doug".** The video delivers it: at about 0:50 the script says the front moves only 20 m an hour and "a grown person can simply walk away", then Doug dies asleep in the hammock, and the closing note is "JUST WALK AWAY." None of the alternates is clearly stronger. "How Army Ants Kill Doug Without Ever Seeing Him" would repeat 035's "How X Kills Doug Without..." formula back to back, and "The Creepiest Things Scientists Have Learned" is too close to 032's formula.
2. **Thumbnail A (DON'T SLEEP): approved.** It is unchanged since the round-2 approval and the screener's PASS. The jaws hang over the sleeping Doug, the swarm comes in from the left, and the 2-word text complements the title. A/B/C go to Test & Compare as planned.
3. **Description: approved.** The first two lines carry the hook (3,000 an hour, nearly blind) and the payoff (twenty million driver ants). There are 6 real sources and the disclaimer and AI-use blocks are present. `{{CHAPTERS}}` is filled from chapters.txt at upload (studio/youtube.py). The chapters start at 0:00 and there are 11 of them, all at least 10 s long.
4. **First 60 s: approved.** Thumbnail open, then the 3,000-an-hour cold open and the twenty-million payoff promise by about 0:10. Item 1's name lands at about word 33, and its twist (you can just walk away) comes inside 45 s. The samples show a clean HUD (DOUG DEATHS 280, DISTANCE TO QUEEN 200 M), Doug on-model, the swarm carpet clearly ants, and nothing cute or gory.
5. Carry-over (not blocking): art director to apply the thumbnail-C oval-gaster fix to the library `army_ant_queen` (screener advisory). The series bible already has the 7 deaths (total 287); its episode log row is now marked final approved. Next pick should leave the animals playlist (this is the 4th big-animal slot in a row).

FINAL: APPROVED
