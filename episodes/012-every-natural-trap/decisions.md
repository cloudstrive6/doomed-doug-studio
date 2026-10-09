# 012 Every Natural Trap: decisions

## 2026-10-09: creative director, script gate APPROVED (draft 3)
Reviewed: `script.md` (draft 3) against `brief.md`, `script_review.md` (draft 3, PASS, 0 required fixes), and spot-checked `facts.md` rows that
looked most at risk (sinkhole count, La Brea buckets, Altamura nasal cavity, avalanche speed attribution, lizards/pigeons). All are sourced.

1. **Brief compliance: met.** 9 items on one declared axis (duration of entrapment), ordered minutes to 230 Myr, with amber as the boss. Section
   headers "Short stay." / "Long stay." / "Permanent stay." are placed as briefed. Counter runs 100 to 107 (7 deaths), survivals are Brinicle
   (sticker pre-printed) and Dead Sea ("Doug is fine."). 7 stickers, and the closing suitcase list matches. Costume gag twice, each with one
   "can't hurt a person" line. Callbacks are exactly two (004 Morecambe Bay, 002 ant suit). Time machine, field guide and Buddy are not used.
2. **Opening: passes.** "Tree well." at word 32; the twist ends at word 144. Condition for the editor: measure the twist end in the narrated
   audio. It must finish by **0:46**. If TTS runs slow, tighten pauses before line 25. Do not cut words.
3. **Overlap rules: met.** No quicksand, Morecambe Bay only as a one-line callback, no Myanmar amber (Dolomites only), and the crevasse beat is
   "the glacier gives Doug back 75 years later", not 007's cap on the rim.
4. **Real victims: met.** Antelope Canyon 1997 and Tsanfleuron 2017 get dates and counts only, on silent caption cards with no people drawn and
   no jokes in the fact lines. Altamura has no skeleton drawn and no real photos.
5. **Safety advice: none.** No rescue, beacon, high-ground or weather-check lines. The NPS flash-flood line and the "danger is highest after a
   storm" line are descriptive facts, not instructions. Keep them that way in any later trims.
6. **Click-and-stay test: yes.** Every item has a real twist (the tree built the trap, the storm you can't see, the icicle that grows down,
   soft falling and hard stopping, the floor left with the sea, the glacier gives you back, the bait restocks itself, the cave grows over you,
   amber gives back everything). The boss earns its slot, and the dire-wolf chain and "match the decor" are strong lines.
7. **Notes, not blocking (do not reopen the script for these):**
   - The Dead Sea kicker (line 173) is the flattest in the episode and sits just before the midpoint zone shift. The director should cover it
     with a strong visual (the sinkhole map multiplying) and the editor should go straight into the "LONG STAY" card with no extra hold.
   - Brinicle (329) and Amber (425) are slightly over their word targets. The editor may tighten pauses, but no line cuts without coming back to me.
   - The optional STAY tags in the script header are approved for the art director as listed (they are monotonic and each one is sourced in facts.md).
8. **For the titler:** the working title "What Dying in Every Natural Trap Would Be Like" holds. The script shows each trap's death as a cartoon
   beat and never describes the dying, which is how every T1 episode on this channel has worked. Run the brief's `signals` queries before you lock
   the title. Thumbnail labels must avoid title words (brief section 3).
9. **Series bible:** no update at this gate. The counter (100 to 107), the 012 log row and the "sticker already printed" survival variant go in
   at the final package gate, matching 011's practice.

SCRIPT: APPROVED. Next: director (shotlist), then titler.

## 2026-10-09: art director, asset review PASS (33/33) and rulings on the director's notes
Full review: `art_review.md`.
1. **Capless upright Doug in the amber bead (s291-s293): approved one-off.** Doug uses `pose: "wave"` and `gear: ["cap_off"]` inside
   the bead, and `doug_cap` sits on the bead top, so the cap is visible in every shot. The counter ticks on a living expression (mid-wave)
   with no `on_back`, because "perfectly preserved" is the scripted death image. This is the "preserved" death variant and does not set
   a precedent for ordinary deaths.
2. **Brinicle background: `#1f3a5f` replaced with the surface colour `#3a9ad9`** in s061-s091 (31 shots), and the water speckle spray
   `#2c4d78` replaced with `#6fc1ee`. The art bible rule (water under sea ice = `#3a9ad9`) applies on every axis, not just depth. The
   ramp is channel-wide colour language, and a brinicle is a shallow under-ice phenomenon. I edited `shotlist.json` directly. The
   director must update the generator's `NAVY` constant to match.
3. **Death beats: confirmed as built.** Every death shows the cap. Cap-only images are used for the canyon, avalanche and glacier, a
   ghost with cap for the crevasse, buried-to-the-hips `dead` plus ghost for the tar pit, the cap on `rock_lump` for Altamura and the
   cap on the bead for amber. No `on_back` is needed.
