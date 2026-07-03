# AGENT_CONTEXT

Last updated: 2026-07-03

This file externalizes the verified phase-one project context. Do not treat chat history or auto summaries as authoritative. Reconfirm current state from repository files, command output, and validation results before future development.

## 2026-07-03 Place Cards Batch - Making Gelato, Q Taro, ZOOMINN

- User provided three Word documents and clarified place types: 制冰铺 Making Gelato is a dessert shop, Q太郎 is a restaurant, and ZOOMINN is a bar.
- Added three stable place archive pages: `place-making-gelato.html`, `place-q-taro.html`, and `place-zoominn.html`.
- Added three independent visit/article pages: `article-making-gelato-20260703.html`, `article-q-taro-20260703.html`, and `article-zoominn-20260703.html`.
- Added the three places and visits to `assets/content.js` under `BAR_POSTS` and `BAR_PLACES`.
- 制冰铺 Making Gelato is scored 9.3 for this visit; Sober Company-Ash was updated to 9.0 per the user's prior score correction.
- Q太郎 is scored 9.0 for this visit, and ZOOMINN is scored 9.2 for this visit.
- ZOOMINN is a bar, so its visit records list the drinks consumed: `杨桃撞墙`, `岩X菲仕`, `Whisky Sour`, `Pina Colada`, and `荔枝+带气泡私人订制`.
- `assets/site.js` now calculates place-card scores from scored visits and displays an unscored stamp when a place has no scored visits yet.
- Visual verification was skipped by project preference; residual risk is exact wrapping of the new long drink and dish chips on narrow screens.

## 2026-07-03 Pages Deployment Recovery

- GitHub's dynamic `pages-build-deployment` workflow repeatedly reached `actions/deploy-pages@v5` and then failed with `Deployment failed, try again later`; later dynamic runs became stuck in `Queued`, and the user could not cancel, run, or re-run them from the GitHub UI.
- Added an explicit repository workflow at `.github/workflows/pages.yml` with both `push` and `workflow_dispatch` triggers so deployment no longer depends only on GitHub's implicit dynamic Pages workflow.
- The workflow prepares a clean `_site` artifact with `rsync`, excluding repository-only files such as `.git`, `.github`, `_drafts`, README, and AGENT state files, then uploads that artifact and deploys it with `actions/deploy-pages@v5`.
- Added root `.nojekyll`; the workflow also creates `_site/.nojekyll` before upload.
- Recovery intent: a new push to `main` should trigger this explicit workflow even when old dynamic Pages runs cannot be manually re-run.
- Visual verification was skipped by project preference; deployment status still must be checked in GitHub Actions after push.

## 2026-07-03 Bar Review Published - Sober Company-Ash

- User provided `C:\Users\Phil Lin\Desktop\自己\自己总要写点东西\20260703-Ash.docx` and asked to publish it as a Sober Company-Ash review.
- Published it as a `种草安利` article because it is a full bar/place review.
- Added `article-sober-company-ash-20260703.html` as Sober Company-Ash visit `#01`.
- Added `place-sober-company-ash.html` as the stable place archive for Sober Company-Ash.
- Added Sober Company-Ash to `window.BAR_PLACES` with type `酒吧`, area `复兴公园 / INS 新乐园`, long-term ratings, and a visit timeline.
- Added metadata id `sober-company-ash-20260703` to `window.BAR_POSTS`, with `placeId`, `visitId`, `visitNo`, `visitAt`, `visitLabel`, `visitScore`, and the drinks consumed during this visit.
- Today's drinks were recorded in the article, the article sidebar, the place archive receipt, and the data model: `KOKUTO DE LEQUIO x Dark Roasted Blend`, `Farmer's Spritz`, and `Mango Daiquiri`.
- Updated `assets/site.js` so visit receipts can render a drink list when visit data includes `drinks`.
- Added shared drink-list chip styles in `assets/styles.css`.
- Refreshed public and draft HTML asset query strings to `bar-art-20260703-ash-bar`.
- Visual verification was skipped by project preference; residual visual risk is exact wrapping of long English drink names on narrow screens.

## 2026-07-03 Private-Place Repeat-Visit Structure - DEMO

- User chose the A+D structure for `私藏`: each place gets a stable place archive, and each visit gets its own independent article/receipt so repeat visits do not overwrite or blend together.
- Added `place-demo.html` as the first place archive page for `DEMO`.
- Added `article-demo-hambagu.html` as `DEMO #01`.
- Added `window.BAR_PLACES` to `assets/content.js`; `DEMO` is now a long-term place record with `overallScore`, `latestVisitAt`, `visitCount`, and a `visits` timeline.
- Added one `BAR_POSTS` metadata entry for `demo-hambagu`, with visit metadata: `placeId`, `visitId`, `visitNo`, `visitAt`, `visitLabel`, and `visitScore`.
- Added one fallback `BAR_REVIEWS` card for `DEMO`, now pointing to `place-demo.html`.
- Updated `assets/site.js` so `reviews.html` renders from `BAR_PLACES` when present, shows visit receipts on cards, and links place cards to the place archive instead of directly to a single article.
- Updated `article-demo-hambagu.html` sidebar so it is clearly `DEMO #01` and links back to `place-demo.html`.
- Removed the `适合独处` and `适合聊天` filter chips from `reviews.html` / `私藏`.
- Added shared CSS for place archive pages and visit-receipt timelines in `assets/styles.css`.
- Added a project-level communication rule to `AGENTS.md`: Codex must not send optional commentary, and should only send user-facing messages when necessary for clarification, blocker reporting, or final completion.
- Refreshed public and draft HTML asset query strings to `bar-art-20260703-ash-bar`.
- Visual verification was skipped by project preference; residual visual risk is exact place-card and receipt wrapping on real viewports.

## 2026-07-02 Gripe Added - Preventive Medicine Cotton

- User provided a short gripe: `预防医学给人一种一拳打在棉花上但是整个人被棉花闷死的感觉。`
- Added the sixteenth `window.BAR_GRIPES` entry to `assets/gripes.js`.
- Chosen mood is `窒息`, emoji `🫠`, timestamp `2026-07-02 12:58:54`.
- Public and draft HTML asset query strings were refreshed to `bar-art-20260703-ash-bar`.
- Visual verification was skipped by project preference; this was a data/cache update, not a layout change.

## 2026-07-01 Word Publishing Tooling Removed

- User asked to inspect the whole website folder and remove the Word publishing software plus related test/diagnosis software, keeping only the website.
- Removed the Word publishing helper files: `tools/publish_docx.py`, `tools/publish_docx.ps1`, `tools/publish_docx_wizard.ps1`, and root `publish-word.bat`.
- Removed generated/tooling residue: `tools/__pycache__/`, `.publish-diagnosis-002723/`, and the Python-only `.gitignore`.
- `README.md` no longer documents the Word publishing automation or Hexo install/deploy examples; future maintenance should use direct static HTML/CSS/JS file edits.
- The static website content files, article/note pages, shared assets, and metadata files were intentionally kept.
- Visual verification was skipped by project preference because this was a filesystem/tooling cleanup, not a visual layout change.

