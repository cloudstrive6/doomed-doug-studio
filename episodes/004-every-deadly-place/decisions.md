# Episode 004: decisions

## 2026-10-01: episode selected (creative director)
- Picked backlog idea #4 (places, 6.7) over #15 Creepiest Fossils (8.1). That resolves memo decision 3. Reasons: #15, #24
  and #27 are all prehistoric, and ep 003 is prehistoric (no topic back-to-back). #14 Venom is held until ep 002 day 7 (10-11).
  #16/#25 are in the saturated ocean lane. #4 is a "dying in every X" severity ranking (the strongest launch formula), the
  format phrase has 3 copies, and it opens the last empty playlist (`places`).
- Engines: Simple Paint "The Worst Places To Die In Space" 1.91M (8.06x); PE "What Dying on Every Planet Would Be
  Like" 12.7M; Paintify "Every Unexplored Place on Earth" 1.55M (5.97x).
- Title skeleton is T1 ("What Dying in Every Deadly Place on Earth Would Be Like"), not the backlog title. The
  backlog title fails titler rule 5 (no scope device), and 003 was T2, so T1 alternates.
- Axis: severity (how fast and how surely each place kills), with spoken bands "Hours.", "Minutes." and "Seconds.". 11 items, counter
  27 to 36, survivals at Lake Natron and Lake Maracaibo. Lake Nyos is played straight with no joke (real mass casualty).
- New lore candidate: Doug's suitcase with travel stickers (`places` prop). It goes into the series bible at script approval.
- The stage stays `idea` until the script writer delivers draft 1.

## 2026-10-01: script approved (creative director)
- Approved draft 2. The script passed screening in 3 rounds: facts have 0 errors and 0 gaps, and policy is clean. Scores are
  hook 9, structure 8 and voice 8. The length is 3,188 words (about 16:21).
- Checked against the brief:
  - All 11 items are in brief order, with the counter running 27 to 36 and survivals at Natron and Maracaibo.
  - "Death Valley." is at spoken words 34-35, the twist lands at about word 133, and the opener is the thumbnail grid.
  - Nyos has no joke, and Nyiragongo covers geology only with no Goma casualties.
  - The banned items are absent: no Morecambe 2004, no Everest bodies and no dead Natron flamingos.
  - The viral myths are debunked with sources: snakes per square metre, Natron "stone", quicksand, and the 1913 dispute.
  - There is no survival or safety advice. The myth-busts are framed as findings.
- Why I approve: every stop has a real twist, the "Hours, Minutes, Seconds" bands make the escalation easy to follow, and
  the Doug beats are adult-coded (the smug quicksand expert, the sunscreen in polar night, the optimistic timer, the
  extinguisher running out first). The Nyos tonal drop into the Maracaibo release is the strongest pacing in the channel so far.
- Known weak line, not blocking: the Natron kicker ("A lake this caustic is also the main nursery...") restates a
  fact from four lines earlier. The director may give it a strong visual (flamingo chicks on the salt-crust moat) so the line still earns its place.
- Lore: Doug's suitcase is now canon in the series bible as the standard `places` prop. The art director needs a
  stickered travel variant that is distinct from the existing `suitcase.json` ("HEAVY", escaping sock), with stickers added
  per death. The death counter moves to 36 after this episode passes QC.
- Next: director shotlist. Titler default is T1, "What Dying in Every Deadly Place on Earth Would Be Like". The description
  must say "11 of the deadliest natural places on Earth".

## 2026-10-01: package approved (creative director): GO
- Thumbnail (Archetype A 3x3 grid): approved. Visual screener and art director both passed it. It is a clean severity read
  (sand, then ice, then neon, then lava), Nyiragongo is the boss tile, Nyos is off, there are no bodies, and no label uses a title word.
