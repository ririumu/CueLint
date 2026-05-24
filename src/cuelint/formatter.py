from __future__ import annotations

import json

from cuelint.errors import UnsupportedFormatError
from cuelint.models import AuditResult


def format_report(result: AuditResult, output_format: str) -> str:
    if output_format == "json":
        return format_json(result)
    if output_format == "markdown":
        return format_markdown(result)
    raise UnsupportedFormatError(f"unsupported output format: {output_format}")


def format_json(result: AuditResult) -> str:
    return json.dumps(result.to_dict(), indent=2, sort_keys=True) + "\n"


def format_markdown(result: AuditResult) -> str:
    lines = [
        "# CueLint Report",
        "",
        "## Summary",
        "",
        f"- Evidence count: {result.summary.evidence_count}",
        f"- Token count: {result.summary.token_count}",
        f"- Cue density per 100 tokens: {result.summary.cue_density_per_100_tokens}",
        f"- First paragraph cue count: {result.summary.first_paragraph_cue_count}",
        "",
        "## Evidence",
        "",
        "| family | pattern_id | start | end | sentence | paragraph | span |",
        "|---|---|---:|---:|---:|---:|---|",
    ]
    for row in result.evidence:
        span = row.span.replace("|", "\\|").replace("\n", " ")
        lines.append(
            f"| {row.family} | {row.pattern_id} | {row.start} | {row.end} | "
            f"{row.sentence_index} | {row.paragraph_index} | `{span}` |"
        )
    return "\n".join(lines) + "\n"
