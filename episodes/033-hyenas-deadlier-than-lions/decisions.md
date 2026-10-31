# 033 Why Hyenas Are Deadlier to Doug Than Lions: decisions

## 2026-10-31, creative director: script gate (draft 2)
Screener draft 2: PASS (0 fact items, policy clean, hook 8, structure 8, voice 8, 2,007 words).
1. **Approved.** Draft 2 delivers the brief. One night, dusk to dawn, 9 items, deaths 261-267, survives The Laugh and The Town, LION 2 / HYENA 9, both callbacks (024, 032), the required honesty line (Packer 2005 plus Mbise 2021), and no cubs, no Lion King, no named victims and no safety advice. The opening meets the retention rules: concrete sentence 1, the promise by about 0:09, "The Lie." at word 35, the twist by about 0:46, and death 261 at about 1:16.
2. **The deviations from the brief are accepted.** They are all fact-driven: Masai Mara 95% in place of the unsourced 93%, Ngorongoro "at least six times" in place of Cooper's secondhand "four", no "store food in water", no IUCN "most abundant", no Malawi hot-season line. These are the right cuts.
3. **CD edits (advisories A1, A3, A4), applied in script.md:**
   - A1: Mekelle now reads "researchers found donkey hair in more than twice as many of the hyenas' droppings" (it was a share of droppings, not an amount eaten).
   - A3: the Mob line is now "So, with dawn still an hour away, Doug hides behind..." The Sleepers kicker keeps "for the last hour of the night", so The Sleepers doesn't lose words (it's already at 188).
   - A4: "...recruit the rest of the clan, and it carries up to about five kilometers." The range still sits next to the soccer-field analogy.
   - The first three sentences are untouched: "The Lie." is still words 34-35. The new count is **2,011 words** (about 10.3 min).
4. **A2 not taken.** The Sleepers stays at 188 words. It is the sensitive item and the bible says never pad.
5. **Editor (A5):** thumbnail hold about 1.5 s, not 4 s, so death 261 lands by about 1:16. "UNESCO" is added to the pronunciation note; check it on the narration pass.
6. **Director notes (not blocking):**
   - a. The opening's "HYENA KILL" panel and The Lie's three-panel strip show carcasses as outlines only. No body is drawn being eaten anywhere (brief gore rule).
   - b. Every hyena keeps the heavy, sloped `spotted_hyena.json` build. Giggling means mouth open, not a smile.
   - c. Harar: the hyena man is drawn respectfully and simply, and never as the joke.
   - d. The 032 separation rules (brief section 0) apply to every frame: no den, no bones pile, no fossils, no time machine.
7. **Series bible updated:** the counter goes to 267, with a 033 log row.
APPROVED

## 2026-10-31, creative director: thumbnail gate (A, B, C)
Screener: visual_review.md round 2 PASS (lioness swap done in A and B). Checked at 1280x720 and 168x94 against the title "Why Hyenas Are Deadlier to Doug Than Lions".

**A (NOT SCAVENGERS): APPROVED, lead variant and opening image.** One focal point at feed size: the huge open-jawed hyena in the torch beam. Doug and the red cap read clearly, and the lioness leaves frame left, which is the title's promise in one picture. The text repeats no title word and sets up The Lie in the first 35 words. The hyena is not smiling and there is no gore.

**C (grid LIE/BITE/CHASE/CLAN/TOWN/MOB): APPROVED as the test variant.** It is the weakest at feed size, but the labels are legible, and "THIEF" on the lion is a real curiosity hook that pays off at line 58. Every tile maps to a script beat (the six-men jaw, the two buses, the lioness leaving in MOB). The school bus is the script's own scale analogy, and the dark MOB tile keeps it from reading as kids' content. No cub and no title words.

**B (WRONG CHOICE): CHANGES REQUIRED (graphic designer). Do not upload B to Test & Compare until these are done.**
1. **Make Doug's body readable.** His stick body is drawn in dark ink on the #3a4a6e ellipse, so at 168x94 he is a floating head and the "cower" pose (the whole story of B) doesn't read. Render his lines white as in A (`"ink": "#ffffff"` on the doug element) and check the small version.
2. **Bring the threat in.** Pull both edge hyenas about 60 px inward and scale them up about 10% (0.92 to about 1.0), so the open jaws sit nearer the lioness and Doug and the snouts are fully in frame. Right now the biggest, most central object is still the lioness, and on a "deadlier than lions" title the hyenas must win the glance.
3. **Make Doug's hiding readable.** Put Doug behind the lioness's shoulder or rump, crouched lower (overlapping her body by about 20-40 px), so it reads as "hiding behind the lion" rather than "standing next to a lion". Keep the gritted face and sweat drop.
4. **Use the empty space.** The band between the text and the action (y about 130-400) holds only scattered eyes. Move 3-4 eye pairs lower and closer to the pair of hyenas so the ring visibly closes around the spotlight. Keep the text, colour and size as they are.
Re-run `python -m studio thumbnail 033-hyenas-deadlier-than-lions` and return B with its _small for a CD re-check. A and C need no further changes.

