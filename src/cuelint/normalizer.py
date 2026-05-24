from __future__ import annotations

import re

from cuelint.models import MatchText, NormalizedDocument, Paragraph, Sentence

_CONTRACTIONS = {
    "can't": "cannot",
    "cannot": "cannot",
    "won't": "will not",
    "don't": "do not",
    "doesn't": "does not",
    "didn't": "did not",
    "isn't": "is not",
    "wasn't": "was not",
    "aren't": "are not",
    "weren't": "were not",
    "hasn't": "has not",
    "haven't": "have not",
    "hadn't": "had not",
    "i'm": "i am",
}

_CONTRACTION_RE = re.compile(
    "|".join(re.escape(key) for key in sorted(_CONTRACTIONS, key=len, reverse=True)),
    re.IGNORECASE,
)
_TOKEN_RE = re.compile(r"[A-Za-z0-9]+(?:'[A-Za-z0-9]+)?")
_SENTENCE_END_RE = re.compile(r"[.!?]+(?:\s+|$)")


def normalize_document(text: str) -> NormalizedDocument:
    match = normalize_for_matching(text)
    paragraphs = tuple(segment_paragraphs(text))
    sentences = tuple(segment_sentences(text, paragraphs))
    return NormalizedDocument(
        original_text=text,
        match_text=match.text,
        original_starts=match.original_starts,
        original_ends=match.original_ends,
        paragraphs=paragraphs,
        sentences=sentences,
        token_count=count_tokens(text),
    )


def normalize_for_matching(text: str) -> MatchText:
    pieces: list[str] = []
    starts: list[int] = []
    ends: list[int] = []
    cursor = 0

    for match in _CONTRACTION_RE.finditer(text):
        if match.start() > cursor:
            _append_literal(text[cursor : match.start()], cursor, pieces, starts, ends)

        replacement = _CONTRACTIONS[match.group(0).lower()]
        pieces.append(replacement)
        starts.extend([match.start()] * len(replacement))
        ends.extend([match.end()] * len(replacement))
        cursor = match.end()

    if cursor < len(text):
        _append_literal(text[cursor:], cursor, pieces, starts, ends)

    return MatchText("".join(pieces), tuple(starts), tuple(ends))


def segment_paragraphs(text: str) -> list[Paragraph]:
    paragraphs: list[Paragraph] = []
    for index, match in enumerate(re.finditer(r"\S(?:.*?\S)?(?=\n\s*\n|\s*\Z)", text, re.DOTALL)):
        paragraphs.append(
            Paragraph(
                index=index,
                start=match.start(),
                end=match.end(),
                text=text[match.start() : match.end()],
            )
        )
    return paragraphs


def segment_sentences(text: str, paragraphs: tuple[Paragraph, ...] | list[Paragraph] | None = None) -> list[Sentence]:
    source_paragraphs = list(paragraphs) if paragraphs is not None else segment_paragraphs(text)
    sentences: list[Sentence] = []

    for paragraph in source_paragraphs:
        local_start = 0
        paragraph_text = paragraph.text
        for match in _SENTENCE_END_RE.finditer(paragraph_text):
            end = match.end()
            sentence = paragraph_text[local_start:end].strip()
            if sentence:
                start_offset = paragraph.start + local_start + len(paragraph_text[local_start:end]) - len(paragraph_text[local_start:end].lstrip())
                sentences.append(
                    Sentence(
                        index=len(sentences),
                        paragraph_index=paragraph.index,
                        start=start_offset,
                        end=paragraph.start + end,
                        text=text[start_offset : paragraph.start + end].strip(),
                    )
                )
            local_start = end

        tail = paragraph_text[local_start:].strip()
        if tail:
            start_offset = paragraph.start + local_start + len(paragraph_text[local_start:]) - len(paragraph_text[local_start:].lstrip())
            sentences.append(
                Sentence(
                    index=len(sentences),
                    paragraph_index=paragraph.index,
                    start=start_offset,
                    end=paragraph.end,
                    text=text[start_offset : paragraph.end].strip(),
                )
            )

    return sentences


def count_tokens(text: str) -> int:
    return len(_TOKEN_RE.findall(text))


def _append_literal(
    literal: str,
    base_offset: int,
    pieces: list[str],
    starts: list[int],
    ends: list[int],
) -> None:
    pieces.append(literal.lower())
    starts.extend(base_offset + index for index in range(len(literal)))
    ends.extend(base_offset + index + 1 for index in range(len(literal)))
