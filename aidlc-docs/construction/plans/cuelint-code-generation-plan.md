# CueLint Code Generation Plan

## Status

Code Generation is complete. Application code has been generated, tested, and documented for CueLint v1.

## Unit Context

- **Unit name**: `cuelint`
- **Project type**: Greenfield single-unit Python CLI
- **Workspace root**: `<workspace-root>`
- **Application code location**: Workspace root only, never under `aidlc-docs/`
- **Documentation location**: `aidlc-docs/construction/cuelint/code/`
- **Primary persona**: Researcher using AI
- **Primary workflow**: Lint-style local inspection through stdin, file input, and `make lint`

## Source Artifacts Read

- [x] `aidlc-docs/aidlc-state.md`
- [x] `aidlc-docs/construction-readiness.md`
- [x] `aidlc-docs/inception/requirements/requirements.md`
- [x] `aidlc-docs/inception/requirements/requirement-verification-questions.md`
- [x] `aidlc-docs/inception/user-stories/stories.md`
- [x] `aidlc-docs/inception/user-stories/personas.md`
- [x] `aidlc-docs/inception/application-design/application-design.md`
- [x] `aidlc-docs/inception/application-design/components.md`
- [x] `aidlc-docs/inception/application-design/component-methods.md`
- [x] `aidlc-docs/inception/application-design/services.md`
- [x] `aidlc-docs/inception/application-design/component-dependency.md`

## Stories Implemented by This Unit

| Story | Coverage in this plan |
|---|---|
| US1: Audit text from stdin | CLI input handling and tests |
| US2: Audit text from a file | CLI file input handling and tests |
| US3: Detect deterministic cue families | Pattern catalog, normalizer, detector, fixture tests |
| US4: Emit structured JSON evidence | Result models, JSON formatter, output tests |
| US5: Show summary metrics and deterministic flags | Metrics calculator, threshold evaluator, tests |
| US6: Run a local lint workflow | `Makefile`, sample fixture, lint target |
| US7: Preserve scope boundaries | README/docs, no network/model/service work |
| US8: Optionally emit Markdown table output | Markdown formatter and tests if scope remains small |

## Dependencies and Interfaces

- No external service dependencies.
- No database or persistence layer.
- No LLM-as-judge or trained model dependency.
- Prefer Python standard library for the first version.
- If a project tool is needed, use lightweight local tooling selected during implementation, documented in `pyproject.toml`.

## Quality-Sensitive Decisions Required in Generation

### Offset Preservation

- Matching may use normalized lowercase text, but evidence spans must point back to original input character offsets.
- The implementation must either preserve a normalized-to-original offset map or restrict normalization so match positions remain compatible with the original string.
- Tests must include contractions, mixed case, and multi-paragraph input to verify original span text and offsets.

### Duplicate Match Policy

- Evidence rows must be stable and deterministic.
- Exact duplicate rows with the same start, end, family, and pattern identifier should be suppressed.
- Overlapping matches from different families may be kept when they explain different cue interpretations.
- Output ordering must be by start offset, end offset, cue family, and pattern identifier.
- Tests must include overlapping and repeated cue examples.

### Sentence Segmentation Limitations

- Use a deterministic first-version sentence splitter.
- Document known limitations such as abbreviations, decimals, initials, and unusual punctuation.
- Sentence and paragraph indexes are evidence metadata, not semantic claims.
- Tests must cover simple punctuation, no punctuation, and paragraph boundaries.

## Planned Application Structure

```text
<workspace-root>/
/pyproject.toml
/Makefile
/README.md
/samples/assistant-response.txt
/src/cuelint/__init__.py
/src/cuelint/__main__.py
/src/cuelint/cli.py
/src/cuelint/errors.py
/src/cuelint/models.py
/src/cuelint/normalizer.py
/src/cuelint/patterns.py
/src/cuelint/detector.py
/src/cuelint/metrics.py
/src/cuelint/flags.py
/src/cuelint/formatter.py
/src/cuelint/service.py
/tests/test_cli.py
/tests/test_detector.py
/tests/test_formatter.py
/tests/test_metrics_flags.py
/tests/test_normalizer.py
```

## Generation Steps

### Step 1: Project Structure Setup

- [x] Create `src/cuelint/` package structure.
- [x] Create `tests/` structure.
- [x] Create `samples/assistant-response.txt`.
- [x] Create or update `pyproject.toml` with package metadata and test configuration.
- [x] Create or update `Makefile` with `lint` and test-oriented targets.

### Step 2: Shared Models and Errors

