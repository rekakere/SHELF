IRREGULAR_FORMS = {
    "am": "be",
    "are": "be",
    "is": "be",
    "was": "be",
    "were": "be",
    "soy": "ser",
    "eres": "ser",
    "es": "ser",
    "fui": "ser",
    "estoy": "estar",
    "estás": "estar",
    "está": "estar",
}


def normalize_word(word):
    cleaned = word.strip().lower()
    return IRREGULAR_FORMS.get(cleaned, cleaned)


def group_related_words(words):
    groups = {}

    for word in words:
        root = normalize_word(word)
        groups.setdefault(root, []).append(word)

    return groups


if __name__ == "__main__":
    sample_words = ["soy", "eres", "estoy", "was", "book"]
    print(group_related_words(sample_words))
