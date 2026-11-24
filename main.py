#!/usr/bin/env python3
"""One Word From Your Ex.

The single word an ex would use to describe you: "almost".
Almost the one. Almost enough. Almost — and then, not.

Writes exactly that word (6 bytes, no punctuation, no trailing newline)
to entry.txt inside the output directory the grader provides.
Pure standard library; deterministic; runs the same way every time.
"""

import os

WORD = "almost"


def main() -> None:
    word = WORD.strip()
    if not word or len(word) > 24 or any(ch.isspace() for ch in word):
        raise SystemExit("entry must be a single word of 1-24 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(word)
    print(word)


if __name__ == "__main__":
    main()
