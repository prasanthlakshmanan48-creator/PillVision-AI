import streamlit as st

from utils.gemini import search_medicine
from utils.history import add_history
from utils.pdf import create_pdf

st.set_page_config(
    page_title="Medicine Search",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 AI Medicine Search")

st.write("""
Search any medicine by entering its name.

Examples:
- Dolo 650
- Paracetamol
- Crocin
- Azithromycin
- Cetirizine
""")

medicine = st.text_input(
    "💊 Medicine Name",
    placeholder="Enter medicine name..."
)

col1, col2 = st.columns(2)

with col1:

    search_btn = st.button(
        "🔍 Search Medicine",
        use_container_width=True
    )

with col2:

    clear_btn = st.button(
        "🗑 Clear",
        use_container_width=True
    )

if clear_btn:
    st.rerun()

if search_btn:

    if medicine.strip() == "":

        st.warning("Please enter a medicine name.")

    else:

        with st.spinner("Searching medicine..."):

            try:

                result = search_medicine(medicine)

                add_history(
                    "Medicine Search",
                    medicine,
                    result
                )

                st.success("Medicine Found")

                st.markdown("---")

                st.markdown(result)

                pdf_file = create_pdf(result)

                with open(pdf_file, "rb") as file:

                    st.download_button(
                        "📄 Download PDF Report",
                        data=file,
                        file_name=f"{medicine}_Report.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )

            except Exception as e:

                st.error("Unable to search medicine.")

                st.exception(e)

st.markdown("---")

st.subheader("💡 Popular Medicines")

c1, c2, c3 = st.columns(3)

with c1:
    st.info("💊 Dolo 650")
    st.info("💊 Crocin")
    st.info("💊 Calpol")

with c2:
    st.info("💊 Cetirizine")
    st.info("💊 Ibuprofen")
    st.info("💊 Paracetamol")

with c3:
    st.info("💊 Azithromycin")
    st.info("💊 Amoxicillin")
    st.info("💊 Pantoprazole")

st.markdown("---")

st.warning("""
⚠️ PillVision AI provides educational information only.

Always consult a qualified doctor or pharmacist before taking any medicine.
""")
