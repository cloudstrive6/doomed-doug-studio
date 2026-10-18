# 022-komodo-can-wait: decisions

## 2026-10-18: script gate, draft 3: APPROVED
- Screener: PASS (script_review.md round 3). Facts 0 errors; hook 8, structure 8, voice 8; TTS and policy clean; 3,032 words, about
  15:33. Readability is at the limit (average 14.37, longest 35, Flesch about 72.0), so nobody downstream lengthens or simplifies sentences.
- My read: I would click and keep watching. The opener states the title promise in its first sentence, "The Ambush." lands at about
  word 29, and "It rarely needs the sprint at all" lands at about 0:35, with the full twist line before the first death (about 1:10).
  Every item is a reason the dragon doesn't need to chase, so the title is delivered. "Rarely" and "does not need to" are used throughout,
  and nothing says it can't run. THE WAIT clock rises steadily and works as the episode's thread. The jokes are adult-coded ("tired of
  insects", "The thermos was not technically food", "Doug was not required"). Predation stays off-screen, there is no bacteria myth, the
  human-attack line is a sober card with no joke, juveniles are "young dragon" and drawn hard-eyed, and the Virgin Birth stays clinical.
- Deviations from the brief, all accepted (driven by facts, listed in the script header):
  1. The Swim twist now says the next island already has its own dragons (Jessop 2018: dragons rarely leave their valley).
  2. The Buffalo is moved before The Meal and its twist is now "outlast, not win" (buffalo usually escape; Bull 2010 shared feeding).
  3. The Fast uses one large prey a month (SDZWA) instead of "a dozen meals a year as a need".
  4. The Tongue uses 4 km (Smithsonian) instead of 9.5 km. The Nursery uses "months", not "years", and drops the cannibalism percentage.
  5. Six spoken headers ("Months." added). Hocknull is framed as fossils of the Komodo dragon itself.
- Applied at the gate: facts.md Follow entry (advisory A3) now quotes the script's Titanic line ("with time left over for a snack").
- Noted, no change: The Buffalo gives about 90 kg for the biggest dragons in field studies, and The Nursery gives more than 100 kg for the
  biggest males. The two figures are consistent (field-study animals against the record males). The director must not put both numbers
  on screen as if they were one figure.
- Carried forward:
  - Director: per A4, don't trim Ambush, Buffalo or Meal narration in shot splits. THE WAIT stays monotonic (0 S, 1 S, 50 MIN, 4 HR,
    1 DAY, SEVERAL DAYS, SEVERAL DAYS, 5 DAYS, 1 MONTH, MONTHS, 2+ YEARS, ABOUT 4,000,000 YR). The art director may cut it if the frame
    is busy, but the counter always stays. The Crowd and Buffalo shots show no carcass (heads around an off-frame shape only).
  - Art director: dragons heavy and menacing; the young dragon lean and hard-eyed, never big-eyed; the bandage white, never red; no
    fantasy dragon imagery.
  - Titler: the lead is "Why the Komodo Dragon Can Kill Doug Without Chasing Him" (T10). It must not read as a noun swap of 021: no
    "Everything", "Except" or "Refuses". "Deadliest Lizard" is not sourced, so don't use it. Include "Entertainment and education only.
    Do not approach wild animals." Metadata must never target kids.
  - Editor: check Chirp on Rinca, Flores, Sungai, Megalania, Stegodon, Hocknull, LeBlanc, parthenogenesis.
- Series bible updated: counter 186, THE WAIT (episode-only), Doug's bandage gear, used-once lines, episode log row 022.

## 2026-10-18: thumbnail pick: A (hero, `thumbnail.json`) WINS; B (grid) kept as `thumbnail_b.json` for a later swap
- Viewed `build/thumbnail.png`, `build/thumbnail_small.png`, `build/thumbnail_b.png` and `build/thumbnail_b_small.png`. Re-rendered A
  with `python -m studio thumbnail 022-komodo-can-wait`. `thumbnail.json` is unchanged and there is no `thumbnail_a.json`.
