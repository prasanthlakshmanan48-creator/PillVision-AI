import streamlit as st
from google import genai
from PIL import Image

client = genai.Client(
    api_key="YOUR_GEMINI_API_KEY"
)

st.title("💊 PillVision AI")

uploaded_file = st.file_uploader(
    "Upload Medicine Strip",
    type=["jpg","jpeg","png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image, use_container_width=True)

    if st.button("Analyze Medicine"):

        with st.spinner("Analyzing..."):

            prompt = """
Analyze this medicine image.

Provide:

Medicine Name

Active Ingredient

Uses

Typical Dosage

Common Side Effects

Drug Interactions

Warnings

If the medicine cannot be identified, clearly mention that.
"""

            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=[prompt,image]
            )

            st.success("Analysis Completed")

            st.write(response.text)
