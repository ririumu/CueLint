# PLAN 4: Public Repository Privacy Audit

## Context

Before making this repository public, audit the current tree and git history for public-readiness risks, with emphasis on PII, absolute paths, local-only artifacts, credentials, and commit metadata.

## Checklist

- [x] cut branch `codex/public-readiness-audit`
- [x] inventory repository state and publication scope
- [x] scan current tracked tree for PII, credentials, and absolute paths
- [x] scan git history blobs for PII, credentials, and absolute paths
- [x] inspect commit log metadata and messages for publication risks
- [x] review packaging and ignored/local artifacts for accidental publication
- [x] record audit evidence and findings
- [ ] commit public-readiness audit notes
- [ ] self-merge to `main`
- [ ] clear it `[x]`

## Completion Criteria

- [x] Audit covers both current files and all reachable git history.
- [x] Findings distinguish blockers from acceptable public metadata.
- [x] Any residual risks are documented with concrete remediation options.
