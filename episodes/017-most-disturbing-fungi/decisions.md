# Decisions: 017 The Most Disturbing Fungi Scientists Have Ever Found

## 2026-10-13: script gate (draft 3)
- Inputs: `brief.md`, `script.md` (draft 3), `facts.md`, `script_review.md` (round 2 FAIL on F2 only) and the draft 2 to draft 3 diff.
- **Screener status:** round 2 failed on one blocking fix (F2, the chytrid recovery denominator) and said a re-check of that one line was enough for a PASS. I checked it.
  - Line 147 now reads "only about one in eight of all the declining species shows any sign of recovery". That is the screener's first option word for word, and it keeps the denominator at 12% of all 501.
  - facts.md row 91 now says "12% of the 501 declined species", and the 1980s clause is gone.
  - The CDC wording advisory (row 117) is fixed with the fetched quote.
  - The count is 2,922 words, which is at least 2,900.
  - No other line changed. F2 is resolved.
- **Order question 1, chytrid vs white-nose: keep chytrid first.**
  - Chytrid's first line ("Every fungus so far has taken one animal at a time, but this one is counted in species") is what turns the corner into the "Whole species." band. It only works in first place.
  - White-nose ends on the bat costume, and Valley Fever opens with Doug unzipping that costume. A swap would break both transitions.
  - The 90-extinct-species card at about 5 minutes is the mid-video retention spike we want. White-nose (5.7 to 6.7 million bats, the endangered listing) is a strong enough follow-up that the dip doesn't feel like one.
- **Order question 2, Kraków before ergot: keep ergot first.**
  - Moving the tomb up would put two survivals back to back ("Doug is fine." at 6 and 7). That would leave about 1,100 words with no death between 144 and 145, the longest dead stretch in the episode.
  - The "People." band also runs on a second axis as it stands: past to present (medieval bread, then a 1973 tomb, then 1999 Vancouver Island, then C. auris today). The tomb's cancer-lead twist also works as a breather before the final two-item climb.
- **Would I click and keep watching:** yes. The opener reaches "Massospora." at word 33 and "It isn't dying. It's delivering." lands early. All 10 twists are distinct. The sober cards are handled cleanly. The boss thesis (the 37-degree wall) and the cap-as-food kicker are the strongest ending since 013.
- **Policy:**
  - No gore and no symptom detail; ergot has no limbs.
  - No medical advice. The asperigimycins are "only in the lab ... a long way from a cure".
  - The disputed claims are all hedged: Bd count challenged and defended, Salem both sides, Gibellula steering unproven, the curse "according to later accounts", C. auris and climate "only a hypothesis".
  - No drug jokes, no game references, no kids framing.
- **Notes for later stages, not blocking:**
  1. Editor: preview "Gibellula bangbangus", "Pseudogymnoascus" and "asperigimycins" in `narrate`.
  2. Writer/editor: facts.md line 30 still says the script reads "within a short time". The script says "within weeks", which matches row 142 (Penn). Update the note.
  3. Titler: the brief's bans stand. No "zombie", "Impossible", "Actually Exists", game references or "?".
  4. Art: the fuzzy white Doug silhouette is a new death variant. The art director approves it once as a reusable `parasites` death.
- Series bible: the counter is now 147 and the 017 log row is added.

SCRIPT: APPROVED

## 2026-10-13: thumbnail pick: A (3x3 grid) WINS, B (hero half-cicada, "STILL FLYING") kept as thumbnail_b.json
I compared `build/thumbnail.png`, `build/thumbnail_b.png` and both `_small` renders.
1. **Title pairing:** "The Most Disturbing Fungi Scientists Have Ever Found" is a list title with "Most Disturbing" in it. Style bible 2 says a grid goes with "Every / Most Disturbing X" titles, and a hero image goes with "What Dying..." and "How Every X Died". A gives the items and the title gives the frame. B sells one item (Massospora) under a title that promises ten.
2. **Grammar:** B has a red arrow on the thumbnail, and style bible 2 does not allow that ("No face-cam, no red arrows, no circles"). B is otherwise clean.
3. **Opening image:** s001 ("Every fungus on this list has taken over something alive,") uses `scene_ref: thumbnail`. A works as the table of contents for that line and leads into tile 1, "Half a Cicada" / "Massospora." B would also lead into item 1, but it does not show "this list".
4. **Feed size (320x180):** B is bolder, and that is its real advantage. A still reads at feed size: 9 distinct silhouettes on saturated tiles, a white-fuzzed spider and cicada plug, and labels that stay legible. Curiosity: "Sunset Pose", "90 Species", "King's Tomb" and "37°C" are four open loops, while B has one.
5. **Variety concern (noted, not decisive):** 014, 015 and 016 all shipped grids or strata, so 017 makes four grid-type thumbnails in a row. The last hero was 013. Pairing a hero with a list title would break the format rule just for variety, so instead the next hero-friendly title (T1 "What Dying..." / single-subject) should get archetype C.
6. **Wording:** A's labels (Half a Cicada, Sunset Pose, Cave Spider, 90 Species, White Nose, St. Anthony's Fire, King's Tomb, Island Trees, 37°C) and B's "STILL FLYING" contain no title or alt-title words (checked against the metadata ban list). None of them appear in `data/competitors` or `style/`. They are our own wording and come from our script's beats. "St. Anthony's Fire" is the historical name for ergotism, not a competitor label.
7. **Policy:** both are clean. Fuzz is soft and cartoon-style, there is no gore, no anatomy, and the tone is adult. Doug does not appear in A, and in B he is a tiny scale figure.
- No file swap: `thumbnail.json` already holds A, and `studio thumbnail` was not re-run.
- B stays on file as the YouTube Test & Compare variant. **Before any test, remove the red arrow** (graphic designer). The chalky plug reads without it.
- **Condition:** there is no visual-screener report on the thumbnail in this folder yet. Pass A through the visual screener (feed-size check) before the package gate.

THUMBNAIL: A APPROVED (pending visual-screener PASS)
- 2026-10-13: packaged. Script 3 rounds (ergot date, copied marker, chytrid ratio fixed), art assets 1 round (PASS), keyframes 3 rounds (both screeners PASS), thumbnail A (3x3 grid) PASS. Risks: Latin-name pronunciation unchecked in narration.wav (Gibellula bangbangus, Pseudogymnoascus destructans, asperigimycins); real-victim cards must stay sober; grid thumbnails 4 in a row (014-017), vary next. B thumbnail has banned red arrow (remove before any test).

## 2026-10-13: final review round 1 (showrunner)
- QC: no problems in qc.json. Visual screener: VERDICT (main): FAIL (sun arc rendered as hollow outline in s031-s034, s036-s040, s043, s051-s054); VERDICT (shorts): PASS. See reviews/visual_final.md.
- Director replaced the arcs with filled half-disc polys + horizon (shotlist only), nudged the s232 microscope. Shotlist validates. Re-render of `final` requested via .rerender; creative-director package approval deferred to round 2.
FINAL: REJECTED round 1: sun-arc render defect, shotlist fixed, awaiting re-render
