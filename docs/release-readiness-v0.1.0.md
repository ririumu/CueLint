# CueLint v0.1.0 Release Readiness

## Release Position

CueLint v0.1.0 is a public portfolio release for `ririumu/cuelint`. It is a finished local CLI for deterministic cue evidence extraction over one English assistant response per invocation.

## Critique Response

- Weak pre-publication wording was removed from the README.
- Package metadata now uses the `Development Status :: 4 - Beta` classifier instead of Alpha.
- The deterministic cue catalog was broadened from 21 to 52 patterns.
- `hedging` is now a first-class cue family alongside raw negation, refusal, disclaimer, meta-negation, and contrastive reframing.
- Nested evidence rows remain visible, but cue density now counts overlapping local spans as cue clusters.
- Threshold flags now use cue-cluster metrics and describe themselves as deterministic tripwires rather than calibrated risk scores.

## Pattern Inventory

| Family | Pattern Count |
|---|---:|
| contrastive_reframing | 6 |
| disclaimer | 8 |
| hedging | 9 |
| meta_negation | 8 |
| raw_negation | 14 |
| refusal | 7 |
| **Total** | **52** |

## Verification

Commands run on 2026-05-24:

```sh
make test
```

Result: 25 tests passed.

```sh
make lint
```

Result: JSON evidence emitted successfully for `samples/assistant-response.txt`.

```sh
PYTHONPATH=src python -m cuelint --format markdown samples/assistant-response.txt
```

Result: Markdown report emitted successfully with cue count, cue cluster count, density, and evidence table.

## Release Judgment

Ready to publish as v0.1.0. The release is intentionally scoped, deterministic, locally runnable, tested, and documented as a complete portfolio artifact rather than a pre-publication prototype.
