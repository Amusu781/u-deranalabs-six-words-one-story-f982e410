#!/usr/bin/env python3
"""Six Words, One Story — entry program.

Writes one original six-word story to /output/entry.txt.
"""

import os

STORY = "She buried him twice. He noticed."

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # Create the output directory first (the grader mounts it read-only
    # for the program, but it exists by then; makedirs is harmless).
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Clear only the CONTENTS of the output dir, never the dir itself.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
