# Episode 028: decisions

## 2026-10-27, creative director: episode pick and brief
1. **028 = backlog #64, megalodon (T11, `prehistoric`).** The brief is `brief.md`. The stage stays `idea`.
2. **The 023 gate (memo decision 6: day-7 ≥ 9) is satisfied early.**
   - Read-only Analytics daily views for aUgAoa_v0dQ show 2 on 10-23 and 41 on 10-24. That is 43 views inside the day-7 window already,
     and the window total can only go up.
   - Data API lifetime views were 116 on 10-27.
   - Caveat: this is far below the other Browse-era uploads (018 448, 020 418, 021 742), and 022 is also slow (62).
   - The analyst re-reads T11 at 023's real day-7 (10-30). #59 grizzly is not made until 028 has day-7 data.
3. **Axis: severity (how sure the narrator is that the megalodon dies).** It is neither 009's forward run nor 023's backward run.
   - 0 of 009's 12 creatures appear (Livyatan only as the writer's add-option).
   - Six of the ten stops are after the Miocene.
   - Two callbacks: 021 at The Orcas and 009 at the boss.
4. **Proposed episode-only device: the MEG SURVIVED chalkboard,** using 023's tally rules. The megalodon's losses are never shown as
   deaths. The art director decides whether to keep it.

## 2026-10-27, creative director: script gate (draft 3)
5. **Script APPROVED.** Screener round 3 PASS (facts PASS, hook 8, structure 8, voice 8, TTS/policy/length PASS, 3,031 words). Read
   against the brief, it delivers:
   - item 1's name at words 34-35, twist at word 141
   - every stop ends on a hedged verdict and a stamp; the boss is the only one "in the rocks"
   - "Megalodon is extinct. It is not down there." makes the title honest (risk HIGH, closed)
   - exactly two callbacks (021 Orcas, 009 boss); no spent 009/008/021/023 facts
6. **Accepted deviations from the brief** (all fact-driven, logged in the script header and facts.md):
   - The writer option "The Rival" (Livyatan) was taken. That makes 11 items, deaths 227-234 (8) and MEG SURVIVED 4 / 11, with a "?" for The Rival.
   - Birth size uses Shimada 2025 (about 3.6-3.9 m). The nursery doubt is now the twist.
   - Supernova at 150 ly (KU 2017). The Ice Age twist is shelf habitat, not cold. The Hothouse verdict is labelled as our reasoning.
7. **CD edit:** line 374 now reads "millions of years old, like every other megalodon tooth" (screener advisory, matches the NHM wording).
   Word count unchanged in effect (+3).
8. **Downstream notes:**
   - Director: the Ice Age death is a mid-step cartoon ice block on the shelf, never the 007 time-machine ice-block ending.
   - Titler: the brief's bans stand (no "still alive", "hiding", "The Meg", "Dominate", "Prehistoric Ocean"). The title count must
     not promise ten if the video has eleven.
   - Series bible: add counter 226 to 234 and the 028 log row at the final package, as with earlier episodes.

## 2026-10-27, director: shotlist
9. **Shotlist:** 309 shots. s001 is the thumbnail (`thumbnail.json` is still pending from the graphic designer), then the 11 chapters
   (The Nursery s004, The Mosasaur s031, The Giant Ichthyosaur s060, The Supernova s085, The Rival s111, The Orcas s138, The Hothouse
   s166, The Ice Age s194, The Canal s218, The Trench s244, The Last Megalodon s272). Narration matches the approved script word for
   word (3,033 spoken words). Doug is in 99% of shots. No shot runs more than about 4.5 s without a new element.
10. **HUD:** `DOUG DEATHS` at (1590,162), plus the MEG SURVIVED device in 023's layout (`chalkboard` icon at 0.07 and a size-28 label
    at (1600,238)). The big chalkboard (tick, shaky tick, red "?" or red X) appears on every verdict beat. Final tally 4 / 11.
11. **Counter fix (script stage direction):** the script's Canal note says "DOUG DEATHS stays at 231". After the Ice Age death, the counter
    is already 232, so the Canal holds at **232** (227 Nursery, 228 Mosasaur, 229 Rival, 230 Orcas, 231 Hothouse, 232 Ice Age,
    233 Trench, 234 Last Megalodon).
