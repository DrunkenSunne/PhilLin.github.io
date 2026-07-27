# Codex project instructions

This repository is a static GitHub Pages website for `Phil Lin的Bar`.

Use this file as the primary Codex project-level instruction entry. Keep business documentation in `README.md`; keep durable agent state in the `AGENT_*.md` files.

## Codex context preservation rules

This project uses repository-level state files to prevent loss of important information during long Codex sessions, automatic context compaction, summarization, or truncated conversation history.

### Communication rule

Codex must not send optional commentary. Only send user-facing messages when they are necessary for clarification, blocker reporting, or final completion.

Before starting any non-trivial work in this project, Codex must first read the low-token state entry:

- `AGENT_BRIEF.md`
- `AGENT_HANDOFF.md`
- `AGENT_TODO.md`

Codex must treat these files as the durable project memory. Chat history alone is not a reliable source of truth.

After reading the low-token state entry, Codex must choose the matching operation file(s) and read only those operation files before task-specific source files:

- `AGENT_OP_CONTENT_PUBLISH.md`
- `AGENT_OP_PLAYLISTS.md`
- `AGENT_OP_PLACES.md`
- `AGENT_OP_PAGE_VISUAL.md`
- `AGENT_OP_FRONTEND_LOGIC.md`
- `AGENT_OP_DEPLOY_GIT.md`
- `AGENT_OP_PROJECT_STATE.md`
- `AGENT_OP_RECOVERY_AUDIT.md`

Operation files are routing files for reducing token use. They must not be used as broad permission to read deeper history.

Read deeper state files only when the chosen operation file allows it and the user has confirmed the read:

- Read `AGENT_CONTEXT.md` for multi-file structural work, architecture questions, uncertain project rules, or work that may affect older decisions.
- Read `AGENT_CHANGELOG.md` for recent change history, rollback notes, or regression checks.
- Read `AGENT_CHANGELOG_ARCHIVE.md` only for older history, detailed audits, old regressions, or rollback beyond the current changelog.

Before reading `AGENT_CONTEXT.md`, `AGENT_CHANGELOG.md`, or `AGENT_CHANGELOG_ARCHIVE.md`, Codex must ask the user for confirmation and state the exact file and reason. If the user explicitly asks to inspect one of those files, that counts as confirmation for that file only.

### Startup procedure for new Codex sessions

At the beginning of a new session, before modifying code, Codex must:

1. Read this project instruction file.
2. Read `AGENT_BRIEF.md`.
3. Read `AGENT_HANDOFF.md`.
4. Read `AGENT_TODO.md`.
5. Check `git status`.
6. Check the current diff.
7. Choose and read the matching `AGENT_OP_*.md` file(s).
8. Decide whether any deeper state file is needed; if yes, ask the user before reading it.
9. Summarize:
   - confirmed project state
   - current phase
   - pending work
   - known risks
   - safe next step

Codex must not modify code until this recovery step is complete.

### If context is compacted or uncertain

If Codex suspects that the conversation was compacted, summarized, truncated, or that earlier instructions may have been lost, Codex must immediately stop making new code changes and recover state by rereading:

- this project instruction file
- `AGENT_BRIEF.md`
- `AGENT_HANDOFF.md`
- `AGENT_TODO.md`
- `git status`
- `git diff`

If the recovered brief/handoff/todo state is insufficient, Codex must then read the smallest deeper file that resolves the uncertainty:

- `AGENT_CONTEXT.md` for project rules and architecture.
- `AGENT_CHANGELOG.md` for recent change history.
- `AGENT_CHANGELOG_ARCHIVE.md` for old detailed history.

The deeper file still requires user confirmation before reading unless the user explicitly requested that file.

After recovery, Codex must clearly distinguish:

- confirmed facts
- uncertain facts
- assumptions
- risks
- next safe action

Codex must not treat a compacted conversation summary as fully reliable.

### Project-level safety requirements

Codex must not:

- modify unrelated files
- expand the task scope without explicit user approval
- introduce new dependencies without recording the reason
- delete or rewrite large sections without recording risk and rollback
- continue adding changes on top of unexplained test failures
- claim verification unless the relevant command was actually run or the relevant output was inspected
- start a new phase before the handoff and context files are current
- read `AGENT_CONTEXT.md`, `AGENT_CHANGELOG.md`, or `AGENT_CHANGELOG_ARCHIVE.md` without user confirmation

### Project-level verification preference

For this project, skip visual verification by default. Do not open browser visual checks unless the user explicitly asks for them later or a higher-priority instruction makes them mandatory.

When visual verification is skipped, Codex must:

- say that visual verification was skipped by project preference
- rely on file-level checks, reference searches, syntax checks when available, and static reasoning
- never claim that layout or screenshots were visually verified
- record any remaining visual risk when the change affects the frontend

If a future instruction conflicts with this preference, Codex must mention the conflict clearly instead of silently ignoring either instruction.

### Project-level command verification policy

For this project, keep attempting Git and JavaScript syntax checks when relevant:

- Keep `git status --short`, `git diff --stat`, and `git diff -- .` as project recovery/diff checks.
- Keep `node --check assets/site.js`, `node --check assets/content.js`, and `node --check assets/gripes.js` as JavaScript syntax checks when those files are relevant.
- If `git` or `node` is unavailable, record the exact limitation and continue with file-level checks.
- Do not use Node REPL as a routine fallback for blocked `node --check` or browser verification. Use Node REPL only if the user explicitly requests deeper runtime debugging or a higher-priority instruction requires it.

### Completion requirement

Before reporting a task as complete, Codex must ensure that any relevant project state has been reflected in the durable state files and must report:

- what project instruction file was used
- what state files were read or updated
- what changed
- how it was verified
- what risks remain
- how to roll back the instruction-file change if needed
