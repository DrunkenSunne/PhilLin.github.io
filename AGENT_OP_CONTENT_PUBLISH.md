# AGENT_OP_CONTENT_PUBLISH

Use this operation file for publishing new site content.

## Covers

- New article pages: `article-*.html`.
- New bar notes: `note-*.html`.
- New gripe entries in `assets/gripes.js`.
- Content created from pasted text, Word text, screenshots, or user-provided source material.
- Metadata updates in `assets/content.js`.
- Asset query string refreshes when content data changes.

## Default Read Set

Read only:

- `AGENT_BRIEF.md`
- this file
- the target content/data files needed for the task

Read `AGENT_HANDOFF.md` only for unfinished or dirty-worktree continuation. Read `AGENT_TODO.md` only when category/phase planning is genuinely needed.

Do not default-read `AGENT_CONTEXT.md`, `AGENT_CHANGELOG.md`, or `AGENT_CHANGELOG_ARCHIVE.md`.

## Deep Read Gate

Before reading any deeper state file, ask the user for confirmation and name the exact file plus reason.

Allowed only when:

- The user asks to follow or restore an older publishing rule.
- The content boundary is unclear after checking current target files.
- Current files conflict with the brief/handoff/todo state.
- A rollback or historical audit becomes part of the task.

`AGENT_CHANGELOG_ARCHIVE.md` is not allowed for normal publishing.

## Common Target Files

- `assets/content.js`
- `assets/gripes.js`
- `article-*.html`
- `note-*.html`
- `gripe-*.html`
- the eight `assets/content.js` consumer pages when content-data cache strings must refresh: `article.html`, `index.html`, `notes.html`, `posts.html`, `reviews.html`, `tag-lab.html`, `tag-recommendations.html`, and `tag-thoughts.html`
- `assets/posts/` or `assets/gripes/` when media is involved

## Verification

- Run `node --check assets/content.js` when `assets/content.js` changes.
- Run `node --check assets/gripes.js` when `assets/gripes.js` changes.
- Run `node --check assets/site.js` only when rendering logic changes.
- Use file-level checks and searches for links, ids, and asset query strings.
- Cache-bust only the resource that changed. A post/note/place metadata change updates only the `assets/content.js` query on its eight consumer pages; do not refresh CSS, badge, gripe, or site-script queries unless those assets changed.
- Static article, note, place, gallery, playlist, and detail pages must not load `assets/content.js` unless they contain a documented `BAR_*` rendering hook.
- Extract DOCX content once. Preserve paragraph and semantic separator order, compare source-to-HTML locally, and report counts plus mismatches instead of printing the full extraction repeatedly.
- Skip visual browser verification by project preference unless the user explicitly asks.

## State Logging

At the end of the whole operation, write one concise entry to `AGENT_CHANGELOG.md`.
Update `AGENT_HANDOFF.md` only if future work needs to remember the published item.
Update `AGENT_BRIEF.md` only for durable workflow-level facts, not every post.