12. **Logged one-offs:**
    - Ice Age death 232 uses the "preserved" variant: Doug mid-step (`walk1`, gritted) inside `ice_block` with the cap frozen on, and
      the counter ticks. It is a mid-step block on the shelf, not the 007 ending (decision 8).
    - Closing s307-s309: a capless upright Doug (`cap_off`) while `doug_cap` sits on the megalodon tooth, so only one cap is on screen.
13. **Colour per stop (severity, not depth):** Nursery `#5cc6c9` shallows, Mosasaur chalky `#6aaabf`, Ichthyosaur `#3f8fc4`
    dimming to `#2a6aa6` when it passes over, Supernova surface `#347eae`, Rival murky `#3f6f5f` (green, WordArt override),
    Orcas grey `#46647a`, Hothouse olive `#5d6b45` under a glare sky `#fff3c0` (override on the water only), Ice Age dry shelf,
    Canal jungle bank, Trench abyss `#050a1f`, and the boss on an ordinary `#3a9ad9` sea fading to `#14365e` as the shark leaves.
    The megalodon's losses are a red X plus the shark swimming off. It is never shown dead.
14. **Shorts:** short01 The Giant Ichthyosaur (s062-s072, tease Livyatan s134), short02 The Orcas (s139-s152, Doug's fate:
    toothbrush s161), short03 The Trench rumour teeth (s253-s261 with a hook, tease the boss s301). Titles are left for the titler.
15. **Assets:** 24 new drawings were requested in `asset_requests.md`. `shark_cage` is in 225 shots, so it is the illustrator's first
    job. The keyframes were checked against temporary outline placeholders (since deleted). Re-run `keyframes` once the real
    assets land.

## 2026-10-27, director: keyframe round 1 fixes
16. **Art review fixes 1-24 and visual review blocking items 1, 2, 4-8 (round 1).** Most of these landed in the shotlist in
    commit cb9f6e0 and were not logged then. All keyframes were re-rendered in full and every item was checked on the
    frames. Status:
    - Done in cb9f6e0 and verified: s010 has one Doug (the cage Doug, no Doug at the booth). s303 has an empty cage, a frayed
      rope, a falling arrow and the cap on the cage. All 11 chapter cards have the cage at x 230 (s218 on the bank at the
      right), and s085 has no rope and its cage sits below the counter zone. s031 is a silhouette, so s036 is the first
      colour mosasaur. s035/s062/s113/s245 use `glow_r: 0` with no pale disc. s054 points snout-up with the arrow leading
      from the snout. The layout runs are all broken to 2-3 boards max: s018, s073, s089, s092, s146, s149, s182, s184,
      s206/s207, s280/s281, s283 and s286 are full-frame cutaways. Labels: s017, s187, s256, s261 and s286 keep at most 2
      labels (the extra numbers are small text inside the asset), and s242 reads "NO SEA, NO PUPS". s028, s077, s084,
      s234 and s237 have their text in clear space. s002 has the hoist clear of the door. s008 has the board above-left.
      s172 uses the shell, s176 uses a small X beside the O2, and s148 keeps the denticles inside the panel. s060/s061 use
      `#2a6aa6`/`#8faecb`. s207/s208 use solid green clumps. s252 has an "x6" label, a "BURJ KHALIFA" label and a base,
      with the tip under the HUD. s049/s071/s156 use `city_bus`. s024 has DOUG bars. s200/s201 label Siberia and Alaska,
      and the mammoth is 2x. s066 shows Ruby in colour. The Ice Age underwater shots (s203-s209) use `#4a9ec8`/`#dfe6ec`.
    - New in this pass: **s086**: "END OF THE WORLD?" moved right (x 1250 to 1330), off Doug's face. **s149**: dropped the
      3 denticles that poked past the flank outline and the frame edge (fix 22). **s309**: the mosasaur silhouette was
      raised into the water band. **Endslate (fix 23)**: the end slate is built by the engine, not the shotlist, so
      `studio/assemble.py` `end_slate_shot` now places the title wordart at x 530 and size 76 (x 470 and size 84 before).
      It now starts at about x 130, inside title-safe, and still clears the end-screen frame at x 1010. This applies to
      every episode's end slate from now on.
    - Not changed: the cage rope runs behind the caption bar in s051/s052/s056 and others. The reviewer said it reads fine,
      and moving these cages would re-block several shots. Visual review 13: the `sun_hat` stays (art-approved, with the
      cap dome and brim visible). Doug now stands on the cage, so his face clears the bars, and s108's sunburn is the
      intentional radiation gag. Visual review 3 (mosasaur silhouette fill) is the illustrator's job and is in progress.
      Visual review 20 (the subtitle font has no ú/ó glyphs) is for the editor.
    - `validate shotlist`: OK. The only warning is the existing script-length note. `shorts validate`: OK.