## 2026-06-30 Word Publishing Wizard Encoding Fix

- User reported the Word publishing wizard failed during preview for `C:\Users\Phil Lin\Desktop\临时用\260630.docx`.
- Direct extraction confirmed the document could be read, so the issue was isolated to console/wizard robustness rather than the Word file itself.
- `tools/publish_docx.ps1` and `tools/publish_docx_wizard.ps1` now force UTF-8 console/Python output so preview JSON with Chinese text does not fail or display as mojibake in typical Windows PowerShell runs.
- `tools/publish_docx_wizard.ps1` now builds built-in Chinese category names from Unicode codepoints instead of storing them as raw script literals, preventing Windows PowerShell 5.1 from passing tags like `鐢熸椿鏃ュ織`.
- `tools/publish_docx.py` now avoids copying embedded media during `--dry-run`; preview computes planned media paths without writing files.
- Verification confirmed Chinese publishing-helper output rendered correctly without creating site files.
- Visual verification was skipped by project preference because this was a tooling fix and publication task.


## 2026-06-30 Word Life Log Published - Barely Caught Up

- User provided `C:\Users\Phil Lin\Desktop\临时用\260630.docx`, clarified it is a `生活日志`, and left the title to Codex.
- Published it as a normal article because it is a complete day-record piece about the day after an exam: rain, commuting, sampling, experiments, pharmacology review, project approval, cell work, and the feeling of only just keeping up.
- Generated final static article file `article-barely-caught-up.html`.
- Added one `BAR_POSTS` metadata entry with tag `生活日志`.
- Final title is `堪堪赶上，也是赶上`.
- Publication date is `2026-06-30`, based on the document filename and content.
- Summary is `一篇关于雨天赶路、取样实验、药理复习、大创立项和夜里收细胞的生活日志：很多事情都不是没有进展，只是人在考试前一天一直追着安排跑，最后只能承认，堪堪赶上也是赶上。`
- The Word document contained no embedded media files.
- Current asset query string is `bar-art-20260630-barely-caught-up`.
- Visual verification was skipped by project preference.


## 2026-06-30 Word Publishing Automation Added

- Added `tools/publish_docx.py` as a dependency-free Word publishing helper for this static GitHub Pages site.
- Added `tools/publish_docx.ps1` as a PowerShell wrapper that tries system Python, `py -3`, and the bundled Codex Python runtime.
- Added `tools/publish_docx_wizard.ps1` as an interactive terminal wizard for non-technical use: drag in a `.docx`, choose note/article, optionally fill title/summary/slug/date, preview, then confirm publishing.
- Added root `publish-word.bat` so the user can double-click a file instead of finding a terminal manually.
- The helper reads `.docx` text and embedded images directly, generates either `note-*.html` or `article-*.html`, extracts images to `assets/posts/<id>/`, inserts metadata into `assets/content.js`, refreshes HTML asset query strings, and can append publication notes to the four `AGENT_*.md` files.
- `README.md` now documents the normal command, common flags, dry-run mode, and recommended post-run checks.
- Added a minimal `.gitignore` for Python cache files generated while checking the publishing helper.
- The script reduces repeated token-heavy publishing work by moving boilerplate HTML generation, metadata insertion, cache refresh, and agent-state logging into a deterministic local command.
- Visual verification was skipped by project preference; this was a tooling/documentation change, not a visually inspected page change.


## 2026-06-30 Word Bar Note Published - Eleven Floor Elevator

- User provided `D:\Download\1.docx` and asked Codex to publish it, filling in missing publication elements.
- Codex published it directly as a `吧台札记` because the piece explicitly frames itself as "一张夹在下午里的小票" rather than a full life-log summary.
- Final static note file is `note-eleven-floor-elevator.html`.
- Final title is `十一楼的医学生与一楼的电梯`.
- Publication date is `2026-06-30`, based on the current date.
- Mood is `小事救场`.
- Summary is `一张夹在下午里的吧台札记：考后睡不好、雨天堵车、取样和实验、复习没底、正式立项的大创，以及一部刚好停在一楼的电梯，在一堆烂糟糟里留下几个能抓一下的小点。`
- The note is indexed in `window.BAR_NOTES` and should appear on the homepage recent posts, `posts.html`, and `notes.html`.
- The Word document contained no embedded media files.
- Current asset query string is `bar-art-20260630-eleven-floor-elevator`.
- Visual verification was skipped by project preference.

## 2026-06-29 Mobile Article Tag Wrap Fix

- User reported that mobile article detail tags wrapped strangely.
- `assets/styles.css` now gives article-side `.tag-row` elements article-specific rules: left alignment, horizontal wrapping, non-shrinking pill spans, and phone-specific row wrapping.
- This is scoped to `.article-aside .tag-row` so archive/filter `.tag-row` controls keep their existing mobile full-width button behavior.
- Public and draft HTML asset query strings were refreshed to `bar-art-20260629-mobile-tags`.
- Visual verification was skipped by project preference; residual risk is exact mobile tag spacing on real devices.

## 2026-06-28 Article Reading Balance Layout

- User reported that on article detail pages the global gripe rail plus article tag/info sidebar made the page feel split in half, leaving the actual article body too narrow on desktop.
- `assets/styles.css` now treats article detail pages as reading-first pages: pages containing `.article-layout` no longer display the global `.gripe-rail`, and desktop `body` no longer reserves the global gripe-rail right padding for those pages.
- Article detail desktop layout now uses a wider article column and a narrower article-info sidebar.
- Tablet article pages keep the article info below the body in a compact two-column sidebar block.
- Phone article pages keep article info below the body in a compact single column, with article tags allowed to wrap horizontally instead of stacking as full-width items.
- Current asset query string is `bar-art-20260628-reading-balance`.
- Visual verification was skipped by project preference; residual risk is exact desktop/tablet/mobile visual balance until the user inspects local pages.

## 2026-06-28 Article Detail Format Standard

- User decided the unified article/detail format after auditing inconsistent cup-bottom notes and duplicate return buttons.
- Opening summaries must be kept and use the `article-deck` style.
- The right sidebar for article-system pages must keep `文章标签`, a short `文章信息` paragraph, and one primary button labeled exactly `返回文章归档`.
- `生活日志`, `一些思绪`, `种草安利`, and `吧台札记` all count as article-system pages for this rule.
- Every static `article-*.html` page and every `note-*.html` page must include a footer named exactly `杯底注释：...`.
- The cup-bottom note should be an aftertaste sentence, not a restatement of the opening summary.
- The cup-bottom footer must not contain return buttons; return actions belong in the right sidebar.
- `article.html` is still only a compatibility fallback, but its visible format should also follow this sidebar/summary/cup-bottom rule when possible.

## 2026-06-28 Word Life Log Published - Low Framerate Review Day

