from __future__ import annotations

from dataclasses import dataclass


IRREGULAR_FORMS = {
    "am": "be",
    "are": "be",
    "is": "be",
    "was": "be",
    "were": "be",
    "been": "be",
    "soy": "ser",
    "eres": "ser",
    "es": "ser",
    "somos": "ser",
    "fui": "ser",
    "fueron": "ser",
    "estoy": "estar",
    "estás": "estar",
    "está": "estar",
    "estamos": "estar",
    "estuve": "estar",
}


@dataclass(frozen=True)
class NormalizedWord:
    original: str
    normalized: str
    changed: bool


def clean_token(token: str) -> str:
    return token.strip(".,!?;:()[]{}"'“”‘’").lower()


def normalize_word(token: str) -> NormalizedWord:
    cleaned = clean_token(token)
    normalized = IRREGULAR_FORMS.get(cleaned, cleaned)

    return NormalizedWord(
        original=token,
        normalized=normalized,
        changed=cleaned != normalized,
    )


def group_by_normalized_form(tokens: list[str]) -> dict[str, list[str]]:
    grouped: dict[str, list[str]] = {}

    for token in tokens:
        result = normalize_word(token)
        grouped.setdefault(result.normalized, []).append(result.original)

    return grouped


if __name__ == "__main__":
    words = ["soy", "eres", "estoy", "was", "books"]
    print(group_by_normalized_form(words))
