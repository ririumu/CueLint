# Application Design Plan

## Status

This retrospective plan was created after the user requested additional Inception artifacts based on the official AI-DLC artifact set. The existing requirements and newly generated user stories provide enough context to define a lightweight application design without additional questions.

## Design Scope

- **Application type**: Local Python CLI
- **Architecture style**: Small modular command-line application
- **Primary contract**: Deterministic audit result emitted as JSON by default
- **No infrastructure**: No service, database, deployment target, or network dependency
- **No trained model**: Deterministic normalization, matching, metrics, and flags only

## Execution Checklist

- [x] Review approved requirements.
- [x] Review user stories and personas.
- [x] Identify main functional components and responsibilities.
- [x] Generate `aidlc-docs/inception/application-design/components.md`.
- [x] Generate `aidlc-docs/inception/application-design/component-methods.md`.
- [x] Generate `aidlc-docs/inception/application-design/services.md`.
- [x] Generate `aidlc-docs/inception/application-design/component-dependency.md`.
- [x] Generate consolidated `aidlc-docs/inception/application-design/application-design.md`.
- [x] Validate design completeness and consistency.

## Design Questions

No open design questions are required for this pass. The requirements already establish a Python CLI, deterministic matching, JSON default output, optional Markdown output, English-only scope, and no ML training pipeline.

## Design Decisions

- Keep CLI orchestration separate from the audit kernel so tests can exercise the kernel without subprocess overhead.
- Keep normalization, matching, metrics, flags, and formatting as separate components with explicit data flow.
- Use simple structured values for evidence rows, summary metrics, and flags.
- Keep cue patterns inspectable in code structures rather than external model files.
- Treat Markdown output as a formatter over the same audit result, not as a separate analysis path.

