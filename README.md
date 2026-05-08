# CueLint

A planned CLI linter for researchers who use AI and want inspectable evidence of recurring LLM response failure patterns.

CueLint will audit saved or piped assistant responses with deterministic cue detection. The first version is intentionally small: English-only, local-first, Python-based, JSON-first, and designed to fit workflows like `make lint`.

> Current status: AI-DLC Inception is complete. Application code has not been generated yet.

## Purpose

CueLint is intended to become a lightweight Python command-line tool for post-hoc auditing of English assistant responses. It focuses on stable textual operators that often appear in disliked LLM behaviors, such as negation, refusal, disclaimers, meta-negation, and contrastive reframing.

CueLint is not intended to be a semantic judge. It will not decide whether an answer is factually correct, legally safe, medically sound, or globally "bad." Instead, it should expose inspectable evidence: matched cue spans, cue families, positions, counts, densities, and simple threshold-derived signals.

## Target User

The primary persona is a researcher using AI: someone who relies on LLMs during research, writing, analysis, or synthesis and wants a lightweight way to inspect whether an assistant response contains recurring discourse patterns that may indicate unwanted refusal, reframing, disclaiming, or over-qualification.

This user needs a tool that can run locally, explain its findings, and fit into ordinary research workflows without requiring an LLM judge or heavyweight evaluation stack.

## Product Thesis

Many disliked assistant behaviors are heterogeneous at the user-experience level but share recurring textual operators. A response that over-refuses, reframes the user's intent, over-qualifies an answer, or adds unwanted disclaimers may contain stable cue patterns such as:

- `not ... but`
- `not ... rather`
- `not ... instead`
- `I cannot`
- `I do not have access`
- `does not constitute`
- `cannot guarantee`
- `does not mean`
- `not necessarily`

The first product move is to capture those signals with deterministic text processing and present them as evidence for human review.

## Intended Workflow

CueLint should fit naturally into lint-style workflows. A representative target workflow is:

```sh
make lint
```

In the first version, this means running deterministic checks against one saved or piped assistant response per invocation and returning evidence that a researcher can inspect. Future versions may expose richer project-level linting, but the first version should stay focused on local CLI behavior.

## First Version Scope

The approved first version is intentionally small:

| Area | Decision |
|---|---|
| Interface | Local CLI |
| Primary persona | Researcher using AI |
| Language scope | English only |
| Implementation | Python |
| Evaluation style | Deterministic cue extraction and thresholding |
| Primary output | JSON evidence table plus summary metrics |
| Lint workflow | Required `make lint` target |
| ML dependency | None |
| Deployment | None |

## Core Requirements

The first implementation should:

- Accept one assistant response per invocation from a file or standard input.
- Normalize text deterministically.
- Segment paragraphs and sentences.
- Detect cue families with explicit patterns.
- Emit evidence rows with matched span, cue family, position, sentence index, paragraph index, and pattern identifier.
- Emit summary metrics such as counts by family, response length, paragraph count, sentence count, cue density, and first-paragraph cue count.
- Emit JSON by default.
- Include deterministic threshold flags for high cue density and first-paragraph cue concentration.
- Include a `Makefile` with a `lint` target.
- Include focused tests for cue detection and output behavior.

## Out of Scope for the First Version

- SDK packaging.
- API service.
- Web dashboard.
- Japanese or multilingual cue families.
- Classical ML training or calibration.
- LLM-as-judge evaluation.
- Hallucination or factuality detection.
- Legal, medical, or safety correctness verification.
- Deployment or infrastructure work.
- Multi-file project scans.
- Prompt-response pairing or conversation-history parsing.
- CSV or JSONL output.

## Current Status

The repository is currently at the end of AI-DLC Inception. Requirements and workflow planning are complete, and the next stage is Construction: Code Generation planning.

No application code has been generated yet.

## AI-DLC Artifacts

The planning artifacts live under `aidlc-docs/`:

- `aidlc-docs/inception/inception-summary.md`
- `aidlc-docs/inception/requirements/requirements.md`
- `aidlc-docs/inception/requirements/requirement-verification-questions.md`
- `aidlc-docs/inception/plans/execution-plan.md`
- `aidlc-docs/aidlc-state.md`
- `aidlc-docs/audit.md`

## Next Step

Start AI-DLC Code Generation planning. The implementation plan must be reviewed and explicitly approved before application code is generated.
