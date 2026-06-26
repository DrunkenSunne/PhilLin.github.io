# AGENT_HANDOFF

Last updated: 2026-06-26

2026-06-26 Word article and gripe: user provided `C:\Users\Phil Lin\Desktop\自己\自己总要写点东西\20260626.docx` with tag `一些思绪`. Codex generated `preview-20260626.html`; user disliked earlier titles and final title is `在风里慢慢好一点`. User then said `发吧`. Final article is `article-better-in-the-wind.html`, publication date `2026-06-26`, summary `一篇写在考试后夜晚的小广场上的随笔：从被游戏和烦躁困住的下午出走，在风、蛙鸣、乌龙茶和黄色月亮里，重新找到一种更安静的解压方式。`, and it is indexed in `window.BAR_POSTS`. The Word document contained no embedded media files. User also asked to publish the gripe `养细胞最忌讳顺手的事和顺便看一眼，莫名其妙就需要我处理然后两个小时消失了。`; Codex chose mood `无语`, emoji `😶`, timestamp `2026-06-26 23:24:04`. HTML asset query strings were refreshed to `bar-art-20260626-wind-gripes`.

2026-06-26 preview cleanup: user noticed preview-only wording and asked whether prior published pages also had it. Codex searched current `article-*.html`, `note-*.html`, and `preview-*.html` files for `Preview`, `预览`, `预览说明`, and `确认后发布`. Only `article-not-yet-return.html` had leftover preview UI, and it was cleaned. After cleanup, the same search returned no matches. JS syntax checks for `assets/site.js`, `assets/content.js`, and `assets/gripes.js` passed. Visual verification was skipped by project preference.

2026-06-26 Word article: user provided `C:\Users\Phil Lin\Desktop\临时用\新建 Microsoft Word 文档.docx` with tag `一些思绪`. Codex generated `preview-20260626.html`, then user said `发`. The final article is `article-not-yet-return.html`, title `不如归去，但还不能归去`, publication date `2026-06-26`, summary `一篇写在实验室深夜的长文：从不想回宿舍的迟疑出发，绕到陶渊明与王羲之，写归去的羡慕、责任的牵引，以及暂时还不能真正放下的自己。`, and it is indexed in `window.BAR_POSTS`. The preview file was deleted. The Word document contained no embedded media files. HTML asset query strings were refreshed to `bar-art-20260626-return`.

2026-06-25 short lab-still note: user provided direct text beginning `还在实验室坐着。` and asked Codex to decide the column, skip preview, and publish directly. Codex chose `吧台札记` because it is a self-contained reflective fragment, not a full article or a gripe. The final note is `note-lab-day-not-over.html`, title `只要不走，今天就还没有结束`, publication date `2026-06-25`, mood `缓冲`, and it is indexed in `window.BAR_NOTES` with tag `吧台札记`. HTML asset query strings were refreshed to `bar-art-20260625-lab-still`.

2026-06-25 bitmap-style drink labels and designed lede: user clarified that drink labels should follow the earlier concept/bitmap style and not resemble the original CSS glyphs. `assets/drink-labels/` now contains standalone illustrated SVG image assets for current and retained fallback drink classes; `assets/styles.css` maps `.drink-glyph` classes to those images and disables the old pseudo-element line drawings. The homepage lede is now a designed `After Hours Note` module on desktop, with separate tablet and phone rules. Current asset query string is `bar-art-20260625-bitmap-labels`.

2026-06-25 material drink labels: user disliked the latest hero lede layout and asked for drink labels with material, lighting, and hand-drawn detail. `index.html` now intentionally breaks the lede into two spans after `白天把事情做完，`. `assets/styles.css` keeps the existing `.drink-glyph` system but adds painted-paper texture, glass highlights, liquid depth, shadow glow, and per-drink garnish variables while preserving the canonical `5.2rem` internal glyph box. Current asset query string is `bar-art-20260625-material-labels`.

