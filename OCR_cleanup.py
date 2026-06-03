from __future__ import annotations

import re


PAGE_NUMBER_PATTERN = re.compile(r"^\s*\d+\s*$")
BROKEN_HYPHEN_PATTERN = re.compile(r"(\w)-\n(\w)")
EXTRA_SPACES_PATTERN = re.compile(r"[ \t]+")


def remove_standalone_page_numbers(text: str) -> str:
    lines = []

    for line in text.splitlines():
        if PAGE_NUMBER_PATTERN.fullmatch(line):
            continue

        lines.append(line)

    return "\n".join(lines)


def repair_hyphenated_line_breaks(text: str) -> str:
    return BROKEN_HYPHEN_PATTERN.sub(r"\1\2", text)


def normalize_whitespace(text: str) -> str:
    text = EXTRA_SPACES_PATTERN.sub(" ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def join_soft_line_breaks(text: str) -> str:
    lines = [line.strip() for line in text.splitlines()]
    paragraphs: list[str] = []
    current: list[str] = []

    for line in lines:
        if not line:
            if current:
                paragraphs.append(" ".join(current))
                current = []
            continue

        current.append(line)

    if current:
        paragraphs.append(" ".join(current))

    return "\n\n".join(paragraphs)


def clean_ocr_text(text: str) -> str:
    text = remove_standalone_page_numbers(text)
    text = repair_hyphenated_line_breaks(text)
    text = normalize_whitespace(text)
    text = join_soft_line_breaks(text)

    return text


if __name__ == "__main__":
    sample = """
    1

    Este texto fue escanea-
    do desde una página.

    2

    Tiene algunos saltos raros.
    """

    print(clean_ocr_text(sample))
