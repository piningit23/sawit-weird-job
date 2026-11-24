#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown — make.fun entry.

Writes a single job title (<=60 chars) to /output/entry.txt.
The title is a real job with one gloriously specific twist: professional
mourners are hired to grieve at funerals; this one only works strangers'.
"""

import os

TITLE = "Professional Mourner for Strangers' Funerals"


def main() -> None:
    if not (1 <= len(TITLE) <= 60) or not TITLE.strip():
        raise ValueError("title must be 1-60 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(TITLE)
    # Gate check: exactly the title, no trailing newline, UTF-8, <= 60 chars.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == TITLE


if __name__ == "__main__":
    main()
