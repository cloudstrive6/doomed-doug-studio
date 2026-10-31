# 033-hyenas-deadlier-than-lions: visual review

## Round 1: pre-render keyframes + thumbnails (2026-10-31)

Scope: `build/contact/sheet_01..17.png` (s001-s202 + endslate), full-res crops of s030, s111, s172, s186, s198 from
`build/keyframes/`, `build/thumbnail.png`, `thumbnail_b.png`, `thumbnail_c.png` and the three `_small` (168x94) versions.

VERDICT: FAIL

Most of it is clean. Doug is on-model in every shot (red cap, white head) and readable against every background.
The HUD (night clock, DOUG DEATHS 260 to 267, LION | HYENA board) stays consistent with the script's tally (the s186
chalkboard has 2 and 8 ticks, which matches the HUD). There is no gore, and every death is the ghost + cap + field
guide gag. The tone is adult-coded. Labels are spelled right and none are cropped. Six fixes are required before the
render: two packaging/accuracy problems, one picture that contradicts its line, one blood-read and one variety run.

### Required fixes

1. **Thumbnail A / s001 (`scene_ref: thumbnail`) → graphic designer.** The lion walking out of frame is `lion_male`
   (dark mane). The video's own claim (s179, "EXCEPT HIM") is that lions always keep the kill when an adult male is
   there, and the climax (s190-s195) shows *lionesses* leaving. The opening image and main thumbnail therefore show
   the one case the script says never happens. Swap to `lioness_walking`, same position, facing and scale. That also
   matches script line 30 (s003 already uses a lioness).
2. **Thumbnail B (`thumbnail_test_b.json`) → graphic designer.** Same problem, and it's worse here: "WRONG CHOICE"
   over Doug hiding behind a **male** lion is factually the *right* choice by the video's own fact, so the package
   misleads. Replace `lion_male` with `lioness` (or `lioness_crouched` on an outline carcass, as in s190). The hyenas
   stay the threat. At 168x94 the lion is also the focal point and the two edge hyenas are half-cropped. Scale the
   lioness down about 15% so the open-jawed hyenas read as the threat.
3. **s172 → director.** The narration says "The sign was right, and no lions came," but a clear black **lion**
   silhouette (tufted tail, cat body) is walking at right (about x=1650, y=840). Remove it, or swap it for a hyena
   silhouette with eyeshine if you want foreshadowing.
4. **s030, s031, s032 (hyena skull) → illustrator.** The cheek teeth are filled solid red inside a dark gum band. On a
   bone-coloured skull at a 1-second glance this reads as bloody teeth (gore read). Change the highlight to a
   yellow or white tooth fill with a thick red *outline*, or keep the teeth bone-coloured and let the s032 red arrow
   do the pointing.
5. **s190-s194 → director (variety).** This is 5 consecutive near-identical compositions: the same three-lioness
   pile, centre, with Doug crouched at right in the same framing. Only the overlays change (HIDING, ?, whoop rings,
   eyes, hyenas). Break the run. Suggestions: s191 tight push-in on Doug's hopeful face with the lioness ear in
   frame; s192 wide high shot with whoop rings from off-screen and the pile small; s193 low wide with the black hyena
   silhouettes big in the foreground.
6. **s167 → director.** "Lions are what people picture," but the thought bubble's tail goes to the dark animal
   silhouette at right, not to Doug or the house, so the *animal* is picturing a lion. Re-anchor the tail to Doug
   (he already has the "?") or to the house window.

### Advisory (fix if cheap, not blocking)

- **s019, s020, s062, s110, s186 → illustrator:** the "HYENA" paw icon on the chalkboard header touches or clips the
  right frame. Nudge it left about 20 px. **s110 and s062 → director:** the narrator's glove/sleeve covers the whole
  HYENA tally column, so the score can't be read on the tick shots. Bring the arm in from the top, or shorten it.
- **s037 → director:** "Then the bone gets digested," but the picture is Doug in the jeep with a "?". Nothing on
  screen says digestion. A hyena with a bone showing in a belly outline (x-ray gag) would match the line.
- **s043 → director:** "The lion eats the meal," but the lioness sits *beside* the plate. Put her head down at the
  pork chop.
- **s183-s185 → director:** the Tanzania map has no label, and s184 names Tanzania. Add a "TANZANIA" label. Also
  label the s185 red dot "SERENGETI".
