# Episode 003: decisions

## 2026-10-01: episode selected (creative director)
- Picked backlog idea #5, mass extinctions (score 8.6, "next up"), per growth memo 2026-10-01 rec. 1. Engines: Fossil
  "How Long You'd Last in Every Prehistoric Era" 8.98M in 51 d; Mr. Science "When Earth Had Supermountains" 2.62M in
  9.6 d (3718 vph) and "When Antarctica Was a Jungle" 4.07M (3.1x). Opens the `prehistoric` playlist.
- **Title skeleton changed from the backlog's T1 to T2** ("How Doug Would Die in Every Mass Extinction"). This revises the
  T1 part of my memo decision 3 (2026-10-01). Reasons: ep 002 is T1, so T1 again would repeat the formula back-to-back,
  and the backlog title has no death verb or dread adjective (titler rule 4). The memo's argument (a second T1
  reading speeds up the formula decision) is noted. Venom (#14, T1) is still held until ep 002 day 7 and gives that reading later.
- No "sixth extinction" tile or item (memo's thumbnail idea): debated framing, preachy-tone risk, and "every" stays
  defined as the Big Five.
- Planned deaths: 9 (counter 18 to 27), survivals at items 4 and 8. New lore candidate: the time machine (added to the
  series bible at script approval).
- Stage stays `idea` until the script-writer delivers draft 1.

## 2026-10-01: draft 3 (script writer)
- Applied draft 2 review fixes 1 to 4. Killer Moss kicker is now flat ("a plant with no real roots and no flowers"); the
  doormat line stays. Hot Tub Doug beat clause is now flat ("the water around him keeps getting slowly, steadily warmer").
  facts.md: PMC8792005 relabelled Bridge, Baird, Pandolfi, McWilliam and Zapalski 2022.
- A1: Pangaea Splits gets one sourced mechanism paragraph on the intrusive CAMP sills (Davies et al. 2017), 237 to 290.
- A2: Ozone Hole Doug beat now 20 words; the supernova sentence was tightened by 10 words so the item stays at 270 and the
  zone shift does not move (A5).
- A3: the Deccan "teams disagree" sentence is kept: cutting it would take Deccan to 256, under its 260 floor.
- Total 3,159 spoken words.

## 2026-10-01: script draft 3 APPROVED (creative director)
- Screener PASS (0 fact errors, 0 policy items, hook 9/10). Checked against the brief: era axis and five spoken headers
  in order; "Killer Moss." at words 33-34, twist at ~127 (under 145); counter 18 to 27 with at least one death per
  section, survivals at items 4 and 8; every gag as briefed (opener line once, moss and Lystrosaurus befriended, one
  costume callback, extinguisher/marshmallow callback, cap fossil in the iridium layer); no sixth extinction, no
  modern-climate commentary; deaths stay cartoon and off Doug's body; outro 20 words. Title promise met.
- Applied directly (no words added; 3,159 to 3,158; Pangaea Splits 290 to 289):
  - A1: "Some of the magma never reached the surface. Underground activity began" became "As in Siberia, some magma
    stayed underground. That activity began" (deliberate flat callback instead of a rerun of the Siberian twist).
  - A2: "rock rich in oil and ancient remains" became "rock rich in oil and organic matter" (matches Davies 2017).
  - A4: facts.md Ozone Hole note now quotes the draft 3 supernova framing.
- Not applied: A3 (Killer Moss kicker restates roots/flowers). It is flat on purpose, rule 10 is at its limit there,
  and it reads fine as a button. A5 and A6 carried to the director and visual screener (Hot Tub steam off the water,
  not Doug; sunburn as a colour fill and nose flakes only, locked design).
- Note for the director: "the size of the United States" is used three times (Gondwana x3, Siberia, CAMP). Accepted
  in narration; vary the on-screen visual (map overlays at different scales) so it does not look repeated.
- Time machine adopted as series lore (series bible updated): the vehicle for the `prehistoric` playlist.

## 2026-10-01: thumbnail + art/package GO (creative director)
- Thumbnail (single option): **GO.** Art director PASS, visual screener PASS. It is an Archetype A 3x3 grid in era order that
  darkens from icy blue to soot black, with the Chicxulub boss tile bottom-right and a tiny Doug in a rubber ring in Hot Tub
  Ocean. The labels are the 9 chapter names and use no title words. It promises "one killer per tile, each one gets
  Doug", and the video delivers that. No gore, nothing kid-coded. I would click it.
- Tweaks applied myself (no layout change, tile geometry untouched):
  - All 9 `label_size` 42 to 48. The screener's ~50 would need shorter tiles, which means moving every absolute
    child coordinate. At 48 the descenders ("Traps", "Purple") still clear the next row's frames, and the labels hold up
    better at 168x94.
  - Gondwana Ice: the ice-cap outline is darker (#1d5f9a to #0b2f5c), so the white cap separates from the green landmass. This is
    still the weakest tile, but it reads as ice on a continent at 320x180. Accepted.
  - Re-rendered with `python -m studio thumbnail` and checked at full size, 320x180 and 168x94. s001 uses `scene_ref:
    thumbnail`, so the opening shot picks up the change automatically.
- Package: **GO.** Title "How Doug Would Die in Every Mass Extinction" (T2) is delivered: at least one Doug death in each
  of the Big Five sections, counter 18 to 27. Description, sources, AI-use and disclaimer blocks are present, the playlist is
  `prehistoric`, and `validate metadata` and `validate shotlist` both report OK.
- Art: **GO** (art_approved stands). The visual screener's polish items 1-5 (s047 flipper, text over outlines, s210
  dashes, s098 map crop, s228/s229 bar labels) are optional. The director may do them in the editor pass if time
  allows, re-rendering only the touched shots. Not blocking.
- Next: the showrunner sets `packaged`, then the editor narrates and renders.

- 2026-10-01: packaged. Script 3 rounds (sourcing/joke density), art assets 1 round, keyframes 2 rounds (new on_back death pose + sunburn gear + time_machine added), thumbnail 1 round. Risks: channel speaking_rate raised 1.1->1.145 (config/channel.yaml) to reach 190+ wpm; validate.py now strips HTML comments from the word count; audio pronunciation of era names not listened to; minor polish items left (s047 flipper, s098 crop, s210 dashes, s228/229 bar labels).

## 2026-10-01: FINAL package approval after final render (creative director)
- Gates: QC 0 problems, 997.1 s (16:37, in the 15-18 min target); visual screener round 5 PASS; `validate metadata` OK.
- Title: keep **"How Doug Would Die in Every Mass Extinction"** (T2). None of the alternates is clearly stronger. "Creepiest
  Extinction Triggers" and "Most Disturbing Discoveries" are the formulas we used back-to-back in earlier episodes and promise
  findings rather than Doug. "Deadlier the Longer You Stay" is weaker for search. "How Every Mass Extinction on Earth Would Kill Doug"
  is the same promise in more words. The video delivers the title: at least one Doug death in every Big Five section, counter 18 to 27.
- Thumbnail: the 3x3 era-ordered grid still reads at feed size (thumbnail_small). Labels are legible, the boss tile sits bottom-right,
  and Doug in the rubber ring is visible. No gore, nothing kid-coded. I would click it.
- Description: the hook sentence matches the video. The comment prompt, sources (NHM, Sam Noble, Science Advances, USGS), the
  cartoon disclaimer and the AI-use disclosure are all present. `{{CHAPTERS}}` is filled from chapters.txt at upload (youtube.py).
  Tags are on topic, and the playlist is `prehistoric`.
- Chapters: 12 entries. They start at 0:00, every chapter is longer than 10 s, they follow the script order, and the names match the
  thumbnail labels.
- First 60 s: thumbnail-grid open, then the time machine. "Killer Moss" is spoken by about word 33 and the twist ("helped start the
  first mass extinction") lands well inside 45 s. Samples f_001-f_003 are clean: Doug is on model, the headers are readable, there
  are no crops. The f_003 thermometer fill sits high for "-5°C". It is cosmetic and not blocking.
- Non-blocking carry-overs (s098 crop, Shorts preview edges) are accepted.
- Next: the showrunner moves to qc_passed and runs the scheduled upload (publishAt >= 1 day out).

FINAL: APPROVED
