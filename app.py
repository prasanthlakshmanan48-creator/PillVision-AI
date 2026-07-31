import streamlit as st

# ---------------------------------------
# Page Configuration
# ---------------------------------------

st.set_page_config(
    page_title="💊 PillVision AI",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------
# Load CSS
# ---------------------------------------

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ---------------------------------------
# Header
# ---------------------------------------

st.markdown(
"""
<h1 class="main-title">
💊 PillVision AI
</h1>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<h4 style='text-align:center;color:gray;'>
AI Powered Medicine Recognition & Healthcare Assistant
</h4>
""",
unsafe_allow_html=True
)

st.markdown("---")

# ---------------------------------------
# Status Cards
# ---------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="🤖 AI Model",
        value="Gemini"
    )

with col2:
    st.metric(
        label="📦 Version",
        value="1.0"
    )

with col3:
    st.metric(
        label="🌐 Status",
        value="Online"
    )

with col4:
    st.metric(
        label="⚡ OCR",
        value="Enabled"
    )

st.markdown("---")

# ---------------------------------------
# Welcome
# ---------------------------------------

st.markdown("""
## 👋 Welcome

PillVision AI helps you identify medicines using AI and provides reliable educational information.

Choose any feature from the sidebar.
""")

st.markdown("---")

# ---------------------------------------
# Features
# ---------------------------------------

st.header("🚀 Available Features")

feature1, feature2 = st.columns(2)

with feature1:

    st.success("📷 Scan Medicine")

    st.success("🔍 AI Medicine Search")

    st.success("⚠️ Drug Interaction Checker")

with feature2:

    st.success("💬 AI Health Chat")

    st.success("📚 Scan History")

    st.success("📄 PDF Report Generator")

st.markdown("---")

# ---------------------------------------
# How It Works
# ---------------------------------------

st.header("⚙️ How It Works")

step1, step2, step3 = st.columns(3)

with step1:

    st.info("""
### 📷 Step 1

Upload a medicine image.
""")

with step2:

    st.info("""
### 🤖 Step 2

Gemini AI + OCR analyze the medicine.
""")

with step3:

    st.info("""
### 📄 Step 3

Receive medicine details and download a PDF report.
""")

st.markdown("---")

# ---------------------------------------
# Supported Analysis
# ---------------------------------------

st.header("🩺 AI Analysis Includes")

left, right = st.columns(2)

with left:

    st.write("✅ Medicine Name")

    st.write("✅ Active Ingredient")

    st.write("✅ Uses")

    st.write("✅ Dosage")

    st.write("✅ Side Effects")

    st.write("✅ Manufacturer")

with right:

    st.write("✅ Drug Interactions")

    st.write("✅ Pregnancy Safety")

    st.write("✅ Alcohol Interaction")

    st.write("✅ Storage")

    st.write("✅ Food Interaction")

    st.write("✅ Summary")

st.markdown("---")

# ---------------------------------------
# Sidebar Reminder
# ---------------------------------------

st.info(
"""
👈 Use the sidebar to access:

📷 Scan Medicine

🔍 Medicine Search

⚠️ Drug Interaction Checker

💬 AI Health Chat

📚 History

ℹ️ About
"""
)

st.markdown("---")

# ---------------------------------------
# Disclaimer
# ---------------------------------------

st.error("""
⚠️ Medical Disclaimer

PillVision AI is intended for educational purposes only.

This application should NOT replace professional medical advice, diagnosis or treatment.

Always consult a qualified doctor or pharmacist before taking, stopping or changing any medicine.
""")

st.markdown("---")

# ---------------------------------------
# Footer
# ---------------------------------------

st.markdown(
"""
<div style="text-align:center;color:gray;">
Made with ❤️ using Streamlit, Gemini AI and EasyOCR
</div>
""",
unsafe_allow_html=True
)
