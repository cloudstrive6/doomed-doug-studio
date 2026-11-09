"""One-off (approved by the owner 2026-11-09): replace still-scheduled cliffhanger Shorts with payoff-ending remakes.

    python pipeline/remake_shorts.py <ep> <short01,short02,...> [--dry-run]

For each named Short whose original is STILL private with a future publishAt (public ones are never touched):
1. render the remake from the episode's current shorts.json entry (payoff ending, simple end card; the old cliffhanger
   settings are kept in the entry under `cliffhanger_original`), same subtitle/loudness code path as new Shorts;
2. upload it private with the original's exact title, description, tags, category and paid-promotion flag, scheduled
   for the original's publishAt when that is >= 18 h away (review window), otherwise the next free Shorts slot;
3. add it to the Shorts playlist;
4. set the original to private with NO publishAt (unscheduled, explicit null) so it never goes public. Nothing is
   deleted: the owner deletes the originals in YouTube Studio;
5. record both ids in shorts.json (`youtube_id` = remake, `replaced_cliffhanger` = original).
Run it in GitHub Actions (.github/workflows/remake_shorts.yml); then `python -m studio social release <ep>` swaps the
draft-release media so the cross-posts use the remakes.
"""
from __future__ import annotations

import datetime as dt
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from studio import shorts  # noqa: E402
from studio.config import load_config  # noqa: E402


def _ep_dir(key: str) -> Path:
    return next(p for p in sorted((ROOT / "episodes").iterdir()) if p.name.startswith(key))


def _utc(s: str) -> dt.datetime:
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00"))


