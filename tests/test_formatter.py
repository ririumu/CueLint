import json

from cuelint.formatter import format_json, format_markdown, format_report
from cuelint.service import audit_text


def test_json_output_is_valid_and_contains_expected_top_level_keys():
    payload = json.loads(format_json(audit_text("I cannot guarantee it.")))

    assert sorted(payload.keys()) == ["evidence", "flags", "summary", "thresholds", "version"]
    assert payload["evidence"][0]["span"] == "cannot"


def test_empty_evidence_outputs_empty_json_array():
    payload = json.loads(format_report(audit_text("Direct answer."), "json"))

    assert payload["evidence"] == []


def test_markdown_output_has_table_header():
    report = format_markdown(audit_text("This does not mean failure."))

    assert "| family | pattern_id | start | end | sentence | paragraph | span |" in report
    assert "meta.does_not_mean" in report
