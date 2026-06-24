# AGENT_TODO

Last updated: 2026-06-21

Use this file before starting phase two or any future multi-file work. Do not rely on chat history as the only source of truth.

## 1. Phase One Completed

- [x] Confirmed repository is a static site with root HTML pages and shared assets.
- [x] Confirmed `index.html` brands site as `Phil Lin的Bar`.
- [x] Confirmed navigation includes `首页`, `文章`, `酒评`, `摄影作品`, `友链`, `关于我`.
- [x] Confirmed no `撰写` nav entry remains in HTML pages.
- [x] Confirmed `write.html` and `editor.html` are deleted from the working tree.
- [x] Confirmed `assets/site.js` no longer contains writer/auth/editor functions.
- [x] Confirmed `assets/styles.css` no longer contains writer/auth/editor styles.
- [x] Confirmed `assets/content.js` uses lightweight article index entries.
- [x] Deleted the placeholder public article index `to-be-continue`.
- [x] Deleted `article-to-be-continue.html`.
- [x] Confirmed tag archive pages exist:
  - `tag-lab.html`
  - `tag-thoughts.html`
  - `tag-recommendations.html`
- [x] Confirmed `posts.html` has tag filter buttons for all three tags.
- [x] Confirmed `friends.html` contains StarCried and CrescentYves friend cards and avatars.
- [x] Added right-side `吐槽` rail rendering from static `window.BAR_GRIPES` data.
- [x] Published first gripe entry with second-level timestamp.
- [x] Split gripe data into `assets/gripes.js` so `assets/content.js` stays focused on article/review metadata.
- [x] Confirmed `reviews.html` and `gallery.html` exist with placeholder content.
- [x] Confirmed `.git/config` remote URL is `https://github.com/Phillin-lrz/Phillin-lrz.github.io.git`.
- [x] Confirmed JavaScript syntax for `assets/site.js` and `assets/content.js` in the final check.

## 2. Phase-One Remaining Issues

- [ ] Run `git status --short` once Git is available; current environment cannot find `git`.
- [ ] Run `git diff --stat` and `git diff -- .` once Git is available; current environment cannot find `git`.
- [ ] Keep attempting relevant `node --check` commands when JavaScript files change; if Node is unavailable, record the limitation.
- [ ] Do not use Node REPL as a routine fallback for blocked `node --check` or browser verification.
- [ ] Visual verification is skipped by current project preference unless the user explicitly asks for it later or a higher-priority instruction requires it.
- [ ] If visual verification is skipped after frontend changes, report residual visual risk instead of claiming browser/layout verification.
- [ ] Verify `assets/cocktail-hero.png` and `assets/hero-workspace.png` are truly unused before deleting or keeping intentionally.
- [ ] Decide whether `article.html` should remain as compatibility fallback or be removed after static article pages are fully adopted.
- [x] Decide whether `BAR_REVIEWS` should render `reviews.html` dynamically or remain a future data hook; as of 2026-06-20 `reviews.html` renders Cellar / 酒柜 cards from `window.BAR_REVIEWS`.
- [ ] Verify the online GitHub Pages deployment reflects local files after push.

## 3. Phase-Two Candidate Tasks

- [x] Published 2026-06-24 life log from schedule screenshot:
  - Generated final article file `article-after-exam-still-held.html`.
  - Deleted review-only `preview-20260624.html`.
  - Added one metadata object to `assets/content.js`.
  - User supplied source as an image schedule table and asked Codex to write/design the life log.
  - Final tag is `生活日志`.
  - Final title is `考完以后，也没有完全散掉`.
  - Publication date is `2026-06-24`, based on the current date and schedule date.
  - Experimental details were intentionally kept vague as `实验室工作` / `细胞状态确认`.
  - User requested the preview endnote be changed before publishing; final endnote is restrained and non-inspirational.
  - Refreshed HTML asset query strings to avoid stale cached `assets/content.js`.
- [x] Published 2026-06-23 user-provided life log text:
  - Generated final article file `article-one-side-cannot-fall.html`.
  - Deleted review-only `preview-20260623.html`.
  - Added one metadata object to `assets/content.js`.
  - User supplied tag `生活日志`.
  - Final title is `起码一边不能倒下`.
  - Publication date is `2026-06-23`, based on the current date and the user's `今天的生活日志` wording.
  - No images were provided.
  - Refreshed HTML asset query strings to avoid stale cached `assets/content.js`.
- [x] Published `C:\Users\Phil Lin\Desktop\临时用\日志.docx`:
  - Generated final article file `article-experiment-review-double-run.html`.
  - Deleted review-only `preview-20260622.html`.
  - Added one metadata object to `assets/content.js`.
  - User supplied tag `生活日志`.
  - Final title is `实验和复习双开的一天`.
  - Publication date is `2026-06-22`, taken from the first paragraph in the Word document.
  - No embedded media files were found in the Word document.
