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

## 2026-10-28, creative director: thumbnail gate (A / B / C)
Checked `build/thumbnail.png`, `thumbnail_b.png`, `thumbnail_c.png` and the 168 px `_small` versions against the title
"The Creepiest Things Scientists Have Found Trapped in Amber". No visual-screener thumbnail report exists yet
(`visual_review.md` covers keyframes only and skipped s001), so this is the creative verdict; the package gate still
needs a visual-screener PASS on the three thumbnails.

**Verdict: APPROVED, no changes. A is the primary, B and C go into the test.**
1. **A (hero: 99 MILLION YEARS).** The strongest click. At feed size it reads in under a second: big toothy dinosaur,
   panicking Doug, glowing bead with the tick on a feather. The video delivers this exact image: s001 opens on it,
   s028 to s030 ("the feather's owner") and s208/s209 ("Young ones come with adults") show the same looming dinosaur over
   Doug. The text uses no title word.
2. **B (peril: STUCK).** It clicks and reads at feed size. The Doug-sized hell ant is in the video (s072 to s075, the
   costume beat). Doug in liquid resin is a composite, but it shows the episode's mechanism (resin traps whatever
   is at the foot of the trunk, s093/s094) and it keeps CD note 5: Doug is in liquid resin, never sealed in amber.
   It's acceptable packaging, not a false promise.
3. **C (grid control).** It's the honest list read, and the bead size ladder pays off "Things". It's the weakest at
   168 px (the labels are small, and the snake skeleton reads a bit like a centipede until you read the label). It's
   fine as the control.
4. **"Baby Snake" label: OK.** It's accurate: Xing et al. 2018, *Science Advances*, "embryonic-to-neonate snake"; Caldwell:
   "the first baby snake" (facts.md rows 75 to 79; script item 6 says "baby snake"). It avoids every title word. In this
   context (a headless skeleton next to TICK, HELL ANT and DINOSAUR TAIL) it doesn't read as kids content.
5. **Kids-appeal check: pass.** No cute eyes, no mascot or nursery tone. Doug is in shock or panic in all three. C's
   bright tiles and the ComicNeue font are the channel's standard grid grammar and match past episodes.
6. **Dinosaur-menace check: pass.** A's dinosaur is hunched, hard-eyed and has open jaws, which meets the "not cute"
   note, and it never touches Doug. B's ant has open jaws and doesn't touch him either. There's no blood or injury
   anywhere and no real-looking gore. Nothing promises "dinosaur DNA", "alive" or Jurassic Park.
7. **For the A/B test:** if the titler's alt "...From Ticks to Dinosaurs" is ever tested, run it with A or B, not C,
   because C's TICK and DINOSAUR TAIL labels would repeat title words.

## 2026-10-28, director: visual review round 1 fixes
1. **Variety:** 63 shots restaged, and no more than 2 centred-bead frames now run back to back (checked by script). The new framings are:
   - extreme close-ups: the bead at scale 2.2 centred at (900, 600), so its top-right edge stays clear of the counter zone;
   - a mirrored card (bead left, Doug right);
   - Doug holding the magnifier to the bead;
   - Doug beside a giant bead resting on the shelf;
   - live bug's-eye forest-floor cutaways (hell ant, vampire ant with its beetle prey, with no fluid shown);
   - split cards.
   Kachin/SVP: s202 is the map with a red Kachin outline, s203 an amber-mine entrance, s204 a journal page crossed out, and s205 the map again.
   The card stays sober: no Doug, no counter, no wordart.
2. **Fixes:**
   - s004: no trunk over the silhouette, and the arrow ends on the tail.
   - s012: no bead. The penny edge is at 2.4 with the tick at true relative scale on the rim (about 2/3), plus a zoomed inset.
   - s065: the ant is at 0.7 with its left end lined up with the rice.
   - s046/s047: the adult male is at 0.8 and fully inside the bead.
   - s172-s174: Doug is at x 640, clear of the trunks.
   - Tray shots: the stray dashed drop line is removed.
   - s048: a silk egg sac with 11 clustered eggs, drawn from shapes.
   - s134: the library `thumbs_up_hand` with the skull on the thumbnail.
3. The art director's round-1 edits from commit b24dc27 (s009, s052, s097, s099, s110, s136, s137, s171, s178, s180) are carried over unchanged.
   The narration is untouched (1,973 words), and the shot ids are unchanged, so shorts.json still validates.
- 2026-10-28: script 3 rounds (screener FAIL x2 then CD approval after 2 one-line fixes), art 2 rounds (art-director PASS, visual-screener FAIL->PASS), thumbnails approved first pass. Risks: kid-appeal (dinosaurs), pronunciations (IPA added, not ear-tested), s128 snake silhouette reads as rope, raw amber lump s165-167, 15s longest shot unchecked.

## 2026-10-28, creative director: final package gate
Reviewed the title, `build/thumbnail.png` (and the 168 px version), the metadata.json description and tags, `build/chapters.txt`, the
script opening, and the first 40 s of `build/final.mp4` (frames at 1, 5, 9, 20 and 40 s) plus samples f_001/f_002. Visual screener
post-render: main PASS, shorts PASS. QC re-run exit 0, no problems; `gate` exit 0.
1. **Title: kept as "The Creepiest Things Scientists Have Found Trapped in Amber"** (59 chars, T4). The alt "...From Ticks to Dinosaurs"
   is the only real challenger. It is not clearly stronger, though: it is 63 chars, so it truncates sooner in the feed, and "Things"
   promises a list that the eight-item video delivers. Keep it as the first A/B title challenger with thumbnail A or B, per the thumbnail gate note 7.
2. **Thumbnail A: approved.** It reads in under a second at 168 px: the looming toothy dinosaur, panicking Doug, and the tick-on-feather
   bead. "99 MILLION YEARS" uses no title word. It is not cute and there is no contact or gore. The video pays it off: 0:00 is this
   exact frame, and the looming adult returns in the boss ("Young ones come with adults").
3. **Opening: passes the 3.2 rules.** The concrete first sentence (tick, dinosaur feather, 99 million years) is on the thumbnail frame.
   The payoff promise ("the owner of the first dinosaur tail ever found in amber") lands by about 0:09 over the FIRST DINOSAUR TAIL silhouette.
   "The Tick." comes at 0:11, and item 1's twist (Dracula's swollen tick, then the DNA/Jurassic question) follows inside 45 s. The counter shows 240 from the start.
4. **Description: approved.** The first line pays off the title with four real specimens, there are 6 sources with links, and it carries the
   disclaimer and AI-use note. The {{CHAPTERS}} placeholder is filled from chapters.txt at upload (studio/youtube.py:174). The chapters start at 0:00, there are
   8 items plus the intro, and every chapter is at least 10 s long. There is no "DNA", "alive" or Jurassic Park claim in the title, the thumbnail or the description.
5. **Lore:** series_bible.md has been updated. The counter is now 246 (+6), and the 030 log row adds the SPECIMEN TRAY device and the cap sealed in amber.
6. **Watch next (non-blocking):** check day-2 CTR for A against B/C. If A's CTR is below the channel median, swap to B before swapping the title.

FINAL: APPROVED
