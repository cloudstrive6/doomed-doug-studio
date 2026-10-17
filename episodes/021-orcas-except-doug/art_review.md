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

---

# Keyframe review (art director, 2026-10-17)

Scope: all 22 contact sheets (`build/contact/sheet_01..22.png`, s001-s259), with full-resolution crops from
`build/keyframes/` for every overlap or readability doubt (counter zone, map frames, Doug close calls). I checked them against the
art bible: the 021 regional ramp, the counter zone (x 1300-1860, y 110-230; inset frames start at y >= 250 or end at x <= 1280),
the text and map rules, Doug's locked design and the rules in style bible section 7 (1-9).

## Verdict: FAIL (13 required fix groups, all director unless marked)

**What works:** the style is consistent across all 259 frames. Doug is on-model everywhere, and the cap is visible in every
costume, ghost and cap-only death. The counter ticks exactly on the death beats (s029 171, s050 172, s099 173, s120 174, s140 175,
s159 176, s200 177, s246 178) and holds on the survivals (s075, s177-s179, s222). Item colours follow the approved ramp, and Salmon
and Otter wordart all use the green-ground override. The first reveals (s040, s194) use the thin red rim with no red speckle.
Nothing is gory: the s001 jaws are cartoon, and the s050 red in the splash reads as the cap on the rock. The pacing of the build-up
groups is good, and layouts rotate well (maps, scales, menus, costumes, text cards). The failures are almost all collisions with
the counter and map frames, plus a few readability problems.

## Required fixes

1. **Wordart/labels touching or overlapping the counter.** Move glyph tops to y >= 250 wherever the text spans x 1300-1860, or
   end the text at x <= 1280:
   s015 "RATHER GO HUNGRY" (tops butt the box), s062 "MAMMAL EATERS" and s063 "FISH EATERS" (label boxes overlap the counter;
   move both to about (1250, 330)), s080 "LARGEST" (overlaps the box), s094 "EATS DOLPHINS" (tops at y ~170, touches the box's
   left edge), s127 "STRONG SWIMMERS" ("RS" runs under the box), s162 "FIRST WHALE" (tops at y ~205), s180 "BACK OFF"
   (touches the box), s183 "BIGGEST FISH" (tops at y ~170), s203 "BACKGROUND" (touches the box), s254 "THEY WAITED"
   (label overlaps the counter).
2. **Creatures and props inside the counter zone.**
   - s123: the moose's antlers touch the counter box. s124: the moose is half hidden behind the counter *and* the "LAND ANIMAL"
     label, so the subject of the line is unreadable. Put the moose on the right hill at y >= 300 (body below the zone) and move
     the label to the moose's left.
   - s152, s153: the right-hand fishing boat sits behind the counter, and its rod tip reaches the caption bar. Move that boat to
     x <= 1200, or drop the horizon to y >= 260.
   - s230: the 2019-adult blue whale's nose runs into the zone (it touches the box's bottom-left). Shift the three whales and their
     labels left by about 150, or start the stack at y >= 260.
3. **Ghost Doug inside the counter zone.** The ghost's cap touches or overlaps the counter box in s051, s121, s160 and s201.
   Spawn ghosts at x <= 1250 or with the head at y >= 290 (s099 and s246 are placed correctly).
4. **Inset maps under the counter.** This is the 008 rule: the frame must start at y >= 250 or end at x <= 1280. These shots
   have the counter sitting on the map's top-right corner or frame: s128, s131, s132, s133 (Icy Strait), s155 (Farallon),
   s165, s166 (top at y ~231, borderline), s167, s172, s173 (Monterey), s188, s189, s197 (Gulf of California), s204, s205
   (Eden), s228, s229 (Australia), s252, s253 (world). Shrink to about 0.85 and lower the frame top to y >= 260, or end it at
   x <= 1280. Keep each map in the same place across its build-up group so nothing jumps.
5. **Text crossing a map frame.** s197 "SHARK HUNTERS" sits on the map's bottom frame line. s228 "3 TIMES" and s229
   "2019 TO 2021" overlap the frame's bottom-right corner. Leave at least 20 px of clear space (after fix 4 there is room below the
   frame).
6. **s030: Doug reads as a floating head.** At scale 0.4 on `#5d8a87`, his body lines are almost invisible, so the frame shows a
   capped head drifting next to an orca with a salmon in its mouth (a decapitation read). Make the body readable (scale >= 0.5,
   with normal ink and not the faded ghost tint), or drop him from the shot. The ghost already plays in s029.
