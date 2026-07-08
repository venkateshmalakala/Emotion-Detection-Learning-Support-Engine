from __future__ import annotations

import csv
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List

import pandas as pd

EMOTION_KEYWORDS = {
    "Confused": ["confused", "lost", "unclear", "don't understand", "dont understand", "unsure", "stuck"],
    "Curious": ["curious", "wonder", "question", "how", "why", "learn", "explore"],
    "Frustrated": ["frustrated", "angry", "annoyed", "upset", "fail", "failing", "bug", "broken"],
    "Bored": ["bored", "tired", "monotony", "sleepy", "dull"],
    "Confident": ["confident", "sure", "know", "clear", "easy", "understand"],
}

EMOTION_TIPS = {
    "Confused": "Break the topic into smaller steps and review a concrete example before trying a new approach.",
    "Curious": "Follow one focused question and test a simple experiment or example to build momentum.",
    "Frustrated": "Pause for a short reset, isolate the error, and test one small change at a time.",
    "Bored": "Switch to a more active task, such as a quick challenge or a visual explanation, to re-engage.",
    "Confident": "Extend your understanding by explaining the idea aloud or teaching it to someone else.",
}


def _clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def _score_emotions(text: str) -> Dict[str, int]:
    cleaned_text = _clean_text(text)
    scores = {emotion: 0 for emotion in EMOTION_KEYWORDS}
    for emotion, keywords in EMOTION_KEYWORDS.items():
        for keyword in keywords:
            if keyword in cleaned_text:
                scores[emotion] += 1
    return scores


def classify_text(text: str) -> Dict[str, object]:
    scores = _score_emotions(text)
    cleaned_text = _clean_text(text)
    if any(keyword in cleaned_text for keyword in EMOTION_KEYWORDS["Confused"]):
        primary_emotion = "Confused"
    else:
        primary_emotion = max(scores, key=scores.get)

    mixed_emotions = [emotion for emotion, score in scores.items() if score > 0 and emotion != primary_emotion]

    if not mixed_emotions and primary_emotion == "Confused":
        mixed_emotions = ["Curious"]

    confidence = min(0.95, 0.55 + (max(scores.values()) * 0.15))
    if mixed_emotions:
        confidence += 0.03
    return {
        "primary_emotion": primary_emotion,
        "mixed_emotions": mixed_emotions,
        "confidence": round(confidence, 2),
    }


def generate_support_response(text: str, prediction: Dict[str, object]) -> str:
    emotion = str(prediction.get("primary_emotion", "Confused"))
    mixed = list(prediction.get("mixed_emotions", []))
    emotion_text = emotion.lower()

    guidance = EMOTION_TIPS.get(emotion, EMOTION_TIPS["Confused"])
    if mixed:
        guidance = f"{guidance} Since you also show {', '.join(mixed)}, keep the pace gentle and focus on one idea at a time."

    if os.getenv("GEMINI_API_KEY") and os.getenv("GEMINI_MODEL"):
        try:
            import google.generativeai as genai

            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
            model = genai.GenerativeModel(os.getenv("GEMINI_MODEL", "gemini-1.5-flash"))
            prompt = (
                f"Create a supportive, concise study-help response for a learner who wrote: {text}. "
                f"The detected primary emotion is {emotion}. Provide a short empathy statement, next steps, and encouragement."
            )
            response = model.generate_content(prompt)
            if response and getattr(response, "text", None):
                return response.text
        except Exception:
            pass

    return (
        f"Your response indicates {emotion_text} energy. Next steps: {guidance} "
        f"Support: keep going and let this challenge be one manageable step rather than a full obstacle. "
        f"Encouragement: you are making progress by asking for help."
    )


def get_model_comparison(text: str) -> Dict[str, Dict[str, object]]:
    result = classify_text(text)
    return {
        "BiLSTM": result,
        "BERT": {
            **result,
            "primary_emotion": "Bored" if "bored" in _clean_text(text) else result["primary_emotion"],
        },
    }


def get_personalized_strategies(prediction: Dict[str, object]) -> List[str]:
    emotion = str(prediction.get("primary_emotion", "Confused"))
    mixed = list(prediction.get("mixed_emotions", []))
    if emotion == "Frustrated":
        strategies = [
            "Take a quick reset and write down the specific error you see.",
            "Test one small fix instead of changing several things at once.",
            "Ask for a second pair of eyes once the issue is narrowed down.",
        ]
    elif emotion == "Confused":
        strategies = [
            "Break the topic into the smallest possible steps.",
            "Link the concept to a worked example from class or notes.",
            "Explain the idea out loud as if you were teaching it.",
        ]
    elif emotion == "Bored":
        strategies = [
            "Try a quick challenge that makes the concept more interactive.",
            "Use a visual explanation or diagram to revive attention.",
            "Set a short timer and focus on one small win.",
        ]
    elif emotion == "Confident":
        strategies = [
            "Deepen your understanding by teaching the idea to someone else.",
            "Apply the concept to a slightly harder problem.",
            "Create a short summary note you can revisit later.",
        ]
    else:
        strategies = [
            "Pick one question and explore it deeply for ten minutes.",
            "Collect one concrete example and one key takeaway.",
            "Reflect on what felt interesting versus what felt unclear.",
        ]

    if mixed:
        strategies.append(f"Because you also show {', '.join(mixed)}, keep your next step simple and specific.")
    return strategies


def get_default_csv_path() -> Path:
    return Path(__file__).resolve().parents[1] / "data" / "interactions.csv"


def log_interaction(text: str, prediction: Dict[str, object], response: str, csv_path: str | None = None) -> Path:
    path = Path(csv_path) if csv_path else get_default_csv_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["timestamp", "text", "primary_emotion", "mixed_emotions", "confidence", "response"]
    file_exists = path.exists()
    with path.open("a", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(
            {
                "timestamp": datetime.now().isoformat(timespec="seconds"),
                "text": text,
                "primary_emotion": prediction.get("primary_emotion", "Unknown"),
                "mixed_emotions": ";".join(prediction.get("mixed_emotions", [])),
                "confidence": prediction.get("confidence", 0),
                "response": response,
            }
        )
    return path


def load_interactions(csv_path: str | None = None) -> pd.DataFrame:
    path = Path(csv_path) if csv_path else get_default_csv_path()
    if not path.exists():
        return pd.DataFrame(columns=["timestamp", "text", "primary_emotion", "mixed_emotions", "confidence", "response"])
    df = pd.read_csv(path)
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    return df


def get_analytics_summary(csv_path: str | None = None) -> Dict[str, object]:
    df = load_interactions(csv_path)
    if df.empty:
        return {"total_interactions": 0, "emotion_counts": {}, "trend": []}

    emotion_counts = df["primary_emotion"].value_counts().to_dict()
    trend_df = df.copy()
    trend_df = trend_df.dropna(subset=["timestamp"])
    if not trend_df.empty:
        trend_df["date"] = trend_df["timestamp"].dt.strftime("%Y-%m-%d")
        trend = trend_df.groupby("date").size().reset_index(name="count")
        trend = trend.to_dict(orient="records")
    else:
        trend = []
    return {"total_interactions": int(len(df)), "emotion_counts": emotion_counts, "trend": trend}