- **s174, s175, s178, s190-s195 → illustrator:** the stacked lioness (standing on top of a lying one) reads as a
  heap or mounting more than "three lionesses on a kill". Spreading them around a visible outline carcass would read
  better. This can be done together with fix 5.
- **s009:** the TAKEAWAY arrow tail runs through the "KE". Start the arrow above the word.

### Thumbnails at feed size (168x94)

- **A (NOT SCAVENGERS):** the strongest. It has one clear focal point (the huge open-jawed hyena in the torch beam),
  Doug and the threat are obvious, the text is legible, and it fits the title "Why Hyenas Are Deadlier to Doug Than
  Lions". Pass once fix 1 is done.
- **B (WRONG CHOICE):** text legible, Doug readable, but the focal point drifts to the lion. Fail until fix 2 is
  done.
- **C (grid):** labels LIE/BITE/CHASE/CLAN/TOWN/MOB are just legible, and Doug appears only in CHASE and is tiny. It
  is acceptable as a test variant but the weakest at feed size. No blood or cubs, and no title words repeated. No
  change required.

### Routing summary

- Graphic designer: 1, 2
- Director: 3, 5, 6 (plus the advisories for s037, s043, s062, s110, s183-s185)
- Illustrator: 4 (plus the chalkboard icon and lioness-pile advisories)
- Art director: none

Re-run `python -m studio keyframes 033-hyenas-deadlier-than-lions --shots s001,s030,s031,s032,s167,s172,s190,s191,s192,s193,s194`
and `python -m studio thumbnail 033-hyenas-deadlier-than-lions` after the fixes, then send them back for round 2.

## Round 2: re-check of fixes 1-6 (2026-10-31)

Scope: regenerated `build/contact/sheet_01..17.png` and full-res `build/keyframes/` for s001, s030-s032, s167, s172,
s189-s196, plus `build/thumbnail.png`, `thumbnail_b.png`, `thumbnail_c.png` and their 168x94 `_small` versions.

VERDICT: PASS

### Required fixes, status

1. **Thumbnail A / s001: FIXED.** `lion_male` is gone. A lioness now walks out of frame to the left, away from Doug,
   which matches s179 and the climax. At 168x94 the focal point is still the open-jawed hyena in the torch beam,
   Doug and his red cap read, and NOT SCAVENGERS is legible.
2. **Thumbnail B: FIXED.** A lioness replaces the male lion, so "WRONG CHOICE" now agrees with the video's own fact.
   She is smaller, and at feed size the two red open-jawed hyenas framing the shot read as the threat.
3. **s172: FIXED.** The lion silhouette is gone. The frame is just the LIONS: NO sign and Doug's cap, which matches
   "no lions came".
4. **s030-s032 skull: FIXED.** The cheek teeth now have a pale yellow fill with a red outline, so there's no blood
   read. In s032 the red arrow still points straight at them.
5. **s190-s194 variety: FIXED.** The run is broken: s190 is the wide pile plus HIDING, s191 a big push-in on Doug's
   hopeful thumbs-up with the lioness in the foreground, s192 a high wide shot with the whoop rings closing on a small
   pile, s193 a low wide shot with two big black hyena silhouettes in the foreground, and s194 the pile flanked by
   the clan. s190 and s194 still share the pile framing, but they aren't consecutive.
6. **s167: FIXED.** The thought-bubble tail now ends just above Doug's head (he has the "?"), so Doug is the one
   picturing the lion.

### Advisory (not blocking)

- **s193 → illustrator/director:** the foreground silhouettes are solid black. The round ears and sloped back make
  them hyenas, but adding a pair of yellow eyeshine dots to each would make them read in under a second and tie
  them to the eyes on the horizon.
- **Thumbnail B → graphic designer:** both edge hyenas are still cut off at the frame edge. That's acceptable, but
  pulling each one about 40 px inward would show more of the snout and teeth at feed size.
- **s167 → director:** there's a small notch where the tail meets the bubble (about x=565-605, y=485-495). It's
  cosmetic.
- The round-1 advisories that weren't picked up (chalkboard paw icon at the right edge in s019/s020/s062/s110/s186,
  the glove covering the tally in s062/s110, s037, s043, the Tanzania/Serengeti labels in s183-s185, and the s009
  arrow) still apply if they're cheap. None of them block.

