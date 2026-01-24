from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    api_key = request.headers.get("x-api-key")
    if api_key != "MY_SECRET_STUDENT_KEY":
        return jsonify({"error": "Invalid API key"}), 401

    data = request.get_json()
    message = data.get("message", "").lower()

    scam_type = "Safe"
    if "lottery" in message or "won" in message or "prize" in message:
        scam_type = "Lottery Scam"
    elif "bank" in message or "password" in message:
        scam_type = "Phishing"

    links = [word for word in message.split() if word.startswith("http")]

    risk_score = 0.9 if scam_type != "Safe" else 0.1

    return jsonify({
        "scam_type": scam_type,
        "suspicious_links": links,
        "risk_score": risk_score
    })

app.run(host="0.0.0.0", port=3000)
