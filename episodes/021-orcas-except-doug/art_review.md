# 021 Why Orcas Kill Everything Except Doug: art review (art director, 2026-10-17)

Scope: the 35 new library files from `asset_requests.md` (including the extra `dolphin_costume_swim`). I checked them against `assets/previews/021-orcas-except-doug-*.png`
(creatures a/b, the dark-water check, costumes alone and on Doug, props, maps), plus zoomed check renders of s048, s119,
s159, `se_alaska_map` with a centre ring, and the harbor seal next to `salmon` at icon scale. I also checked the JSON
bboxes, the costume x/y/scale/pose pairings in the shotlist, and `validate` (it is clean apart from the s001 `thumbnail`
scene_ref, which the graphic designer still owes).

## Verdict: FAIL (1 required fix, illustrator). 34 of 35 assets are APPROVED.
Only `harbor_seal` goes back to the illustrator. I made one fix myself (`shark_costume_flat`, see #24). Once fix 1 is
re-previewed, this becomes a PASS without a full re-review.

## Required fixes
1. **`harbor_seal` (illustrator):** the hind end is a symmetric forked fish tail with a single hanging pectoral-style
   flipper. At icon scale (0.4) it reads as a spotted copy of `salmon`, and this episode puts the two side by side on the
   MENU and in the map shots. Replace the tail with **two paired hind flippers held together and pointing back**: webbed,
   with 4-5 short digit lines each, slightly splayed at the tips, and no fork notch. Keep the anchor, bbox (~420 x 170),
   spots, head, eye and whiskers exactly as they are. The front flipper can stay but should get 3 short claw/digit
   strokes so it reads as a flipper, not a fin. Re-preview at scale 1 and 0.4 next to `salmon`.

## Creatures
| # | Asset | Verdict | Notes |
|---|---|---|---|
| 1 | `orca_fin` | APPROVE | Tall, straight, slightly back-swept, jet black with a mid-grey leading-edge highlight and a white ripple ring. It is clearly not `shark_fin`, and it reads on `#14365e`-class navy at icon size. |
| 2 | `orca_female` | APPROVE | Same pattern and same x bbox as `orca` (-460..445). Fin top at y -198 against -262 for `orca`, so the fin is about half height and falcate. Hard small eye, no smile, so it looks powerful rather than cute. Swaps 1:1. |
| 3 | `harbor_seal` | **FIX 1** | Spots, silver body, pale belly, dog-like head and whiskers are all good. The tail is the problem (fix 1). |
| 4 | `sea_otter` | APPROVE | On its back, stone on chest, hind feet up, cream face. The closed-eye "content" face is fine for an adult-coded channel because it is a single animal, not a nursery look. On dark navy the brown body is low contrast but the cream head carries it. |
| 5 | `pacific_white_sided_dolphin` | APPROVE | Suspender stripes, bicoloured fin and short beak are all present. It is distinct from `dolphin`. |
| 6 | `short_tail_stingray` | APPROVE | Disc, pale rim, eyes and spiracles at the front, short thick tail, pale serrated barb about half-way along it. Barb sits where the director's s111 arrows point. Not gory. |
| 7 | `deer` | APPROVE | No antlers, big ears, black tail top, pale throat. Optional (not blocking, one shot): the brow stroke over the eye makes it look slightly sly, so dropping it would be better. |
| 8 | `whale_shark` | APPROVE | Spots and checkerboard lines, wide flat terminal mouth, crescent tail. It looks calm. |
| 9 | `gray_whale` | APPROVE | Mottled slate with barnacle patches, dorsal knuckles, no fin. It also works as a silhouette (s206). |
| 10 | `humpback_whale` | APPROVE | The long white pectoral flipper is the key read and it holds at icon size. Head knobs are present. |
| 11 | `orca_skeleton` | APPROVE | Clean off-white museum bone on a dark plinth with two steel posts. Teeth are uncoloured notches, so it is not gory. |

## Costumes (checked alone and fitted on Doug)
| # | Asset | Verdict | Notes |
|---|---|---|---|
| 12 | `salmon_costume` | APPROVE | Kype hood frames the face from above, cap fully visible, works on float/wave/stand. The pink stripe is pink, not red, which is good. |
| 13 | `sea_otter_costume` | APPROVE | In context (s048/s049: Doug `on_back` at 900, costume `rotate -90` at 918 = x + 30 x 0.6) the face ring clears the cap and face, and the rock sits on the chest. |
| 14 | `otter_rock` | APPROVE | Flat top, and `doug_cap` sits on it cleanly (s050 death image). |
| 15 | `dolphin_costume` | APPROVE | Upright suit (float/stand/wave). The dorsal fin clears the cap. Used correctly in s098 (`float`). |
| 16 | `dolphin_costume_swim` | APPROVE | Native to the swim1/swim2 lean, no rotate. The head, face and cap are clear. See the s097 note below. |
| 17 | `stingray_costume` | APPROVE | Blanket over `on_back` Doug. Head, eyes and cap are clear on the left (s119). |
| 18 | `moose_costume` | APPROVE | The cap sits visible between the antlers and the dewlap is there. Hoof mitts on the suit sides are fine for `stand`. |
| 19 | `moose_costume_flat` | APPROVE | The antler outline reads on its own (Short #2 end card), and the cap gap works. |
| 20 | `whale_shark_costume` | APPROVE | Wide open-mouth hood frames the face, and Doug's open mouth matches. |
| 21 | `whale_shark_costume_flat` | APPROVE | Belly-up, X eyes and cap clear. |
| 22 | `gray_whale_calf_costume` | APPROVE | Blunt head hood, barnacles, flipper mitts on the float hands. |
| 23 | `blue_whale_costume` | APPROVE | Doug is fully hidden, the cap pokes out of the blowhole at (300,-192), and the zip seam and patch sell "homemade". |
| 24 | `shark_costume_flat` | APPROVE (AD fix) | The suit's mouth interior was danger red `#7a0d0d` with a tooth row, sitting right against dead Doug's neck in s159. At phone size that read as the shark biting his head or as blood at the neck on a death beat. **AD fix:** that poly's fill changed to grey felt `#4a4f57`, and the white felt teeth stay. Re-rendered s159: it now reads as an empty felt suit. The upright 008 `shark_costume` is unchanged. |

## Props and people
| # | Asset | Verdict | Notes |
|---|---|---|---|
| 25 | `surfboard` | APPROVE | |
| 26 | `surfboard_bitten` | APPROVE | Clean half-moon notch with no tooth marks and no red. |
| 27 | `whaleboat` | APPROVE | Clinker planks and a rope coil at the bow. There is no harpoon. Optional: the two oars on the thwarts read as a second gunwale rail at small scale, so a slightly darker oar shaft colour would help. |
| 28 | `rowboat` | APPROVE | Suits the thumbnail. The seat top is where Doug sits. |
| 29 | `whaler` | APPROVE | Crude tier with `auto_ink`. Flat cap, beard, waistcoat, no red cap. (In the sheet the cap is cut off by the cell edge only. The JSON top is y -296, which is fine.) |
| 30 | `whaler_old` | APPROVE | Grey beard and a stoop. The cane is a welcome extra. |
| 31 | `wildlife_official` | APPROVE | Peaked cap, mustache, khaki and a badge. The cap clipping is from the sheet cell only (JSON top is y -326). |

## Maps
| # | Asset | Verdict | Notes |
|---|---|---|---|
| 32 | `aleutian_map` | APPROVE | The chain runs lower-left to upper-right with the mainland at top right, matching the otter-icon placements. |
| 33 | `se_alaska_map` | APPROVE | At 1.2 with a ring at (0,0), the centre lands in open water between the mainland and Chichagof. Icy Strait is short, but the ring and fins read as "here, between islands". |
| 34 | `gulf_of_california_map` | APPROVE | Baja on the left, the gulf between. (60,150) lands in the southern gulf water. |
| 35 | `eden_bay_map` | APPROVE | Sepia paper, brown ink, hatched sea, compass rose. The Twofold Bay bite is at (120,40). |

## s097 asset swap (director to confirm)
Checked with `git diff` and grep. The sed changed exactly one line (shotlist line 19014) in s097: `dolphin_costume` →
`dolphin_costume_swim`, at the same x 620 / y 640 / scale 0.55 as the `swim1`/`swim2` Doug, with no `rotate`. The JSON
parses and `validate` passes. s098 correctly keeps `dolphin_costume` on the `float` pose. No other shot pairs a swim pose with
an upright costume (I checked every costume against its Doug pose). **Director:** please confirm this and commit it with your shotlist.

## Rulings on the director's flagged questions

### A. Background colours: APPROVED as the 021 episode ramp (now in the art bible)
The brief gave the ramp to the art director: "North Pacific grey-green, kelp green, open blue, colder southern blue, deep
navy, boss at dusk". The shotlist's colours deliver it, and I am adopting them as is:

| Item | Water | Sky / extra |
|---|---|---|
| Chinook Salmon | `#5d8a87` | `#cfd8d6` |
| Sea Otter (kelp) | `#4f8a7f` | `#d6e4e8` |
| Harbor Seal, Dolphin | `#3a9ad9` | `#cfe9ff` |
| Stingray (sand flats) | `#5cc6c9` | `#cfe9ff` |
| Moose (Icy Strait) | `#4a86a8` | `#cfe2ee` |
| Great White Shark | `#2f7fbf` | |
| Gray Whale Calf | `#2a6aa6` | |
| Whale Shark ("Giants.") | `#1f5a94` | |
| Law of the Tongue (Eden) | `#3f6f86` | sepia `#e9dcc0` |
| Blue Whale (boss) | `#14365e` | |
| Closing (dusk boat) | | `#e88a4a` over `#f2a24a` |
| Sombre text cards (1972 bite s066-s071, Hauraki s113-s114) | `#2f6f9f`, night `#1b2f5a` | |

Why this does not break the "surface water = `#3a9ad9`" rule: 021 has no depth axis. The axis is prey size, and the
colour shifts by region and item, the way 009 did with eras. None of these values is a depth-zone hex (`#1b4f86`,
`#0b2447`...), so the depth language is untouched. From Moose to the boss, luminance falls at every item (0.21 → 0.04),
so "Giants." feels darker and bigger. The bright Stingray turquoise is honest shallow sand flats. Conditions:
- Keep every shot of an item on its item colour, death beats included. Survival and death beats do not change colour.
- s088 (`#2f80b8`, inside the Dolphin item) is allowed only as a one-off sombre beat ("attacks are rarely seen"). Do not
  add more mid-item darkenings.
- On the boss `#14365e`, Doug must auto-ink white. Do not set `ink`.
- WordArt on the grey-green and kelp items (`#5d8a87`, `#4f8a7f`) uses the green-ground override (white→`#ffe24a`, outline
  `#1a1a1a`). s048 already does this, so keep it on every Salmon and Otter wordart.

### B. Orange "MAYBE" stamp: APPROVED as is (orange `#e07b00`, not red)
The brief and the script say "red MAYBE", but that wording is wrong. The art bible field-guide spec (from 010) is: **"NO"
in red `#e0201b` after a death, "MAYBE" in orange `#e07b00` after a survival**. Red is reserved for the death verdict, and
making MAYBE red would muddle that grammar. I checked the closing shot against the spec at `field_guide_open` scale 1.15:
the stamp centre is (900 + 140 x 1.15, 560 + 50 x 1.15) = (1061, 617.5), size 64 x 1.15 = 73.6, outline 3 x 1.15 = 3.45.
The name "ORCA" is at (739, 433.5), size 32 x 1.15 = 36.8. All of these match exactly. No change needed. I am telling the
creative director so the brief/script wording does not get "fixed" later.

## Routing
- Illustrator: fix 1 (`harbor_seal`). Optional: deer brow, whaleboat oar shade.
- Director: confirm the s097 swap. Keep the Salmon/Otter wordart override and the item-colour discipline above.
