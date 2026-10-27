# 028-megalodon-every-era: art review (new assets)

Reviewer: art director, 2026-10-27
Scope: the 24 new library drawings in `asset_requests.md` (previews `assets/previews/028-megalodon-every-era-assets-*`).
Checked against `channel/art_bible.md`, style bible section 7 (Art Director rules 1-9) and Doug's locked design.
Extra checks rendered with `python -m studio art`: the new creatures side by side with the library `megalodon`,
`tylosaurus` and `ichthyosaur` on `#2a6aa6`; the two humans next to Doug at large scale; `mosasaurus` flat and tilted
-50 degrees on near-black; both Panama maps at 0.62. Local extents of all 24 JSONs checked against the requested
anchors.

## Verdict: PASS (all 24 APPROVE; 3 small direct fixes applied, no illustrator rework needed)

| # | Asset | Verdict | Notes |
|---|---|---|---|
| 1 | `shark_cage` | APPROVE | Bars only, Doug clearly visible through them; cap on the roof and Doug seated on the roof both work. Reads on cyan, olive, mid-blue and `#050a1f`. Shackle at (0,-470), extent -162..156 x -470..0. |
| 2 | `megalodon_pup` | APPROVE | Same family as `megalodon` (slate back, countershading, pale belly), mouth closed, hard eye with a brow: menacing, not cute. The black silhouette with a white rim still reads as a shark. |
| 3 | `mosasaurus` | APPROVE (fixed) | Blunt deep skull, no rostrum, so it clearly differs from `tylosaurus`. Reads when tilted and as a red-rim silhouette. **Fixed:** the two far-side flippers sat directly behind the near ones, so only 2 of 4 showed. I moved them 48 units toward the tail so all four paddles read. **Fixed:** three back spray patches spilled dots outside the outline, visible on light water. I moved them down 22 units and set r 44 to 34. Extents unchanged. |
| 4 | `mosasaurus_skull` | APPROVE | Museum fossil on a limestone block, cream bone, not gory. The engraving hatch is light; this is fine at the s039-s045 sizes. |
| 5 | `ichthyotitan` | APPROVE | Bulkier and longer than `ichthyosaur`, with a small eye as requested. Reads as a ceiling at 1.6 and as a silhouette. |
| 6 | `ichthyotitan_jaw` | APPROVE | Long curved bone with glue-crack lines, no teeth. Reads on mid-blue and navy. |
| 7 | `fossil_hunter_girl` | APPROVE | Crude tier with Doug's head, crescent and oval eyes; ponytail, bone in hand. Plain and not kids-show. Her silhouette reads as a child. |
| 8 | `fossil_hunter_dad` | APPROVE | Crude tier, short hair, jacket, hammer. On-model next to Doug. |
| 9 | `sun_hat` | APPROVE | Sits above the cap, and the red dome and brim stay visible (rule 2). Works with `doug_sunglasses`. |
| 10 | `livyatan_skull` | APPROVE | Massive toothy skull in sand with cream teeth in both jaws. Not gory. |
| 11 | `orca_tooth` | APPROVE | Clean cartoon tooth with a crown/root split. |
| 12 | `orca_tooth_worn` | APPROVE | Flat worn top with a pink gum band. Not medical. The gum runs to y +130 (asked 120), which does no harm. |
| 13 | `toothbrush` | APPROVE | Bristles are small, but the shape reads as a toothbrush down to scale 0.4. |
| 14 | `rubber_duck` | APPROVE | Classic shape, bold silhouette. |
| 15 | `statue_of_liberty` | APPROVE | Instantly recognisable. Copper green with a shaded side, torch tip at -620 (the glow reaches -640). |
| 16 | `beringia_map` | APPROVE | `world_map` style, tan bridge in the centre, dashed modern coast. |
| 17 | `panama_seaway_map` | APPROVE (fixed) | Open gap at the centre, with Pacific bottom-left and Caribbean top-right. **Fixed:** a land spray at (-560,-330) r110 leaked green dots above the black frame (y -440). I changed it to (-560,-300) r100. |
| 18 | `panama_isthmus_map` | APPROVE (fixed) | Matches the seaway map, and the canal and lake read. Same frame-leak spray fix as #17. |
| 19 | `container_ship` | APPROVE | Containers, red bottom and stern bridge all read at small size. |
| 20 | `hms_challenger` | APPROVE | A period corvette (white band, gun ports, three masts, funnel) that is clearly not `research_ship`. |
| 21 | `manganese_tooth_nodule` | APPROVE | Rings around a pale tooth, and the pale rim reads on dark water. |
| 22 | `megalodon_vertebra` | APPROVE | End-on disc with strong growth rings. |
| 23 | `stone_tool` | APPROVE | Faceted flake scars and a pale working edge. It reads as a "rock", which is right for a Lomekwi core. The narration and label carry the rest. |
| 24 | `sea_turtle` | APPROVE | Shell scutes, four flippers, bold silhouette. |

