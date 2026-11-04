# 037 Sperm Whale Dive: Visual Review

## Round 3: revised thumbnails (2026-11-04)

Checked build/thumbnail.png, thumbnail_b.png, thumbnail_c.png at 1280x720, their _small versions at 168x94,
build/smalls.png (side by side) and build/c_small_x3.png. Title: "Why the Sperm Whale Gets Deadlier the Deeper Doug Follows It".
Keyframes already passed in Round 2 (all 13 items fixed; s004 Doug scale is advisory only) and were not re-checked here.

VERDICT: FAIL (A PASS, B PASS, C FAIL on one tile)

- **A, thumbnail.png (2 KM DOWN)**: PASS. The background is now near-black navy, so it reads as deep water, and the warm beam
  lands on a lit patch on the head. There is one focal point (the scarred head over two-thirds of the frame). Doug is on-model
  (red cap, white head, goggles, tank) and his light reads at 168 px. The text is the biggest element and is legible at feed size.
  Cartoon teeth, no gore, nothing cutesy. It pays off "deeper" and doesn't mislead.
- **B, thumbnail_b.png (IT HEARD YOU)**: PASS. IT HEARD YOU now parses at 168 px. The water is dark, Doug is lit by his short beam
  and sits clearly between the open jaw and the head, and the stray blob on the left is gone (the left edge is now plainly the head
  with its eye). One focal point (the jaw), no blood, adult horror tone. Doug is on-model.
- **C, thumbnail_c.png (2x3 chapter grid)**: FAIL. The CD's structure is met: six tiles, one-word chapter labels in escalation
  order (HEAD, CLICK, JAW, SCARS, CABLE, DEEP), the head hits the bow with an impact star, and the squid is reused on SCARS.
  **The labels read at 168x94.** Each is about 9-10 px tall, black on a white bar, and all six words are legible in the _small and
  in c_small_x3. Doug is on-model in every tile. The one failure is the DEEP tile, which is the payoff tile for the title: the
  whale is a thick red outline in a cloud of red spray dots on black. At feed size it reads as a red smear, or a blood cloud, rather
  than a whale silhouette in the dark. The outline's shape (flat top, notched tail) is not recognisable as a sperm whale, and it
  is horizontal, so there is no "diving deeper" cue. The red-spray gore read is the policy-risk part, since the click and jaw
  tiles already say "danger".

### Required fixes

1. **thumbnail_c, DEEP tile (graphic designer)**: remove the red spray-dot cloud completely and drop the red outline. Draw the
   `sperm_whale` asset as a dark silhouette (about #1b2436 fill) with a thin pale rim light (about #9fb3c8, 3-4 px), rotated about
   30-40 degrees nose-down so it is diving toward the bottom-right corner. Keep its square head inside Doug's beam so the beam
   lands on the blunt head (the same lit-patch treatment as A). Keep the tile black and keep Doug and his torch where they are.
   Re-export thumbnail_c_small.png and smalls.png and re-check that the whale shape reads at 168x94.

### Advisory (not blocking)

2. **thumbnail_c, CABLE tile (graphic designer)**: the yellow cable ends in Doug's hand, so it reads as Doug lassoing the whale
   rather than the whale being snagged. End the cable off the tile edge, or at a seabed splice box, instead of at Doug.
3. **s004 (director)**: carried over from Round 2. Scale Doug up (about 0.3).

Order once fixed: A is primary, with B and C as test variants (per the CD).

## Rounds 1-2: keyframes (2026-11-04)

Keyframes: PASS as of Round 2. All Round 1 items (s001, s159, s024, s043, s044-s047, s166-s168, s208, s006, s161, s138,
field guide s031/s054/s078/s124/s174/s200, s216) were fixed. s004 Doug scale and the field-guide MAYBE continuity are advisory only.
No gore and no kids-show framing. Doug is on-model and the HUD and death counter are consistent.
