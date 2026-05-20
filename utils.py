import logging
from typing import Any

app_logger = logging.getLogger("tasky")
app_logger.setLevel(logging.INFO)


def find_duplicate_titles(todos: list[dict[str, Any]]) -> list[str]:
    """Return titles that appear more than once.

    PLANTED ISSUE #4: This is an O(n^2) scan. A dict/Counter pass is O(n).
    """
    duplicates: list[str] = []
    for i, a in enumerate(todos):
        for j, b in enumerate(todos):
            if i >= j:
                continue
            if a["title"] == b["title"] and a["title"] not in duplicates:
                duplicates.append(a["title"])
    return duplicates
