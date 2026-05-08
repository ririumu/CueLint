# Services

## Service Overview

CueLint does not need network services or infrastructure services. In this design, "service" means an internal orchestration layer that coordinates the audit pipeline for the CLI and tests.

## Audit Service

### Purpose

The Audit Service is the core application service. It accepts raw assistant response text and returns an `AuditResult` without knowing whether the caller is the CLI, a test, or a future library wrapper.

### Responsibilities

- Build or receive audit configuration.
- Normalize raw text.
- Load deterministic cue patterns.
- Detect cue evidence.
- Calculate summary metrics.
- Evaluate deterministic flags.
- Return a single structured audit result.

### Interactions

1. Receives raw text from CLI Adapter.
2. Calls Text Normalizer.
3. Retrieves patterns from Cue Pattern Catalog.
4. Calls Cue Detector.
5. Calls Metrics Calculator.
6. Calls Flag Evaluator.
7. Returns `AuditResult` to CLI Adapter.

## Formatting Service

### Purpose

The Formatting Service converts the structured `AuditResult` into the user's selected representation.

### Responsibilities

- Keep output rendering separate from analysis.
- Serialize JSON output by default.
- Render optional Markdown output from the same result object.
- Avoid changing cue detection, metrics, or flags based on output format.

### Interactions

1. Receives `AuditResult` from CLI Adapter.
2. Receives output format selection from CLI options.
3. Calls Report Formatter.
4. Returns text for stdout.

## Error Handling Service Boundary

CueLint should use lightweight application errors rather than a large error framework.

### Expected Error Categories

- Empty input.
- Missing or unreadable file.
- Unsupported output format.
- Unexpected internal error.

### Handling Policy

- Expected user errors return clear stderr messages and non-zero exit codes.
- Internal errors should fail visibly and avoid partial or misleading audit output.
- The audit kernel should avoid process exits so it remains testable.