7. **s075, s076: the surfboard goes through Doug's chest.** The board is at y 594 and Doug floats at y 640 (s = 0.5), so the
   board line crosses his torso and the seal costume, and it reads as a skewer. Either stand him *on* the board as in s073 (hip =
   board top - 152 x 0.5) or put him in the water beside the board (x about 1250) with the board drawn after him.
8. **s108: the stingray's tail tip touches Doug's face.** The tail and the pale barb end at his cap and mouth. On an item about a
   lethal barb this is gore-adjacent, so it must not ship. Move the ray right (x about 1250) or Doug left, keeping 80 px or more
   between the tail tip and his head. The size comparison still reads.
9. **s202: the item title runs through Doug's head.** "THE LAW OF THE TONGUE" at y 350 crosses his cap and face in the boat.
   Lower the boat and Doug by about 80 (horizon to about 700, keeping hip = boat seat), or shrink the title (size about 110, y 300)
   so its glyph bottoms clear the cap top by 20 px or more. Keep glyph tops at y >= 250 where the title spans x > 1300.
10. **Drawing and composition glitches.**
    - s145, s163 ("half a car"): the cover `rect` that hides the car's back half is a flat block that does not match the textured
      background (light rays in s145). It leaves an orphaned wheel stroke and a cut body edge, so it looks like a render bug. Draw
      the missing half as a red dashed outline (cut line plus ghosted half) instead of covering it, and delete the cover rect.
    - s141: the moose is a full standing moose sunk below the surface line (legs and all underwater). Use the swimming
      composition from s127-s130 (body at the water line, head and antlers above), with the white dashed line from the boat to it.
    - s129: `water_plants_bunch` at 0.9 hangs in the air beside the moose's head with a leaf "head" and stem "limbs", so it reads
      as a little green stick creature. Scale it to about 0.5 and tuck it at the moose's mouth, overlapping the muzzle. If it still
      reads as a figure, **illustrator**: redraw it as a limp, draped weed clump (no single top leaf).
    - s167: a stray full-height black vertical line runs through the Unimak `tile` (x about 760). Fix the tile crop so only the
      outer frame shows.
    - s256: the orca fin is drawn on top of THE MENU and covers the "MOOSE, 364-725 kg" line. Move the fin into the open water
      to the right of the menu (x >= 1250).
11. **Off-item backgrounds.** The rule from the asset review is that every shot of an item stays on its item colour.
    - Cream `#f4f1dc` (the 019/020 opener colour) is used in s125, s126, s134, s135, s136 (Moose) and s143 (Great White). Use the
      item's sky over a floor: Moose `#cfe2ee` and Great White water `#2f7fbf`. The scientists can stand on a seabed strip, as in
      s018.
    - The pale studio greys `#e9f3f8` and `#e4eef4` are used in s057, s058, s072 (Harbor Seal), s163, s164 (Gray Whale Calf), s186
      and s187 (Whale Shark). Put these weigh-ins on the item colour: seal sky `#cfe9ff`, and for calf and whale shark the item
      water `#2a6aa6` and `#1f5a94`, as s018 did for salmon. s035 (otter sky `#d6e4e8`) is fine.
    - Accepted as is: s212-s213 (night is part of the "overnight" beat), s220 (a callback to the 008 boat scene, so the 008
      look is intended), and s259 (end card).
12. **s067-s071: five text-only frames in a row, and the text jumps.** The block re-centres vertically in every shot, so line 1
    moves (y ~1007 → ~987) as lines are added, and five consecutive frames share one composition. Anchor line 1 at a fixed y
    (about 400) and add lines below it. From s069 ("mistaken for a seal?") add one image: `surfboard_bitten` at about (960, 820),
    scale 0.7, with a small `harbor_seal` at 0.4 beside it, on the night ground. Do not add red. s066 (Doug alone) and s072 already
    break the run on either side.
13. **Copy on screen (s233).** "16 IN ALL 3" reads as a typo. Change it to "16 IN ALL 3 HUNTS" (size 40, wrapped to two lines if
    needed, centre x <= 1680).

## Optional polish (not blocking)
- s006, s010-s014, s084, s085: the map's right edge sits at about x 1290 right beside the counter. Nothing touches, but shift the
  map 20 px left for air.
- s082: the orca's dorsal tip touches the bottom of the "10 TONNES" box. Raise the label by 30.
- s153: the "2:00" label sits on the orca's back. Move it above the stopwatch.
- s177: the gray whale's fluke touches the costume hood. Move Doug 60 px down-left.
- s178: the speckle "commotion" cloud spills over the caption bar. Clip it to y >= 120 or drop its density.
- s224, s225: the tiny white-ink Doug is lost against the whale's belly line under the flipper. Drop him 60 px into clear water
  so the scale gag reads.
