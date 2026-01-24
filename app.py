from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Home page (just to check server is alive)
@app.route("/", methods=["GET"])
def home():
    return "Agentic Honeypot is running", 200


# Honeypot API endpoint
@app.route("/analyze", methods=["GET", "POST"])
def analyze():
    api_key = request.headers.get("x-api-key")

    # API key check
    if api_key != os.environ.get("API_KEY"):
        return jsonify({
            "status": "error",
            "message": "Unauthorized"
        }), 401

    # If API key is correct
    return jsonify({
        "status": "ok",
        "message": "Honeypot active"
    }), 200


# Needed for Render deployment
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
