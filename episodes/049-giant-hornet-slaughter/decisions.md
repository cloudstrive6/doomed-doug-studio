# 049 decisions

## 2026-11-16, creative director: episode chosen, brief written
- 049 = backlog #112, giant hornets (8.0). This confirms CD decision 3 in `data/insights/2026-11-15.md`. It deliberately overrides the playlist default:
  047 and 048 are both `animals`, and the default pick, #55 plants (6.3), has no engine. #111 great white vs orcas (8.7 in `topics`) is held so that
  it comes at least 3 slots after 048.
- Axis: size of the target (BEE, HIVE, DOUG, NORTH AMERICA). It is not a distance axis, because 043 and 048 both used distance.
- Title numbers (30 / 30,000 / afternoon) are provisional until they are sourced. The title changes to match the sources.
- 050 must leave `animals`.

## 2026-11-16, creative director: script approved (draft 2 + screener round-2 fixes)
- Verified fix 1 (line 9): "Later, Doug holds open a tree that could have produced nearly two hundred hornet queens." 15 words; "The Hunter." still at spoken words 34-35.
- Verified fix 2 (line 167): "But here's what the scary reputation leaves out." No remaining "nickname" reference; marker unique.
- Advisories (line 239 "straight", line 55 corner-shop analogy) left to the director/editor's discretion; not blocking.
- Stage -> script_approved after 3 screening rounds. Deaths 369-374 go into the series bible when the episode ships.

## 2026-11-16, director: shotlist
- 202 shots (s001 thumbnail ref, 2,013 spoken words matching the approved script exactly), 9 chapters, Doug in 82% of shots.
  Generator: `episodes/049-giant-hornet-slaughter/build/gen_shotlist.py` (build/ is git-ignored; regenerate from it before editing by hand).
- HUD: counter at (1590,162) plus THE TARGET (`the_target` icon at 0.2 + size-28 label "TARGET: ..." at (1590,238)). BEE from s002,
  HIVE from "One hive." (s047), DOUG from "One person." (s113), NORTH AMERICA from "One continent." (s154), stamped red-on-pink from death 374 (s193).
- Item palette (severity, light to dark): Hunter day meadow `#cfe9ff`/`#7cc25a`, Mark `#8fd3ff`/`#6fb24f`, Slaughter afternoon `#f6c45a`/`#b8913a`,
  Occupation dusk `#e88a4a`/`#9a7a4a`, Heat Ball `#8a6a8a`/`#5a4b3d`, Sting overcast forest `#b9c4a8`/`#5d6b45`, Toll sober cards `#15181a`,
  Hitchhiker night `#1b2f5a`/`#2b3d33`, Nest pre-dawn `#0b1020`/`#141e1a`. Diagram cards cream `#f4f1dc`; hornet nest interior `#d8cfbd`; hive interior `#e9b64a`.
- **One-off `cap_off` (logged per art bible):** The Toll s150-s153, Doug holds his cap in both hands (script stage direction); `doug_cap` is
  drawn at his hands, so exactly one cap is on screen. Sober item: no death, no joke, counter stays 372.
- Deaths: 369 meat ball bundle with the cap (no body); 370 `bee_costume_flat` + cap among X-eyed bees; 371 `hornet_costume_flat` + cap + steam;
  372 `on_back` dead + `beekeeper_suit_on_back`; 373 `on_back` dead behind the NO HORNETS sign; 374 empty hollow + vacuum hose + ghost.
- Shorts: short01 Heat Ball s093-s107 (ends on the 4-degree margin), short02 Nest s175-s187 with hook (ends on "nearly two hundred queens"),
  short03 Slaughter s049-s059 (ends "killed one by one"). Titles/descriptions left to the titler.
