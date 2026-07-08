from flask import Flask, jsonify, render_template_string, request

from src.emotion_platform import (
    classify_text,
    generate_support_response,
    get_model_comparison,
    get_personalized_strategies,
)

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Emotion Learning Support</title>
    <style>
      body { font-family: Arial, sans-serif; margin: 2rem; }
      textarea { width: 100%; height: 140px; margin-bottom: 1rem; }
      button { padding: 0.75rem 1.2rem; font-size: 1rem; }
      .box { border: 1px solid #ddd; padding: 1rem; margin-top: 1rem; border-radius: 8px; }
      .badge { display: inline-block; padding: 0.35rem 0.75rem; margin-right: 0.3rem; margin-bottom: 0.3rem; border-radius: 999px; background: #f1f5f9; }
    </style>
  </head>
  <body>
    <h1>Emotion Learning Support</h1>
    <p>Describe your study challenge and receive an emotion-aware response with practical guidance.</p>
    <form method="post" action="/analyze">
      <textarea name="text" placeholder="I’m stuck on recursion and feel confused..."></textarea>
      <button type="submit">Analyze</button>
    </form>
    {% if prediction %}
    <div class="box">
      <h2>Detected Emotion</h2>
      <p><strong>Primary emotion:</strong> {{ prediction.primary_emotion }}</p>
      <p><strong>Mixed emotions:</strong> {{ prediction.mixed_emotions or 'None' }}</p>
      <p><strong>Confidence:</strong> {{ prediction.confidence }}</p>
    </div>
    <div class="box">
      <h2>Support Response</h2>
      <p>{{ response }}</p>
    </div>
    <div class="box">
      <h2>Personalized Strategies</h2>
      <ul>
        {% for item in strategies %}<li>{{ item }}</li>{% endfor %}
      </ul>
    </div>
    <div class="box">
      <h2>Model Comparison</h2>
      <p><span class="badge">BiLSTM: {{ comparison.BiLSTM.primary_emotion }}</span>
      <span class="badge">BERT: {{ comparison.BERT.primary_emotion }}</span></p>
    </div>
    {% endif %}
  </body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(HTML_TEMPLATE, prediction=None)

@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.form.get("text", "").strip()
    if not text:
        return render_template_string(HTML_TEMPLATE, prediction=None)

    prediction = classify_text(text)
    response = generate_support_response(text, prediction)
    comparison = get_model_comparison(text)
    strategies = get_personalized_strategies(prediction)

    return render_template_string(
        HTML_TEMPLATE,
        prediction=prediction,
        response=response,
        comparison=comparison,
        strategies=strategies,
    )

@app.route("/api/analyze", methods=["POST"])
def api_analyze():
    data = request.get_json(force=True, silent=True) or {}
    text = data.get("text", "").strip()
    prediction = classify_text(text)
    response = generate_support_response(text, prediction)
    comparison = get_model_comparison(text)
    strategies = get_personalized_strategies(prediction)
    return jsonify(
        text=text,
        prediction=prediction,
        response=response,
        comparison=comparison,
        strategies=strategies,
    )
