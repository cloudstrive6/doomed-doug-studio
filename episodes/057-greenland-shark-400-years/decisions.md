# 057 decisions

## 2026-11-24 · Script gate (draft 3): APPROVED
Creative director. Read brief.md, script.md (draft 3), facts.md and script_review.md (draft 2 screen).

- The draft 2 screen failed on one required fix only (F5, l.176) and stated "Once F5 is fixed, the script passes"; all score
  gates already passed (hook 9, structure 8, voice 8, TTS/policy/length PASS).
- F5 is fixed: l.176 now reads "It's a sandwich you have to leave alone for about three months before anyone will eat it, which is
  the exact opposite of how sandwiches work." No "safe", no fridge, the time is the whole 8 + 5 week process. facts.md row for
  The Meat updated to match (no safety claim). No other line changed; 2,105 spoken words, ~10.8 min at 195 wpm.
- Screener nit l.86 is applied ("A big Greenland shark can be five meters long", boss line stays fresh); nit l.88 ("since") left
  as is, not blocking. Header and footer comment relabelled draft 3.
- Would I click and keep watching: yes. Strong cold open (older than the United States, eye parasite twist by ~word 118), the
  birthday-cake payoff is specific and delivered, every age claim carries its range, no attack implication, cartoon deaths only.
- Counter 414 to 420 (deaths at 1, 3, 4, 5, 8, 9). Series bible lore is updated when the episode is packaged/uploaded, not here.
- Notes for the director/art director: the seal costume at item 4 needs the art director to confirm it reads differently from 051's;
  SHARK AGE card needs art-director approval; the copepod stays a pale streamer on a dot eye (no eye damage shown).
- Housekeeping: style bible Script Writer rule 1 and Editor rule 10 updated to the 10-12 min / 1,950-2,350 word targets
  (config `video.target_minutes`), as the screener flagged.

## 2026-11-24 · Shotlist (director)
- 208 shots (s001 = thumbnail), all 2,105 spoken words once and in order, max 22 words per shot; 9 chapters; Doug in 203/208 shots.
  Counter 414 to 420 ticks at s021, s063, s089, s112, s183, s204 (boss death and closing red-on-pink).
- SHARK AGE device: `shark_age_icon` + size-28 label at (1590,238) under the counter, values ? / 0 / ~10 / ~50 / ~100 / ~100 / ~150 /
  ~250 / ~392 (±120) (red from the reveal s187), `+ 1 MIN` on the LIVE feed. **Pending art-director approval.**
- Item 4 costume: new `harp_seal_costume_prone` (pale silver, black harp saddle, mask hood) so it reads differently from 051's grey
  `seal_costume`. **Pending art-director approval.**
- Item 7: no party hat (facts.md director note); the CONGRATULATIONS card only.
- Background ramp: sky one step dimmer per item (`#cfe9ff` to polar night `#1b2f5a` at the boss); water under the ice stays `#3a9ad9`
  (art bible); only The Deep uses the depth ramp (to `#0b2447` at 2,200 m). Closing = LIVE feed (cap on the upturned cake).
- Shorts: short01 The Oldest (s186-s198), short02 seals / Slowest Shark (s076-s089, hook line), short03 The Menu (s094-s108).
  Titles and descriptions left for the youtube-titler.
- Thumbnail (`thumbnail.json`) is still to come from the graphic designer; s001 references it.

## 2026-11-24 · Package gate (thumbnails A/B/C + title order): CHANGES REQUIRED
Creative director. Read metadata.json `packaging` (10 ranked candidates, variants A/B/C), the three PNGs at full size and at
feed size (246 px wide side by side), the brief (section 3 thumbnail, payoff line), visual_review.md and 050-056 titles.

**Not approvable yet for two reasons:** (1) no visual-screener report covers the thumbnails (visual_review.md round 2 says
"thumbnails A/B/C are still to come"), and (2) the fixes below. Resubmit after the designer's fixes and a screener PASS.

### Title order: reorder (tie at 100 broken by channel data and formula variety)
- **New A = "The Greenland Shark Has the Creepiest Eye Parasite Alive" + thumb `HI FRIEND?`** (was B). Parasites/body horror is
  our best CTR lane (002 at 6.5%, 014 at 5.1%; D4 gives it +0.5), item 1 delivers it with the twist inside 45 s, and it breaks the
  "Why ..." streak (054, 055 and 056 all open with "Why"; a 4th in a row is the repetitive packaging we said we would avoid).
- **New B = "Why the Greenland Shark Is the Creepiest Fish Alive" + thumb `392 ± 120 YRS`** (was A). Best pairing of the three
  (title gives the frame, thumb gives the shock number) and it stays in the test.
- **C unchanged = "The Greenland Shark Is the Creepiest Teenager in the Ocean" + thumb `CONGRATULATIONS?`**. Delivered by item 7
  (~150 years to mature); fine as a figurative joke.
- Youtube-titler: swap the A/B variants and make the new A the `title` in metadata.json; re-run `package <ep> check`.

