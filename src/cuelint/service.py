from __future__ import annotations

from cuelint import __version__
from cuelint.detector import detect_cues
from cuelint.flags import default_thresholds, evaluate_flags
from cuelint.metrics import calculate_metrics
from cuelint.models import AuditConfig, AuditResult
from cuelint.normalizer import normalize_document
from cuelint.patterns import load_patterns


def build_default_config() -> AuditConfig:
    return AuditConfig(thresholds=default_thresholds())


def audit_text(text: str, config: AuditConfig | None = None) -> AuditResult:
    runtime_config = config or build_default_config()
    document = normalize_document(text)
    evidence = detect_cues(document, load_patterns())
    summary = calculate_metrics(document, evidence)
    flags = evaluate_flags(summary, runtime_config.thresholds)
    return AuditResult(
        evidence=evidence,
        summary=summary,
        flags=flags,
        metadata={
            "version": __version__,
            "language_scope": "en",
            "deterministic": True,
            "thresholds": {
                "high_cue_density": runtime_config.thresholds.high_cue_density,
                "first_paragraph_cue_cluster_count": runtime_config.thresholds.first_paragraph_cue_cluster_count,
            },
            "density_basis": "overlapping cue spans are collapsed into cue clusters",
        },
    )
