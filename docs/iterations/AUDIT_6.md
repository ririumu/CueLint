# AUDIT 6: v0.1.1 Scope Regrounding Release

## Log

- 2026-05-24T16:03:43+09:00: Started iteration 6 from a clean `main` branch aligned with `origin2/main`.
- 2026-05-24T16:03:43+09:00: Reviewed README, prior iteration plan/audit, requirements, user stories, and design artifacts to re-ground v0.1.1 in the existing AI-DLC scope.
- 2026-05-24T16:03:43+09:00: Created `PLAN_6.md` and `AUDIT_6.md`.
- 2026-05-24T16:04:00+09:00: Created branch `codex/v011-scope-language`.
- 2026-05-24T16:05:00+09:00: Updated README wording from response failure framing to surface discourse cue evidence framing.
- 2026-05-24T16:05:00+09:00: Added an Interpretation Contract section clarifying that CueLint does not infer quality, over-refusal, safety correctness, factual correctness, semantic adequacy, or user intent.
- 2026-05-24T16:06:00+09:00: Ran Python syntax compilation for package modules successfully.
- 2026-05-24T16:07:00+09:00: Committed README scope-language changes as `54b8611`.
- 2026-05-24T16:07:00+09:00: Self-merged `codex/v011-scope-language` into `main`.
- 2026-05-24T16:07:00+09:00: Cleared the scope-language checklist item.
- 2026-05-24T16:08:00+09:00: Created branch `codex/v011-output-contract`.
- 2026-05-24T16:09:00+09:00: Added non-breaking JSON metadata fields for `analysis_scope`, `interpretation_contract`, and `not_evaluated`.
- 2026-05-24T16:09:00+09:00: Updated README output metadata documentation and formatter tests for the interpretation contract.
- 2026-05-24T16:10:00+09:00: Initial focused unittest command without `PYTHONPATH=src` failed with import errors; reran with repository test environment.
- 2026-05-24T16:10:00+09:00: Ran focused formatter and CLI tests with `PYTHONPATH=src`: 10 tests passed.
- 2026-05-24T16:10:00+09:00: Ran sample JSON audit and confirmed interpretation-contract metadata is emitted while version remains `0.1.0` until the release-evidence branch.

## Findings

### Review Targets

1. README opening language still says "failure patterns," which can be read as stronger than surface cue evidence.
2. README product thesis still centers disliked behaviors rather than observable cue patterns.
3. JSON metadata does not yet expose the interpretation contract that output is evidence, not a quality label.
4. Package/runtime version still reports `0.1.0`.
5. Release evidence needs a v0.1.1 record that documents scope correction without adding benchmark or dataset features.
