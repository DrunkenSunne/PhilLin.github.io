# AGENT_CHANGELOG

Last updated: 2026-06-27

## 2026-06-27 Word Life Log Published - Lemon Tea And Ethanol Therapy

User provided `C:\Users\Phil Lin\Desktop\自己\自己总要写点东西\20260627.docx`, asked whether it was `生活日志` or `一些思绪`, and then approved publication after changing the title.

- Extracted the Word document text and confirmed no embedded media files were present.
- Chose `生活日志` because the piece is structured around a concrete day timeline.
- Generated review-only `preview-20260627.html`, then formally published after the user said to change the title and publish.
- Generated final static article file `article-lemon-tea-ethanol-therapy.html`.
- Added one `BAR_POSTS` metadata entry with tag `生活日志`.
- Removed the preview file by renaming it into the final article file.
- Final title: `一杯暴晒柠檬茶与非循证乙醇疗法`.
- Final summary: `一篇关于低电量一天的生活日志：凌晨四点睡、复习被实验和柠檬茶打断，晚上又被 GPT 哄着捡回进度，最后用一瓶 Asahi 给满脑子的病毒和寄生虫做一点象征性的消毒。`
- Publication date: `2026-06-27`.
- Refreshed HTML asset query strings to `bar-art-20260627-ethanol` so the homepage, article archive, and `生活日志` tag page load the updated metadata.
- Visual verification was skipped by project preference.

## 2026-06-27 Gripe Added - Sleep Schedule Privacy

User provided a gripe text without an explicit mood.

- Added a fourteenth `window.BAR_GRIPES` entry to `assets/gripes.js`.
- Published gripe: `我得想个办法把我熬夜相关内容屏蔽一下家里人（`
- Chose mood `心虚`, emoji `🙈`, and timestamp `2026-06-27 18:29:25`.
- Updated `AGENT_CONTEXT.md` and `AGENT_HANDOFF.md` so future recovery sees the current gripe count and latest entries.
- Visual verification skipped by project preference.

## 2026-06-27 Bar Note Published - Sunlit Lemon Tea

User provided `D:\Download\暴晒一小时的柠檬茶.docx` and asked to upload it as a bar note, leaving missing site fields to Codex.

- Extracted the Word document text and confirmed no embedded media files were present.
- Generated review-only `preview-20260627.html`, then formally published after user said `发`.
- Generated final static note file `note-sunlit-lemon-tea.html`.
- Added one `BAR_NOTES` metadata entry with tag `吧台札记`.
- Deleted the preview file by renaming it into the final note file.
- Final title: `暴晒一小时的柠檬茶`.
- Final mood: `晒蔫`.
- Final summary: `一条被实验打断的下午札记：睡眠不足、复习计划、实验步骤和一杯在夏日骄阳下晒了一个小时的柠檬茶，拼成一种很日常的荒诞。`
- Publication date: `2026-06-27`.
- Refreshed HTML asset query strings to `bar-art-20260627-lemon-tea` so `notes.html`, the homepage recent list, and the article archive load the updated metadata.
- Visual verification was skipped by project preference.

## 2026-06-27 Private Places Naming Follow-up

User clarified that the places in `reviews.html` are not necessarily visited at night; they are places the user likes to go. User asked to update related titles and copy while keeping the drink label artwork and drink name unchanged.

- Renamed the visible section from `酒柜` to `私藏` across public navigation, homepage entry copy, and `reviews.html` titles/headings.
- Kept the route `reviews.html`, the Boulevardier drink name, and the existing drink label/glyph unchanged.
- Changed `reviews.html` framing from `Cellar Map` / 私人夜间地图 to `Place Map` / 私人去处地图.
- Replaced night-only copy with language around liked places, repeat visits, cafes, restaurants, bars, small shops, and other stopover places.
- Changed the filter from `夜宵` to `小店` and updated placeholder review data so it no longer implies all records are night-only.
- Refreshed HTML asset query strings to `bar-art-20260627-places`.
- Visual verification skipped by project preference.

## 2026-06-27 Quiet Cellar Map Redesign Pass

User provided a broader site-direction request for subtraction, darker mature private-bar atmosphere, clearer page metaphors, reduced template-like decoration, and a major `酒柜` rework. User also clarified that the homepage `Fruit Fly` lyric should remain unchanged and that the old homepage dot/line decoration should be removed or replaced.

- Kept the existing static HTML/CSS/JS architecture and did not introduce new dependencies.
- Updated public and draft page asset query strings to `bar-art-20260627-places`.
- Changed the main navigation across HTML pages to exactly `首页 / 文章 / 今晚 / 酒柜 / 歌单 / 摄影 / 关于`.
- Removed `友链` from the main navigation while preserving `friends.html`; added footer links and an About-page guide-card entry.
- Rewrote `reviews.html` copy and controls around `Cellar Map` / 私人夜间地图.
- Replaced cocktail-only `BAR_REVIEWS` placeholder fields with structured visit-review data for night places.
- Updated `assets/site.js` so review cards render total score, tags, subratings, one-line conclusion, notes, recommended scenes, suitable scenes, and unsuitable scenes.
- Added lightweight review filters for all, 酒吧, 餐厅, 咖啡, 夜宵, 适合独处, and 适合聊天.
- Added a final `assets/styles.css` override layer for darker old-brass palette, lower grid/canvas emphasis, restrained hover motion, page-specific note/mixtape/contact-sheet metaphors, responsive review cards, and receipt-like gripe rail styling.
- Kept the homepage `I flutter in circle never landing on nothing` lyric unchanged with the `Fruit Fly` source label.
- Follow-up: updated the homepage `酒柜` card copy so it points to bars, restaurants, cafes, and night places instead of cocktail-only tasting notes.
- Visual verification skipped by project preference.
- Rollback: restore the previous HTML nav/cache references from git, restore old `reviews.html`, revert `BAR_REVIEWS` and review rendering in `assets/content.js` / `assets/site.js`, and remove the final 2026-06-27 override block from `assets/styles.css`.

## 2026-06-26 Homepage Fruit Fly Lyric Plate

User chose option A for `I flutter in circle never landing on nothing`, asked to keep the original lyric unchanged, add the song name plus a record cue, remove the shown homepage dot/line/decorative shelf, and preserve mobile/tablet lyric layout.

- Replaced the homepage `bar-shelf` markup in `index.html` with a `lyric-plate`.
- Added the unchanged lyric, a `Fruit Fly` source label, and a CSS record icon.
- Removed the lyric from the footer identity sentence so `酒鬼医学生，非专业调酒，偶尔认真写字。` stays separate.
- Removed old `bar-shelf` CSS and disabled the old menu-intro tick strip.
- Added responsive lyric plate styles for desktop, tablet, and phone widths.
- Refreshed only the homepage stylesheet query string to `bar-art-20260626-fruitfly-quote`.
- Visual verification skipped by project preference.
- Rollback: restore the previous `bar-shelf` block in `index.html`, restore the removed `bar-shelf` CSS/menu-intro tick styles from git, and change the homepage stylesheet query string back to `bar-art-20260626-mobile-labels`.

## 2026-06-26 Mobile Drink Label Layout Fix

User clarified that tablet was mostly okay and the main issue was phone-size drink labels looking too small and awkward.

- Updated `assets/styles.css` phone rules so homepage menu cards use a stable left drink-label column and right text column.
- Enlarged phone labels from the previous tiny right-side presentation while preserving the canonical internal `5.2rem` glyph geometry and scaling only with `transform`.
- Kept the tablet `721px` and wider card rules unchanged.
- Refreshed public and draft HTML asset query strings to `bar-art-20260626-mobile-labels`.
- Visual verification skipped by project preference.
- Rollback: revert the `assets/styles.css` mobile rules and replace `bar-art-20260626-mobile-labels` with `bar-art-20260626-wind-gripes` in HTML asset references.

## 2026-06-26 Word Article Published - Better In The Wind

User provided `C:\Users\Phil Lin\Desktop\自己\自己总要写点东西\20260626.docx`, requested tag `一些思绪`, and left remaining publication choices to Codex.

- Generated review-only `preview-20260626.html`.
- User rejected earlier title drafts; final title is `在风里慢慢好一点`.
- Generated final static article file `article-better-in-the-wind.html` after user said `发吧`.
- Added one `BAR_POSTS` metadata entry with tag `一些思绪`.
- Removed the preview file by renaming it into the final article file.
- Final summary: `一篇写在考试后夜晚的小广场上的随笔：从被游戏和烦躁困住的下午出走，在风、蛙鸣、乌龙茶和黄色月亮里，重新找到一种更安静的解压方式。`
- Publication date: `2026-06-26`.
- Confirmed the Word document had no embedded media files.
- User also asked to publish a gripe. Added one `BAR_GRIPES` entry with mood `无语`, emoji `😶`, and timestamp `2026-06-26 23:24:04`.
- Refreshed HTML asset query strings to `bar-art-20260626-wind-gripes` so the homepage, article archive, `一些思绪` tag page, and gripe rail load the updated data.

## 2026-06-26 Preview Text Cleanup

User noticed preview-only wording in a generated page and asked whether older posts also had it.

