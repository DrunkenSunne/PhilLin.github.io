# AGENT_OP_PLAYLISTS

Use this operation file for maintaining the public playlist section.

## Covers

- Adding, removing, or replacing playlist pages.
- Updating `playlist.html` and any `playlist-*.html` detail pages.
- Updating homepage references that describe the playlist section.
- Refreshing only the specific shared-asset query string whose underlying asset changed.

## Default Read Set

Read only:

- `AGENT_BRIEF.md`
- this file
- the target playlist HTML files
- shared HTML pages that link to or describe the playlist section

Read `AGENT_HANDOFF.md` only for unfinished playlist continuation. Read `AGENT_TODO.md` only for playlist planning or a pending-work audit.

Do not default-read `AGENT_CONTEXT.md`, `AGENT_CHANGELOG.md`, or `AGENT_CHANGELOG_ARCHIVE.md`.

## Deep Read Gate

Before reading any deeper state file, ask the user for confirmation and name the exact file plus reason.

Allowed only when:

- The playlist behavior conflicts with the current files.
- The user asks to restore an older playlist.
- A rollback or historical audit becomes part of the task.

## Verification

- Search for stale links to deleted `playlist-*.html` files.
- Search for stale playlist names when replacing all playlists.
- Run JavaScript syntax checks for shared scripts if asset query strings or linked shared data changed.
- Skip visual browser verification by project preference unless the user explicitly asks.

## State Logging

At the end of the operation, write one concise entry to `AGENT_CHANGELOG.md`.
Update `AGENT_HANDOFF.md` if future work needs to remember the playlist set.
