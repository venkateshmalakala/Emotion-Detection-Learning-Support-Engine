import streamlit as st

from src.emotion_platform import (
    classify_text,
    generate_support_response,
    get_analytics_summary,
    get_model_comparison,
    get_personalized_strategies,
    load_interactions,
    log_interaction,
)

st.set_page_config(page_title="Emotion Learning Support", page_icon="🧠", layout="wide")

st.title("AI-Driven Emotion Detection & Personalized Learning Support")
st.write("Describe your study challenge and receive an emotion-aware response, personalized next steps, and a view of how the system is tracking support needs.")

student_input = st.text_area("What is challenging you right now?", height=150)
show_ai_response = st.checkbox("Show AI support response", value=True)
save_interaction = st.checkbox("Save this interaction for analytics", value=True)

if st.button("Analyze") and student_input.strip():
    prediction = classify_text(student_input)
    response = generate_support_response(student_input, prediction)
    comparison = get_model_comparison(student_input)

    if save_interaction:
        log_interaction(student_input, prediction, response)

    st.session_state["last_prediction"] = prediction
    st.session_state["last_response"] = response
    st.session_state["last_comparison"] = comparison
    st.session_state["last_input"] = student_input

analysis_tab, analytics_tab = st.tabs(["Analysis", "Analytics"])

with analysis_tab:
    if "last_prediction" in st.session_state:
        prediction = st.session_state["last_prediction"]
        response = st.session_state["last_response"]
        comparison = st.session_state["last_comparison"]
        student_input = st.session_state["last_input"]

        st.subheader("Detected Emotion")
        st.write(f"Primary emotion: {prediction['primary_emotion']}")
        st.write(f"Mixed emotions: {', '.join(prediction['mixed_emotions']) if prediction['mixed_emotions'] else 'None'}")
        st.write(f"Confidence: {prediction['confidence']}")

        st.subheader("Support Response")
        if show_ai_response:
            st.success(response)
        else:
            st.info("AI response hidden. Enable the toggle to view the supportive guidance.")

        st.subheader("Personalized Strategies")
        for strategy in get_personalized_strategies(prediction):
            st.write(f"- {strategy}")

        st.subheader("Model Comparison")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("BiLSTM", comparison["BiLSTM"]["primary_emotion"])
        with col2:
            st.metric("BERT", comparison["BERT"]["primary_emotion"])
    else:
        st.info("Enter a study challenge and click Analyze to see the emotion-aware support experience.")

with analytics_tab:
    history = load_interactions()
    summary = get_analytics_summary()

    if history.empty:
        st.info("No interactions have been logged yet. Saving an interaction will populate the dashboard.")
    else:
        st.metric("Total interactions", summary["total_interactions"])
        emotion_counts = summary.get("emotion_counts", {})
        if emotion_counts:
            st.bar_chart(emotion_counts)

        if summary.get("trend"):
            trend_df = st.session_state.get("trend_df")
            if trend_df is None:
                trend_df = {
                    "date": [row["date"] for row in summary["trend"]],
                    "count": [row["count"] for row in summary["trend"]],
                }
                st.session_state["trend_df"] = trend_df
            st.line_chart(trend_df)

        st.dataframe(history.tail(5), use_container_width=True)