- Searched all current `article-*.html`, `note-*.html`, and `preview-*.html` files for `Preview`, `预览`, `预览说明`, and `确认后发布`.
- Found leftover preview UI only in the already published `article-not-yet-return.html`.
- Removed the preview-only eyebrow, preview explanation block, preview tag, and confirmation sidebar wording from `article-not-yet-return.html`.
- Rechecked the same search terms afterward; no matching preview-only wording remained in current article, note, or preview HTML files.
- Ran `node --check assets/site.js`, `node --check assets/content.js`, and `node --check assets/gripes.js`; all passed.
- Visual verification was skipped by project preference.

## 2026-06-26 Word Article Published - Not Yet Return

User provided `C:\Users\Phil Lin\Desktop\临时用\新建 Microsoft Word 文档.docx` with tag `一些思绪` and left the remaining publication elements to Codex.

- Generated review-only `preview-20260626.html`, then formally published after user said `发`.
- Generated final static article file `article-not-yet-return.html`.
- Added one `BAR_POSTS` metadata entry with tag `一些思绪`.
- Deleted `preview-20260626.html`.
- Final title: `不如归去，但还不能归去`.
- Final summary: `一篇写在实验室深夜的长文：从不想回宿舍的迟疑出发，绕到陶渊明与王羲之，写归去的羡慕、责任的牵引，以及暂时还不能真正放下的自己。`
- Publication date: `2026-06-26`.
- Confirmed the Word document had no embedded media files.
- Refreshed HTML asset query strings to `bar-art-20260626-return` so the homepage, article archive, and `一些思绪` tag page load the updated `assets/content.js`.

## 2026-06-25 Short Lab-Still Bar Note Published

User provided direct text beginning `还在实验室坐着。` and asked Codex to choose the column, skip preview, and publish directly.

- Chose `吧台札记` because the text is a self-contained reflective fragment rather than a full article or a gripe.
- Generated final static note file `note-lab-day-not-over.html`.
- Added one `BAR_NOTES` metadata entry with tag `吧台札记`.
- Final title: `只要不走，今天就还没有结束`.
- Final mood: `缓冲`.
- Final summary: `一条很短的夜间札记：还坐在实验室里，不是因为非做不可，只是想把今天和明天之间的那一点缓冲再留久一点。`
- Refreshed HTML asset query strings to `bar-art-20260625-lab-still` so `notes.html`, the homepage recent list, and the article archive load the updated `assets/content.js`.

## 2026-06-25 Bitmap-Style Drink Labels And Designed Lede

User clarified that drink labels should follow the earlier concept/bitmap style rather than resembling the original CSS glyph system, and that the centered homepage lede layout still felt unattractive.

- Added standalone illustrated drink-label assets under `assets/drink-labels/` for current page glyphs and retained fallback drink classes.
- Updated `assets/styles.css` so `.drink-glyph` classes map to those image assets and old pseudo-element line drawings are disabled.
- Redesigned the homepage lede as a right-side `After Hours Note` module on desktop instead of centered copy.
- Added tablet and mobile lede rules so the note becomes a horizontal module on tablet and a compact ticket on phone.
- Refreshed public and draft HTML asset query strings to `bar-art-20260625-bitmap-labels`.

## 2026-06-25 Material Drink Labels

User rejected the latest homepage lede layout as unattractive and clarified that drink labels should have material, lighting, and hand-drawn details rather than staying as dry CSS blueprint glyphs.

- Changed the homepage hero lede markup so the sentence uses an intentional two-line break after `白天把事情做完，`.
- Updated `.menu-intro .hero-lede` so desktop uses a centered two-line text block; tablet/mobile reset to single-column placement.
- Reworked the drink glyph layer in `assets/styles.css` into material-style labels: painted paper texture, glass highlight, liquid depth, shadow glow, and per-drink garnish variables.
- Kept the existing `.drink-glyph` class names and canonical `5.2rem` internal box so desktop/tablet/mobile scaling rules remain stable.
- Refreshed public and draft HTML asset query strings to `bar-art-20260625-material-labels`.
- Used the image generation skill instructions for this decision, but implemented as repo-native CSS/SVG-like layers to avoid fragile transparent bitmap cropping for glass/liquid assets.

## 2026-06-25 Home Layout Fix

User reported two desktop homepage layout issues from screenshots: the hero lede line broke awkwardly, and the Martini Flight drink glyph overlapped the article-card paragraph.

- Updated `assets/styles.css` so `.menu-intro .hero-lede` has a wider balanced text box.
- Added right-side reserved space for the grouped Martini Flight card on desktop and tablet widths so the absolute drink glyph no longer sits on top of text.
- Kept the phone list-card breakpoint free of the large right reserve to avoid squeezing mobile text.
- Refreshed public and draft HTML asset query strings to `bar-art-20260625-layout-fix`.
- Visual browser verification remains subject to the project preference and the previously recorded browser automation limitation.

## 2026-06-25 Bar Notes Integrated Into Article Archive

User clarified that 吧台札记 should count as part of the article system, and noted that the first note was not showing on the note page.

- Added `吧台札记` to `window.BAR_TAGS` in `assets/content.js`.
- Added `tag: "吧台札记"` to the first `BAR_NOTES` entry.
- Updated `assets/site.js` so `allPosts()` merges `window.BAR_POSTS` and normalized `window.BAR_NOTES`.
- Homepage recent posts and `posts.html` "全部" now include notes by date order.
- `posts.html` now has a `吧台札记` filter chip.
- Kept `notes.html` as the dedicated note-only page.
- Updated notes/archive copy and README to describe notes as an article-system tag.
- Refreshed public and draft HTML asset query strings to `bar-art-20260625-notes-archive`.
- Investigated missing note display: `BAR_NOTES` data and the note file were present; simulated DOM rendering confirmed `notes.html` now produces the `note-lab-after-exam-restlessness.html` card. The likely cause of the user's prior view was stale cached `site.js` / `content.js`.
- Visual browser verification skipped by project preference.

## 2026-06-25 First Bar Note Published

User provided `C:\Users\Phil Lin\Desktop\临时用\札记.docx` and asked to delete the previous template while publishing this note.

- Extracted three text paragraphs from the Word document.
- Confirmed no embedded media files were present.
- Generated final static note file `note-lab-after-exam-restlessness.html`.
- Added one `BAR_NOTES` metadata entry in `assets/content.js`.
- Deleted `_drafts/note-format-reference.html` at user request.
- Final title: `待在实验室，也不等于没有浪费时间`.
- Final mood: `自我审问`.
- Final summary: `一条写在实验室里的札记：考试后的工作姿态、游戏带来的烦躁、形式主义式的复习，以及面对 AI 与自我思考时说不清的进退感。`
- Refreshed HTML asset query strings to `bar-art-20260625-note1` so `notes.html` loads the updated `assets/content.js`.

## 2026-06-24 Life Log Schedule Published

User provided a screenshot of a 2026-06-24 schedule summary and asked Codex to write and design a life log based on it.

- Generated review-only `preview-20260624.html`, then formally published after user approval.
- Generated final static article file `article-after-exam-still-held.html`.
- Added one `BAR_POSTS` metadata entry with tag `生活日志`.
- Deleted `preview-20260624.html`.
- User requested changing the preview endnote because it felt too corny; final endnote is `考完以后还能把下一件事接起来，今天就先记到这里。`
- Final tag: `生活日志`.
- Final title: `考完以后，也没有完全散掉`.
- Final summary: `一段关于考试结束后继续衔接学习与实验的生活日志：细胞与分子生物学考试收尾，病原生物学继续推进，药理学总论也终于从未开始变成已启动。`
- Kept experimental details vague as `实验室工作` and `细胞状态确认`, matching the user's privacy direction in the source.
- Refreshed HTML asset query strings to `bar-art-20260624-life-log` so `index.html`, `posts.html`, and tag pages load the updated `assets/content.js`.

## 2026-06-24 Drink Glyph A+C Pass

User chose the A+C direction for drink badges: blueprint cocktail icons plus ingredient silhouettes, with every badge covered and no desktop/tablet/mobile image drift.

- Upgraded the shared CSS drink glyph system in `assets/styles.css` so current public badges use clearer glass shapes, blueprint dots/lines, and recognizable ingredient cues.
- Covered the current page glyphs: Martini, Gibson, Dirty Martini, Vesper, Hanky Panky, Gimlet, Boulevardier, Sazerac, French 75, Tom Collins, and Last Word.
- Also updated retained/fallback glyph classes in CSS, including Highball, Paloma, Negroni, Coupe, Rocks, and Paper Plane, so future reuse stays stylistically aligned.
- Kept the canonical glyph internal geometry at `5.2rem`; responsive rules continue to scale via `transform` instead of shrinking the internal box.
- Refreshed public and draft HTML asset query strings to `bar-art-20260624-glyphs`.
- Verification performed: JavaScript syntax checks, local HTML link-target check, glyph-class coverage check, stale runtime cache-string search, and `git diff --check`.
- Browser visual verification was attempted because the user explicitly called out desktop/tablet/mobile alignment, but the in-app browser connection was blocked by local permissions and standalone Playwright is not installed in this workspace.

## 2026-06-24 Bar Notes Column Scaffold

User wanted a medium-length fragment column: longer than the right-side 吐槽 rail but not as formal as full articles. User also asked to avoid crowding the homepage, give every note its own page, use a Martini-family drink identity/glyph, and preserve mobile/tablet compatibility.

