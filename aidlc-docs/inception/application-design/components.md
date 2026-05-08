# Components

## Component Overview

CueLint is a small local CLI built around a deterministic audit pipeline. The design separates input handling, normalization, cue matching, metrics, flag calculation, and output formatting so each behavior can be tested independently.

## Components

### CLI Adapter

**Purpose**: Parse command-line options, collect input text, invoke the audit service, and write formatted output.

**Responsibilities**

- Accept one assistant response from stdin or a file.
- Select output format, defaulting to JSON.
- Convert operational errors into clear user-facing messages and non-zero exits.
- Keep business logic out of argument parsing.

**Interfaces**

- Input: command-line arguments, stdin, file path.
- Output: stdout for audit output, stderr for errors, process exit code.

### Input Reader

**Purpose**: Resolve the one-response input source and return raw text.

**Responsibilities**

- Read UTF-8 text from a file path.
- Read UTF-8 text from stdin.
- Reject empty input with a clear error.
- Avoid multi-file scans and conversation-history parsing.

**Interfaces**

- Input: optional file path and stdin stream.
- Output: raw response text string.

### Text Normalizer

**Purpose**: Produce deterministic text structures needed by cue matching and metrics.

**Responsibilities**

- Lowercase normalized matching text while preserving original offsets for evidence spans.
- Handle basic contractions used by cue patterns.
- Segment paragraphs.
- Segment sentences.
- Count tokens using a simple deterministic policy.

**Interfaces**

- Input: raw response text.
- Output: normalized document representation containing original text, paragraphs, sentences, token count, and offset metadata.

### Cue Pattern Catalog

**Purpose**: Store inspectable cue patterns and metadata.

**Responsibilities**

- Define cue families and pattern identifiers.
- Keep deterministic English patterns for raw negation, contrastive reframing, refusal, disclaimer, and meta-negation.
- Make patterns easy to review and modify.

**Interfaces**

- Input: none at runtime beyond module import or initialization.
- Output: iterable cue pattern definitions.

### Cue Detector

**Purpose**: Match cue patterns against normalized text and emit evidence rows.

**Responsibilities**

- Apply pattern definitions deterministically.
- Produce matched span text from the original input.
- Attach cue family, pattern identifier, character offsets, sentence index, and paragraph index.
- Preserve stable ordering by span position and pattern order.

**Interfaces**

- Input: normalized document and cue pattern catalog.
- Output: evidence row collection.

### Metrics Calculator

**Purpose**: Compute transparent summary metrics from the normalized document and evidence rows.

**Responsibilities**

- Count cues by family.
- Compute total response length, paragraph count, sentence count, token count, cue density, and first-paragraph cue count.
- Avoid semantic scoring or calibrated model outputs.

**Interfaces**

- Input: normalized document and evidence rows.
- Output: summary metrics structure.

### Flag Evaluator

**Purpose**: Emit deterministic threshold flags from transparent metrics.

**Responsibilities**

- Evaluate high cue-density flag.
- Evaluate first-paragraph cue concentration flag.
- Include threshold values or criteria in flag metadata.
- Ensure every flag is explainable from metrics and evidence.

**Interfaces**

- Input: summary metrics.
- Output: flag collection.

### Report Formatter

**Purpose**: Convert audit results into the selected output format.

**Responsibilities**

- Emit valid JSON by default.
- Optionally emit a Markdown evidence table.
- Preserve the same analysis result across formats.

**Interfaces**

- Input: audit result and selected format.
- Output: string suitable for stdout.

## Out-of-Scope Components

- Web dashboard.
- API server.
- SDK packaging layer.
- Training or calibration pipeline.
- LLM judge integration.
- Database or persistence layer.