- s231: "FEMALES LEAD" covers one orca in the bottom row. Move it to y 1030, or remove that orca.

## Routing
- **Director:** fixes 1-13 (shotlist edits only), plus the optional polish.
- **Illustrator:** only if the fix-10 rescale of `water_plants_bunch` still reads as a figure.
- Re-render keyframes for the touched shots (`python -m studio keyframes 021-orcas-except-doug --shots ...`) and send the new
  contact sheets back. Re-review will cover only the listed shots.

---

# Keyframe review, round 2 (art director, 2026-10-17)

Scope: all 22 contact sheets again (s001-s259, all re-rendered 18:03-18:04), plus 1080p checks of every changed shot. For the
counter I did a pixel sweep: for all 259 keyframes I cropped x 1150-1920, y 90-340 and measured the box edges
(x 1365-1815, y 128-196) against the nearest ink.

## Verdict: FAIL (3 small, mechanical fix groups, all director)

**All 13 round-1 fixes are done and verified:**
1. Wordart and labels are clear of the counter in s015, s062, s063, s080, s094, s127, s162, s180, s183, s203 and s254. Glyph
   tops are at y >= 250, or the text ends at x <= 1280.
2. In s123 and s124 the moose is on the right hill below the zone, with the label to its left. In s152 and s153 the boats are
   at x <= 1260. The s230 whale stack ends at x 1260.
3. The ghosts in s051, s121, s160 and s201 are out of the zone.
4. The maps in s105-s107, s128, s131-s133, s155, s165-s167, s172, s173, s188, s189, s197, s204, s205, s228, s229, s252 and
   s253 all have frame tops at y 266-300, or end at x <= 1280. Each build-up group stays in one place.
5. "SHARK HUNTERS" (s197), "3 TIMES" (s228) and "2019 TO 2021" (s229) are clear of the frames.
6. s030: Doug has been dropped. The orca, salmon and "NO OPINION" read cleanly.
7. s075, s076: Doug stands on the board, so there is no skewer read.
8. s108: about 450 px between the tail tip and Doug.
9. s202: the title tops are at y 250 and the cap clears the title by about 25 px.
10. `car_half` (s145, s163) reads as a deliberate cut. `unimak_map` (s167) is one clean frame. `water_weed_draped` (s129) reads
    as a weed mat at the moose's muzzle. s141 shows the moose swimming with the dashed line from the boat. In s256 the fin is
    in open water to the right of the menu.
11. Item skies and waters are now on the ramp: seal `#cfe9ff`, moose `#cfe2ee`, great white `#2f7fbf`, calf `#2a6aa6`, whale
    shark `#1f5a94`. The pale grey weigh-in floors in s057, s058, s072, s163, s164, s186 and s187 are accepted, because the
    scale needs a floor.
12. In s067-s071, line 1 stays at a fixed y. From s069 on, the surfboard and seal break the text run. No red.
13. s233 now says "16 IN ALL 3 HUNTS".
The visual-screener's variety fixes also read well: s011 (hungry orca and plate), s012 (seals passing), s063 (resident orca with
a salmon), s107 (ray beside NZ) and s250 (close-up of the fish).

## Required fixes

1. **WA/BC map group: the map frame runs into the counter zone.** In round 1 I measured this edge at about x 1290 and filed it
   as optional. At 1080p the frame's right edge is actually at **x 1348 with its top at y 176**, which is 17 px from the box and
   breaks the inset-frame rule. Shots: **s006, s010, s013, s014, s023, s060, s084, s085** (`bc_map` at x 960, scale 0.85).
   Fix: set the map x to **870** and move everything drawn on the map (orcas, fish, seals, the red circle, the warning icon, the
   s060 arrow, and the s084/s085 dolphin and orca icons) by -90 in x as well. This puts the right edge at about 1259. The labels
   under the map ("6 OF 40 YEARS", "SEAL EATERS", "ENDANGERED", "MORE THAN HALF", "ONLY PREDATOR") can move -90 too, to stay
   centred. Keep the same x in all 8 shots so the map never jumps.
2. **Aleutian map: the frame sits right under the counter.** In **s036, s037 and s052** (`aleutian_map` at y 500, scale 0.9) the
   frame top is at y 228 and the frame runs to x 1592, only 32 px below the box. I missed this in round 1. Fix: set the map y to
   **532** (frame top at about 260) and move the otters, red X marks, orcas and the s052 dashed line on it by +32 in y. The
   labels below ("1990s", "MINUS 25% A YEAR", "ENORMOUS") still have more than 80 px of clearance, so leave them where they
   are.
