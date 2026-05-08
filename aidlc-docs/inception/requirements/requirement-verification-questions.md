# Requirements Verification Questions

Please answer each question by filling in the letter choice after the `[Answer]:` tag. If none of the options match your needs, choose `X) Other` and describe your preference after the `[Answer]:` tag.

## Intent Captured So Far

The project intent is to build a lightweight, classical, cue-based audit kernel for monitoring disliked LLM output behaviors. The system should analyze assistant responses post-hoc, detect stable discourse operators such as negation, refusal, reframing, caveating, disclaimers, and contrastive clarification, and emit interpretable evidence tables rather than opaque moral judgments. The design should emphasize deterministic text processing, classical machine-learning-compatible features, low latency, portability, maintainability, and human review compatibility.

## Question 1
What should this greenfield repository become first?

A) Library or SDK for the audit kernel
B) Command-line tool for batch/local audits
C) API or backend service for integrating audits into pipelines
D) Web application or dashboard for human review
X) Other (please describe after [Answer]: tag below)

[Answer]: B

## Question 2
What is the first product outcome?

A) Prototype the deterministic cue kernel and evidence output
B) Build a production-ready embeddable package
C) Build a review workflow for QA/product teams
D) Build a research/evaluation harness for experiments
X) Other (please describe after [Answer]: tag below)

[Answer]: A

## Question 3
Who are the primary users or stakeholders?

A) Developers integrating the audit kernel
B) QA or product teams reviewing LLM output failures
C) Researchers evaluating discourse cues and failure categories
D) Individual users auditing assistant responses locally
X) Other (please describe after [Answer]: tag below)

[Answer]: D

## Question 4
What level of requirements detail should AI-DLC use for this project?

A) Minimal: document the core intent and move quickly
B) Standard: capture functional and non-functional requirements with focused clarification
C) Comprehensive: create detailed requirements with traceability and deeper review
X) Other (please describe after [Answer]: tag below)

[Answer]: A

## Question 5
What implementation language should be preferred for the first version?

A) Python
B) TypeScript/JavaScript
C) Rust
D) No preference, recommend during planning
X) Other (please describe after [Answer]: tag below)

[Answer]: A

## Question 6
What should the kernel emit as its primary output?

A) Evidence table with cue spans, categories, counts, densities, and positions
B) Binary or scored flags such as over-reframing, excessive disclaimer, or refusal candidate
C) Both evidence table and calibrated scores
D) Human-readable audit report only
X) Other (please describe after [Answer]: tag below)

[Answer]: A

## Question 7
Which language scope should be supported first?

A) English only
B) English first, Japanese cue families designed but not fully implemented
C) English and Japanese from the first version
D) Language-agnostic architecture with no committed initial language
X) Other (please describe after [Answer]: tag below)

[Answer]: A

## Question 8
Should the first version include classical machine-learning classifiers?

A) No, deterministic cue extraction and thresholding only
B) Yes, include feature extraction suitable for logistic regression or linear SVM, but no training pipeline
C) Yes, include a small training/evaluation pipeline for classical models
D) Defer this decision to Workflow Planning
X) Other (please describe after [Answer]: tag below)

[Answer]: A

## Question 9
Should security extension rules be enforced for this project?

A) Yes, enforce all SECURITY rules as blocking constraints (recommended for production-grade applications)
B) No, skip all SECURITY rules (suitable for PoCs, prototypes, and experimental projects)
X) Other (please describe after [Answer]: tag below)

[Answer]: B

## Question 10
Should property-based testing (PBT) rules be enforced for this project?

A) Yes, enforce all PBT rules as blocking constraints (recommended for projects with business logic, data transformations, serialization, or stateful components)
B) Partial, enforce PBT rules only for pure functions and serialization round-trips (suitable for projects with limited algorithmic complexity)
C) No, skip PBT rules (suitable for simple CRUD applications, UI-only projects, or thin integration layers with no significant business logic)
X) Other (please describe after [Answer]: tag below)

[Answer]: C
