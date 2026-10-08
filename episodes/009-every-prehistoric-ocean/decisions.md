# Decisions: 009-every-prehistoric-ocean

**2026-10-08, creative director**
1. Chose backlog #3 (prehistoric ocean). Its engine is now the hottest in the lane: Fossil "How Long You'd Last in Every Prehistoric Era", 10.6M at 15,215 vph. The queue is empty after 008, so this could not wait for the #14 Venom hold (ep 002 day-7 data) to clear. Venom is planned for 010.
2. Risk accepted: BeyondTheBlue posted the same concept (311K, 6,704 vph). We differentiate with a T1 title (no "How Long You'd Last"), our own twists and the episode-only night clock.
3. After this episode, the next two must come from outside `prehistoric`.
4. Series bible: corrected the stale "next counter starts at 65" to 74. This episode runs 74 to 84.

**2026-10-08, creative director: script gate (draft 3) APPROVED**
1. Screener PASS after 3 rounds (facts 0 errors, hook 9/10, structure 8/10, voice 8/10, 3,165 words, about 16:14). Read the full script: I would click and keep watching.
2. Why it works: "Anomalocaris." at word 30, twist by about 42 s; every item has a real twist (soft prey, half-estimated shell, one claw, scientists shrank it, where the spiral went, first giant, wrong animal, meal killed it, roof teeth, whale-eating whale, same sea, above the top of the food chain). Two survivals at items 2 and 8 break the rhythm. Night clock trends down to 3 s at the boss. Callbacks capped at 4. Deaths cartoon-only; stomach contents and bite marks stated clinically. Tone adult-coded.
3. Title promise holds: 12 stops across Paleozoic, Mesozoic and Cenozoic, with a death in 10 of them.
4. My only edit: the header comment now says draft 3 (it still said draft 2). No spoken words changed.
5. Advisory for the director and editor, not blocking: the Pliosaurus bite is in pounds while Dunkleosteus is in newtons. Leave it, since the source gives pounds. Pliosaurus is the longest non-boss item (301 words), so keep its shots brisk. The "still inside that cliff" line expires with the 2027 Kimmeridge dig: re-check it before any Short or re-upload.
6. Series bible: add the night clock (episode-only, like 007's FROZEN meter) and the 009 log row (74 to 84, survivals Endoceras and Xiphactinus) at QC, as we did for earlier episodes.

**2026-10-08, creative director: thumbnail gate (v1) CHANGES**
Strengths: clean archetype A, legible labels at 168x94, a good era-darkening gradient, and strong tiles 1-5 (Anomalocaris, Endoceras, Jaekelopterus, Dunkleosteus, Helicoprion). No title words are repeated, and there is no gore.
Problems: the grid is a stamp sheet. All 12 creatures face right at the same size, height and crop. In the feed, tiles 6, 8, 9, 10 and 12 (Cymbospondylus, Xiphactinus, Tylosaurus, Basilosaurus, Megalodon) read as the same grey fish, so the bottom row, which should be the payoff, is the weakest part. Megalodon, the boss, has no more presence than tile 1, and the overall read is "picture book", not nature horror.
Required changes:
1. Break the rhythm by mirroring (`flip: true`) Endoceras, Pliosaurus and Basilosaurus so they face left. Vary the framing across the grid: about 4 full-body, 4 mid and 4 tight head crops. No two neighbouring tiles should share a crop.
2. Basilosaurus: show the long serpentine body undulating across the tile (smaller scale, full length, slight `rotate`), not a shark-like head crop. Its eel-whale silhouette is its only distinctive feature.
3. Tylosaurus: swap to `tylosaurus_mouth` or a gaping-jaw crop, or show the full body with paddles and tail so it stops reading as a shark. Keep its green colouring.
4. Megalodon (tile 12, the boss): a tight head-on or three-quarter crop with jaws wide open, with the mouth taking at least 40% of the tile. Add a tiny snorkelled Doug (red cap readable, scale about 0.12-0.15) floating in front of the jaw for human scale (style bible 7, idea 2). That is the one image that sells the title. Try `megalodon_bulky` if it fills the tile better. Keep Doug in the Anomalocaris tile as well.
5. Livyatan: open the jaw wider so the tooth row reads at 168x94, since it currently looks like it is smiling. Push the body bigger so it bleeds out of the frame and feels huge.
6. Cymbospondylus and Xiphactinus: vary them as well. Pull Cymbospondylus back to a fuller body so its long thin profile reads (it is the "first giant"), and leave Xiphactinus as a tight upturned-jaw crop.
7. Keep the palette gradient, labels, frames and order exactly as they are. Re-render thumbnail.png and thumbnail_small.png, then send them to the visual screener before resubmitting.

**2026-10-08, creative director: thumbnail gate (v2) CHANGES (one small fix, then approve)**
Against my v1 CHANGES: 1 done (Endoceras, Pliosaurus and Basilosaurus face left, and the crops now run full, mid and tight). 2 done (Basilosaurus is a long thin full body, its own silhouette). 3 done (Tylosaurus is a green-and-red gaping maw and no longer a shark). 4 done (Megalodon is a tight jaw crop with the teeth filling the tile, and a tiny snorkelled Doug for scale). 5 done (the Livyatan teeth read and the head bleeds out of the frame). 6 done (Cymbospondylus is full body, Xiphactinus a tight upturned jaw). 7 done (palette, labels, frames and order are unchanged). The stamp sheet is gone, and the bottom row now pays off: three mouths getting bigger and darker toward the boss. I would click this.
Blocking: the visual screener's Round 4 is a FAIL. YouTube's duration badge (about x 1095-1251, y 620-691) hides Doug from the waist down in the Megalodon tile, which kills the human-scale cue that sells the title.
Required changes:
1. Megalodon tile: move Doug up 40-50 px so his whole figure, fins included, sits above y 610 on the navy gap right of the jaw. If he collides with the white jaw edge, shift the shark about 30 px left or down. Keep Doug's scale at 0.12 or more, and never place him over the white teeth.
2. Now required (cheap, and flagged three rounds running): shift the "Megalodon" label left so it ends before x 1085, because the boss name must not read "Megal..." in the feed.
3. Optional: open the Livyatan jaw about 20% more to separate it further from Megalodon.
Re-render thumbnail.png and thumbnail_small.png and get a visual screener PASS with the badge overlay tested. If only items 1-3 changed, that PASS approves the package without another CD round.

- 2026-10-08 Showrunner: packaged. Rounds: script 3 (screener FAIL, FAIL, PASS; CD approved), assets 2 (helicoprion redraw + cleanups), keyframes 3 (AD/visual screener PASS), thumbnail 3 versions (CD asked for changes, then v3 visual-screener PASS incl. duration-badge test). Runtime 17.2 min. Risks: BeyondTheBlue's near-identical concept; Dorset pliosaur "still in the cliff" line dates after the 2027 dig; 1 px white line at left edge of ~77 keyframes (check in draft render); editor did not check music/stings; s276 tusks small.
