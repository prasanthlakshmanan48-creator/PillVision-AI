import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About PillVision AI")

st.markdown("""
# 💊 PillVision AI

PillVision AI is an AI-powered medicine recognition and healthcare assistant.

It helps users identify medicines from images and provides educational information about medicines using Google's Gemini AI.
""")

st.markdown("---")

st.header("🚀 Features")

col1, col2 = st.columns(2)

with col1:

    st.success("📷 Scan Medicine")

    st.success("🔍 Medicine Search")

    st.success("⚠️ Drug Interaction Checker")

    st.success("💬 AI Health Chat")

with col2:

    st.success("📚 Scan History")

    st.success("📄 PDF Report")

    st.success("📝 OCR Text Recognition")

    st.success("🤖 Gemini AI")

st.markdown("---")

st.header("🛠 Technologies Used")

st.info("""
• Python

• Streamlit

• Google Gemini AI

• EasyOCR

• ReportLab

• Pillow

• NumPy

• OpenCV
""")

st.markdown("---")

st.header("📋 Version")

st.write("Version : **1.0**")

st.write("Status : **Development**")

st.write("Platform : **Streamlit**")

st.write("Language : **Python**")

st.markdown("---")

st.header("🎯 Future Updates")

st.write("✅ Medicine Scanner")

st.write("✅ AI Medicine Search")

st.write("✅ Drug Interaction Checker")

st.write("✅ AI Health Chat")

st.write("🔜 Voice Assistant")

st.write("🔜 Barcode Scanner")

st.write("🔜 Medicine Reminder")

st.write("🔜 User Login")

st.write("🔜 Permanent Cloud History")

st.write("🔜 Mobile App")

st.markdown("---")

st.header("👨‍💻 Developer")

st.write("Developed by:")

st.write("**Prasanth L**")

st.write("Biomedical Engineering Student")

st.markdown("---")

st.header("⚠️ Medical Disclaimer")

st.warning("""
PillVision AI is intended for educational and informational purposes only.

The information provided by this application should not replace professional medical advice, diagnosis, or treatment.

Always consult a qualified doctor or pharmacist before taking, stopping, or changing any medication.
""")

st.markdown("---")

st.success("Thank you for using 💊 PillVision AI ❤️")