### Would I click?
- `392 ± 120 YRS`: yes. The number reads at feed size and is honest (range shown). The shark face is the weak part.
- `HI FRIEND?`: yes, the strongest curiosity gap of the three, but the eye is ambiguous.
- `CONGRATULATIONS?`: no. Flat hot pink, a smiling Doug and a candle on a card read as a kids' birthday card with no dread.

### Required fixes (graphic designer)
1. **Thumb `HI FRIEND?` (new A), two eyes.** The dark oval near the snout reads as the shark's eye, so the copepod's ringed circle
   reads as a porthole or mouth. Make the snout oval a small flat nostril right at the tip (or drop it) and give the copepod's eye a
   dark pupil so it is unmistakably the eye. No eye damage, as before.
2. **Thumb `HI FRIEND?`, copepod pose.** Its legs stop mid-body as if it were standing on the shark (it reads as a mummy person).
   Scale it to about 70% and make it dangle from the eye: a slight curve with the two egg-sac streamers trailing back with the
   current. Keep the waving arm (that is the gag).
3. **Thumb `HI FRIEND?`, torch.** It is unlit. Add a soft pale-yellow beam cone from Doug's torch onto the copepod and darken the
   open water by one step, so it reads as dark under the ice and the eye pops.
4. **Thumb `392 ± 120 YRS` (new B), shark face.** At feed size it reads as a grey blob or whale (no mouth, and the fin under the
   hole looks like a hump). Add the wide flat grim mouth line across the lower face (brief: "mouth line"; scale the shark to about
   0.9 or raise it so the mouth sits near y 640), and drop the fin bump or tuck it behind the ice edge.
5. **Thumb `392 ± 120 YRS`, cake.** Doug and the cake are a white smudge at 246 px, and the cake is the episode's payoff. Scale
   Doug and the cake about 1.6x, stand him at the hole's edge leaning over it, and draw the candle flames as one bright
   yellow-orange cluster so "birthday cake" reads at feed size. The text block and the yellow sky stay as they are.
6. **Thumb `CONGRATULATIONS?` (C), setting and tone.** Move it under the ice: a white ice ceiling band at the top (text on or just
   under it), and water in the art-bible ocean blue to a darker blue at the bottom. No flat magenta.
7. **Thumb `CONGRATULATIONS?`, card.** Remove the candle on the card (it reads as a kids' card), and replace the unreadable fin
   doodle with a big black "~150" on the card face. That is the number that lands "teenager", and it is not in the title.
8. **Thumb `CONGRATULATIONS?`, shark.** Make it the hero: about 15% larger, a half-lidded unimpressed eye with the pale copepod
   streamer (continuity with the other two thumbs). Doug stays small, holding the card up, still pleased with himself.

### After the fixes
- Visual-screener: screen all three thumbnails at full size and at 246 px. Check text legibility, the copepod (no eye damage), and
  kid-appeal on C.
- Then back to me for the package gate. Series bible lore (counter 414 to 420, new gags) is updated at upload, as planned.

## 2026-11-24 · Package gate, round 2 (rebuilt thumbnails A/B/C, title order): CHANGES REQUIRED (one fix, C only)
Creative director. Viewed build/thumbnail.png, thumbnail_b.png, thumbnail_c.png at full size and the _small versions; checked
metadata.json (new A is the `title`; order A = eye parasite + HI FRIEND?, B = Why ... Creepiest Fish + 392 ± 120 YRS,
C = Teenager + CONGRATULATIONS? ~150, as requested).

- **A `HI FRIEND?`: approved.** Fixes 1-3 done: snout oval gone, the copepod's eye has a dark pupil and is unmistakably the eye,
  the copepod dangles with egg sacs trailing and keeps the wave, torch beam is lit and the water is a dark navy. Would click.
- **B `392 ± 120 YRS`: approved.** Fixes 4-5 done: wide grim mouth line, no fin hump, Doug and the cake ~1.6x with one bright
  flame cluster that reads as a birthday cake at feed size; copepod dangles from the left eye. Would click.
- **C `CONGRATULATIONS? ~150`: one fix.** Fixes 6-8 done (under the ice, no magenta, no candle, big "~150" on the card, shark is
  the hero with a half-lidded eye). Remaining problem: the copepod here is the old "mummy person" (the problem fix 2 solved on A):
  the eye reads as its head and its legs run down to the belly with a foot sticking out.
  1. **Graphic designer:** replace C's copepod with the same dangling copepod used on A, scaled to C's eye (about 0.4x of A's),
     hanging from the half-lidded eye with the two egg-sac streamers trailing back toward the tail. Keep the eye half-lidded and
     separate from the copepod. Change nothing else.

Gate condition: this becomes APPROVED once C's copepod is fixed and the concurrent visual-screener returns PASS on all three
(if the screener asks for other fixes, apply those too and send back). No need to send A or B back to me unless they change.
- 2026-11-24: script 3 rounds (facts/jokes/sandwich fixes); art 3 rounds (keyframes + s137); thumbnails 3 rounds (A/B swapped by CD, C copepod); runtime ~11.2 min. Risks: reindeer claim is 'reportedly' (secondary source); thumbnail text ~150 added to C; shotlist generator in build/ is git-ignored.
