import streamlit as st
from PIL import Image
from utils.gemini import analyze_medicine_image

st.set_page_config(
    page_title="Scan Medicine",
    page_icon="💊",
    layout="wide"
)

st.title("💊 Scan Medicine")

st.write(
    """
Upload a medicine strip, medicine box, or bottle image.

PillVision AI will identify the medicine and provide educational information.
"""
)

uploaded_file = st.file_uploader(
    "📷 Upload Medicine Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(
            image,
            caption="Uploaded Medicine",
            use_container_width=True
        )

    with col2:

        st.info("Click the button below to analyze the medicine.")

        if st.button("🔍 Analyze Medicine"):

            with st.spinner("Analyzing medicine..."):

                try:
from utils.history import add_history
                  result = analyze_medicine_image(image)

add_history(
    "Medicine Scan",
    "Medicine Image Analysis",
    result
)

st.success("Analysis Completed")

st.markdown(result)

                except Exception as e:

                    st.error("Analysis failed.")

                    st.exception(e)

st.markdown("---")

st.warning(
    """
⚠️ Disclaimer

PillVision AI provides educational information only.

• Do not use this app as a substitute for professional medical advice.

• Always verify medicine information with a qualified healthcare professional.

• Never start, stop, or change medication based only on AI output.
"""
)
