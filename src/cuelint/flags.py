from __future__ import annotations

from cuelint.models import Flag, SummaryMetrics, ThresholdConfig


def default_thresholds() -> ThresholdConfig:
    return ThresholdConfig()


def evaluate_flags(metrics: SummaryMetrics, thresholds: ThresholdConfig) -> list[Flag]:
    return [
        Flag(
            flag_id="high_cue_density",
            triggered=metrics.cue_density_per_100_tokens >= thresholds.high_cue_density_per_100_tokens,
            metric="cue_density_per_100_tokens",
            value=metrics.cue_density_per_100_tokens,
            threshold=thresholds.high_cue_density_per_100_tokens,
            description="Cue density meets or exceeds the configured per-100-token threshold.",
        ),
        Flag(
            flag_id="first_paragraph_concentration",
            triggered=metrics.first_paragraph_cue_count >= thresholds.first_paragraph_cue_count,
            metric="first_paragraph_cue_count",
            value=metrics.first_paragraph_cue_count,
            threshold=thresholds.first_paragraph_cue_count,
            description="First paragraph cue count meets or exceeds the configured threshold.",
        ),
    ]
