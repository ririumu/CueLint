# User Stories

## Story Map

| Story | Persona | Capability | Priority |
|---|---|---|---|
| US1 | Researcher using AI | Audit text from stdin | Must |
| US2 | Researcher using AI | Audit text from a file | Must |
| US3 | Researcher using AI, Future maintainer | Detect deterministic cue families | Must |
| US4 | Researcher using AI, Future maintainer | Emit structured JSON evidence | Must |
| US5 | Researcher using AI, Future maintainer | Show summary metrics and deterministic flags | Must |
| US6 | Researcher using AI, Future maintainer | Run a local lint workflow | Must |
| US7 | Researcher using AI, Future maintainer | Preserve scope boundaries | Must |
| US8 | Researcher using AI | Optionally emit Markdown table output | Should |

## US1: Audit Text From Stdin

As a researcher using AI, I want to pipe one assistant response into CueLint so that I can inspect saved or generated text without creating an intermediate file.

### Acceptance Criteria

- Given plain text is provided on stdin, when CueLint runs without a file input argument, then it audits exactly that one response.
- Given stdin is empty, when CueLint runs, then it exits with a clear error rather than emitting misleading evidence.
- Given a valid response is provided, when CueLint completes, then output includes evidence, summary metrics, and flags.

### INVEST Check

- **Independent**: Can be implemented without file input.
- **Negotiable**: CLI flag names can be adjusted during implementation planning.
- **Valuable**: Supports shell pipeline workflows.
- **Estimable**: Small CLI behavior.
- **Small**: One input path.
- **Testable**: Can be tested with subprocess or CLI unit tests.

## US2: Audit Text From a File

As a researcher using AI, I want to pass a text file to CueLint so that I can audit saved assistant responses reproducibly.

### Acceptance Criteria

- Given a readable text file path, when CueLint runs with that path, then it audits the file contents as one response.
- Given the file does not exist or is unreadable, when CueLint runs, then it exits with a clear non-zero error.
- Given both file input and stdin are possible, when file input is provided, then the behavior is deterministic and documented by the CLI help or usage text.

### INVEST Check

- **Independent**: Can be implemented separately from stdin.
- **Negotiable**: Exact option shape can be chosen in code generation planning.
- **Valuable**: Supports saved-response review.
- **Estimable**: Small input handling behavior.
- **Small**: One input path.
- **Testable**: Can be tested with temporary files.

## US3: Detect Deterministic Cue Families

As a researcher using AI, I want CueLint to detect explicit English cue families so that I can inspect surface discourse patterns without relying on a semantic judge.

### Acceptance Criteria

- Given text containing raw negation cues, when audited, then matching spans are reported with a raw negation family.
- Given text containing contrastive reframing candidates such as `not ... but`, when audited, then matching spans are reported with a contrastive reframing family.
- Given text containing refusal, disclaimer, or meta-negation candidates, when audited, then matching spans are reported with the appropriate family.
- Given contracted forms, when normalization expands or recognizes them, then cue detection remains deterministic.
- Given non-matching text, when audited, then CueLint does not invent evidence.

### INVEST Check

- **Independent**: Core detector can be built before formatting choices.
- **Negotiable**: Pattern identifiers and exact regex forms can be refined.
- **Valuable**: This is the core product capability.
- **Estimable**: Defined list of cue families.
- **Small**: Deterministic first-version scope.
- **Testable**: Fixture strings can assert exact matches.

## US4: Emit Structured JSON Evidence

As a researcher using AI, I want CueLint to emit JSON evidence so that I can inspect, compare, or process audit output with other tools.

### Acceptance Criteria

- Given matched cues, when JSON output is emitted, then each evidence row includes matched span text, cue family, start offset, end offset, sentence index, paragraph index, and pattern identifier.
- Given no matched cues, when JSON output is emitted, then the evidence list is empty and summary metrics still describe the input.
- Given the same input, when CueLint is run repeatedly, then JSON output is deterministic apart from any explicitly documented ordering guarantee.
- Given the output is parsed by a JSON parser, then it is valid JSON.

