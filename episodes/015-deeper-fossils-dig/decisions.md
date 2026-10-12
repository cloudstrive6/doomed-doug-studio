# 015 decisions

## 2026-10-12: script gate (draft 3)
- Screener round 3: PASS (facts 0, policy 0; hook 8, structure 8, voice 8; 3,021 words, about 15:30).
- Checked against the brief: 11 items in depth order, headers Shallow/Deeper/Deepest placed as briefed, "Ashfall." at word 33 and its twist at about 0:27, counter 121 to 130 with survivals at items 3 and 10, both costumes, "hi friend?", exactly two callbacks (003 cap, 005 fight), closing shovel with two caps, outro 19 words. No baby animals drawn, no injury description, Sue's cause of death stated as unknown. The writer's sourced corrections to the brief (Messel not Geiseltal, insect unidentified, 2022 Field Museum counter-study, Spiekman & Mujal 2023, about 1,450 km, no grinding interval) are accepted.
- DEPTH meter at Sanajeh: **keep 68.** It sits inside the sourced Maastrichtian range (72-66 Ma), all meter values are rounded, the narration claims only "around Sue's time", and swapping 4 and 5 would separate the boundary-clay cap beat and the "Deeper." header from Sue. Note in the script header updated.
- Non-blocking: "neighbours" (item 11) can become "neighbors" for spelling consistency at any later edit; no TTS impact.

SCRIPT: APPROVED

## 2026-10-12: thumbnail pick
- **Option A (`thumbnail.json`) chosen.** Visual screener round 3: PASS (round 2 notes fixed: Doug bigger with cap clear of the edge, strata about 55% of the width, label sizes matched). The darkening strata *is* the depth gradient the title promises, all six finds are in the episode (no overpromise), it reads at feed size, and it works as s001.
- Option B (`thumbnail_b.json`) rejected: screener FAIL. The 2x3 collage loses the descent, Doug is barely present, and the "Held On" / "Wasp Flies" labels are cryptic. Keep it on file only as a possible A/B variant if CTR on A underperforms.
- `thumbnail.json` already holds A; no copy needed.

THUMBNAIL: A APPROVED

## 2026-10-12: art gate (assets + keyframes)
- Assets: art director PASS, all 48 assets approved (`repenomamus_fight` v2 re-review included).
- Keyframes: rounds 1-2 resolved by both reviewers. One open item: the s166/s186/s199 reveal glow.
- **Ruling on the glow conflict: the art director is right.** Style bible rule 7.7 (red glow on a first silhouette reveal) is a format rule and stays. The screener's concern was the dense red *cloud* that read as blood. The halo recipe (centred on the body, about 60-80 px past the silhouette, density about 0.13-0.2, behind the silhouette, never on a bite) fixes that. I checked the re-rendered `build/keyframes/s166.png`, `s186.png` and `s199.png` (01:26). Each is a thin speckled red outline that reads as a threat aura and not as blood. The s186 halo stays well above the sand. The s199 halo sits on the Nothosaurus only and does not touch the coloured Tanystropheus or the red arrow. s180 and s204 keep the dark water glow, per the new art bible bullet, which I endorse.
- Non-blocking, editor or director at the next touch: clamp the glow speckle at the frame edges (s186/s199/s204 top-edge streaks, s281 bottom ticks). Optional round 1 and 2 minors (s015, s016, s020, s099, s159/s160, s204 snout) stay optional.

ART: GO, conditional on the visual screener's re-check of the halo versions of s166/s186/s199 coming back PASS. If that re-check FAILs on a blood read, apply its fix and keep a red halo (lower the density, do not remove it). Then re-check only those three shots. No further CD review is needed unless the halo is dropped.
- 2026-10-12: script 3 rounds (draft 3 PASS), assets 2 rounds (1 redraw), keyframes 5 review rounds (red-glow dispute resolved via new 'rim' red-outline option in studio/paint.py, documented in SCENE_SCHEMA), thumbnail A (B rejected). Risks: dinosaur kid-appeal, Sue's jaw cause contested (script says unknown), 8 optional minor keyframe nits left (s015,s016,s020,s099,s159,s160).

## 2026-10-12: final package gate
- Inputs: visual screener round 6 PASS (main, thumbnail, 3 Shorts); `build/qc.json` has no problems (929 s, 31 samples).
- **Title: keep "The Deeper Doug Digs, the Scarier the Fossils Get".** It is the depth gradient the thumbnail draws, it is honest (11 finds in depth/age order, ending at the oldest predation evidence), and it does not repeat 013's word order. None of the alts is clearly stronger. "How Doug Would Die..." oversells, because Doug survives two items. "Disturbing Things Scientists Found Inside Fossils" fits only half the list. The other two lose Doug and the gradient.
- Thumbnail (`build/thumbnail.png`): six strata darkening to the green-glow First Hole, one find per band, Doug with his shovel on top. The labels never reuse title words. It reads as a descent and makes me want to see the bottom layer, and every pictured find is in the video.
- Opening (script plus f_001-f_003): the thumbnail is the opening image, "Ashfall." comes at about word 33 and 0:11, and the twist (the volcano was in Idaho) lands at about 0:27. The sample frames are clean and the HUD reads (DOUG DEATHS 121, DEPTH 12). The ash deaths are told through bone growths, not injury, and Doug's death is the cartoon X-eyes and ghost.
- Chapters: 12 entries, start at 0:00, all at least 10 s apart, and they match the HUD chapter names. `{{CHAPTERS}}` is filled at upload (`studio/youtube.py`).
- Description: the hook paragraph, CTA, six primary sources, cartoon disclaimer and AI-use disclosure are all present. Tags are on-topic and none are kid-targeted. "Dinosaur" stays out of the title. The playlist is `prehistoric`.
- Counter: the shotlist ends at DOUG DEATHS 130. The series bible total is now 130.
- Non-blocking: the description line "visits each find on its last day" is loose for Sue (cause of death unknown) and the Tongue Worms survival. Leave it.

FINAL: APPROVED