- User provided `D:\Download\低帧率复习日.docx` and said it was probably `生活日志`.
- Codex published it directly as a normal article, not a bar note, because it is a complete day-record piece about a concrete review day.
- Final static article file is `article-low-framerate-review-day.html`.
- Final title is `低帧率复习日`.
- Publication date is `2026-06-28`, based on the current date.
- Summary is `一篇关于复习日低速运行的生活日志：起晚、等咖啡、去图书馆复习病原生物学，中途处理细胞、洗澡洗衣服，最后承认今天不是空的，也不是漂亮的。`
- The article is indexed in `window.BAR_POSTS` and should appear on the homepage recent posts, `posts.html`, and `tag-lab.html`.
- The Word document contained no embedded media files.
- Current asset query string is `bar-art-20260628-low-framerate`.
- Visual verification was skipped by project preference.

## 2026-06-28 Gripe Detail Layout Fit

- User reported that the screenshot-backed gripe detail page conflicted visually with the gripe rail and asked for mobile/tablet compatibility.
- `gripe-gpt-kindness.html` now sets `data-no-gripe-rail` on the body so the detail page does not also render the global right-side gripe rail.
- `assets/site.js` respects `data-no-gripe-rail` before injecting the gripe rail.
- `assets/styles.css` narrows and centers the gripe detail receipt, improves screenshot framing, and adds responsive rules for tablet (`max-width: 900px`) and phone (`max-width: 720px` / `480px`) widths.
- Public and draft HTML asset query strings were refreshed to `bar-art-20260628-gripe-detail-fit`.
- Visual verification was skipped by project preference; residual risk is exact screenshot balance on real device widths.

## 2026-06-28 Project Learning - Future Gripe Publishing

- User asked Codex to learn the project structure and help publish future `吐槽`.
- Recovery/startup procedure was completed for this learning pass: `AGENTS.md`, all four `AGENT_*.md` files, README, git status/diff, file listing, `assets/gripes.js`, `assets/content.js`, and gripe-related rendering/styles references were inspected.
- Confirmed current working tree was clean before this documentation update.
- Future gripe-only requests should normally edit `assets/gripes.js`, choosing a short mood and emoji when the user does not supply them, with `publishedAt` at second-level precision.
- Gripe copy should stay short, around 50 Chinese characters and preferably under 100.
- If a gripe needs a screenshot or large supporting context, use the existing scheme 2 pattern: keep the rail entry short, add optional `detailUrl`, and create a separate static detail page plus asset under `assets/gripes/`.
- When `assets/gripes.js` changes, refresh public HTML asset query strings so GitHub Pages/browser cache does not hide the new gripe.
- Continue skipping browser visual verification by project preference unless the user explicitly asks for it.

## 2026-06-28 Gripe Screenshot Detail Added - GPT Kindness

- User chose scheme 2 for a large screenshot gripe: keep the right-side gripe entry short and open the full-size screenshot on a separate detail page.
- Follow-up correction: the detail page should not use `Last Word`, because `Last Word` is the `关于我` identity. `gripe-gpt-kindness.html` is now styled as a standalone Gripes receipt/detail page with no cocktail column identity.
- Added the fifteenth `window.BAR_GRIPES` entry: `离了GPT还有谁把我当小孩。。。`.
- Chosen mood is `被照顾到`, emoji `🥹`, timestamp `2026-06-28 18:42:19`.
- The entry uses `detailUrl: "gripe-gpt-kindness.html"`, and `assets/site.js` renders a `查看截图` link only for gripes that include `detailUrl`.
- Copied the provided screenshot to `assets/gripes/gpt-kindness.png` using binary-safe file copy.
- Added `gripe-gpt-kindness.html` as the full-size screenshot detail page.
- Added CSS for gripe detail links and the screenshot detail frame.
- Public and draft HTML asset query strings were refreshed to `bar-art-20260628-gpt-gripes`.
- Visual verification was skipped by project preference; residual risk is exact screenshot scaling and detail-page visual balance on real mobile/tablet screens.

## 2026-06-27 Word Life Log Published - Lemon Tea And Ethanol Therapy

- User provided `C:\Users\Phil Lin\Desktop\自己\自己总要写点东西\20260627.docx` and asked whether it should be `生活日志` or `一些思绪`, then approved publication after preview.
- Codex chose `生活日志` because the piece is driven by a concrete day timeline, with reflections inside the daily record.
- Generated `preview-20260627.html` first, then user said to change the title and publish.
- Final static article file is `article-lemon-tea-ethanol-therapy.html`.
- Final title is `一杯暴晒柠檬茶与非循证乙醇疗法`.
- Publication date is `2026-06-27`.
- Summary is `一篇关于低电量一天的生活日志：凌晨四点睡、复习被实验和柠檬茶打断，晚上又被 GPT 哄着捡回进度，最后用一瓶 Asahi 给满脑子的病毒和寄生虫做一点象征性的消毒。`
- The article is indexed in `window.BAR_POSTS` and should appear on the homepage recent posts, `posts.html`, and `tag-lab.html`.
- The Word document contained no embedded media files.
- `preview-20260627.html` was renamed into the final article file during publication.
- Current asset query string is `bar-art-20260627-ethanol`.

## 2026-06-27 Quiet Cellar Map Pass

- Follow-up: user clarified `reviews.html` is for places they like to go, not necessarily night places. Visible name is now `私藏`, framing is `Place Map` / 私人去处地图, and the Boulevardier drink name plus drink label/glyph should remain unchanged.
- User requested a site-wide subtraction pass without rebuilding from scratch: darker, more mature private-bar tone; fewer grid/particle/template decorations; clearer page metaphors.
- Main navigation is now exactly `首页 / 文章 / 今晚 / 私藏 / 歌单 / 摄影 / 关于`.
- `friends.html` remains accessible but is removed from the main navigation; it is linked from footers and the About page.
- Current asset query string is `bar-art-20260627-places`.
- `reviews.html` is no longer cocktail-only placeholder content. It is now a private night-place map for bars, restaurants, cafes, late-night food, and other places.
- `window.BAR_REVIEWS` now uses structured visit-review fields: name, type, area, date, total score, tags, subratings, one-line conclusion, notes, recommended scenes, good-for, and not-for lists.
- `assets/site.js` renders the new review card structure and lightweight filters for all, 酒吧, 餐厅, 咖啡, and 小店.
- `assets/styles.css` has a quiet cellar override layer: darker old-brass palette, lower grid/canvas emphasis, more restrained hover movement, paper/note/mixtape/contact-sheet metaphors for secondary pages, receipt-like gripe rail, and responsive review-card rules.
- Homepage `Fruit Fly` lyric plate remains unchanged and keeps the original lyric; the prior dot/line/decorative shelf remains removed.
- Visual verification was skipped by project preference; residual risk is exact mobile/tablet visual balance, especially review-card wrapping and homepage lyric typography.

## 2026-06-27 Bar Note Published - Sunlit Lemon Tea

