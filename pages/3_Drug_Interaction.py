import streamlit as st
from utils.gemini import drug_interaction
from utils.history import add_history
from utils.pdf import create_pdf

st.set_page_config(
    page_title="Drug Interaction Checker",
    page_icon="⚠️",
    layout="wide"
)

st.title("⚠️ Drug Interaction Checker")

st.markdown("""
Check whether **two medicines** may interact with each other.

### Examples
- Dolo 650 + Ibuprofen
- Paracetamol + Alcohol
- Warfarin + Aspirin
""")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    medicine1 = st.text_input(
        "💊 Medicine 1",
        placeholder="Example: Dolo 650"
    )

with col2:
    medicine2 = st.text_input(
        "💊 Medicine 2",
        placeholder="Example: Ibuprofen"
    )

st.markdown("---")

button = st.button(
    "🔍 Analyze Interaction",
    use_container_width=True
)

if button:

    if medicine1.strip() == "" or medicine2.strip() == "":

        st.warning("Please enter both medicine names.")

    else:

        with st.spinner("Checking interaction..."):

            try:

                result = drug_interaction(
                    medicine1,
                    medicine2
                )

                add_history(
                    "Drug Interaction",
                    f"{medicine1} + {medicine2}",
                    result
                )

                st.success("✅ Analysis Completed")

                st.markdown("---")

                st.markdown(result)

                pdf = create_pdf(result)

                with open(pdf, "rb") as file:

                    st.download_button(
                        "📄 Download PDF Report",
                        file,
                        file_name="Drug_Interaction_Report.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )

            except Exception as e:

                st.error("Unable to analyze interaction.")

                st.exception(e)

st.markdown("---")

st.subheader("🩺 Interaction Risk Levels")

green, orange, red = st.columns(3)

with green:

    st.success("""
🟢 LOW RISK

Generally considered safe.

Still follow your doctor's advice.
""")

with orange:

    st.warning("""
🟠 MODERATE RISK

May require monitoring.

Consult a healthcare professional.
""")

with red:

    st.error("""
🔴 HIGH RISK

Avoid combining without medical supervision.

Seek professional advice immediately.
""")

st.markdown("---")

st.subheader("💊 Popular Interaction Checks")

left, right = st.columns(2)

with left:

    st.info("Paracetamol + Ibuprofen")

    st.info("Warfarin + Aspirin")

    st.info("Cetirizine + Alcohol")

with right:

    st.info("Azithromycin + Antacid")

    st.info("Metformin + Alcohol")

    st.info("Amoxicillin + Paracetamol")

st.markdown("---")

st.subheader("📋 AI Report Includes")

st.success("🟢 Risk Level")

st.success("📖 Interaction Summary")

st.success("⚠️ Possible Problems")

st.success("💊 Side Effects")

st.success("💡 Recommendations")

st.success("🚑 When to Contact a Doctor")

st.markdown("---")

st.warning("""
⚠️ PillVision AI provides educational information only.

Never stop or start medicines based only on AI advice.

Always consult your doctor or pharmacist.
""")
