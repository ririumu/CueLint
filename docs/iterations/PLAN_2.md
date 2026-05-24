# PLAN 2: CueLint v1 Four-Block Completion

## Context

The previous `PLAN_1` / `AUDIT_1` iteration artifacts were discarded at user request.

Goal: complete CueLint v1 in four block iterations, following the repository iteration pattern.

## Block Checklist

- [x] Block 1: cut branch -> implement project core -> commit -> self-merge -> clear it [x]
- [x] Block 2: cut branch -> implement metrics, flags, service, formatters -> commit -> self-merge -> clear it [x]
- [x] Block 3: cut branch -> implement CLI, Makefile, sample, README updates -> commit -> self-merge -> clear it [x]
- [ ] Block 4: cut branch -> verification, construction summary, final plan updates -> commit -> self-merge -> clear it [x]

## Completion Criteria

- [ ] CueLint accepts stdin and file input.
- [ ] CueLint emits JSON evidence by default.
- [ ] CueLint detects the required first-version cue families.
- [ ] CueLint computes summary metrics and deterministic flags.
- [ ] `make lint` runs locally without network or LLM judge.
- [ ] Tests pass.
- [ ] AI-DLC construction summary is created.
