from flask import Flask, jsonify, request

from db import TodoStore
from utils import app_logger

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


if __name__ == "__main__":
    app.run(debug=True)
