# AGENT_BRIEF

Last updated: 2026-07-29

This is the lightweight startup file for Codex work in this repository. Read this file first, then read only the operation file and source files required by the task type.

## Project Snapshot

- Static GitHub Pages site for `Phil Lin的Bar`.
- No framework, backend, database, package manager, or build pipeline is configured.
- Main shared files:
  - `assets/content.js`: posts, notes, places, review metadata.
  - `assets/gripes.js`: right-side gripe data.
  - `assets/site.js`: rendering and interaction logic.
  - `assets/styles.css`: shared visual system.
- Public content is mostly static root HTML files.
- Article bodies should live in independent `article-*.html` files.
- Bar notes should live in independent `note-*.html` files.
- Place records use stable `place-*.html` archive pages plus independent visit/article pages.

## Current Operating Rules

- Default to low-token recovery: read this file, `AGENT_HANDOFF.md`, and `AGENT_TODO.md` first.
- Then choose the matching operation file:
  - `AGENT_OP_CONTENT_PUBLISH.md`
  - `AGENT_OP_PLAYLISTS.md`
  - `AGENT_OP_PLACES.md`
  - `AGENT_OP_PAGE_VISUAL.md`
  - `AGENT_OP_FRONTEND_LOGIC.md`
  - `AGENT_OP_DEPLOY_GIT.md`
  - `AGENT_OP_PROJECT_STATE.md`
  - `AGENT_OP_RECOVERY_AUDIT.md`
- Do not read `AGENT_CONTEXT.md`, `AGENT_CHANGELOG.md`, or `AGENT_CHANGELOG_ARCHIVE.md` by default.
- Before reading `AGENT_CONTEXT.md`, `AGENT_CHANGELOG.md`, or `AGENT_CHANGELOG_ARCHIVE.md`, ask the user for confirmation and name the exact file plus reason.
- Skip visual browser verification by project preference unless the user explicitly asks for it or a higher-priority instruction requires it.
- Keep using `git status --short`, `git diff --stat`, and `git diff -- .` for recovery/diff checks.
- Run `node --check assets/site.js`, `node --check assets/content.js`, and `node --check assets/gripes.js` when those files are relevant.
- Do not use Node REPL as a routine fallback for blocked `node --check` or browser verification.

## Current State To Remember

- Current general asset query string is `bar-art-20260729-clean-background`; verify current files before changing cache strings.
- `BAR_PLACES` exists and powers the `reviews.html` / private-place map flow.
- Sober Company-Ash, Making Gelato, Q Taro, ZOOMINN, and DEMO have place/visit structures.
- `gallery.html` now renders 38 location-group photos from `assets/gallery.js`, with optimized images under `assets/gallery/<place-slug>/` and generated `gallery-*.html` detail pages for each retained photo.
- `playlist.html` must remain a playlist index page; currently only `playlist-writing.html` is kept as a playlist detail page.
- The explicit GitHub Pages workflow exists at `.github/workflows/pages.yml`, with `.nojekyll` at the root.
- Word publishing tooling was removed on 2026-07-01; future publishing is direct static file editing unless the user asks to restore tooling.
- `AGENT_CHANGELOG_ARCHIVE.md` contains the full pre-2026-07-04 historical changelog.

## Safe Default Workflow

1. Read `AGENT_BRIEF.md`, `AGENT_HANDOFF.md`, and `AGENT_TODO.md`.
2. Check `git status --short` and `git diff --stat`.
3. Choose and read the matching `AGENT_OP_*.md` file(s).
4. Read target source files directly.
5. Ask the user before any deeper state-file read.
6. Make the smallest relevant change.
7. Run only relevant checks.
8. Write one concise `AGENT_CHANGELOG.md` entry after all operations finish when the project state actually changed.

## Current Known Risks

- Some existing state files contain mojibake text inherited from earlier Windows/encoding issues; do not fix broad text encoding unless the user asks.
- Visual layout risk remains whenever CSS or frontend markup changes because visual verification is skipped by default.
- The online GitHub Pages deployment still needs confirmation after pushes.