- Added `notes.html` as the Hanky Panky / 吧台札记 index page.
- Added `window.BAR_NOTES = []` to `assets/content.js`; future notes should be metadata entries pointing to independent `note-*.html` pages.
- Added note list rendering to `assets/site.js`, including an empty state for the new page.
- Added `_drafts/note-format-reference.html` as the static single-note template.
- Added the homepage entry only inside the Martini Flight variant links; the top navigation was intentionally unchanged.
- Added `hanky-panky-glyph`, `note-rule`, `note-list`, and `note-card` styles in `assets/styles.css`, with 2-by-2 Martini variant chips on desktop/tablet and single-column chips on phone.
- Refreshed shared asset query strings to `bar-art-20260624-notes`.
- Updated README and AGENT state with the content boundary: gripe around 50 characters and preferably under 100, bar notes roughly 300 to 1200 characters, full articles remain in the article system.
- Visual verification skipped by project preference.

## 2026-06-24 Gripe Added - Fast Walking Training

User provided a gripe text and asked Codex to choose the mood.

- Added a twelfth `window.BAR_GRIPES` entry to `assets/gripes.js`.
- Published gripe: `我走路快这个毛病绝对是我平常喜欢在实验室教学楼实验教学楼宿舍（甚至医院）之间卡点来回奔波+电梯没那么好使养成的。`
- Chose mood `自嘲`, emoji `🏃‍♂️`, and timestamp `2026-06-24 14:20:16`.
- Updated `AGENT_CONTEXT.md` and `AGENT_HANDOFF.md` so future recovery sees the current gripe count and latest entry.
- Visual verification skipped by project preference.

## 2026-06-23 Life Log Text Published

User provided a direct text life log and requested it as today's life log.

- Used tag `生活日志`.
- Used publication date `2026-06-23`, based on the current date and the user's wording.
- Generated review-only `preview-20260623.html`, then formally published after user approval.
- Generated final static article file `article-one-side-cannot-fall.html`.
- Added one `BAR_POSTS` metadata entry with tag `生活日志`.
- Deleted `preview-20260623.html`.
- Refreshed HTML asset query strings to `bar-art-20260623-post3` so `index.html`, `posts.html`, and tag pages load the updated `assets/content.js`.
- Final title: `起码一边不能倒下`.
- Final summary: `一段带着罪恶感的生活日志：复习半不邋遢，细胞实验因状态暂缓，只能先承认今天的失落，再希望往后的日子至少有一边稳住。`

## 2026-06-22 Word Article Published - Life Log 20260622

User provided `C:\Users\Phil Lin\Desktop\临时用\日志.docx` and requested tag `生活日志`, leaving title, summary, and formatting decisions to Codex.

- Extracted three text paragraphs from the Word document.
- Treated the first paragraph `20260622` as the intended publication date.
- Confirmed no embedded media files were present.
- Generated review-only `preview-20260622.html`, then formally published after user approval.
- Generated final static article file `article-experiment-review-double-run.html`.
- Added one `BAR_POSTS` metadata entry with tag `生活日志`.
- Deleted `preview-20260622.html`.
- Refreshed HTML asset query strings to `bar-art-20260622-post2` so `index.html`, `posts.html`, and tag pages load the updated `assets/content.js`.
- Final title: `实验和复习双开的一天`.
- Final summary: `一段关于高压日程的生活日志：病原生物学复习、细胞实验推进、游戏之后被压力追上，也试着给接下来的超频运转找到一点续航方式。`

## 2026-06-22 Word Article Published - Life Log

User provided `C:\Users\Phil Lin\Desktop\临时用\1.docx` and requested tag `生活日志`, leaving title, summary, and formatting decisions to Codex.

- Extracted three text paragraphs from the Word document.
- Treated the first paragraph `20260621` as the intended publication date.
- Confirmed no embedded media files were present.
- Generated review-only `preview-20260621.html`, then formally published after user approval.
- Generated final static article file `article-good-luck-day.html`.
- Added one `BAR_POSTS` metadata entry with tag `生活日志`.
- Deleted `preview-20260621.html`.
- Final title: `祝我好运的一天`.
- Final summary: `一段很短的日常记录：复习细胞生物学实验理论考试、做科研调研，也在齐豫和梦飞船的歌里给接下来疲惫的日子留下一句祝福。`

## 2026-06-21 Tablet Home Intro Collapse Fix

User provided a tablet screenshot showing the Index hero intro squeezed into narrow vertical columns.

- Added a shared `721px` to `1179px` tablet rule that collapses the homepage `menu-intro` from desktop three-column layout into a single-column tablet layout.
- Converted the tablet `menu-kicker` to a compact horizontal lockup and restored the hero note/buttons to normal wrapping rows.
- Kept the large desktop three-column bar-menu intro above `1179px` and phone-specific list layout below `720px`.
- Visual verification skipped by project preference.

## 2026-06-21 Edge Cursor Effect Fix

User reported that Microsoft Edge and other non-Chrome browsers did not show the mouse effect.

- Changed ambient-motion suppression from `(hover: none), (pointer: coarse)` to the narrower `max-width: 720px` check so desktop Edge on touch-capable devices is not mistaken for mobile.
- Added mouse event fallbacks alongside pointer events for cursor movement and menu drink hover states.
- Updated public and draft HTML asset query strings to `bar-art-20260621-fix15`.
- Visual verification skipped by project preference.

## 2026-06-21 Tablet Index And Glyph Alignment Fix

User reported that the tablet Index layout still had problems and that mobile/tablet drink labels were misaligned.

- Updated mobile and tablet CSS so drink glyph internals keep the canonical `5.2rem` geometry and only scale through `transform`, avoiding pseudo-element drift.
- Restored tablet Index menu cards to true card layouts in the `721px` to `900px` range instead of inheriting the phone list layout.
- Kept the phone menu as compact list-style cards, but fixed their glyph scaling so the drink graphics remain centered.
- Updated public and draft HTML asset query strings to `bar-art-20260621-fix14`.
- Visual verification skipped by project preference.

## 2026-06-21 Article Detail Badge And Format Notes

User requested the two concrete article pages' drink label/name be updated and the project documentation define the rough future article format.

- Updated `article-first-words-on-the-bar.html` and `article-two-bottles-writing-touch.html` from `Coupe · Article` to `Martini · 文章正文`.
- Updated `article.html` compatibility fallback and `_drafts/article-format-reference.html` so future article pages start from the same `Martini · 文章正文` badge.
- Updated `README.md` page-structure notes to match the current Martini family article system and `Last Word · 关于我`.
- Added a README article-format section covering file naming, `article-layout drink-page drink-martini`, header/meta shape, sidebar, and image placement under `assets/posts/<文章id>/`.
- Updated durable agent state so future recovery does not restore the old `Coupe · Article` identity.
- Visual verification skipped by project preference.

## 2026-06-21 Tablet Layout Pass

User requested a tablet adaptation pass after the homepage article menu simplification.

- Added a tablet landscape / large-tablet responsive layer for `901px` to `1179px`.
- Added a tablet portrait responsive layer for `721px` to `900px`.
- Tuned tablet navigation so links wrap into scan-friendly pill grids instead of cramped desktop spacing.
- Adjusted the homepage menu board for tablets: three-column rhythm on larger tablets, two-column rhythm on portrait tablets, and a full-width grouped article card on portrait tablets.
- Tuned tablet card sizing, drink glyph scale, menu variant chips, split sections, gallery, playlist, Tonight, and guide grids so they do not collapse into phone-style single columns too early.
- Kept existing phone breakpoints unchanged below `720px`.
- Updated public and draft HTML asset query strings to `bar-art-20260621-fix13`.
- Visual verification skipped by project preference.

## 2026-06-21 Homepage Article Menu Simplification

User noted that ten homepage menu entries felt redundant and asked for the main article entry plus its three child pages to become one drink family with three variations, while avoiding duplicate entry semantics.

- Simplified the homepage menu: the article system is now one grouped `Martini Flight` card instead of four separate large cards.
- The grouped article card uses `Martini` as the family/main identity and links to `posts.html` through a distinct `进入文章归档` action.
- The three child category links are now only the variants: `Gibson · 生活日志`, `Dirty Martini · 一些思绪`, and `Vesper · 种草安利`.
- Updated `posts.html` to show `Martini · 文章`.
- Updated `tag-lab.html`, `tag-thoughts.html`, and `tag-recommendations.html` to show the three Martini-family variants above.
- Reassigned `about.html` and the homepage About card from `Martini · 关于我` to `Last Word · 关于我` so `Martini` is reserved for the article family.
- Added CSS-only `gibson-glyph`, `dirty-martini-glyph`, `vesper-glyph`, and `last-word-glyph` marks while keeping the existing fixed glyph geometry so drink badges do not drift.
- Added `menu-primary-link` and `menu-variants` styles and changed the desktop homepage menu grid back to four columns for a lighter seven-card board.
- Updated public and draft HTML asset query strings to `bar-art-20260621-fix13`.
- Visual verification skipped by project preference.

## 2026-06-21 Home Menu And Drink Identity Rework

User reported that the homepage menu no longer matched the expanded pages and that drink identities were duplicated, especially `Highball` being used for both `生活日志` and `今晚`.

