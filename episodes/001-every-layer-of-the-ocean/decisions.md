# Decisions: 001 Every Layer of the Ocean

## 2026-09-29: script gate, draft 2: GO
- Screener round 2: PASS (0 fact errors, hook 8/10, policy pass, 3,231 words / ~16:34).
- Checked against the brief: 12 items in depth order with 5 spoken zone headers; item 1 named at word 32 and its twist at about 0:41;
  7 deaths with at least one in every zone, so the title holds; every gag from the brief is used; the boss kicker plus a 23-word outro with one CTA.
- Accepted deviations: the Humboldt beat changed from the flashlight to the squid costume (stronger, and it ties to the cannibalism fact).
  The death order is zombie worms 6 and snailfish 7, which follows the depth order.
- The CD made one fix itself: line 275 "The worst part is that he isn't..." became "But he isn't...", because "worst part" was used 3 times.
- Screener recs R1 to R5 are non-blocking and waived. The editor must preview the pronunciations listed in the script header before the full render.
- Series bible updated: death total 7, episode log row, cap-survives and disappointed-narrator gags.

## 2026-09-29: thumbnail gate (one candidate, `build/thumbnail.png` from `thumbnail.json`): GO, conditional on visual-screener PASS
- Screener status: the only visual report (`visual_review.md`, fix 2) covers the old director placeholder, which has now been replaced.
  No screener pass exists for this version yet. This is a creative GO, and packaging must not advance until the visual screener passes this version.
- Checked against the brief and `metadata.json` `thumbnail_brief`: it is Archetype B, a 5-tier pyramid on the art-bible ramp
  (#3a9ad9 → #1b4f86 → #0b2447 → #050a1f → #020308). There are 9 tiles, the requested 8-10. The man o' war is at the top, and the snailfish plus
  the Challenger Deep plastic bag are at the bottom. Labels sit outside the tiers on both sides, in one comic font, each 2 words or fewer, and match
  the chapter names. Doug appears only as a small scale figure (shock, red cap visible). No arrows, circles, title text or gore.
  The earlier cropped labels are fixed.
- Title complementarity: "How Doug Would Die in Every Layer of the Ocean" shares no word with any label (style bible 7 titler rule 7).
  The title gives the frame and the pyramid gives the items. The promise matches the video, since every tier holds an item that is in the video.
- Feed test at 168x94: the dark gradient reads, and the 9 tiles are separable. Man o' war, giant squid, barreleye, anglerfish, zombie worms,
  bag and snailfish are recognisable. Labels are about as legible as PE's own grids. I would click it.
- Non-blocking notes for the graphic designer (fix now only if the visual screener asks):
  1. Safe area for s001: "Challenger Deep" starts at about x=32 and "Snailfish" ends at about x=1237, just outside the central 90% (x 64-1216)
     that `visual_review.md` fix 2 requested for the opening shot. If the screener holds that rule, pull the bottom tier in by about 30 px per side,
     or move both labels inward, and set "Challenger Deep" to the same 52 px as the other labels (it is 45 px now and sits 22 px lower than "Snailfish").
  2. The Black Swallower tile is the weakest at feed size. It reads as a beige oval. A tighter crop on the head and the swollen belly would help.
  3. Reading order: the boss (Challenger Deep) is on the left of the bottom tier, so readers see it before the snailfish. Swapping the two bottom tiles
     and labels would put the boss last, which matches the video. This is optional.

## 2026-09-29: packaged
- Rounds: script 2 (earlier), shotlist 1, asset art review 1 (PASS), keyframes 2 (art-director + visual-screener FAIL then PASS), thumbnail 1 (CD GO, screener PASS).
- Risks: Chirp pronunciations (Man o' War, Vampyroteuthis infernalis, Osedax, Ogasawara) not auditioned, so listen in the draft. Draft render of the first 60 s not checked. Ice block s197/s198 and anglerfish male s156 are flat/small (optional polish). Thumbnail label edge margins slightly outside the 90% safe area in s001. Engine fixes: paint.py auto_ink, assemble/scene upscale (art-director). Shotlist edited directly after generation, so build/make_shotlist.py is stale.

## 2026-09-29: final package gate: APPROVED (after one CD fix to the description)
- Inputs: QC `build/qc.json` has no problems (1034.6 s). Visual screener round 3 (post-render) PASS. I checked `build/thumbnail.png` and
  `thumbnail_small.png`, `metadata.json`, `build/chapters.txt`, samples f_001 to f_003, and the script opening.
- **Title: keep "How Doug Would Die in Every Layer of the Ocean".** It is the proven depth-gradient formula with a clear Doug + threat promise,
  and the video delivers it: 7 deaths with at least one in every zone. None of the alternates is clearly stronger. "How Every Layer of the Ocean Kills Doug"
  is a close second and a good A/B candidate. "Creepiest Things Scientists Found..." breaks the Doug frame and overpromises "found".
- **Thumbnail: GO.** At 320x180 the depth ramp and the 9 tiles read, and the labels are legible. It shares no word with the title and every tile is a chapter.
  Doug is small but visible. Next time make him about 20% bigger, or overlap him with the pyramid edge (same note as the screener).
- **First 60 s: GO.** The pyramid is the opening image. "Portuguese Man o' War" is at word 32, the committee/clone twist lands at about 0:41, and death 1
  comes before the 1:19 chapter change. f_001 to f_003 are clean, on-model and match the narration (party balloon, float and tentacles, stranded man o' war).
- **Description: blocking defect, fixed by the CD.** With chapters filled, it was 6,151 characters. `studio/youtube.py` hard-cuts at 5,000 characters,
  which would have cut a source URL in half and dropped the DISCLAIMER, the AI USE disclosure and the hashtags. I removed 26 redundant sources
  (Wikipedia, press rewrites of the same study, duplicate species pages), going from 76 to 50 and keeping at least one institutional or primary source per item.
  The filled description is now 4,481 characters (4,497 bytes) with no angle brackets, and `validate metadata` returns OK. All facts stay sourced in `facts.md`.
- Chapters: 12, starting at 0:00, all over 10 s, in video order. Tags and playlist `ocean` are fine.
- Process note for the titler: check that the length of the *filled* description is at most 4,800 characters before handing off. Nothing else is blocking.
  Pronunciation risks from the script gate went through QC and the screener. The owner should still listen to 0:00 to 1:30 in the Studio review window.
