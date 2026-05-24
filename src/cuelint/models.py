from __future__ import annotations

from dataclasses import asdict, dataclass, field
from re import Pattern
from typing import Literal


CueFamily = Literal[
    "raw_negation",
    "contrastive_reframing",
    "refusal",
    "disclaimer",
    "meta_negation",
    "hedging",
]


@dataclass(frozen=True)
class Paragraph:
    index: int
    start: int
    end: int
    text: str


@dataclass(frozen=True)
class Sentence:
    index: int
    paragraph_index: int
    start: int
    end: int
    text: str


@dataclass(frozen=True)
class MatchText:
    text: str
    original_starts: tuple[int, ...]
    original_ends: tuple[int, ...]


@dataclass(frozen=True)
class NormalizedDocument:
    original_text: str
    match_text: str
    original_starts: tuple[int, ...]
    original_ends: tuple[int, ...]
    paragraphs: tuple[Paragraph, ...]
    sentences: tuple[Sentence, ...]
    token_count: int


@dataclass(frozen=True)
class CuePattern:
    pattern_id: str
    family: CueFamily
    regex: Pattern[str]
    description: str


@dataclass(frozen=True)
class EvidenceRow:
    span_text: str
    cue_family: CueFamily
    start: int
    end: int
    sentence_index: int
    paragraph_index: int
    pattern_id: str

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(frozen=True)
class SummaryMetrics:
    cue_counts_by_family: dict[str, int]
    response_length: int
    paragraph_count: int
    sentence_count: int
    token_count: int
    cue_count: int
    cue_density: float
    first_paragraph_cue_count: int

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(frozen=True)
class Flag:
    flag_id: str
    triggered: bool
    metric: str
    value: float | int
    threshold: float | int
    description: str

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(frozen=True)
class ThresholdConfig:
    high_cue_density: float = 0.08
    first_paragraph_cue_count: int = 3


@dataclass(frozen=True)
class AuditConfig:
    thresholds: ThresholdConfig = field(default_factory=ThresholdConfig)


@dataclass(frozen=True)
class AuditResult:
    evidence: list[EvidenceRow]
    summary: SummaryMetrics
    flags: list[Flag]
    metadata: dict[str, object]


@dataclass(frozen=True)
class CliOptions:
    input_path: str | None
    output_format: str = "json"