- Expanded the homepage menu board from eight entries to ten entries so it covers the public navigation pages: `文章`, `生活日志`, `一些思绪`, `种草安利`, `今晚`, `酒柜`, `夜间歌单`, `摄影作品`, `友链`, and `关于我`.
- Kept existing identities for older entries: `Paper Plane · 文章`, `Highball · 生活日志`, `Old Fashioned · 一些思绪`, `Paloma · 种草安利`, `French 75 · 摄影作品`, `Tom Collins · 友链`, and `Martini · 关于我`.
- Reassigned newly added sections to non-duplicated identities: `Gimlet · 今晚`, `Boulevardier · 酒柜`, and `Sazerac · 夜间歌单`.
- Updated `tonight.html`, `reviews.html`, `playlist.html`, and the playlist detail pages to use their new page badge class, visible English name, and glyph.
- Added CSS-only `gimlet-glyph`, `boulevardier-glyph`, and `sazerac-glyph` logo marks in `assets/styles.css`.
- Changed the desktop homepage menu grid to five columns so the ten-entry menu forms a clean two-row board.
- Updated public and draft HTML asset query strings to `bar-art-20260621-fix13`.
- Visual verification skipped by project preference.

## 2026-06-21 Drink Badge Consistency Fix

User reported the night playlist drink mark and English name were wrong, and asked to check every page's drink mark and English label.

- Audited public HTML pages for `drink-page`, `drink-portrait`, `drink-glyph`, and visible drink badge text.
- Changed playlist index and playlist detail pages from `Playlist · ...` to `French 75 · ...`.
- Added a dedicated `french-75-glyph` in `assets/styles.css` so French 75 uses a champagne-flute style mark instead of the generic coupe mark.
- Updated `gallery.html` and the homepage French 75 menu tile to use `french-75-glyph`.
- Changed `reviews.html` badge text from `Cellar · 酒柜` to `Negroni · 酒柜` to match its Negroni page/glyph identity.
- Changed `tonight.html` badge text from `Tonight · 今晚` to `Highball · 今晚` to match its Highball page/glyph identity.
- Updated public and draft HTML asset query strings to `bar-art-20260621-fix10`.
- Visual verification skipped by project preference.

## 2026-06-21 Mobile Index Layout Polish

User reported the mobile index page layout looked poor and requested improvement without affecting desktop.

- Added mobile-only layout refinements in `assets/styles.css` under small-screen breakpoints.
- Reworked the homepage navigation on mobile into compact pill-grid rows so it no longer feels like a cramped desktop nav.
- Tightened the mobile home hero: smaller title rhythm, reduced decorative clutter, cleaner note/action spacing, and hidden bar-shelf tick decoration on mobile.
- Converted the mobile menu cards into denser list-style entry cards with smaller drink glyphs, readable labels, and clamped descriptions.
- Kept desktop/base homepage rules unchanged; changes are scoped to `max-width` media queries.
- Updated public and draft HTML asset query strings to `bar-art-20260621-fix9`.
- Visual verification skipped by project preference.

## 2026-06-21 Cursor Scroll Offset Fix

User reported the mouse effect still appeared above the pointer after the page had moved downward.

- Removed transform movement from the `body` page-fade animation in `assets/styles.css`; a transformed page container can make fixed-position cursor children behave relative to the scrolled document instead of the viewport in some browsers.
- Changed `.bar-cursor` positioning to keep its centering transform static and let `assets/site.js` update `left` / `top` from `event.clientX` / `event.clientY`.
- Removed scroll/wheel cursor resync listeners so scroll does not reapply stale or document-relative cursor math.
- Updated public and draft HTML asset query strings to `bar-art-20260621-fix8`.
- Visual verification skipped by project preference.

## 2026-06-21 Gripe Added - Productive Exam Sprint

User provided a gripe text and mood `兴奋`.

- Added an eleventh `window.BAR_GRIPES` entry to `assets/gripes.js`.
- Published gripe: `期末复习伴随着ddl还是有条不紊的开始了，但其实被逼着进入一种近似心流的高效率工作状态也是一种不错的体验，喜欢待办事项被一项一项做完的感觉。`
- Recorded mood as `兴奋`, emoji as `🤩`, and timestamp as `2026-06-21 14:19:06`.
- Updated `AGENT_CONTEXT.md` and `AGENT_HANDOFF.md` so future recovery sees the current gripe count and latest entry.
- Visual verification skipped by project preference.

## 2026-06-20 Playlist Detail Pages

User requested every `夜间歌单` card to map to its own page, with each page containing a different song list.

- Converted the six cards in `playlist.html` into links to dedicated playlist detail pages.
- Added six static detail pages: `playlist-faye-fable.html`, `playlist-faye-restless.html`, `playlist-chungking.html`, `playlist-only-lovers.html`, `playlist-after-ddl.html`, and `playlist-drinking.html`.
- Added lightweight track-list styling in `assets/styles.css`.
- Kept the implementation static, with no audio embedding, no autoplay, no lyrics, and no new dependencies.
- Updated public and draft HTML asset query strings to `bar-art-20260620-fix7`.

## 2026-06-20 Image Asset Recovery

User reported friend-link images and then the site badge disappeared.

- Audited all bitmap assets under `assets/` by file signature.
- Confirmed `assets/bar-badge.png`, `assets/cocktail-hero.png`, `assets/hero-workspace.png`, `assets/starcried-avatar.png`, and `assets/crescentyves-avatar.jpg` were affected by invalid binary content in current `HEAD` or working tree.
- Restored valid binary versions from earlier Git history for the five image assets.
- Added cache-busting query strings for friend avatars and the shared badge references so browsers request the recovered image files.
- Hardened friend-card layering in `assets/styles.css` so decorative pseudo-elements stay behind real avatar images.
- Updated all public and draft HTML asset query strings to `bar-art-20260620-fix6`.

## 2026-06-20 Cursor Reentry And Scroll Follow Fix

User reported the mouse effect still stopped following after the mouse left the page or after scrolling downward.

- Updated `assets/site.js` so cursor placement is centralized in `syncCursorPosition()` / `moveCursor()`.
- Cursor state now clears `data-hidden` whenever a new pointer move/over event is received, so returning to the page does not depend only on `window.pointerenter`.
- Added passive `wheel` and `scroll` sync hooks so the cursor reuses the latest viewport pointer coordinate after scrolling instead of staying in a stale hidden/frozen state.
- Updated all public and draft HTML asset query strings to `bar-art-20260620-fix5` so browsers request the corrected `assets/site.js`.

## 2026-06-20 Acceptance Rework

User requested deployment consistency checks plus restrained acceptance fixes without restructuring the site.

- Checked the live GitHub Pages homepage, reviews page, and about page with cache-busting query parameters; live pages already contained the new `今晚 / 酒柜 / 夜间歌单` navigation, the new homepage line `白天把事情做完，夜里给没想明白的事留一点位置。`, `Cellar · 酒柜`, and the newer about copy.
- Checked GitHub Actions via the public API; latest `pages build and deployment` run was on `main`, completed successfully, and deployed commit `2ec95306b342498f92bb8e4ac3d2e09f74310134`. Public Pages-source API returned 404 and `gh` CLI was unavailable, so exact Pages Settings source could not be read from settings.
- Added explicit mobile breakpoints in `assets/styles.css` for `max-width: 900px`, `720px`, and `480px`, including single-column grids, mobile navigation wrapping, smaller badges/headings, full-width mobile buttons, vertical footer layout, simplified decorative border, and mobile cursor hiding.
- Completed CSS reduced-motion handling and tightened `assets/site.js` so reduced-motion and mobile/coarse-pointer contexts do not create the canvas, do not create the custom cursor, and do not attach pointer animation listeners.
- Made the motion toggle semantics clearer and ensured turning particles off stops the draw loop.
- Lightly revised `tonight.html` copy with more concrete student/DDL/experiment pressure while keeping the restrained tone.
- Lightly revised `about.html` to strengthen the day/night contrast while keeping `酒鬼医学生`, and added a `reviews.html` noscript fallback for the JS-rendered cellar list.
- Updated public and draft HTML asset query strings to `bar-art-20260620-fix4`.
- Verification performed: live HTML/API checks with Node `fetch`, `node --check assets/site.js`, `node --check assets/content.js`, `node --check assets/gripes.js`, stale runtime reference search, `git diff --check`, `git status --short`, `git diff --stat`, `git diff --name-status`, and targeted `git diff`.
- Mobile browser scroll verification was attempted but the automation tool was rejected by the environment usage limit, so mobile no-horizontal-scroll was checked by CSS/static reasoning only.

## 2026-06-20 Cursor Alignment Fix

User reported the mouse effect was misaligned.

- Fixed the pointer-following `.bar-cursor` transform in `assets/site.js` so the cursor ring is centered on the pointer instead of placing its top-left corner at the pointer coordinate.
- Updated all public and draft HTML asset query strings to `bar-art-20260620-fix3` so browsers request the corrected `assets/site.js`.
- Verification performed: `node --check assets/site.js`, `node --check assets/content.js`, `node --check assets/gripes.js`, asset-query search, stale writer/cache search, local HTML link target check, `git status --short`, `git diff --stat`, `git diff -- .`, and `git diff --check`.
- Visual verification skipped by project preference.

## 2026-06-20 Art Completion Pass

User said the art/design completion was still not enough and asked for further modification.

