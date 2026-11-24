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
