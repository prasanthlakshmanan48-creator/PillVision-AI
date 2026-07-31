import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ",
    layout="wide"
)

st.title("ℹ About PillVision AI")

st.markdown("""
# 💊 PillVision AI

AI Powered Medicine Recognition System
""")

st.markdown("---")

st.header("🚀 Features")

features=[
"📷 Scan Medicine",
"🔍 Medicine Search",
"⚠ Drug Interaction",
"💬 AI Health Chat",
"📚 History",
"📄 PDF Report",
"📝 OCR",
"🤖 Gemini AI"
]

for feature in features:
    st.success(feature)

st.markdown("---")

st.header("🛠 Technology")

st.info("""
Python

Streamlit

Gemini AI

EasyOCR

ReportLab

Pillow

NumPy
""")

st.markdown("---")

st.header("📦 Version")

st.write("Version : 2.0")

st.write("Platform : Streamlit")

st.write("Status : Development")

st.markdown("---")

st.header("👨‍💻 Developer")

st.write("Name : Prasanth L")

st.write("Department : Biomedical Engineering")

st.write("Project : PillVision AI")

st.markdown("---")

st.header("🔮 Upcoming Features")

st.success("📸 Camera Scan")

st.success("🔊 Voice Assistant")

st.success("🌍 Multi Language")

st.success("📱 Android App")

st.success("☁ Cloud Database")

st.success("🔐 Login System")

st.success("💊 Medicine Reminder")

st.markdown("---")

st.warning("""
⚠ Medical Disclaimer

This application is for educational purposes only.

Always consult a qualified doctor or pharmacist before taking medicines.
""")

st.markdown("---")

st.markdown(
"""
<center>

Made with ❤️ using

Python | Streamlit | Gemini AI

</center>
""",
unsafe_allow_html=True
)