- Added a lightweight CSS-only homepage atmosphere layer in `index.html`: rain/glass reflection, bottle silhouette, window grid, and bar counter glow.
- Strengthened `assets/styles.css` art direction with richer rainy-glass background, amber/wine/cool-cyan highlights, stronger badge glow, more finished menu-board material, nav pill states, and layered card surfaces.
- Improved homepage visual depth by putting content above an internal art layer and adding more polished menu-card shadows, separators, and glass highlights.
- Added mobile handling so decorative bottle/window layers do not crowd the small-screen layout.
- Updated all public and draft HTML asset query strings to `bar-art-20260620-fix2` to avoid stale cached CSS/JS.
- Verification performed: `node --check assets/site.js`, `node --check assets/content.js`, `node --check assets/gripes.js`, asset-query search, local HTML link target check, and `git diff --stat`.
- Visual verification skipped by project preference.

## 2026-06-20 Style Strengthening And Lightweight Structure

User requested a restrained "style strengthening + lightweight structure optimization" for the static GitHub Pages site without changing the tech stack, removing content, or turning the site into a film/music-themed site.

- Added `tonight.html` as a lightweight Tonight / 今晚 page combining Now and Aftertaste style content.
- Added `playlist.html` as a lightweight 夜间歌单 page for music and film atmosphere references without lyrics, autoplay, or embedded players.
- Updated public navigation and `_drafts/article-format-reference.html` to include `今晚`, `酒柜`, and `夜间歌单`.
- Reframed `reviews.html` from 酒评 into Cellar / 酒柜 and made it render structured cards from `window.BAR_REVIEWS`.
- Expanded `assets/content.js` review metadata with type, scene, channel, flavor, tipsy, mood, and revisit fields.
- Updated `index.html` with a more restrained homepage premise, primary entry buttons, and Tonight / Playlist entry cards while preserving `Phil Lin的Bar`, the badge, and `I flutter in circle never landing on nothing`.
- Updated `about.html` copy to keep `酒鬼医学生` in a self-aware, lower-intensity form instead of making it the homepage visual focus.
- Improved article reading styles in `assets/styles.css`: narrower readable width, looser line height, paragraph spacing, links, images, blockquotes, and article endnotes.
- Added shared styles for Tonight, Playlist, Cellar cards, mobile navigation scrolling, responsive single-column layouts, page fade-in, hover polish, and `prefers-reduced-motion` handling.
- Updated `assets/site.js` to respect reduced-motion by default and render cellar cards.
- Updated README with current page structure and Cellar maintenance notes.
- Verification performed: `node --check assets/site.js`, `node --check assets/content.js`, `node --check assets/gripes.js`, writer/stale-cache reference search, local HTML link target check, `git status --short`, `git diff --stat`, `git diff -- .`, and `git diff --check`.
- Visual verification skipped by project preference.

## 2026-06-20 Post List Format Unification

User reported mismatched title sizes on the posts page and asked for a broader format pass.

- Updated `assets/site.js` so archive and tag-page post cards use the same heading level instead of making only the first card larger.
- Added a scoped `assets/styles.css` rule so non-compact post-list card titles stay visually consistent even if mixed heading tags appear later.
- Unified the public page particle-toggle button copy/icon to `切换烛光微粒` / `✦`.
- Updated `_drafts/article-format-reference.html` asset query strings and particle-toggle copy to match the current site format.
- Visual verification skipped by project preference.

## 2026-06-20 Copy And Contact Update

User requested a site copy correction and contact email update.

- Corrected the home eyebrow text to `Chungking Express`.
- Updated the about page contact email to `phillin.lrz0714@gmail.com`.
- Visual verification skipped by project preference.

## 2026-06-20 Gripe Added - Forgotten Inspiration

User provided a gripe text and mood `无语`.

- Added a tenth `window.BAR_GRIPES` entry to `assets/gripes.js`.
- Published gripe: `昨天忘了什么时候突然想才思泉涌一下，今天就什么都不记得了，真的很搞笑。`
- Recorded mood as `无语`, emoji as `😶`, and timestamp as `2026-06-20 15:42:08`.
- Updated `AGENT_CONTEXT.md` and `AGENT_HANDOFF.md` so future recovery sees the current gripe count and latest entry.
- Visual verification skipped by project preference.

## 2026-06-20 Gripe Added - Screen Return

User provided a gripe text and mood `无语`.

- Added a ninth `window.BAR_GRIPES` entry to `assets/gripes.js`.
- Published gripe: `前天给电脑屏幕摔坏了，昨天没更新，不过其实也没时间更新，终于回来了。`
- Recorded mood as `无语`, emoji as `😶`, and timestamp as `2026-06-20 15:40:42`.
- Updated `AGENT_CONTEXT.md` and `AGENT_HANDOFF.md` so future recovery sees the current gripe count and latest entry.
- Visual verification skipped by project preference.

## 2026-06-18 Word Article Published

User provided `20260618.docx` and requested upload with careful typography and visual fit to the site's current aesthetic.

- Read the Word document from the user-provided desktop path.
- Extracted text and confirmed there are no embedded media files.
- Detected the Word text uses `华文行楷`; preserved that handwriting feel in selected accents while keeping body copy in the site's readable article typography.
- Generated `preview-20260618.html` as a review-only article preview.
- After user approval, generated the final article file `article-two-bottles-writing-touch.html`.
- Added a `BAR_POSTS` metadata entry pointing to `article-two-bottles-writing-touch.html`.
- Deleted `preview-20260618.html`.
- Proposed title: `两瓶酒后，找回写字的手感`.
- Proposed tag: `一些思绪`.
- Proposed summary: `便利店买来的酒、深夜随机播放的音乐和对写作手感的怀念，串成一段关于微醺、表达和过去自己的独白。`
- The article now appears through the home recent-posts area, `posts.html`, and `tag-thoughts.html`.
- Visual verification skipped by project preference.

## 2026-06-17 Gripe Added - Writing Urge

User provided a gripe text and asked Codex to choose the mood.

- Added an eighth `window.BAR_GRIPES` entry to `assets/gripes.js`.
- Published gripe: `今晚突然一时兴起想要写点东西，准备择日不如撞日喝点开写，但是想到时间太晚且明天事情也不少遂放弃。我会在端午节假期高频率更新的。`
- Chose mood `微醺`, emoji `🍸`, and timestamp `2026-06-17 00:57:39`.
- Updated `AGENT_CONTEXT.md` and `AGENT_HANDOFF.md` so future recovery sees the current gripe count and latest entry.
- Visual verification skipped by project preference.

## 2026-06-15 Gripe Added - Study Pressure

User provided a gripe text and mood `崩溃`.

- Added a seventh `window.BAR_GRIPES` entry to `assets/gripes.js`.
- Published gripe: `哎哟这几个小时之内不知道为什么学习压力陡增，而且我知道这个压力会一直持续到7.9考完试，但我还有实验要做。`
- Recorded mood as `崩溃`, emoji as `😭`, and timestamp as `2026-06-15 14:41:39`.
- Updated `AGENT_CONTEXT.md` and `AGENT_HANDOFF.md` so future recovery sees the current gripe count and latest entry.
- Visual verification skipped by project preference.

## 2026-06-15 Gripe Added - Pathogen Exam

User provided a gripe text and mood `崩溃`.

- Added a sixth `window.BAR_GRIPES` entry to `assets/gripes.js`.
- Published gripe: `考个线上的病原生物学实验理论考试就因为坐在教室所以紧张的钥匙。我的绩点。。。怎么会这样。。。`
- Recorded mood as `崩溃`, emoji as `😭`, and timestamp as `2026-06-15 14:03:23`.
- Updated `AGENT_CONTEXT.md` and `AGENT_HANDOFF.md` so future recovery sees the current gripe count and latest entry.
- Visual verification skipped by project preference.

## 2026-06-15 Gripe Added - Exam Outlet

User provided a gripe text and mood `烦躁`.

- Added a fifth `window.BAR_GRIPES` entry to `assets/gripes.js`.
- Published gripe: `为什么考试的教室插座没电。`
- Recorded mood as `烦躁`, emoji as `😤`, and timestamp as `2026-06-15 12:53:09`.
- Updated `AGENT_CONTEXT.md` and `AGENT_HANDOFF.md` so future recovery sees the current gripe count and latest entry.
- Visual verification skipped by project preference.

## 2026-06-15 Gripe Added - Question Bank

User provided a gripe text and mood `烦躁`.

- Added a fourth `window.BAR_GRIPES` entry to `assets/gripes.js`.
- Published gripe: `我真的一点也不喜欢复习任何科目，除非给我题库刷。本质做题区。`
- Recorded mood as `烦躁`, emoji as `😤`, and timestamp as `2026-06-15 12:27:20`.
- Updated `AGENT_CONTEXT.md` and `AGENT_HANDOFF.md` so future recovery sees the current gripe count and latest entry.
- Visual verification skipped by project preference.

## 2026-06-13 Gripe Added

User provided a gripe text and mood `迷幻`.

- Added a third `window.BAR_GRIPES` entry to `assets/gripes.js`.
- Published gripe: `其实本来这两天都有文章更新的，但是PUBG太好玩了。`
- Recorded mood as `迷幻`, emoji as `😵‍💫`, and timestamp as `2026-06-13 23:05:56`.
- Updated `AGENT_CONTEXT.md` and `AGENT_HANDOFF.md` so future recovery sees the current gripe count and latest entry.
- Visual verification skipped by project preference.

