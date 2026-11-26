# 058 decisions

## 2026-11-25 · Script gate (draft 2 + outro fix): APPROVED
Creative director. Read brief.md, script.md, facts.md and script_review.md (draft 2 screen).

- The draft 2 screen failed on one required fix only (outro CTA copied from 049) and stated "Fix that one sentence and the script
  passes; no other re-check is needed". All other gates passed: facts 0 errors, opening 8, structure 8, voice 8, TTS/policy/length PASS.
- Fix verified: l.256 now ends "Subscribe before Doug finds a worse pod." Grep of `episodes/0*/script.md` finds it only in 058. One CTA,
  no comment prompt, outro 26 words (cap 30). No other line changed; 2,160 spoken words, about 11.1 min at 195 wpm.
- Would I click and keep watching: yes. Cold open with a death stake in sentence 1, "The Speaker." at word 34, twist by about word 88, a
  specific payoff (Doug as the orca who can't porpoise), honest "why" (two hypotheses, attributed, neither ruled out).

### Sign-off (a): item 6 reversal. APPROVED
The brief was wrong. The documented case is a female killer whale (Sædís) seen with a newborn long-finned pilot whale calf, August 2021,
off Snæfellsnes (Mrusczok et al. 2023, *Canadian Journal of Zoology*, doi 10.1139/cjz-2022-0161; Dalhousie 2023). No source exists for
pilot whales with an orca calf. The script's version is better than the brief's: it gives the pilot whales a plausible motive (orcas
taking calves), clearly labelled "a suggestion, not a finding", and the re-hook into item 7 ("That calf had a family") now makes literal
sense. Conditions for downstream: the calf is drawn plain (dot eye, no cute proportions); the "NOT HERS" label stays; no packaging may
say "adopted" or imply pilot whales raised an orca.

### Sign-off (b): dropping "A Third Their Weight". APPROVED, with a wider rule
NOAA maxima give about 10 t vs about 2.3 t (roughly a quarter), and comparing maxima of two species is shaky anyway. Titler rules:
- No weight or size ratio in the title or thumbnail: not "a third", "a quarter", "four times", or "half their size" (lengths are about
  9.8 m vs 6.7 m, so "half" also fails).
- Allowed scale wording, if any: "Smaller" / "Much Smaller" (the script says "the bigger animal, by a long way"), or no scale phrase.
  Preferred leads remain brief §1 ("Why Orcas Flee When Pilot Whales Show Up", "Why the Ocean's Top Predator Runs From Pilot Whales").
- Location claims stay honest: "off Iceland" / "the bay"; no "out of fjords" (per facts.md title notes).

### Notes downstream
- Editor: check Chirp reads "Sædís" (SIGH-deess); if not, write "Saedis" in narration text.
- Art director: approve the WHO RAN scoreboard and the orca costume (new gear) before keyframes.
- Counter 420 to 425 (deaths at items 1, 2, 4, 7, 8). Series bible lore is updated at packaging/upload, not here.

## 2026-11-26 Director: WHO RAN board tallies moved (visual screener round 1, fix #1). FOR CD SIGN-OFF
The screener flagged the board as reading backwards: header "WHO RAN", but the tally ticks piled up under PILOT WHALES (7 by the end),
which says "pilot whales ran 7 times", the opposite of the thesis. Meanwhile the red ORCAS stamp sat under EVERYONE ELSE, so the board
contradicted itself.
- Change: every tick now lands in the **EVERYONE ELSE** column (s002-s219). The **PILOT WHALES column stays empty all episode**:
  they never ran, and that's the joke. At the boss (s216 from 0.88, s217-s219) the red **ORCAS** stamp goes on a second line under
  the ticks, in the same column.
- Each tick still marks a beat where someone other than the pilot whales backed off (Doug included). No narration changes.
- The board asset (`who_ran_board`) artwork is unchanged; only its description changed (tally zone usage). The tick and stamp positions
  live in `build/lib058.py` (`tick_lines`, `hud`).
- I rejected the screener's alternative of renaming the header to "WHO BACKED OFF?" / "NOT PILOT WHALES" because it's weaker.
- CD: please confirm this reading of the device. Thumbnail and packaging don't use the board, so nothing changes there.

## 2026-11-26 · CD sign-off: WHO RAN board change. APPROVED
Creative director. Checked keyframes s130 (423) and s219 (425) full-res.
- The new reading is right and funnier: PILOT WHALES stays empty the whole episode; every tick lands under EVERYONE ELSE; at the
  boss the red ORCAS sits on its own line under the ticks. The board now says the thesis at a glance and no longer contradicts it.
- Agree with rejecting the "WHO BACKED OFF?" / "NOT PILOT WHALES" rename.
- Script stage directions (l.2, 40, 216, 250) still say ticks go under PILOT WHALES. Those lines are never spoken and the shotlist
  is the source of truth; no script edit needed. Series bible: no lore change (episode-only device).

## 2026-11-26 · Package gate: thumbnails A/B/C with ranked titles. A APPROVED · B and C CHANGES
Checked at full size and at 168 px feed size (`build/*_small.png`). None of the titles or thumbnails uses a weight or size ratio
or says "adopted"/"raised". Every title is honest against facts.md: Selbmann 2022 and HI news support "abandon feeding events",
and 425 deaths support "How Doug Would Die". The decision is about the art.

**A. "Why Orcas Give Up Their Kill When Pilot Whales Show Up" + WRONG WAY: APPROVED.** At feed size the wall of round black heads
pulls the eye. Doug's costume points into the pod while the real orca's tail exits right with a sweat drop, so WRONG WAY lands
and the title gets its twist. It also works as the opening frame.

**B. "Why Orcas Leave Their Kill to Get Away From Pilot Whales" + THEY CHASE: CHANGES.**
1. At 168 px the pod (pilot_whale at scale 0.34-0.38) reads as four small grey dolphins in the corner. "THEY" has no visible
   referent, so the chase doesn't read. Scale the pilot whales to about 0.6, pull them in to x 80-420, and point all of them right,
   toward Doug and the orca, so the round melon heads read at feed size. Keep the orca at least as large as the biggest pilot whale
   (raise orca from 0.6 to about 0.7 if needed). The pilot whales must not look bigger than the orca.
2. (Recommended) The small_fish's black band reads as a bandit mask, not a dropped meal. Use a plain fish, and place it falling
   behind the orca (about x 980, y 300) so it reads as "dropped".

**C. "How Doug Would Die Dressed as an Orca Among Pilot Whales" + TOO SLOW: CHANGES.**
1. Scale inversion. pilot_whale_head is at 2.2 and 1.4, against fleeing orcas at 0.20-0.22, so one pilot whale towers about three
   times over the orcas. That tells the viewer pilot whales are giants, the opposite of the episode's paradox ("the bigger animal,
   by a long way"), and it breaks the spirit of the 2026-11-25 no-size-ratio rule. At 168 px it also reads as a black rock, not a
   whale.
   Fix: replace the two giant heads with a wall of 4-5 pilot_whale_head at scale about 0.8-1.0. Heads stay below about y 250 so
   they don't run under TOO SLOW. Eyes look at Doug (the script's "the wall of black heads turns toward him").
   Raise the fleeing orcas to about 0.45-0.5, with the nearer one partly exiting the right edge. Each orca must be visibly longer
   than any one pilot whale head is tall.
