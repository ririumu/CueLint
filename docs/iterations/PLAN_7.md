# PLAN 7: v0.1.2 README Expectation Cleanup

## Context

CueLint v0.1.2 should reduce README wording that suggests an actively managed product roadmap or ongoing portfolio release. The release keeps the CLI, JSON output contract, cue catalog, thresholds, and v0.1.1 interpretation metadata intact.

## Checklist

- [x] cut branch `codex/readme-expectation-cleanup`
- [x] remove README status and long scope-management sections
- [x] replace versioned scope wording with compact limits
- [x] commit README expectation cleanup
- [ ] self-merge `codex/readme-expectation-cleanup` to `main`
- [ ] clear it `[x]`
- [ ] cut branch `codex/v012-release`
- [ ] bump version to `0.1.2`
- [ ] add v0.1.2 release-readiness documentation
- [ ] run full verification
- [ ] commit v0.1.2 release changes
- [ ] self-merge `codex/v012-release` to `main`
- [ ] clear it `[x]`
- [ ] push `main` to `origin2`
- [ ] create annotated tag `v0.1.2`
- [ ] push tag `v0.1.2` to `origin2`

## Completion Criteria

- [ ] README no longer says `Current status`, `public, verified`, or `portfolio release`.
- [ ] README no longer contains the long `Version 0.1.x Scope`, `Implemented Requirements`, or `Out of Scope for Version` sections.
- [ ] Runtime and package metadata report `0.1.2`.
- [ ] `make test`, `make lint`, and Markdown output smoke test pass.
- [ ] `main` and tag `v0.1.2` are pushed to `origin2`.
