# natural-writing skill

Claude skill that helps write prose without the patterns that mark text as AI-generated. Built from Wikipedia's field guide [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).

- `skills/natural-writing/SKILL.md` — the skill.
- `source/article.txt`, `source/state.json` — snapshot of the guide the skill was last checked against.
- `scripts/check_article.py` — fetches the guide, writes the snapshot and a diff (`source/last-diff.diff`).
- `skills/natural-writing/references/web.md` — SEO, e-commerce and AI-search rules, loaded only for web pages.
- `scripts/validate_skill.py` — rejects an automatic update that touches protected sections, `references/` or exceeds 2400 words.
- `reviews/` — independent reviews and the blind A/B test (2026-11-04).
- `scripts/daily_update.sh` — daily cron job on the home server (`agent@192.168.1.60`, `~/projects/Claude_code_folder/Natural-writing`). If the guide's text changed, `claude -p` reads the diff (`scripts/update_prompt.md`) and decides whether the skill needs an update. Skill changes are committed to `main` with a summary in `CHANGELOG.md`; otherwise only the snapshot is committed.

## Server setup

- `.env` (not in git) holds `CLAUDE_CODE_OAUTH_TOKEN` from `claude setup-token`.
- Push goes through the deploy key `~/.ssh/natural_writing_deploy` (host alias `github-natural_writing`).
- Cron: `15 7 * * * ~/projects/Claude_code_folder/Natural-writing/scripts/daily_update.sh >> ~/projects/Claude_code_folder/Natural-writing/daily.log 2>&1`
- Manual run: `scripts/daily_update.sh`
