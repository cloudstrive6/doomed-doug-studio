# 025: decisions

## 2026-10-22, creative director: script gate (draft 2, screener round 2 PASS)
Read script.md, script_review.md (round 2) and the brief. Decision on the screener's three advisories:
1. **"largest bug that ever lived" (lines 292, 314):** fixed by CD. Both now say "land bug" ("the largest land bug that ever lived",
   "The biggest land bug that ever lived"). This matches line 300's "largest land arthropod known" and leaves Jaekelopterus (009, aquatic)
   undisputed. +2 words.
2. **First death at about 1:35 vs the 1:20 target:** fixed by CD without cutting words. The "A quick word on bugs" aside is moved from
   before the cupcake to after death 204 (just before "Arm-sized."), where it works as the bridge into the list. Death 204 now
   lands at about spoken word 295 (was about 338), about 13 s earlier, so about 1:22 on the screener's clock. The twist timing (word 122) is
   unchanged. Director: the cupcake beat follows the charcoal card directly. The aside plays over the time machine/dial before item 2.
3. **Title promise (bugs cause 3-4 of 7 deaths):** accepted, not a blocker. Bugs directly kill Doug at 207 (Meganeura), 208
   (Pulmonoscorpius) and 210 (Arthropleura), and indirectly at 206 (Megarachne drags him into the river). 204 is the oxygen itself, which
   the title names as the cause. Both thumbnail creatures kill Doug on screen. The outro ("Bugs that noticed him: almost none") makes the
   irony the joke. **Titler note:** the title must keep the oxygen as the cause and must not claim bugs "hunted" or "attacked" people.
   The working title or "When Bugs Were Big Enough to Kill Doug" are fine. Don't use "Bugs That Killed..." phrasing.
   Thumbnail: keep Meganeura and Arthropleura as the hero creatures (both are kills).
- Word count after edits: 2,968 (floor 2,950). Footer updated. Not blocking: the Griffinfly runs 332 words. Rotate out "Here comes the
  strange part" next episode.
- Would I click and keep watching? Yes. Fire in the first 40 s, the spider that wasn't, and the walking sea scorpion are strong mid-video
  re-hooks. The oxygen debate is honest and resolved on air.

SCRIPT: APPROVED

## 2026-10-22, director: shotlist (260 shots), shorts, asset requests
- **Coverage:** all 2,968 spoken words appear once and in order (checked word by word against script.md). Max 31 words a shot; every
  shot over about 15 words builds with `appear` pop-ins (no static stretch over about 4.6 s at 195 wpm). Doug is in 96% of shots.
- **HUD:** `DOUG DEATHS: N` at (1590,162) on every shot from s002 (203 to 210), with the DOUG FOR SCALE reading under it as a size-28
  label at (1600,238) and `tape_measure` at 0.16. Readings: SMALLER THAN A DOT → 40 CM → 54 CM → 55 CM → ABOUT 70 CM (items 5 and 6)
  → 1.6 M → DOUG-SIZED (s195 onward, held through item 8) → ABOUT 2.6 M → DOUG (closing). Monotonic. Each item's scale shot has a
  DOUG FOR SCALE panel (vertical 0-3 m tape, `doug_silhouette` = 1.6 m so "1.6 M" is Doug-sized). Item 8 adds only the dashed
  "2 TO 3 M?" bracket; the solid line stays at 1.6 M; item 9's solid line reaches 2.6 M inside the kept bracket (script deviation 4).
- **Palette:** one step darker per item on a swamp ramp (sky `#cfd8c0` → `#5f6a50`, ground `#5d6b45` → `#3a3a28`), cream `#f4f1dc`
  diagram cards, 2026 park `#8fd3ff` / `#7cc25a` at the close. All WordArt on the swamp scenes uses the green-ground override.
- **Deaths:** 204 soot (on_back dead + soot spray + smoke curl, no burn detail); 205 cap on peat; 206 cap under the upturned glass;
  207 cap drifting (no body, cut before landing); 208 cap on the log; 209 cap in ripples; 210 on_back dead, played flat (no shake). s030
  (cap on the fern) and s254 (cap on Arthropleura) show **no body**, because `cap_off` would put a second cap on the ground (art bible
  "death images without a body"). The script's "cut to black on contact" (208, 209) is a hard cut to the death shot, not a black
  frame, so keyframes stay reviewable.
- **Survivals:** 206 and 208 held on the counter at The Beak (s115) and the trackway (s195, `sit` + neutral dot eyes, no X eyes).
- Brief reuse check: `meganeura`, `arthropleura`, `scale_tree`, `fern`, `tape_measure`, `time_machine` reused; `jaekelopterus` not reused
  (Megarachne and Hibbertopterus must look distinct). 27 new drawings requested in asset_requests.md.
- **Shorts:** short01 The Spider s079-s087 (+hook), short02 The Millipede s223-s229, short03 The Sea Scorpion That Walked s178-s186
  (+hook), short04 The Griffinfly s137-s143 (+hook). All four cut just before Doug's death or survival beat (Doug's-fate loop).
  Titles and descriptions are left for the titler.
- Thumbnail (s001 `scene_ref`) is pending from the graphic designer; it is the only non-asset validator item.
