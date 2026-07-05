# AGENT_CHANGELOG

Last updated: 2026-07-05

This file now stores only recent, high-value change records. Older detailed history was moved to `AGENT_CHANGELOG_ARCHIVE.md` on 2026-07-04 to reduce default Codex token usage.

## 2026-07-05 Article Published - Cat

User provided `C:\Users\Phil Lin\Desktop\自己\自己总要写点东西\猫-20260705.docx` and asked to upload it as `一些思绪`.

- Extracted the Word document text and confirmed no embedded media files were present.
- Published it as a normal `一些思绪` article.
- Generated final static article file `article-cat-20260705.html`.
- Added metadata id `cat-20260705` to `assets/content.js`.
- Final title: `猫`.
- Publication date: `2026-07-05`.
- Refreshed HTML asset query strings to `bar-art-20260705-cat`.
- Visual verification was skipped by project preference.

Rollback:

- Delete `article-cat-20260705.html`.
- Remove the `cat-20260705` entry from `assets/content.js`.
- Restore the previous HTML asset query string from git.
- Remove this changelog entry if reverting the publication.

## 2026-07-05 Article Published - So Tired

User provided `C:\Users\Phil Lin\Desktop\自己\自己总要写点东西\20260705.docx`, specified the tag `一些思绪`, and chose the final title `好累。`.

- Extracted the Word document text and confirmed no embedded media files were present.
- Published it as a normal `一些思绪` article.
- Generated final static article file `article-so-tired.html`.
- Added metadata id `so-tired` to `assets/content.js`.
- Final title: `好累。`.
- Publication date: `2026-07-05`.
- Refreshed HTML asset query strings to `bar-art-20260705-so-tired`.
- Visual verification was skipped by project preference.

Rollback:

- Delete `article-so-tired.html`.
- Remove the `so-tired` entry from `assets/content.js`.
- Restore the previous HTML asset query string from git.
- Remove this changelog entry if reverting the publication.

## 2026-07-04 Bar Note Published - About Past

User provided `C:\Users\Phil Lin\Desktop\自己\自己总要写点东西\About Past-20260704.docx` and asked to upload the note.

- Extracted the Word document text and confirmed no embedded media files were present.
- Published it as a `吧台札记` because the piece is a short reflective note rather than a full life-log article.
- Generated final static note file `note-about-past.html`.
- Added metadata id `about-past` to `assets/content.js`.
- Final title: `About Past`.
- Mood: `回望`.
- Publication date: `2026-07-04`.
- Refreshed HTML asset query strings to `bar-art-20260704-about-past`.
- Visual verification was skipped by project preference.

Rollback:

- Delete `note-about-past.html`.
- Remove the `about-past` entry from `assets/content.js`.
- Restore the previous HTML asset query string from git.
- Remove this changelog entry if reverting the publication.

## 2026-07-04 Token Recovery Rule Slimming

User asked why token usage had grown and then approved the low-token state-file plan.

- Added `AGENT_BRIEF.md` as the lightweight startup entry.
- Moved the former full `AGENT_CHANGELOG.md` to `AGENT_CHANGELOG_ARCHIVE.md`.
- Recreated `AGENT_CHANGELOG.md` as a compact recent changelog.
- Updated `AGENTS.md` so default recovery reads `AGENT_BRIEF.md`, `AGENT_HANDOFF.md`, and `AGENT_TODO.md` first.
- Changed deeper reads to be task-based:
  - `AGENT_CONTEXT.md` for structural, architectural, uncertain, or multi-file work.
  - `AGENT_CHANGELOG.md` for recent rollback/change history.
  - `AGENT_CHANGELOG_ARCHIVE.md` for older history, detailed audits, old regressions, or older rollback needs.
- Updated durable state guidance in `AGENT_TODO.md` and `AGENT_HANDOFF.md`.
- Visual verification was skipped by project preference because this is an instruction/state-file change, not a frontend rendering change.

Rollback:

- Move `AGENT_CHANGELOG_ARCHIVE.md` back to `AGENT_CHANGELOG.md`.
- Delete `AGENT_BRIEF.md`.
- Restore the previous `AGENTS.md` startup procedure requiring all four state files every time.
- Remove this entry from the recreated changelog if reverting fully.

## 2026-07-04 Operation File Routing

User clarified that operation types should be grouped and each operation type should have its own `.md` file. User also required that Codex ask for confirmation before reading deeper files such as `AGENT_CONTEXT.md`, `AGENT_CHANGELOG.md`, or `AGENT_CHANGELOG_ARCHIVE.md`.

- Added seven operation files:
  - `AGENT_OP_CONTENT_PUBLISH.md`
  - `AGENT_OP_PLACES.md`
  - `AGENT_OP_PAGE_VISUAL.md`
  - `AGENT_OP_FRONTEND_LOGIC.md`
  - `AGENT_OP_DEPLOY_GIT.md`
  - `AGENT_OP_PROJECT_STATE.md`
  - `AGENT_OP_RECOVERY_AUDIT.md`
- Updated `AGENTS.md` so the workflow is brief/handoff/todo, git status/diff, matching operation file, target files, execution, verification, then one final changelog entry.
- Added a hard rule that `AGENT_CONTEXT.md`, `AGENT_CHANGELOG.md`, and `AGENT_CHANGELOG_ARCHIVE.md` require user confirmation before reading, unless the user explicitly asked to inspect that exact file.
- Updated `AGENT_BRIEF.md`, `AGENT_TODO.md`, `AGENT_HANDOFF.md`, and `AGENT_CONTEXT.md` to reflect operation-file routing.
- Visual verification was skipped by project preference because this is a project-rule/state-file change, not a frontend rendering change.

Rollback:

- Delete the seven `AGENT_OP_*.md` files.
- Remove operation-file routing and the deep-read confirmation rule from `AGENTS.md`, `AGENT_BRIEF.md`, `AGENT_TODO.md`, `AGENT_HANDOFF.md`, and `AGENT_CONTEXT.md`.
- Remove this changelog entry.