Stage not changed (art_approved stays; package gate pending B).

## 2026-10-31, creative director: thumbnail B re-check (after the 4 changes)
Checked `build/thumbnail_b.png` (1280x720) and `build/thumbnail_b_small.png` (168x94, also viewed at 4x nearest-neighbour) against the four changes above and the visual-screener criteria.
1. **Doug readable: DONE.** White ink (`"ink": "#ffffff"`). At 168x94 the stick body and bent legs now read against the spotlight ellipse, so he is no longer a floating head.
2. **Threat brought in: DONE.** Hyenas are at x 50 / 1240, scale 1.0. Snouts, red mouths and teeth are fully in frame and aimed at the lioness and Doug, and at feed size the two hyenas win the glance over the lioness.
3. **Hiding readable: DONE.** Doug is in `crouch` (gritted, sweat), low at the lioness's rump and overlapping her by about 30 px, so the read is "ducking behind the lion". The lioness faces the left hyena while the right hyena's open jaw is about 150 px from Doug, which makes the "wrong choice" visible.
4. **Empty band used: DONE.** Four eye pairs moved down to y 320-380, next to the hyenas, so the ring closes on the spotlight. The text is unchanged.
Feed-size screen (168x94): WRONG CHOICE is legible, the red cap is clearly visible, and Doug, the lioness and both hyenas are all identifiable. There is no gore: the red is the open-mouth interior with white teeth, as in A, and there is no carcass and no blood. Nothing kid-coded, no cub, no title word repeated.
Advisory (not blocking, only if cheap on a later pass): Doug is drawn on top of her rump. Putting him one layer under the lioness so her haunch covers his shoulder would make "behind" literal.
**B: APPROVED** as a Test & Compare variant with A (lead) and C.
Stage not changed.
- 2026-10-31: packaged. Rounds: script 2 (screener FAIL then PASS), assets 1, keyframes 2 (art+visual PASS r2), thumbnails A/C approved, B revised once. Runtime ~11.3 min. Risks: day-7 gate on 024 (judged 11-02), 032 hyena overlap (thumbnails differ).

## 2026-10-31, showrunner: post-render
QC ok; visual screener main PASS, shorts FAIL (short03 outro gave away the answer). Outro reworded; shorts re-render requested.

## 2026-10-31, creative director: final package gate
Inputs: metadata.json, build/thumbnail.png (A, lead), build/chapters.txt, build/samples/f_001-f_004 (plus f_022/f_023 to confirm the ending), script.md opening, visual_review.md round 3 (main PASS; QC problems: none; 678 s, about 11.3 min).
1. **Title: approved as is.** "Why Hyenas Are Deadlier to Doug Than Lions" (42 chars). It is honest because of "to Doug": the board ends LION 2 / HYENA 9, Doug dies to hyenas 7 times and to lions 0 times, and the script (line 374) and the description both say plainly that lions kill more people. T9 was last used on 031, two uploads back, and 032 was T5, so it is not a back-to-back repeat. No alt swap: none of the alts is clearly stronger. Alt 4 ("The Most Disturbing Thing Scientists Learned...") overlaps 030/032 phrasing and stays a fallback only.
2. **Thumbnail A: approved** (already gated). NOT SCAVENGERS shares no word with the title, it pays off as The Lie in the first 35 words, the lioness leaving frame matches the promise, and there is no gore and no cub. B and C stay as the Test & Compare variants.
3. **Opening 60 s: approved.** Concrete sentence 1 (Kruuk via SDZWA), the payoff promise "Doug hides behind lions, and the lions leave" by about 0:09 (delivered in The Mob, f_022: lionesses walk off as the clan closes), "The Lie." at word 35, THIEF sign / FAMOUS flip (f_001), and death 261 by f_004 (1:30 sample, HUD 261 and HYENA 1). f_002's empty panels are a build-in, not missing art. The HUD runs 260 to 267 / HYENA 9 in the shotlist after the last 30 s sample; end card (f_023) is clean.
4. **Description: approved.** Every hook claim maps to the script: 80%+ (line 1), about 5 km chases (Kruuk), clans of about 130, hand feeding in Harar, the lions leaving. Six sources, disclaimer, AI-use note, no safety advice. Chapters start at 0:00, there are 10 entries, and "Intro" is 11 s. Tags and the `animals` playlist are fine.
5. **Not made for kids**: adult-coded tone throughout and no nursery signals. Shorts (short03 re-render) are outside this gate.
FINAL: APPROVED
