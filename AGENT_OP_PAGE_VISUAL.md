# AGENT_OP_PAGE_VISUAL

Use this operation file for page copy, markup, style, layout, and responsive adjustments.

## Covers

- Page text, navigation labels, titles, and button copy.
- Small HTML structure changes.
- CSS style and layout changes.
- Mobile/tablet/desktop fit fixes.
- Visual polish that does not primarily change data rendering logic.

## Default Read Set

Read only:

- `AGENT_BRIEF.md`
- `AGENT_HANDOFF.md`
- `AGENT_TODO.md`
- this file
- the target HTML file(s)
- `assets/styles.css`
- `assets/site.js` only if the visual change depends on JS-created markup

Do not default-read `AGENT_CONTEXT.md`, `AGENT_CHANGELOG.md`, or `AGENT_CHANGELOG_ARCHIVE.md`.

## Deep Read Gate

Before reading any deeper state file, ask the user for confirmation and name the exact file plus reason.

Allowed only when:

- The user asks to preserve or restore an older visual rule.
- Current files do not explain a cross-page design convention.
- The change affects global navigation, article format, or site identity.
- A visual regression must be traced to old history.

`AGENT_CHANGELOG_ARCHIVE.md` is not allowed for routine styling.

## Common Target Files

- `index.html`
- `posts.html`
- `reviews.html`
- `article-*.html`
- `note-*.html`
- `place-*.html`
- `assets/styles.css`

## Verification

- Use file-level checks, searches, and static reasoning.
- Run JS syntax checks only if JS files change.
- Skip browser visual verification by project preference unless the user explicitly asks.
- Report residual visual risk when layout or CSS changes are not visually checked.

## State Logging

At the end of the whole operation, write one concise entry to `AGENT_CHANGELOG.md` only if the change is durable or cross-page.
For tiny copy fixes, changelog can be skipped unless the user asks or project rules changed.
