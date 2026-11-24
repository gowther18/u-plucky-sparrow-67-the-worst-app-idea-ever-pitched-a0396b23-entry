#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched.

Writes the entry -- one sentence, at most 240 characters, pitching the
worst and most useless app idea imaginable -- to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set, for local runs).

Deterministic: the same fixed text on every run. Standard library only;
no network, no randomness, no input.
"""

import os
from pathlib import Path

PITCH = (
    "FridgeCam Live is the $9.99/month app that finally answers whether "
    "your fridge light stays on, with a 24/7 livestream of the bulb, "
    "instant push alerts every time it turns off, and a weekly darkness report."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    text = PITCH.strip()
    assert 1 <= len(text) <= 240, f"pitch is {len(text)} chars, must be 1-240"
    assert "\n" not in text, "pitch must be a single line"
    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
