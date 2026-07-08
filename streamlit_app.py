import streamlit as st

from src.emotion_platform import (
    classify_text,
    generate_support_response,
    get_model_comparison,
    get_personalized_strategies,
)

st.set_page_config(
    page_title="Emotion Learning Support",
    page_icon="🧠",
    layout="wide",
)

page_styles = """
<style>
body {
    background: linear-gradient(135deg, #eef2ff 0%, #fdf2f8 40%, #ffffff 100%);
}
section.main {
    background: rgba(255,255,255,0.94) !important;
    border-radius: 30px;
    box-shadow: 0 30px 70px rgba(15, 23, 42, 0.08);
    padding: 2rem 2.5rem 2.5rem;
}
header.block-container {
    padding-top: 1rem;
}
.stTextArea>div>div>textarea {
    min-height: 200px;
    border-radius: 22px;
    border: 1px solid rgba(148, 163, 184, 0.24);
    background: rgba(255, 255, 255, 0.95);
    box-shadow: inset 0 18px 30px rgba(15, 23, 42, 0.04);
    font-size: 1rem;
}
.stButton button {
    background: #4338ca;
    color: #fff;
    border-radius: 16px;
    padding: 0.95rem 1.8rem;
    border: none;
    box-shadow: 0 16px 50px rgba(67, 56, 202, 0.22);
    transition: transform 0.22s ease, box-shadow 0.22s ease;
}
.stButton button:hover {
    transform: translateY(-3px);
    box-shadow: 0 20px 60px rgba(67, 56, 202, 0.28);
}
.card {
    border-radius: 28px;
    padding: 1.6rem;
    background: rgba(255, 255, 255, 0.96);
    border: 1px solid rgba(148, 163, 184, 0.14);
    box-shadow: 0 18px 40px rgba(15, 23, 42, 0.06);
    margin-bottom: 1.2rem;
}
.card h2 {
    margin-top: 0;
}
.badge {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    margin: 0.2rem 0.35rem 0.35rem 0;
    padding: 0.45rem 0.95rem;
    border-radius: 999px;
    background: #eef2ff;
    color: #4338ca;
    font-weight: 700;
}
.glow {
    position: absolute;
    border-radius: 50%;
    filter: blur(85px);
    opacity: 0.55;
}
.glow-1 { width: 260px; height: 260px; background: #c7d2fe; top: -80px; left: -80px; }
.glow-2 { width: 220px; height: 220px; background: #fbcfe8; top: 40px; right: -100px; }
.glow-3 { width: 320px; height: 320px; background: #a7f3d0; bottom: -100px; right: 40px; }
@media (max-width: 1000px) {
    .glow { display: none; }
    section.main { padding: 1.5rem 1.5rem 2rem; }
    .stTextArea>div>div>textarea { min-height: 180px; }
}
@media (max-width: 760px) {
    section.main { padding: 1.25rem 1rem 1.5rem; }
    .stButton button { width: 100%; }
    .card { padding: 1.3rem; }
    .badge { font-size: 0.95rem; }
}
</style>
"""

st.markdown(page_styles, unsafe_allow_html=True)

st.markdown(
    """
    <div style='position: relative; overflow: hidden; padding: 2rem 0;'>
      <div class='glow glow-1'></div>
      <div class='glow glow-2'></div>
      <div class='glow glow-3'></div>
      <div style='position: relative; z-index: 1;'>
        <p style='color: #4338ca; font-weight: 700; margin-bottom: 0.5rem; letter-spacing: 0.08em;'>LEARNING SUPPORT DASHBOARD</p>
        <h1 style='font-size: clamp(2.4rem, 3.8vw, 3.8rem); margin: 0; line-height: 1.05; color: #0f172a;'>Emotion-aware guidance for focused study progress.</h1>
        <p style='max-width: 720px; color: #475569; margin-top: 1rem; font-size: 1.02rem;'>Analyze how the learner feels, get tailored next steps, and compare models with a clean, modern interface built for educators and self-directed students.</p>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

user_text = st.text_area("Describe your study challenge", "I’m stuck on recursion and feel confused...")
show_ai = st.checkbox("Show AI support response", value=True)

if st.button("Analyze emotions") and user_text.strip():
    prediction = classify_text(user_text)
    response = generate_support_response(user_text, prediction)
    comparison = get_model_comparison(user_text)
    strategies = get_personalized_strategies(prediction)

    col1, col2 = st.columns([2, 1], gap="large")
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Emotion insights")
        st.write(f"**Primary emotion:** {prediction['primary_emotion']}")
        st.write(f"**Mixed emotions:** {', '.join(prediction['mixed_emotions']) if prediction['mixed_emotions'] else 'None'}")
        st.write(f"**Confidence:** {prediction['confidence']}")
        st.markdown("</div>", unsafe_allow_html=True)

        if show_ai:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.subheader("Support response")
            st.success(response)
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Personalized strategies")
        for strategy in strategies:
            st.write(f"- {strategy}")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Model comparison")
        st.markdown(
            f"<span class='badge'>🧠 BiLSTM: {comparison['BiLSTM']['primary_emotion']}</span> <span class='badge'>⚡ BERT: {comparison['BERT']['primary_emotion']}</span>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Why this matters")
        st.write("An emotionally intelligent support path helps learners feel seen, reduces stress, and improves direction when tackling difficult concepts.")
        st.write("\n- Emotion-aware feedback\n- Clear next actions\n- Encouraging tone\n- Easy comparison between models")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Pro tips")
        st.write("Use concise descriptions, include what you’ve tried, and let the assistant guide the next step.")
        st.write("\n- Keep one issue per entry\n- Highlight concepts you’re unsure about\n- Note your feelings clearly")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Visual clarity")
        st.write("The layout was designed for quick scanning, calm focus, and professional presentation for learners and educators alike.")
        st.markdown("</div>", unsafe_allow_html=True)
else:
    st.info("Enter your study challenge and click Analyze emotions to launch the professional learning support experience.")
