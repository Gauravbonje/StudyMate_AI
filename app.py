import streamlit as st
import time
from agents import create_study_crew
from pdf_generator import generate_pdf

st.set_page_config(page_title="StudyMate AI", layout="wide")

st.title("StudyMate AI – Multi-Agent Learning Assistant")
st.markdown("CSET395 Project – Agentic AI System")

topic = st.text_input("Enter Topic")

if st.button("Generate Study Pack"):

    if not topic:
        st.error("Please enter a topic")
        st.stop()

    with st.spinner("🤖 Agents working..."):

        start = time.time()

        crew = create_study_crew(topic)
        result = crew.kickoff()

        latency = round(time.time() - start, 2)

    st.success("✅ Study Pack Ready")
    st.markdown(str(result))

    # -------- PDF Download --------
    pdf_path = generate_pdf(str(result), "study_pack.pdf")
    st.download_button(
        "📄 Download PDF",
        data=open(pdf_path, "rb"),
        file_name="StudyMate_Notes.pdf"
    )

    # -------- Metrics --------
    st.divider()
    st.subheader("📊 Observation Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Latency", f"{latency} sec")
    col2.metric("Architecture", "Sequential Multi-Agent")
    col3.metric("Model", "Gemini Flash Latest")

    st.info("Tip: Check terminal for Agent Thought Logs for Accountability Audit.")
