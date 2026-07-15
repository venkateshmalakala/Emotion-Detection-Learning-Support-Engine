# 🧠 Emotion Detection & Learning Support Engine

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat&logo=vercel&logoColor=white)](https://vercel.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An intelligent, emotion-aware learning support system that transforms student free-text study challenges into personalized, empathetic pedagogical guidance. By detecting core affective states, the platform delivers tailored learning strategies to optimize student engagement and academic outcomes.

### 🚀 [**Live Demo →**](https://share.google/3OOGtIsIbL6wJCILG)

---

## Table of Contents

- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Media & Previews](#️-media--previews)
- [Technology Stack](#️-technology-stack)
- [System Architecture](#️-system-architecture)
- [Folder Structure](#-folder-structure)
- [Installation & Setup](#-installation--setup)
- [Configuration & Environment Variables](#️-configuration--environment-variables)
- [Execution Guide](#-execution-guide)
- [Testing Protocol](#-testing-protocol)
- [Example Usage](#-example-usage)
- [Assumptions & Limitations](#-assumptions--limitations)
- [Contributors](#-contributors)
- [License](#-license)

---

## 📌 Project Overview

### Problem Statement

When students face obstacles during self-paced or online learning, their emotional state heavily influences their cognitive capacity to process information. Traditional Learning Management Systems (LMS) treat text inputs statically and fail to account for a student's affective state — such as frustration, boredom, or confusion. Without immediate, emotionally grounded intervention, learners are highly prone to disengagement, academic burnout, or complete abandonment of the learning material.

### Solution

The **Emotion Detection & Learning Support Platform** serves as an empathetic middleware layer. It accepts natural-language study challenges written by users, classifies their core emotional state — specifically **Confused, Curious, Frustrated, Bored, and Confident** — and maps these signals to responsive support strategies. With mixed-emotion profiling and a side-by-side comparative architectural view (BiLSTM vs. BERT-style modeling), it gives educators and platforms deep insight into learner psychology while logging behavioral metrics for administrative review.

---

## ✨ Key Features

| Feature | Description |
| :--- | :--- |
| **Affective Classification Engine** | Evaluates free-text input across 5 core emotional states: *Confused, Curious, Frustrated, Bored,* and *Confident*. |
| **Mixed-Emotion Analytics** | Provides granular confidence scoring alongside multi-faceted emotion distribution metrics. |
| **Tailored Pedagogical Strategies** | Outputs dynamic guidance based on the predominant emotional profile detected. |
| **Model Comparison Matrix** | Displays side-by-side inference analytics tracking performance profiles (BiLSTM vs. BERT-style). |
| **Operational Logs** | Automatically records user sessions, classifications, and responses into local CSV files for auditable review. |
| **Analytics Dashboard** | Embedded visual metrics tracking aggregated interaction trends and frequent blocker states over time. |
| **Hybrid Deployment** | Ready-to-go architecture supporting both local Streamlit dashboard execution and serverless hosting on Vercel. |

---

## 🖼️ Media & Previews

### Dashboard Preview

```
+-------------------------------------------------------------------+
|  🧠 EMOTION DETECTION & LEARNING SUPPORT ENGINE                   |
+-------------------------------------------------------------------+
|                                                                   |
|  [ Enter your study challenge...                               ]  |
|  "I've been trying to understand recursion for hours and I'm      |
|   about to give up. Nothing makes sense anymore."                 |
|                                                                   |
|  +---------------------------+   +----------------------------+   |
|  | DETECTED EMOTION          |   | RECOMMENDED STRATEGY        |  |
|  | > FRUSTRATED (84%)        |   | > Break the task into tiny  |  |
|  | > CONFUSED (12%)          |   |   sub-goals. Take a 5-min   |  |
|  |                           |   |   breather.                 |  |
|  +---------------------------+   +----------------------------+   |
|                                                                   |
|  📊 Model Architecture Comparison                                 |
|  +---------------------------+---------------------------------+  |
|  | BiLSTM Confidence: 82.1%  | BERT-Style Confidence: 85.4%    |  |
|  +---------------------------+---------------------------------+  |
+-------------------------------------------------------------------+
```

### System Walkthrough

A walkthrough video demonstrating the live application is available in the repository root:
[`Emotion detection system.mp4`](./Emotion%20detection%20system.mp4)

---

## 🛠️ Technology Stack

| Category | Technology / Library | Usage |
| :--- | :--- | :--- |
| **Frontend UI** | Streamlit | Analytical dashboard interface and interactive text playground |
| **API Deployment** | Vercel / WSGI | Serverless production host wrapper (`api/index.py`) |
| **Data Orchestration** | Pandas | Data interfacing, structured metric calculation, and log mutations |
| **Testing** | Pytest | Automated regression suites and validation checks |
| **LLM Integration** *(optional)* | Gemini Flash API | Generative orchestration for fluid, hyper-personalized support prompts |

---

## 🏗️ System Architecture

```
                     [ User Text Input: Study Challenge ]
                                    │
                                    ▼
                       [ Core Processing Layer ]
              ┌─────────────────────┴─────────────────────┐
              ▼                                            ▼
    [ Model Architecture A ]                    [ Model Architecture B ]
          (BiLSTM)                                    (BERT-Style)
              │                                            │
              └─────────────────────┬─────────────────────┘
                                    ▼
                       [ Combined Emotion Scoring ]
              (Confused / Frustrated / Bored / Curious / Confident)
                                    │
                                    ▼
                    [ Pedagogical Strategy Router ]
              ┌─────────────────────┴─────────────────────┐
              ▼                                            ▼
    [ Local Policy Mapping ]                     [ LLM Gen-AI Pipeline ]
    (Static Strategy Framework)                  (Gemini 1.5 Flash Engine)
              │                                            │
              └─────────────────────┬─────────────────────┘
                                    ▼
                     [ Final Supportive Output UI ]
                                    │
              ┌─────────────────────┴─────────────────────┐
              ▼                                            ▼
    [ Local CSV Data Logging ]                  [ Historical Analytics ]
```

---

## 📂 Folder Structure

```
code/
├── .gitignore               # System, cache, and log exclusion definitions
├── README.md                # Comprehensive documentation
├── app.py                   # Central server hook & routing configuration
├── requirements.txt         # Core project environment declarations
├── streamlit_app.py         # Main analytical dashboard execution script
├── vercel.json               # Serverless platform target configuration
├── api/
│   └── index.py              # Vercel function edge-entrypoint implementation
├── docs/                     # Contextual architectural definitions and design logs
├── src/                       # Core internal application source logic
└── tests/                    # Automated test scripts and regression configurations
```

---

## 🚀 Installation & Setup

### Prerequisites

- Python **3.9** or higher installed locally
- `pip` package manager configured on your system PATH

### 1. Clone & Set Up the Environment

```bash
# Clone the repository
git clone https://github.com/venkateshmalakala/Emotion-Detection-Learning-Support-Engine.git
cd Emotion-Detection-Learning-Support-Engine/code

# Set up a clean, isolated virtual environment
python -m venv venv

# Activate the environment
# macOS/Linux:
source venv/bin/activate
# Windows (Command Prompt):
venv\Scripts\activate
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration & Environment Variables

The platform runs out of the box using local, rule-based strategy mappings. To enable high-fidelity, dynamic responses via generative AI, set the following optional environment variables.

**Linux / macOS (Bash/Zsh)**
```bash
export GEMINI_API_KEY="your_api_key_here"
export GEMINI_MODEL="gemini-1.5-flash"
```

**Windows (Command Prompt)**
```cmd
set GEMINI_API_KEY="your_api_key_here"
set GEMINI_MODEL="gemini-1.5-flash"
```

**Windows (PowerShell)**
```powershell
$env:GEMINI_API_KEY="your_api_key_here"
$env:GEMINI_MODEL="gemini-1.5-flash"
```

---

## 🖥️ Execution Guide

### Local Interactive Dashboard (Streamlit)

To review model output comparisons, mixed-emotion metrics, and historical logs visually:

```bash
streamlit run streamlit_app.py
```

### Core Engine API Application

To run the web-server backend API locally:

```bash
python app.py
```

### Serverless Deployment (Vercel)

The repository includes a configured `vercel.json` and uses the serverless function handler located at `api/index.py`.

```bash
# Ensure the Vercel CLI is installed globally
npm i -g vercel

# Deploy directly from the project root
vercel --prod
```

---

## 🧪 Testing Protocol

The testing framework uses regression validation suites powered by `pytest` to guarantee model output consistency and logical flow mapping.

```bash
# Run tests silently with summary output
pytest -q

# Run verbose tests to inspect structural passes
pytest -v
```

---

## 📖 Example Usage

**Input**

> "I've been trying to fix this bug in my system for over 4 hours, and I'm still getting a memory allocation error. I'm completely stuck."

**System Evaluation & Output**

```
────────────────────────────────────────────────────────────────
 Emotion Metrics
 • Frustrated: 🟡 78%
 • Confused:   🔵 15%
 • Confident:  ⚪ 7%

 Pedagogical Recommendation
 We detect frustration levels peaking. Try taking a step away for
 5 minutes. Before jumping back in, write down a structured mental
 model or diagram of how memory flows through this isolated block.
 Let's tackle it in segments.
────────────────────────────────────────────────────────────────
```

---

## 🔍 Assumptions & Limitations

- **Model Architectures:** The system references dual processing pipelines (BiLSTM & BERT-style). In lightweight local environments, the classifiers fall back to optimized representations if GPU hardware resources are unavailable.
- **External Network Dependencies:** If an API key is missing or invalid, the platform safely skips LLM orchestration and falls back to local template strategies.
- **Local CSV File I/O:** The analytics subsystem uses continuous CSV logging. If the host platform restricts multi-threaded file writes under heavy concurrent load, performance degradation may occur.

---

## 👥 Contributors

| Name | Role | GitHub |
| :--- | :--- | :--- |
| Venkatesh Malakala | Lead Architect & Maintainer | [@venkateshmalakala](https://github.com/venkateshmalakala) |

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.
