import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# ✅ Health check (MANDATORY)
@app.route('/', methods=['GET'])
def health():
    return jsonify({"status": "alive"}), 200


# ✅ Main honeypot endpoint
@app.route('/analyze', methods=['POST'])
def analyze_honeypot():
    # Read API key from Render environment
    expected_key = os.environ.get('API_KEY', 'MY_SECRET_STUDENT_KEY')
    provided_key = request.headers.get('x-api-key')

    if provided_key != expected_key:
        return jsonify({
            "status": "error",
            "message": "Unauthorized"
        }), 401

    data = request.json or {}
    message = data.get("message", {}).get("text", "")

    # 🔹 Simple scam-engagement reply (baseline)
    reply_text = "Why is my account being suspended?"

    return jsonify({
        "status": "success",
        "reply": reply_text
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
