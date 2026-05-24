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
- [x] commit cue catalog hardening
- [x] self-merge `codex/cue-catalog-hardening` to `main`
- [x] clear it `[x]`
- [x] cut branch `codex/density-calibration`
- [x] make cue density resilient to nested overlapping evidence rows
- [x] expose the density basis in summary and metadata
- [x] update threshold descriptions and tests
- [x] commit density calibration changes
- [x] self-merge `codex/density-calibration` to `main`
- [x] clear it `[x]`
- [x] cut branch `codex/release-evidence`
- [x] record public release readiness evidence and final verification
- [x] run the full local verification suite
- [x] commit release evidence
- [x] self-merge `codex/release-evidence` to `main`
- [x] clear it `[x]`

## Completion Criteria

- [x] README no longer frames the repository as pre-publication, alpha-only, or unfinished.
- [x] The cue catalog is meaningfully broader while remaining deterministic and inspectable.
- [x] Nested evidence rows remain visible, but density no longer overcounts the same local cue cluster.
- [x] Tests and `make lint` pass.
- [x] Iteration audit records each branch, commit, merge, and verification step.
