import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# The tester sends a POST request to this specific path
@app.route('/analyze', methods=['POST'])
def analyze_honeypot():
    # 1. Fetch the secret key from your Render environment
    # Use 'x-api-key' as the key name to match the tester's header
    expected_key = os.environ.get('x-api-key', 'MY_SECRET_STUDENT_KEY')
    
    # 2. Get the key the tester is sending in the 'x-api-key' header
    provided_key = request.headers.get('x-api-key')

    # 3. Validation Logic
    if provided_key == expected_key:
        return jsonify({
            "status": "success",
            "message": "Honeypot is active and authorized.",
            "data": request.json # Captures any data the tester sends
        }), 200
    else:
        # If the key doesn't match, return 401 Unauthorized
        return jsonify({"status": "error", "message": "Unauthorized"}), 401

if __name__ == '__main__':
    # Render requires binding to 0.0.0.0 and port 10000 by default
    app.run(host='0.0.0.0', port=10000)
