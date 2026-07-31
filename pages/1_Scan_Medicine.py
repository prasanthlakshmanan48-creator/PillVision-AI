import streamlit as st
from PIL import Image

from utils.gemini import analyze_medicine_image
from utils.ocr import extract_text
from utils.history import add_history
from utils.pdf import create_pdf

st.set_page_config(
    page_title="Scan Medicine",
    page_icon="💊",
    layout="wide"
)

st.title("💊 Scan Medicine")

st.write("""
Upload a medicine strip, medicine box, blister pack or bottle.

PillVision AI will analyze the medicine using OCR and Gemini AI.
""")

uploaded_file = st.file_uploader(
    "📷 Upload Medicine Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns([1, 2])

    with col1:

        st.image(
            image,
            caption="Uploaded Medicine",
            use_container_width=True
        )

    with col2:

        st.info("Click Analyze to start AI analysis.")

        if st.button("🔍 Analyze Medicine", use_container_width=True):

            with st.spinner("Reading medicine text..."):

                ocr_text = extract_text(image)

            st.subheader("📝 OCR Detected Text")

            if ocr_text.strip() == "":
                st.warning("No readable text detected.")
            else:
                st.text_area(
                    "OCR Result",
                    ocr_text,
                    height=120
                )

            with st.spinner("Analyzing with Gemini AI..."):

                try:

                    result = analyze_medicine_image(
                        image,
                        ocr_text
                    )

                    add_history(
                        "Medicine Scan",
                        "Medicine Image Analysis",
                        result
                    )

                    st.success("✅ Analysis Completed")

                    st.markdown("---")

                    st.markdown(result)

                    pdf_file = create_pdf(result)

                    with open(pdf_file, "rb") as file:

                        st.download_button(
                            label="📄 Download PDF Report",
                            data=file,
                            file_name="Medicine_Report.pdf",
                            mime="application/pdf",
                            use_container_width=True
                        )

                except Exception as e:

                    st.error("❌ Unable to analyze medicine.")

                    st.exception(e)

st.markdown("---")

with st.expander("💡 Tips for Better Accuracy"):

    st.write("""
- Use a clear image.
- Capture the full medicine strip or box.
- Avoid blurry or dark photos.
- Ensure the medicine name is visible.
- Avoid reflections from flash.
""")

st.markdown("---")

st.warning("""
⚠️ Disclaimer

PillVision AI provides educational information only.

Always consult a qualified healthcare professional before taking, stopping, or changing any medication.

Never rely solely on AI for emergency medical decisions.
""")
