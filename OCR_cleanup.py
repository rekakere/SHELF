import re


def remove_page_numbers(text):
    lines = text.splitlines()
    cleaned = []

    for line in lines:
        stripped = line.strip()

        if re.fullmatch(r"\d+", stripped):
            continue

        cleaned.append(line)

    return "\n".join(cleaned)


def normalize_spacing(text):
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def clean_ocr_text(text):
    text = remove_page_numbers(text)
    text = normalize_spacing(text)
    return text


if __name__ == "__main__":
    sample = """1

    Este es un texto escaneado.

    2
    Tiene espacios raros.
    """

    print(clean_ocr_text(sample))
