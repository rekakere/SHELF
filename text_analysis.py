from __future__ import annotations

import re
from dataclasses import dataclass
from collections import Counter


WORD_PATTERN = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ']+")


@dataclass(frozen=True)
class TextAnalysis:
    word_count: int
    unique_words: int
    lexical_diversity: float
    average_word_length: float
    most_common_words: list[tuple[str, int]]
    estimated_level: str


def tokenize(text: str) -> list[str]:
    return [match.group(0).lower() for match in WORD_PATTERN.finditer(text)]


def estimate_reading_level(
    word_count: int,
    lexical_diversity: float,
    average_word_length: float,
) -> str:
    if word_count < 25 and average_word_length < 5:
        return "beginner"

    if lexical_diversity >= 0.7 or average_word_length >= 6.2:
        return "advanced"

    if lexical_diversity >= 0.55 or average_word_length >= 5.3:
        return "intermediate"

    return "early-intermediate"


def analyze_text(text: str, top_n: int = 8) -> TextAnalysis:
    words = tokenize(text)

    if not words:
        return TextAnalysis(
            word_count=0,
            unique_words=0,
            lexical_diversity=0.0,
            average_word_length=0.0,
            most_common_words=[],
            estimated_level="unknown",
        )

    counts = Counter(words)
    word_count = len(words)
    unique_words = len(counts)
    lexical_diversity = unique_words / word_count
    average_word_length = sum(len(word) for word in words) / word_count

    return TextAnalysis(
        word_count=word_count,
        unique_words=unique_words,
        lexical_diversity=round(lexical_diversity, 3),
        average_word_length=round(average_word_length, 2),
        most_common_words=counts.most_common(top_n),
        estimated_level=estimate_reading_level(
            word_count,
            lexical_diversity,
            average_word_length,
        ),
    )


if __name__ == "__main__":
    sample_text = "Estoy leyendo un texto nuevo y quiero guardar palabras útiles."
    print(analyze_text(sample_text))
