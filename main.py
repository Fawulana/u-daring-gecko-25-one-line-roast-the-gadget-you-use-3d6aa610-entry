#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line (<= 200 chars) to /output/entry.txt.
Deterministic, offline, stdlib-only.
"""

import os

LINE = (
    # Chosen from 5 brainstormed candidates: the robot-vacuum angle is the
    # freshest (no battery/update/rating cliche), with a concrete daily
    # detail (same chair, every day) and a two-beat punchline.
    "My robot vacuum has a perfect map of my flat and still gets stuck "
    "under the same chair every single day - it memorized the floor plan "
    "and learned nothing."
)

OUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "line must be 1-200 characters"
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
