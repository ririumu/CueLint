import unittest

from cuelint.detector import detect_cues
from cuelint.normalizer import normalize_document
from cuelint.patterns import load_patterns, pattern_families


def _detect(text):
    return detect_cues(normalize_document(text), load_patterns())


class DetectorTests(unittest.TestCase):
    def test_pattern_families_include_required_groups(self):
        self.assertEqual(
            pattern_families(),
            [
                "contrastive_reframing",
                "disclaimer",
                "meta_negation",
                "raw_negation",
                "refusal",
            ],
        )

    def test_detects_refusal_and_preserves_original_span_offsets(self):
        text = "Maybe. I CAN'T guarantee that."
        rows = _detect(text)
        guarantee = next(row for row in rows if row.pattern_id == "disclaimer_cannot_guarantee")

        self.assertEqual(guarantee.span_text, "CAN'T guarantee")
        self.assertEqual(text[guarantee.start : guarantee.end], guarantee.span_text)
        self.assertEqual(guarantee.sentence_index, 1)
        self.assertEqual(guarantee.paragraph_index, 0)

    def test_allows_overlapping_matches_from_different_families(self):
        rows = _detect("This does not mean the plan is bad.")
        ids = [row.pattern_id for row in rows]

        self.assertIn("raw_not", ids)
        self.assertIn("raw_does_not", ids)
        self.assertIn("meta_not_mean", ids)

    def test_repeated_cues_are_stable_and_sorted(self):
        rows = _detect("No. No. It is not X but Y.")

        self.assertEqual([row.start for row in rows], sorted(row.start for row in rows))
        self.assertEqual(sum(1 for row in rows if row.pattern_id == "raw_no"), 2)
        self.assertTrue(any(row.pattern_id == "contrast_not_but" for row in rows))

    def test_non_match_input_has_no_evidence(self):
        self.assertEqual(_detect("Everything looks complete and direct."), [])


if __name__ == "__main__":
    unittest.main()
