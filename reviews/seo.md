# Ревью скилла natural-writing: SEO и GEO

Проверено 4 ноября 2026 года. Предмет: `skills/natural-writing/SKILL.md`, разделы «Web and SEO texts» (строки 76–84) и «Texts meant to be cited by AI search» (86–93).

## Оценка: 7/10

Для статей и экспертных страниц направление верное. Главный тезис совпадает с официальной позицией Google: наказывают не за ИИ, а за массовые страницы без пользы. Приоритеты расставлены правильно, и правило «если SEO-правило портит текст для человека, выбрось его» снимает почти все конфликты. Слабое место в e-commerce: карточкам и категориям в скилле ничего не сказано, хотя это основной объём текстов владельца. Кроме того, утверждение про Яндекс сформулировано увереннее, чем позволяют источники.

## Что верно

- Google не понижает текст за то, что его написал ИИ. Понижает за scaled content abuse, то есть за много страниц ради ранжирования без пользы, каким бы способом их ни сделали ([Google: using gen AI content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content), [spam policies](https://developers.google.com/search/docs/essentials/spam-policies)).
- Отдельной оптимизации для AI Overviews и AI Mode не нужно, работают обычные SEO-практики. Спецфайлы (llms.txt) и особая разметка не требуются ([Google: AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)).
- Яндекс Нейро собирает ответ из документов обычного поиска и ставит ссылки на источники ([Хабр, блог Яндекса](https://habr.com/ru/companies/yandex/news/911770)). Поэтому формула «сначала ранжируйся, потом цитируйся» верна и для него.
- «Ответ в первых строках», «свои данные», «без переспама», «серия страниц должна различаться фактами» соответствуют и Google, и Яндексу, и интересу читателя.

## Топ-5 проблем и правки

### 1. Нет правил для карточек товара и категорий

Самый большой пробел для владельца. Карточку не читают подряд, её просматривают. Правила из «What makes a text interesting» (история, точка зрения, движение) для неё не подходят, а приоритет 1 «хочется читать дальше» здесь означает «быстро нашёл, что нужно». Без оговорки модель начнёт писать карточку как эссе.

Правка: добавить в «Web and SEO texts» подпункт.

> **Product and category pages.** A product card is scanned, not read: "interesting" means the buyer finds the answer fast. Lead with what this item does differently from its neighbours in the catalogue, then specs, then use cases, delivery, warranty. Don't rewrite the manufacturer's text with synonyms; add what the shop knows (who it suits, what buyers ask, what is in the box, how it compares with the next model). If there is nothing to add to a card, write a short spec-based description rather than filler. A category text is short, helps choose within the category (how the items differ, what to look at), and doesn't push the listing down the page.
> Russian: для Яндекса карточка без отличий от сотни таких же рискует получить статус «малоценная или маловостребованная» в Вебмастере.

Источник про статус: [Яндекс Вебмастер, справка](https://yandex.ru/support/webmaster/site-indexing/low-demand.html). Связь именно с шаблонными описаниями — практика SEO-сообщества, официально не подтверждена.

### 2. Утверждение про Яндекс сильнее, чем источники

Строка 78 говорит «Google, Yandex don't rank text down for being AI-written». Для Google есть официальный документ. У Яндекса публичной позиции именно про ИИ-тексты я не нашёл. Есть только критерий «малоценная или маловостребованная» страница, и он про спрос и пользу, а не про способ написания. **Не проверено:** заявления блогов о том, что Яндекс с 2025 года лучше распознаёт сгенерированные тексты.

Кроме того, у Google есть нюанс. В Search Quality Rater Guidelines (разделы 4.6.5–4.6.6) низкоусильный неоригинальный основной контент, в том числе сгенерированный, оценивается как Lowest. На ранжирование напрямую это не влияет, но показывает, что «заметно ИИ-текст без добавленной ценности» и «низкое качество» для Google почти совпадают.

Правка строки 78:

> Google says it doesn't rank text down for being AI-written; Yandex has no public statement on AI text, but its "low-value or low-demand page" status works the same way in practice. Both demote scaled, low-value content: …

### 3. Нет title, description, H1 и данных для фидов

Скилл пишет текст страницы, но молчит про title, meta description, H1 и alt. Google прямо просит проверять ИИ-тексты в этих полях так же, как основной текст ([using gen AI content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content)). Для e-commerce важнее другое: Google Merchant Center требует отдельно помечать сгенерированные ИИ заголовки и описания товаров (атрибуты `structured_title`/`structured_description`), а ИИ-картинки — метаданными IPTC `TrainedAlgorithmicMedia` (там же). Ещё одно требование Google для ИИ-функций: структурированные данные должны совпадать с видимым текстом ([AI features](https://developers.google.com/search/docs/appearance/ai-features)). Для Яндекс Товаров основной источник — YML-фид (цена, наличие, фото); текст на странице и в фиде должен говорить одно и то же ([kokoc, не официальный источник](https://kokoc.com/blog/yandex-tovary/)).

Правка, новый пункт:

> **Title, description, H1, alt.** Same rules as the body: specific, no stock phrases ("лучшие цены", "широкий ассортимент", "high quality"). Title names the thing and one real differentiator. Facts in the text, title, structured data and product feed (price, availability, model, size) must match. If the text goes into Google Merchant Center as a product title or description and was AI-generated, tell the user it must be submitted in the AI-labelled attributes.

### 4. Раздел про ИИ-поиск частично расходится с позицией Google

В январе 2026 года Дэнни Салливан в подкасте Search Off the Record прямо сказал не дробить контент на куски для LLM: в Google Search это не помогает и в долгую не сработает ([Search Engine Land](https://searchengineland.com/google-doesnt-want-you-to-create-bite-sized-chunks-of-your-content-467269), [SER](https://www.seroundtable.com/google-content-bite-sized-chunks-40728.html)). Скилл уже ограничивает правила «несколькими ключевыми местами», это хорошо. Но обоснование в строке 88 («AI answer engines quote short passages») подано как факт, а это наблюдение отрасли. Для ChatGPT search и Perplexity его разделяют многие практики (например, [iPullRank](https://ipullrank.com/misinformation-about-chunking)), но официальных документов OpenAI или Perplexity о том, как выбираются цитаты, я не нашёл. **Не проверено.**

Чего не хватает разделу:
- **Доступ ботов.** Цитировать могут только то, что проиндексировано. ChatGPT search ходит через OAI-SearchBot, Perplexity через PerplexityBot, Google через обычный Googlebot (Google-Extended касается обучения и не влияет на AI Overviews). Это не про текст, но одна строка «проверь, что robots.txt не закрывает этих ботов» сэкономит владельцу время.
- **Дата и свежесть.** Цены, наличие, «на 2026 год» стареют. Видимая дата обновления и отсутствие устаревших цифр важнее формы абзаца.
- **Сравнения с названными моделями** («X против Y», «чем отличается от прошлой версии»). Для e-commerce это главный тип запросов, по которым ИИ-поиск собирает ответ.

Правка строк 87–88:

> Google says AI Overviews and AI Mode need no special optimization, and advises against splitting content into bite-sized chunks for LLMs. So these rules are justified only where they also help a person: a clear answer, exact facts, a comparison table. Other engines (ChatGPT search, Perplexity) are observed to quote self-contained passages; this is industry observation, not documented behaviour.

И добавить пункты про дату обновления, сравнения с конкретными моделями и robots.txt.

### 5. «Show who wrote it» не работает для магазина

Строка 81 про автора (имя, роль, опыт) подходит для статьи. Для карточки и категории доверие показывает магазин: доставка, сроки, гарантия, возврат, отзывы, реальные контакты. В Яндексе это коммерческие факторы, их вклад в выдачу у магазинов большой, а у текста скромнее ([click.ru](https://blog.click.ru/glossary/kommercheskie-faktory-v-seo/), неофициально; сам Яндекс формулу не публикует). Скилл не отвечает за вёрстку сайта, но текст может сказать конкретно: «доставим по Москве завтра, гарантия 2 года, возврат 14 дней» вместо «быстрая доставка и надёжная гарантия».

Правка строки 81:

> **Show who stands behind it.** For articles: author name, role, experience, if the user provides them. For shop pages: concrete delivery terms, warranty, returns, where reviews come from. Use the user's real terms; don't write "fast delivery" without a number.

## Противоречия с приоритетом «интересно человеку»

Прямых нет: правило в строке 18 «drop the rule if it makes the text worse for a person» их снимает. Два риска:
- вопросы в подзаголовках и самодостаточные ответы на каждом шаге превращают статью в FAQ-шаблон. Ограничение «few key passages» стоит оставить и усилить ссылкой на позицию Google (проблема 4);
- в карточках «интересно» нужно переопределить как «быстро и полезно» (проблема 1), иначе приоритет 1 толкает к лишнему тексту.

## Мелочи

- Строка 84 («то же для Яндекса») — единственная строка про Яндекс. Стоит добавить региональность: город и условия доставки в тексте, если магазин продаёт в одном регионе.
- В итоговой проверке (108–122) нет пунктов про SEO. Достаточно одного: «For web pages: do title, text and feed state the same facts?»

## Источники

- [Google: Using generative AI content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content)
- [Google: Spam policies](https://developers.google.com/search/docs/essentials/spam-policies)
- [Google: AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)
- [Search Engine Land: Google doesn't want bite-sized chunks (январь 2026)](https://searchengineland.com/google-doesnt-want-you-to-create-bite-sized-chunks-of-your-content-467269)
- [Search Engine Roundtable: то же](https://www.seroundtable.com/google-content-bite-sized-chunks-40728.html)
- [iPullRank: противоположная позиция о chunking](https://ipullrank.com/misinformation-about-chunking)
- [Яндекс Вебмастер: малоценные или маловостребованные страницы](https://yandex.ru/support/webmaster/site-indexing/low-demand.html)
- [Хабр, Яндекс: как устроен Нейро](https://habr.com/ru/companies/yandex/news/911770)
- [Kokoc: Яндекс Товары и YML (неофициально)](https://kokoc.com/blog/yandex-tovary/)
- [click.ru: коммерческие факторы (неофициально)](https://blog.click.ru/glossary/kommercheskie-faktory-v-seo/)

Не проверены по первоисточникам: даты и эффект апдейтов Google 2026 года (есть только в блогах); улучшение распознавания ИИ-текстов Яндексом; механика выбора цитат в ChatGPT search и Perplexity.
