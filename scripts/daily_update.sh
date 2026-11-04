#!/usr/bin/env bash
# Daily run on the home server: fetch the guide, let Claude update the skill, push.
set -euo pipefail
cd "$(dirname "$0")/.."

[ -f .env ] && set -a && . ./.env && set +a
export PATH="$HOME/.local/bin:$PATH"

echo "== $(date -Is)"
git pull --ff-only -q

changed=$(GITHUB_OUTPUT=/dev/stdout python3 scripts/check_article.py | sed -n 's/^changed=//p')
if [ "$changed" != "true" ]; then
  git checkout -q -- source/state.json
  echo "no text changes"
  exit 0
fi

rm -f CHANGES.md
claude -p "$(cat scripts/update_prompt.md)" --model sonnet \
  --allowedTools "Read,Edit,Write,Glob,Grep" >/dev/null

if git diff --quiet -- skills/; then
  git add source/
  git commit -qm "Update article snapshot (no skill changes)"
  echo "snapshot only"
else
  summary=$(cat CHANGES.md 2>/dev/null || echo "Update from Wikipedia guide")
  { printf '## %s\n\n%s\n\n' "$(date +%F)" "$summary"; cat CHANGELOG.md 2>/dev/null; } > CHANGELOG.tmp
  mv CHANGELOG.tmp CHANGELOG.md
  git add skills/ source/ CHANGELOG.md
  git commit -qm "Update natural-writing skill from Wikipedia guide" -m "$summary"
  echo "skill updated"
fi
git push -q
