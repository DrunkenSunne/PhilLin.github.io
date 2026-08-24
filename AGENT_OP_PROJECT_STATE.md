# AGENT_OP_PROJECT_STATE

Use this operation file for project rules, Codex state files, and token-usage policy.

## Covers

- `AGENTS.md`.
- `AGENT_BRIEF.md`.
- `AGENT_TODO.md`.
- `AGENT_HANDOFF.md`.
- `AGENT_CHANGELOG.md`.
- operation files: `AGENT_OP_*.md`.
- Token-reduction rules, logging rules, and state-file organization.

## Default Read Set

Read only:

- `AGENT_BRIEF.md`
- this file
- the specific project-state files being edited

Read `AGENT_HANDOFF.md` when continuity/recovery is involved and `AGENT_TODO.md` when pending-work organization is involved.

Do not default-read `AGENT_CONTEXT.md`, `AGENT_CHANGELOG.md`, or `AGENT_CHANGELOG_ARCHIVE.md`.

## Deep Read Gate

Before reading any deeper state file, ask the user for confirmation and name the exact file plus reason.

Allowed only when:

- The user explicitly asks to inspect current context or changelog history.
- A state-file rule conflicts with another state-file rule.
- A rollback of project-rule changes is requested.
- The requested change cannot be made safely from the brief/handoff/todo plus target files.

`AGENT_CHANGELOG_ARCHIVE.md` is only allowed for user-confirmed archival or rollback work.

## Common Target Files

- `AGENTS.md`
- `AGENT_BRIEF.md`
- `AGENT_TODO.md`
- `AGENT_HANDOFF.md`
- `AGENT_CONTEXT.md`
- `AGENT_CHANGELOG.md`
- `AGENT_CHANGELOG_ARCHIVE.md`
- `AGENT_OP_*.md`

## Verification

- Run `git status --short`, `git diff --stat`, and `git diff --check`.
- Inspect targeted state-file diffs; for a large archival rewrite, report line/byte counts and unexpected content rather than dumping the full historical diff.
- No JS syntax check is needed unless JS files change.
- Skip visual browser verification because state files do not affect page rendering.

## State Logging

At the end of the whole operation, write one concise entry to `AGENT_CHANGELOG.md`.
Update `AGENT_BRIEF.md`, `AGENT_TODO.md`, and `AGENT_HANDOFF.md` when the workflow itself changes.
Update `AGENT_CONTEXT.md` only for durable project-level rules, and only when necessary.
