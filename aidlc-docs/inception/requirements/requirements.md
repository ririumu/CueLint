# Requirements: CueLint

## Intent Analysis

- **User request**: Build CueLint, a lightweight, classical, cue-based audit kernel for detecting recurring disliked LLM output behaviors through surface discourse operators.
- **Request type**: New project.
- **Scope estimate**: Single small CLI application with internally reusable parsing/audit modules.
- **Complexity estimate**: Simple initial version, with future expansion paths for SDK packaging, multilingual cues, and classical ML calibration.
- **Requirements depth**: Minimal.
- **Product name**: CueLint.
- **Primary persona**: Researcher using AI.

## Product Summary

The first version will be a local command-line tool that accepts LLM assistant output text and emits an interpretable evidence table. It will focus on English responses and detect deterministic cue families related to negation, refusal, disclaimers, meta-negation, and contrastive reframing. The product is an audit instrument, not a semantic judge.

The primary user is a researcher using AI who wants a lint-style way to inspect saved or piped assistant responses for recurring discourse patterns. The intended workflow should be compatible with command-line habits such as `make lint`.

## Functional Requirements

### FR1: Input Handling

The tool must accept one assistant response per invocation from either a text file or standard input.

For the first version, multi-file project scans, conversation-history parsing, prompt-response pairing, and dataset batch processing are out of scope.

### FR1.1: Lint Workflow Compatibility

The repository must include a `Makefile` with a `lint` target. The `make lint` workflow should run CueLint against a small local sample or documented fixture without requiring network access or an LLM judge.

### FR2: Deterministic Normalization

The tool must normalize input text using deterministic processing, including lowercasing, basic contraction handling, sentence segmentation, paragraph segmentation, and token counting.

### FR3: Cue Family Detection

The tool must detect English cue patterns for at least these families:

- Raw negation cues: `no`, `not`, `never`, `cannot`, `do not`, `does not`, `is not`, `was not`, `has not`, and common contracted forms.
- Contrastive reframing candidates: `not ... but`, `not ... rather`, `not ... instead`.
- Refusal candidates: `I cannot`, `I do not have access`, `I am not able`.
- Disclaimer candidates: `not a doctor`, `does not constitute`, `cannot guarantee`.
- Meta-negation candidates: `not saying`, `does not mean`, `not necessarily`.

### FR4: Evidence Table Output

The tool must emit a structured evidence table containing matched span text, cue family, start/end character offsets, sentence index, paragraph index, and a short pattern identifier.

The default machine-readable output format must be JSON. A human-readable Markdown table may be added as an optional `--format markdown` output, but CSV and JSONL are out of scope for the first version.

### FR5: Summary Metrics

The tool must compute simple summary metrics, including cue counts by family, total response length, paragraph count, sentence count, cue density, and first-paragraph cue count.

### FR6: Deterministic Threshold Flags

The first version must include a small fixed set of deterministic threshold flags derived only from transparent counts or densities. At minimum, include a high cue-density flag and a first-paragraph cue concentration flag. It must not require or include a trained ML classifier.

## Non-Functional Requirements

### NFR1: Interpretability

Every flag or metric must be traceable to explicit matched spans or transparent counts.

### NFR2: Low Latency

The tool should run locally with predictable latency and no neural-model dependency.

### NFR3: Maintainability

Cue patterns should be stored in code structures that are easy to inspect and modify.

### NFR4: Portability

The first implementation should use Python and avoid heavyweight runtime dependencies unless clearly justified.

### NFR5: Scope Control

The first version must remain English-only, CLI-first, and deterministic. API service, web dashboard, Japanese cue families, SDK packaging, training pipelines, and ML calibration are out of scope for this iteration.

## Extension Configuration

| Extension | Enabled | Decided At | Rationale |
|---|---|---|---|
| Security Baseline | No | Requirements Analysis | Disabled to keep the prototype scope minimal. |
| Property-Based Testing | No | Requirements Analysis | Disabled to minimize initial delivery overhead. |

## Out of Scope

- Hallucination or factuality detection.
- Legal, medical, or safety correctness verification.
- LLM-as-judge evaluation.
- Classical ML training pipeline.
- Web dashboard or review workflow.
- Multilingual cue implementation.
- Browser extension or enterprise gateway integration.
- Multi-file project scans.
- Prompt-response pairing or conversation-history parsing.
- CSV or JSONL output.

## Open Assumptions

- The first useful artifact is a local CLI rather than a packaged SDK.
- The input is plain assistant response text, one response per invocation.
- Human reviewers will use evidence output as inspection material, not as a final verdict.