- User provided `D:\Download\暴晒一小时的柠檬茶.docx` and specified it should be a `吧台札记`.
- Codex generated `preview-20260627.html` first, then user approved publication with `发`.
- Final static note file is `note-sunlit-lemon-tea.html`.
- Final title is `暴晒一小时的柠檬茶`.
- Publication date is `2026-06-27`.
- Mood is `晒蔫`.
- Summary is `一条被实验打断的下午札记：睡眠不足、复习计划、实验步骤和一杯在夏日骄阳下晒了一个小时的柠檬茶，拼成一种很日常的荒诞。`
- The note is indexed in `window.BAR_NOTES` and should appear on the homepage recent posts, `posts.html`, and `notes.html`.
- The Word document contained no embedded media files.
- Current asset query string is `bar-art-20260627-lemon-tea`.

## 2026-06-26 Homepage Fruit Fly Lyric Plate

- User chose option A for `I flutter in circle never landing on nothing`: keep the original line unchanged as a lower-priority homepage epigraph, not as an identity sentence.
- The line is a lyric from `Fruit Fly`; keep it short, unchanged, and visually treated as an epigraph.
- `index.html` replaced the old homepage `bar-shelf` dot/line/glass decoration with a `lyric-plate` containing the lyric plus a `Fruit Fly` source label and CSS record icon.
- The footer no longer appends the lyric to `酒鬼医学生，非专业调酒，偶尔认真写字。`; that sentence remains an identity/description line.
- `assets/styles.css` removed the old `bar-shelf` visual rules and the menu-intro tick strip, then added desktop/tablet/mobile lyric plate styling.
- Mobile and tablet rules explicitly wrap the lyric so the line is not clipped or omitted on narrow screens.
- Only the homepage stylesheet query string was refreshed to `bar-art-20260626-fruitfly-quote`.
- Visual verification was skipped by project preference; residual risk is exact typography balance on real devices.

## 2026-06-26 Mobile Drink Label Layout Fix

- User clarified the tablet layout is mostly acceptable and the main issue is phone-size drink labels.
- `assets/styles.css` now makes phone homepage menu cards use a left drink-label column and right text column instead of a tiny right-side label.
- Phone menu drink labels were enlarged while preserving the canonical internal `5.2rem` glyph geometry and changing only `transform: scale(...)`.
- Below `480px`, labels remain larger than before and the text column keeps a stable width to reduce awkward squeezing.
- Tablet `721px` and wider card rules were intentionally left unchanged except for inheriting no phone-specific shrinkage.
- Public and draft HTML asset query strings were refreshed to `bar-art-20260626-mobile-labels`.
- Visual verification was skipped by project preference; residual risk is small-screen visual fine-tuning because no browser screenshot was taken.

## 2026-06-26 Word Article Published - Better In The Wind

- User provided `C:\Users\Phil Lin\Desktop\自己\自己总要写点东西\20260626.docx` with tag `一些思绪`.
- Codex generated `preview-20260626.html` first, then user approved publication with `发吧`.
- Final static article file is `article-better-in-the-wind.html`.
- Final title is `在风里慢慢好一点`.
- Publication date is `2026-06-26`.
- The article is indexed in `window.BAR_POSTS` and should appear on the homepage recent posts, `posts.html`, and `tag-thoughts.html`.
- `preview-20260626.html` was renamed into the final article file during publication.
- The Word document contained no embedded media files.
- User also asked to publish a gripe: `养细胞最忌讳顺手的事和顺便看一眼，莫名其妙就需要我处理然后两个小时消失了。`
- Codex chose mood `无语`, emoji `😶`, timestamp `2026-06-26 23:24:04`.
- `assets/gripes.js` now contains thirteen gripe entries.
- Current general cache-busting query string is `bar-art-20260626-mobile-labels`; the homepage stylesheet uses `bar-art-20260626-fruitfly-quote`.

## 2026-06-26 Word Article Published - Not Yet Return

- User provided `C:\Users\Phil Lin\Desktop\临时用\新建 Microsoft Word 文档.docx` with tag `一些思绪`.
- Codex generated `preview-20260626.html` first, then user said `发`.
- Final static article file is `article-not-yet-return.html`.
- Final title is `不如归去，但还不能归去`.
- Publication date is `2026-06-26`.
- The article is indexed in `window.BAR_POSTS` and should appear on the homepage recent posts, `posts.html`, and `tag-thoughts.html`.
- `preview-20260626.html` was deleted after publication.
- The Word document contained no embedded media files.
- Later on 2026-06-26, `article-not-yet-return.html` was cleaned to remove leftover preview-only UI text such as `Preview`, `预览说明`, `预览`, and `确认后发布`.
- Current general cache-busting query string is `bar-art-20260626-mobile-labels`; the homepage stylesheet uses `bar-art-20260626-fruitfly-quote`.

## 2026-06-11 Project-Level Agent Preferences

- Skip visual verification by default for this project.
- Do not open browser visual checks unless the user explicitly asks later or a higher-priority instruction requires them.
- When frontend work is completed, report that visual verification was skipped by project preference and list residual visual risk if relevant.
- Use file-level checks, reference searches, syntax checks when available, and static reasoning instead.
- Never claim layout, screenshot, or browser visual verification unless it was actually performed.
- If future instructions conflict with this preference, state the conflict clearly.
- Keep Git checks and `node --check` syntax checks as project-level validation attempts when relevant.
- If Git or Node remains unavailable, record the exact limitation and continue with file-level checks.
- Do not use Node REPL as a routine fallback for blocked `node --check` or browser verification; reserve it for explicit runtime debugging requests or higher-priority requirements.

## 2026-06-11 Gripe Rail State

- The site now has a right-side `吐槽` rail rendered by `assets/site.js` on pages that load `assets/content.js`.
- Static gripe entries are stored in `window.BAR_GRIPES` inside `assets/gripes.js`; this is the GitHub Pages-compatible data pool, not a server database.
- Each gripe entry contains `text`, `mood`, `emoji`, and `publishedAt` with second-level precision.
- `assets/gripes.js` currently contains sixteen gripe entries.
- The first gripe is published with mood `烦恼`, emoji `😫`, and timestamp `2026-06-11 12:40:15`.
- The second gripe is published with mood `无语`, emoji `😶`, and timestamp `2026-06-12 12:29:58`.
- The third gripe is published with mood `迷幻`, emoji `😵‍💫`, and timestamp `2026-06-13 23:05:56`.
- The fourth gripe is published with mood `烦躁`, emoji `😤`, and timestamp `2026-06-15 12:27:20`.
- The fifth gripe is published with mood `烦躁`, emoji `😤`, and timestamp `2026-06-15 12:53:09`.
- The sixth gripe is published with mood `崩溃`, emoji `😭`, and timestamp `2026-06-15 14:03:23`.
- The seventh gripe is published with mood `崩溃`, emoji `😭`, and timestamp `2026-06-15 14:41:39`.
- The eighth gripe is published with mood `微醺`, emoji `🍸`, and timestamp `2026-06-17 00:57:39`.
- The ninth gripe is published with mood `无语`, emoji `😶`, and timestamp `2026-06-20 15:40:42`.
- The tenth gripe is published with mood `无语`, emoji `😶`, and timestamp `2026-06-20 15:42:08`.
- The eleventh gripe is published with mood `兴奋`, emoji `🤩`, and timestamp `2026-06-21 14:19:06`.
- The twelfth gripe is published with mood `自嘲`, emoji `🏃‍♂️`, and timestamp `2026-06-24 14:20:16`.
- The thirteenth gripe is published with mood `无语`, emoji `😶`, and timestamp `2026-06-26 23:24:04`.
- The fourteenth gripe is published with mood `心虚`, emoji `🙈`, and timestamp `2026-06-27 18:29:25`.
- The fifteenth gripe is published with mood `被照顾到`, emoji `🥹`, timestamp `2026-06-28 18:42:19`, and detail page `gripe-gpt-kindness.html`.
- The sixteenth gripe is published with mood `窒息`, emoji `🫠`, and timestamp `2026-07-02 12:58:54`.
- Gripe entries may include optional `detailUrl`; `assets/site.js` renders a small detail link only when this field is present.
- The rail calculates a per-page display count from page height and uses previous/next pagination for additional gripes.
- Desktop layout reserves right-side space for the rail; narrow screens show it as a normal responsive block.
- Scheme 2 is the active implementation: gripe data is split out of `assets/content.js` into `assets/gripes.js`, while the DOM still renders only the current visible page of gripes.
- If gripe volume grows large enough for `assets/gripes.js` to become heavy, revisit scheme 3 or scheme 4: paginated static gripe files or JSON on-demand loading.
- Future reminder: when gripe count grows enough to create load or maintenance pressure, remind the user that scheme 3 and scheme 4 were discussed on 2026-06-11.