2026-06-25 home layout fix: user reported desktop screenshot issues in the homepage menu intro and Martini Flight card. `assets/styles.css` now gives `.hero-lede` a wider balanced text box, and the grouped Martini Flight card reserves right-side space for its absolute drink glyph on desktop/tablet while phone cards remove that large reserve. Current asset query string is `bar-art-20260625-layout-fix`.

2026-06-25 note/archive integration: user clarified that 吧台札记 counts as article-system content. `assets/site.js` now merges `BAR_POSTS` and normalized `BAR_NOTES` inside `allPosts()`, so homepage recent posts, `posts.html` "全部", and the new `吧台札记` filter include notes. `notes.html` remains note-only. The first note missing from `notes.html` was investigated: data/file were present, and a simulated DOM check now confirms `note-lab-after-exam-restlessness.html` renders into `data-note-list`; stale cache was the likely prior cause. Current asset query string is `bar-art-20260625-notes-archive`.

2026-06-24 publication: user provided a schedule screenshot for a life log. The final article is `article-after-exam-still-held.html`, tag `生活日志`, title `考完以后，也没有完全散掉`, publication date `2026-06-24`, and vague experiment wording (`实验室工作` / `细胞状态确认`). It has been added to `assets/content.js`; `preview-20260624.html` was deleted. User asked to change the original endnote because it felt too corny; final endnote is restrained. HTML asset query strings were refreshed to `bar-art-20260624-life-log` so index/archive/tag pages load the updated article metadata.

2026-06-24 drink glyph pass: user chose A+C for drink badges, meaning blueprint cocktail icon structure plus ingredient silhouette cues. `assets/styles.css` now upgrades all current page glyphs and retained fallback glyph classes while keeping the canonical `5.2rem` internal geometry and responsive transform scaling. Browser visual verification was attempted but blocked by local browser permissions; standalone Playwright is not installed. Current asset query string is `bar-art-20260624-glyphs`.

2026-06-25 first bar note: user provided `C:\Users\Phil Lin\Desktop\临时用\札记.docx` and asked to delete the previous template while publishing this note. The final note is `note-lab-after-exam-restlessness.html`, title `待在实验室，也不等于没有浪费时间`, publication date `2026-06-25`, mood `自我审问`, and it is indexed in `window.BAR_NOTES`. `_drafts/note-format-reference.html` was deleted at user request. HTML asset query strings were refreshed to `bar-art-20260625-note1` so `notes.html` loads the updated note metadata.

2026-06-24 column scaffold: added Hanky Panky / 吧台札记 for medium-length fragments. The new index is `notes.html`; note metadata lives in `window.BAR_NOTES` in `assets/content.js`; individual notes should be independent `note-*.html` files. The old `_drafts/note-format-reference.html` template has now been deleted, so future notes should follow existing published `note-*.html` pages instead. The top navigation was intentionally not expanded; the homepage entry is only inside the Martini Flight variant links. Content boundary: 吐槽 should stay around 50 Chinese characters and preferably under 100, 吧台札记 is roughly 300 to 1200 characters, full essays remain normal articles.

2026-06-23 publication: user provided direct text for today's life log with tag `生活日志`. The final article is `article-one-side-cannot-fall.html`, title `起码一边不能倒下`, publication date `2026-06-23`, and no images. It has been added to `assets/content.js`; `preview-20260623.html` was deleted. HTML asset query strings were refreshed to `bar-art-20260623-post3` so index/archive/tag pages load the updated article metadata.

Important publishing reminder: whenever `assets/content.js` changes for a new post, refresh the HTML asset query string on public pages in the same turn. On 2026-06-22, the article index was updated but the HTML pages initially still referenced the old query string, so the homepage/archive/tag pages could appear stale from browser cache.

2026-06-22 publication: user provided `C:\Users\Phil Lin\Desktop\临时用\日志.docx` with tag `生活日志`. The final article is `article-experiment-review-double-run.html`, title `实验和复习双开的一天`, publication date `2026-06-22`, and no extracted images. It has been added to `assets/content.js`; `preview-20260622.html` was deleted. HTML asset query strings were refreshed to `bar-art-20260622-post2` so index/archive/tag pages load the updated article metadata.

