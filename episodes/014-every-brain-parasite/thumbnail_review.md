# 014 Thumbnail review (visual screener)

## Round 1 (2026-10-11): build/thumbnail.png from thumbnail.json (variant A, 3x3 grid)

Title: "What Dying From Every Brain Parasite Would Feel Like"

Checked: full size at 1280x720, a 320x180 downscale, build/thumbnail_small.png, and 2x crops of the Lancet Liver Fluke, Spirometra, Gnathostoma and Balamuthia tiles.

**Readability at feed size (320x180):** PASS. All 9 labels are legible and spelled correctly (Killifish Fluke, Lancet Liver Fluke, Gid Tapeworm, Rat Lungworm, Pork Tapeworm, Spirometra, Gnathostoma, Halicephalobus, Balamuthia). They match the chapter names and none overlap the drawings. The green-to-black ramp reads clearly. The near-black boss tile with the red cap on the flowerpot is the strongest eye-catch. The red cap shows up in 8 of 9 tiles, so the image is plainly Doug's.

**Cropping:** PASS. Nothing important is cut off by the tile frames. The tile margin is 26 px. The "Balamuthia" label ends at about x=1150, so the YouTube duration badge (bottom right) may touch the pot tile's corner but won't cover the label.

**On-model Doug:** PASS. Row 1 Doug (killifish, ant and sheep costumes) has the white round head, red cap and line-art face, so he's on-model. The 4 head-diagram tiles use a grey profile head with the red cap. The brief asks for exactly this ("Doug's head outline"), and the cap makes it clear it's Doug.

**Gore / violence:** PASS. There's no anatomy, blood, scans or photos. The worms are smooth pink cartoon shapes, and the cysts in Pork Tapeworm are simple rings. The red speckle around the flowerpot reads as a glow, not blood.

**Kid appeal:** PASS. The worm-with-suitcase and worm-with-boots props are slightly whimsical. But they're tiny, and the overall look (dark ramp, worm-in-head diagrams, empty-pot boss) is adult-coded nature horror, not nursery.

**Matches title / honesty:** PASS. "Every" is delivered as a 9-item table of contents. "Brain" is carried by the worm-inside-head motif in rows 2-3 without repeating any title words. Every tile is an item that really appears in the video, so nothing is misleading.

**Non-blocking notes (no change required this round):**
1. Rows 2-3 have four near-identical head-profile tiles (Rat Lungworm, Pork Tapeworm, Spirometra, Gnathostoma). Each one is told apart only by its host prop (slug, ham, frog, fish). Accepted per decisions.md 2026-10-11.
2. Graphic designer: at 320x180 the Gnathostoma "boots" and the Spirometra "suitcase" turn into brown blobs. In Gnathostoma they sit right next to the eye dot and could read as marks on the face. Optional polish: shift `worm_boots` in the Gnathostoma tile about 10 px up and left (x 126 -> 116, y 86 -> 80) so it clears the eye. In the Spirometra tile, enlarge `worm_suitcase` from 0.4 to 0.5.
3. Graphic designer: the Lancet Liver Fluke ant costume is dark brown on gold and a little murky, but it still reads (Doug's cap and face stand out). If thumbnail A gets a refresh, lighten that tile's fill slightly (#ecd47c -> #f3e09a) to add contrast.
4. If CTR is weak after 7 days, swap in thumbnail_b.json as already planned in decisions.md.

THUMBNAIL: PASS
