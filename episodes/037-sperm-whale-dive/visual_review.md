# 037 Sperm Whale Dive: Visual Review

## Round 1: keyframes (2026-11-04, contact sheets 01-20, s001-s231 + endslate)

VERDICT: FAIL

Overall the episode is in good shape: Doug is on-model in every shot (red cap, white head, scuba gear consistent from s072),
the death counter runs 287 to 294 with ticks exactly on the seven death shots (s030, s077, s102, s149, s172, s198, s226),
the depth HUD rises monotonically and matches each band, all text is spelled right and uncropped, and all deaths are
cartoon (splash + floating cap, flat costume, crumpled tank). No gore, no kid-show framing; the giant squid eye (s142),
skeletons (s176-s196) and fingernail (s185-s186) are fine. The fixes below are about picture/narration mismatch, one
wrong-scale fact graphic, two stale runs, and the missing opening image.

### Required fixes

1. **s001 (graphic designer)**: tile still reads "(thumbnail pending)". The thumbnail is also the opening image; render
   `build/thumbnail.png` (`python -m studio thumbnail 037-sperm-whale-dive`) before the final render, then re-run keyframes for s001.
2. **s159 (director)**: the scale graphic is wrong and contradicts the line "with about three hundred meters to spare". The
   inverted Burj Khalifa tip reaches about y=905 against the 1,134 M line at y=1000, so it looks ~95% as deep. Scale it so the
   tip sits at about y=808 (828/1,134 of the 290-1000 span; roughly `scale` 0.8 instead of 1.05, check the asset height), and
   move the red "ABOUT 300 M" bracket from x=560 to directly under the tip (x≈760, y 808 to 1000) so the gap reads.
3. **s024 (director)**: "both ships were there to hunt them" shows two neutral sailing ships, a "?" and a shrug, so nothing
   says *hunting*. Add a harpoon (or harpoon + rope) on each ship's bow, or a "WHALERS" label over both, and swap the "?" for
   something that sells "to be fair" (e.g. a small balance/scale icon or "FAIR" label).
4. **s043 (illustrator)**: `tennis_court_side` rotated -90 reads as a thin green-white stripe, not a tennis court. A viewer
   won't get "half a tennis court standing on its end" in a second. Redraw as a recognisable court (green rectangle with white
   lines + net and posts at mid-length), drawn at the same height as the whale, with a "HALF" bracket on it.
5. **s044-s047 (director)**: four near-identical frames in a row (the same six upright whales, same framing; only the orange
   boat and a "!" change), coming right after the same layout at s033-s035. Break it up: s044 push in on two sleepers (eyes
   closed), s046 put "3 OF 6" ticks on three specific whales, and s047 crop close on the boat bumping one whale's head with an
   impact mark, so the touch is the subject instead of a tiny "!".
6. **s166-s170 (director)**: five consecutive near-identical cable-hump compositions (s166 OLD REPAIR, s167 SLACK, s168
   INSPECTION, s169 VOLUNTEERED, s170 WAS VOLUNTEERED). Keep s169/s170 as the joke pair, but change s166-s168: e.g. s166
   close-up of the repair splice box with the label, s167 a wide shot with the slack coil, s168 Doug walking up with clipboard
   (a different camera from s169).
7. **s208 (director)**: Doug is on the 1 KM line and the whale on the 2 KM line, the reverse of s207 (Doug at 2 KM) and of
   the HUD ("MORE THAN 2,000 M"). Put Doug on the 2 KM line next to the whale and the "average" whale ghosted on the 1 KM
   line, so "twice a normal day's work" reads as the gap between the lines.

### Advisory (fix if cheap)

8. **s004 (director)**: cold-open teaser says "two kilometers down" but the HUD shows "DEPTH: 0 M" and Doug is tiny and dim.
   Hide the depth HUD on s004 (or show "MORE THAN 2,000 M") and scale Doug up (~0.3).
9. **s006 (director)**: the red "THE HEAD" title runs into the whale's left edge. Move the title left ~60 px or the whale right.
10. **s161 (illustrator/director)**: "around the tail and flippers": one loop floats detached to the left of the tail. Put
    the loop on the tail stock/flukes.
11. **s132-s138 (director)**: the skin close-up layout appears five times in seven shots (s132, s134, s135, s136, s138).
    Consider pushing in tighter on the single big scar for s138 "OLD SCAR" so it reads as a new beat.
12. **s031, s054, s078, s124, s174, s200 (illustrator)**: the field-guide headings "SPERM WHALE" / "FRIEND?" are too small to
    read at this size. Fine as a recurring prop, since s222 is the legible payoff close-up, but bumping the page-heading
    size would help at 1080p.
13. **s216 (director)**: "the whale at its most dangerous" is a near-empty black frame with a tiny click arc. Intentional
    suspense is OK, but a faint whale outline or larger click arcs closing on Doug would give it a subject.
