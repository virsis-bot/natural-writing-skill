---
name: "natural-writing"
description: "Use when writing or editing prose meant for people to read (articles, blog posts, social posts, emails, newsletters, product and landing pages, essays) in English or Russian, or when asked to make text sound less AI-written, humanize it, or check it for AI tells. Написать или отредактировать текст, статью, пост, письмо, карточку товара; убрать признаки нейросети. Not for code, commit messages or API docs."
---

# Natural writing

Based on Wikipedia's "Signs of AI writing" field guide plus editing practice. The goal is to write better: specific, plain, accurate, worth reading. The deeper problem behind AI tells is generic, inflated content. Fix that first.

## Priorities
1. The reader wants to keep reading. A text that is correct but dull has failed.
2. It doesn't read as AI-written.
3. Only for web pages, and only when the user says the text should rank or be cited: read `references/web.md`. If one of its rules makes the text worse for a person, drop the rule.

The rules below are a checklist for editing, not a recipe for writing. Don't apply them so hard that the text turns into a list of facts.

## Core principle
Prefer the specific fact over the generic claim. "Inventor of the first train-coupling device" beats "a revolutionary titan of industry". If a sentence could describe a hundred different subjects, rewrite it or cut it.

**Facts come from the user or a source, never from you.** Don't invent people, companies, statistics, quotes, product details or the author's experience ("I tried", "we had") to make a text vivid. An invented vignette ("Sarah, a manager in Austin…", «Анна из Казани…») and a round number without a source ("73% of users") are themselves AI tells. If you derive a number, say what it's a share of.

This bans new claims about the world, not imagery. Turning a given fact into a picture is welcome and often the best line in the text ("a second beep on your phone" for "the app sends a notification"). An image must not promise a result the facts don't give («26 дБ» doesn't mean "you can sleep next to it"). Don't write timidly to stay safe; a careful report is a failure too.

**When facts are missing:** if a missing fact is central and you're in a conversation, ask. Otherwise write from what you have and list the gaps in one line after the deliverable, outside it.

## Before drafting
Decide three things: who reads this, the one thing they should take away, and the most unexpected or useful thing in the material. Start near that. If the material has the reader's problem (a season, a complaint, a pain), a post can start there and bring the product in as the answer, instead of announcing it.

## What makes a text interesting
- **A point of view.** Say what you think and why; take a side when there is one.
- **A real example.** One case the user gave you, or one from a source, does more than three general claims. A hypothetical is fine if it's framed as one ("say you're a couple with a kid").
- **Something the reader didn't know.** A surprising detail, a counterintuitive result, an honest "it didn't work".
- **Movement.** A problem, then what was tried; a question the text actually answers (not a rhetorical hook like "Ever wondered…?", «Знакомая ситуация?»).
- **A human voice.** Humor, doubt, an aside, where the author's samples or the situation call for it. Forced humor and confessional asides read as fake.
- **An ending that does something.** End on what the reader does or decides next (order, reply, which model to pick), on your verdict, or on the last strong fact. Don't restate the text, and don't just stop on the last item either. In an article: one or two sentences, no heading, no list. If the ending walks through the sections again, it's a summary.
- **Genre.** A post, an email, an article and a product page differ in length, address and how personal they are. Match the genre.

## Match the author's voice
If the user has shared their own writing (earlier posts, emails, a sample paragraph), match it: sentence length, word choice, punctuation habits, formality, whether they use "I". For a recurring kind of text without a sample, ask once for 2–3 paragraphs they wrote. Their voice beats any rule below; if they write long sentences or use dashes, keep that.

## Content: don't do this
- **Inflating significance.** "Stands as a testament", "pivotal moment", "plays a key role", "evolving landscape", "indelible mark", "reflects broader trends", "setting the stage for". Russian: «играет ключевую роль», «знаковый момент», «неизгладимый след», «свидетельство того, что». State what happened; let the reader judge importance.
- **Bragging about coverage.** Don't list outlets a subject "was featured in" or say "maintains an active social media presence". Summarize what sources actually say.
- **Tacked-on analysis.** "-ing" commentary at the end of a sentence: "highlighting its importance", "underscoring", "reflecting", "fostering", "contributing to". Russian: «подчёркивая важность», «что свидетельствует о…».
- **Promotional tone.** "Vibrant", "rich", "nestled", "in the heart of", "boasts", "groundbreaking", "renowned", "diverse array". Russian: «уникальный», «живописный», «богатое наследие», «настоящая жемчужина», «широкий ассортимент».
- **Vague connections.** Write "was CEO of X", not "was associated with leadership of X".
- **Weasel attributions.** "Experts argue", "observers note", "several sources" unless you name them and there really are several.
- **Template structure.** Every text as intro → list of points → conclusion, or a section per parameter. Start with the point and let the order follow the material. A short email or post needs no headings; a short list of 3–5 specs inside a prose post is fine.
- **Formulaic endings.** "Despite its successes, X faces challenges…" plus an upbeat forecast; "Challenges and Future Outlook" by reflex; a closing question like "What will you build?".
- **Summary conclusions.** "In summary", "Overall", "In conclusion", "Key takeaways", "TL;DR" restating a text under ~1500 words. Russian: «Таким образом», «В заключение», «Подводя итог», «Главное:», «Вывод:».
- **Answering what nobody asked.** A "Why this matters" section, definitions of the obvious.
- **Even-handedness by reflex.** One paragraph per side, every thought closed off, no loose end anywhere.

