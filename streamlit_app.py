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
    background: radial-gradient(circle at top left, #d6eafd, transparent 30%),
                radial-gradient(circle at bottom right, #fde2ff, transparent 25%),
                #f8fafc;
}
.main {
    background: rgba(255, 255, 255, 0.88);
    box-shadow: 0 16px 60px rgba(15, 23, 42, 0.08);
    border-radius: 24px;
    padding: 1.5rem 2rem 2rem;
}
.block-container {
    padding-top: 1rem;
}
.row-widget.stTextArea > div > textarea {
    min-height: 160px;
    border-radius: 18px;
    border: 1px solid #cbd5e1;
    box-shadow: inset 0 2px 10px rgba(15, 23, 42, 0.06);
}
.stButton button {
    background-color: #4f46e5;
    color: white;
    border-radius: 14px;
    padding: 0.9rem 1.6rem;
    box-shadow: 0 14px 30px rgba(79, 70, 229, 0.18);
    transition: transform 0.24s ease, box-shadow 0.24s ease;
}
.stButton button:hover {
    transform: translateY(-2px);
    box-shadow: 0 20px 45px rgba(79, 70, 229, 0.26);
}
.card {
    border-radius: 24px;
    padding: 1.5rem;
    background: rgba(255, 255, 255, 0.95);
    border: 1px solid rgba(148, 163, 184, 0.16);
    box-shadow: 0 10px 30px rgba(15, 23, 42, 0.06);
    animation: float 8s ease-in-out infinite;
}
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-6px); }
}
.badge {
    display: inline-block;
    margin: 0.1rem 0.35rem 0.35rem 0;
    padding: 0.45rem 0.85rem;
    border-radius: 999px;
    background: #eef2ff;
    color: #4338ca;
    font-weight: 600;
}
</style>
"""

st.markdown(page_styles, unsafe_allow_html=True)

st.markdown("""
# Emotion Learning Support

**Turn study stress into supportive action with emotion-aware guidance, quick next steps, and positive momentum.**
"""
)

with st.container():
    st.markdown("***")

col1, col2 = st.columns([2, 1], gap="large")
with col1:
    user_text = st.text_area("Describe your study challenge", "I’m stuck on recursion and feel confused...")
    analyze = st.button("Analyze emotions")

    if analyze and user_text.strip():
        prediction = classify_text(user_text)
        response = generate_support_response(user_text, prediction)
        comparison = get_model_comparison(user_text)
        strategies = get_personalized_strategies(prediction)

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Detected emotions")
        st.write(f"**Primary emotion:** {prediction['primary_emotion']}")
        st.write(f"**Mixed emotions:** {', '.join(prediction['mixed_emotions']) if prediction['mixed_emotions'] else 'None'}")
        st.write(f"**Confidence:** {prediction['confidence']}")
        st.markdown("</div>", unsafe_allow_html=True)

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
        st.markdown(f"<span class='badge'>BiLSTM: {comparison['BiLSTM']['primary_emotion']}</span> <span class='badge'>BERT: {comparison['BERT']['primary_emotion']}</span>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Why this helps")
    st.write(
        "The assistant combines emotion detection, rule-based support, and model comparison to help learners move from confusion to clarity with confidence."
    )
    st.write("\n- Fast emotional insight\n- Clear next steps\n- Encouraging tone\n- Transparent comparisons")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("How to use")
    st.write(
        "Paste a problem description, click Analyze, and review the emotion-aware guidance. Save this as your learning support dashboard with better clarity and confidence."
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Animated mood pickup")
    st.markdown(
        "<div style='font-size: 1rem; color: #4338ca;'>✨ The interface is designed to feel calm, modern, and supportive — not overwhelming.</div>",
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)