2026-06-22 publication: user provided `C:\Users\Phil Lin\Desktop\临时用\1.docx` with tag `生活日志`. The final article is `article-good-luck-day.html`, title `祝我好运的一天`, publication date `2026-06-21`, and no extracted images. It has been added to `assets/content.js`; `preview-20260621.html` was deleted.

## 1. One-Sentence Project State

`Phil Lin的Bar` is currently a static GitHub Pages personal site with a dark cocktail-bar visual style, metadata-driven article lists/tags, separate static article-file direction, two public articles, friend links, review placeholders, gallery placeholders, and no writer/editor feature.

2026-06-20 update: the site also has lightweight `tonight.html` and `playlist.html` pages, and the old 酒评 page has been reframed as Cellar / 酒柜.

2026-06-20 art completion update: the homepage now has a CSS-only rainy-glass/bar-counter atmosphere layer, stronger badge glow, richer menu-board material, and asset query string `bar-art-20260620-fix2`.

2026-06-20 cursor alignment update: `.bar-cursor` now centers on the pointer with `translate(...px, ...px) translate(-50%, -50%)`; asset query string was `bar-art-20260620-fix3`.

2026-06-20 acceptance rework: live GitHub Pages was checked and already had the pre-rework new navigation/home/reviews/about content from deployed `main` commit `2ec95306b342498f92bb8e4ac3d2e09f74310134`; local rework added explicit `900/720/480` responsive rules, reduced-motion/mobile motion suppression, Tonight/About copy refinements, reviews noscript fallback, and asset query string `bar-art-20260620-fix4`.

2026-06-20 cursor reentry/scroll fix: cursor placement now uses `syncCursorPosition()` / `moveCursor()`, clears `data-hidden` on fresh pointer movement, syncs on passive wheel/scroll, and current asset query string is `bar-art-20260620-fix5`.

2026-06-20 image asset recovery: disappearing badge and friend avatars were caused by corrupted bitmap files. Valid historical binaries were restored for all five bitmap assets in `assets/`, friend/badge references were cache-busted, and current asset query string is `bar-art-20260620-fix6`.

2026-06-20 playlist detail update: the six `夜间歌单` cards now link to six static detail pages with separate song lists; current asset query string is `bar-art-20260620-fix7`.

2026-06-21 cursor scroll-offset fix: removed transform movement from the `body` page-fade animation and changed `.bar-cursor` to update fixed `left` / `top` from viewport pointer coordinates; current asset query string is `bar-art-20260621-fix8`.

2026-06-21 mobile index polish: the homepage mobile layout now has compact nav pills, tighter hero spacing, reduced mobile decoration, and denser list-style menu cards; current asset query string is `bar-art-20260621-fix9`.

2026-06-21 homepage article menu simplification: the homepage menu is now a lighter seven-card board. Article/category entries are grouped into one `Martini Flight · 文章` card; the archive is `Martini · 文章`, and child variants are `Gibson · 生活日志`, `Dirty Martini · 一些思绪`, and `Vesper · 种草安利`. About now uses `Last Word · 关于我`; current asset query string is `bar-art-20260621-fix13`.

2026-06-21 tablet Index/glyph fix: tablet Index cards in the `721px` to `900px` range were restored to true card layout, while mobile/tablet drink glyph internals now keep the canonical `5.2rem` geometry and only use transform scaling; current asset query string is `bar-art-20260621-fix14`.

2026-06-21 Edge cursor effect fix: ambient motion now disables only for reduced motion or `max-width: 720px`, not `(pointer: coarse)` / `(hover: none)`, and `assets/site.js` has mouse event fallbacks alongside pointer events; current asset query string is `bar-art-20260621-fix15`.

2026-06-21 tablet home intro fix: the homepage `menu-intro` collapses to one column across `721px` to `1179px`, with horizontal kicker/buttons, to avoid iPad-sized screens squeezing copy into narrow vertical columns; asset query string at that time was `bar-art-20260621-fix16`.

