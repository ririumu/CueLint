from __future__ import annotations

import re

from cuelint.models import CuePattern


def load_patterns() -> list[CuePattern]:
    return [
        _pattern("raw_no", "raw_negation", r"\bno\b", "Standalone no cue"),
        _pattern("raw_not", "raw_negation", r"\bnot\b", "Standalone not cue"),
        _pattern("raw_never", "raw_negation", r"\bnever\b", "Standalone never cue"),
        _pattern("raw_cannot", "raw_negation", r"\bcannot\b", "Cannot cue"),
        _pattern("raw_do_not", "raw_negation", r"\bdo\s+not\b", "Do not cue"),
        _pattern("raw_does_not", "raw_negation", r"\bdoes\s+not\b", "Does not cue"),
        _pattern("raw_is_not", "raw_negation", r"\bis\s+not\b", "Is not cue"),
        _pattern("raw_was_not", "raw_negation", r"\bwas\s+not\b", "Was not cue"),
        _pattern("raw_has_not", "raw_negation", r"\bhas\s+not\b", "Has not cue"),
        _pattern("contrast_not_but", "contrastive_reframing", r"\bnot\b.{0,120}?\bbut\b", "not ... but cue"),
        _pattern("contrast_not_rather", "contrastive_reframing", r"\bnot\b.{0,120}?\brather\b", "not ... rather cue"),
        _pattern("contrast_not_instead", "contrastive_reframing", r"\bnot\b.{0,120}?\binstead\b", "not ... instead cue"),
        _pattern("refusal_i_cannot", "refusal", r"\bi\s+cannot\b", "I cannot refusal cue"),
        _pattern("refusal_no_access", "refusal", r"\bi\s+do\s+not\s+have\s+access\b", "No access refusal cue"),
        _pattern("refusal_not_able", "refusal", r"\bi\s+am\s+not\s+able\b", "Not able refusal cue"),
        _pattern("disclaimer_not_doctor", "disclaimer", r"\bnot\s+a\s+doctor\b", "Not a doctor disclaimer cue"),
        _pattern("disclaimer_not_constitute", "disclaimer", r"\bdoes\s+not\s+constitute\b", "Does not constitute disclaimer cue"),
        _pattern("disclaimer_cannot_guarantee", "disclaimer", r"\bcannot\s+guarantee\b", "Cannot guarantee disclaimer cue"),
        _pattern("meta_not_saying", "meta_negation", r"\bnot\s+saying\b", "Not saying cue"),
        _pattern("meta_not_mean", "meta_negation", r"\bdoes\s+not\s+mean\b", "Does not mean cue"),
        _pattern("meta_not_necessarily", "meta_negation", r"\bnot\s+necessarily\b", "Not necessarily cue"),
    ]


def pattern_families() -> list[str]:
    return sorted({pattern.family for pattern in load_patterns()})


def _pattern(pattern_id: str, family: str, regex: str, description: str) -> CuePattern:
    return CuePattern(
        pattern_id=pattern_id,
        family=family,  # type: ignore[arg-type]
        regex=re.compile(regex, re.IGNORECASE | re.DOTALL),
        description=description,
    )
