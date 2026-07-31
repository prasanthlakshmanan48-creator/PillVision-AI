import streamlit as st
from utils.gemini import drug_interaction

st.set_page_config(
    page_title="Drug Interaction Checker",
    page_icon="⚠️",
    layout="wide"
)

st.title("⚠️ Drug Interaction Checker")

st.write("""
Check whether two medicines may interact with each other.

⚠️ This tool is for educational purposes only.
""")

col1, col2 = st.columns(2)

with col1:
    medicine1 = st.text_input(
        "💊 Medicine 1",
        placeholder="Example: Paracetamol"
    )

with col2:
    medicine2 = st.text_input(
        "💊 Medicine 2",
        placeholder="Example: Ibuprofen"
    )

if st.button("🔍 Check Interaction"):

    if medicine1 == "" or medicine2 == "":
        st.warning("Please enter both medicine names.")

    else:

        with st.spinner("Checking Drug Interaction..."):

            try:

                result = drug_interaction(
                    medicine1,
                    medicine2
                )

                st.success("Interaction Analysis Completed")

                st.markdown("---")

                st.markdown(result)

            except Exception as e:

                st.error("Unable to analyze interaction.")

                st.exception(e)

st.markdown("---")

st.info("""
Examples

Medicine 1:
Paracetamol

Medicine 2:
Ibuprofen

----------------------

Medicine 1:
Azithromycin

Medicine 2:
Warfarin

----------------------

Medicine 1:
Cetirizine

Medicine 2:
Alcohol
""")

st.warning("""
⚠️ Never stop or start medicines based only on AI advice.

Always consult your doctor or pharmacist.
""")
