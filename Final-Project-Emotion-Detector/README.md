# Emotion Detector (Final Project)

A minimal, self-contained emotion detection web application:
- Packaged as `EmotionDetection` with `emotion_predictor`.
- Flask web deployment with error handling.
- Unit tests via pytest.
- Clean code for static analysis.

## Quickstart

```bash
python -m venv .venv
# Windows (PowerShell)
. .venv/Scripts/Activate.ps1
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt

# Run tests
pytest -q

# Run server
python server.py
# Open http://localhost:5000
