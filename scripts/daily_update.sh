#!/usr/bin/env bash
# Weekly run on the home server: fetch the guide, let Claude update the skill, push.
set -euo pipefail
cd "$(dirname "$0")/.."

[ -f .env ] && set -a && . ./.env && set +a
export PATH="$HOME/.local/bin:$PATH"

on_error() {
  # Without this rollback the changed snapshot stays on disk and the next run sees no changes
  git checkout -q -- skills/ source/ README.md || true
  git clean -fdq -- skills/ source/ || true
  rm -f CHANGES.md
  echo "failed at line $1"
  python3 scripts/notify_telegram.py "natural-writing: проверка статьи упала (строка $1 в daily_update.sh). Попытка повторится в следующий запуск, подробности в daily.log на сервере." || true
}
trap 'on_error $LINENO' ERR

echo "== $(date -Is)"
git pull --ff-only -q

changed=$(GITHUB_OUTPUT=/dev/stdout python3 scripts/check_article.py | sed -n 's/^changed=//p')
if [ "$changed" != "true" ]; then
  git checkout -q -- source/state.json
  git push -q
  echo "no text changes"
  exit 0
fi

rm -f CHANGES.md
claude -p "$(cat scripts/update_prompt.md)" --model sonnet \
  --allowedTools "Read,Edit,Write,Glob,Grep" </dev/null >/dev/null

if ! python3 scripts/validate_skill.py; then
  # Throw away the update and the snapshot so the next run retries it
  git checkout -q -- skills/ source/
  git clean -fdq -- skills/ source/
  rm -f CHANGES.md
  echo "update rejected"
  python3 scripts/notify_telegram.py "natural-writing: автообновление скилла отклонено проверкой. Подробности в daily.log на сервере." || true
  exit 1
fi

if git diff --quiet -- skills/; then
  git add source/
  git commit -qm "Update article snapshot (no skill changes)"
  echo "snapshot only"
else
  summary=$(cat CHANGES.md 2>/dev/null || echo "Обновление по справочнику Википедии.")
  version=$(python3 scripts/add_version.py "$summary")
  git add skills/ source/ README.md
  git commit -qm "Update natural-writing skill to $version from Wikipedia guide" -m "$summary"
  echo "skill updated: $version"
fi
git push -q

if [ -n "${version:-}" ]; then
  python3 scripts/notify_telegram.py "natural-writing $version: скилл обновлён

$summary

https://github.com/virsis-bot/natural-writing-skill#история-версий" || true
fi
