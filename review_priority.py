from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class ReviewHistory:
    times_seen: int = 0
    times_correct: int = 0
    times_wrong: int = 0
    personal_difficulty: int = 3
    last_reviewed_at: str | None = None


@dataclass(frozen=True)
class ReviewScore:
    priority: float
    error_rate: float
    recency_weight: float
    familiarity_weight: float


def parse_utc_datetime(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return parsed.astimezone(timezone.utc)


def days_since(value: str | None) -> int:
    if not value:
        return 14

    reviewed_at = parse_utc_datetime(value)
    now = datetime.now(timezone.utc)

    return max((now - reviewed_at).days, 0)


def calculate_review_priority(history: ReviewHistory) -> ReviewScore:
    total_answers = history.times_correct + history.times_wrong

    error_rate = (
        history.times_wrong / total_answers
        if total_answers > 0
        else 0.5
    )

    recency_weight = min(days_since(history.last_reviewed_at) / 30, 1)
    familiarity_weight = 1 / max(history.times_seen, 1)
    difficulty_weight = min(max(history.personal_difficulty, 1), 5) / 5

    priority = (
        error_rate * 0.40
        + recency_weight * 0.25
        + familiarity_weight * 0.20
        + difficulty_weight * 0.15
    )

    return ReviewScore(
        priority=round(priority, 3),
        error_rate=round(error_rate, 3),
        recency_weight=round(recency_weight, 3),
        familiarity_weight=round(familiarity_weight, 3),
    )


if __name__ == "__main__":
    item = ReviewHistory(
        times_seen=4,
        times_correct=2,
        times_wrong=2,
        personal_difficulty=4,
        last_reviewed_at="2026-05-20T10:00:00Z",
    )

    print(calculate_review_priority(item))
