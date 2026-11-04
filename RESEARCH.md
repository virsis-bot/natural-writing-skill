# Prior work and ideas (2026-11-04)

## Projects
- blader/humanizer — https://github.com/blader/humanizer (~64.7k stars). Claude Code skill on WP:AISIGNS. Extras: voice matching from the user's samples, draft → self-critique → final pass, never invents facts, edits only prose in files. Targets human readers, not detectors. No auto-update.
- Antislop — https://github.com/sam-paech/antislop-sampler, https://arxiv.org/abs/2510.15061. Finds over-represented words/phrases (some >1000x vs human text), bans them at sampling time. Open slop list.
- Russian: https://habr.com/ru/posts/986840 (prompt from WP:AISIGNS), blog lists on vc.ru and skillbox: канцелярит, отглагольные существительные, «в современном мире», too many lists, even tone. No corpus study found.

## What detectors do
- GPTZero dropped raw perplexity/burstiness scoring in 2023: https://support.gptzero.me/hc/en-us/articles/15130070230551
- Pangram is a trained classifier; its phrase list is a second pass after flagging: https://www.pangram.com/blog/pangram-ai-phrases
- Pangram claims 93.7% recall on humanizer output (vendor claim). UChicago study: Pangram near-perfect on medium/long text; GPTZero/Originality fooled by humanizers.
- What beats classifiers works at decoding time: DIPPER, Adversarial Paraphrasing (https://arxiv.org/abs/2506.07001), StealthRL (https://arxiv.org/abs/2602.08934). A prompt-only skill can't do this.
- Tell words shift over time (Kobak et al., https://arxiv.org/abs/2406.07016): "delve" fell after exposure, "significant" kept rising.

## Ideas for the skill (H = humans, J = LLM judges, D = statistical detectors)
1. Concrete checkable details; ask the user instead of writing filler. H, J.
2. Voice anchor: match a sample of the user's writing. H, J, maybe D.
3. Real burstiness: very short and long sentences, uneven paragraphs, fragments. H, J; small D.
4. Self-audit pass against the rules before delivering. H, J.
5. Ban the structural template (intro → list → conclusion, headings on short text). H, J.
6. Second-tier vocabulary from Antislop/Pangram lists; note that lists age. H, J, a bit D.
7. Fuller Russian section: канцелярит, «данный», «в рамках», «стоит отметить», typography. H, J.
8. Keep opinion and rough edges in personal writing. H.
9. State limits: no guarantee against Pangram/Turnitin.

Vendor numbers and paper results are not independently verified.
