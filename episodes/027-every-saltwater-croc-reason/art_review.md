# 027-every-saltwater-croc-reason: art review (round 3: keyframe fixes)

Reviewer: art director, 2026-10-26
Scope: the 89 shots the director re-rendered in round 1 (full-res keyframes), plus the neighbours on all 28 contact sheets (to check the run breaks),
plus the director's second-look list (s282, s235, s195).

## Verdict: PASS

The hard rules still pass. There is no gore, teeth never touch Doug, and every death is a splash plus cap plus ghost. Doug is on-model and readable
on every ground. Zone colours follow the ramp in the art bible.

## Round-2 fixes: all resolved
1. **`croc_jaws_open` severed edge.** Fixed in s054, s055, s065-s068, s070 and s105. The back of the head now runs off the right edge, and every head sits in water or
   runs off the frame. The s068 arrow and "?" and the s070 SALT GLANDS arrow point at the new mouth. The s054 fish and speed lines are clean, with no stray dash.
2. **Text over the treeline.** All 40 shots are clear. Words sit in open sky at y ≤ 255, and the chapter titles sit at y 245. I checked the tightest counter clearances at
   full res (s114, s120, s122, s123): no overlaps.
3. **Composition runs.** Every run is now 4 shots or fewer:
   - s132 is a calendar card, s134-s136 are the Australia map and s137 is a two-bar chart.
   - s146 is the tape-end close crop, s148 is the sleeping close-up and s151/s152 are the tape diagram on cream.
   - s161 is the sling over the sea and s170 is the release-point close-up.
   - s282 is a coin card and s283 is the boat alone.
   - s298/s299 show the graph at full width.
4. **s107.** Doug wades with a shock face and a ripple at his shins. The flood runs to the bottom of the frame and the rectangle has no edge.
5. **s086.** Doug's feet are on the sand.
Visual-screener items are also confirmed: s030 knee ripple, s041/s042 ALLIGATOR label, s154 FAR AWAY clear of the crate, s227 shows four ticks and one X,
s245 is text on black, and s292 uses the standard splash on the jetty.

## Second-look list
- **s282 (fixed by me).** The `us_quarter` "25¢" was wrong for an Indonesia beat. I added the library asset `assets/library/coin_generic.json`, which copies
  `us_quarter` with the value text removed: a silver coin with a star motif and no country. I swapped it into s282 and re-rendered. *Illustrator: use `coin_generic`
  for any non-US coin beat from now on.*
- **s235.** It passes. The standard death now reads: splash, white roll arcs, cap on the bank, ghost Doug. The grey cone is gone.
- **s195.** It passes. The `kitchen_counter` prop stands on the waterline, and its top is level with the branch, about half Doug's standing height. The dashed height line
  and the KITCHEN COUNTER label make the scale read, and s196-s212 keep the same low branch. In s201 the croc's head and front third rise beside the branch with the jaws closed,
  under half the body. That meets the Lunge rule.

## Small fix I made
- **s123.** "FOLLOWED." (size 140, centred at x 960) almost touched the bottom-left corner of the counter box. I moved it to x 880 and re-rendered.

## Optional (not blocking, carried over)
- s084, s286, s287: the red X still covers only the middle letters. A strike line across the whole word would be cleaner.
- s001 is the thumbnail placeholder (graphic designer).
- s197 uses a black silhouette with a red rim for the coiled croc. That is on-system (house silhouette device, glow off), so keep it.

Contact sheets were rebuilt from a full 331-shot keyframe pass after my --shots run (see the note to the showrunner), so all 28 sheets in `build/contact/` are current.