4. **Real-victim cards: confirmed** (s047-s051, s169-s175: muted, no Doug, no people, no jokes; no skeleton at Altamura).

ART: PASS.

## 2026-10-09: creative director, thumbnail pick: B (3x3 labelled grid, archetype A)
Compared `build/thumbnail.png` (A, funnel ladder) and `build/thumbnail_b.png` (B, 3x3 grid) at full size and as 168 px feed tiles.
1. **B wins on feed legibility.** At 168 px all nine B labels still read as words ("Tree Well", "Tar Pit", "Amber"), and every tile subject
   stays recognisable (tree with skis, brinicle, snowball avalanche, sinkhole, crevasse, bison in tar, amber bead with the red cap).
   In A the white-outlined labels sit on the tile art (snow, ice, sand) and turn into grey smears at 168 px. "Dead Sea Sinkholes" also
   runs past both edges of its tile, and "Brinicle" and "Crevasse" can't be read.
2. **A is also inconsistent:** six labels sit inside the tiles and three sit outside them. The outside ones are bigger than the inside ones,
   so "Tar Pit", "Altamura Cave" and "Amber" pull the eye more than the escalation does. The funnel also looks like a wrong-way pyramid
   with a lot of white space on both sides.
3. **Variety:** 011 used archetype B (stepped pyramid). Running B again back-to-back would repeat the look in the feed. Archetype A is the
   default style-bible format, has 9 tiles (12 max), and every label is 4 words or fewer.
4. **Boss slot:** the amber bead with Doug and the cap on top sits bottom-right, where the eye finishes reading, so it still works as
   the payoff tile. Doug appears as one tile only, which follows the style-bible rule.
5. **Files:** the old `thumbnail.json` is kept as `thumbnail_a.json`. `thumbnail_b.json` has been copied to `thumbnail.json`, which means
   shotlist s001 (`scene_ref: "thumbnail"`) now opens on the grid. `validate` returns OK and `build/thumbnail.png` was re-rendered from the grid.
6. **Warning for the graphic designer:** `build/gen_thumbnail.py` still writes the funnel to `thumbnail.json`. If you re-run it, swap the
   outputs first, or it will undo this pick.

THUMBNAIL: B APPROVED. No redesign requested.

2026-10-09 Showrunner: packaged. Script 3 rounds (screener fixed facts, hook, Flesch); art assets 1 round; keyframes 2 rounds (Doug ink/overlap fixes); thumbnail grid chosen over funnel. Narration 15:30, 199 wpm. Risks: brinicle/amber slightly over target length; thumbnail Slot Canyon/Amber/Altamura read weakly at feed size (optional fixes in visual_review.md); real-victim cards (Antelope Canyon, Tsanfleuron) handled with no jokes.

## 2026-10-09: creative director, final package gate
Reviewed: title and alts, `build/thumbnail.png` (3x3 grid), description with `build/chapters.txt`, `metadata.json`, the
script opening, samples f_001/f_002 (15 s, 45 s), `build/qc.json` (929.5 s, `problems: []`) and visual_review.md round 3
(main PASS, Shorts PASS).
1. **Title kept:** "What Dying in Every Natural Trap Would Be Like" (T1). Last used in 009, so it isn't back-to-back
   (010 T2, 011 T7). The video delivers on it: 7 cartoon deaths across 9 traps, and the 2 survivals are played as gags.
   None of the alts is clearly stronger. The "How Long ... Before Killing Him" alt is longer and puts the twist in the
   title, so no swap. Keep it as the first A/B candidate if CTR comes in under the channel median.
2. **Thumbnail:** the grid follows chapter order, the labels are item names only, there's no gore, and Doug appears
   once, in the boss tile with his cap on top. It isn't misleading, and it's the s001 opening frame. I'd click.
3. **Opening:** "Tree well." is spoken about 33 words in, and the twist ("the calmest place... is the most dangerous
   spot on the slope") lands within about 20 s. The 230-million-year line is an open loop to the final item. The
   on-screen opening is DEATHS: 100, the clean suitcase and "Doug did not agree to this." It would keep me watching.
4. **Description/metadata:** the chapters are valid (0:00 start, 9 chapters, each well over 10 s), the sources and
   the disclaimer are present, and there's no safety advice. The "two mites ... 230 million years" claim is sourced
   (Schmidt et al. 2012). `validate metadata` returns OK. I fixed a stale doc field: `thumbnail_brief` now describes
   the Archetype A grid that shipped instead of the rejected ladder (screener advisory 3).
5. **Non-blocking, for later:** short01 s080/s087 counter clipping during zooms (set camera.x to 960 and re-render
   short01 only, if time allows). The thumbnail tile advisories (Slot Canyon wave, Altamura lump) are optional and
   aren't worth a re-render.
6. **Series bible updated:** counter total 107, and the 012 row is added to the episode log.

FINAL: APPROVED