## Style consistency
- Two-tier rule (section 7.1) holds. All creatures, props and places are in the detailed tier. Both humans are crude stick figures with the same head, crescent and eye language as Doug. Doug's locked design was not touched.
- Gore (7.8): none. Mouths are dark red interiors, with no blood anywhere.
- Silhouette and rim use (7.7): `megalodon_pup`, `mosasaurus` and `ichthyotitan` all keep a readable outline when blacked out.

## Fixes applied directly (for the record)
1. `assets/library/mosasaurus.json`: shifted far-side flippers (elements 0, 1) by -48 x. Moved back sprays 35-37 down 22 units with r 34.
2. `assets/library/panama_seaway_map.json`, `assets/library/panama_isthmus_map.json`: moved the top-left land spray inside the frame.

## Open items
- None for the illustrator.
- Director: the shotlist validator currently flags `s001: scene_ref 'thumbnail' file missing`. This is expected until the graphic designer delivers `thumbnail.json`, and it is not an art issue.
- Keyframe review (contact sheets) is still to come after `python -m studio keyframes`.

## Keyframes round 1

Reviewer: art director, 2026-10-27
Scope: all 309 shots + endslate (`build/contact/sheet_01..26.png`, spot crops from `build/keyframes/`), checked against
`channel/art_bible.md` and style bible section 7 (Art Director rules 1-9).

### Verdict: FAIL (24 required fixes, all composition: route to the director; nothing for the illustrator)

What already works: the style is consistent across all 11 stops. Every stop has its own readable water/sky pair, the
detailed-tier creatures sit well next to crude Doug, and Doug is on-model everywhere except the two duplicate-Doug shots
below. The counter ticks 226 -> 234 on every death beat. Section header cards (s030, s084, s165, s271) correctly use
white text with no top bar. Every item has its annotations, and there is no gore. The logged exceptions in `decisions.md`
(ice-block "preserved" death s215-s217, capless Doug with the cap on the tooth s307-s309) and the `sunburn` gear
(s108) are on spec.

### Required fixes (director)

**Doug on-model / continuity**
1. **s010**: two Dougs in one frame (one at the booth at 480,556 and one in the cage at 1094,955). Keep one: either Doug
   at the booth with an empty cage, or Doug in the cage with no booth Doug.
2. **s303**: the ghost Doug (560,450) floats up while a living Doug is still in the cage (550,918). Remove the cage
   Doug (empty cage), as in every other death beat (s025, s135, s162, s190, s267).

**Title cards (big red title + date label)**
3. The date label box overlaps the cage top, and the cage rope runs through the red title glyphs. Shots: **s004, s031,
   s060, s111, s138, s166, s218, s244, s272**. Move the cage clear of the title block (for example cage x ≥ 1300
   below the counter zone, or cage lower so its top is ≥ 40 px under the date label), or drop the cage on the title card.
4. **s085**: the cage rope at x≈1600 runs through the reserved counter zone (between the DOUG DEATHS and MEG SURVIVED
   boxes). Move the cage to x ≤ 1280.

**Reveals / silhouettes (bible: silhouette first, colour 1-3 beats later; dark water-tone glow, inside the frame, off the floor)**
5. **s031**: the mosasaurus appears in full colour on the title card, then goes back to silhouette in s034/s035 and is
   revealed again in s036. Make s031 a silhouette (or show no creature) so the first colour reveal is s036.
6. **s035, s062, s113, s245**: the silhouette glow renders as a big pale speckle disc. In s035 it spills onto the sand,
   in s062 it bleeds into the sky band and touches the caption bar, and in s245 it runs off the bottom of the frame. Use
   `"glow_r": 0` + a dark water-tone `spray` placed before the silhouette (s035 `#3f7f96`, s062 `#1b4f86`, s113 `#2c5a4c`,
   s245 keep the dark tone but pull it inside the frame), and add a ground-colour `rect` after the spray in s035.

**Layout variety (no more than 4 shots in a row with the same composition)**
7. **s278-s288**: 11 consecutive "small cage bottom-left + cream board right" frames. Break it at least every 4 shots.
   Suggestions: s280/s281 a full-frame scientist + clipboard scene (like s254), s283 full-frame rock strata with Doug
   standing on it, s286 a full-frame timeline with Doug walking along it, and s288 Doug holding the stone tool next to
   the meg.
