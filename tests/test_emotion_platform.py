from src.emotion_platform import (
    classify_text,
    generate_support_response,
    get_model_comparison,
)


def test_classify_text_detects_confusion_and_curiosity():
    result = classify_text("I am confused about recursion and curious about how it works")

    assert result["primary_emotion"] == "Confused"
    assert "Curious" in result["mixed_emotions"]
    assert result["confidence"] >= 0.5


def test_generate_support_response_includes_next_steps():
    response = generate_support_response(
        "I am frustrated because my code keeps failing",
        {"primary_emotion": "Frustrated", "mixed_emotions": []},
    )

    assert "next steps" in response.lower()
    assert "encouragement" in response.lower() or "support" in response.lower()


def test_model_comparison_returns_both_models():
    comparison = get_model_comparison("I feel bored and need motivation")

    assert "BiLSTM" in comparison
    assert "BERT" in comparison
    assert comparison["BiLSTM"]["primary_emotion"] == "Bored"
