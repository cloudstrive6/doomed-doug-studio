# 055 decisions

## 2026-11-22: script gate (creative director): GO
- Screener draft-2 FAIL items verified closed: item 7 now reads "then got away, and the orcas got nothing" (Arnbom 1987);
  facts.md cites Gero, Gordon & Whitehead 2013, *Proc. R. Soc. B* 280:20131113 (Dominica).
- Brief conditions met: no-dive fact first, payoff "thirty-five orcas outside" by ~0:10, item name by word 34, twist ~word 121;
  attack-stage axis, 9 items, 2,162 words (~11.1 min); deaths 403-408 (6), survivals 1/5/8; orcas stay weather, no orca item;
  no gore (kill at 11:00 told without wounds, deaths cut to black); honesty line that the ring failed in 1997; date corrected to
  21 October 1997 per Pitman 2001.
- One CD wording fix applied directly (no fact impact): item 2 "Doug volunteers for a shift" contradicted "Doug did not agree to
  this"; now "Doug's name is on the rota, because he agreed to wear the costume." Stage direction: name pencilled in by someone else.
- Notes for downstream: art director signs off the calf costume (grey, block head, no big eyes, no smile; kid-appeal risk) and
  THE RING card; titler must not imply the whales win or orcas fear them; series bible counter goes to 408 at final approval.

## 2026-11-22: shotlist (director)
- 203 shots, ~11.4 min at 195 wpm; every spoken word of draft 2 once, in order (checked by diff); max 24 words/shot; estimated
  longest static stretch under 4.1 s. Doug in 140/203 shots (69%). Generator: `build/gen_shotlist.py` (scratch, git-ignored).
- **Colour ramp (attack stage, not depth):** water steps darker per item, sky greys toward the attack: items 1-3 `#3a9ad9`
  (polar shots `#dfe7ee` sky, cold shown with ice, not dark water), 4 `#2f7fbf` / `#b9c4cc`, 5 `#2a6aa6` / `#aab8c4`, 6 `#24609e` /
  `#9aa8b6`, 7 `#1f5a94` / `#8a98a8`, 8 `#18497e` / `#6a7686`, 9 first light `#e88a4a` over `#f2a24a` on `#14365e`. Depth-ramp
  colours only on real dive cross-sections. Cards cream `#f4f1dc`, sober cards `#15181a`, cut-to-black `#0b0f14`.
- **THE RING** is drawn inline (no asset): 160x112 tile under the counter (x 1510-1670, y 202-314), so the reserved HUD zone is
  x 1300-1860, y 100-320 on every shot. Item 7 flips it to a mini world map (2 ticks Galápagos, 1 Gulf), fins stay 9. Red frame
  and red-on-pink counter from death 408 to the end.
- **Costume count vs brief ("at most 4 times"):** the approved script puts Doug in the calf costume in items 1, 2, 4, 5, 7, 8 and
  9 (stage directions), and the art bible's costume-continuity rule keeps it on every Doug in that run, so it is on screen in
  most Doug shots; off only for the scripted kayak run (item 3). Art director: please confirm, or tell me which items to strip.
- Deaths: 403 cap only beside the rolled calf; 404 `doug_frozen_kayak`; 405 cut to black then cap on the hydrophone cable;
  406 a tiny X-eyed Doug on the horizon, then the cap lands; 407 cut away, then cap in the ring gap; 408 gap opens, cut to black.
  No orca is ever shown touching a whale or Doug. "Badly hurt" and "killed" are told with labels and empty gaps only.
- Narrator's quiet disappointment (s170): the pencil has already drawn a plain grey headstone reading DOUG / 408 (no cap on it,
  so only one cap in frame).
- Shorts: short01 s094-s107 (Marguerite, hook from s090), short02 s112-s123 (Tail, opens on "five meters"), short03 s161-s170
  (Rescue, hook from s154). Each ends on its payoff. Titles are drafts so `shorts validate` passes; youtube-titler replaces them.

## 2026-11-22: costume count (art director ruling, logged by director)
- **Deviation from brief, approved:** the calf costume is on in 7 of 9 items (1, 2, 4-9). It comes off only for the scripted item 3
  kayak run, not the brief's "at most 4". The art director reads "max 4" as a cap on featured costume beats (thumbnail, item 1, item 5,
  boss), not on the items he wears it in. Costume continuity rule (049) applies, and the costume passed the kid-appeal check. Conditions
  were checked at keyframes: varied framing (top-down rings, cards without Doug, headphone shots, item 3 break) and no costume-only
  gags in items 2, 4, 6 and 7.
- Keyframe fixes: s061 Doug switched to `sit` at y 390 with cap_snow at 390 (matches s060/s062). `point` at y 432 still left his
  legs hanging below the hull, so the line is carried by the speech bubble, which now clears his head. Clipboard rows in s035/s039/s040
  are centred in the ruled rows (y 510/580/640, x +20 off the time column, size 34). Costume Doug lowered 45 px in 15 shots where the
  hood touched THE RING tile (s022 s032 s037 s038 s047 s057 s069 s074 s075 s114 s117-s120 s122). s152 "CONTACT." raised clear of the fins.
