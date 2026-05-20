from flask import Flask, jsonify, request

from db import TodoStore
from external import fetch_weather_hint
from utils import find_duplicate_titles, app_logger

app = Flask(__name__)
store = TodoStore()


@app.route("/health")
def health():
    return jsonify({"ok": True})


@app.route("/todos", methods=["GET"])
def list_todos():
    user_id = request.args.get("user_id", "")
    app_logger.info("listing todos for user_id=%s", user_id)
    return jsonify(store.list_for_user(user_id))


@app.route("/todos", methods=["POST"])
def create_todo():
    payload = request.get_json(force=True)
    todo = store.create(
        user_id=payload["user_id"],
        title=payload["title"],
    )
    return jsonify(todo), 201


@app.route("/todos/suggest", methods=["GET"])
def suggest_todo():
    city = request.args.get("city", "SF")
    hint = fetch_weather_hint(city)
    suggestion = hint["summary"] + " — remember to plan accordingly."
    return jsonify({"suggestion": suggestion})


@app.route("/todos/duplicates", methods=["GET"])
def duplicate_titles():
    user_id = request.args.get("user_id", "")
    todos = store.list_for_user(user_id)
    dupes = find_duplicate_titles(todos)
    print(f"found {len(dupes)} duplicate titles for {user_id}")
    return jsonify({"duplicates": dupes})


if __name__ == "__main__":
    app.run(debug=True)
