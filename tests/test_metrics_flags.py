import unittest

from cuelint.flags import evaluate_flags
from cuelint.metrics import calculate_cue_cluster_count, calculate_cue_density
from cuelint.models import SummaryMetrics, ThresholdConfig
from cuelint.service import audit_text


class MetricsFlagsTests(unittest.TestCase):
    def test_zero_token_density_is_zero(self):
        self.assertEqual(calculate_cue_density(3, 0), 0.0)

    def test_summary_metrics_for_zero_cue_input(self):
        result = audit_text("Everything is direct.")

        self.assertEqual(result.summary.cue_count, 0)
        self.assertEqual(result.summary.cue_cluster_count, 0)
        self.assertEqual(result.summary.cue_counts_by_family, {})
        self.assertEqual(result.summary.cue_density, 0.0)

    def test_nested_evidence_is_clustered_for_density(self):
        result = audit_text("This does not mean failure.")

        self.assertEqual(result.summary.cue_count, 3)
        self.assertEqual(result.summary.cue_cluster_count, 1)
        self.assertEqual(result.summary.cue_density, round(1 / result.summary.token_count, 4))
        self.assertEqual(calculate_cue_cluster_count(result.evidence), 1)

    def test_threshold_flags_trigger_at_boundaries(self):
        metrics = SummaryMetrics(
            cue_counts_by_family={},
            response_length=10,
            paragraph_count=1,
            sentence_count=1,
            token_count=10,
            cue_count=1,
            cue_cluster_count=1,
            cue_density=0.1,
            first_paragraph_cue_count=2,
            first_paragraph_cue_cluster_count=2,
        )
        flags = evaluate_flags(metrics, ThresholdConfig(high_cue_density=0.1, first_paragraph_cue_cluster_count=2))

        self.assertEqual(
            {flag.flag_id: flag.triggered for flag in flags},
            {
                "high_cue_density": True,
                "first_paragraph_concentration": True,
            },
        )
        self.assertTrue(all(flag.threshold is not None for flag in flags))


if __name__ == "__main__":
    unittest.main()