## 2. Phase-One Completion Summary

2026-06-12 visual redesign update: the site now uses an abstract bar-menu concept. The home page is a menu board, each destination is paired with a cocktail, and secondary pages present a drink identity badge. Friend-link information and avatars must remain unchanged unless the user explicitly asks.

Phase one is sealed. Verified first-stage work includes:

- Site branding/navigation around `Phil Lin的Bar`.
- Cocktail/bar visual redesign using CSS glyphs and canvas constellations.
- Article archive with tag filtering.
- Three tag landing pages:
  - `tag-lab.html`
  - `tag-thoughts.html`
  - `tag-recommendations.html`
- Lightweight article metadata in `assets/content.js`.
- Placeholder public article `article-to-be-continue.html` deleted at user request.
- Friend page for StarCried and CrescentYves.
- Placeholder `酒评` and `摄影作品` pages.
- Removed writer/validation/editor pages and related code.
- Added context sealing files:
  - `AGENT_CONTEXT.md`
  - `AGENT_TODO.md`
  - `AGENT_CHANGELOG.md`
  - `AGENT_HANDOFF.md`

Follow-up after phase-one sealing:

- Deleted the placeholder article `To Be Continue` / `To Be Continued`.
- Cleared `window.BAR_POSTS` in `assets/content.js`.
- Added a right-side `吐槽` rail rendered from `window.BAR_GRIPES`.
- Published the first gripe with mood `烦恼`, emoji `😫`, and timestamp `2026-06-11 12:40:15`.
- Published the second gripe with mood `无语`, emoji `😶`, and timestamp `2026-06-12 12:29:58`.
- Published the third gripe with mood `迷幻`, emoji `😵‍💫`, and timestamp `2026-06-13 23:05:56`.
- Published the fourth gripe with mood `烦躁`, emoji `😤`, and timestamp `2026-06-15 12:27:20`.
- Published the fifth gripe with mood `烦躁`, emoji `😤`, and timestamp `2026-06-15 12:53:09`.
- Published the sixth gripe with mood `崩溃`, emoji `😭`, and timestamp `2026-06-15 14:03:23`.
- Published the seventh gripe with mood `崩溃`, emoji `😭`, and timestamp `2026-06-15 14:41:39`.
- Published the eighth gripe with mood `微醺`, emoji `🍸`, and timestamp `2026-06-17 00:57:39`.
- Published the ninth gripe with mood `无语`, emoji `😶`, and timestamp `2026-06-20 15:40:42`.
- Published the tenth gripe with mood `无语`, emoji `😶`, and timestamp `2026-06-20 15:42:08`.
- Published the eleventh gripe with mood `兴奋`, emoji `🤩`, and timestamp `2026-06-21 14:19:06`.
- Published the twelfth gripe with mood `自嘲`, emoji `🏃‍♂️`, and timestamp `2026-06-24 14:20:16`.

