"""Writes staging.json, cast_looks.json and voices.json for w01 (the director's blocking, in code so it is easy to tweak).
Run: py build_staging.py"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

LOOKS = {
    "tanner": {"skin": "#e8b48c", "hair": ["quiff", "#f0c75a"], "top": ["jacket", "#8a4fd6"], "bottom": "#22222c",
               "shoes": "#f4f1ea", "extras": ["sunglasses"], "_role": "rival"},
    "wren": {"skin": "#7a4a30", "hair": ["bun", "#1a1210"], "top": ["tee", "#3fa37a"], "bottom": "#3c3a48",
             "shoes": "#d6d2c8", "extras": ["apron"], "head_r": 62},
    "hobbs": {"skin": "#f0c8a4", "hair": ["bob", "#a2a2aa"], "top": ["uniform", "#2b3b5c"], "bottom": "#2b3b5c",
              "shoes": "#1e1d26", "extras": ["officer_cap", "badge"], "build": 1.15, "head_r": 64},
}

VOICES = {
    "narrator": {"name": "en-US-Chirp3-HD-Charon", "language": "en-US", "speaking_rate": 1.06},
    "doug": {"name": "en-US-Chirp3-HD-Puck", "language": "en-US", "speaking_rate": 1.08},
    "tanner": {"name": "en-US-Chirp3-HD-Fenrir", "language": "en-US", "speaking_rate": 1.12},
    "wren": {"name": "en-US-Chirp3-HD-Kore", "language": "en-US", "speaking_rate": 1.08},
    "hobbs": {"name": "en-US-Chirp3-HD-Gacrux", "language": "en-US", "speaking_rate": 0.98},
    "_pronunciations": [{"phrase": "Adeyemi", "ipa": "ɑˈdɛjɛmi"}],
}

ALIASES = {"backyard_pool_storm": "backyard_storm", "ocean_title": "underwater_mid", "backyard_pool": "backyard",
           "doug_kitchen": "kitchen", "bait_shop": "bait_shop", "lagoon_nursery": "lagoon", "harbour_dock": "harbor_dusk",
           "reef_edge_night": "reef_night", "open_sea_night": "sea_night", "beach_dawn": "beach_dawn",
           "honesty_studio": "studio", "yard_night": "backyard_night", "street": "street"}

NAME_CARDS = {
    "tanner": {"name": "Tanner Sloane", "tag": "Neighbour. 41,000 followers. Met four."},
    "wren": {"name": "Wren Adeyemi", "tag": "Bait shop. Marine biology student."},
    "hobbs": {"name": "Officer Marlene Hobbs", "tag": "Fisheries. Has a form for everything."},
}

# pool geometry (backyard set): surface y 850, centre y 935; characters stand behind it on y 790
POOL = dict(y=945, water=850)


def meg(x, scale, **kw):
    d = {"x": x, "y": kw.pop("y", POOL["y"]), "scale": scale, "pup": kw.pop("pup", 1.0), "facing": kw.pop("facing", -1),
         "mood": kw.pop("mood", "happy"), "swim": kw.pop("swim", 0.6)}
    if kw.pop("behind", False):
        d["depth"] = 700
    if kw.pop("pool", True):
        d["water"] = POOL["water"]
    d.update(kw)
    return d


def ch(x, facing=1, **kw):
    d = {"x": x, "facing": facing}
    d.update(kw)
    return d


S = {}

# 01 storm night, pool. Doug with a torch, Tanner over the fence with the ring light.
S["01"] = {"set": "backyard_pool_storm", "wide_zoom": 1.1,
           "chars": {"doug": ch(620, 1, holds="torch", extras_add=["stripes"]),
                     "tanner": ch(1600, -1, holds="phone_ring", idle=["stand"])},
           "meg": meg(1050, 1.15),
           "lines": {"0": {"shots": ["pt:1000,820,1.5", "meg"], "fx": ["shake"], "hide": ["tanner"]},
                     "1": {"shots": ["meg", "close:doug"], "hide": ["tanner"]},
                     "2": {"hide": ["tanner"], "meg": {"mood": "happy"}},
                     "3": {"shots": ["close:tanner", "wide"], "fx": ["flash"]},
                     "5": {"pose": {"doug": "point"}},
                     "7": {"holds": {"doug": "tin"}, "shots": ["close:doug", "meg"], "meg": {"mood": "guilty"}}}}

# 02 flash forwards and the title drop
S["F1"] = {"set": "harbour_dock", "chars": {"tanner": ch(820, 1, holds="phone_ring", emo="smug")},
           "props": [{"id": "buyer", "x": 1150, "y": 640, "scale": 1.0, "facing": -1}]}
S["F2"] = {"set": "open_sea_night", "chars": {"tanner": ch(760, 1, y=1000, water=790, pose=["tread1", "tread2"], emo="scared")},
           "meg": meg(1450, 2.2, y=880, pool=False, water=800, pup=0.3, mood="hungry", col="#3c5068", facing=-1)}
S["F3"] = {"set": "street", "chars": {"tanner": ch(1150, -1, holds="phone_ring", emo="smug")},
           "props": [{"id": "ute", "x": 980, "y": 930, "scale": 1.1, "front": True}]}
S["F4"] = {"set": "ocean_title", "chars": {},
           "props": [{"id": "great_white", "x": 1250, "y": 560, "scale": 1.6, "facing": -1}],
           "meg": meg(560, 0.95, y=640, pool=False, pup=0.8, mood="curious", facing=1)}
S["02"] = {"set": "ocean_title", "chars": {},
           "meg": meg(900, 2.6, y=560, pool=False, pup=0.0, mood="calm", col="#2c3e58", facing=1, swim=0.9),
           "lines": {"0": {"shots": ["11|meg", "13|close:hobbs"], "holds": {"hobbs": "net"}},
                     "1": {"shots": ["F1|wide"]},
                     "2": {"shots": ["F2|wide", "F2|meg"], "fx": ["dark"]},
                     "3": {"shots": ["F2|close:tanner", "F2|meg"]},
                     "4": {"shots": ["meg"], "title": "WHAT IF A BABY MEGALODON|LIVED IN YOUR POOL?", "noword": True,
                           "move": {"meg": [1250, 520]}}}}

S["03"] = {"set": "backyard_pool",
           "chars": {"doug": ch(640, 1), "wren": ch(1420, -1, emo="deadpan", idle=["arms_cross"])},
           "meg": meg(1000, 1.15),
           "lines": {"0": {"shots": ["close:wren", "wide"]},
                     "5": {"meg": {"jaw": 0.9, "mood": "calm"}, "shots": ["meg"]},
                     "6": {"meg": {"jaw": 1.0}, "shots": ["meg"]},
                     "7": {"meg": {"mood": "happy"}}}}

S["04"] = {"set": "backyard_pool",
           "chars": {"doug": ch(700, 1), "wren": ch(1350, -1, emo="deadpan")},
           "meg": meg(1020, 1.15, mood="sleepy", swim=0.15, y=965),
           "lines": {"3": {"shots": ["meg", "wide"]}}}

S["05"] = {"set": "backyard_pool",
           "chars": {"doug": ch(300, 1, holds="bucket"), "wren": ch(180, 1, holds="bucket"),
                     "tanner": ch(1650, -1, pose="sit", holds="phone_ring", y=800)},
           "props": [{"id": "deckchair", "x": 1650, "y": 800, "scale": 1.1, "facing": -1}],
           "meg": meg(1050, 1.2),
           "lines": {"0": {"shots": ["wide", "medium:doug"], "pose": {"doug": ["walk1", "walk2", "walk3", "walk4"],
                                                                      "wren": ["walk1", "walk2", "walk3", "walk4"]},
                           "move": {"doug": [760], "wren": [600]}},
                     "1": {"pose": {"doug": "worry"}}}}

S["06"] = {"set": "backyard_pool",
           "chars": {"doug": ch(700, 1), "wren": ch(1400, -1, emo="deadpan")},
           "meg": meg(1000, 1.2, mood="sleepy", swim=0.05),
           "lines": {"0": {"shots": ["meg", "meg"], "move": {"meg": [1000, 990]}},
                     "1": {"fx": ["speedlines"]},
                     "5": {"shots": ["wide", "medium:doug"], "holds": {"doug": "fish_rod"},
                           "pose": {"doug": ["walk1", "walk2", "walk3", "walk4"]}, "move": {"doug": [1300], "meg": [1350]},
                           "meg": {"mood": "curious", "swim": 0.9}},
                     "6": {"holds": {"doug": "fish_rod"}, "meg": {"mood": "happy", "swim": 0.9}}}}

S["07"] = {"set": "yard_night",
           "chars": {"doug": ch(1150, 1), "wren": ch(1600, -1, emo="deadpan")},
           "props": [{"id": "sand_pile", "x": 1300, "y": 900, "scale": 1.1, "front": True}],
           "meg": meg(700, 1.15, facing=1, mood="curious"),
           "lines": {"3": {"shots": ["meg", "close:doug"], "move": {"meg": [1150]}, "meg": {"mood": "happy"}},
                     "5": {"shots": ["megclose", "close:doug"], "meg": {"x": 1150}},
                     "6": {"meg": {"x": 1150}, "holds": {"doug": "fish"}},
                     "7": {"meg": {"x": 1150, "mood": "happy"}, "holds": {"doug": "fish"}},
                     "8": {"meg": {"x": 1150}}}}

S["08"] = {"set": "doug_kitchen",
           "chars": {"doug": ch(760, 1), "wren": ch(1060, -1, emo="deadpan"), "tanner": ch(330, 1, holds="contract")},
           "props": [{"id": "fridge", "x": 1500, "y": 900, "scale": 1.0}, {"id": "receipts", "x": 560, "y": 470, "scale": 0.6}],
           "lines": {str(i): {"hide": ["tanner"]} for i in range(7)}}
S["08"]["lines"]["0"]["shots"] = ["pt:1500,620,1.5", "wide"]
S["08"]["lines"]["10"] = {"holds": {"doug": "crayon"}, "shots": ["close:doug", "close:tanner"]}

S["09"] = {"set": "backyard_pool",
           "chars": {"doug": ch(450, 1, emo="worried", idle=["worry"]), "tanner": ch(1350, -1, holds="melon_stick")},
           "meg": meg(900, 1.2, facing=1),
           "lines": {"1": {"shots": ["close:tanner", "megclose"], "meg": {"chomp": True, "mood": "hungry"}, "fx": ["shake"]},
                     "2": {"holds": {"tanner": "handle"}, "shots": ["megclose", "close:tanner"], "word": "CRUNCH",
                           "meg": {"chomp": True, "mood": "hungry"}, "fx": ["flash"]},
                     "3": {"holds": {"tanner": "handle"}},
                     "4": {"holds": {"tanner": "handle"}, "meg": {"mood": "guilty"}}}}

S["10"] = {"set": "backyard_pool",
           "chars": {"doug": ch(620, 1, holds="basket"), "wren": ch(940, -1, emo="deadpan"),
                     "tanner": ch(1550, -1, holds="phone_ring")},
           "meg": meg(1150, 1.25),
           "lines": {"0": {"hide": ["tanner"], "shots": ["close:doug", "wide"]}, "1": {"hide": ["tanner"]},
                     "2": {"hide": ["tanner"], "shots": ["meg", "medium:doug"]}}}

S["11"] = {"set": "backyard_pool",
           "chars": {"doug": ch(420, 1), "wren": ch(1600, -1, emo="deadpan")},
           "meg": meg(960, 1.7, pup=0.7),
           "lines": {"0": {"shots": ["wide", "meg"], "fx": ["splash"]}}}

S["12"] = {"set": "backyard_pool",
           "chars": {"doug": ch(760, 1, pose="sit", y=830), "wren": ch(1180, -1, pose="sit", y=830, emo="deadpan")},
           "meg": meg(650, 1.7, pup=0.7, facing=1, depth=700),
           "lines": {"0": {"move": {"meg": [1300]}}, "2": {"card_art": "size_compare", "shots": ["wide"]},
                     "5": {"shots": ["megclose", "close:doug"], "fx": ["splash"], "meg": {"x": 1300}},
                     "6": {"shots": ["close:wren"], "meg": {"x": 1300}}, "1": {"meg": {"x": 1300}},
                     "2": {"card_art": "size_compare", "shots": ["wide"], "meg": {"x": 1300}},
                     "3": {"meg": {"x": 1300}}, "4": {"meg": {"x": 1300}}}}

S["13"] = {"set": "backyard_pool",
           "chars": {"doug": ch(560, 1), "wren": ch(800, 1, emo="deadpan"), "hobbs": ch(1250, -1, holds="clipboard", emo="deadpan"),
                     "tanner": ch(1650, -1, holds="phone_ring")},
           "props": [{"id": "ute", "x": 1500, "y": 760, "scale": 0.9}],
           "meg": meg(1000, 1.7, pup=0.7),
           "lines": {"0": {"shots": ["pt:1500,640,1.6", "wide"]}, "6": {"pose": {"doug": "worry"}},
                     "11": {"shots": ["close:tanner", "close:doug"]}}}

S["14"] = {"set": "yard_night",
           "chars": {"doug": ch(560, 1, pose="sleep", y=800)},
           "props": [{"id": "deckchair", "x": 560, "y": 800, "scale": 1.2}],
           "meg": meg(800, 1.7, pup=0.7, facing=1, mood="calm"),
           "lines": {"0": {"move": {"meg": [1350]}}, "1": {"meg": {"x": 1350}}, "2": {"shots": ["meg", "close:doug"], "move": {"meg": [650]}, "meg": {"facing": -1, "x": 1350}}}}

S["15"] = {"set": "bait_shop",
           "chars": {"wren": ch(1150, -1, holds="", emo="deadpan"), "doug": ch(560, 1)},
           "props": [{"id": "counter", "x": 1150, "y": 925, "scale": 1.0, "front": True},
                     {"id": "fossil_tooth", "x": 1380, "y": 700, "scale": 1.0, "front": True}],
           "lines": {"1": {"shots": ["pt:860,300,2.2", "pt:1380,700,2.6"]}, "2": {"shots": ["pt:860,300,2.0", "wide"]}}}

LAG_KAYAK = {"doug": ch(1020, 1, pose="sit", y=820, water=812, holds="paddle"),
             "wren": ch(1240, 1, pose="sit", y=820, water=812, emo="deadpan")}
S["16"] = {"set": "lagoon_nursery",
           "chars": {**LAG_KAYAK, "hobbs": ch(300, 1, y=700, emo="deadpan", holds="clipboard")},
           "props": [{"id": "fish_truck", "x": 240, "y": 760, "scale": 0.8, "facing": -1},
                     {"id": "kayak", "x": 1130, "y": 820, "scale": 1.0, "front": True}],
           "meg": meg(1500, 1.8, y=870, pool=False, water=830, pup=0.7, behind=True),
           "lines": {"0": {"shots": ["pt:400,620,1.4", "close:hobbs"]},
                     "2": {"shots": ["wide", "meg"], "move": {"meg": [1700]}, "meg": {"facing": 1}},
                     "4": {"meg": {"facing": 1, "x": 1700}}}}

S["17"] = {"set": "lagoon_nursery",
           "chars": dict(LAG_KAYAK),
           "props": [{"id": "kayak", "x": 1130, "y": 820, "scale": 1.0, "front": True},
                     {"id": "fish_school", "x": 1450, "y": 930, "scale": 1.0}],
           "meg": meg(1700, 1.8, y=920, pool=False, water=830, pup=0.7, behind=True),
           "lines": {"0": {"shots": ["meg", "wide"], "move": {"meg": [1450]}, "meg": {"chomp": True, "mood": "hungry"}},
                     "1": {"meg": {"x": 1450}}, "2": {"meg": {"x": 1450}}, "3": {"meg": {"x": 1450}},
                     "4": {"meg": {"x": 1450}}, "5": {"meg": {"x": 1450}}}}

S["18"] = {"set": "lagoon_nursery",
           "chars": dict(LAG_KAYAK),
           "props": [{"id": "great_white", "x": 1470, "y": 470, "scale": 0.55, "facing": -1},
                     {"id": "kayak", "x": 1130, "y": 820, "scale": 1.0, "front": True}],
           "meg": meg(900, 1.8, y=880, pool=False, water=830, pup=0.7, behind=True, mood="curious", facing=1),
           "lines": {"0": {"shots": ["pt:1470,470,2.4", "wide"]}, "2": {"shots": ["pt:1470,470,2.4", "close:wren"]},
                     "4": {"shots": ["close:doug"]},
                     "5": {"shots": ["pt:1130,830,1.8", "wide"], "meg": {"x": 1130, "y": 860, "facing": -1}},
                     "6": {"shots": ["F4|wide"]},
                     "7": {"meg": {"x": 1130, "y": 860}}, "8": {"meg": {"x": 1130, "y": 860}},
                     "9": {"shots": ["wide"], "hide": ["great_white"]}}}

S["19"] = {"set": "lagoon_nursery",
           "chars": {"hobbs": ch(170, 1, y=720, holds="clipboard", emo="deadpan"), "doug": ch(360, 1, y=800),
                     "wren": ch(520, 1, y=880, emo="deadpan")},
           "meg": meg(1250, 1.8, y=900, pool=False, water=830, pup=0.7, facing=-1),
           "lines": {"6": {"shots": ["F3|close:tanner", "F3|wide"]}}}

S["20"] = {"set": "harbour_dock",
           "chars": {"tanner": ch(1050, 1, holds="phone_ring"), "doug": ch(380, 1, holds="fish")},
           "props": [{"id": "rental_boat", "x": 1450, "y": 800, "scale": 1.2}, {"id": "lamp_post", "x": 1780, "y": 640, "scale": 1.0}],
           "lines": {"0": {"hide": ["doug"], "shots": ["wide", "pt:1450,760,2.0"]}, "1": {"hide": ["doug"]},
                     "2": {"hide": ["doug"], "shots": ["pt:1450,760,2.0", "close:tanner"]},
                     "3": {"move": {"doug": [720]}, "pose": {"tanner": "talk1"}}}}
for k in ("4", "5", "6", "7", "8"):
    S["20"]["lines"].setdefault(k, {})
    S["20"]["chars"]["doug"]["x"] = 380
S["20"]["lines"]["4"] = {"shots": ["close:doug"], "move": {"doug": [720]}}
for k in ("5", "6", "7", "8"):
    S["20"]["lines"][k] = {"pose": {}, "move": {"doug": [720, 640]}}
S["20"]["lines"]["5"]["pose"] = {"doug": "arms_cross"}

S["21"] = {"set": "reef_edge_night",
           "chars": {"tanner": ch(1000, 1, y=752, holds="net", pose="reach")},
           "props": [{"id": "rental_boat", "x": 980, "y": 790, "scale": 1.3, "front": True}],
           "meg": meg(1500, 1.8, y=840, pool=False, water=780, pup=0.5, mood="curious", col="#3c5068", facing=-1),
           "lines": {"0": {"shots": ["wide", "close:tanner"]},
                     "1": {"shots": ["close:tanner", "meg"]},
                     "2": {"hide": ["tanner"], "fx": ["flash", "shake"], "shots": ["wide", "pt:960,700,1.3"]},
                     "3": {"shots": ["F2|close:tanner", "F2|wide"], "fx": ["dark"]}}}

SEA_KAYAK = {"doug": ch(640, 1, pose="sit", y=820, water=812, extras_add=["headlamp"]),
             "wren": ch(860, 1, pose="sit", y=820, water=812, extras_add=["headlamp"], emo="deadpan")}
S["22"] = {"set": "open_sea_night",
           "chars": {**SEA_KAYAK, "tanner": ch(1500, -1, y=1010, water=800, pose=["tread1", "tread2"], emo="scared")},
           "props": [{"id": "kayak", "x": 750, "y": 820, "scale": 1.0, "front": True}],
           "lines": {"0": {"shots": ["close:tanner", "wide"], "fx": ["shake"]},
                     "6": {"shots": ["07|meg", "07|close:doug"], "fx": ["flash"]}}}

S["23"] = {"set": "open_sea_night",
           "chars": {**SEA_KAYAK, "tanner": ch(1500, -1, y=1010, water=800, pose=["tread1", "tread2"], emo="scared")},
           "props": [{"id": "kayak", "x": 750, "y": 820, "scale": 1.0, "front": True}],
           "meg": meg(1250, 1.9, y=930, pool=False, water=830, pup=0.5, mood="curious", col="#3c5068", facing=1),
           "lines": {"0": {"shots": ["meg", "close:doug"], "move": {"meg": [1450]}},
                     "4": {"shots": ["wide", "medium:tanner"], "move": {"tanner": [1050, 1010], "meg": [1100]}, "meg": {"facing": -1, "x": 1500}},
                     "5": {"move": {"tanner": [1050, 1010]}, "meg": {"x": 1100, "facing": -1, "mood": "happy"}},
                     "6": {"meg": {"x": 1100, "facing": -1, "mood": "happy"}},
                     "7": {"meg": {"x": 1100, "facing": -1, "mood": "happy"}}}}
for k in ("6", "7"):
    S["23"]["lines"][k]["move"] = {"tanner": [1050, 860]}

S["24"] = {"set": "beach_dawn",
           "chars": {"wren": ch(330, 1, emo="deadpan"), "doug": ch(560, 1), "tanner": ch(900, 1, pose="sit", extras_add=["foil"], emo="sad"),
                     "hobbs": ch(1280, -1, holds="clipboard", emo="deadpan")},
           "props": [{"id": "rental_boat", "x": 1650, "y": 840, "scale": 1.0, "rot": -12}]}

S["25"] = {"set": "lagoon_nursery",
           "chars": {"doug": ch(900, 1, y=800, water=730), "wren": ch(120, 1, y=700, emo="deadpan"),
                     "hobbs": ch(290, 1, y=760, emo="deadpan"), "tanner": ch(450, 1, y=830, extras_add=["foil"], holds="phone_ring")},
           "meg": meg(1250, 2.3, y=880, pool=False, water=760, pup=0.3, mood="happy", facing=-1),
           "lines": {"0": {"shots": ["close:doug", "meg"], "hide": ["wren", "hobbs", "tanner"]},
                     "1": {"shots": ["meg", "wide"], "move": {"meg": [2300]}, "meg": {"facing": 1}, "hide": ["wren", "hobbs", "tanner"]},
                     "2": {"pose": {"doug": ["wave1", "wave2"]}, "hide": ["meg"]},
                     "3": {"hide": ["meg"]}, "4": {"hide": ["meg"]}, "5": {"hide": ["meg"]}, "6": {"hide": ["meg"]}}}

S["26"] = {"set": "honesty_studio",
           "chars": {"doug": ch(520, 1, idle=["explain1", "explain2"], y=900)},
           "meg": meg(1250, 1.0, y=560, pool=False, pup=1.0, mood="happy", facing=-1),
           "lines": {str(i): {"shots": ["wide", "meg"] if i % 2 else ["medium:doug", "wide"]} for i in range(10)}}

S["27"] = {"set": "doug_kitchen",
           "chars": {"doug": ch(700, 1, emo="confused", idle=["think"]), "tanner": ch(1250, -1, holds="envelope", emo="smug")},
           "props": [{"id": "fridge", "x": 1650, "y": 900, "scale": 1.0}],
           "lines": {"1": {"title": "COMMENT|CASH OR MEATBALL?", "shots": ["wide"]}}}

S["END"] = {"set": "honesty_studio", "chars": {"doug": ch(330, 1, pose="point", y=900)}}

WORDS = {"04": {"5": "CHIPS?"}, "06": {"1": "BROKEN?"}, "10": {"3": "LINK IN BIO"}, "13": {"7": "NO FORM"},
         "14": {"3": "PROMISE"}, "16": {"1": "NEVER HERE"}, "17": {"0": "FIRST FISH"}, "19": {"6": "TOMORROW"},
         "22": {"5": "TAP TAP"}, "23": {"6": "AM I THE FISH?"}, "24": {"7": "STAY WILD"}, "25": {"2": "BYE, BUDDY"},
         "26": {"1": "REAL", "4": "MADE UP", "5": "UP CLOSE ONLY"}}
for sc, ws in WORDS.items():
    for li, w in ws.items():
        S[sc].setdefault("lines", {}).setdefault(li, {})["word"] = w

json.dump({"aliases": ALIASES, "name_cards": NAME_CARDS, "scenes": S}, open(HERE / "staging.json", "w", encoding="utf-8"), indent=1)
json.dump(LOOKS, open(HERE / "cast_looks.json", "w", encoding="utf-8"), indent=1)
json.dump(VOICES, open(HERE / "voices.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("staging, looks, voices written")
