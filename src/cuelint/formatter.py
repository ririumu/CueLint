from __future__ import annotations

import json

from cuelint.errors import OutputFormatError
from cuelint.models import AuditResult


def format_report(result: AuditResult, output_format: str) -> str:
    if output_format == "json":
        return format_json(result)
    if output_format == "markdown":
        return format_markdown(result)
    raise OutputFormatError(f"unsupported output format: {output_format}")


def format_json(result: AuditResult) -> str:
    return json.dumps(_result_to_dict(result), indent=2, sort_keys=True) + "\n"


def format_markdown(result: AuditResult) -> str:
    lines = [
        "# CueLint Report",
        "",
        "## Summary",
        "",
        f"- Cue count: {result.summary.cue_count}",
        f"- Cue cluster count: {result.summary.cue_cluster_count}",
        f"- Token count: {result.summary.token_count}",
        f"- Cue density: {result.summary.cue_density}",
        f"- First paragraph cue count: {result.summary.first_paragraph_cue_count}",
        f"- First paragraph cue cluster count: {result.summary.first_paragraph_cue_cluster_count}",
        "",
        "## Evidence",
        "",
        "| family | pattern_id | start | end | sentence | paragraph | span |",
        "|---|---|---:|---:|---:|---:|---|",
    ]
    for row in result.evidence:
        span = row.span_text.replace("|", "\\|").replace("\n", " ")
        lines.append(
            f"| {row.cue_family} | {row.pattern_id} | {row.start} | {row.end} | "
            f"{row.sentence_index} | {row.paragraph_index} | `{span}` |"
        )
    return "\n".join(lines) + "\n"


def _result_to_dict(result: AuditResult) -> dict[str, object]:
    return {
        "evidence": [row.to_dict() for row in result.evidence],
        "summary": result.summary.to_dict(),
        "flags": [flag.to_dict() for flag in result.flags],
        "metadata": result.metadata,
    }
