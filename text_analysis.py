import re
from collections import Counter


def tokenize(text):
    return re.findall(r"[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]+", text.lower())


def estimate_level(word_count, unique_ratio, avg_word_length):
    if word_count < 40 and avg_word_length < 5:
        return "A1-A2"

    if unique_ratio > 0.65 or avg_word_length > 6:
        return "B2+"

    return "B1"


def analyze_text(text):
    words = tokenize(text)

    if not words:
        return {
            "word_count": 0,
            "unique_words": 0,
            "unique_ratio": 0,
            "avg_word_length": 0,
            "estimated_level": "unknown",
        }

    counts = Counter(words)
    word_count = len(words)
    unique_words = len(counts)
    unique_ratio = unique_words / word_count
    avg_word_length = sum(len(word) for word in words) / word_count

    return {
        "word_count": word_count,
        "unique_words": unique_words,
        "unique_ratio": round(unique_ratio, 3),
        "avg_word_length": round(avg_word_length, 2),
        "estimated_level": estimate_level(word_count, unique_ratio, avg_word_length),
    }


if __name__ == "__main__":
    sample = "Estoy aprendiendo español porque quiero leer textos más difíciles."
    print(analyze_text(sample))
