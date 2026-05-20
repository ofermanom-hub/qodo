import sqlite3
from typing import Any


class TodoStore:
    """Tiny SQLite-backed todo store (in-memory for the demo)."""

    def __init__(self) -> None:
        self._conn = sqlite3.connect(":memory:", check_same_thread=False)
        self._conn.execute(
            """
            CREATE TABLE todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                title TEXT NOT NULL,
                done INTEGER NOT NULL DEFAULT 0
            )
            """
        )
        self._conn.commit()

    def create(self, user_id: str, title: str) -> dict[str, Any]:
        cur = self._conn.execute(
            "INSERT INTO todos (user_id, title) VALUES (?, ?)",
            (user_id, title),
        )
        self._conn.commit()
        return {"id": cur.lastrowid, "user_id": user_id, "title": title, "done": False}

    def list_for_user(self, user_id: str) -> list[dict[str, Any]]:
        # PLANTED ISSUE #1: SQL injection via string concatenation.
        # A request like /todos?user_id=' OR '1'='1 leaks every user's todos.
        query = "SELECT id, user_id, title, done FROM todos WHERE user_id = '" + user_id + "'"
        rows = self._conn.execute(query).fetchall()
        return [
            {"id": r[0], "user_id": r[1], "title": r[2], "done": bool(r[3])}
            for r in rows
        ]
