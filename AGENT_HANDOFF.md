# AGENT_HANDOFF

Last updated: 2026-08-24

Use this file only for unfinished-work continuity, dirty-worktree recovery, or compacted/uncertain sessions. Completed history belongs in `AGENT_CHANGELOG.md` and `AGENT_CHANGELOG_ARCHIVE.md`.

## Current Handoff State

- `Phil Lin的Bar` is a static GitHub Pages site with root HTML pages and shared files under `assets/`.
- No content-publication task is currently unfinished.
- The 2026-08-24 token-reduction pass changed project instructions, state routing, verification-output policy, and `assets/content.js` loading scope.
- The pass is intentionally uncommitted and unpushed unless the user separately requests Git publication.

## Current Cache Policy

- Cache versions are asset-scoped; do not refresh every asset when only one changes.
- Shared CSS, badge, `assets/site.js`, and `assets/gripes.js` currently retain `bar-art-20260824-ten-pm` unless that specific resource changes.
- `assets/content.js` uses `bar-content-20260824-ten-pm` on exactly eight consumer pages:
  - `article.html`
  - `index.html`
  - `notes.html`
  - `posts.html`
  - `reviews.html`
  - `tag-lab.html`
  - `tag-recommendations.html`
  - `tag-thoughts.html`
- Static article, note, place, gallery, playlist, gripe-detail, and gallery-detail pages do not need `assets/content.js` unless a documented `BAR_*` rendering hook is added.
- `assets/gripes.js` remains global because `assets/site.js` may inject the gripe rail on any public page.

## Current Verification Policy

- Baseline checks are `git status --short`, `git diff --stat`, and `git diff --check`.
- Inspect semantic files with targeted diffs.
- For more than 400 changed lines, audit bulk mechanical edits with deterministic counts and changed-line allowlists; print only unexpected lines or failing hunks.
- Run `node --check` only for relevant JavaScript files.
- DOCX source-to-HTML checks should return title, counts, and mismatches rather than repeated full extraction output.
- Browser visual verification remains skipped by project preference unless explicitly requested or required by a higher-priority instruction.

## Known Risks

- The current cache/script cleanup changes many HTML files once; static allowlist verification is required before completion.
- Visual layout is not browser-verified by default.
- Online GitHub Pages freshness still requires a push followed by remote deployment verification.
- Some old state text may contain inherited mojibake; do not perform broad encoding cleanup without a separate request.

## Next Safe Step

If resuming this exact pass, check Git status/stat, run the structured content-script audit, inspect targeted instruction/state diffs, and finish the relevant syntax/reference checks. For later ordinary publishing, start from `AGENT_BRIEF.md` and `AGENT_OP_CONTENT_PUBLISH.md`; do not read historical state unless its gate is satisfied.