- [x] Published `C:\Users\Phil Lin\Desktop\临时用\1.docx`:
  - Generated final article file `article-good-luck-day.html`.
  - Deleted review-only `preview-20260621.html`.
  - Added one metadata object to `assets/content.js`.
  - User supplied tag `生活日志`.
  - Final title is `祝我好运的一天`.
  - Publication date is `2026-06-21`, taken from the first paragraph in the Word document.
  - No embedded media files were found in the Word document.
- [x] Implement broad abstract cocktail-bar visual redesign:
  - Home page becomes a bar-menu style board.
  - Secondary pages present as different drink identities.
  - Mouse interaction includes a bar cursor and menu drink hover labels.
  - Existing copy mostly preserved.
  - Friend-link avatars restored unchanged per user clarification.
  - Screenshots not generated because user chose direct `.html` review.
- [x] Published approved Word article preview:
  - Confirmed `preview-20260611.html` was acceptable.
  - Generated final static article HTML at `article-first-words-on-the-bar.html`.
  - Added one metadata object to `assets/content.js` with tag `一些思绪`.
  - Deleted `preview-20260611.html`.
  - Verified generated article path from metadata.
- [ ] Implement broader Word-to-article conversion workflow:
  - Extract text and images from a provided `.docx`.
  - Save images to `assets/posts/<article-id>/`.
  - Generate `article-<article-id>.html`.
  - Add one metadata object to `assets/content.js`.
  - Verify generated article path from `posts.html`.
- [x] Published approved 2026-06-18 Word article preview:
  - Confirmed `preview-20260618.html` was acceptable.
  - Generated final static article HTML at `article-two-bottles-writing-touch.html`.
  - Added one metadata object to `assets/content.js` with tag `一些思绪`.
  - Deleted `preview-20260618.html`.
  - Verified generated article path from metadata.
- [x] Add a reusable article HTML template for generated articles, based on `_drafts/article-format-reference.html`.
- [x] Make `reviews.html` render from `window.BAR_REVIEWS` instead of hardcoded placeholder cards.
- [x] Add lightweight `tonight.html` page combining Now / 今晚状态 and Aftertaste / 余味.
- [x] Add lightweight `playlist.html` page for night playlist and atmosphere references without players, lyrics, or autoplay.
- [x] Reframe `reviews.html` as Cellar / 酒柜 and render structured cards from `window.BAR_REVIEWS`.
- [x] Strengthen homepage copy/entry structure while preserving badge, `Phil Lin的Bar`, and `I flutter in circle never landing on nothing`.
- [x] Improve article long-form reading styles and mobile responsiveness in shared CSS.
- [x] Improve art completion after user feedback: CSS-only homepage atmosphere layer, richer rainy-glass/menu-board material, stronger badge glow, and updated asset cache string `bar-art-20260620-fix2`.
- [x] Fix mouse effect alignment by centering `.bar-cursor` on the pointer and updating asset cache string to `bar-art-20260620-fix3`.
- [x] Acceptance rework: checked live Pages content and Actions deployment, added explicit mobile breakpoints, completed reduced-motion/mobile motion suppression, refined Tonight/About copy, added Cellar noscript fallback, and updated asset cache string to `bar-art-20260620-fix4`.
- [x] Fix mouse cursor reentry/scroll follow: clear hidden state on fresh pointer movement, sync cursor on wheel/scroll, and update asset cache string to `bar-art-20260620-fix5`.
- [x] Recover corrupted bitmap assets after badge and friend avatars disappeared; restore valid historical binaries for all five `assets/` bitmap images and update cache string to `bar-art-20260620-fix6`.
- [x] Split `playlist.html` cards into dedicated playlist detail pages, with each detail page containing its own song list.
- [x] Fix mouse cursor scroll-offset drift by removing body transform movement and updating the fixed cursor with viewport `left` / `top` coordinates.
- [x] Polish mobile `index.html` layout with mobile-only nav, hero, and menu-card refinements while leaving desktop rules untouched.
- [x] Audit and fix page drink badge consistency: align visible English names with glyph/page identities and add a dedicated French 75 glyph.
- [x] Rework homepage menu and top-level page drink identities so all public navigation destinations appear in the menu and no top-level page drink identity is duplicated.
- [x] Simplify the homepage article/category menu into one grouped Martini-family card with three distinct child variants.
- [x] Fix tablet Index menu layout and mobile/tablet drink glyph alignment by keeping glyph internals at canonical size.
- [x] Fix Edge/non-Chrome cursor effect by avoiding coarse-pointer desktop suppression and adding mouse event fallbacks.
- [x] Fix tablet Index hero intro by collapsing the desktop three-column menu intro across iPad-sized widths.
- [x] Add a Hanky Panky / 吧台札记 column scaffold:
  - Added `notes.html` as the note index.
  - Added `window.BAR_NOTES` in `assets/content.js`.
  - Added list rendering in `assets/site.js`.
  - Added `_drafts/note-format-reference.html` for individual note pages.
  - Kept the top navigation unchanged; the homepage entry is only inside Martini Flight variants.
  - Added mobile/tablet-aware styles and a Martini-family Hanky Panky glyph.
