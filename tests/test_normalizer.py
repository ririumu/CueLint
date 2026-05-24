import unittest

from cuelint.normalizer import count_tokens, normalize_document, normalize_for_matching


class NormalizerTests(unittest.TestCase):
    def test_matching_normalization_preserves_offsets_for_case_and_curly_apostrophe(self):
        text = "I CAN'T guarantee this."
        normalized = normalize_for_matching(text)

        self.assertEqual(normalized.text, "i cannot guarantee this.")
        start = normalized.text.index("cannot")
        end = start + len("cannot")
        self.assertEqual(normalized.original_starts[start], 2)
        self.assertEqual(normalized.original_ends[end - 1], 7)

    def test_segments_paragraphs_and_sentences_with_offsets(self):
        text = "First sentence. Second sentence!\n\nThird paragraph"
        document = normalize_document(text)

        self.assertEqual([p.text for p in document.paragraphs], ["First sentence. Second sentence!", "Third paragraph"])
        self.assertEqual([s.text for s in document.sentences], ["First sentence.", "Second sentence!", "Third paragraph"])
        self.assertEqual(document.sentences[2].paragraph_index, 1)
        self.assertEqual(text[document.sentences[1].start : document.sentences[1].end], "Second sentence!")

    def test_no_punctuation_sentence_boundary(self):
        document = normalize_document("No final punctuation")

        self.assertEqual(len(document.sentences), 1)
        self.assertEqual(document.sentences[0].text, "No final punctuation")

    def test_token_count_is_deterministic_for_contractions(self):
        self.assertEqual(count_tokens("I can't, and I do not."), 6)


if __name__ == "__main__":
    unittest.main()
