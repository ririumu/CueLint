# CueLint

A CLI linter for researchers who use AI and want inspectable evidence of recurring LLM response failure patterns.

CueLint will audit saved or piped assistant responses with deterministic cue detection. The first version is intentionally small: English-only, local-first, Python-based, JSON-first, and designed to fit workflows like `make lint`.

> Current status: CueLint v1 application code has been generated in Construction and is available as a local Python CLI.

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

## Local Usage

Run against the included sample:

```sh
make lint
```

Run tests:

```sh
make test
```

Audit a file:

```sh
PYTHONPATH=src python -m cuelint samples/assistant-response.txt
```

Audit stdin:

```sh
printf 'I cannot guarantee this does not mean failure.' | PYTHONPATH=src python -m cuelint
```

Emit Markdown instead of JSON:

```sh
PYTHONPATH=src python -m cuelint --format markdown samples/assistant-response.txt
```

## Output Shape

JSON is the default output format. The top-level object contains:

- `evidence`: matched cue spans with `span_text`, `cue_family`, `start`, `end`, `sentence_index`, `paragraph_index`, and `pattern_id`.
- `summary`: counts by family, response length, paragraph count, sentence count, token count, cue count, cue density, and first-paragraph cue count.
- `flags`: deterministic threshold flags with metric, value, threshold, and trigger state.
- `metadata`: version, language scope, deterministic marker, and threshold configuration.

Compact example:

```json
{
  "evidence": [
    {
      "span_text": "I cannot",
      "cue_family": "refusal",
      "start": 0,
      "end": 8,
      "sentence_index": 0,
      "paragraph_index": 0,
      "pattern_id": "refusal_i_cannot"
    }
  ],
  "summary": {
    "cue_count": 1,
    "cue_density": 0.25
  },
  "flags": [],
  "metadata": {
    "language_scope": "en",
    "deterministic": true
  }
}
```

## First-Version Limitations

CueLint is an audit instrument, not a semantic judge. It does not detect factuality, hallucination, legal correctness, medical safety, or whether an answer is globally good or bad.

Sentence segmentation is deterministic and intentionally simple. Abbreviations, decimals, initials, and unusual punctuation can produce imperfect sentence indexes; those indexes are evidence metadata, not semantic claims.

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

The repository is currently in AI-DLC Construction after Code Generation. The generated application code lives under `src/cuelint/`, tests live under `tests/`, and local workflow targets are provided by `Makefile`.

## AI-DLC Artifacts

The planning artifacts live under `aidlc-docs/`:

- `aidlc-docs/inception/inception-summary.md`
- `aidlc-docs/inception/requirements/requirements.md`
- `aidlc-docs/inception/requirements/requirement-verification-questions.md`
- `aidlc-docs/inception/user-stories/personas.md`
- `aidlc-docs/inception/user-stories/stories.md`
- `aidlc-docs/inception/application-design/application-design.md`
- `aidlc-docs/inception/application-design/components.md`
- `aidlc-docs/inception/application-design/component-methods.md`
- `aidlc-docs/inception/application-design/services.md`
- `aidlc-docs/inception/application-design/component-dependency.md`
- `aidlc-docs/inception/plans/user-stories-assessment.md`
- `aidlc-docs/inception/plans/story-generation-plan.md`
- `aidlc-docs/inception/plans/application-design-plan.md`
- `aidlc-docs/inception/plans/execution-plan.md`
- `aidlc-docs/construction-readiness.md`
- `aidlc-docs/construction/plans/cuelint-code-generation-plan.md`
- `aidlc-docs/aidlc-state.md`
- `aidlc-docs/audit.md`

## Next Step

Run verification with `make test` and `make lint`, then proceed through the remaining Construction Build and Test closure artifacts.
