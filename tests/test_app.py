import pytest

from app import app, store


@pytest.fixture()
def client():
    app.config.update(TESTING=True)
    with app.test_client() as c:
        yield c


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"ok": True}


def test_create_and_list(client):
    resp = client.post("/todos", json={"user_id": "alice", "title": "ship demo"})
    assert resp.status_code == 201

    resp = client.get("/todos?user_id=alice")
    assert resp.status_code == 200
    titles = [t["title"] for t in resp.get_json()]
    assert "ship demo" in titles


# PLANTED ISSUE #3: /todos/duplicates and /todos/suggest have no test coverage.
# Qodo should flag the gap and offer to generate tests for them.
