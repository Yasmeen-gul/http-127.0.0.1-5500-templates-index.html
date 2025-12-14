"""
Unit tests for EmotionDetection.emotion_detector
Run: pytest -q
"""

import pytest
from EmotionDetection.emotion_detector import emotion_predictor

def test_blank_input_returns_400():
    result = emotion_predictor("")
    assert result["status"] == 400
    assert "error" in result

def test_none_input_returns_400():
    result = emotion_predictor(None)
    assert result["status"] == 400
    assert "error" in result

def test_non_string_input_returns_400():
    result = emotion_predictor(123)
    assert result["status"] == 400
    assert "error" in result

def test_valid_input_has_scores_and_dominant():
    text = "I am so happy and delighted today!"
    result = emotion_predictor(text)
    assert result["status"] == 200
    for k in ["anger", "disgust", "fear", "joy", "sadness"]:
        assert k in result
        assert isinstance(result[k], float)
    assert result["dominant_emotion"] in ["anger", "disgust", "fear", "joy", "sadness"]

def test_anger_detection():
    result = emotion_predictor("I am furious and angry about this.")
    assert result["status"] == 200
    assert result["dominant_emotion"] == "anger"

def test_sadness_detection():
    result = emotion_predictor("I feel very sad and heartbroken.")
    assert result["status"] == 200
    assert result["dominant_emotion"] == "sadness"