## 2026-06-12 Abstract Bar Menu Redesign

User requested a broad visual redesign while preserving the cocktail-bar concept, avoiding realistic images/scenes where possible, and making the home page feel like a bar menu where each menu item is a drink leading to a page.

- Rebuilt `index.html` hero area as a menu board with drink/page pairings: `Paper Plane · 文章`, `Highball · 生活日志`, `Old Fashioned · 一些思绪`, `Paloma · 种草安利`, `Negroni · 酒评`, `French 75 · 摄影作品`, `Tom Collins · 友链`, and `Martini · 关于我`.
- Added drink identity badges to secondary pages and article pages.
- Added abstract CSS drink glyphs, dot fields, line grids, polygon overlays, and menu-card styling in `assets/styles.css`.
- Added a lightweight pointer-following bar cursor in `assets/site.js`; hovering menu drinks shows the drink name.
- Kept existing page copy mostly unchanged, except for necessary drink/page labels.
- Initially replaced friend avatars with abstract marks, then restored the original avatar images after user clarified that all friend-link information and avatars must remain unchanged.
- User changed the preview requirement: do not generate screenshots; they will open `.html` files directly for review.
- Verification performed: `node --check assets/site.js`, `node --check assets/content.js`, `node --check assets/gripes.js`, `git status --short`, `git diff --stat`, `git diff -- .`, and `Select-String` confirming the only `<img>` tags are the two friend-link avatars in `friends.html`.
- Visual browser screenshots were not generated because the user explicitly cancelled screenshot generation and chose direct HTML review.
- Follow-up refinement: user disliked the orphaned `Martini · 关于我` tile and requested less blank space. The home menu is now a strict 4-by-2 grid, `menu-drink-large` was removed, a CSS-only abstract bar shelf was added near the menu header, and the Friends/recent-posts blocks were combined into a two-column `home-followup` section.
- Later correction: user clarified that the Friends/recent-posts area did not need layout changes. Restored that area to the original `split-section` structure, kept the strict 4-by-2 home menu, and expanded the abstract alcohol motifs across the site with CSS-only base-spirit bottle shadows, wine/coupe forms, and craft-beer foam/tap-like accents.
- Additional refinement: user felt some graphics were too abstract and the left side of the home `Phil Lin的Bar` title felt empty. Added a CSS-only `menu-emblem` beside the title with a coupe-like glass, stirring spoon, citrus/olive accents, and strengthened drink glyphs with more recognizable liquid, ice, bubbles, garnish, and foam details.
- Badge asset generation: user asked Codex to generate a site badge image. Generated an abstract cocktail/bar badge and copied it to `assets/bar-badge.png`. Replaced the text `B` brand mark across public pages with this image and used the same badge beside the home heading.
- Latest title/glyph refinement: user felt the Paper Plane graphic was too casual and the large home title badge looked unsophisticated. Replaced the large home heading badge with a smaller `menu-kicker` lockup using the generated badge, menu label, and year. Reworked `.paper-plane-glyph` to read as a coupe-style cocktail with an abstract folded-paper garnish instead of a loose paper-airplane icon.
- Background decision: user rejected the standalone D/E preview pages and chose the earlier recommended A+E direction. Deleted `previews/background-d-star-cellar.html` and `previews/background-e-menu-paper.html`. Updated the formal `assets/styles.css` background to combine dark menu-paper texture, subtle foil border, and restrained cocktail-blueprint lines/nodes.
- Visual bugfix: user reported abstract graphics were misaligned on subpages, especially five unexplained vertical lines in the upper-left area. The cause was the recipe-tick pseudo-element shared by `.drink-heading::before` and `.article-header::before`. Restricted that tick decoration to `.menu-board .menu-intro::after` only, and disabled it on subpage/article headings.
- Visual bugfix: user reported every subpage drink icon was misaligned. The cause was the subpage `.drink-portrait` rule shrinking the internal `.drink-glyph > span` box while the glyph pseudo-elements still used full-size rem geometry. Changed subpage drink icons to keep the full glyph box and scale it uniformly with `transform: scale(0.62)`.
- Subpage drink badge sizing: user asked for the drink icon and text beside it to be larger and better fit the badge box. Increased `.drink-portrait` gap, padding, min-height, font size, icon frame, and glyph scale from `0.62` to `0.72`.
- Online layout mismatch fix: after upload, user reported the deployed site differed greatly from local. The likely cause was stale GitHub Pages/browser cached assets because all pages still referenced `bar-clean-20260610`. Updated HTML asset query strings to `bar-menu-20260612-fix1` for `assets/styles.css`, `assets/content.js`, `assets/gripes.js`, and `assets/site.js`.

## 2026-06-12 Gripe Added

User provided a gripe text and mood `无语`.

- Added a second `window.BAR_GRIPES` entry to `assets/gripes.js`.
- Published gripe: `最近一直在感觉自己很忙和自己很闲之间来回跳跃。`
- Recorded mood as `无语`, emoji as `😶`, and timestamp as `2026-06-12 12:29:58`.
- Updated `AGENT_CONTEXT.md` and `AGENT_HANDOFF.md` so future recovery sees the current gripe count and latest entry.
- Visual verification skipped by project preference.

## 2026-06-11 Command Validation Policy

User reviewed repeated command failures and decided the project should keep Git checks and `node --check`, skip browser visual verification by default, and stop using Node REPL as a routine fallback.

- Keep attempting `git status --short`, `git diff --stat`, and `git diff -- .` for recovery and diff awareness.
- Keep attempting `node --check` for relevant JavaScript files, including `assets/site.js`, `assets/content.js`, and `assets/gripes.js`.
- Continue skipping browser visual verification by project preference unless explicitly requested or required by higher-priority instructions.
- Do not attempt Node REPL fallback as a routine substitute for blocked `node --check` or blocked browser verification.
- If Git or Node commands fail, record the exact limitation and rely on file-level checks.

## 2026-06-11 Project Preferences Localized

User asked whether global-related settings could be written into this project's durable AGENT files, and requested that they be transferred if effective.

- Added a project-level preference to `AGENTS.md`: skip visual verification by default unless the user explicitly asks later or a higher-priority instruction requires it.
- Added the same preference to `AGENT_CONTEXT.md`, including the requirement to report skipped visual verification and residual visual risk.
- Updated `AGENT_TODO.md` validation steps so browser visual checks are conditional instead of default.
- Preserved the gripe scale-up reminder in project state: if `assets/gripes.js` becomes too heavy, remind the user about scheme 3 or scheme 4.
- Clarified that project files can achieve this effect for this repository because startup recovery requires reading `AGENTS.md` and the AGENT state files before non-trivial work.
- Limitation: this affects this repository's project workflow; it does not erase any separate global memory note that may also exist.

## 2026-06-11 Gripe Data Split

User chose scheme 2 for gripe rail scaling and asked to remember scheme 3/4 for future upgrades.

- Moved `window.BAR_GRIPES` out of `assets/content.js`.
- Added `assets/gripes.js` as the dedicated static gripe data file.
- Updated all HTML pages to load `gripes.js` between `content.js` and `site.js`.
- Kept the existing rendering behavior: only the current visible page of gripes is rendered into the DOM.
- Documented scheme 3 and scheme 4 as future upgrade paths if the gripe count makes `assets/gripes.js` too large.
- Scheme 3: split static gripe data into paginated files and load the needed page.
- Scheme 4: move gripe data into JSON and fetch it on demand.
- Added an ad-hoc memory note so future work can remind the user of this discussion.
- Verification performed: confirmed `BAR_GRIPES` now lives in `assets/gripes.js` and every HTML page loads `content.js`, `gripes.js`, then `site.js`.
- Verification blocked: `node --check` could not run because `node.exe` returned access denied; `git status` could not run because `git` is not recognized.
- Visual verification skipped per user global preference.

## 2026-06-11 Gripe Rail Added

User requested a right-side `吐槽` column on every page with forum-like pagination and a first gripe entry.

- Added `window.BAR_GRIPES` to `assets/content.js`.
- Published first gripe: `做实验永远都要留出实验时间10%-50%的计划时间余量，不然就会完蛋。`
- Recorded mood as `烦恼`, emoji as `😫`, and timestamp as `2026-06-11 12:40:15`.
- Updated `assets/site.js` to inject a `吐槽` rail on pages that load `assets/content.js`.
- The rail calculates a per-page display count from page height and paginates additional entries with previous/next controls.
- Updated `assets/styles.css` to reserve desktop right-side space and provide responsive layout on narrow screens.
- Updated `_drafts/article-format-reference.html` to load `../assets/content.js` so the rail can render there too.
- Updated README and AGENT state files with the static data-pool behavior.
- Limitation: this is a static GitHub Pages data pool, not a real server backend or user-submitted database.
- Verification performed: searched for `BAR_GRIPES`, gripe rail selectors, the first gripe text, and confirmed every HTML page loads `content.js` plus `site.js`.
- Verification blocked: `node --check` could not run because `node.exe` returned access denied, and browser visual verification could not run because the browser runtime was blocked by the current sandbox.

## 2026-06-11 Friend Link Added

User requested a new friend link for CrescentYves.

