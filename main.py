#!/usr/bin/env python3
"""Write one funny one-star cat review of its human to entry.txt.

Stdlib only. Honors MAKEFUN_OUTPUT_DIR (defaults to /output).
"""
import os

REVIEW = (
    "One star. He refills my bowl on time, then sits on my warm laptop "
    "all day and calls ME needy. I pay rent in purrs; he pays in betrayal."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = REVIEW.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be whitespace only"
    assert "\n" not in text, "entry must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