- Why A:
  1. Pairing (style bible, title/thumbnail complementarity): the title is a T2 "How [X] Kills" revelation and not an "Every / Most
     Disturbing" list. That pairs with a hero. A grid would promise a list the title doesn't frame.
  2. A tells the title's story in one glance: a huge, still dragon with one eye on Doug, the tongue out, and Doug walking off whistling
     with the bandage. "IT CAN WAIT" is the stakes-phrase variant of archetype C (white bold sans with an underline on a flat earth-tone
     field). It still reads at 320x180: three words, one creature, one tiny red cap.
  3. B is weaker. TEETH, TONGUE and CROWD are three crops of the same head, so the grid looks samey. The BUFFALO tile's animal has long,
     thin, swept-back horns and reads as an ibex or goat, not a water buffalo. "4M" inside the stopwatch only repeats the label. With no
     stakes and no Doug, nothing in it says "without chasing".
- Note on A, no change needed: the half-lidded eye reads as patient and cold rather than sleepy, and that fits "it can wait". The
  bandage is white with no red. No gore, nothing cute.
- Consistency check: the title "How the Komodo Dragon Kills Doug Without Chasing Him" shares no word with "IT CAN WAIT", and the
  thumbnail_brief in metadata.json matches both JSONs (A's text, and B's labels and order). The promise is delivered (script gate). If a
  title A/B test runs, don't use the alt "...Weapon Scientists Found Is Patience" against this thumbnail, because "Patience" and "WAIT"
  say the same thing twice. The other three alts are fine.
- Fallback: if day-7 CTR is under the channel median, swap to B (as with 015 and 012), but first have the illustrator fix the
  buffalo tile (wide, sweeping horns, heavy body) and give TONGUE or CROWD a distinct drawing.
- Next: the visual screener checks the thumbnail. Shot s001 (the opening image) uses the A hero for 1.5 to 4 s.
- 2026-10-18: script 3 rounds (fact/rule fixes), art 2 rounds + thumbnail check round 3 (s184 tail), thumbnail A hero, packaged 15:44. Risks: Flesch/sentence-length at limits; weak 'rare attacks' source (AP 2009); hero thumbnail claws unclear at feed size (fallback B grid after buffalo redraw).

## 2026-10-18: final package gate: APPROVED
- Screener: visual_review.md post-render VERDICT (main) PASS. All 31 samples are clean and qc.json shows no problems. The Shorts FAIL is
  being re-rendered separately and doesn't block the main upload.
- Title: I'm keeping the lead "How the Komodo Dragon Kills Doug Without Chasing Him" (52 chars, T2 plus a revelation clause). It reads
  more cleanly than my gate lead, avoids opening with "Why" right after 021, and shares no word with "IT CAN WAIT". None of the alts is
  clearly stronger. "Why Komodo Dragons Don't Need to Chase Doug to Kill Him" is the best A/B challenger, but it's longer and opens with
  "Why". It stays the A/B option, and the "Patience" alt is still excluded because it doubles the thumbnail. No swap. The promise is
  delivered: none of the eight deaths is a chase, and item 1 says it can sprint.
- Thumbnail (build/thumbnail.png): one huge, still, hard-eyed dragon, its tongue at tiny whistling Doug's white-bandaged ankle, and a
  three-word stakes line. It reads in one glance and asks "when does it strike?" I would click. No gore and nothing cute.
- First 60 s (captions plus f_001 to f_003): the thesis comes in the first sentence, "Seconds. The Ambush." by about 0:10 (about word 29),
  and "It rarely needs the sprint at all" by about 0:35. Map, then trail, then a warning sign with the dragon lying low beside Doug. The
  HUD (DEATHS 178, THE WAIT) is legible. The Copenhagen-cyclist scale beat and "Doug did not agree to this." land before the first death
  (about 1:15). I would keep watching.
- Description and chapters: the 12 chapters match build/chapters.txt and the 15:44 runtime, starting at 0:00. There are 6 primary or
  institutional sources, the disclaimer includes "Do not approach wild animals.", there is an AI-use disclosure, and nothing is
  medical or safety advice. made_for_kids is false (config). The tags are on-topic. Playlist: animals.
- Series bible: row 022 updated to the final title and status, with the formula note corrected to T2. The counter stays at 186.
- Watch: day-7 CTR. If it's below the channel median, swap to thumbnail B after the buffalo tile is redrawn (see the thumbnail pick above).

- Showrunner: QC exit 1 at workflow time, re-run exits 0 with no problems. Main PASS; Shorts FAIL (fixes applied, .rerender shorts).
FINAL: APPROVED

- Showrunner round 2: QC OK (no problems). VERDICT (main): PASS; VERDICT (shorts): FAIL (short03 end-card silhouette unreadable; short01/02 fixed). Shorts held back; suggested fix: short03 tease_asset wait_stopwatch. Main video stays qc_passed.
FINAL: APPROVED
