"""
Flask web deployment for the Emotion Detection application.
Includes error handling for blank input (returns 400) and clean JSON responses.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_predictor

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    # Home page with a simple form
    return render_template("index.html")

@app.route("/detect-emotion", methods=["POST"])
def detect_emotion():
    """
    POST endpoint: expects JSON {"text": "..."} or form data 'text'.
    Returns JSON with emotion scores and dominant_emotion.
    Blank input triggers status 400 with descriptive error.
    """
    text = None

    # Accept JSON
    if request.is_json:
        payload = request.get_json(silent=True) or {}
        text = payload.get("text")

    # Accept form fallback
    if text is None:
        text = request.form.get("text")

    result = emotion_predictor(text)

    if result.get("status") == 400:
        return jsonify(result), 400

    return jsonify(result), 200

if __name__ == "__main__":
    # Run local server
    app.run(host="0.0.0.0", port=5000, debug=True)