- Project-level preference localized from user request: skip visual verification by default unless the user explicitly asks later or a higher-priority instruction requires it.
- Abstract redesign follow-up:
  - Home menu pairings are grouped `Martini Flight · 文章`, plus `Gimlet · 今晚`, `Boulevardier · 酒柜`, `Sazerac · 夜间歌单`, `French 75 · 摄影作品`, `Tom Collins · 友链`, and `Last Word · 关于我`. The article child variants are `Gibson · 生活日志`, `Dirty Martini · 一些思绪`, and `Vesper · 种草安利`.
  - Article detail pages use `Martini · 文章正文`, matching the article archive's Martini identity.
  - Keep `assets/starcried-avatar.png` and `assets/crescentyves-avatar.jpg` for friend links.
  - User cancelled screenshot generation and will review by opening local `.html` files directly.
  - Follow-up homepage refinement removed the orphaned final tile by making the menu a strict 4-by-2 grid and grouping Friends/recent-posts in a `home-followup` section.
  - User later clarified Friends/recent-posts should not get a special new layout; that area was restored to the original `split-section` structure. Keep the strict 4-by-2 menu and expanded abstract alcohol motifs.
  - Latest refinement adds a `menu-emblem` beside the home title and more recognizable drink-glyph details: liquid, ice, bubbles, garnish, citrus/olive, foam, and stirring-spoon cues.
  - Generated badge image lives at `assets/bar-badge.png`; it replaces the old text `B` brand mark and is also used beside the home heading.
  - Latest title/glyph refinement replaced the oversized home heading badge with a smaller `menu-kicker`, and changed Paper Plane from a loose plane icon into a coupe cocktail with folded-paper garnish.
  - Background decision: use A+E, meaning dark menu-paper texture plus restrained cocktail-blueprint linework. Temporary D/E preview files were deleted.
  - Visual bugfix: the five vertical lines on subpage headings came from sharing the homepage recipe-tick strip with `.drink-heading::before` and `.article-header::before`; keep that strip homepage-only.
  - Visual bugfix: subpage drink icons should use full glyph geometry scaled uniformly in `.drink-portrait`; do not shrink the internal glyph span dimensions directly.
  - Current subpage drink badge is intentionally larger: `.drink-portrait` font size `0.95rem`, icon frame `4.55rem`, glyph scale `0.72`.
  - Responsive glyph bugfix: mobile/tablet breakpoints should keep `.drink-glyph > span` at `5.2rem` square and only alter `transform: scale(...)`; shrinking the internal box causes cocktail pseudo-elements to drift.
  - Tablet Index layout bugfix: the `721px` to `900px` breakpoint should restore menu cards to card-style layout instead of inheriting the phone list-card grid.
  - Tablet Index intro bugfix: across `721px` to `1179px`, `.menu-intro` should be single-column with a horizontal `menu-kicker`; the desktop three-column intro starts above `1179px`.
  - Posts archive and tag-page card titles should remain visually uniform across all cards.
  - Public page particle-toggle buttons use `切换烛光微粒` with the `✦` icon.
  - Latest style strengthening added `今晚`, `酒柜`, and `夜间歌单` navigation entries while keeping the static site architecture.
  - `tonight.html` combines Now / Aftertaste style status fragments.
  - `playlist.html` records music and film atmosphere references without lyrics, autoplay, or embedded players.
  - `reviews.html` now renders Cellar / 酒柜 cards from `window.BAR_REVIEWS`.
  - `酒鬼医学生` should remain a restrained self-aware line in about/footer/description areas, not the homepage's main visual label.
  - Latest art pass added homepage atmosphere spans (`hero-atmosphere`, `atmo-rain`, `atmo-bottle`, `atmo-window`, `atmo-counter`) and CSS-only rainy glass/bar counter treatment. Keep these lightweight and avoid replacing them with heavy background images unless explicitly requested.
  - Pointer-following `.bar-cursor` should keep its `translate(-50%, -50%)` centering transform; otherwise the ring appears down/right of the actual pointer.
  - Cursor reentry and scroll recovery depends on clearing `cursor.dataset.hidden` inside the shared pointer movement path, not only on `window.pointerenter`.
  - Do not reintroduce transform-based page movement on `body` while `.bar-cursor` is a fixed child; it can recreate scroll-offset cursor drift.
  - Homepage mobile polish is intentionally scoped to small-screen media queries; avoid changing desktop/base menu-board rules unless the user explicitly asks.
  - Page drink badges should keep class, glyph, and visible English name aligned. Current newer section identities are `Gimlet · 今晚`, `Boulevardier · 酒柜`, `Sazerac · 夜间歌单`, `Martini · 文章`, `Gibson · 生活日志`, `Dirty Martini · 一些思绪`, `Vesper · 种草安利`, and `Last Word · 关于我`; French 75 remains for `摄影作品` and uses `french-75-glyph`, not `coupe-glyph`.
  - Image assets must be handled as binary files. Do not restore or copy PNG/JPG files through text-encoding paths; use binary-safe Git extraction or normal file copy.
  - Playlist detail pages should stay lightweight: no lyrics, no audio embeds, no autoplay, and no new dependency unless the user explicitly changes scope.
  - Reduced motion and mobile/coarse-pointer contexts should not create the canvas, custom cursor, or pointer animation listeners.
  - Edge cursor compatibility: do not use `(pointer: coarse)` or `(hover: none)` as a desktop ambient-motion kill switch; use reduced motion and compact width checks, with mouse event fallbacks kept beside pointer events.

