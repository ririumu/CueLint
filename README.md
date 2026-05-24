# CueLint

A deterministic CLI linter for researchers who use AI and want inspectable evidence of recurring surface discourse cue patterns.

CueLint audits saved or piped assistant responses with deterministic cue detection. Version 0.1.x is English-only, local-first, Python-based, JSON-first, and designed to fit workflows like `make lint`.

> Current status: CueLint v0.1.1 is a public, verified local Python CLI and portfolio release.

## Purpose

CueLint is a lightweight Python command-line tool for post-hoc auditing of English assistant responses. It focuses on stable textual operators that may be useful review cues, such as negation, refusal, disclaimers, meta-negation, contrastive reframing, and hedging.

CueLint is deliberately non-semantic: it does not decide whether an answer is factually correct, legally safe, medically sound, or globally "bad." Its job is evidence extraction: matched cue spans, cue families, positions, counts, density signals, and deterministic threshold flags that a human can inspect.

## Target User

The primary persona is a researcher using AI: someone who relies on LLMs during research, writing, analysis, or synthesis and wants a lightweight way to inspect whether an assistant response contains recurring discourse cue patterns such as refusal-like, disclaimer-like, reframing-like, or over-qualification-like wording.

This user needs a tool that can run locally, explain its findings, and fit into ordinary research workflows without requiring an LLM judge or heavyweight evaluation stack.

## Product Thesis

Assistant responses can contain recurring surface cue patterns that are worth reviewing without asking a model to judge them. A response may include refusal-like, reframing-like, over-qualification-like, or disclaimer-like wording through stable cue patterns such as:

- `not ... but`
- `not ... rather`
- `not ... instead`
- `I cannot`
- `I do not have access`
- `does not constitute`
- `cannot guarantee`
- `does not mean`
- `not necessarily`
- `in general`
- `it depends`
- `may vary`

CueLint captures those signals with deterministic text processing and presents them as evidence for human review.

## Interpretation Contract

CueLint detects surface cue evidence. It does not infer response quality, over-refusal, safety correctness, factual correctness, semantic adequacy, or user intent.

Threshold flags are deterministic review tripwires over transparent counts and densities. They are not calibrated labels, risk scores, benchmark results, or judgments that an answer is bad.

Prompt-response pairing, dataset evaluation, ML calibration, multilingual cue families, and LLM-as-judge evaluation remain out of scope for version 0.1.x.

## Intended Workflow

CueLint fits naturally into lint-style workflows. A representative workflow is:

```sh
make lint
```

Version 0.1.x runs deterministic checks against one saved or piped assistant response per invocation and returns evidence that a researcher can inspect. The scope is intentionally tight so the output remains transparent, fast, and reproducible.

## Local Usage

Install locally in editable mode:

```sh
python -m pip install -e .
```

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
- `summary`: counts by family, response length, paragraph count, sentence count, token count, cue count, cue cluster count, cue density, first-paragraph cue count, and first-paragraph cue cluster count.
- `flags`: deterministic threshold flags with metric, value, threshold, and trigger state.
- `metadata`: version, language scope, deterministic marker, analysis scope, interpretation contract, non-evaluated claim list, density basis, and threshold configuration.

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
    "cue_cluster_count": 1,
    "cue_density": 0.25
  },
  "flags": [],
  "metadata": {
    "language_scope": "en",
    "analysis_scope": "surface_cue_evidence",
    "interpretation_contract": "evidence_not_quality_label",
    "not_evaluated": [
      "factual_correctness",
      "safety_correctness",
      "semantic_quality",
      "over_refusal_classification",
      "user_intent"
    ],
    "density_basis": "overlapping cue spans are collapsed into cue clusters",
    "deterministic": true
  }
}
```

## Design Boundaries

CueLint is an audit instrument, not a semantic judge, quality evaluator, over-refusal classifier, or safety evaluator. It does not detect factuality, hallucination, legal correctness, medical safety, user intent, or whether an answer is globally good or bad.

Sentence segmentation is deterministic and intentionally simple. Abbreviations, decimals, initials, and unusual punctuation can produce imperfect sentence indexes; those indexes are evidence metadata, not semantic claims.

Nested cue spans are preserved in evidence. For density, overlapping local cue rows are collapsed into cue clusters so a phrase like `does not mean` remains inspectable without inflating the density metric three times.

Threshold flags are deterministic tripwires over transparent metrics. They are meant to sort evidence for review, not to masquerade as calibrated risk scores.

## Version 0.1.x Scope

Version 0.1.x is deliberately focused:

| Area | Decision |
|---|---|
| Interface | Local CLI |
| Primary persona | Researcher using AI |
| Language scope | English only |
| Implementation | Python |
| Analysis style | Deterministic cue extraction and thresholding |
| Primary output | JSON evidence table plus summary metrics |
| Lint workflow | Required `make lint` target |
| ML dependency | None |
| Deployment | None |

## Implemented Requirements

Version 0.1.x:

- Accepts one assistant response per invocation from a file or standard input.
- Normalizes text deterministically.
- Segments paragraphs and sentences.
- Detects cue families with explicit patterns.
- Emits evidence rows with matched span, cue family, position, sentence index, paragraph index, and pattern identifier.
- Emits summary metrics such as counts by family, response length, paragraph count, sentence count, cue cluster count, cue density, first-paragraph cue count, and first-paragraph cue cluster count.
- Emits JSON by default.
- Includes deterministic threshold flags for high cue density and first-paragraph cue concentration.
- Includes a `Makefile` with a `lint` target.
- Includes focused tests for cue detection, metrics, flags, formatting, normalization, and CLI behavior.

## Out of Scope for Version 0.1.x

- SDK packaging.
- API service.
- Web dashboard.
- Japanese or multilingual cue families.
- Classical ML training or calibration.
- LLM-as-judge evaluation.
- Hallucination or factuality detection.
- Legal, medical, or safety correctness verification.
- Response-quality evaluation.
- Over-refusal classification.
- User-intent inference.
- Deployment or infrastructure work.
- Multi-file project scans.
- Prompt-response pairing or conversation-history parsing.
- CSV or JSONL output.
