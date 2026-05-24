from cuelint.normalizer import normalize_document, normalize_for_matching, segment_paragraphs


def test_normalize_for_matching_expands_contractions_with_original_offsets() -> None:
    text = "I can't do that."
    normalized = normalize_for_matching(text)

    start = normalized.text.index("cannot")
    end = start + len("cannot")

    assert normalized.text == "i cannot do that."
    assert normalized.original_starts[start] == 2
    assert normalized.original_ends[end - 1] == 7
    assert text[2:7] == "can't"


def test_segment_paragraphs_preserves_offsets() -> None:
    text = "First paragraph.\n\nSecond paragraph."
    paragraphs = segment_paragraphs(text)

    assert len(paragraphs) == 2
    assert paragraphs[0].start == 0
    assert paragraphs[1].text == "Second paragraph."
    assert text[paragraphs[1].start : paragraphs[1].end] == "Second paragraph."


def test_normalize_document_segments_sentences_across_paragraphs() -> None:
    document = normalize_document("No. This is not ideal.\n\nStill no panic")

    assert document.token_count == 8
    assert len(document.paragraphs) == 2
    assert len(document.sentences) == 3
    assert document.sentences[2].paragraph_index == 1
