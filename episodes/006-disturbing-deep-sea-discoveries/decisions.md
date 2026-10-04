# Decisions: 006 Disturbing Deep Sea Discoveries

## 2026-10-04: script gate (draft 2), APPROVED
- Screener round 2: PASS, no required fixes. Facts 0 errors, hook 8, structure 8, voice 8, policy 0 items.
- Checked against the brief: depth axis 20 m to 9,533 m, 12 items, gauge drops at every item, "Sunlit." / "Pitch black." /
  "Rock bottom." headers (the last at about 65%). "The Sharkcano." is at spoken words 31-32 and the twist lands at about word
  140 (inside 0:45). Counter 46 to 56 with survivals at the crop circles and the golden orb. Befriending at 1, 8 and 12, the
  cap survives at 1, 5, 6, 9 and the finale, one 001 callback, no costume, suitcase or time machine. Nothing from 001's item
  list returns. Sharks never hurt Doug. Brine, acid, heat and pressure deaths are all cartoon with zero bodily description.
  Mining is neutral and dark oxygen is stated as contested (both sides plus the April 2026 editor's note). The golden orb is
  identified (NOAA/Smithsonian, April 2026), so it plays as the anticlimax and the "unexplained" promise rests honestly on
  Kavachi's sharks, Taam Ja', the Upsweep and dark oxygen. The working title does not say "Can't Explain".
- CD polish applied myself (no fact changes): line 37 "They were swimming inside the crater" became "That's the crater"
  (removes the repeated "swimming inside"); line 151 kicker now opens "A hundred and twenty thousand years of venting."
  (removes the echo of line 141); line 25 split into two sentences ("...standing on end. That's how close..."). Footer
  stats updated: 3,173 words, about 16:16, inside the 3,100-3,400 target.
- Lore: the "LIVE" feed ending is adopted as the standard closing image for `ocean` episodes (series bible updated).
  The death count (46 to 56) and the episode-log row go into the series bible at QC, per existing practice.
- Notes for the director/editor: the fingernail pressure analogy is used twice on purpose (two men at 1,600 m, a small car
  at 9,533 m); stage it as a visual callback. Respell "Taam Ja'" in the TTS input if Chirp mispronounces it.

## 2026-10-04: thumbnail + Shorts titles, APPROVED (CD side)
- Thumbnail (`build/thumbnail.png`, `thumbnail.json`): approved with no changes. Archetype A 3x3, white canvas, depth-ordered
  tiles turquoise to navy to black, boss "9,533 m" bottom-right with red glow, tiny Doug in the brine lake as the one
  human-for-scale gag. No label repeats a title or alt-title word (title = depth frame, grid = items). Readable at 320 px and
  168 px: every subject keeps its silhouette, and labels are 2 words or fewer. No gore, no shark attack, no Titan imagery.
  Weakest tile is "Blue Hole" (abstract shaft plus "?"), but the label and the "?" carry it, so it stays.
  Labels are short forms of the chapters (Brine Lake = Jacuzzi of Despair, Iron Snail = Scaly-Foot Snail, Tar Volcano = Asphalt
  Volcano, 9,533 m = Deepest Ecosystem). This is accepted because "of" and "Deep" are title words.
  A visual-screener pass on the thumbnail is still required at the package gate.
- Shorts titles and descriptions written by CD (titler job), all sourced in facts.md:
  1. "This Blue Hole Is So Deep the Cable Ran Out First" (Taam Ja', 420 m, Dec 2023)
  2. "The Ocean's Loudest Mystery Sound Turned Out to Be Ice" (Bloop = icequakes; Upsweep still unresolved)
  3. "This Underwater Lake Kills and Preserves Whatever Falls In" (Jacuzzi of Despair)
  `python -m studio shorts validate` OK; `validate metadata` OK.

- 2026-10-04: Script 2 rounds (r1 FAIL on 2 facts), art/keyframes 2 rounds, thumbnail 1 round PASS. Risks: Taam Ja' pronunciation untested (no TTS respell support); dark oxygen disputed; 17:18 runtime.

## 2026-10-04: final package gate, APPROVED
- Screeners: visual-screener post-render round 2 PASS (all four round-1 blockers verified in the re-rendered final.mp4
  and the three Shorts, no regressions). QC `build/qc.json`: 0 problems, 1037.8 s (17:18). Thumbnail PASS (unchanged).
- Title: keeping "The Most Disturbing Discoveries at Every Depth of the Ocean" (T3 depth gradient, the strongest proven
  formula, and the video delivers it exactly: 12 real discoveries in depth order, 20 m to 9,533 m). None of the alts is
  clearly stronger. "How Every Deep Sea Discovery Would Kill Doug" relies on a character nobody knows yet, and the
  "Scientists Found" and "Scariest Places" variants are weaker restatements. Title and grid split the work cleanly
  (title gives the depth frame, tiles give the items, no shared words).
- Thumbnail: 3x3 depth-ordered grid, with turquoise to black reading as "going down" at feed size. The brine-lake Doug
  is the one human gag and the 9,533 m boss sits bottom-right. Drawn only, no gore, no real tragedy imagery. I would click.
- Description: the first two lines sell the hook (sharks in a volcano, a lake under the sea, dark oxygen, 9,533 m).
  It has a comment prompt, 6 primary sources (Nature, NOAA, UW), a cartoon-death disclaimer and an AI-use disclosure.
  Not made for kids, paid_promotion false, playlist `ocean`. Chapters (build/chapters.txt): 13 entries from 0:00, all
  named after the items, all longer than 10 s, matching the script order.
- First 60 s: f_001 is the Solomon Islands map, f_002 the red-glow hammerhead silhouette in the crater, f_003 the
  satellite plume ("2022"). "The Sharkcano" is spoken at about 0:10 (word 31). The twist "The crater wasn't empty." lands at
  0:43-0:45, inside the 45 s rule, though only just. It is followed straight away by the silhouette reveal, the open
  question (how do the sharks cope) and the 2022 eruption beat, so retention has a reason to keep going at 1:00. Doug,
  the death counter (46) and "Doug did not agree to this." are all in the opening.
- Non-blocking carry-overs, fix in the engine or the next episode rather than here: depth meter over the left edge of
  map shots (visible in f_001), the meter scrolling in s068, "~9,533 M" vs "9,533 M" plate inconsistency, the Shorts
  meter crop edge, and the preview subtitle `[:40]` cut. Dark oxygen stays framed as contested, and the Taam Ja'
  pronunciation risk is accepted.
- Next episode note: aim the item-1 twist at 25-35 s rather than 43 s. A twist this close to the limit is a retention
  risk.

FINAL: APPROVED
