# AGENT_OP_RECOVERY_AUDIT

Use this operation file for rollback, old-history lookup, regression tracing, and audits.

## Covers

- Reverting or reconstructing an older state.
- Explaining why an old decision was made.
- Tracing a regression across previous changes.
- Comparing current behavior with older project records.
- Explicit requests to inspect archived history.

## Default Read Set

Read only:

- `AGENT_BRIEF.md`
- `AGENT_HANDOFF.md`
- `AGENT_TODO.md`
- this file
- current target files and git diff/status

Do not default-read `AGENT_CONTEXT.md`, `AGENT_CHANGELOG.md`, or `AGENT_CHANGELOG_ARCHIVE.md`.

## Deep Read Gate

Before reading any deeper state file, ask the user for confirmation and name the exact file plus reason.

Possible requests:

- `AGENT_CONTEXT.md` for durable architecture or rule confirmation.
- `AGENT_CHANGELOG.md` for recent rollback notes.
- `AGENT_CHANGELOG_ARCHIVE.md` for old detailed history.

This is the only operation type where `AGENT_CHANGELOG_ARCHIVE.md` is commonly relevant, but it still requires explicit user confirmation before reading.

## Common Target Files

- Any file involved in the requested rollback or audit.
- Git diff/status output.
- State files only after user-confirmed need.

## Verification

- Use `git status --short`, `git diff --stat`, and `git diff -- .`.
- Run JS syntax checks only if JS files change.
- Do not use destructive git commands unless the user explicitly requests them.
- Clearly separate confirmed facts, assumptions, risks, and next safe action.

## State Logging

At the end of the whole operation, write one concise entry to `AGENT_CHANGELOG.md` if files changed or a durable audit conclusion should persist.
Do not write to `AGENT_CHANGELOG_ARCHIVE.md` during normal recovery.
