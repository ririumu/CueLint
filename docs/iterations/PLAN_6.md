# PLAN 6: v0.1.1 Scope Regrounding Release

## Context

CueLint v0.1.1 is a scope-correction release. It should align public wording and machine-readable metadata with CueLint's actual contract: deterministic English surface-cue evidence extraction for one assistant response per invocation. It must not expand into benchmark evaluation, over-refusal classification, semantic quality scoring, prompt-response pairing, datasets, calibration, or LLM-as-judge critique work.

## Checklist

- [x] cut branch `codex/v011-scope-language`
- [x] update README scope, purpose, product thesis, and design-boundary language
- [x] commit README scope-language changes
- [x] self-merge `codex/v011-scope-language` to `main`
- [x] clear it `[x]`
- [x] cut branch `codex/v011-output-contract`
- [x] add metadata interpretation-contract fields and tests
- [x] commit output-contract changes
- [ ] self-merge `codex/v011-output-contract` to `main`
- [ ] clear it `[x]`
- [ ] cut branch `codex/v011-release-evidence`
- [ ] bump version to `0.1.1`
- [ ] add release-readiness documentation
- [ ] run full verification
- [ ] commit release evidence
- [ ] self-merge `codex/v011-release-evidence` to `main`
- [ ] clear it `[x]`

## Completion Criteria

- [x] README describes CueLint as a surface cue evidence linter, not a quality evaluator or over-refusal classifier.
- [x] JSON metadata records the interpretation contract without changing the CLI interface.
- [ ] Version metadata reports `0.1.1`.
- [ ] `make test`, `make lint`, and Markdown output smoke test pass.
- [ ] Release evidence documents that v0.1.1 corrects scope framing rather than expanding capability.