- [x] Upgrade drink badges toward A+C:
  - Applied blueprint-style structure plus recognizable ingredient cues to all current public drink badge glyphs.
  - Also covered retained CSS fallback glyphs such as Highball, Paloma, Negroni, Coupe, Rocks, and Paper Plane.
  - Kept internal glyph geometry at `5.2rem` with responsive `transform: scale(...)`.
  - Refreshed asset query string to `bar-art-20260624-glyphs`.
- [ ] If gripe count grows large, revisit scheme 3 or 4 for the gripe rail: paginated static files or JSON on-demand loading.
- [ ] Add the first real `note-*.html` page when the user provides a bar-note text.
- [ ] Add real photography entries to `gallery.html` and decide image folder structure, likely `assets/gallery/`.
- [ ] Add better empty-state text for tag pages with no articles.
- [x] Add a small documentation section showing how to manually add a new static article.
- [ ] Reassess whether `article.html` dynamic fallback is still needed after static article generation is stable.
- [ ] Audit all pages for consistent footer text and theme toggle labels.
- [ ] Consider moving repeated header/nav/footer into a generation workflow only if user approves introducing tooling.

## 4. Current Blockers

- [x] `git` is available in the current shell as of 2026-06-20; `git status --short`, `git diff --stat`, and `git diff -- .` can be run.
- [ ] In-app browser automation has been unreliable/blocked; visual verification cannot be claimed until a browser check succeeds.
- [x] One Word document has been published as `article-first-words-on-the-bar.html`.
- [x] One Word document has been published as `article-two-bottles-writing-touch.html`.
- [x] User approved the 2026-06-20 style strengthening and lightweight structure optimization scope.

## 5. Needs Human Confirmation

- [ ] Confirm whether phase two should start with Word-to-article conversion.
- [ ] Confirm whether article file names should use English slugs, pinyin, or generated ids.
- [ ] Confirm whether new article images should be compressed/resized or preserved as-is.
- [ ] Confirm whether unused assets `assets/cocktail-hero.png` and `assets/hero-workspace.png` may be deleted.
- [ ] Confirm whether the public site title should remain `Phil Lin的Bar | 酒鬼医学生的博客`.
- [ ] Confirm whether `article.html?id=...` should remain publicly available as fallback.
- [ ] Confirm whether review/gallery content should stay placeholder until manually authored.

## 6. Validation Steps That Must Not Be Skipped

- [ ] Before future development, read:
  - `AGENT_CONTEXT.md`
  - `AGENT_TODO.md`
  - `AGENT_CHANGELOG.md`
  - `AGENT_HANDOFF.md`
  - `README.md`
- [ ] Attempt `git status --short`; record if unavailable.
- [ ] Attempt `git diff --stat`; record if unavailable.
- [ ] Run JavaScript syntax checks:
  - `node --check assets/site.js`
  - `node --check assets/content.js`
  - `node --check assets/gripes.js`
- [ ] Search for accidental writer resurrection:
  - `write.html`
  - `editor.html`
  - `write-link`
  - `data-auth`
  - `data-editor`
  - `WRITER`
  - `撰写`
- [ ] Search for stale cache query strings before finalizing:
  - old values such as `bar-export-20260610` or earlier.
  - previous asset version strings such as `bar-art-20260623-post3`.
- [ ] Skip browser visual verification by project preference unless the user explicitly asks for it later or a higher-priority instruction requires it.
- [ ] If browser visual verification is requested or required, browser-check at least:
  - `index.html`
  - `posts.html`
  - one tag page
  - one public article page after a new article is added
  - `friends.html`
- [ ] If Word conversion is implemented, verify:
  - generated article HTML opens
  - all extracted image paths resolve
  - `assets/content.js` syntax remains valid
  - article appears in home recent posts when date is newest
  - article appears in the correct tag page

## 7. Recommended First Step Next Time

1. Read `AGENT_HANDOFF.md`.
2. Read this file and `AGENT_CONTEXT.md`.
3. Run or attempt:
   - `git status --short`
   - `git diff --stat`
   - `node --check assets/site.js`
   - `node --check assets/content.js`
   - `node --check assets/gripes.js`
4. Ask the user to confirm the exact phase-two objective before changing code.
