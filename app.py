import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="💊 PillVision AI",
    page_icon="💊",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("💊 PillVision AI")
st.sidebar.success("Select a feature above.")

# -----------------------------
# Home Page
# -----------------------------
st.title("💊 PillVision AI")
st.subheader("AI-Powered Medicine Recognition & Healthcare Assistant")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("AI Model", "Gemini")

with col2:
    st.metric("Version", "1.0")

with col3:
    st.metric("Status", "🟢 Online")

st.markdown("---")

st.header("🚀 Features")

c1, c2 = st.columns(2)

with c1:
    st.success("📷 Scan Medicine")
    st.success("🔍 Search Medicine")
    st.success("⚠️ Drug Interaction Checker")

with c2:
    st.success("💬 AI Health Chat")
    st.success("📄 Download PDF Report")
    st.success("📚 Scan History")

st.markdown("---")

st.info(
    """
👈 Use the **sidebar** to open:

• Scan Medicine

• Medicine Search

• Drug Interaction Checker

• AI Health Chat

• History

• About
"""
)

st.markdown("---")

st.warning(
    "⚠️ Educational use only. Always consult a qualified healthcare professional before starting, stopping, or changing any medication."
)
