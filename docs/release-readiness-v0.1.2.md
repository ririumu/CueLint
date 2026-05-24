# CueLint v0.1.2 Release Readiness

## Release Position

CueLint v0.1.2 is a README expectation cleanup release. It keeps the existing CLI behavior, cue catalog, JSON output contract, thresholds, and v0.1.1 interpretation metadata intact.

## README Cleanup

- Removed the current-status block that described the project as a public verified portfolio release.
- Removed the long versioned scope table, implemented-requirements section, and out-of-scope list from the README.
- Replaced those sections with a compact Limits section that describes the current English-only, one-response, surface-cue evidence scope without implying a roadmap.
- Reworded `Version 0.1.x` language to neutral current-implementation language.
- Renamed `Product Thesis` to `Why cues?` so the README reads less like a managed product document.

## Verification

Commands run on 2026-05-24:

```sh
make test
```

Result: 25 tests passed.

```sh
make lint
```

Result: JSON evidence emitted successfully for `samples/assistant-response.txt`, including version `0.1.2`.

```sh
PYTHONPATH=src python -m cuelint --format markdown samples/assistant-response.txt
```

Result: Markdown report emitted successfully with cue count, cue cluster count, density, and evidence table.

README cleanup checks confirmed that the README no longer contains `Current status`, `portfolio release`, `public, verified`, `Version 0.1.x Scope`, `Implemented Requirements`, or `Out of Scope for Version`.

## Release Judgment

Ready to publish as v0.1.2. This is not a feature release; it is a documentation expectation cleanup and version/tag release.