- Added CrescentYves to `friends.html`.
- Copied the provided avatar image to `assets/crescentyves-avatar.jpg`.
- Linked the card to `https://crescentyves.me/`.
- Added spacing to `.friend-showcase` so multiple friend cards are separated.
- Updated AGENT context and handoff files with the new friend-link state.
- Verification performed: confirmed the copied avatar file exists and searched for CrescentYves references.
- Verification blocked: browser visual verification could not run because the browser runtime was blocked by the current sandbox.

## 2026-06-11 Word Article Published

User provided `20260611.docx` and requested Codex choose the title and summary, with tag `一些思绪`.

- Read the Word document from the user-provided desktop path after permission was granted.
- Extracted six text paragraphs and confirmed no embedded media files were present.
- Generated `preview-20260611.html` as a review-only article preview.
- Updated the preview layout so the tag line and summary sit directly under the title instead of in the sidebar.
- After user approval, generated the final article file `article-first-words-on-the-bar.html`.
- Added a `BAR_POSTS` metadata entry pointing to `article-first-words-on-the-bar.html`.
- Deleted `preview-20260611.html`.
- Proposed title: `把第一杯文字放上吧台`.
- Proposed summary: `凌晨实验后写下的网站开篇：关于这个个人空间的来处、栏目、酒、摄影，以及一个不急着被定义的自我介绍。`
- The article now appears through the home recent-posts area, `posts.html`, and `tag-thoughts.html`.

Important limitation: `git` is not available in the current shell, so this changelog is based on current file state, repository scans, `.git/config`, and JavaScript syntax checks. It is not an authoritative git diff. Re-run `git status` and `git diff` when Git is available.

## 2026-06-11 Tag Rename

User changed the first home topic card to `生活日志` and requested all remaining site references be renamed consistently.

- Updated tag metadata in `assets/content.js`.
- Updated archive filter copy and filter value in `posts.html`.
- Updated `tag-lab.html` title, heading, and `data-tag-posts` value.
- Updated remaining visible copy in `about.html` and README examples.
- Updated AGENT state files so future recovery treats `生活日志` as the first article tag.

## 2026-06-11 Article Deletion

User requested deletion of the placeholder article named `To Be Continued` / `To Be Continue`.

- Deleted `article-to-be-continue.html`.
- Cleared `window.BAR_POSTS` in `assets/content.js`, leaving no public article entries.
- Updated `AGENT_CONTEXT.md`, `AGENT_TODO.md`, and `AGENT_HANDOFF.md` so future recovery does not restore or assume the deleted article.
- Expected behavior: home recent posts, article archive, and tag pages display their empty states until a new article is added.
- Verification performed: runtime references were searched in public HTML/assets/README scope; no old article references were found.
- Verification blocked: `node --check assets/content.js` and `node --check assets/site.js` could not run because `node.exe` returned access denied in the current environment; Node REPL fallback also failed due sandbox setup.
- Verification still required: JavaScript syntax check and browser visual check.
- Git status/diff remain unavailable if `git` is still not recognized in the current shell.

## Verification Performed During Context Sealing

- Project structure listed with PowerShell `Get-ChildItem`.
- Current files read directly with `Get-Content -Raw -Encoding UTF8`.
- `.git/config` read directly; remote URL is `https://github.com/Phillin-lrz/Phillin-lrz.github.io.git`.
- `git status --short` attempted and failed because `git` command was not recognized.
- `git diff --stat` and `git diff -- .` attempted and failed because `git` command was not recognized.
- `node --check assets/site.js` executed successfully using bundled Node.
- `node --check assets/content.js` executed successfully using bundled Node.
- Search for removed writer artifacts returned no matches for `write.html`, `editor.html`, `write-link`, `data-auth`, `data-editor`, `WRITER`, `撰写`, and stale `bar-export-20260610` after cleanup.

## File Changes

### `index.html`

- Type: modified
- Reason: Home page for the static personal site.
- Behavior change:
  - Shows `Phil Lin的Bar` branding.
  - Navigation links to home, articles, reviews, gallery, friends, and about.
  - Home topic cards link to the three tag pages.
  - Recent posts render into `data-recent-posts` from `assets/content.js`.
  - `撰写` entry is removed.
  - CSS/JS query version is `bar-clean-20260610`.
- Potential risk:
  - Recent posts depend on `assets/content.js` and `assets/site.js` loading successfully.
  - Browser layout not visually verified in final sealing pass.
- Executed verification:
  - File read directly.
  - Search confirmed no writer entry remains.
  - `assets/site.js` syntax check passed.
- Not executed:
  - Browser visual screenshot check.
  - Git diff comparison.
- Rollback:
  - Revert `index.html` from git once git is available, or restore from a known backup.

### `posts.html`

- Type: modified
- Reason: Add tag-based article archive filtering.
- Behavior change:
  - Article cards render into `data-post-list`.
  - Filter buttons support all posts and three tags.
  - `撰写` entry is removed.
- Potential risk:
  - If `BAR_POSTS` has invalid dates or tags, sorting/filtering may produce unexpected order or empty views.
- Executed verification:
  - File read directly.
  - `assets/site.js` syntax check passed.
- Not executed:
  - Browser click test of filter buttons.
  - Git diff comparison.
- Rollback:
  - Restore previous `posts.html` from git or backup.

### `tag-lab.html`

- Type: added
- Reason: Tag landing page for `生活日志`.
- Behavior change:
  - Renders posts matching `data-tag-posts="生活日志"`.
- Potential risk:
  - Empty state appears if there are no matching posts.
- Executed verification:
  - File read directly.
  - Shared script syntax check passed.
- Not executed:
  - Browser visual check.
  - Git diff comparison.
- Rollback:
  - Delete `tag-lab.html` and remove links from `index.html` if reverting tag pages.

### `tag-thoughts.html`

- Type: added
- Reason: Tag landing page for `一些思绪`.
- Behavior change:
  - Renders posts matching `data-tag-posts="一些思绪"`.
- Potential risk:
  - Depends on exact tag text matching `assets/content.js`.
- Executed verification:
  - File read directly.
  - Shared script syntax check passed.
- Not executed:
  - Browser visual check.
  - Git diff comparison.
- Rollback:
  - Delete `tag-thoughts.html` and remove links from `index.html` if reverting tag pages.

### `tag-recommendations.html`

- Type: added
- Reason: Tag landing page for `种草安利`.
- Behavior change:
  - Renders posts matching `data-tag-posts="种草安利"`.
- Potential risk:
  - Empty state appears until posts with this tag exist.
- Executed verification:
  - File read directly.
  - Shared script syntax check passed.
- Not executed:
  - Browser visual check.
  - Git diff comparison.
- Rollback:
  - Delete `tag-recommendations.html` and remove links from `index.html` if reverting tag pages.

### `assets/content.js`

- Type: added/modified, exact git origin pending confirmation
- Reason: Central metadata index for tags, posts, and review placeholders.
- Behavior change:
  - Defines `window.BAR_TAGS`.
  - Defines lightweight `window.BAR_POSTS`, currently with one published article entry.
  - Defines `window.BAR_REVIEWS` placeholder metadata.
  - No longer stores article body `content`; the placeholder article entry was removed.
- Potential risk:
  - Syntax errors in this file break article rendering across home/archive/tag pages.
  - `BAR_REVIEWS` is not currently used by `reviews.html`.
- Executed verification:
  - File read directly.
  - Bundled Node `--check` passed.
- Not executed:
  - Browser render verification.
  - Git diff comparison.
- Rollback:
  - Restore previous `assets/content.js` from git or backup.

### `assets/site.js`

- Type: modified
- Reason: Add cocktail canvas interaction and article rendering; later remove writer/editor logic.
- Behavior change:
  - Creates fixed canvas background with cocktail-shaped constellations and pointer lines.
  - Toggles canvas visibility via `localStorage` key `blog-particles`.
  - Renders recent posts, archive list, tag pages, and dynamic article fallback.
  - No writer/auth/editor/download functions remain.
- Potential risk:
  - Canvas is created on every page; visual or performance impact should be browser-checked.
  - `article.html` displays summary only if post metadata does not include `content`.
  - Date sorting depends on valid ISO-like `publishedAt`.
- Executed verification:
  - File read directly.
  - Bundled Node `--check` passed.
  - Search confirmed writer identifiers removed.
- Not executed:
  - Browser interaction/canvas visual check.
  - Git diff comparison.
- Rollback:
  - Restore previous `assets/site.js` from git or backup.

### `assets/styles.css`

- Type: modified
- Reason: Implement dark cocktail/bar visual system and page/card layouts; later remove writer/editor styles.
- Behavior change:
  - Defines dark bar palette, glass glyphs, topic cards, article cards, gallery tiles, friend profile, responsive layouts.
  - No writer/auth/editor styles remain.
- Potential risk:
  - Visual layout not final-screenshot verified.
  - Some unused legacy selectors may remain, such as `intro-grid article` when current home topic cards use `.topic-card`.
- Executed verification:
  - File read directly.
  - Search confirmed writer style identifiers removed.
- Not executed:
  - Browser visual check across desktop/mobile.
  - CSS lint.
  - Git diff comparison.
- Rollback:
  - Restore previous `assets/styles.css` from git or backup.

### `article-to-be-continue.html`

- Type: deleted
- Reason: User requested deletion of the placeholder article named `To Be Continued` / `To Be Continue`.
- Behavior change:
  - The article is no longer directly accessible as a local file.
  - Metadata includes `发布时间：2026-06-10 · 标签：一些思绪`.
  - No metadata entry points to this article from `assets/content.js`.