2. Keep everything else: Doug's grimace, the centimetre-of-air splash, the red sky and the TOO SLOW placement all work.

Re-render B and C (`python -m studio thumbnail` / small previews). Then send all three back to the visual screener and to me.
A may ship as-is. If B or C can't be fixed in time, ship A and drop the failing variant rather than run it.

## 2026-11-26 · Director: art review round 2 fixes applied (in `build/gen_shotlist.py`)
- Required: s187 is now the surface fin shot as specced (4 pilot fins, orca_fin at 1300, wake lines, splash). s068/s095 use
  `push1`/`push2` with trolley/groceries at the AD's coordinates (new `push_groceries()` helper); s068's second man is 150 px left.
  The s122/s123 mask is widened to x 532, y 545, w 56, h 168.
- Recommended: s201 shows the orca (0.7) and pilot whale (0.65, facing it) side by side at true relative length, with equal
  10 TONNES / 2.25 TONNES labels; Doug moved to the right. s125's top arrow (bend 260) now arcs over Doug. s006 has the speaker
  on the left with waves, 4 tagged whales facing it with short red arrows, the 5th turned away, and a confused Doug.
- Validate shotlist OK; full keyframes re-run (223).

## 2026-11-26 · Package gate re-review: thumbnails B and C (reworked). B APPROVED · C APPROVED (art). Visual screener pass still required
Creative director. Checked `build/thumbnail_b.png` and `build/thumbnail_c.png` at full size and at 168 px (`*_small.png`), against
`thumbnail_test_b.json` and `thumbnail_test_c.json` (rendered 00:20). There is no visual-screener report on these renders yet, since
`visual_review_keyframes.md` covers keyframes only. My approval of both is on the art. Neither variant ships until the visual screener passes them.

**B. THEY CHASE: APPROVED.** Every fix from the earlier package gate is done.
- Fix 1: the pod is three pilot_whale at 0.58-0.60, at x 120-380, all pointing right toward Doug and the orca, two of them breaching
  with splashes. At 168 px they read as a pod of round-headed whales in pursuit, so "THEY" now has a referent. The orca was raised
  to 0.7 and is still the biggest animal in frame. No pilot whale looks larger than it.
