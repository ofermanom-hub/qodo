import logging
from collections import Counter
from typing import Any

app_logger = logging.getLogger("tasky")
app_logger.setLevel(logging.INFO)


def find_duplicate_titles(todos: list[dict[str, Any]]) -> list[str]:
    """Return titles that appear more than once."""
    counts = Counter(todo["title"] for todo in todos)
    return [title for title, count in counts.items() if count > 1]
