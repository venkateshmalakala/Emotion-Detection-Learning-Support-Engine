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
      :root {
        color-scheme: light;
        font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      }
      * {
        box-sizing: border-box;
      }
      body {
        margin: 0;
        background: linear-gradient(135deg, #eef2ff 0%, #fdf2f8 45%, #ffffff 100%);
        color: #0f172a;
      }
      .page {
        min-height: 100vh;
        padding: 2rem;
      }
      .layout {
        max-width: 1180px;
        margin: 0 auto;
      }
      .hero {
        display: grid;
        gap: 1.5rem;
        padding: 2.4rem;
        background: rgba(255,255,255,0.94);
        border-radius: 32px;
        box-shadow: 0 24px 80px rgba(15, 23, 42, 0.08);
      }
      .hero h1 {
        margin: 0;
        font-size: clamp(2.8rem, 3.5vw, 4.4rem);
        line-height: 1.02;
      }
      .hero p {
        margin: 1rem 0 0;
        max-width: 760px;
        font-size: 1.05rem;
        color: #475569;
      }
      .grid {
        display: grid;
        gap: 1.5rem;
        grid-template-columns: 2fr 1fr;
        margin-top: 1.8rem;
      }
      .card {
        background: rgba(255, 255, 255, 0.96);
        border-radius: 28px;
        padding: 1.8rem;
        border: 1px solid rgba(148, 163, 184, 0.16);
        box-shadow: 0 24px 50px rgba(15, 23, 42, 0.08);
      }
      .card h2 {
        margin-top: 0;
        font-size: 1.35rem;
        color: #1e293b;
      }
      .hero .metrics {
        display: flex;
        gap: 1rem;
        flex-wrap: wrap;
        margin-top: 1.5rem;
      }
      .metric {
        min-width: 170px;
        background: #eef2ff;
        border-radius: 18px;
        padding: 1rem 1.1rem;
        color: #3730a3;
        font-weight: 700;
      }
      textarea {
        width: 100%;
        min-height: 200px;
        border-radius: 22px;
        border: 1px solid rgba(148, 163, 184, 0.24);
        padding: 1rem;
        font-size: 1rem;
        resize: vertical;
      }
      button {
        background: #4338ca;
        color: white;
        border: none;
        border-radius: 16px;
        padding: 1rem 1.8rem;
        font-size: 1rem;
        cursor: pointer;
        transition: transform 0.24s ease, box-shadow 0.24s ease;
      }
      button:hover {
        transform: translateY(-2px);
        box-shadow: 0 18px 40px rgba(67, 56, 202, 0.24);
      }
      .badges {
        display: flex;
        flex-wrap: wrap;
        gap: 0.6rem;
        margin-top: 1rem;
      }
      .badge {
        padding: 0.6rem 1rem;
        border-radius: 999px;
        background: #eef2ff;
        color: #3730a3;
        font-weight: 700;
      }
      .highlight {
        color: #4338ca;
        font-weight: 700;
      }
      .subtle {
        color: #64748b;
      }
      ul {
        padding-left: 1.25rem;
      }
      li {
        margin-bottom: 0.6rem;
      }
      .footer {
        margin-top: 2rem;
        text-align: center;
        color: #64748b;
      }
      @media (max-width: 920px) {
        .grid { grid-template-columns: 1fr; }
      }
    </style>
  </head>
  <body>
    <div class="page">
      <div class="layout">
        <section class="hero">
          <div>
            <p class="highlight">Empathy-first learner support</p>
            <h1>Emotion-aware guidance for every study challenge.</h1>
            <p>Instantly identify how a learner feels, deliver supportive next steps, and keep responses professional, consistent, and easy to read.</p>
            <div class="metrics">
              <div class="metric">Mixed-emotion detection</div>
              <div class="metric">Model comparison</div>
              <div class="metric">Real-time suggestions</div>
            </div>
          </div>
        </section>

        <form method="post" action="/analyze">
          <div class="card">
            <h2>Enter the learner’s challenge</h2>
            <textarea name="text" placeholder="I’m stuck on recursion and feel confused..."></textarea>
            <div style="margin-top: 1.25rem;"><button type="submit">Analyze emotions</button></div>
          </div>
        </form>

        {% if prediction %}
        <div class="grid">
          <div class="card">
            <h2>Detected emotion</h2>
            <p><strong>Primary emotion:</strong> {{ prediction.primary_emotion }}</p>
            <p><strong>Mixed emotions:</strong> {{ prediction.mixed_emotions or 'None' }}</p>
            <p><strong>Confidence:</strong> {{ prediction.confidence }}</p>
          </div>
          <div class="card">
            <h2>Model comparison</h2>
            <div class="badges">
              <span class="badge">BiLSTM: {{ comparison.BiLSTM.primary_emotion }}</span>
              <span class="badge">BERT: {{ comparison.BERT.primary_emotion }}</span>
            </div>
            <p class="subtle">Use the comparison to verify consistency across emotional predictions.</p>
          </div>
          <div class="card">
            <h2>Support response</h2>
            <p>{{ response }}</p>
          </div>
          <div class="card">
            <h2>Personalized strategies</h2>
            <ul>
              {% for item in strategies %}
              <li>{{ item }}</li>
              {% endfor %}
            </ul>
          </div>
        </div>
        {% endif %}

        <div class="footer">
          Built for educators, support teams, and self-directed learners who need emotional clarity and fast next steps.
        </div>
      </div>
    </div>
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
