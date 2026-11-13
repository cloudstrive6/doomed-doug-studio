# 046 decisions

## 2026-11-13, creative director: script approval (draft 2)
- Read: brief.md, script.md (draft 2), script_review.md round 2 (PASS, 0 fact errors, 8/8/8), facts.md (Malheur age, Pando wording, tyre analogy).
- Approved. The axis holds (inside something, under the ground, under a forest), every item opens on its hook, the honesty line (Shark Bay seagrass)
  keeps the title promise exact ("biggest fungus ever found"), item 3 stays a tape-measure gag with no anatomy and no food-safety or medical advice,
  and the costumes play deadpan.
- One edit made (the screener's optional polish): the payoff promise in sentence 2 was vague ("one fungus eating a whole forest"). It now reads "By the
  end, Doug is standing on one fungus bigger than a thousand football pitches, and it has been eating that forest for thousands of years." (Sourced:
  965 ha is about 1,350 pitches, and the age is at least 2,400 years per Guinness and Ferguson et al. 2003.) Adds about 13 words, still inside the target length.
- Kept "It doesn't need sunlight. It has a vine." It is set up for the dodder's "It has a tomato." and it's the better joke; item 1's density is acceptable.
- Series bible: counter total 356, 046 log row added, deaths 353 and 356 noted as played flat.
SCRIPT: APPROVED

## 2026-11-13, director: shotlist (184 shots), asset requests, Shorts
- Shotlist: 184 shots, narration matches the approved script word-for-word (2,015 spoken words), Doug in 68% of shots, and no
  build-free stretch over about 4.6 s by estimate. Generator: `build/gen_shotlist.py` (git-ignored scratch, as in 045).
- HUD: DOUG DEATHS top right, plus the HOW BIG meter (a `label` at (1600, 238) with `tape_measure` at 0.17). It is unspoken, from s005
  (1 M) to the boss (ABOUT 965 HECTARES, stamped red from the boss title card on).
- Overgrowth deaths: death 354 uses `doug_fuzz_silhouette` (its single use this episode, art bible rule). Death 355 uses a new,
  separate drawing, `pine_costume_fuzz` (the pine costume overgrown, a faint foxfire glow, cap on top), so the fuzz silhouette is not
  used twice. The other deaths: 351 is the flat tomato suit in dodder threads plus the cap and the AGAIN stamp; 352 is a black card
  with the handset, the cap and ghost Doug; 353 is the cap on the bitten aspen sprout (flat); 356 is the fallen Douglas-fir suit with
  the cap in the honey mushrooms (flat).
- Item 3 has no worm drawing at all (brief sec 7). The tape measure, the bus and the calendar carry it.
- Section headers "Under the ground." / "Under a forest." are white header cards with `topbar: false`. "INSIDE SOMETHING." is shown
  above the item 1 title, unspoken.
- Shorts (`shorts.json`): short01 Pando (s097-s108 + hook), short02 Cable-Cutting Tree (s080-s089 + hook), short03 Blue Mountains
  (s173-s181 + hook). Each ends on its Doug beat. **The titles are working placeholders** (the validator needs a non-empty title),
  and the youtube-titler owns the final titles and descriptions.