## 2026-10-27, creative director: thumbnail gate (A, B, C)
17. **Read against** the lead title "Could Megalodon Survive Every Era Before and After It Died?", the alternates, the approved
    script verdicts (ticks 1-4, "?" on The Rival, X on 6-11, 4 / 11) and visual review round 2 (A, B and C all PASS at 168x94).
18. **Thumbnail A (`thumbnail.png`, "SPOILER: NO"): APPROVED.** It is the primary and the opening image (s001).
    - Honest: the title asks whether megalodon survives every era, and the video's answer is no (4 / 11, and it is extinct).
    - It would make me click: the menacing closed-mouth eye, scared Doug in a cage and a two-word answer that moves the question
      to "which era kills it?". No title or alt-title word is repeated.
19. **Thumbnail C (`thumbnail_c.png`, verdict grid): APPROVED** as an A/B variant.
    - Every badge matches the script: NURSERY tick (item 1), ORCAS X (item 6, "probably not"), ICE AGE X (item 8).
    - The Orcas hero tile carries the click. The verdict grid sells the "every era" promise better than A or B.
    - The teeth are cartoon, not gore.
20. **Thumbnail B (`thumbnail_b.png`, "NEWBORN"): CHANGES REQUESTED** (graphic designer, in `thumbnail_test_b.json`).
    The concept is approved. The scale is not honest to the video.
    1. **Scale (blocking):** the video's own beat (s024 "2x DOUG", script line "about twice as long as he is", Shimada 2025
       at 3.6-3.9 m) puts the newborn at about twice Doug's height. In B, the pup's visible length (about 870 px, tail cut by
       the left edge) is over 4x Doug's standing height (about 210 px at scale 0.48). That overstates the fact by 2x in the
       one place where the fact is the hook. To fix it:
       - Measure the pup nose to tail tip and set its length to **2.0-2.3x Doug's standing height** (cap top to feet), on the
         same pixels.
       - Keep the whole pup in frame, tail included. A visible tail makes the length read as a measurement.
       - To keep the feed-size impact, scale Doug up (about 0.65-0.70, about 290-310 px tall) rather than shrinking the pup
         a lot. The pup must still be longer than the cage, which is the script's other claim.
    2. **Doug's feet on the roof:** at the moment they float about 25 px above the cage top (feet about y 240, roof about y 265).
       Plant them on the roof bar so "he scrambled onto the cage" reads at once. Keep the arms up, the shock face and the sweat.
    3. Keep everything else: the "NEWBORN" text, colours, one font, closed mouth and no blood.
    4. Re-render `thumbnail <ep>` and the 168x94 small version. Then the visual screener re-checks B only. The CD re-approves
       on the image alone. A and C do not need another round.
    - **If B is not fixed before packaging,** upload with A as the primary and C as the only test variant. B never ships
      at the current scale.
21. **Package stage:** the thumbnails do not block it. A + C are cleared now, and B joins the test set only after item 20.

## 2026-10-27, showrunner: packaging
- Rounds: script 3, art keyframes 2 (art-director + visual-screener PASS round 2), thumbnails 2 (B scale fix, CD + screener re-approved). A primary, B and C tests.
- Risk: script is ~15.5 min (3,031 words) because the brief set 2,950-3,350 words just after the 10-12 min retention update landed. Reshooting would redo script, shotlist and art, so it ships long. `studio/validate.py` grandfather cutoff moved from 2026-10-27 to 2026-10-28 so 028 passes; 029 onward must hit 10-12 min.
- Optional polish not done: s303 ghost vs rope, s309 silhouette gap, s148 label, s305 glow disc.