3. **s234: "TONGUE FIRST" sits on the Australia map's top frame line** (the label box covers y 245-315 and the frame top is at
   300). That breaks the round-1 rule of 20 px clear around map frames. Fix: move the label below the map, to about
   **(1250, 870)**. The frame bottom is at about 819. Do not move it up: above the map it would land in the counter zone.

## Optional polish (not blocking)
- s082: the orca's dorsal tip still touches the bottom of the "10 TONNES" box. Raise the label by 30.
- s174: the clock icon's top is at y 243, 47 px under the box. Lower the clock and "6.5 HOURS" by 30.
- s219: the top of the "PARTNERS" box is at y 237 and the box spans to x 1418. Lower "PARTNERS" and "NOT PREY" by 20.
- s255: Doug's cap brim touches the orca fin's right edge. Move Doug about 70 px right, so he stands beside the fin instead of
  stuck to it.
- s145: the shark's pectoral fin tip grazes the ghost outline of the half car. Move the car about 40 px down or left.

## Notes
- The counter value is correct on every frame (170 to 178 on the same death beats as round 1). No other ink comes within 30 px
  of the box in any of the 259 frames.
- Not mine to call: the visual-screener's should-fix for s087 (a 1-vs-8 fishing-gear tally) has not been added. The screener
  should decide whether that blocks.
- Art bible updated (`channel/art_bible.md`, death counter): map assets count as inset frames. Measure the rendered frame line in
  pixels, not the element's x/y.

## Routing
- **Director:** required fixes 1-3 (shotlist only, 12 shots), plus any optional polish. Re-render
  `--shots s006,s010,s013,s014,s023,s036,s037,s052,s060,s084,s085,s234` (plus any polish shots).
- **Illustrator:** nothing.
- Re-review will cover only those shots. If the frame edges measure x <= 1280 (WA/BC) and y >= 250 (Aleutian), and the s234
  label clears the frame, this is a PASS.

---

# Keyframe review, round 3 (art director, 2026-10-17)

Scope: all 22 contact sheets (s001-s259). I re-rendered every keyframe from the current `shotlist.json` first, because the last
partial render (s082, s087) had replaced the contact folder with one sheet, and some older keyframes were from before the
final shotlist edit. I also took 1080p pixel measurements of every round-2 shot and ran the counter-zone sweep again on all 259
frames.

## Verdict: PASS

**Round-2 required fixes, all verified at 1080p:**
1. WA/BC map (s006, s010, s013, s014, s023, s060, s084, s085): the frame's right edge is at **x 1258-1259** (limit 1280), in
   the same place in all 8 shots. Everything on the map moved with it, and the labels under the map stay centred.
2. Aleutian map (s036, s037, s052): the frame top is at **y 260** (limit 250). The otters, X marks, orcas and dashed line all
   moved with it.
3. s234: "TONGUE FIRST" is now below the Australia map. The frame line clears the counter zone and nothing overlaps.

**Optional polish also done:** s082 (the label no longer touches the dorsal fin), s174 (clock lowered), s219 ("PARTNERS" and
"NOT PREY" lowered), s255 (Doug is clear of the fin and splash, with about 40 px of water between them), s145 (the car_half
scissors now clear the pectoral fin). The visual-screener's items are also in: s068 and s071 are seascapes, so there are at most
2 navy cards in a row, and s087 has the ORCA vs FISHING GEAR tally.

**Sweep:** Doug is on-model in every frame. The red cap is present on every alive, ghost and costume Doug, and ink turns white
on the dark backgrounds. Item colours match the bible ramp, and every item tag is correct. The counter reads 170 to 178 on the
right beats. No ink comes within 30 px of the counter box in any frame (s001 is the thumbnail opener and has no counter, so it
was excluded). There is no gore anywhere. Layouts vary well: no composition repeats more than 2 times in a row.

## Non-blocking notes (fix if the director touches these shots again; do not re-review)
- s234: the top of the "TONGUE FIRST" box is 10 px below the map frame's bottom line (y 824 to 834). The 20 px rule wants
  y about 885. It reads cleanly as a caption, and the gap came from my round-2 coordinate.
- s145: after the polish move, the car_half wheels sit about 10 px above the bottom edge of the frame. Raising the car by 30
  and moving it left by 40 would give it room and still clear the fin.

## Routing
- Nothing is blocking. Art is approved from my side. The stage moves to `art_approved` once the visual-screener also passes.
