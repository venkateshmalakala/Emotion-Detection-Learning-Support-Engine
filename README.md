# Emotion Detection & Learning Support Platform

A Streamlit app that turns a learner's free-text study challenge into an emotion-aware, supportive response. It classifies emotions such as Confused, Curious, Frustrated, Bored, and Confident, offers personalized next steps, logs interactions, and shows basic analytics.

## Features
- Emotion detection from free text
- Mixed-emotion analysis and confidence scoring
- Personalized support strategies
- Side-by-side BiLSTM/BERT-style comparison view
- CSV interaction logging
- Streamlit analytics dashboard

## Setup
1. Create and activate a Python environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the local Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```

## Vercel Deployment
The Vercel function entrypoint is `api/index.py`.

## Testing
Run the regression tests with:
```bash
pytest -q
```

## Optional Gemini integration
Set these environment variables to enable Gemini-generated support responses:
```bash
set GEMINI_API_KEY=your_api_key
set GEMINI_MODEL=gemini-1.5-flash
```
