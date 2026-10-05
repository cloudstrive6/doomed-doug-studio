# Decisions: 008 Every Step of the Ocean Food Chain

## 2026-10-05: script gate, APPROVED (draft 3 + CD TTS edits)
- Screener: draft 3 PASS (facts 0 errors, hook 9, structure 8, voice 8, TTS/policy PASS, 3,044 words, about 15:37). The round-2
  Seal Island count fix was checked against the Martin et al. 2005 full text.
- Against the brief: all 11 items are in the briefed order and the axis climbs steadily from the mantis shrimp to the orca. The counter runs
  65 to 74 (9 deaths), with survivals at the trevally ("Doug is fine.") and the orca (narrator quietly disappointed). The costume
  spine runs snail to squid, with breaks at the croc and the orca. Befriending: the grouper informant and "hi friend?". The cap
  floats, lands, then ends on the orca, with the salmon-hat fad sourced. There is one callback each to 006 and 001. There are no human-attack facts and no
  captive orcas, the liver line is one flat sentence, and there is no death-roll detail. The name "Mantis Shrimp." is spoken at words 32-33 and the twist lands at about 37 s.
  Would I click and keep watching? Yes. "It hits twice", the grouper informant, "He did the packaging himself", the sky-hunting trevally
  and the Farallon kicker into the sperm whale all land, and the orca reversal is a real payoff for the 7.72M OctoLab engine.
- **"No predators." header: APPROVED at about 87% (directly before "Orca.").** This changes the brief, which put it at about 70%. Reasons:
  1. At 70% it sat over the sperm whale, whose own item describes the marguerite defence against orcas, so the header would contradict
     the facts under it. We don't ship a header that the next minute disproves.
  2. At 87% it works as a boss card. It is literally true (NOAA calls the orca the top predator, and nothing on the list hunts it), and it pays off the
     sperm whale kicker ("the animal that makes it necessary is next on this list") right away.
  3. The spacing is still fine. "Apex." runs about 53-87% with four items, and the silent deep-navy shift before the sperm whale gives
     the eye a reset in that stretch without spending a spoken header. "The top." was considered and rejected because it is weaker and adds nothing.
  - Director note: give the "NO PREDATORS" card the full boss treatment (black, single spotlight, a 1-1.5 s hold before "Orca.").
    The silent background shift before the sperm whale must read as a change of zone (deep navy, no label), not as a glitch.
- CD edits applied directly to script.md (wording only, no re-screen needed; 3,045 words):
  1. Line 323, "Over a whole day" changed to "Averaged over every attack". This matches the paper's mean predatory success rate (47.3%).
  2. Line 323, "A seal that realizes it's being chased zigzags" changed to "When a seal realizes it's being chased, it zigzags". This avoids the TTS
     misreading "chased zigzags" as a noun phrase.
  3. Header comments: "about 89%" corrected to 87%, and "pending approval" markers cleared.
- Carry to the director/art: the closing frame shows Doug capless and far off, waving, while the orca wears the cap. This is a deliberate
  one-off exception to "Doug is never shown capless" (brief 2, item 11). Keep Doug tiny in that shot and give the cap to the orca clearly.
- Carry to the titler: the working title is T2 "How Doug Would Die at Every Step of the Ocean Food Chain". The video delivers 9 deaths and 2 survivals,
  so a death promise is honest. Don't use competitor wordings ("Refuses To Kill Us", "Terrified of", "Weirdest Apex Predator").
  If the description cites the orca fact, quote it as narrowly as the script does ("no record of ever killing a person in the wild").
- Carry to the editor: preview trevally, Farquhar, Gansbaai, marguerite, pharyngeal and Puget in `narrate`, and the new line 323.
- Series bible: the counter goes to 74 and the "cap with a new owner" ending gets logged after QC, following the usual practice.

SCRIPT: APPROVED

