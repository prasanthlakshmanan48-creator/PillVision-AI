import streamlit as st
from utils.gemini import search_medicine

st.set_page_config(
    page_title="Medicine Search",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Medicine Search")

st.write("""
Search any medicine and PillVision AI will provide detailed information.
""")

medicine = st.text_input(
    "💊 Enter Medicine Name",
    placeholder="Example: Dolo 650, Crocin, Paracetamol..."
)

if st.button("🔍 Search Medicine"):

    if medicine.strip() == "":
        st.warning("Please enter a medicine name.")
    else:

        with st.spinner("Searching..."):

            try:
from utils.history import add_history
             result = search_medicine(medicine)

add_history(
    "Medicine Search",
    medicine,
    result
)

st.success("Medicine Found")

st.markdown(result)
            except Exception as e:

                st.error("Unable to search medicine.")

                st.exception(e)

st.markdown("---")

st.info("""
Examples

• Dolo 650

• Paracetamol

• Azithromycin

• Crocin

• Amoxicillin

• Cetirizine

• Ibuprofen
""")

st.warning("""
⚠️ Educational purposes only.

Always consult a doctor or pharmacist before taking medicines.
""")