Cleared for render. Post-render screening (samples, qc.json, Shorts) is still required.

## Round 3: post-render (final.mp4, thumbnails, Shorts) (2026-10-31)

Inputs: `build/samples/f_001..f_023` (every 30 s of the 678.2 s final), `build/qc.json` (problems: none),
`build/thumbnail*.png` + `_small`, `metadata.json`, `build/shorts/short01-03.mp4` + `_preview.png`
(8 frames pulled per Short, 4 from the last ~9 s).

### Main video
- No black, blank or glitched frames. f_008 (9 PM, black field with only Doug's cap on the ground) is the chase
  death beat, and the HUD is still drawn, so it's not a dropout. f_022/f_023 are the end card (DOUG'S NEXT DEATH
  plus the subscribe slot) and render cleanly.
- The HUD (chapter tag, clock 7 PM to 5 AM, DOUG DEATHS 260 to 266, LION|HYENA tally to 2|8) progresses in
  order across all the samples. Nothing freezes; every sample is a different composition.
- The round-2 fixes held in the final: no gore read anywhere. f_013's brown ellipse reads as a dirt patch, not blood.
  The lionesses leave in f_021 (s195) while the hyena clan closes in, which matches the title and the thumbnail.
- Text is legible and nothing is cropped. In f_014 the red X over "BACK" in COME BACK LATER is intentional.
- f_002's empty panels 2 and 3 are a mid-build reveal (the panels fill in), not a missing asset.

### Thumbnails
- **A (thumbnail.png)**: one focal point (the open-jawed hyena in the torch beam), Doug with his red cap and
  screaming face is obvious, and the lioness walks away left. NOT SCAVENGERS reads at 168x94. Honest to the title.
- **B (thumbnail_b.png, CD pick)**: WRONG CHOICE is crisp at feed size, Doug's grimace and cap read, and the two
  red-mouthed hyenas plus eyeshine make the threat clear. Honest: the lioness doesn't protect him.
- **C (grid)**: the six labels are legible at feed size and every panel is recognisable. It's the busiest at
  168x94 but acceptable as the test variant.
- All three complement "Why Hyenas Are Deadlier to Doug Than Lions" and none of them repeat a title word.

### Shorts
- All three: 1080x1920, the title is readable in the top band, the 16:9 picture isn't cut off at the sides,
  subtitles are large and legible, @DoomedDoug is present, and the end-card arrow points down to the link.
- **short01** (bones/hair, 32.2 s): pays off the title (skull, 4,500 N gauge, teeth tray). The outro ("It wanted
  his walking stick instead") opens one specific question that the clip doesn't answer: what it did with the stick
  (s046-s047). The end-card silhouette is a red-outlined hyena with round ears and a sloped back, which is
  recognisable. PASS.
- **short02** (laugh/status, 50.5 s): pays off the title (pitch graph, OFF A KILL, WHOOP rings). The outro
  "Doug counted to twelve" leads to the question WHAT HAPPENED AFTER DOUG COUNTED TWELVE? (s115-s116), which stays
  unanswered. The hyena silhouette is recognisable. PASS.
- **short03** (Harar, 44.8 s): pays off the title (wall, holes, scraps, hyena men). The lioness silhouette is
  recognisable. **However, the outro answers its own cliffhanger.** "Then the whooping started, and the lions
  left" tells the viewer the cause (the hyena clan arrived) right before the card asks WHY DID THE LIONS LEAVE
  DOUG?. FAIL.

### Required fixes
1. **short03 outro → director (`shorts.json`, short03 `outro`)**: remove the cause. Suggested wording: "Two hours
   later, Doug hid behind a pride of lionesses for safety. Then the lions got up and walked away from him. Full
   video below." Keep `tease_from: s195`, `tease_asset: lioness_walking` and the end card text. Re-render
   short03 only (`python -m studio shorts render`), then re-check its last 8 s.

### Advisory (not blocking)
- short01: the "???" sits over the hyena's body and head. Moving it about 60 px up (above the back) would show
  more of the silhouette.
- short01/short02 use nearly identical hyena silhouettes on their end cards. That's fine on its own, but a
  different pose (e.g. a whooping, head-up hyena for short02) would help when they appear on the Shorts shelf side
  by side.

VERDICT (main): PASS
VERDICT (shorts): FAIL
