# AGENT_HANDOFF

Last updated: 2026-08-30

Use this file only for unfinished-work continuity, dirty-worktree recovery, or compacted/uncertain sessions. Completed history belongs in `AGENT_CHANGELOG.md` and `AGENT_CHANGELOG_ARCHIVE.md`.

## Current Handoff State

- `Phil Lin的Bar` is a static GitHub Pages site with root HTML pages and shared files under `assets/`.
- A new gripe about workload changes and not wanting to enter the cell room is committed locally as `6189616`.
- Publishing is unfinished: `git push origin main` failed because HTTPS credentials were unavailable, and SSH authentication was also unavailable.
- The working tree was clean immediately after commit `6189616`; only durable state files changed afterward to document the blocked push.

## Current Cache Policy

- Cache versions are asset-scoped; do not refresh every asset when only one changes.
- Shared CSS, badge, and `assets/site.js` retain `bar-art-20260824-ten-pm`.
- `assets/gripes.js` uses `bar-gripe-20260830-cell-room` on all 120 current HTML consumers.
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

- Visual layout is not browser-verified by default.
- Local `main` is ahead by the gripe publication commit plus the state follow-up commit once created; online GitHub Pages remains unchanged until authenticated push succeeds.
- Some old state text may contain inherited mojibake; do not perform broad encoding cleanup without a separate request.

## Next Safe Step

Restore GitHub authentication, push local `main` to `origin/main`, then verify the GitHub Pages deployment. The content and cache-reference changes already passed local syntax, diff, and deterministic reference checks.
