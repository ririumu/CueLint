from __future__ import annotations

from collections import Counter

from cuelint.models import EvidenceRow, NormalizedDocument, SummaryMetrics


def calculate_metrics(document: NormalizedDocument, evidence: list[EvidenceRow]) -> SummaryMetrics:
    return SummaryMetrics(
        cue_counts_by_family=count_by_family(evidence),
        response_length=len(document.original_text),
        paragraph_count=len(document.paragraphs),
        sentence_count=len(document.sentences),
        token_count=document.token_count,
        cue_count=len(evidence),
        cue_density=calculate_cue_density(len(evidence), document.token_count),
        first_paragraph_cue_count=sum(1 for row in evidence if row.paragraph_index == 0),
    )


def count_by_family(evidence: list[EvidenceRow]) -> dict[str, int]:
    return dict(sorted(Counter(row.cue_family for row in evidence).items()))


def calculate_cue_density(evidence_count: int, token_count: int) -> float:
    if token_count <= 0:
        return 0.0
    return round(evidence_count / token_count, 4)
