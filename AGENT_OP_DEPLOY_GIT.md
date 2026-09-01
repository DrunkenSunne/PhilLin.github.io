# AGENT_OP_DEPLOY_GIT

Use this operation file for Git, GitHub Pages, and deployment work.

## Covers

- Git status, diff, staging, commits, pushes.
- GitHub Pages deployment checks.
- GitHub Actions workflow issues.
- `.github/workflows/pages.yml`.
- `.nojekyll`.
- Online site not reflecting local files.

## Local-only Default

- Ordinary website changes stop after local file edits and local verification.
- “发布”, “部署”, and similar wording authorize local-file updates only; they do not authorize staging, committing, pushing, authentication, CI checks, or GitHub Pages checks.
- Perform a Git commit, push, or other remote operation only when the user explicitly requests that exact operation in the current request.
- Do not troubleshoot credentials or try alternate remote methods unless the user explicitly asks for remote publication or Git authentication help.

## Default Read Set

Read only:

- `AGENT_BRIEF.md`
- this file
- Git status and diff output
- deployment files directly involved in the task

Read `AGENT_HANDOFF.md` for unfinished deployment continuation and `AGENT_TODO.md` only for deployment planning.

Do not default-read `AGENT_CONTEXT.md`, `AGENT_CHANGELOG.md`, or `AGENT_CHANGELOG_ARCHIVE.md`.

## Deep Read Gate

Before reading any deeper state file, ask the user for confirmation and name the exact file plus reason.

Allowed only when:

- A previous deployment incident must be compared.
- The user asks why the workflow exists.
- A rollback of deployment files is requested.
- Current deployment state conflicts with brief/handoff/todo.

`AGENT_CHANGELOG_ARCHIVE.md` is only allowed for user-confirmed old deployment incident research.

## Common Target Files

- `.github/workflows/pages.yml`
- `.nojekyll`
- root static site files when deployment freshness depends on asset query strings

## Verification

- Use `git status --short`, `git diff --stat`, and `git diff --check`.
- Inspect targeted semantic diffs. If a diff exceeds 400 changed lines, use deterministic allowlist/count audits for mechanical edits and print only unexpected lines or failing hunks.
- Inspect workflow YAML when changed.
- When a remote operation was explicitly requested, do not claim remote deployment success unless the relevant remote check was actually inspected.
- Skip visual browser verification unless the user asks.

## State Logging

At the end of the whole operation, write one concise entry to `AGENT_CHANGELOG.md` for workflow, commit, push, or deployment changes.
Update `AGENT_HANDOFF.md` when a deployment follow-up remains.
