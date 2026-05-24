from __future__ import annotations

from bisect import bisect_right

from cuelint.models import CuePattern, EvidenceRow, NormalizedDocument, Paragraph, Sentence


def detect_cues(document: NormalizedDocument, patterns: list[CuePattern]) -> list[EvidenceRow]:
    rows: list[EvidenceRow] = []
    seen: set[tuple[int, int, str, str]] = set()

    for pattern in patterns:
        for match in pattern.regex.finditer(document.match_text):
            if match.start() >= len(document.original_starts) or match.end() == 0:
                continue
            start = document.original_starts[match.start()]
            end = document.original_ends[match.end() - 1]
            key = (start, end, pattern.family, pattern.pattern_id)
            if key in seen:
                continue
            seen.add(key)
            rows.append(
                EvidenceRow(
                    span_text=document.original_text[start:end],
                    cue_family=pattern.family,
                    start=start,
                    end=end,
                    sentence_index=locate_sentence(document, start),
                    paragraph_index=locate_paragraph(document, start),
                    pattern_id=pattern.pattern_id,
                )
            )

    return sort_evidence(rows)


def locate_sentence(document: NormalizedDocument, start: int) -> int:
    return _locate_by_start(document.sentences, start)


def locate_paragraph(document: NormalizedDocument, start: int) -> int:
    return _locate_by_start(document.paragraphs, start)


def sort_evidence(rows: list[EvidenceRow]) -> list[EvidenceRow]:
    return sorted(rows, key=lambda row: (row.start, row.end, row.cue_family, row.pattern_id))


def _locate_by_start(items: tuple[Sentence, ...] | tuple[Paragraph, ...], start: int) -> int:
    starts = [item.start for item in items]
    index = bisect_right(starts, start) - 1
    if index < 0:
        return -1
    item = items[index]
    if item.start <= start < item.end:
        return item.index
    return -1