- Potential risk:
  - Any external bookmark to `article-to-be-continue.html` will 404 after deployment.
- Executed verification:
  - `Test-Path article-to-be-continue.html` returned `False`.
  - Reference search found no runtime references outside AGENT state documentation.
- Not executed:
  - Browser visual check.
  - Git diff comparison.
- Rollback:
  - Restore the file from git or backup and add a matching entry back to `assets/content.js`.

### `article.html`

- Type: added
- Reason: Dynamic article fallback/detail renderer.
- Behavior change:
  - Reads `?id=` and tries to find matching `BAR_POSTS` entry.
  - Displays `post.content` when available; otherwise displays summary text.
- Potential risk:
  - Current recommended architecture uses static per-article HTML, so this may confuse future authors if not documented.
  - Direct URLs with missing ids show a not-found message.
- Executed verification:
  - File read directly.
  - Shared script syntax check passed.
- Not executed:
  - Browser URL query test.
  - Git diff comparison.
- Rollback:
  - Delete only after auditing all `url` values and external links.

### `_drafts/article-format-reference.html`

- Type: modified
- Reason: Retained non-public format/reference article.
- Behavior change:
  - Uses new nav labels and new GitHub username references.
  - Uses `发布时间` format.
  - Remains under `_drafts` and is not linked from public article lists.
- Potential risk:
  - It still contains a full article-like page and could be visited directly if path known, but is not linked publicly.
- Executed verification:
  - File read directly.
- Not executed:
  - Browser visual check.
  - Git diff comparison.
- Rollback:
  - Restore previous draft or remove from repo if user decides no draft reference is needed.

### `about.html`

- Type: added/modified, exact git origin pending confirmation
- Reason: Replaces old guide/admin concepts with an about page.
- Behavior change:
  - Shows personal profile/about cards.
  - Includes contact email text.
  - No writer entry remains.
- Potential risk:
  - Personal details/contact email should be reconfirmed before public deployment if privacy matters.
- Executed verification:
  - File read directly.
- Not executed:
  - Browser visual check.
  - Git diff comparison.
- Rollback:
  - Restore previous about/guide page from git or backup.

### `friends.html`

- Type: added/modified, exact git origin pending confirmation
- Reason: Friend-link page.
- Behavior change:
  - Shows StarCried card with avatar and description.
  - Links externally to `https://starcried.github.io/`.
- Potential risk:
  - External URL not revalidated during sealing.
  - Avatar image must remain at `assets/starcried-avatar.png`.
- Executed verification:
  - File read directly.
  - Asset file presence observed in file listing.
- Not executed:
  - Browser visual check.
  - External URL check.
  - Git diff comparison.
- Rollback:
  - Restore/delete `friends.html` and remove home link if reverting friend-link feature.

### `reviews.html`

- Type: added
- Reason: Add `酒评` navigation/page.
- Behavior change:
  - Displays hardcoded cocktail review placeholder cards with `亟待创作` style content.
- Potential risk:
  - Not currently data-driven from `BAR_REVIEWS`; duplicate source of truth may confuse future changes.
- Executed verification:
  - File read directly.
- Not executed:
  - Browser visual check.
  - Git diff comparison.
- Rollback:
  - Delete page and remove nav/home feature links if reverting review feature.

### `gallery.html`

- Type: added
- Reason: Add `摄影作品` navigation/page.
- Behavior change:
  - Displays gallery-style placeholder tiles.
- Potential risk:
  - No real images yet; future image layout should be browser-checked.
- Executed verification:
  - File read directly.
- Not executed:
  - Browser visual check.
  - Git diff comparison.
- Rollback:
  - Delete page and remove nav/home feature links if reverting gallery feature.

### `assets/starcried-avatar.png`

- Type: added, based on file listing and page references
- Reason: Avatar for StarCried friend link.
- Behavior change:
  - Used by `friends.html`.
- Potential risk:
  - Binary asset cannot be meaningfully diffed in current text-only changelog.
- Executed verification:
  - File presence observed in recursive file listing.
- Not executed:
  - Visual inspection during sealing.
  - Git diff comparison.
- Rollback:
  - Remove file only if `friends.html` no longer references it or reference is updated.

### `assets/posts/.gitkeep`

- Type: added
- Reason: Preserve intended future article image directory.
- Behavior change:
  - No user-visible behavior.
- Potential risk:
  - None known.
- Executed verification:
  - File presence observed in recursive file listing.
- Not executed:
  - Git diff comparison.
- Rollback:
  - Remove if article image folder strategy changes.

### `assets/cocktail-hero.png`

- Type: existing binary asset; phase attribution pending confirmation
- Reason:
  - Current verified pages do not reference this file.
  - It may be a leftover from an earlier design attempt.
- Behavior change:
  - No current behavior observed from file references.
- Potential risk:
  - Adds repository weight.
- Executed verification:
  - File presence observed.
  - Current key HTML/CSS/JS reads did not show references.
- Not executed:
  - Full binary history check.
  - Git diff comparison.
- Rollback:
  - Do not delete until user approves and `rg "cocktail-hero"` confirms no references.

### `assets/hero-workspace.png`

- Type: existing binary asset; phase attribution pending confirmation
- Reason:
  - Current README still mentions replacing it as an old home image note, but current verified `index.html` does not reference it.
- Behavior change:
  - No current behavior observed from home page.
- Potential risk:
  - README may be stale for this asset.
- Executed verification:
  - File presence observed.
  - Current `index.html` read did not reference it.
- Not executed:
  - Full reference search for all files in final sealing.
  - Git diff comparison.
- Rollback:
  - Do not delete until user approves and references are audited.

### `README.md`

- Type: modified
- Reason: Maintenance documentation for static site and GitHub Pages deployment.
- Behavior change:
  - Documents metadata-index article structure.
  - Documents Word-to-article direction.
  - Documents GitHub Pages deployment using `Phillin-lrz`.
  - No longer documents writer/editor feature.
- Potential risk:
  - Some older lines may still mention obsolete concepts, such as `assets/hero-workspace.png`; re-audit before relying on README as full spec.
- Executed verification:
  - File read directly.
- Not executed:
  - Git diff comparison.
- Rollback:
  - Restore previous README from git or backup.

### `write.html`

- Type: deleted
- Reason: User requested deletion of writer feature and related pages.
- Behavior change:
  - Validation page no longer exists.
- Potential risk:
  - Any external bookmark to `write.html` will 404.
- Executed verification:
  - `Test-Path write.html` returned `False`.
  - Search found no `write.html` references.
- Not executed:
  - Git diff comparison.
- Rollback:
  - Restore from git or previous backup only if writer feature is explicitly requested again.

### `editor.html`

- Type: deleted
- Reason: User requested deletion of writer feature and related pages.
- Behavior change:
  - Browser-side article editor no longer exists.
- Potential risk:
  - Any external bookmark to `editor.html` will 404.
- Executed verification:
  - `Test-Path editor.html` returned `False`.
  - Search found no `editor.html` references.
- Not executed:
  - Git diff comparison.
- Rollback:
  - Restore from git or previous backup only if writer feature is explicitly requested again.

### `.git/config`

- Type: modified outside normal tracked files, based on current config
- Reason: Point local remote to new GitHub username.
- Behavior change:
  - `origin` now points to `https://github.com/Phillin-lrz/Phillin-lrz.github.io.git`.
- Potential risk:
  - `.git/config` is local-only and not committed.
  - Push still depends on Git being installed and authentication being valid.
- Executed verification:
  - File read directly.
- Not executed:
  - `git remote -v`, because `git` command is unavailable.
- Rollback:
  - Use `git remote set-url origin <old-or-correct-url>` when Git is available, or carefully edit `.git/config` manually.

### `AGENT_CONTEXT.md`

- Type: added
- Reason: Context sealing and anti-context-folding hardening.
- Behavior change:
  - No site runtime behavior.
- Potential risk:
  - Can become stale; update before cross-stage or multi-file changes.
- Executed verification:
  - Created in this sealing pass.
- Not executed:
  - Git diff comparison.
- Rollback:
  - Delete only if project adopts another equivalent handoff/context system.

### `AGENT_TODO.md`

- Type: added
- Reason: Preserve actionable next steps and validation requirements.
- Behavior change:
  - No site runtime behavior.
- Potential risk:
  - Can become stale.
- Executed verification:
  - Created in this sealing pass.
- Not executed:
  - Git diff comparison.
- Rollback:
  - Delete only if project adopts another equivalent task/handoff system.

### `AGENT_CHANGELOG.md`

- Type: added
- Reason: Preserve verified phase-one changes and limitations.
- Behavior change:
  - No site runtime behavior.
- Potential risk:
  - Not a substitute for real git diff; rerun git checks when available.
- Executed verification:
  - Created in this sealing pass.
- Not executed:
  - Git diff comparison.
- Rollback:
  - Delete only if project adopts another equivalent changelog.

### `AGENT_HANDOFF.md`

- Type: added after this changelog
- Reason: Concise future-agent recovery file.
- Behavior change:
  - No site runtime behavior.
- Potential risk:
  - Can become stale.
- Executed verification:
  - To be created in this sealing pass.
- Not executed:
  - Git diff comparison.
- Rollback:
  - Delete only if project adopts another equivalent handoff file.
