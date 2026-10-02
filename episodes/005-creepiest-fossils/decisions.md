# Decisions: 005 Creepiest Fossils

## 2026-10-01: script gate (draft 3), APPROVED
- Screener round 3: PASS, with no required fixes. Hook 8, structure 8, voice 8. 3,252 words, about 16:41.
- Checked against the brief. Age axis youngest to oldest (28 kyr to 506 Myr), 12 items, "Frozen." and "Stone." headers,
  the item 1 name in the first 35 words, and the twist at word 137. The mummy/fossil honesty line is in item 1. The
  counter goes from 36 to 46 with survivals at Blue Babe and Zhùr, and Zhùr is played straight. One reef callback to 003,
  cartoon deaths only, and the humour is adult-coded.
- I applied advisory A6 myself. Line 174 now reads "preserved together, apparently while mating", which matches the
  hedged frame. I also corrected the stale "Draft 2" label in the header comment.
- Series bible: the death count goes up (36 to 46) and the episode log row is added at QC, which is the existing practice.

## 2026-10-01: art gate, APPROVED (recorded)
- Keyframes approved after fix rounds 1-2 (commit 2f6e051).

## 2026-10-01: thumbnail gate, APPROVED (with one CD tweak)
- Visual-screener PASS. The grid matches the brief: Archetype A 3x3 in age order, ice blue to brown to near-black, Stanleycaris
  as the red-glow boss bottom-right, Zhùr left off, no real photos, and no label shares a word with the title or alternates.
  It delivers the title's promise (every animal drawn as if it could get up).
- Tweak applied: Doug was ~6 px tall at feed size. Scaled 0.2 -> 0.3 (x 240 -> 246) in the fighting-dinosaurs tile and
  re-rendered. He now sits wedged between the two dinosaurs, and the red cap reads at 320 px.
- 2026-10-01 showrunner: script 3 rounds (fact/policy fixes), art 3 rounds (44 assets, 2 redrawn; keyframe fixes), thumbnail approved after Doug scale tweak (not re-screened at feed size). Engine/config: art-director added thumbs_up/sit_thumbs_up poses; editor lowered voice.speaking_rate 1.145 -> 1.10 in config/channel.yaml (narration was 208 wpm). Risks: no real photo insets (drawn stand-ins); Blue Babe age 36k vs newer ~50k estimates; Batagaika blood is a university claim, hedged; s019 narration says kneels but Doug sits.

## 2026-10-02: final package gate, APPROVED
- Inputs: QC exits 0 with no problems (1007.27 s, about 16:47), and the visual screener PASSED post-render round 3 (final.mp4, Shorts 01-03, thumbnail).
- Title: I'm keeping "The Creepiest Fossils That Still Look Alive" (T4). It breaks the run of T1/T2 titles from 001-004, so the formula isn't repeated back-to-back. It's also a curiosity promise the video keeps: every item is a find that froze at its moment of death.
  None of the alternates is clearly stronger. "How Doug Would Die in Every..." and "What Dying in Every..." would bring the T1/T2 formula straight back after 004. "Every Era of Earth" is a weaker click than "Still Look Alive". So no swap.
- Thumbnail (full size and 320 px): a 3x3 labelled grid in age order, going from ice blue to brown to near-black. Stanleycaris is the red-glow boss, and the red cap reads between the fighting dinosaurs at feed size. All of it is drawn, with no carcass photos or exposed tissue, and no label shares a word with the title. The cartoon blue on Blue Babe is a stylised take on the vivianite coat, which is acceptable.
- Description and chapters: "12 fossils" matches the 12 chapters (0:00 Intro, then 0:10 Sparta through 14:43 Stanleycaris). Six museum or university sources are listed, along with the cartoon-death disclaimer and the AI-use disclosure. The tags are on-topic, the playlist is "prehistoric", and there's no paid promotion.
- First 60 s: the script names the item 1 header (Sparta the Cave Lion Cub) right after the two-line opener and "Frozen." The twist (the cubs were born about 15,000 years apart) lands at about 40 s, inside the style-bible window. Samples f_001-f_003 are clean: the title plate reads, the 15 M / 1-2 MONTHS OLD labels read, and the "28,000 YEARS AGO" booth is whole. Doug is on-model, with no gore and no nursery tone.
- Accepted minor issues (not blocking): the s019 narration says Doug "kneels" while the drawing shows him sitting. The Blue Babe age is given as about 36 kyr, though newer estimates are older. The map icons in s008 and s043 sit slightly off-centre.
- Series bible: per existing practice, the death count goes from 36 to 46 and the episode-log row is added at QC/upload.

FINAL: APPROVED