- I applied both optional notes myself in `thumbnail.json` and re-rendered (`python -m studio thumbnail`):
  1. Natron Doug and his flamingo costume went from scale 0.37 at y=160 to 0.43 at y=184 (x=990). Doug's red cap and deadpan
     face now read at 320 px. I tried 0.47 first, but it cropped the costume's flamingo head at the tile top.
  2. The Antarctic tile gets six white icicles hanging from the top edge (`#e8f8ff`, black 4 px outline), and the snow spray
     density goes from 0.15 to 0.30. The tile now says "lethal cold" and not "cosy cabin". I rejected `thermometer` because its red fill means heat.
- Metadata: approved as is. The T1 title, "What Dying in Every Deadly Place on Earth Would Be Like", is delivered by the video
  (11 places, deaths ranked hours, then minutes, then seconds). The description says "11 of the deadliest natural places", and every
  teaser in it (lanceheads, quicksand myth, Natron "stone" myth, Maracaibo lightning) is in the script. Sources, disclaimer
  and AI-use note are present, playlist is `places`, and `validate metadata` returns OK.
- Next: editor (narrate, render, QC).
2026-10-01: rounds: script 3, keyframes 3 (art+visual), thumbnail 1. Risks: Nyos sombre item, pronunciations unverified by ear (Chirp), Kivu gas figure hedged.

## 2026-10-01: final package approval (creative director): GO
- Title: keeping T1, "What Dying in Every Deadly Place on Earth Would Be Like". It is the proven "what it feels like to
  die in every X" outlier formula and the video delivers it (11 places, ranked hours to minutes to seconds). None of
  the alternates is clearly stronger. "How Every Deadly Place on Earth Would Kill Doug" spends words on a name nobody
  searches yet. The "Deadliest... Nature Fights Back" alternate is vague, "Farther Doug Goes" implies a distance axis
  we don't use, and "Booked Anyway" is weaker as a curiosity gap. No swap.
- Thumbnail (`build/thumbnail.png`): final render checked. The 3x3 grid reads sand, then ice, then neon, then lava.
  Nyiragongo is the boss tile, Natron Doug reads with his cap and deadpan face, the Antarctic icicles are in, there
  are no bodies and Nyos is off. It matches the title and opens the video (frame at 0:01 is the grid).
- Description and chapters: they are accurate. They say "11 of the deadliest natural places", every teaser is in
  the script, and the sources, disclaimer and AI-use note are present. The `build/chapters.txt` list has 12 entries
  from 0:00, all at least 10 s apart, in script order, and each one opens on the item name. Tags and playlist
  (`places`) are fine.
- First 60 s: the grid is up at 0:01, Doug with his blank suitcase and DOUG DEATHS: 27 is up by 0:06, "Death Valley"
  is spoken within the first 35 words with its chapter at 0:11, and the twist ("watching the wrong thermometer", 201°F
  ground) lands well inside 45 s with the WRONG ONE visual. The night beat keeps it moving. This would keep me watching.
- Main video: `qc.json` is clean (1009.6 s, about 190 wpm overall), and the post-render visual screener passed the main
  video and thumbnail.
- Condition (Shorts only, does not block the long-form): the visual screener FAILed all three Shorts on the
  9:16 zoom-crop (fixes 1-4 in `visual_review.md`: s243 "5x THE SUN" clipped, s071/s094-s096 Doug cropped, plus the
  x>1600 sweep). No Short goes up until the director's fixes are re-rendered and the Shorts pass re-screening. The
  long-form `final.mp4` must not be re-rendered over an approved build without a fresh `qc`.
- Non-blocking: the s123 "CHART" placeholder box (about 1.5 s) gets a frostbite-grid motif if the director touches it again.
- Lore: QC has passed, so the series bible now has the death counter at 36 and an episode log row for 004 (same as the 003 precedent).

FINAL: APPROVED
- Showrunner note: the Shorts hold above is resolved. The director fixed the safe-area shots, the final and Shorts were re-rendered, QC exits 0, and the round-2 visual screen PASSED (main video, thumbnail, all 3 Shorts).
FINAL: APPROVED
