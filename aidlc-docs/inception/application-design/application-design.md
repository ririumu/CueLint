# Application Design

## Overview

CueLint is designed as a small modular Python CLI for deterministic, local, English-only audit of LLM assistant responses. The application accepts one response per invocation, normalizes text, detects cue families, computes transparent metrics, evaluates deterministic flags, and emits JSON by default.

## Design Goals

- Keep the audit kernel deterministic and testable.
- Separate CLI concerns from analysis logic.
- Preserve evidence traceability for every cue and flag.
- Keep cue patterns inspectable and easy to modify.
- Avoid infrastructure, model training, LLM judging, and dashboard concerns in the first version.

## Primary Components

- **CLI Adapter**: Parses arguments, reads input, calls services, writes output.
- **Input Reader**: Reads one response from stdin or file.
- **Text Normalizer**: Performs deterministic normalization, segmentation, and token counting.
- **Cue Pattern Catalog**: Defines cue families and pattern identifiers.
- **Cue Detector**: Emits evidence rows with spans, offsets, family, sentence index, paragraph index, and pattern identifier.
- **Metrics Calculator**: Computes counts, density, lengths, and first-paragraph cue count.
- **Flag Evaluator**: Emits deterministic high-density and first-paragraph concentration flags.
- **Report Formatter**: Emits JSON by default and optional Markdown.

## Service Design

The central internal service is `audit_text(text, config) -> AuditResult`. It coordinates the pipeline and returns structured data without handling CLI exits or formatting. A separate formatting path renders the result for stdout.

## Output Contract

The first-version audit result should contain these top-level concepts:

- `evidence`: list of cue evidence rows.
- `summary`: transparent metrics.
- `flags`: deterministic threshold flags.
- `metadata`: version, language scope, and format-relevant metadata if needed.

Each evidence row should include:

- `span_text`
- `cue_family`
- `start`
- `end`
- `sentence_index`
- `paragraph_index`
- `pattern_id`

## Dependency Design

The application follows a one-directional pipeline:

```text
CLI -> Input -> Audit Service -> Normalize -> Detect -> Metrics -> Flags -> Format -> stdout
```

There are no network, database, service deployment, or model dependencies.

## Design Constraints

- English-only cue families for the first version.
- One assistant response per invocation.
- JSON default output.
- Optional Markdown output only.
- Deterministic cue extraction and thresholding only.
- No hallucination, factuality, legal, medical, or safety correctness detection.
- No CSV, JSONL, multi-file scans, prompt-response pairing, or conversation parsing in this iteration.

## References

- Components: `aidlc-docs/inception/application-design/components.md`
- Methods: `aidlc-docs/inception/application-design/component-methods.md`
- Services: `aidlc-docs/inception/application-design/services.md`
- Dependencies: `aidlc-docs/inception/application-design/component-dependency.md`