## 3. Current Code State

- Static site only: no framework, no package manager, no backend, no database.
- Shared data:
  - `assets/content.js`
- Shared behavior:
  - `assets/site.js`
- Shared styling:
  - `assets/styles.css`
- Current abstract visual system:
  - CSS-only drink glyphs, dot fields, line grids, polygon overlays, and a menu-board home layout.
  - `assets/site.js` adds a pointer-following bar cursor and drink-name hover labels for menu items.
  - `assets/styles.css` now also includes shared Tonight, Playlist, Cellar, article-reading, mobile navigation, and reduced-motion polish.
- Current cache-busting query string is `bar-art-20260626-return`; it was updated after the 2026-06-26 Word article publish to avoid stale cached CSS/JS and metadata.
- Gripe rail:
  - `assets/gripes.js` stores static `window.BAR_GRIPES` entries; it currently contains twelve entries.
  - `assets/site.js` injects the rail and handles page-size calculation and pagination.
  - `assets/styles.css` positions the rail on the right for desktop and makes it responsive on narrower screens.
  - Current scale strategy is scheme 2: keep gripe data separate from `assets/content.js` and render only the current page.
  - If gripe count grows enough to make `assets/gripes.js` heavy, remind the user about scheme 3 or 4: paginated static files or JSON on-demand loading.
- Verification preference:
  - Skip browser visual verification by default for this project.
  - Use file-level checks, reference searches, syntax checks when available, and static reasoning.
  - Report residual visual risk when skipping visual checks after frontend changes.
  - Never claim visual verification unless it was actually performed.
  - Keep attempting Git checks and `node --check` syntax checks when relevant.
  - Do not use Node REPL as a routine fallback for blocked `node --check` or browser verification.
- Article architecture:
  - Home/archive/tag pages read summary metadata from `assets/content.js`.
  - Real article bodies should live in separate HTML files, for example `article-my-post.html`.
  - Public article entries include `article-not-yet-return.html`, `article-two-bottles-writing-touch.html`, and `article-first-words-on-the-bar.html`.
  - Future article images should go under `assets/posts/<article-id>/`.
- `article.html` remains as a dynamic compatibility fallback, but static article HTML files are the recommended primary path.

## 4. Current Git State

Verified:

- `.git/config` remote URL is `https://github.com/Phillin-lrz/Phillin-lrz.github.io.git`.
- `git status --short`, `git diff --stat`, and `git diff -- .` are available in the current shell as of 2026-06-20.

Current caution:

- The working tree may include uncommitted local changes from recent site updates.
- No commit or push was performed during the 2026-06-20 style strengthening pass.

Before any future work, run `git status --short` and `git diff --stat`.

## 5. Important File Index

