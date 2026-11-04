# natural-writing skill

Claude skill that helps write prose without the patterns that mark text as AI-generated. Built from Wikipedia's field guide [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).

- `skills/natural-writing/SKILL.md` — the skill.
- `source/article.txt`, `source/state.json` — snapshot of the guide the skill was last checked against.
- `scripts/check_article.py` — fetches the guide, writes the snapshot and a diff (`source/last-diff.diff`).
- `.github/workflows/daily-check.yml` — runs every day at 06:00 UTC. If the guide's text changed, Claude reads the diff and decides whether the skill needs an update. Skill changes arrive as a pull request; otherwise only the snapshot is committed.

## Setup

Add one repository secret: `ANTHROPIC_API_KEY`, or `CLAUDE_CODE_OAUTH_TOKEN` (from `claude setup-token`, uses a Claude subscription).
Enable "Allow GitHub Actions to create and approve pull requests" in Settings → Actions → General.

Run manually: Actions → "Daily check of Signs of AI writing" → Run workflow.
