from __future__ import annotations

from cuelint.models import Flag, SummaryMetrics, ThresholdConfig


def default_thresholds() -> ThresholdConfig:
    return ThresholdConfig()


def evaluate_flags(metrics: SummaryMetrics, thresholds: ThresholdConfig) -> list[Flag]:
    return [
        Flag(
            flag_id="high_cue_density",
            triggered=metrics.cue_density >= thresholds.high_cue_density,
            metric="cue_density",
            value=metrics.cue_density,
            threshold=thresholds.high_cue_density,
            description="Cue-cluster density meets or exceeds the configured deterministic threshold.",
        ),
        Flag(
            flag_id="first_paragraph_concentration",
            triggered=metrics.first_paragraph_cue_cluster_count >= thresholds.first_paragraph_cue_cluster_count,
            metric="first_paragraph_cue_cluster_count",
            value=metrics.first_paragraph_cue_cluster_count,
            threshold=thresholds.first_paragraph_cue_cluster_count,
            description="First paragraph cue-cluster count meets or exceeds the configured deterministic threshold.",
        ),
    ]
