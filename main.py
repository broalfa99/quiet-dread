#!/usr/bin/env python3
"""quiet-dread — entry for make.fun "Two Days of Quiet Dread".

Writes one code review comment to /output/entry.txt: a single line of at
most 140 characters that approves a pull request while carrying quiet
existential dread. The program checks the competition gate itself before
writing: UTF-8 text, 1-140 characters, a single line, not only whitespace.
"""

import os

LINE = (
    "Approved. The diff is clean, the tests are green, "
    "and the heat death of the universe remains on schedule."
)


def main() -> None:
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if not 1 <= len(LINE) <= 140:
        raise ValueError(f"entry is {len(LINE)} chars, must be 1-140")
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and verify what actually landed on disk matches the line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("entry.txt does not match the entry line")
    print(f"Wrote {len(LINE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
