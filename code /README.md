# 🧠 Emotion Detection & Learning Support Engine

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat&logo=vercel&logoColor=white)](https://vercel.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An intelligent, emotion-aware learning support system that transforms student free-text study challenges into personalized, empathetic pedagogical guidance. By detecting core affective states, the platform delivers tailored learning strategies to optimize student engagement and academic outcomes.

---

## 📌 Project Overview

### Problem Statement
When students face obstacles during self-paced or online learning, their emotional states heavily influence their cognitive capacity to process information. Traditional Learning Management Systems (LMS) treat text inputs statically but fail to account for the student's affective state (such as frustration, boredom, or confusion). Without immediate, emotionally grounded intervention, learners are highly prone to disengagement, academic burnout, or complete abandonment of the learning material.

### Solution
The **Emotion Detection & Learning Support Platform** serves as an empathetic middleware. It accepts natural-language study challenges written by users, classifies their core emotional states—specifically **Confused, Curious, Frustrated, Bored, and Confident**—and maps these metrics to responsive support strategies. Featuring mixed-emotion profiling and a side-by-side comparative architectural view (BiLSTM vs. BERT-style modeling), it equips educators and platforms with deep insights into learner psychology while logging behavioral metrics for administrative overview.

---

## ✨ Key Features

*   **Affective Classification Engine:** Evaluates free-text inputs for 5 pivotal emotional states: *Confused, Curious, Frustrated, Bored, and Confident*.
*   **Mixed-Emotion Analytics:** Provides granular confidence scoring alongside multi-faceted emotion distribution metrics.
*   **Tailored Pedagogical Strategies:** Outputs dynamic guidance based on the predominant emotional profile detected.
*   **Model Comparison Matrix:** Displays side-by-side inference analytics tracking performance profiles (BiLSTM vs. BERT architectural constructs).
*   **Operational Logs:** Automatically records user sessions, classifications, and responses into local CSV files for auditable training or behavior reviews.
*   **Analytics Dashboard:** Embedded visual metrics tracking aggregated interaction trends and frequent blocker states over time.
*   **Hybrid Deployment Matrix:** Ready-to-go architecture matching local Streamlit dashboard executions with serverless microservice hosting on Vercel.

---

## 🖼️ Media & Previews

### Dashboard Preview

+-----------------------------------------------------------------+
|  🧠 EMOTION DETECTION & LEARNING SUPPORT ENGINE                 |
+-----------------------------------------------------------------+
|                                                                 |
|  [ Enter your study challenge...                             ]  |
|  "I've been trying to understand recursion for hours and I'm    |
|   about to give up. Nothing makes sense anymore."               |
|                                                                 |
|  +---------------------------+   +----------------------------+ |
|  | DETECTED EMOTION          |   | RECOMMENDED STRATEGY       | |
|  | > FRUSTRATED (84%)        |   | > Break the task into tiny | |
|  | > CONFUSED (12%)          |   |   sub-goals. Take a 5-min  | |
|  |                           |   |   breather.                | |
|  +---------------------------+   +----------------------------+ |
|                                                                 |
|  📊 Model Architect Comparison                                  |
|  +---------------------------+--------------------------------+ |
|  | BiLSTM Confidence: 82.1%  | BERT-Style Confidence: 85.4%   | |
|  +---------------------------+--------------------------------+ |
+-----------------------------------------------------------------+
