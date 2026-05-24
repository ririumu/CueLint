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
        _pattern("raw_did_not", "raw_negation", r"\bdid\s+not\b", "Did not cue"),
        _pattern("raw_will_not", "raw_negation", r"\bwill\s+not\b", "Will not cue"),
        _pattern("raw_is_not", "raw_negation", r"\bis\s+not\b", "Is not cue"),
        _pattern("raw_are_not", "raw_negation", r"\bare\s+not\b", "Are not cue"),
        _pattern("raw_was_not", "raw_negation", r"\bwas\s+not\b", "Was not cue"),
        _pattern("raw_has_not", "raw_negation", r"\bhas\s+not\b", "Has not cue"),
        _pattern("raw_have_not", "raw_negation", r"\bhave\s+not\b", "Have not cue"),
        _pattern("raw_had_not", "raw_negation", r"\bhad\s+not\b", "Had not cue"),
        _pattern("contrast_not_but", "contrastive_reframing", r"\bnot\b.{0,120}?\bbut\b", "not ... but cue"),
        _pattern("contrast_not_rather", "contrastive_reframing", r"\bnot\b.{0,120}?\brather\b", "not ... rather cue"),
        _pattern("contrast_not_instead", "contrastive_reframing", r"\bnot\b.{0,120}?\binstead\b", "not ... instead cue"),
        _pattern("contrast_issue_is_not", "contrastive_reframing", r"\b(?:the\s+)?issue\s+is\s+not\b", "Issue is not cue"),
        _pattern("contrast_instead_of", "contrastive_reframing", r"\binstead\s+of\b", "Instead of cue"),
        _pattern("contrast_rather_than", "contrastive_reframing", r"\brather\s+than\b", "Rather than cue"),
        _pattern("refusal_i_cannot", "refusal", r"\bi\s+cannot\b", "I cannot refusal cue"),
        _pattern(
            "refusal_i_cannot_action",
            "refusal",
            r"\bi\s+cannot\s+(?:assist|help|provide|give|create|comply|complete|access|browse)\b",
            "I cannot action refusal cue",
        ),
        _pattern("refusal_no_access", "refusal", r"\bi\s+do\s+not\s+have\s+access\b", "No access refusal cue"),
        _pattern("refusal_no_ability", "refusal", r"\bi\s+do\s+not\s+have\s+the\s+ability\b", "No ability refusal cue"),
        _pattern("refusal_not_able", "refusal", r"\bi\s+am\s+not\s+able\b", "Not able refusal cue"),
        _pattern("refusal_unable_to_assist", "refusal", r"\bunable\s+to\s+(?:assist|help|provide|comply)\b", "Unable to assist cue"),
        _pattern("refusal_i_will_not", "refusal", r"\bi\s+will\s+not\b", "I will not refusal cue"),
        _pattern("disclaimer_not_doctor", "disclaimer", r"\bnot\s+a\s+doctor\b", "Not a doctor disclaimer cue"),
        _pattern("disclaimer_not_constitute", "disclaimer", r"\bdoes\s+not\s+constitute\b", "Does not constitute disclaimer cue"),
        _pattern("disclaimer_cannot_guarantee", "disclaimer", r"\bcannot\s+guarantee\b", "Cannot guarantee disclaimer cue"),
        _pattern("disclaimer_informational_only", "disclaimer", r"\bfor\s+informational\s+purposes\s+only\b", "Informational purposes only cue"),
        _pattern("disclaimer_not_advice", "disclaimer", r"\bnot\s+(?:legal|medical|financial|professional)\s+advice\b", "Not advice cue"),
        _pattern("disclaimer_consult_professional", "disclaimer", r"\bconsult\s+(?:a|an|your)\s+(?:doctor|lawyer|attorney|professional|qualified\s+professional)\b", "Consult professional cue"),
        _pattern("disclaimer_not_substitute", "disclaimer", r"\bnot\s+a\s+substitute\s+for\b", "Not a substitute cue"),
        _pattern("disclaimer_as_ai", "disclaimer", r"\bas\s+an\s+ai(?:\s+language\s+model)?\b", "As an AI cue"),
        _pattern("meta_not_saying", "meta_negation", r"\bnot\s+saying\b", "Not saying cue"),
        _pattern("meta_not_mean", "meta_negation", r"\bdoes\s+not\s+mean\b", "Does not mean cue"),
        _pattern("meta_not_necessarily", "meta_negation", r"\bnot\s+necessarily\b", "Not necessarily cue"),
        _pattern("meta_not_imply", "meta_negation", r"\bdoes\s+not\s+imply\b", "Does not imply cue"),
        _pattern("meta_not_intended", "meta_negation", r"\bnot\s+intended\s+to\b", "Not intended to cue"),
        _pattern("meta_not_exhaustive", "meta_negation", r"\bnot\s+exhaustive\b", "Not exhaustive cue"),
        _pattern("meta_not_definitive", "meta_negation", r"\bnot\s+definitive\b", "Not definitive cue"),
        _pattern("meta_not_always", "meta_negation", r"\bnot\s+always\b", "Not always cue"),
        _pattern("hedge_in_general", "hedging", r"\bin\s+general\b", "In general hedging cue"),
        _pattern("hedge_generally_speaking", "hedging", r"\bgenerally\s+speaking\b", "Generally speaking cue"),
        _pattern("hedge_typically", "hedging", r"\btypically\b", "Typically cue"),
        _pattern("hedge_often", "hedging", r"\boften\b", "Often cue"),
        _pattern("hedge_may_vary", "hedging", r"\bmay\s+vary\b", "May vary cue"),
        _pattern("hedge_can_vary", "hedging", r"\bcan\s+vary\b", "Can vary cue"),
        _pattern("hedge_it_depends", "hedging", r"\bit\s+depends\b", "It depends cue"),
        _pattern("hedge_depends_on", "hedging", r"\bdepends\s+on\b", "Depends on cue"),
        _pattern("hedge_in_many_cases", "hedging", r"\bin\s+many\s+cases\b", "In many cases cue"),
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
