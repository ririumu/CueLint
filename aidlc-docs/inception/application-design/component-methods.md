# Component Methods

## CLI Adapter

### `main(argv: list[str] | None = None) -> int`

Parses arguments, reads input, runs the audit service, writes formatted output, and returns a process exit code.

### `parse_args(argv: list[str] | None) -> CliOptions`

Builds the CLI option structure. Expected options include optional input file path and output format.

## Input Reader

### `read_input(options: CliOptions, stdin: TextIO) -> str`

Returns raw assistant response text from the selected input source.

### `read_file(path: str) -> str`

Reads a UTF-8 text file and returns its contents.

### `validate_non_empty(text: str) -> str`

Rejects empty or whitespace-only input with a clear application error.

## Text Normalizer

### `normalize_document(text: str) -> NormalizedDocument`

Creates the deterministic document representation used by the rest of the pipeline.

### `segment_paragraphs(text: str) -> list[Paragraph]`

Splits text into paragraphs while preserving offsets.

### `segment_sentences(text: str) -> list[Sentence]`

Splits text into sentences using a deterministic first-version policy.

### `count_tokens(text: str) -> int`

Counts tokens with a simple deterministic tokenizer suitable for density calculations.

### `normalize_for_matching(text: str) -> str`

Creates lowercase matching text and handles basic contraction normalization.

## Cue Pattern Catalog

### `load_patterns() -> list[CuePattern]`

Returns the first-version English cue pattern definitions.

### `pattern_families() -> list[str]`

Returns supported cue family names for validation and reporting.

## Cue Detector

### `detect_cues(document: NormalizedDocument, patterns: list[CuePattern]) -> list[EvidenceRow]`

Applies cue patterns to the document and returns evidence rows.

### `locate_sentence(document: NormalizedDocument, start: int) -> int`

Finds the sentence index containing a matched span start offset.

### `locate_paragraph(document: NormalizedDocument, start: int) -> int`

Finds the paragraph index containing a matched span start offset.

### `sort_evidence(rows: list[EvidenceRow]) -> list[EvidenceRow]`

Sorts evidence rows by start offset, end offset, cue family, and pattern identifier for stable output.

## Metrics Calculator

### `calculate_metrics(document: NormalizedDocument, evidence: list[EvidenceRow]) -> SummaryMetrics`

Computes summary metrics from the normalized document and evidence rows.

### `count_by_family(evidence: list[EvidenceRow]) -> dict[str, int]`

Returns cue counts grouped by cue family.

### `calculate_cue_density(evidence_count: int, token_count: int) -> float`

Computes deterministic cue density. The first version should handle zero-token input defensively.

## Flag Evaluator

### `evaluate_flags(metrics: SummaryMetrics, thresholds: ThresholdConfig) -> list[Flag]`

Evaluates deterministic threshold flags.

### `default_thresholds() -> ThresholdConfig`

Returns first-version threshold values for high cue density and first-paragraph cue concentration.

## Report Formatter

### `format_report(result: AuditResult, output_format: str) -> str`

Dispatches to JSON or Markdown formatting.

### `format_json(result: AuditResult) -> str`

Serializes the audit result as valid JSON.

### `format_markdown(result: AuditResult) -> str`

Renders a human-readable Markdown evidence table and summary.

## Audit Service

### `audit_text(text: str, config: AuditConfig | None = None) -> AuditResult`

Coordinates normalization, pattern loading, cue detection, metrics calculation, and flag evaluation.

### `build_default_config() -> AuditConfig`

Creates default runtime configuration for the first version.

