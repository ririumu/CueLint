# CueLint v0.1.1 Release Readiness

## Release Position

CueLint v0.1.1 is a scope-regrounding release. It preserves the existing local CLI behavior while making the public wording and JSON metadata clearer about CueLint's interpretation contract.

## Scope Correction

- README language now describes CueLint as a surface discourse cue evidence linter rather than a detector of response failure patterns.
- The Product Thesis now centers observable cue evidence for human review instead of disliked behavior classification.
- A new Interpretation Contract section states that CueLint does not infer response quality, over-refusal, safety correctness, factual correctness, semantic adequacy, or user intent.
- The design boundaries now explicitly exclude quality evaluation, over-refusal classification, safety evaluation, and user-intent inference.
- The valid local-first position is preserved: CueLint remains deterministic, inspectable, and runnable without an LLM judge or heavyweight evaluation stack.

## Output Contract

The CLI interface is unchanged. JSON metadata now includes non-breaking interpretation fields:

- `analysis_scope`: `surface_cue_evidence`
- `interpretation_contract`: `evidence_not_quality_label`
- `not_evaluated`: factual correctness, safety correctness, semantic quality, over-refusal classification, and user intent

These fields document how to read the output. They do not add a score, classifier, benchmark mode, dataset workflow, prompt-response pairing, or calibration pipeline.

## Verification

Commands run on 2026-05-24:

```sh
make test
```

Result: 25 tests passed.

```sh
make lint
```

Result: JSON evidence emitted successfully for `samples/assistant-response.txt`, including the v0.1.1 version and interpretation-contract metadata.

```sh
PYTHONPATH=src python -m cuelint --format markdown samples/assistant-response.txt
```

Result: Markdown report emitted successfully with cue count, cue cluster count, density, and evidence table.

## Release Judgment

Ready to publish as v0.1.1. The release corrects scope framing and output interpretation metadata without expanding CueLint into evaluation, benchmarking, calibration, multilingual analysis, or LLM-as-judge work.