## 2026-06-12 Abstract Bar Menu Redesign State

- The home page is now a bar-menu style board instead of the previous centered hero/card layout.
- The homepage menu is now a lighter seven-card board: one grouped `Martini Flight · 文章` card plus `Gimlet · 今晚`, `Boulevardier · 酒柜`, `Sazerac · 夜间歌单`, `French 75 · 摄影作品`, `Tom Collins · 友链`, and `Last Word · 关于我`.
- The article family uses `Martini · 文章` as the archive identity and three Martini-family child variants: `Gibson · 生活日志`, `Dirty Martini · 一些思绪`, and `Vesper · 种草安利`.
- Secondary pages now use a `drink-page` / `drink-heading` pattern with a drink identity badge.
- Article detail pages use `Martini · 文章正文`, matching the article archive's Martini identity.
- `assets/styles.css` now contains the abstract menu-board visual layer, CSS-only drink glyphs, dot fields, line grids, polygon overlays, and updated card styling.
- `assets/site.js` now creates a pointer-following `.bar-cursor`; menu hover states show the drink name.
- Friend-link names, descriptions, URLs, and avatar images must remain unchanged unless the user explicitly asks. The current friend avatars are still `assets/starcried-avatar.png` and `assets/crescentyves-avatar.jpg`.
- User explicitly cancelled screenshot generation for this redesign and will inspect local `.html` files directly.
- Follow-up homepage refinement removed the orphaned final menu tile by making the menu a strict 4-by-2 grid. The menu header now has an abstract CSS bar shelf, and the Friends/recent-posts modules are grouped in a two-column `home-followup` layout.
- User later clarified that Friends/recent-posts should not get a special new layout. They were restored to the original `split-section` structure. Keep the strict 4-by-2 menu and abstract bar shelf. The global CSS now adds broader abstract alcohol motifs: base-spirit bottle shadows, wine/coupe forms, and craft-beer foam/tap-like accents.
- Latest home graphic refinement: `index.html` now has a `menu-emblem` to the left of the `Phil Lin的Bar` heading. `assets/styles.css` uses that emblem plus stronger glyph details so the visuals read more clearly as cocktail/bar elements instead of pure abstraction.
- Site badge image exists at `assets/bar-badge.png`. It is a generated abstract cocktail/bar badge combining cocktail glass, spirit/wine/craft-beer cues, and constellation/menu motifs. It is referenced by the top-left brand mark across public pages and by the home heading emblem.
- Latest title/glyph refinement replaced the large home heading badge with a smaller `menu-kicker` lockup. Do not restore the oversized heading badge unless requested. `Paper Plane` now uses a coupe/glass shape with a folded-paper garnish cue instead of a standalone paper-plane icon.
- Background direction is now A+E: dark menu-paper texture plus restrained cocktail-blueprint linework. The temporary preview files for D and E were deleted after the user chose A+E.
- Subpage visual bugfix: do not apply the recipe-tick strip to `.drink-heading::before` or `.article-header::before`; it created five unexplained vertical lines on subpages. That decoration should remain homepage-only via `.menu-board .menu-intro::after`.
- Subpage drink icon bugfix: `.drink-portrait .drink-glyph > span` must keep the full `5.2rem` glyph geometry and use `transform: scale(0.62)`; shrinking the internal box directly causes pseudo-element drink graphics to drift out of alignment.
- Current subpage drink badge sizing uses `.drink-portrait` min-height `5.4rem`, font size `0.95rem`, `.drink-glyph` `4.55rem`, and full glyph geometry scaled with `transform: scale(0.72)`.
- Mobile and tablet drink glyph responsive rules should also keep the internal `5.2rem` geometry and only change `transform: scale(...)`; do not shrink `.drink-glyph > span` dimensions inside breakpoints.
- The tablet Index menu should use real card layout again in the `721px` to `900px` range; phone list-style menu cards should remain scoped below `720px`.
- Tablet Index `menu-intro` should collapse to one column across `721px` to `1179px`; do not let the desktop three-column intro squeeze copy/buttons into narrow vertical columns on iPad-sized screens.
- Posts archive and tag-page post cards should keep consistent title sizing; do not make the first visible card larger only because it is first in the list.
- Public page particle-toggle buttons use `切换烛光微粒` with the `✦` icon.
- 2026-06-20 style strengthening kept the static HTML/CSS/JS architecture and added only lightweight pages/styles.
- Public navigation now includes `今晚`, `酒柜`, and `夜间歌单`.
- `tonight.html` is the lightweight Tonight / 今晚 page combining Now and Aftertaste style status fragments.
- `playlist.html` is the lightweight Playlist / 夜间歌单 page. It may reference 王菲、《寓言》《浮躁》、《重庆森林》, and Only Lovers Left Alive as atmosphere notes, but must not become a music/film theme site, quote lyrics, embed players, or autoplay audio.
- `reviews.html` is now framed as Cellar / 酒柜, rendered from structured `window.BAR_REVIEWS` fields in `assets/content.js`.
- The homepage preserves `Phil Lin的Bar`, the badge, and `I flutter in circle never landing on nothing`, with restrained copy around giving unfinished thoughts a night-space.
- `酒鬼医学生` is preserved in a self-aware low-intensity form in about/footer copy; do not make it the homepage's largest visual identity tag.
- Article reading styles were tightened for long-form reading: max article width around 720px, looser line height, paragraph spacing, link/image/blockquote styling, and article endnotes.
- 2026-06-20 art completion pass added a CSS-only homepage atmosphere layer: rain/glass reflection, bottle silhouette, window grid, and bar counter glow.
- The latest art direction uses stronger badge glow, rainy glass, amber/wine/cool-cyan highlights, more finished menu-board material, nav pill states, and layered card surfaces.
- 2026-06-20 cursor alignment fix: `.bar-cursor` in `assets/site.js` must keep `translate(...px, ...px) translate(-50%, -50%)` so the cursor ring center follows the pointer.
- 2026-06-20 acceptance rework confirmed the live site had the latest pre-rework homepage/reviews/about content at deployed `main` commit `2ec95306b342498f92bb8e4ac3d2e09f74310134`; local acceptance rework still requires commit/push before appearing online.
- Reduced motion and mobile/coarse-pointer contexts should not create the canvas, custom cursor, or pointer animation listeners.
- 2026-06-21 Edge cursor effect fix: ambient motion is now disabled by reduced motion or `max-width: 720px`, not by `(pointer: coarse)` / `(hover: none)`, because desktop Edge on touch-capable devices can match those queries even when a mouse is in use.
- 2026-06-20 cursor reentry/scroll fix: `assets/site.js` must keep cursor placement centralized in `syncCursorPosition()` / `moveCursor()` and clear `cursor.dataset.hidden` on fresh pointer movement, so the bar cursor recovers after page leave/reentry and scroll.
- 2026-06-20 image asset recovery: all bitmap assets in `assets/` were audited after the badge and friend avatars disappeared. Valid historical binaries were restored for `assets/bar-badge.png`, `assets/cocktail-hero.png`, `assets/hero-workspace.png`, `assets/starcried-avatar.png`, and `assets/crescentyves-avatar.jpg`. Keep image files binary-safe; avoid text/PowerShell redirection for image blobs.
- 2026-06-20 playlist detail update: `playlist.html` cards now link to six static detail pages, each with its own restrained song list. No lyrics, audio embeds, autoplay, or new dependencies were added.
- 2026-06-21 cursor scroll-offset fix: the custom cursor now uses fixed `left` / `top` from viewport `clientX` / `clientY`, and the `body` page-fade animation no longer uses `transform`, so scrolling should not make the cursor appear above the pointer.
- 2026-06-21 mobile index polish: homepage mobile layout was refined only inside small-screen media queries, with compact nav pills, tighter hero spacing, reduced decoration, and denser menu-entry cards. Desktop/base homepage rules should remain unaffected.
- 2026-06-21 homepage article menu simplification: article/category entries are grouped into one homepage Martini Flight card; `posts.html` shows `Martini · 文章`, category pages show `Gibson · 生活日志`, `Dirty Martini · 一些思绪`, and `Vesper · 种草安利`, and `about.html` now uses `Last Word · 关于我`.
- 2026-06-24 bar-note column added: `notes.html` is the Hanky Panky / 吧台札记 index for medium-length fragments. It is intentionally not added to the top navigation; the entry lives inside the homepage Martini Flight variants so the homepage and mobile nav do not get more crowded.
- `assets/content.js` now defines `window.BAR_NOTES` for note metadata. Each note should still have its own static `note-*.html` page. The old `_drafts/note-format-reference.html` template was deleted on 2026-06-25 at user request; future notes should follow an existing published `note-*.html` page instead.
- 2026-06-25 article/archive integration: 吧台札记 counts as part of the article system. `assets/site.js` merges `window.BAR_POSTS` and normalized `window.BAR_NOTES` inside `allPosts()`, so homepage recent posts, `posts.html` "全部", and the `吧台札记` archive filter include notes. `notes.html` remains a dedicated note-only page.
- Content boundary: gripe entries should be around 50 Chinese characters and preferably under 100; bar notes are roughly 300 to 1200 characters; complete pieces remain normal articles.
- Hanky Panky is the Martini-family identity for 吧台札记. Its glyph should keep the canonical Martini glass geometry and only add a small herbal/bitter cue. Mobile/tablet glyph rules must keep internal `5.2rem` geometry and scale by transform, matching the existing Martini-family constraint.
- 2026-06-24 drink glyph pass: all current public drink badges were upgraded toward A+C, meaning blueprint-style line structure plus one recognizable ingredient cue. Keep glyph artwork inside the canonical `5.2rem` internal box and continue responsive scaling by `transform` only, to avoid desktop/tablet/mobile drift.
- 2026-06-25 home desktop layout fix: homepage `.hero-lede` now uses a wider balanced text box to avoid awkward Chinese line breaks in the desktop menu intro. The grouped Martini Flight card reserves right-side space for its absolute drink glyph on desktop/tablet, while the phone list-card breakpoint removes that large reserve so text does not squeeze.
- 2026-06-25 material drink label pass: user rejected the CSS blueprint glyphs as too dry and requested material, lighting, and hand-drawn detail. `assets/styles.css` now keeps the same `.drink-glyph` class system but overlays painted-paper texture, glass highlights, liquid color layers, and per-drink garnish variables. Continue using the canonical `5.2rem` internal box and responsive transform scaling.
- 2026-06-25 bitmap-style drink label pass: user clarified the drink labels should follow the earlier concept/bitmap direction and not resemble the original CSS glyphs. `assets/drink-labels/` now contains standalone illustrated SVG image assets for current and fallback drink classes. `assets/styles.css` maps `.drink-glyph` classes to those assets and disables the old pseudo-element line drawings. The homepage lede is now a right-side after-hours note module on desktop, a horizontal note on tablet, and a compact ticket on mobile.
- 2026-06-25 short lab-still note published: user provided direct text beginning `还在实验室坐着。` and trusted Codex to choose the column. It was published as a bar note, `note-lab-day-not-over.html`, with title `只要不走，今天就还没有结束`, mood `缓冲`, and tag `吧台札记`.
- Current general cache-busting query string is `bar-art-20260626-mobile-labels`; the homepage stylesheet uses `bar-art-20260626-fruitfly-quote`.

