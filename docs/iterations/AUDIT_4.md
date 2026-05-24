# AUDIT 4: Public Repository Privacy Audit

## Log

- 2026-05-24T15:23:00+09:00: Created branch `codex/public-readiness-audit` from `main`.
- 2026-05-24T15:23:00+09:00: Created `PLAN_4.md` and `AUDIT_4.md` for public-readiness audit tracking.
- 2026-05-24T15:24:00+09:00: Inventoried tracked files and git log; repository has 76 tracked files and 21 reachable commits before this audit commit.
- 2026-05-24T15:25:00+09:00: Scanned the current tracked tree for absolute paths, email-like strings, credentials, API keys, private keys, phone-like values, SSN-like values, and credit-card-like values.
- 2026-05-24T15:27:00+09:00: Scanned all reachable git history with `git grep` for absolute paths, email-like strings, credential keywords, API key/token/private-key signatures, and obvious numeric PII patterns.
- 2026-05-24T15:29:00+09:00: Inspected commit metadata with `git log --all --format='%H %an <%ae> %cn <%ce> %s'`.
- 2026-05-24T15:31:00+09:00: Reviewed `.gitignore`, `pyproject.toml`, tracked-file sizes, and ignored/untracked status for packaging or generated-artifact exposure.
- 2026-05-24T15:33:00+09:00: Redacted current-tree absolute paths in `aidlc-docs/aidlc-state.md`, `aidlc-docs/audit.md`, and `aidlc-docs/construction/plans/cuelint-code-generation-plan.md`.
- 2026-05-24T15:35:00+09:00: Re-ran current-tree absolute-path and credential-signature scans; no hits remained outside `.git/`.
- 2026-05-24T15:36:00+09:00: Re-ran history scan for obvious phone-like, SSN-like, and credit-card-like numeric PII patterns; no hits found.
- 2026-05-24T15:36:00+09:00: Ran `make test`: 22 tests passed.

## Findings

### Blocking / High-Confidence Risks

1. **Reachable git history still contains personal absolute paths.**
   - Affected paths in history:
     - `aidlc-docs/aidlc-state.md`
     - `aidlc-docs/audit.md`
     - `aidlc-docs/construction/plans/cuelint-code-generation-plan.md`
   - Values observed were user-home absolute paths for the old and current workspace roots; the exact strings are intentionally redacted from this audit note.
   - Current tree has been redacted, but publicizing the repository with full existing history would still expose these paths.
   - Remediation before public release: either rewrite history to replace those strings, or publish a fresh/squashed repository that starts after redaction.

### Non-Blocking / Acceptable Public Metadata

1. **Commit metadata uses GitHub noreply email only.**
   - Observed unique author/committer email: `33805628+ririumu@users.noreply.github.com`.
   - This is expected public GitHub metadata, not a private mailbox.

2. **Credential keyword hits are documentation examples, not secrets.**
   - Hits are in `.aidlc-rule-details/common/question-format-guide.md` and `.aidlc-rule-details/extensions/security/baseline/security-baseline.md`.
   - They describe password/token handling requirements and example answer text.
   - No API key, bearer token, private key block, GitHub token, OpenAI-style `sk-...`, AWS `AKIA...`, or similar credential-shaped value was found in the current tree scan.

3. **No obvious numeric PII found.**
   - Focused scans for phone-like, SSN-like, and credit-card-like patterns returned no current-tree or reachable-history hits.

4. **Packaging metadata is narrow.**
   - `pyproject.toml` packages only `src/` via setuptools package discovery.
   - No dependency secrets or private indexes are configured.

5. **Ignored generated artifacts are covered.**
   - `.gitignore` excludes `__pycache__/`, `*.py[cod]`, `.pytest_cache/`, `.venv/`, `dist/`, `build/`, and `*.egg-info/`.
   - `git status --ignored --short` showed only the new audit docs as untracked at inspection time.

### Current-Tree Remediation Completed

- Replaced current-tree workspace-root disclosures with `<workspace-root>`.
- Replaced old absolute Markdown reference targets under the prior user-home workspace path with repository-root style paths.
- Verified with a follow-up current-tree absolute-path scan: no user-home, `/home`, `/private`, `/var/folders`, Windows user-profile, or `file` URL path hits remain outside `.git/`.

### Public Release Judgment

Not ready for public release with full history intact. The current tree is clean for the checked absolute-path concern after remediation, and no credential/obvious PII blockers were found, but the reachable git history still discloses local absolute paths. Publish only after history rewrite/squash/fresh-import, then rerun the same scans on the final public branch.