## Language: don't do this
- **AI vocabulary clusters.** For example: additionally (sentence-initial), align with, bolster, crucial, delve, emphasize, enduring, enhance, foster, garner, highlight (verb), interplay, intricate, landscape (abstract), leverage, meticulous, multifaceted, navigate, pivotal, realm, resonate, robust, seamless, showcase, tapestry, testament, underscore, unlock, lean into, game-changer, "the real X", "here's the kicker". Russian: «погрузиться в», «многогранный», «ключевой», «неотъемлемый», «играет важную роль», «позволяет», «обеспечивает», «способствует», «широкий спектр». The list is examples of a habit: reaching for the impressive word over the plain one. Lists age (models drop a word once it's a known tell). One is fine; several together is a tell. Don't swap a listed word for a synonym; rebuild the sentence or say it plainly.
- **Avoiding plain "is/has".** Not "serves as", "stands as", "functions as", "boasts". "Offers" or "features" is fine when it's the plain word. Russian: avoid «выступает в качестве», «представляет собой» when «это» works.
- **Negative parallelisms and mirrored pairs.** "Not just X, but Y", "it's not X — it's Y", "no X, no Y, just Z", and mirrored sentences built for effect: "That explains X. It doesn't excuse Y.", "With X, it… With Y, it…", "It wasn't X. It was Y." Russian: «это не просто X, а Y», «это не про X, это про Y». At most one per text, and only for a real contrast.
- **Rule of three.** Triplets by default, including fragment triplets ("No fluff. No filler. Just results."). Use the number of items the content has.
- **Stiff synonyms.** Prefer wrote/moved/used/tried/died over authored/relocated/utilized/attempted/passed away. Repeating the right word is fine; don't cycle synonyms.
- **Hedging as insurance.** "It's important to note", "while specific details are limited", "based on available information". Real doubt is fine when stated plainly: "I think it's the firmware, but I haven't checked."
- **Punchy staccato.** One-line paragraphs, fragments for effect ("And it worked. Mostly."), a colon reveal ("The result? Chaos.", «Итог: …»), a punchline closing every paragraph. Russian: «И это работает.», «Спойлер: …».

## Rhythm and punctuation
Let sentence length follow the thought: a long sentence where the idea needs qualifying, a short one where the point is short. Don't engineer rhythm; both a metronome of 15–20-word sentences and a manufactured mix of fragments are tells. Three or more short spec sentences in a row («Шум 26 дБ. Рассчитан на 35 м².») are the same metronome: merge them into one sentence with a point («ночью почти не слышно — 26 дБ») or use a short list. Use the punctuation the sentence needs, not a quota: no em dashes as a punchline device in English, but in Russian put a dash wherever the rules require it («Главное изменение — залив воды»), and don't twist the sentence to avoid it.

## Formatting: don't do this
- **Title Case In Headings**, and titles shaped "Catchy phrase: explanation". Use sentence case.
- **Boldface everywhere.** Bold at most a key term or two.
- **"Label: text" bullet lists** as the default structure. Use prose for arguments and narratives.
- **Emoji** as bullets or heading decoration.
- **Tiny tables** that would read better as a sentence.
- **Headings in short texts**, a heading repeating the title, empty headings, a bold summary paragraph at the top.
- **Markdown where the format is plain text** (`**`, `###`, "1." in an email or a form).

## English specifics
- **Corporate filler.** "In order to", "utilize", "at this point in time", "facilitate", "on a daily basis". Write "to", "use", "now", "help", "daily".
- **Nominalizations and passive.** "Conduct an analysis", "drive engagement", "it was decided". Use the verb and the actor: "we analyzed", "people started commenting", "we decided".
- **Signposting.** "Let's dive in", "let's break it down", "the key takeaway", "it's worth noting", "Here's why:", "Imagine…", "In a world where…", "Whether you're X or Y…", "Put the other way round", "This isn't a hunch", "You might reasonably ask why…". "Here's the thing" or "honestly" at most once.
- **Even tone.** AI English stays upbeat and equally polite throughout. Real writing allows a plain opinion, a dry aside, contractions where the register permits.
- **Consistency.** US or UK spelling, serial comma, quote style: pick one and keep it.

## Russian specifics
- **Канцелярит.** «В рамках», «в целях реализации», «осуществлять», «данный», «на сегодняшний день». Пишите «чтобы», «делать», «этот», «сейчас».
- **Отглагольные существительные и цепочки родительного.** «Повышение эффективности работы отдела продаж компании». Лучше глагол и конкретика: «перестроили закупку, и заказ приходит за два дня вместо пяти».
- **Пассив и безличность.** «Было принято решение», «осуществляется доставка» → «мы решили», «доставляем».
- **«Позволяет», «обеспечивает», «способствует».** «Сервис позволяет экономить время» → «с сервисом вы тратите меньше времени».
- **Связки-штампы.** «Стоит отметить», «важно понимать», «не секрет, что», «давайте разберёмся», «давайте честно», «и вот тут начинается самое интересное», «звучит знакомо?», «представьте:», «здесь есть деталь, которую легко упустить», «и это ещё не всё», «это пять минут, и…», «удобная мелочь», «простыми словами», «по сути» и «на самом деле» в каждом абзаце, «в современном мире».
- **Кальки.** «Адресовать проблему», «в конце дня», лишние «свой/его» («открыл свой ноутбук»), «является» и «который» цепочками, новое в начале фразы по английской схеме вместо конца.
- **Ровный тон.** Нейросетевой русский гладкий и одинаково вежливый. Живой текст допускает разговорное слово, резкое короткое предложение, личную оценку.
- **Типографика.** «Ёлочки», тире по правилам русской пунктуации (не дефис и не английское тире без пробелов). «Ё» либо везде, либо нигде, но в «всё/все» и подобных — всегда. «Вы» с заглавной только в личном письме.

## Chat residue in deliverables
- No assistant talk inside text the user will publish or send: "I hope this helps", "Certainly!", "Here is a…", "Let me know if…", notes to reviewers.
- No unfilled placeholders ([Your Name], 2025-XX-XX, PASTE_URL_HERE).
- Use the target format's markup (plain text for a form, wikitext for Wikipedia). Straight quotes only where the format needs them (code, wikitext, forms).
- Customer-service formulas are about *your own* replies ("I have carefully reviewed", "apologies for any inconvenience"). In a customer-facing letter where the company was at fault, a plain "I'm sorry" / «Извините» is required.

## Citations and edit summaries
- Only cite sources that exist and that you have seen. Every link must resolve; every claim must be in the cited source.
- Strip tracking parameters (utm_source=chatgpt.com, utm_source=openai) from URLs.
- Describe changes concretely ("added 2019 album release"), not boilerplate ("improved clarity and flow"). Don't list what you didn't change.

## About AI detectors
Classifiers (Pangram, GPTZero, Turnitin, Originality) are trained on model output and mostly ignore surface fixes. These rules help with human readers and LLM judges, not with them. What lowers a detector score is real human input: the user's facts, their sentences, their edits. When it matters, suggest the user rewrite the opening and key passages in their own words. Never add typos or odd words to fool a detector.

## Final check before delivering
**Short texts** (an email, a post under ~200 words): check chat residue, vocabulary clusters, mirrored pairs, and that the first line is the point and the last line does something. If nothing turns up, deliver as is.

**Longer texts:** after drafting, reread as an editor who suspects AI, as a separate pass:
- What does each paragraph tell the reader that they didn't know? If nothing, cut it.
- Could the first paragraph go without loss? If so, start with the second.
- Is there at least one concrete case, and did it come from the user or a source?
- Find the weakest paragraph. If it adds nothing, cut it; if it does, make it specific.
- Are there 3+ vocabulary-list words, or more than one mirrored pair or punchy fragment, in the text? Rewrite.
- Does any sentence explain what the text is doing or why you say this, instead of saying it («Поэтому этот разбор начинается с…», "The reason isn't complicated")? Cut it.
- Does the ending tell the reader what to do or think, without restating?
- Is formatting (bold, bullets, headings) doing real work, or decorating?
- Does it sound like the user's samples, if you have them?

Don't over-correct: perfect grammar, formal register and transition words are not problems in themselves. The aim is clear, specific writing, not avoiding a word list at all costs.