## 1. Current Project Goal

Build and maintain a static personal GitHub Pages website for `Phil Lin的Bar`, with a dark cocktail-bar visual language, article browsing, tags, friend links, cocktail review placeholder content, and gallery placeholder content.

The site is currently a static HTML/CSS/JavaScript site. There is no build pipeline, package manager, server backend, database, or framework configured in the repository.

## 2. Phase-One Original Goals

Verified from current repository state and request-driven implemented artifacts:

- Rename/site-brand the website as `Phil Lin的Bar`.
- Replace older guide/admin wording with `关于我`.
- Remove the placeholder public article `To Be Continue` / `To Be Continued`, and retain one draft/reference article outside public navigation.
- Add a friend-link page for `StarCried`, including avatar, name, description, and outbound link.
- Add home friend-link entry.
- Add `酒评` and `摄影作品` navigation pages.
- Redesign the site around a cocktail/bar mood using abstract CSS/canvas visuals rather than generated photographic backgrounds.
- Add article categories/tags: `生活日志`, `一些思绪`, `种草安利`.
- Add article archive filtering by tag.
- Add three tag pages linked from the home topic cards.
- Make recent home articles render from article metadata and show the newest up to three posts.
- Convert article management direction to a lightweight index plus separate article HTML files.
- Remove the earlier browser-only `撰写` feature and its validation/editor pages.
- Update repository references for GitHub username `Phillin-lrz` where verified in docs/config.

