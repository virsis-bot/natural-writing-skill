#!/usr/bin/env python3
"""Fetch Wikipedia:Signs of AI writing and compare it with the stored snapshot.

Writes source/article.txt, source/state.json and, when the text changed,
source/last-diff.diff. Prints changed=true|false to $GITHUB_OUTPUT if set.
"""
import difflib
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

TITLE = "Wikipedia:Signs of AI writing"
API = "https://en.wikipedia.org/w/api.php"
USER_AGENT = "natural-writing-skill-updater/1.0 (https://github.com/)"

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "source"
ARTICLE = SOURCE / "article.txt"
STATE = SOURCE / "state.json"
DIFF = SOURCE / "last-diff.diff"


def fetch():
    params = {
        "action": "query",
        "prop": "extracts|revisions",
        "explaintext": "1",
        "rvprop": "ids|timestamp",
        "titles": TITLE,
        "redirects": "1",
        "format": "json",
        "formatversion": "2",
    }
    req = urllib.request.Request(
        f"{API}?{urllib.parse.urlencode(params)}", headers={"User-Agent": USER_AGENT}
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        page = json.load(resp)["query"]["pages"][0]
    rev = page["revisions"][0]
    text = "\n".join(line.rstrip() for line in page["extract"].splitlines()).strip() + "\n"
    return text, {"revid": rev["revid"], "timestamp": rev["timestamp"]}


def set_output(changed):
    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a") as f:
            f.write(f"changed={'true' if changed else 'false'}\n")


def main():
    text, state = fetch()
    old = ARTICLE.read_text() if ARTICLE.exists() else ""
    old_state = json.loads(STATE.read_text()) if STATE.exists() else {}

    changed = text != old
    if changed:
        diff = difflib.unified_diff(
            old.splitlines(keepends=True),
            text.splitlines(keepends=True),
            fromfile=f"rev {old_state.get('revid', 'none')}",
            tofile=f"rev {state['revid']}",
            n=2,
        )
        SOURCE.mkdir(exist_ok=True)
        DIFF.write_text("".join(diff))
        ARTICLE.write_text(text)
    STATE.write_text(json.dumps(state, indent=2) + "\n")

    print(f"revid {old_state.get('revid')} -> {state['revid']}, text changed: {changed}")
    set_output(changed)


if __name__ == "__main__":
    sys.exit(main())