def _iso(t: dt.datetime) -> str:
    return t.astimezone(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def main(argv: list[str]) -> int:
    from googleapiclient.http import MediaFileUpload
    from studio import notify
    from studio.youtube import _parse_utc, add_to_playlist, local, yt

    dry = "--dry-run" in argv
    args = [a for a in argv if not a.startswith("--")]
    ep, ids = _ep_dir(args[0]), args[1].split(",")
    cfg = load_config()
    window = dt.timedelta(days=cfg["schedule"]["review_window_days"])
    meta = json.loads((ep / "metadata.json").read_text(encoding="utf-8"))
    api = yt()
    now = dt.datetime.now(dt.timezone.utc)

    # --- 1. which originals are still scheduled (private + future publishAt)?
    data = shorts.load(ep)
    by_id = {s["id"]: s for s in data["shorts"]}
    todo = []
    for sid in ids:
        s = by_id[sid]
        if s.get("replaced_cliffhanger"):
            print(f"{sid}: already remade ({s['youtube_id']}); skipping")
            continue
        old = s["youtube_id"]
        items = api.videos().list(part="snippet,status,paidProductPlacementDetails", id=old).execute().get("items", [])
        if not items:
            print(f"{sid}: original {old} not found; skipping")
            continue
        v = items[0]
        st = v["status"]
        if st.get("privacyStatus") != "private" or not st.get("publishAt") or _utc(st["publishAt"]) <= now:
            print(f"{sid}: original {old} is {st.get('privacyStatus')} (publishAt {st.get('publishAt')}); left as it is")
            continue
        todo.append((sid, v))
    if not todo:
        print("nothing to remake")
        return 0

    probs = [p for p in shorts.validate(ep) if p.split(":")[0] in {sid for sid, _ in todo}]
    if probs:
        raise SystemExit("shorts.json problems:\n" + "\n".join(probs))

    # --- 2. render the remakes (only these)
    made = shorts.render(ep, [sid for sid, _ in todo])
    print("rendered:", *[str(m) for m in made])

    data = shorts.load(ep)   # render() saved duration_s
    by_id = {s["id"]: s for s in data["shorts"]}
    report = []
    for sid, v in todo:
        s, old, st, sn = by_id[sid], v["id"], v["status"], v["snippet"]
        f = ep / "build" / "shorts" / f"{sid}.mp4"
        if not f.exists():
            print(f"{sid}: render missing, original left scheduled")
            continue
        slot = _utc(st["publishAt"])
        moved = False
        if slot - dt.datetime.now(dt.timezone.utc) < window:
            taken = [x for x in shorts.taken_slots() if _utc(x) != slot]
            slot = shorts.next_slot(taken, _parse_utc(meta["publish_at"])).astimezone(dt.timezone.utc)
            moved = True
        publish_at = _iso(slot)
        body = {"snippet": {k: sn[k] for k in ("title", "description", "tags", "categoryId", "defaultLanguage",
                                               "defaultAudioLanguage") if k in sn},
                "status": {"privacyStatus": "private", "publishAt": publish_at, "selfDeclaredMadeForKids": False,
                           "embeddable": True, "license": "youtube", "containsSyntheticMedia": False},
                "paidProductPlacementDetails": {"hasPaidProductPlacement": bool(
                    v.get("paidProductPlacementDetails", {}).get("hasPaidProductPlacement", False))}}
        print(f"{sid}: remake of {old} -> {publish_at} ({local(publish_at)})" + (" MOVED (slot < 18 h away)" if moved else "")
              + f", {s.get('duration_s')} s")
        if dry:
            continue
        resp = None
        for attempt in range(3):
            try:
                req = api.videos().insert(part="snippet,status,paidProductPlacementDetails", body=body,
                                          media_body=MediaFileUpload(str(f), chunksize=16 * 1024 * 1024, resumable=True))
                while resp is None:
                    _, resp = req.next_chunk()
                break
            except Exception as e:
                resp = None
                print(f"{sid}: upload attempt {attempt + 1} failed: {str(e)[:200]}")
                time.sleep(20 * (attempt + 1))
        if resp is None:
            notify.send(f"Shorts remake upload failed for {ep.name} {sid}; the cliffhanger original {old} is still scheduled.")
            continue
        new = resp["id"]
        try:
            add_to_playlist(api, new, cfg["shorts"].get("playlist", "Doomed Doug Shorts"))
        except Exception as e:
            s["playlist_warning"] = str(e)[:200]
        # --- 4. unschedule the original: private, publishAt explicitly null (keep its other status fields)
        keep = {k: st[k] for k in ("embeddable", "license", "publicStatsViewable", "selfDeclaredMadeForKids") if k in st}
        api.videos().update(part="status", body={"id": old, "status": {**keep, "privacyStatus": "private",
                                                                         "publishAt": None}}).execute()
        for _ in range(6):   # the API can return the old publishAt for a few seconds after the update
            time.sleep(10)
            chk = api.videos().list(part="status", id=old).execute()["items"][0]["status"]
            ok = chk.get("privacyStatus") == "private" and not chk.get("publishAt")
            if ok:
                break
        s["replaced_cliffhanger"] = {"youtube_id": old, "publish_at": s.get("publish_at"),
                                     "uploaded_at": s.get("uploaded_at"), "related_set": s.get("related_set"),
                                     "unscheduled": ok, "note": "cliffhanger original; private, unscheduled; owner deletes in Studio"}
        s.update(youtube_id=new, publish_at=publish_at, related_video=meta["youtube_id"], related_set=False,
                 uploaded_at=dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), remade_at="2026-11-09")
        s.pop("social", None)
        shorts.save(ep, data)
        line = (f"{ep.name} {sid}: {old} -> {new}, slot {local(publish_at)}" + (" (moved: old slot < 18 h away)" if moved else "")
                + ("" if ok else " WARNING: original still has a publishAt"))
        report.append(line)
        print(line, f"https://youtu.be/{new}")
    if report and not dry:
        notify.send("🩳 Cliffhanger Shorts remade with payoff endings (originals set private + unscheduled; delete them "
                    "in Studio):\n" + "\n".join(report) +
                    f"\nSet each remake's Related video to: {meta['title']} (https://youtu.be/{meta['youtube_id']})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