- [x] Create `src/cuelint/models.py` with data structures for normalized documents, cue patterns, evidence rows, summary metrics, flags, audit result, thresholds, and CLI options.
- [x] Create `src/cuelint/errors.py` for expected application errors.
- [x] Ensure models support JSON serialization without heavyweight dependencies.

### Step 3: Text Normalization and Segmentation

- [x] Create `src/cuelint/normalizer.py`.
- [x] Implement paragraph segmentation with original offsets.
- [x] Implement deterministic sentence segmentation with documented limitations.
- [x] Implement token counting.
- [x] Implement matching normalization with offset preservation strategy.
- [x] Add unit tests for offset preservation, contractions, paragraph indexes, sentence indexes, and empty input boundaries.

### Step 4: Cue Pattern Catalog

- [x] Create `src/cuelint/patterns.py`.
- [x] Define first-version English cue families and pattern identifiers.
- [x] Include raw negation, contrastive reframing, refusal, disclaimer, and meta-negation patterns.
- [x] Keep pattern definitions inspectable in code.
- [x] Add tests that verify required families and pattern identifiers are present.

### Step 5: Cue Detection

- [x] Create `src/cuelint/detector.py`.
- [x] Apply cue patterns against the normalized document.
- [x] Emit original span text, family, start/end offsets, sentence index, paragraph index, and pattern identifier.
- [x] Implement duplicate match policy.
- [x] Implement deterministic evidence ordering.
- [x] Add tests for basic matches, non-matches, overlapping matches, repeated cues, and original offsets.

### Step 6: Metrics and Flags

- [x] Create `src/cuelint/metrics.py`.
- [x] Compute cue counts by family, response length, paragraph count, sentence count, token count, cue density, and first-paragraph cue count.
- [x] Create `src/cuelint/flags.py`.
- [x] Implement high cue-density and first-paragraph concentration threshold flags.
- [x] Add tests for zero-cue input, zero-token defensive behavior, threshold boundaries, and traceability metadata.

### Step 7: Audit Service

- [x] Create `src/cuelint/service.py`.
- [x] Implement `audit_text(text, config=None)` as the orchestration entry point.
- [x] Ensure service code has no process exits and no CLI-specific side effects.
- [x] Add integration-style unit tests for complete audit results.

### Step 8: Output Formatting

- [x] Create `src/cuelint/formatter.py`.
- [x] Implement JSON output as the default format.
- [x] Implement optional Markdown output if it remains small and does not delay the core JSON path.
- [x] Add tests for valid JSON, empty evidence output, stable ordering, and Markdown table headers if Markdown is included.

### Step 9: CLI Adapter

- [x] Create `src/cuelint/cli.py`.
- [x] Create `src/cuelint/__main__.py`.
- [x] Support stdin input.
- [x] Support file input.
- [x] Support output format selection.
- [x] Return clear non-zero errors for empty input, missing files, unreadable files, and unsupported formats.
- [x] Add CLI tests for stdin, file input, JSON default, Markdown option if included, and error paths.

### Step 10: Lint Workflow

- [x] Create or update `Makefile` so `make lint` runs CueLint against `samples/assistant-response.txt`.
- [x] Ensure `make lint` requires no network access and no LLM judge.
- [x] Add a documented test command or make target for local verification.

### Step 11: Documentation Updates

- [x] Update `README.md` with installation or local execution instructions once exact commands exist.
- [x] Document first-version limitations, especially sentence segmentation and audit-not-judge scope.
- [x] Document JSON output shape with a compact example.
- [x] Create `aidlc-docs/construction/cuelint/code/code-generation-summary.md` summarizing generated files and story coverage.

### Step 12: Verification Before Completion

- [x] Run the selected test command.
- [x] Run `make lint`.
- [x] Verify generated code is outside `aidlc-docs/`.
- [x] Verify construction documentation remains under `aidlc-docs/construction/cuelint/code/`.
- [x] Verify all implemented stories are covered by code or tests.
- [x] Mark completed plan steps with `[x]` in this file as generation proceeds.

## Out of Scope for Code Generation

- API service.
- Web dashboard.
- SDK packaging.
- ML training or calibration.
- LLM-as-judge evaluation.
- Hallucination, factuality, legal, medical, or safety correctness detection.
- Multi-file project scans.
- Conversation-history parsing.
- Prompt-response pairing.
- CSV or JSONL output.
- Infrastructure or deployment artifacts beyond local project files.

## Approval Gate

Code Generation proceeded under the approved four-block iteration plan and is now complete for CueLint v1.