## 2026-10-05: thumbnail gate (creative director), CHANGES REQUESTED (round 1)
Inputs: `thumbnail.json`, `build/thumbnail.png`, `build/thumbnail_small.png`, my own 168x94 downscale, the title in `metadata.json`,
style bible 1.4 / 2.B / 2 grammar / Designer rules 10-11, and brief 3 + 7. There is one candidate (archetype B).
- **What passes:** this is archetype B with 11 items (12 is the limit) and labels outside the pyramid that alternate sides bottom-up in exact chapter order
  (mantis shrimp, moray, octopus, trevally, grouper, tiger shark, croc, polar bear, great white, sperm whale, orca). Each label is 3 words or fewer.
  ComicNeue-Bold is the only font. There's no title text, and no label repeats a title or alt-title word (Every, Step, Ocean, Food, Chain,
  Kill, Doug, Predator). There's no gore and the canvas is clean. At 168x94 all 11 animals keep their silhouettes and most labels still read, so
  the A-grid fallback isn't needed. "Orca above Great White Shark" and "Mantis Shrimp on the bottom rung" are good curiosity gaps.
- **Why it isn't approved yet:** brief 7 makes "the thumbnail must look like nature horror, not a picture book" a hard condition, and this one
  reads like a classroom food-chain poster. Every animal is in a calm side profile, the bands are evenly cheerful, and nothing tells the
  viewer that climbing this pyramid gets worse. Next to a topic of animals plus a costume, that's our biggest kid-appeal and CTR risk. The fixes below are
  small and keep the layout. The visual screener also hasn't done a thumbnail pass yet.

Change requests (graphic designer). Keep the geometry, label positions and fonts.
1. **Apex band = boss band.** Change the apex poly fill from `#ff4a3a` to near-black `#111111`, matching the "NO PREDATORS" boss card.
   Put a clean, flat red halo behind the orca: a filled `ellipse` of about rx 150 / ry 50 at the orca's centre, fill about `#e8231f`, **no
   outline** so it reads as a glow and not an annotation circle, and **not** `spray`, because thumbnails carry no paint artefacts. Draw the orca at full
   colour on top. The white eye patch and belly must still separate from the black band at 168 px.
2. **The top two tiers darken, so the climb reads as more dangerous.** Change the Great White Shark half from `#ffe24a` to deep navy (about
   `#1b2a6b`) and the Sperm Whale half from `#4fd6f0` to deep red (about `#a3162a`). Leave the bottom four tiers as they are. Check that the grey
   shark and grey whale outlines still separate from the new fills at 168 px. If one doesn't, lighten that fill one step. Don't recolour the animal.
3. **The hook item shows its weapon.** Swap `mantis_shrimp` for `mantis_shrimp_strike` (same body, club swung forward), which is the "it hits
   twice" hook. Keep at least 20 px between the club tip and Doug's costume. Move Doug right (about x 585-595) if needed, and keep him inside the band.
4. (Optional, do it if it costs nothing) Raise Doug from scale 0.175 to about 0.20 so his red cap registers as a red dot at 320 px. He stays
   smaller than the mantis shrimp, as a scale figure only.
5. (Optional) The YouTube duration badge sits over the bottom-right corner (roughly x > 1135, y > 650 at 1280x720), and "Moray" is under it.
   If the label can be nudged up or left without touching "Giant Trevally" or the pyramid edge, do it. If not, leave it, because the eel itself stays visible.

After the changes: run `python -m studio thumbnail 008-ocean-food-chain` and `python -m studio validate 008-ocean-food-chain`, re-check the 168x94 downscale,
update the `_note` and `metadata.json` → `thumbnail_brief` if the description changes (dark apex), then do a visual-screener thumbnail pass.
s001 uses `scene_ref: thumbnail`, so the opening image updates without a shotlist edit. Re-submit to the CD. If items 1-3 come back as specified and the
screener passes, I'll approve it without another round.

THUMBNAIL: CHANGES REQUESTED (round 1)
