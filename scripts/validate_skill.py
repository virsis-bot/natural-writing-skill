#!/usr/bin/env python3
"""Reject an automatic skill update that breaks the rules in update_prompt.md.

Compares the working-tree skill with HEAD. Exit code 1 with reasons on failure.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = "skills/natural-writing/SKILL.md"
MAX_WORDS = 2600
EDITABLE = {
    "Content: don't do this",
    "Language: don't do this",
    "Formatting: don't do this",
    "Chat residue in deliverables",
    "Citations and edit summaries",
}


def sections(text):
    """Split into {heading: body}; text before the first '## ' goes under ''."""
    parts = re.split(r"^## (.+)$", text, flags=re.M)
    out = {"": parts[0]}
    for i in range(1, len(parts), 2):
        out[parts[i].strip()] = parts[i + 1]
    return out


def main():
    old = subprocess.run(
        ["git", "show", f"HEAD:{SKILL}"], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout
    new = (ROOT / SKILL).read_text()
    errors = []

    words = len(new.split())
    if words > MAX_WORDS:
        errors.append(f"{words} words, limit {MAX_WORDS}")

    old_s, new_s = sections(old), sections(new)
    if list(old_s) != list(new_s):
        errors.append("section headings were added, removed or reordered")
    for name, body in old_s.items():
        if name not in EDITABLE and new_s.get(name) != body:
            errors.append(f"protected section changed: {name or 'frontmatter/intro'}")

    refs = subprocess.run(
        ["git", "status", "--porcelain", "--", "skills/natural-writing/references"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout
    if refs.strip():
        errors.append("references/ changed")

    for e in errors:
        print(f"validate_skill: {e}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