### INVEST Check

- **Independent**: Can be tested from detector output.
- **Negotiable**: Top-level field names can be finalized in code generation planning.
- **Valuable**: Enables downstream analysis.
- **Estimable**: Concrete field list exists.
- **Small**: JSON only by default.
- **Testable**: JSON schema-like assertions can be used.

## US5: Show Summary Metrics and Deterministic Flags

As a researcher using AI, I want summary metrics and transparent flags so that I can quickly identify responses with high cue concentration while still seeing the evidence behind each flag.

### Acceptance Criteria

- Given audited text, when output is produced, then summary metrics include cue counts by family, total response length, paragraph count, sentence count, cue density, and first-paragraph cue count.
- Given cue density exceeds a fixed threshold, when output is produced, then a high cue-density flag is emitted.
- Given first-paragraph cue concentration exceeds a fixed threshold, when output is produced, then a first-paragraph concentration flag is emitted.
- Given any flag is emitted, when output is reviewed, then the flag is traceable to transparent counts or densities.

### INVEST Check

- **Independent**: Can be implemented from evidence and normalized text.
- **Negotiable**: Exact thresholds can be chosen during code generation planning.
- **Valuable**: Helps triage audit results.
- **Estimable**: Small deterministic calculations.
- **Small**: Two required flags.
- **Testable**: Threshold fixtures can assert flag presence or absence.

## US6: Run a Local Lint Workflow

As a researcher using AI, I want `make lint` to run CueLint locally so that the repository demonstrates the intended workflow without network access or model dependencies.

### Acceptance Criteria

- Given the repository is checked out locally, when `make lint` is run after setup, then it runs CueLint against a local sample or documented fixture.
- Given the lint target runs, then it does not call an external service or LLM judge.
- Given lint output is produced, then it is compatible with the first-version output contract.

### INVEST Check

- **Independent**: Can be implemented with fixtures and CLI.
- **Negotiable**: Fixture location can be selected during code generation planning.
- **Valuable**: Demonstrates intended usage.
- **Estimable**: Small build workflow.
- **Small**: One Makefile target.
- **Testable**: Can be verified by running `make lint`.

## US7: Preserve Scope Boundaries

As a future maintainer, I want the first version to preserve its deterministic local scope so that CueLint remains small, interpretable, and shippable.

### Acceptance Criteria

- Given first-version implementation work, when scope decisions arise, then SDK packaging, API service, web dashboard, multilingual cue families, ML training, and LLM-as-judge evaluation remain out of scope.
- Given output flags are emitted, when documentation or code names describe them, then they avoid claiming factuality, safety, legal, medical, or hallucination detection.
- Given cue patterns are maintained, when new patterns are added later, then the structure remains inspectable and deterministic.

### INVEST Check

- **Independent**: Guides implementation boundaries across stories.
- **Negotiable**: Future versions can revisit deferred scope.
- **Valuable**: Prevents prototype over-expansion.
- **Estimable**: Scope-control checks are clear.
- **Small**: First-version boundary only.
- **Testable**: Review and tests can enforce absence of out-of-scope features.

## US8: Optionally Emit Markdown Table Output

As a researcher using AI, I want optional Markdown output so that I can quickly read evidence in a terminal, note, or document.

### Acceptance Criteria

- Given `--format markdown` or equivalent is selected, when CueLint produces output, then evidence appears as a readable Markdown table.
- Given Markdown output is emitted, then it includes the core evidence fields needed for review.
- Given default behavior is used, then JSON remains the default output format.

### INVEST Check

- **Independent**: Can be implemented after JSON output.
- **Negotiable**: Optional for first version.
- **Valuable**: Improves human review ergonomics.
- **Estimable**: Formatting-only behavior.
- **Small**: One alternate format.
- **Testable**: Can assert table headers and rows.

