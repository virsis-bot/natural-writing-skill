#!/usr/bin/env python3
"""Add a new entry to the version history in README.md and print its name.

Usage: add_version.py "summary"
"""
import datetime
import re
import sys
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"
HEADING = "## История версий\n"


def main():
    text = README.read_text()
    if HEADING not in text:
        print("add_version: no version history section in README.md", file=sys.stderr)
        return 1
    numbers = [int(n) for n in re.findall(r"^### v(\d+) ", text, flags=re.M)]
    version = f"v{max(numbers, default=0) + 1}"
    today = datetime.date.today().isoformat()
    entry = f"\n### {version} ({today})\n\n{sys.argv[1].strip()}\n"
    README.write_text(text.replace(HEADING, HEADING + entry, 1))
    print(version)
    return 0


if __name__ == "__main__":
    sys.exit(main())
