"""Narration via Google Cloud Text-to-Speech (Chirp 3: HD voices), REST + API key.

Env: GOOGLE_TTS_API_KEY (restrict the key to the Text-to-Speech API only).
Without a key (local dry runs) a silent track with an estimated duration is produced
so the rest of the pipeline can still be tested.
"""
from __future__ import annotations

import base64
import hashlib
import io
import json
import os
import time
import urllib.error
import urllib.request
import wave
from pathlib import Path

SAMPLE_RATE = 24000
ENDPOINT = "https://texttospeech.googleapis.com/v1/text:synthesize"


def _silence(seconds: float) -> bytes:
    return b"\x00\x00" * int(SAMPLE_RATE * seconds)


def wav_bytes_to_pcm(data: bytes) -> bytes:
    with wave.open(io.BytesIO(data)) as w:
        if w.getframerate() != SAMPLE_RATE or w.getnchannels() != 1 or w.getsampwidth() != 2:
            raise ValueError("unexpected TTS audio format")
        return w.readframes(w.getnframes())


def synthesize(text: str, voice: dict, cache_dir: Path) -> tuple[bytes, bool]:
    """Return (pcm16 mono 24 kHz, is_real_voice)."""
    from .config import load_dotenv
    load_dotenv()
    key = os.environ.get("GOOGLE_TTS_API_KEY")
    cache_dir.mkdir(parents=True, exist_ok=True)
    h = hashlib.sha1(json.dumps([text, voice], sort_keys=True).encode()).hexdigest()[:16]
    cached = cache_dir / f"{h}.pcm"
    if cached.exists():
        return cached.read_bytes(), True
    if not key:
        words = max(1, len(text.split()))
        wpm = voice.get("fallback_wpm", 165) * voice.get("speaking_rate", 1.0)
        return _silence(words / wpm * 60), False

    body = {
        "input": {"text": text},
        "voice": {"languageCode": voice.get("language", "en-US"), "name": voice["name"]},
        "audioConfig": {"audioEncoding": "LINEAR16", "sampleRateHertz": SAMPLE_RATE},
    }
    if voice.get("speaking_rate", 1.0) != 1.0:
        body["audioConfig"]["speakingRate"] = voice["speaking_rate"]
    last = None
    for attempt in range(6):
        req = urllib.request.Request(f"{ENDPOINT}?key={key}", data=json.dumps(body).encode(),
                                     headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                audio = base64.b64decode(json.loads(r.read())["audioContent"])
            pcm = wav_bytes_to_pcm(audio)
            cached.write_bytes(pcm)
            return pcm, True
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}: {e.read()[:300]!r}"
            if e.code == 400 and "speakingRate" in last and "speakingRate" in body["audioConfig"]:
                body["audioConfig"].pop("speakingRate")  # voice doesn't support pace control
                continue
            if e.code not in (429, 500, 502, 503, 504):
                break
        except Exception as e:  # network hiccup
            last = repr(e)
        time.sleep(2 ** attempt)
    raise RuntimeError(f"TTS failed for text {text[:60]!r}: {last}")


def write_wav(path: Path, pcm: bytes):
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SAMPLE_RATE)
        w.writeframes(pcm)


def pcm_seconds(pcm: bytes) -> float:
    return len(pcm) / 2 / SAMPLE_RATE
