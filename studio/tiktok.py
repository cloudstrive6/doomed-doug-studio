"""TikTok via Post for Me (https://postforme.dev), project "Doomed Doug" (Quickstart = Post for Me's approved
TikTok app, so posts go public right away). Mirrors the InforMed publisher.
Safety: only ever posts to the TikTok account whose external id / username is config social.tiktok_handle.
Env: POSTFORME_API_KEY (project-scoped key).
"""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path

from .config import load_config, load_dotenv

API = "https://api.postforme.dev/v1"


def _call(method: str, path: str, body: dict | None = None):
    load_dotenv()
    req = urllib.request.Request(f"{API}{path}", method=method,
                                 data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Authorization": f"Bearer {os.environ['POSTFORME_API_KEY']}",
                                          "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"Post for Me {e.code}: {e.read()[:400]!r}") from None


def enabled() -> bool:
    load_dotenv()
    return bool(os.environ.get("POSTFORME_API_KEY"))


def account() -> dict:
    handle = load_config().get("social", {}).get("tiktok_handle", "doomeddoug").lstrip("@").lower()
    accts = _call("GET", "/social-accounts?platform=tiktok&limit=50").get("data", [])
    a = next((x for x in accts if (x.get("external_id") or "").lower() == handle
              or (x.get("username") or "").lstrip("@").lower() == handle), None)
    if not a:
        raise RuntimeError(f"Post for Me: no TikTok account @{handle} in this project "
                           f"(found: {', '.join(x.get('username') or '?' for x in accts) or 'none'})")
    if a.get("status") != "connected":
        raise RuntimeError(f"Post for Me: @{handle} TikTok is {a.get('status')}; reconnect it at app.postforme.dev")
    return a


def _upload(file: Path) -> str:
    u = _call("POST", "/media/create-upload-url", {})
    req = urllib.request.Request(u["upload_url"], data=file.read_bytes(), method="PUT",
                                 headers={"Content-Type": "video/mp4"})
    with urllib.request.urlopen(req, timeout=1800) as r:
        if r.status >= 300:
            raise RuntimeError(f"Post for Me upload HTTP {r.status}")
    return u["media_url"]


def post_video(file: Path, caption: str) -> dict:
    acct = account()
    media = _upload(file)
    p = _call("POST", "/social-posts", {
        "caption": caption[:2200],
        "social_accounts": [acct["id"]],
        "media": [{"url": media, "thumbnail_timestamp_ms": 1000}],
        "platform_configurations": {"tiktok": {
            "privacy_status": os.environ.get("TIKTOK_PRIVACY", "public"),
            "allow_comment": True, "allow_duet": True, "allow_stitch": True,
            # narration is an AI voice: label it as AI-generated, like the InforMed publisher
            "is_ai_generated": True}},
    })
    for _ in range(40):  # TikTok processing usually takes 1-3 minutes
        time.sleep(15)
        res = (_call("GET", f"/social-post-results?post_id={p['id']}").get("data") or [None])[0]
        if not res:
            continue
        if not res.get("success"):
            raise RuntimeError(f"TikTok (Post for Me) failed: {json.dumps(res.get('error'))[:400]}")
        pd = res.get("platform_data") or {}
        return {"id": pd.get("id") or p["id"], "url": pd.get("url")}
    return {"id": p["id"], "url": None}
