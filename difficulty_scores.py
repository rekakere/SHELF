from datetime import datetime, timezone


def days_since(date_string):
    if not date_string:
        return 0

    last_seen = datetime.fromisoformat(date_string).replace(tzinfo=timezone.utc)
    now = datetime.now(timezone.utc)

    return max((now - last_seen).days, 0)


def calculate_review_priority(
    times_seen,
    times_correct,
    times_wrong,
    last_reviewed=None,
):
    total_answers = times_correct + times_wrong
    error_rate = times_wrong / total_answers if total_answers else 0.5
    recency_gap = days_since(last_reviewed) if last_reviewed else 7

    priority = (
        error_rate * 0.55
        + min(recency_gap / 30, 1) * 0.30
        + (1 / max(times_seen, 1)) * 0.15
    )

    return round(priority, 3)


if __name__ == "__main__":
    score = calculate_review_priority(
        times_seen=3,
        times_correct=1,
        times_wrong=2,
        last_reviewed="2026-05-20T10:00:00",
    )
    print(score)
