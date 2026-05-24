from cuelint.flags import evaluate_flags
from cuelint.metrics import calculate_cue_density
from cuelint.models import SummaryMetrics, ThresholdConfig
from cuelint.service import audit_text


def test_zero_token_density_is_zero():
    assert calculate_cue_density(3, 0) == 0.0


def test_summary_metrics_for_zero_cue_input():
    result = audit_text("Everything is direct.")

    assert result.summary.evidence_count == 0
    assert result.summary.counts_by_family == {}
    assert result.summary.cue_density_per_100_tokens == 0.0


def test_threshold_flags_trigger_at_boundaries():
    metrics = SummaryMetrics(
        counts_by_family={},
        response_length_chars=10,
        paragraph_count=1,
        sentence_count=1,
        token_count=10,
        evidence_count=1,
        cue_density_per_100_tokens=10.0,
        first_paragraph_cue_count=2,
    )
    flags = evaluate_flags(metrics, ThresholdConfig(high_cue_density_per_100_tokens=10.0, first_paragraph_cue_count=2))

    assert {flag.flag_id: flag.triggered for flag in flags} == {
        "high_cue_density": True,
        "first_paragraph_concentration": True,
    }
    assert all(flag.threshold is not None for flag in flags)
