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

st.markdown("""
Search any medicine using its **Brand Name** or **Generic Name**.

### Examples

- Dolo 650
- Crocin
- Paracetamol
- Cetirizine
- Azithromycin
- Amoxicillin
""")

st.markdown("---")

medicine = st.text_input(
    "💊 Medicine Name",
    placeholder="Example: Dolo 650"
)

col1, col2 = st.columns(2)

with col1:
    search = st.button(
        "🔍 Search",
        use_container_width=True
    )

with col2:
    clear = st.button(
        "🗑 Clear",
        use_container_width=True
    )

if clear:
    st.rerun()

if search:

    if medicine.strip() == "":

        st.warning("Please enter a medicine name.")

    else:

        with st.spinner("Searching Medicine..."):

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

                pdf = create_pdf(result)

                with open(pdf, "rb") as file:

                    st.download_button(
                        "📄 Download PDF Report",
                        file,
                        file_name=f"{medicine}.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )

            except Exception as e:

                st.error("Unable to search medicine.")

                st.exception(e)

st.markdown("---")

st.subheader("💊 Popular Medicines")

c1, c2, c3 = st.columns(3)

with c1:

    st.info("Paracetamol")

    st.info("Crocin")

    st.info("Dolo 650")

with c2:

    st.info("Ibuprofen")

    st.info("Cetirizine")

    st.info("Amoxicillin")

with c3:

    st.info("Azithromycin")

    st.info("Pantoprazole")

    st.info("Metformin")

st.markdown("---")

st.subheader("🩺 Information You Will Receive")

st.success("💊 Medicine Name")

st.success("🧪 Active Ingredient")

st.success("🏭 Manufacturer")

st.success("🩺 Uses")

st.success("💉 Dosage")

st.success("⚠️ Side Effects")

st.success("🔄 Drug Interactions")

st.success("🤰 Pregnancy")

st.success("🍺 Alcohol Interaction")

st.success("🥛 Food Interaction")

st.success("📦 Storage")

st.success("📝 Summary")

st.markdown("---")

st.warning("""
⚠️ PillVision AI is for educational purposes only.

Always consult a qualified healthcare professional before taking or changing any medication.
""")
