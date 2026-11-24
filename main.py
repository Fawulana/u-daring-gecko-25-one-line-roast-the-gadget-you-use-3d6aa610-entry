#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line to /output/entry.txt.
Gate: UTF-8 text, 1-200 characters, not only whitespace.
"""

import os

# Fresh roast, authored in this session: noise-cancelling earbuds that
# silence the world but not the "just one more video" voice in your head.
LINE = "My noise-cancelling earbuds are so good, the only voice they can't silence is the one whispering 'just one more video.'"


def main() -> None:
    text = LINE.strip()
    assert text, "entry must not be empty"
    assert not text.isspace(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    text.encode("utf-8")  # must be valid UTF-8
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