- Fix 2: the banded small_fish was replaced by a plain silver_fish. It tumbles behind the fleeing orca's tail (x 900), so it reads as
  a dropped meal. Doug in the costume is stuck between the pod and the exit, so the title and image match.

**C. TOO SLOW: APPROVED.** Fix 1 is done and everything I asked to keep was kept.
- The two giant heads are now a wall of five pilot_whale_head at 0.85-1.0. Their tops stay around y 340, so they sit well clear of
  TOO SLOW, with the eyes and deadpan lids facing right at Doug.
- The fleeing orcas are at 0.45/0.5, and the nearer one exits the right edge. Each orca is more than twice as long as one head is
  tall, so the scale inversion is gone and nothing contradicts "the bigger animal, by a long way".
- Doug's grimace, the splash, the red sky and the TOO SLOW placement are unchanged.
- Non-blocking note: at 168 px the wall reads more as "a row of dark humps" than as whales, because the eyes fall below one pixel.
  The title ("...Among Pilot Whales") carries it, and this is the A/B test variant, so I'm not holding it. If C loses the test
  badly, the first thing to try next time is a bigger, brighter eye on pilot_whale_head (an art-director call).

Packaging rules re-checked: no weight or size ratio, no "adopted"/"raised", and every title stays honest against facts.md.
Next: the visual screener screens A/B/C (the full-size images plus the 168 px small versions). If it passes, the episode can move to `packaged` with A as the primary and B and C as test variants.
If the screener fails B or C, ship A alone, as the earlier package gate set out.
- 2026-11-26: rounds: script 2 (+outro fix), art 3, thumbnails 3 (B/C reworked for feed size). Risks: Sædís pronunciation via IPA unverified by ear; chapters ~1-2s late, regenerate from final render; WHO RAN board ticks under EVERYONE ELSE (CD approved); Doug push1/push2 poses added to doug.py by art-director.

## 2026-11-26 · Final package gate (post-render): APPROVED
Creative director. I reviewed `metadata.json`, `build/thumbnail.png` plus the `_small` version at 168 px, `build/chapters.txt`,
`build/qc.json` (no problems, 702.4 s), `visual_review.md` (main PASS, Shorts PASS), the first 60 s (frames at 1 s and 45 s pulled
from `final.mp4`, samples f_001-f_003) and script lines 1-40.

- **Title kept**: "Why Orcas Give Up Their Kill When Pilot Whales Show Up" (54 chars, subject in the first two words on mobile). The
  video delivers it: script l.238 says the orcas "were often feeding when the pilot whales arrived, so they gave up their meal to
  leave" (Selbmann 2022; HI news "abandon feeding events"). I swapped in no alt. "Leave Their Kill to Get Away" is the same promise
  but weaker, "Drop Their Kill and Flee" overclaims speed for every encounter, and the Doug title belongs to variant C's test.
  The title has no size or weight ratio and doesn't say "adopted" or "raised", so the 2026-11-25 rules hold.
- **Thumbnail A (WRONG WAY)**: same verdict as the art gate. At 168 px the wall of round heads, Doug's costume pointing into the pod
  and the orca exiting right with a sweat drop all read. It is the 0-1 s frame of `final.mp4`, so the click and the opening match.
- **First 60 s**: the death stake is in sentence 1, the payoff promise in sentence 2 ("the real orcas leave without him"), the THE
  SPEAKER card appears at 0:10, and the twist (4 of 5 swam toward the sound) comes at about 0:15. The 45 s frame (tagged whales
  converging on the speaker, Doug with a "?") matches the narration. The counter reads 420 and the WHO RAN board is empty, as
  intended. Pacing is about 198 wpm while speaking.
- **Description**: it is honest and sourced (six links that match facts.md), with the AI-use and cartoon disclaimers and one CTA.
  One fix I applied: three timestamps ran 1 s later than the render's `build/chapters.txt` (4:05, 8:12 and 9:35, against 4:04,
  8:11 and 9:34; the shots start at 244.996, 491.79 and 574.798 s). I copied the render's chapter list over them verbatim, and
  `validate metadata` passes. Note: `youtube.py` only substitutes `{{CHAPTERS}}`, and this description hardcodes its timestamps, so
  any re-render must re-sync them by hand.
- **Policy**: deaths are cartoon cut-aways only, the humour is adult-coded, the playlist is `animals` (057 was `ocean`), and
  `paid_promotion` is false.
- **Watch item for the growth analyst**: orcas are a co-star again (051, 055, 058). Their CTR history supports it (021 at 4.3%), but
  the next 5 episodes should not have orcas in the title.
- Series bible: 058 added to the episode log (counter 420 to 425).

FINAL: APPROVED
