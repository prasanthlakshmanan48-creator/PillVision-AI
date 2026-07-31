import streamlit as st

st.set_page_config(
    page_title="💊 PillVision AI",
    page_icon="💊",
    layout="wide"
)

st.title("💊 PillVision AI")

st.subheader("AI Powered Medicine Recognition System")

st.markdown("---")

col1,col2,col3=st.columns(3)

with col1:
    st.metric("AI Model","Gemini 3.5")

with col2:
    st.metric("Recognition","Medicine")

with col3:
    st.metric("Status","Online")

st.markdown("---")

st.header("✨ Features")

st.success("📷 Scan Medicine")

st.success("🔍 Search Medicine")

st.success("⚠️ Drug Interaction Checker")

st.success("💬 AI Health Chat")

st.success("📄 Download PDF")

st.success("📚 Scan History")

st.markdown("---")

st.info("👈 Use the sidebar to open each feature.")
