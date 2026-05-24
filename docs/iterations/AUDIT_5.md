# AUDIT 5: Public Portfolio Hardening

## Log

- 2026-05-24T15:40:30+09:00: Started iteration 5 after review of public critique and local repository state.
- 2026-05-24T15:40:30+09:00: Confirmed current branch `main` is aligned with `origin2/main` and the working tree is clean.
- 2026-05-24T15:40:30+09:00: Reviewed README, pattern catalog, detector, metrics, flags, formatter, tests, pyproject metadata, and prior iteration notes.
- 2026-05-24T15:40:30+09:00: Created `PLAN_5.md` and `AUDIT_5.md`.
- 2026-05-24T15:41:00+09:00: Created branch `codex/portfolio-positioning`.
- 2026-05-24T15:42:00+09:00: Rewrote README language from pre-publication/prototype framing to public v0.1 portfolio positioning.
- 2026-05-24T15:42:00+09:00: Changed package development classifier from Alpha to Beta to match a verified public v0.1 CLI.
- 2026-05-24T15:43:00+09:00: Ran focused formatter and CLI tests: 10 tests passed.
- 2026-05-24T15:43:00+09:00: Committed portfolio positioning changes as `cf1a56c`.
- 2026-05-24T15:44:00+09:00: Self-merged `codex/portfolio-positioning` into `main`.
- 2026-05-24T15:44:00+09:00: Cleared the portfolio positioning checklist item.
- 2026-05-24T15:45:00+09:00: Created branch `codex/cue-catalog-hardening`.
- 2026-05-24T15:47:00+09:00: Added `hedging` as a cue family and broadened deterministic patterns from 21 to 52 entries.
- 2026-05-24T15:48:00+09:00: Added detector tests for expanded refusal/reframing, safety-script disclaimer, and hedging cues.
- 2026-05-24T15:48:00+09:00: Ran detector, formatter, and metrics/flags tests: 13 tests passed.
- 2026-05-24T15:48:00+09:00: Ran sample CLI audit to inspect expanded evidence output.
- 2026-05-24T15:49:00+09:00: Committed cue catalog hardening as `f0cb7ed`.
- 2026-05-24T15:49:00+09:00: Self-merged `codex/cue-catalog-hardening` into `main`.
- 2026-05-24T15:49:00+09:00: Cleared the cue catalog hardening checklist item.
- 2026-05-24T15:50:00+09:00: Created branch `codex/density-calibration`.
- 2026-05-24T15:53:00+09:00: Added cue cluster metrics so overlapping evidence rows remain visible while density counts each local cluster once.
- 2026-05-24T15:53:00+09:00: Switched high-density and first-paragraph concentration flags to cue-cluster metrics.
- 2026-05-24T15:54:00+09:00: Exposed `density_basis` metadata and updated Markdown/JSON summary expectations.
- 2026-05-24T15:54:00+09:00: Added tests proving `does not mean` emits three evidence rows but one density cluster.
- 2026-05-24T15:54:00+09:00: Ran the full unittest suite: 25 tests passed.
- 2026-05-24T15:54:00+09:00: Ran sample CLI audit; density dropped from raw evidence overcounting to 2 clusters / 29 tokens.
- 2026-05-24T15:55:00+09:00: Committed density calibration changes as `232ae58`.
- 2026-05-24T15:55:00+09:00: Self-merged `codex/density-calibration` into `main`.
- 2026-05-24T15:55:00+09:00: Cleared the density calibration checklist item.
- 2026-05-24T15:56:00+09:00: Confirmed `gh` is installed and no remote tags currently exist on `origin2`.
- 2026-05-24T15:56:00+09:00: Created branch `codex/release-evidence`.
- 2026-05-24T15:57:00+09:00: Ran `make test`: 25 tests passed.
- 2026-05-24T15:57:00+09:00: Ran `make lint`: JSON evidence emitted successfully.
- 2026-05-24T15:57:00+09:00: Ran Markdown output smoke test successfully.
- 2026-05-24T15:58:00+09:00: Counted cue patterns by family: 52 total patterns across 6 cue families.
- 2026-05-24T15:58:00+09:00: Created `docs/release-readiness-v0.1.0.md` with critique response, pattern inventory, verification commands, and release judgment.
- 2026-05-24T15:59:00+09:00: Committed release evidence as `03701b4`.
- 2026-05-24T15:59:00+09:00: Self-merged `codex/release-evidence` into `main`.
- 2026-05-24T15:59:00+09:00: Cleared the release evidence checklist item and completion criteria.
- 2026-05-24T16:00:00+09:00: Ran final `make test` on `main`: 25 tests passed.
- 2026-05-24T16:00:00+09:00: Ran final `make lint` on `main`: JSON evidence emitted successfully with cue-cluster density metadata.

## Findings

### Review Targets

1. Public-positioning language still includes pre-publication wording.
2. Package metadata still uses an Alpha classifier.
3. Cue catalog is intentionally small and can be broadened without adding ML or semantic judgment.
4. Evidence output preserves overlapping rows, but current density uses raw evidence count and therefore overcounts nested cues.
5. Threshold flags need clearer wording that describes deterministic trigger mechanics rather than calibrated risk.
