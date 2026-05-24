import json
import unittest

from cuelint.formatter import format_json, format_markdown, format_report
from cuelint.service import audit_text


class FormatterTests(unittest.TestCase):
    def test_json_output_is_valid_and_contains_expected_top_level_keys(self):
        payload = json.loads(format_json(audit_text("I cannot guarantee it.")))

        self.assertEqual(sorted(payload.keys()), ["evidence", "flags", "metadata", "summary"])
        self.assertTrue(any(row["span_text"] == "cannot" for row in payload["evidence"]))
        self.assertIn("cue_cluster_count", payload["summary"])
        self.assertEqual(payload["metadata"]["density_basis"], "overlapping cue spans are collapsed into cue clusters")

    def test_empty_evidence_outputs_empty_json_array(self):
        payload = json.loads(format_report(audit_text("Direct answer."), "json"))

        self.assertEqual(payload["evidence"], [])

    def test_markdown_output_has_table_header(self):
        report = format_markdown(audit_text("This does not mean failure."))

        self.assertIn("| family | pattern_id | start | end | sentence | paragraph | span |", report)
        self.assertIn("- Cue cluster count:", report)
        self.assertIn("meta_not_mean", report)


if __name__ == "__main__":
    unittest.main()
