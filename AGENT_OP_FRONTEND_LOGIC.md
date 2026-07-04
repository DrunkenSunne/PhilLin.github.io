# AGENT_OP_FRONTEND_LOGIC

Use this operation file for JavaScript rendering, data behavior, and frontend logic.

## Covers

- Lists not rendering.
- Filters, pagination, sorting, or score calculations.
- Gripe rail behavior.
- Place-card or visit-receipt rendering.
- Compatibility between `assets/site.js` and data files.
- JS-driven markup changes.

## Default Read Set

Read only:

- `AGENT_BRIEF.md`
- `AGENT_HANDOFF.md`
- `AGENT_TODO.md`
- this file
- `assets/site.js`
- the relevant data file: `assets/content.js` or `assets/gripes.js`
- the relevant HTML page only if needed to inspect data attributes or containers

Do not default-read `AGENT_CONTEXT.md`, `AGENT_CHANGELOG.md`, or `AGENT_CHANGELOG_ARCHIVE.md`.

## Deep Read Gate

Before reading any deeper state file, ask the user for confirmation and name the exact file plus reason.

Allowed only when:

- The logic depends on an older architectural decision not visible in current files.
- The user asks why a behavior was implemented.
- A regression must be traced across old changes.
- Current code contradicts brief/handoff/todo rules.

`AGENT_CHANGELOG_ARCHIVE.md` is only allowed for user-confirmed old regression tracing.

## Common Target Files

- `assets/site.js`
- `assets/content.js`
- `assets/gripes.js`
- pages with `data-*` render targets

## Verification

- Run `node --check assets/site.js` when `assets/site.js` changes.
- Run `node --check assets/content.js` when `assets/content.js` changes.
- Run `node --check assets/gripes.js` when `assets/gripes.js` changes.
- Search for all affected render targets and data field names.
- Do not use Node REPL as routine fallback.

## State Logging

At the end of the whole operation, write one concise entry to `AGENT_CHANGELOG.md` for behavior changes.
Update `AGENT_HANDOFF.md` only for behavior rules future work must preserve.
