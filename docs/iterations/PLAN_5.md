# PLAN 5: Public Portfolio Hardening

## Context

CueLint is now public as `ririumu/cuelint`. This iteration responds to external critique by removing weak pre-publication language, strengthening the cue catalog, correcting nested-cue density behavior, and leaving release-ready evidence that matches the repository's public portfolio status.

## Checklist

- [x] cut branch `codex/portfolio-positioning`
- [x] replace weak pre-publication README and package classifier language with confident v0.1 public positioning
- [x] commit portfolio positioning changes
- [x] self-merge `codex/portfolio-positioning` to `main`
- [x] clear it `[x]`
- [x] cut branch `codex/cue-catalog-hardening`
- [x] broaden the deterministic cue catalog for refusal, disclaimers, meta-negation, contrastive reframing, and hedging
- [x] add tests for the broadened catalog and overlapping evidence preservation
- [ ] commit cue catalog hardening
- [ ] self-merge `codex/cue-catalog-hardening` to `main`
- [ ] clear it `[x]`
- [ ] cut branch `codex/density-calibration`
- [ ] make cue density resilient to nested overlapping evidence rows
- [ ] expose the density basis in summary and metadata
- [ ] update threshold descriptions and tests
- [ ] commit density calibration changes
- [ ] self-merge `codex/density-calibration` to `main`
- [ ] clear it `[x]`
- [ ] cut branch `codex/release-evidence`
- [ ] record public release readiness evidence and final verification
- [ ] run the full local verification suite
- [ ] commit release evidence
- [ ] self-merge `codex/release-evidence` to `main`
- [ ] clear it `[x]`

## Completion Criteria

- [ ] README no longer frames the repository as pre-publication, alpha-only, or unfinished.
- [ ] The cue catalog is meaningfully broader while remaining deterministic and inspectable.
- [ ] Nested evidence rows remain visible, but density no longer overcounts the same local cue cluster.
- [ ] Tests and `make lint` pass.
- [ ] Iteration audit records each branch, commit, merge, and verification step.
