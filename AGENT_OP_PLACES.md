# AGENT_OP_PLACES

Use this operation file for private-place records and visit timelines.

## Covers

- New or updated places in `BAR_PLACES`.
- New visit records for bars, restaurants, dessert shops, cafes, or other private places.
- Place archive pages: `place-*.html`.
- Visit/article pages tied to a place.
- Scores, dishes, drinks, visit labels, visit dates, and repeat-visit metadata.

## Default Read Set

Read only:

- `AGENT_BRIEF.md`
- `AGENT_HANDOFF.md`
- `AGENT_TODO.md`
- this file
- `assets/content.js`
- the relevant `place-*.html` and `article-*.html` files
- `assets/site.js` / `assets/styles.css` only if rendering or styling must change

Do not default-read `AGENT_CONTEXT.md`, `AGENT_CHANGELOG.md`, or `AGENT_CHANGELOG_ARCHIVE.md`.

## Deep Read Gate

Before reading any deeper state file, ask the user for confirmation and name the exact file plus reason.

Allowed only when:

- Repeat-visit structure is disputed or unclear from current files.
- The user asks why an older place decision was made.
- A prior score/content correction must be traced historically.
- A rollback or regression investigation is requested.

`AGENT_CHANGELOG_ARCHIVE.md` is only allowed for user-confirmed old-history investigations.

## Common Target Files

- `assets/content.js`
- `place-*.html`
- `article-*.html`
- `reviews.html`
- `assets/site.js`
- `assets/styles.css`

## Verification

- Run `node --check assets/content.js` when place or post metadata changes.
- Run `node --check assets/site.js` when place-card rendering changes.
- Search for matching `placeId`, `visitId`, URLs, scores, drinks, and dishes.
- Skip visual browser verification by project preference unless the user explicitly asks.

## State Logging

At the end of the whole operation, write one concise entry to `AGENT_CHANGELOG.md`.
Update `AGENT_HANDOFF.md` when a new place structure or important correction should persist.
Update `AGENT_BRIEF.md` only when the place workflow itself changes.
