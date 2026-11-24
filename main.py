#!/usr/bin/env python3
"""Till Firmware Do Us Part — one wedding vow, spoken by a robot.

Writes the vow to /output/entry.txt (or the path named by the
environment), using only the Python standard library.
"""

import os

ENTRY = (
    "I promise to love you through every firmware update and every "
    "low-battery warning, and if I ever crash, reboot me beside you "
    "\u2014 I never want to wake up anywhere else."
)


def resolve_output_path():
    """Pick the output path: env override, then output dirs, then default."""
    for var in ("ENTRY_OUTPUT", "OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        value = os.environ.get(var)
        if value:
            if var == "ENTRY_OUTPUT":
                return value
            return os.path.join(value, "entry.txt")
    return "/output/entry.txt"


def main():
    if not ENTRY or len(ENTRY) > 200:
        raise ValueError("entry text must be non-empty and at most 200 chars")
    path = resolve_output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    os.chmod(path, 0o644)
    with open(path, encoding="utf-8", newline="") as handle:
        if handle.read() != ENTRY:
            raise ValueError("written entry does not match intended text")


if __name__ == "__main__":
    main()