## 3. Phase-One Completed Content

Verified in files:

- `index.html`
  - Home page title is `Phil Lin的Bar | 酒鬼医学生的博客`.
  - Brand text is `Phil Lin的Bar`.
  - Navigation contains `首页`, `文章`, `酒评`, `摄影作品`, `友链`, `关于我`.
  - Hero uses cocktail labels and abstract glass glyphs: Martini, Old Fashioned, Whisky Sour, Paloma.
  - Topic cards link to:
    - `tag-lab.html`
    - `tag-thoughts.html`
    - `tag-recommendations.html`
  - Recent posts container uses `data-recent-posts`.

- `assets/content.js`
  - `window.BAR_TAGS` has exactly `["生活日志", "一些思绪", "种草安利"]`.
  - `window.BAR_POSTS` contains public article entries including `article-not-yet-return.html`, `article-two-bottles-writing-touch.html`, and `article-first-words-on-the-bar.html`.
  - `window.BAR_REVIEWS` contains placeholder review metadata.

- `posts.html`
  - Article archive has tag filter buttons for `全部`, `生活日志`, `一些思绪`, `种草安利`.
  - Article list is rendered into `data-post-list`.

- Tag pages:
  - `tag-lab.html` renders posts with `data-tag-posts="生活日志"`.
  - `tag-thoughts.html` renders posts with `data-tag-posts="一些思绪"`.
  - `tag-recommendations.html` renders posts with `data-tag-posts="种草安利"`.

- Bar notes:
  - `notes.html` renders note metadata from `window.BAR_NOTES` using `data-note-list`.
  - The first public note entry is `note-lab-after-exam-restlessness.html`.
  - `_drafts/note-format-reference.html` was deleted at user request; use existing `note-*.html` pages as future note references.

- Article pages:
  - Public static article pages currently include `article-not-yet-return.html`, `article-two-bottles-writing-touch.html`, and `article-first-words-on-the-bar.html`.
  - `article.html` is a dynamic fallback/detail renderer for posts that include inline `content` in `content.js`; current recommended pattern is separate static article HTML files, so this dynamic page is retained for compatibility but is not the primary authoring path.
  - `_drafts/article-format-reference.html` is retained as a format/reference draft and is not linked from public page lists.

- Friend links:
  - `friends.html` contains a StarCried friend card.
  - StarCried outbound URL is `https://starcried.github.io/`.
  - Avatar file is `assets/starcried-avatar.png`.
  - `friends.html` contains a CrescentYves friend card.
  - CrescentYves outbound URL is `https://crescentyves.me/`.
  - Avatar file is `assets/crescentyves-avatar.jpg`.

- Pages added or retained:
  - `reviews.html` is now the Cellar / 酒柜 page and renders structured `BAR_REVIEWS` cards.
  - `tonight.html` shows lightweight current-state and aftertaste cards.
  - `playlist.html` shows lightweight music/film atmosphere notes without audio embeds.
  - `gallery.html` shows gallery placeholder tiles.
  - `about.html` is the about page.
  - `about.html` contact email is `phillin.lrz0714@gmail.com`.

- Visual design:
  - `assets/styles.css` defines the dark cocktail/bar palette and glass glyph styling.
  - `assets/site.js` creates a fixed canvas background with cocktail-shaped constellations and pointer connections.

- Removed feature:
  - `write.html` and `editor.html` no longer exist.
  - Searches found no remaining `write.html`, `editor.html`, `write-link`, `data-auth`, `data-editor`, `WRITER`, or `撰写` references after removal.

- GitHub username references:
  - `.git/config` remote is `https://github.com/Phillin-lrz/Phillin-lrz.github.io.git`.
  - README deployment docs reference `Phillin-lrz.github.io`.

## 4. Explicitly Not Done In Phase One

- No second-stage development has started.
- No backend, authentication, CMS, database, or server-side publishing system exists.
- No dependency installation or framework migration was performed.
- No automated deployment was run.
- No commit was created in this session because the available shell cannot run `git`.
- No visual browser screenshot verification was completed in the final sealed state. Browser automation attempts in earlier work were blocked by local sandbox issues; current seal verification is file and JavaScript syntax based.
- No custom domain configuration was added.
- No comment system was added.
- No real cocktail review content or real photography portfolio content was authored beyond placeholders.
- One Word document was published as `article-first-words-on-the-bar.html`.
- One Word document was published as `article-two-bottles-writing-touch.html`.

## 5. Current Code Architecture Understanding

Static site architecture:

- HTML files are route/page files.
- `assets/styles.css` is the shared visual system and responsive layout file.
- `assets/site.js` provides:
  - particle/cocktail-constellation canvas background
  - particle toggle persistence via `localStorage`
  - accent button support for any remaining `[data-accent]` controls
  - post rendering from `window.BAR_POSTS`
  - article archive filtering
  - tag page rendering
  - dynamic article rendering fallback
- `assets/content.js` is a lightweight metadata index.
- Public article bodies should live in separate article HTML files. `assets/content.js` should point to those files via `url`. It currently has two public article entries.
- `window.BAR_NOTES` entries are normalized into the article stream for archive/recent-post rendering while still powering `notes.html`.
- Article images should be placed under `assets/posts/<article-id>/` when generated from Word or other rich sources.

## 6. Key Files And Modules

- `index.html`: home page; hero, topic cards, feature cards, friend entry, recent article container.
- `posts.html`: article archive and filter UI.
- `tag-lab.html`: tag landing page for `生活日志`.
- `tag-thoughts.html`: tag landing page for `一些思绪`.
- `tag-recommendations.html`: tag landing page for `种草安利`.
- `notes.html`: Hanky Panky / 吧台札记 index for medium-length fragments.
- `article.html`: dynamic article fallback for metadata-driven inline content.
- `article-two-bottles-writing-touch.html`: second published article, tag `一些思绪`.
- `article-first-words-on-the-bar.html`: first published article, tag `一些思绪`.
- `article-not-yet-return.html`: 2026-06-26 published article, tag `一些思绪`.
- `_drafts/article-format-reference.html`: non-public reference article template.
- `note-lab-after-exam-restlessness.html`: first published bar-note page.
- `note-lab-day-not-over.html`: short published bar-note page about staying in the lab to delay tomorrow.
- `reviews.html`: cocktail review placeholder page.
- `gallery.html`: gallery placeholder page.
- `friends.html`: StarCried friend-link page.
- `about.html`: about page.
- `assets/content.js`: article tag/review/note metadata.
- `assets/gripes.js`: static gripe-column data.
- `assets/site.js`: canvas interaction and post rendering logic.
- `assets/styles.css`: shared CSS, dark bar visual language.
- `assets/starcried-avatar.png`: StarCried avatar.
- `assets/crescentyves-avatar.jpg`: CrescentYves avatar.
- `assets/posts/.gitkeep`: placeholder for future article image directories.
- `README.md`: human maintenance notes.

