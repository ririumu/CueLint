# Personas

## Primary Persona: Researcher Using AI

### Profile

A researcher who regularly saves or pipes LLM assistant responses and wants a lightweight local tool to inspect recurring discourse patterns. This user is comfortable with command-line workflows and values transparent evidence over opaque judgments.

### Goals

- Inspect one assistant response quickly from stdin or a text file.
- See concrete cue spans, offsets, cue families, and pattern identifiers.
- Compare responses using simple counts, densities, and deterministic flags.
- Keep analysis local, reproducible, and independent of network access or LLM-as-judge services.

### Needs

- A predictable CLI that fits into `make lint` and shell pipelines.
- Machine-readable JSON output suitable for downstream analysis.
- Optional human-readable output for quick review.
- Explicit evidence that explains why each cue or flag was emitted.

### Frustrations

- Opaque model judgments that do not show supporting evidence.
- Tools that overstate semantic conclusions from surface-level signals.
- Heavy setup, service dependencies, or dashboards for a small local audit task.
- Output formats that are hard to test or compare.

### Relevant Stories

- US1: Audit text from stdin.
- US2: Audit text from a file.
- US3: Detect deterministic cue families.
- US4: Emit structured JSON evidence.
- US5: Show summary metrics and deterministic flags.
- US6: Run a local lint workflow.
- US7: Preserve scope boundaries.

## Secondary Persona: Future Maintainer

### Profile

A developer who maintains CueLint's cue patterns, normalization behavior, CLI interface, and tests after the first prototype.

### Goals

- Understand component responsibilities without reverse engineering the code.
- Add or adjust cue patterns without rewriting the audit pipeline.
- Keep tests focused on deterministic behavior and output contracts.
- Avoid accidental expansion into service, dashboard, or ML training work.

### Relevant Stories

- US3: Detect deterministic cue families.
- US4: Emit structured JSON evidence.
- US5: Show summary metrics and deterministic flags.
- US6: Run a local lint workflow.
- US7: Preserve scope boundaries.

