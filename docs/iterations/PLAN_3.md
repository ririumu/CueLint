# PLAN 3: Release Readiness and Repository Hygiene

## Context

CueLint v1 implementation and four-block construction verification are complete. This block prepares the repository for publication without expanding the product scope.

## Checklist

- [x] cut branch `codex/block-5-release-readiness`
- [x] clean generated local caches and ignored build artifacts
- [x] add release-facing license and package metadata
- [x] update README status, install notes, and release checklist
- [x] verify CLI stdin, file input, Markdown output, tests, lint workflow, and packaging
- [x] record release-readiness audit evidence
- [x] commit release readiness changes
- [x] self-merge to `main`
- [x] clear it `[x]`

## Completion Criteria

- [x] Working tree is clean after completion.
- [x] `make test` passes.
- [x] `make lint` passes.
- [x] stdin, file, and Markdown CLI paths work.
- [x] local wheel build succeeds.
- [x] README and AI-DLC docs describe the current implemented state.