8. **s088-s093**: 6 board shots in a row. Turn s089 (exploding star) into a full-frame space shot like s094, or turn
   s092 into Doug at the sea floor with the three blasts overhead.
9. **s203-s208**: 6 board shots in a row. Make s206/s207 (food scattered vs dense patches) full-frame open-water shots
   with Doug's cage among them.
10. **s146-s150**: 5 board shots in a row. Make s148 or s149 a close-up of a shark's flank with Doug touching the
    denticles through the bars.

**Overlaps / text**
11. **s057, s135**: the death debris (splash in s057, sign + cap in s135) crosses the caption bar. Keep surface props at
    x outside the caption bar span or start them at y ≥ 110.
12. **s234**: the wordart "WHERE PUPS WERE BORN" starts over the second tree's canopy (treelines count as land). Shorten
    it (for example "PUPS WERE BORN") and centre it at x ≥ 1100, or remove the second tree in this shot.
13. **s237**: the label "PUPS GREW UP HERE" sits on the sun. Move the sun to about (1720,330) per the counter rule, or
    move the label left.
14. **s242**: the label "NO PUPS" sits on the cage top. This shot also has 3 labels on screen (max 2). Merge them into
    one label, "NO SEA, NO PUPS", or drop "NO NURSERY".
15. **More than 2 labels on screen** (rule 7.4): **s017** (2025 + NURSERY + NOT NEEDED?), **s187** (SEA 36 °C +
    MEG 27 °C + +9 °C), **s256** (ONLY + 11,000 + 24,000), **s261** (MILLIONS OF YEARS + two crossed dates), **s286**
    (3.6 + 2.6 + 1 MILLION YEARS EARLIER). Drop one each. For the thermometers and timeline ticks, numbers can go
    inside the asset as small bar text.
16. **s077**: the wordart "THE SMALL ONE" lies across the ichthyotitan's belly and flippers. Put it under the megalodon
    (y ≈ 900) with a short red arrow to the shark.
17. **s084**: the coin sits behind "SS." of "COIN TOSS.". Move the coin above the text (y ≈ 300) or to the right of
    the period.
18. **s028**: the wordart "PLENTY TO EAT" sits on the green seagrass (lime-on-lime rule). Raise it to y ≈ 560.
19. **s002**: the hoisted cage covers the open time-machine door (door zone x +180..+330 x scale must stay clear).
    Move the hoist about 200 px right.
20. **s176**: the red X hides almost all of "O2". Shrink the X to about 70% so the text reads, or put the X beside the
    text.
21. **s172**: the crossed-out "plankton" is a faint grey circle that doesn't read. Use the shell from s170 at scale
    ≥ 0.5 under the X.
22. **s148, s149**: the denticle triangle pattern spills past the right edge of the grey panel. Clip it, or end the
    rows one triangle earlier.
23. **Endslate**: the wordart "DOUG'S NEXT DEATH" starts at x≈30, outside the safe area (x ≥ 64). Shift it right or
    shrink it.

**Zone colour consistency**
24. **The Giant Ichthyosaur**: s060-s061 use water `#3f8fc4` with sky `#cfe9ff`, while s062-s083 use `#2a6aa6` with
    sky `#8faecb`. Set s060/s061 to `#2a6aa6` / `#8faecb` so the stop keeps one colour.

### Minor (fix if cheap, not blocking)
- The Ice Age underwater shots (s203-s209) and The Last Megalodon (s272-s300) use the same water, `#3a9ad9`. A
  slightly greener ice tone (for example `#4a9ec8` with sky `#dfe6ec`) would keep every stop distinct.
- When the cage hangs between x 760 and 1160 (s051, s052, s056, s086, s087, s097-s110 and the Canal cage shots), the
  rope goes behind the caption bar. It reads fine, but nudging the cage off that span is cleaner.
- **s024**: "2x DOUG" has a dashed line but no Doug next to the pup. A small Doug (scale 0.5) under the line would make
  the comparison literal (scale-comparison layout).
- **s309**: the second silhouette of the next giant lies on the sand. Move it into the water band.
- **s066**: Ruby is drawn as a solid black silhouette for scale. She would read better in her normal colours.
- **s252**: the six stacked Burj Khalifas read as grey spikes. A slightly wider scale (or one labelled tower plus "x6")
  would help.
- The contact-sheet narration strip shows "Gat?n"/"Col?n" (the strip font has no glyphs for ú/ó). The on-frame labels
  are correct. This is only a note for the editor if burned-in subtitles use the same font.

### Next
Director: apply fixes 1-24, re-render only the touched shots with `python -m studio keyframes 028-megalodon-every-era --shots ...`,
then I'll review round 2. No illustrator work and no Doug rig changes are needed.
