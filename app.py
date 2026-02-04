
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

API_KEY = os.environ.get("API_KEY", "MY_SECRET_STUDENT_KEY")

@app.route("/analyze", methods=["POST"])
def analyze():
    provided_key = request.headers.get("x-api-key")

    if provided_key != API_KEY:
        return jsonify({
            "status": "error",
            "message": "Invalid API key"
        }), 401

    return jsonify({
        "status": "success",
        "reply": "Why is my account being suspended?"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
