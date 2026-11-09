# 041 Decisions

## 2026-11-09 Creative Director: script gate (draft 2)
Read: script_review.md (draft 2, PASS: facts 0 errors, hook 8/10, structure 8/10, voice 8/10, TTS and policy PASS), script.md, facts.md, brief.md.

**Decision: APPROVED.** The title promise ("won't try to kill") is delivered honestly item by item, with the bear's wins said plainly
(wolf kills, the black-bear wolverine kill, moose cows and calves, tiger kills). The opening works: a first sentence with a number, the payoff
promise by about 0:10, "The Wolf Pack." at word 35, and the twist by about 0:42. The BEAR'S COST tag only ever goes up, and the tiger to human
inversion is a strong boss. Deaths are cartoon cut-to-blacks, infanticide gets one clinical clause, and the jokes are adult-coded.
I'd click it and keep watching.

Light edits I applied myself (screener R1-R6, no change to any claim):
1. R1: Bull Moose trimmed from 271 to 257 words ("Every year in late September and early October, it spends the rut shoving..." became "In the fall rut, it shoves...",
   and I cut "when the calves are brand new").
2. R2: bison speed is now "about fifty kilometers an hour". It holds under both NPS figures (35 mph and 30 mph).
3. R3: the moose Doug beat now says "...a moose-calf costume, so it can see how the calves feel." (21 words, same length as before).
4. R4: "car park" became "parking lot" (narration and both stage directions; en-US voice).
5. R5: pie label is now "OLDER KILLS: 88% COWS". I didn't add the narration baseline, to keep the segment under 260.
6. R6: facts.md now has the Dahle 60% female population baseline and the yearling note, plus the NPS 30 mph note in the bison row.

Spoken words are now about 2,094 (about 10.7 min), inside 1,950-2,350.

Notes for the director and editor:
- Hold the thumbnail 1.5 s or less, and don't add a word before "The Wolf Pack.". It is at the 35-word limit.
- Death 320 stays flat, and so does 322.
- The series bible counter (315 to 322) and the 041 log row get updated at the final gate, as with 040.

## 2026-11-09 Director: shotlist
- **194 shots**, and the narration matches the approved script word for word (2,094 words). Doug is in 88% of shots, no shot runs over
  45 words, and on a 195 wpm estimate no stretch goes longer than about 4.6 s without a pop-in.
- **Opening:** s001 is `scene_ref: thumbnail` and carries only "One three-hundred-kilo grizzly" (about 1.3 s, `pause_after` 0.05), so the
  hold stays at 1.5 s or less. Nothing is added before "The Wolf Pack." (s005). `thumbnail.json` belongs to the graphic designer, so that
  validate error is expected until it exists.
- **HUD:** "DOUG DEATHS: N" at (1590,162) plus a BEAR'S COST tag (library `price_tag` icon + size-28 label at y 238) on every shot after
  s001. It moves DINNER, FACE, BONES, CUBS, LIFE on the spoken band shots (s004, s052, s077, s123, s147). Each band shot is a big torn tag
  card with the old word struck out. LIFE uses a pink label with red text. The tag is never read aloud.
- **Backdrops by band** (luminance falls toward the boss): Wolf Pack = Yellowstone January snow (034 JAN). Wolverine = late snow
  `#dbe6ee` with snowy firs. Porcupine = pale forest floor. Bull Moose = overcast willow flats (green, so wordart uses the white/yellow
  override). Bull Bison = March thaw (034 MAR). Big Male = sedge meadow (green override). Tiger = Sikhote-Alin snow at dusk `#4a4f5e`.
  Human = Montana trail at dusk plus a dusk parking lot. Diagram cards are cream `#f4f1dc`, sober cards `#15181a`, and death beats
  `#0b0f14` (snow-night ground `#232a36` / `#2a3240` for the snow items).
- **Deaths:** 316 cap in wolf tracks + ghost + field guide NO; 317 cap on one quill + ghost; 318 bull silhouette (pale rim) walking off
  with the cap on an antler; 319 cap on the bison's back, the folded deck chair left behind; 320 a **silent** shot (`narration: ""`,
  1.8 s, like 031) with the cap at the meadow edge and MAYBE rubbed out, played flat; 321 cap in a tiger print + ghost; 322 flat
  (cap at the treeline, no ghost). Survival at The Wolverine: thumbs-up, the counter stays at 316, and MAYBE is pencilled in.
  No `on_back` bodies and no gore. Cubs are never shown hurt: the infanticide beats use a pie chart, silhouettes and a dotted line.
- **Reveals:** wolverine (silhouette s027, colour s029), porcupine (s050/s051), moose (s075-s076/s078), bison humps (s101/s102),
  big male (s122, s124/s127), tiger (s003, s146/s148).
- **Shorts:** short01 Amur Tiger s155-s164 (hook from s149, ends on the fair-fight death); short02 Porcupine s064-s074 (hook from s054,
  ends on the quills-inward death); short03 Bull Moose s079-s087 (opens on the somersaulting bear, ends on the vending-machine kicker).
  The titler adds the titles.
- 33 missing drawings are listed in `asset_requests.md`. I rendered the 101 shots that need no new art (keyframes) and fixed what I found:
  the counter-zone title collisions (titles now at y 380), the big male's ridge moved left, tag-card layout, and sign text size.
- 2026-11-09 (showrunner): script 2 rounds (FAIL then PASS), art 3 rounds (visual-screener PASS r2, art-director fixes verified), thumbnails A/B/C ok. Risks: pacing pass (long-shot/pop-in check, draft render of first 60s) not completed by editor; opening already at word limit before 'The Wolf Pack.'; price_tag asset edited (ep 030 s198 checked ok); shotlist.json is authoritative, build/gen.py stale.

## 2026-11-09 Creative director: final package approval
Reviewed: title, thumbnail A (build/thumbnail.png), metadata.json description and tags, build/chapters.txt, opening of script.md,
sample frames f_001/f_002, visual_review.md (post-render PASS main + shorts), qc.json (no problems, 657.8 s).
- **Title kept:** "Why a 300 kg Grizzly Still Won't Try to Kill These Animals" (58 chars, T9). The number gives scale and the
  "still" sets up the curiosity gap; no alt title is clearly stronger. The video delivers it: every item is something a grizzly avoids
  fighting, and the script is honest where bears do kill (adult moose, mostly cows; the chapter is the bull). Formula differs from
  039 (Every Reason) and 040 (The Most).
- **Thumbnail A:** bear, Doug and tiger read at feed size; "NOT WORTH IT" complements the title without repeating it. No gore, no
  cubs, adult-coded. (The script's stage direction still says "EVEN BEARS RUN"; stale text only, the render uses the approved A.)
- **Description:** promise matches the content, six key sources linked, AI-use and disclaimer present, {{CHAPTERS}} is filled at
  upload (studio/youtube.py). Chapters start 0:00, item 1 at 0:10, eight item chapters.
- **First 60 s:** number in the first sentence, payoff promise (Doug between a bear and a tiger that eats bears) by about 0:08,
  "The Wolf Pack." at about 0:10, twist ("Here's the strange part.") inside 45 s. Frames are clean, HUD legible.
- Non-blocking notes carried from the visual screener (s175 label overlap, s079 moose reads horse-like, s161 arrow) are logged for
  asset revisits, not this upload.
- Series bible updated: counter 315 to 322, deaths 320 and 322 flat, 041 log row added.

FINAL: APPROVED