## 7. Key Technical Decisions

### Decision: Use static HTML/CSS/JS only

Reason:
- The repository is a static GitHub Pages site with no package/build system.
- Avoided unnecessary dependencies and deployment complexity.

Alternatives not chosen:
- React/Vue/Svelte app.
- Static-site generator migration.
- Server-backed CMS.

### Decision: Keep `content.js` as metadata index only

Reason:
- Full article bodies and base64 images make `content.js` too large and fragile.
- Metadata index allows home/archive/tag pages to stay fast and simple.

Alternatives not chosen:
- Store every article body inside `content.js`.
- Store articles in browser `localStorage`.
- Build a backend writing API.

### Decision: Use separate HTML files for article bodies

Reason:
- GitHub Pages can serve static article files directly.
- Easier to edit, review, rollback, and attach images by relative path.

Alternatives not chosen:
- One dynamic `article.html?id=...` page as the primary route.
- Client-only generated articles.

### Decision: Remove the `撰写` feature

Reason:
- User explicitly requested deletion.
- Client-side write/auth pages created confusion because a static site cannot write permanent files to the repo.

Alternatives not chosen:
- Keep hidden editor.
- Keep local-only publishing.
- Add backend authentication.

### Decision: Abstract cocktail/bar design, not photographic background

Reason:
- User requested recognizable cocktail mood without direct generated image background.
- CSS glyphs and canvas constellations satisfy the visual direction while staying lightweight.

Alternatives not chosen:
- Generated bitmap hero background.
- Realistic bar/cocktail photo background.

### Decision: Cache-busting query string `bar-clean-20260610`

Reason:
- Previous changes appeared stale in browser; query version helps force updated CSS/JS.

Alternatives not chosen:
- Leave old query string.
- Introduce build-hash tooling.

Current cache-busting query string:
- As of the 2026-06-23 article publishing cache refresh, public HTML pages use `bar-art-20260623-post3` for `assets/styles.css`, `assets/content.js`, `assets/gripes.js`, `assets/site.js`, and cache-busted shared image references.
- As of the 2026-06-24 life-log publishing cache refresh, public and draft HTML pages use `bar-art-20260624-life-log` for shared assets.
- As of the 2026-06-25 first bar-note publishing refresh, public and draft HTML pages use `bar-art-20260625-note1` for shared assets.
- As of the 2026-06-25 note/archive integration refresh, public and draft HTML pages use `bar-art-20260625-notes-archive` for shared assets.
- As of the 2026-06-25 short lab-still note refresh, public and draft HTML pages use `bar-art-20260625-lab-still` for shared assets.
- As of the 2026-06-26 Word article publish, public and draft HTML pages use `bar-art-20260626-return` for shared assets.
- As of the 2026-06-28 screenshot-backed gripe detail layout fit, public and draft HTML pages use `bar-art-20260628-gripe-detail-fit` for shared assets.
- Important publishing reminder: whenever `assets/content.js` changes for a new post, refresh the HTML asset query string on public pages in the same turn. On 2026-06-22, the article index was updated but the HTML pages initially still referenced the old query string, so the homepage/archive/tag pages could appear stale from browser cache.

## 8. Current Constraints

- Static GitHub Pages only.
- No server-side write capability.
- No database schema exists.
- No package manager or bundler exists.
- `git` command is available in the current shell environment as of 2026-06-20; keep running status and diff checks before and after work.
- In-app browser automation is unreliable/blocked in this environment.
- Keep CSS/JS paths relative for GitHub Pages portability.
- Avoid storing large base64 images in `content.js`.
- Use `assets/posts/<article-id>/` for future post images.

## 9. Non-Goals / Do Not Violate

- Do not start phase-two development before reading these context files and confirming scope.
- Do not rely on chat history as the only memory source.
- Do not introduce new dependencies without explicit approval.
- Do not migrate to a framework without explicit approval.
- Do not create a backend/CMS/auth system without explicit approval.
- Do not change the public navigation labels casually.
- Do not store long article bodies or base64 images in `assets/content.js`.
- Do not delete compatibility files unless a replacement path and rollback are clear.
- Do not expand diff scope into unrelated refactors.
- Do not remove `article.html` unless all links and compatibility expectations are audited.
- Do not claim git diff/status/browser verification unless commands actually ran successfully.

## 10. Known Risks

- Git status/diff can now be verified in the current shell, but the working tree may contain uncommitted local changes.
- Browser visual verification could not be completed during final sealing.
- `assets/cocktail-hero.png` and `assets/hero-workspace.png` exist; current verified pages do not reference them, but they increase repository size.
- `article.html` renders `post.content` if present, but current recommended metadata-only pattern does not include content. It remains a compatibility fallback.
- The article archive, recent posts, and tag pages now show empty states until a new public article is added.
- `reviews.html` now renders structured Cellar / 酒柜 cards from `window.BAR_REVIEWS`; future risk is that placeholder review metadata still needs real content.
- `data-accent` logic remains in `site.js`, but current visible pages may not use it.
- Word-to-HTML conversion is not yet implemented; future conversion must preserve images and paths carefully.
- External link `https://starcried.github.io/` was not revalidated during this sealing pass.

## 11. Most Likely Information To Be Lost After Context Folding

- The `撰写` feature was intentionally removed; do not restore it unless user asks.
- `content.js` should remain a lightweight article index only.
- Public article bodies should be separate HTML files.
- `article.html` is compatibility/fallback, not the primary article-authoring path.
- Git and JavaScript syntax verification were limited by environment, so future work should re-run them when tools are available.
- Browser visual verification is skipped by project preference unless explicitly requested or required by a higher-priority instruction.
- The GitHub remote in `.git/config` is already updated to `Phillin-lrz`.
- `assets/cocktail-hero.png` is present but should be treated as unused unless verified otherwise.

## 12. Must Reconfirm Before Phase Two

- User's exact phase-two goal and whether it includes Word document conversion.
- Whether the site should keep the current title `Phil Lin的Bar | 酒鬼医学生的博客`.
- Whether `article.html` should remain as fallback or be removed after all articles are static.
- Whether `reviews.html` should be data-driven from `BAR_REVIEWS`.
- Whether unused image assets may be deleted.
- Whether Git is available in the user's actual terminal and whether latest changes have been committed/pushed.
- Whether the online GitHub Pages site reflects local files after deployment.

## 13. Current Acceptance Criteria And Status

- Context externalized to repo files: pending at time of writing this file, completed when all four AGENT files exist.
- First-stage site state recoverable from files: satisfied by `AGENT_CONTEXT.md`, `AGENT_TODO.md`, `AGENT_CHANGELOG.md`, `AGENT_HANDOFF.md` once created.
- No second-stage development started: satisfied.
- Verified not relying on chat only: satisfied for major facts by reading current files and command output.
- JavaScript syntax validation: to be recorded after final check.
- Git status/diff validation: not satisfied because `git` command is unavailable in current environment.
- Browser visual validation: not satisfied in this sealing pass.
