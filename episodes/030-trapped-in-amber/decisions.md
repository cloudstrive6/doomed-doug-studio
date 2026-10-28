# Episode 030: decisions

## 2026-10-28, creative director: script gate (draft 3)
1. **Script APPROVED.** In screener round 2, facts, hook, structure, voice, TTS, policy and length all passed except two one-line
   wording fixes. The screener said that once those were made, only the two lines needed confirming. I confirmed both in script.md
   and facts.md:
   - Line 123 says "This hell ant's final victim was a young cockroach relative". facts.md row 58 quotes NJIT's "unsuspecting final
     victim".
   - Line 229 says "found in amber from the same area". facts.md row 96 cites Bolet et al. 2021 / UCL for "same area".
   No new claims were added, so no full re-screen is needed.
2. **Rule 9 Flesch (A2): accepted at about 75 for this episode only.** The average sentence length (15.3) is in its band, and the
   longest sentence is at its limit. Getting Flesch to 72 would mean merging about 24 short punch lines, and retention depends on
   those. Plain words are a feature for a 10-minute retention target. The style bible band is not widened yet. If the next two
   scripts also come in above 72 with the sentence-length band met, I will propose widening it to 60-76.
3. **CD edits made at the gate (A1, A3).** These are wording-only, with no new facts:
   - The Wrong Dinosaur is trimmed from 262 to 250 words. The repeated "tip of your finger" size line is cut, "March twenty twenty" is
     now "that March", and "they found" is now "found".
   - "Here's where it gets strange." (item 6) is now "Then it got awkward." The repetition with item 7's "strangest thing" is gone,
     and the retraction is played deadpan.
   - The spoken total is now 1,973 words, about 10:07, inside the 1,950-2,350 band.
4. **Read against the brief, it delivers:**
   - The first sentence is concrete (the tick and the feather, 99 million years).
   - The payoff promise (the owner of the first dinosaur tail in amber) comes by word 32, and The Tail pays it off.
   - "The Tick." is at words 34-35, and its twist is at about word 116.
   - The size axis is told in four spoken bands.
   - The counter goes from 240 to 246, with two survivals.
   - Running gags: "Doug did not agree to this" once and the costume gag once. Callbacks to 019 and 012 are one sentence each.
   - Kachin/SVP is on a sober card with no Doug.
5. **Notes for the director (not blocking):**
   - The young dinosaur at the boss and the hatchling stay hunched and sharp-clawed. No big eyes, nothing cute.
   - The closing cap-in-amber is a prop sealed in a bead. Doug is never shown inside amber (012's one-off "preserved" variant is not
     a precedent).
   - The Jurassic Park card stays generic: no film title, logo or poster likeness.
6. **Notes for the titler:**
   - The title must promise "creepiest things found in amber" and nothing the video lacks: no "dinosaur DNA", no "alive".
   - Don't reuse 029's "How the X..." formula.
7. **Series bible:** the 030 log row and the counter total (to 246) are added at the final package gate, as with 028 and 029.

## 2026-10-28, director: shotlist
1. **216 shots**, every spoken word of draft 3 once and in order (1,973 words, checked word by word against script.md). s001 is the
   thumbnail (`scene_ref`, "A tick has been holding on", min 2.0 s); `thumbnail.json` is the graphic designer's and does not exist yet,
   so validate flags it until then. Doug (incl. ghost) is in 94% of shots; every shot has an `appear` build within 4.5 s (estimated at
   3.25 words/s).
2. **Episode devices:** every specimen is an `amber_bead` + specimen + `amber_bead_glint` group on a "museum shelf" card whose backdrop
   darkens one step per spoken size band (Bugs `#4a3520`, Bigger `#3b2a17`, Backbones `#2c1f12`, Dinosaur `#1a120b`), so the size axis
   is also a value ramp. Each item ends on the **specimen tray** (8 slots): the item's bead drops in on the kicker line and a red `?` marks
   the next slot. Slot 8 gets the cap-in-amber bead at the close. Counter on every shot from s002 at 240, ticking to 246 on the six death
   beats; not on the Kachin/SVP sober card (s202-s205: no Doug, no counter, no wordart, white labels only) or the big end card.
3. **CD notes applied:** the young dinosaur and the adult (`feathered_dino_looming`) and the enantiornithine parent are requested hunched,
   toothy and not cute. The Jurassic Park card is `film_poster_generic` (no title, logo or poster likeness) with a mosquito bead and a `?`.
   Doug is never inside amber: s211 seals only the cap (`doug_cap` in a bead) while ghost Doug floats away; s212-s213 show it in slot 8.
4. **Stage directions not used (to avoid capless-Doug one-offs):** the cap snagged on the silk (The Web) and the cap on the saddle
   (The Wrong Dinosaur). s053 instead shows Doug walking off while a hell-ant silhouette appears (re-hooks into item 3); Doug keeps his cap
   in both survivals. No `cap_off`/`cap_taken` anywhere in the episode.
5. **Silhouette glows** use the purple `#5e4670` spray on the brown/red forest and shelf backdrops (art bible: red speckle on brown reads
   as blood); only the night-forest snake reveal (s128, dark-cool ground) keeps red. Silhouettes use `glow_r: 0` with a body-centre spray.
6. **Shorts:** short01 The Wrong Dinosaur (s132-s143, loop = the toothed bird at the nest, tease s178), short02 The Hell Ant (s056-s065,
   loop = Doug's costume fate, tease s075), short03 The Tail (s184-s195, loop = what came with the young one, tease s209). Titles and
   descriptions are left for the youtube-titler (validate reports only "missing title").
7. **Keyframes not run:** 40 drawings are missing (asset_requests.md) and the renderer stops on a missing asset. I previewed 48 shots with
   placeholder ellipses for the missing drawings to check Doug placement, ground lines, counter zone, the wave and the tray layout. Once
   the illustrator delivers, run `python -m studio keyframes 030-trapped-in-amber` and check the beads (specimen readable at tray scale
   0.22), the hand-held props (`dna_kit`, `tiny_saddle`, `torch`) against Doug's hands, and the costume on the `crouch` pose (s073-s074).
