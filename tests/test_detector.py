from cuelint.detector import detect_cues
from cuelint.normalizer import normalize_document
from cuelint.patterns import load_patterns, pattern_families


def test_pattern_catalog_contains_required_families() -> None:
    assert pattern_families() == [
        "contrastive_reframing",
        "disclaimer",
        "meta_negation",
        "raw_negation",
        "refusal",
    ]


def test_detects_required_families_and_original_spans() -> None:
    text = "I can't guarantee this. This is not a diagnosis but a note."
    rows = detect_cues(normalize_document(text), load_patterns())
    families = {row.cue_family for row in rows}

    assert "raw_negation" in families
    assert "disclaimer" in families
    assert "contrastive_reframing" in families
    assert any(row.span_text == "can't guarantee" for row in rows)
    assert any(row.span_text == "not a diagnosis but" for row in rows)


def test_keeps_overlapping_different_family_matches_but_orders_stably() -> None:
    rows = detect_cues(normalize_document("This does not mean no."), load_patterns())

    assert [row.start for row in rows] == sorted(row.start for row in rows)
    assert any(row.pattern_id == "meta_not_mean" for row in rows)
    assert any(row.pattern_id == "raw_does_not" for row in rows)


def test_non_matching_text_has_no_evidence() -> None:
    rows = detect_cues(normalize_document("Clear direct answer with evidence."), load_patterns())

    assert rows == []
