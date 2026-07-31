import streamlit as st

st.set_page_config(
    page_title="💊 PillVision AI",
    page_icon="💊",
    layout="wide"
)

st.title("💊 PillVision AI")

st.subheader("AI Powered Medicine Recognition & Healthcare Assistant")

st.markdown("---")

col1,col2,col3=st.columns(3)

with col1:
    st.metric("AI Model","Gemini")

with col2:
    st.metric("Version","1.0")

with col3:
    st.metric("Status","🟢 Online")

st.markdown("---")

st.header("✨ Features")

c1,c2=st.columns(2)

with c1:

    st.success("📷 Scan Medicine")

    st.success("🔍 Medicine Search")

    st.success("⚠️ Drug Interaction Checker")

with c2:

    st.success("💬 AI Health Chat")

    st.success("📚 History")

    st.success("📄 Download PDF Report")

st.markdown("---")

st.info("👈 Use the sidebar to open all features.")

st.warning(
"""
Educational use only.

Always consult a qualified doctor or pharmacist before taking medicines.
"""
)