- `AGENT_CONTEXT.md`: full phase-one context, decisions, constraints, risks.
- `AGENT_TODO.md`: actionable completed/pending/phase-two tasks and validation checklist.
- `AGENT_CHANGELOG.md`: file-by-file change log with verification limits and rollback notes.
- `README.md`: human-facing maintenance notes.
- `index.html`: home page.
- `posts.html`: article archive and tag filter UI.
- `tag-lab.html`: `生活日志` tag page.
- `tag-thoughts.html`: `一些思绪` tag page.
- `tag-recommendations.html`: `种草安利` tag page.
- `notes.html`: Hanky Panky / 吧台札记 index.
- `note-lab-after-exam-restlessness.html`: first published bar-note page.
- `note-lab-day-not-over.html`: short published bar-note page about staying in the lab to delay tomorrow.
- `article.html`: dynamic article fallback.
- `article-two-bottles-writing-touch.html`: second published article, tag `一些思绪`.
- `article-first-words-on-the-bar.html`: first published article, tag `一些思绪`.
- `article-not-yet-return.html`: 2026-06-26 published article, tag `一些思绪`.
- `_drafts/article-format-reference.html`: retained non-public format/reference draft.
- `friends.html`: friend links, currently StarCried and CrescentYves.
- `reviews.html`: Cellar / 酒柜 page, rendered from `window.BAR_REVIEWS`.
- `tonight.html`: Tonight / 今晚 lightweight status page.
- `playlist.html`: Playlist / 夜间歌单 lightweight atmosphere page.
- `gallery.html`: gallery placeholder page.
- `about.html`: about page.
  - Current contact email is `phillin.lrz0714@gmail.com`.
- `assets/content.js`: tags, article metadata, review metadata, and `window.BAR_NOTES` note metadata.
- `assets/gripes.js`: static gripe data.
- `assets/site.js`: canvas interaction and post rendering.
- `assets/styles.css`: shared visual system.
- `assets/posts/`: intended future article image folders.

## 6. Known Risks

- Git is currently available, but uncommitted local changes may be present.
- Browser visual verification was not completed in the final sealed state.
- Article archive, recent posts, and `一些思绪` tag page depend on `assets/content.js` loading successfully.
- `assets/cocktail-hero.png` and `assets/hero-workspace.png` appear present but currently unused; do not delete without user approval and reference search.
- `reviews.html` renders `BAR_REVIEWS`, but review metadata is still placeholder content.
- `article.html` can confuse future article flow; current preferred flow is separate static article HTML plus index entry.
- Large/base64 article images should not be placed in `assets/content.js`.

## 7. Suggested Phase-Two Entry

Do not start phase two automatically. First ask the user to confirm the exact next objective.

Likely phase-two entry if user confirms Word conversion:

1. Receive `.docx` file from user.
2. Extract text and images.
3. Choose article id/slug with user or use a safe generated slug.
4. Save images to `assets/posts/<article-id>/`.
5. Generate `article-<article-id>.html`.
6. Add metadata entry to `assets/content.js`.
7. Verify JS syntax and browser article rendering.

## 8. Must-Read Files For New Conversation

Read these before editing code:

1. `AGENT_HANDOFF.md`
2. `AGENT_CONTEXT.md`
3. `AGENT_TODO.md`
4. `AGENT_CHANGELOG.md`
5. `README.md`
6. `assets/content.js`
7. `assets/site.js`
8. `assets/styles.css`

## 9. Forbidden Immediate Actions In New Conversation

- Do not start phase-two development without user confirmation.
- Do not rely on chat history or auto summaries as the only source of truth.
- Do not reintroduce `write.html`, `editor.html`, or the `撰写` feature unless explicitly requested.
- Do not put full article bodies or base64 images into `assets/content.js`.
- Do not delete unused image assets without approval.
- Do not install dependencies or migrate frameworks without approval.
- Do not claim git diff/status/browser verification unless actually run successfully.
- Do not make broad refactors before reading the four AGENT files.

## 10. Recovery Steps

1. Read the four AGENT files.
2. Attempt:
   - `git status --short`
   - `git diff --stat`
   - `git diff -- .`
3. If Git is unavailable, record that limitation in the next report.
4. Run:
   - `node --check assets/site.js`
   - `node --check assets/content.js`
   - `node --check assets/gripes.js`
5. Search for writer feature leftovers:
   - `write.html`
   - `editor.html`
   - `write-link`
   - `data-auth`
   - `data-editor`
   - `WRITER`
   - `撰写`
6. Skip browser visual verification by project preference unless the user explicitly asks later or a higher-priority instruction requires it. If requested or required, browser-check local pages:
   - `index.html`
   - `posts.html`
   - one tag page
   - one public article page after a new article is added
   - `friends.html`
7. Ask the user what phase two should do.
