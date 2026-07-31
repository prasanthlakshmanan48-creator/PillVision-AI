import streamlit as st

from utils.history import (
    get_history,
    clear_history,
    history_count
)

from utils.pdf import create_pdf

st.set_page_config(
    page_title="History",
    page_icon="📚",
    layout="wide"
)

st.title("📚 History")

st.write("""
View your previous:

• Medicine Scans

• Medicine Searches

• Drug Interaction Checks

• AI Health Chats
""")

st.markdown("---")

count = history_count()

st.metric(
    "Total Records",
    count
)

history = get_history()

if len(history) == 0:

    st.info("No history available.")

else:

    for i, item in enumerate(history):

        with st.expander(
            f"{item['type']} | {item['time']}"
        ):

            st.subheader(item["title"])

            st.write(item["content"])

            pdf = create_pdf(item["content"])

            with open(pdf, "rb") as file:

                st.download_button(
                    label="📄 Download Report",
                    data=file,
                    file_name=f"History_{i+1}.pdf",
                    mime="application/pdf",
                    key=f"pdf_{i}"
                )

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "🗑 Clear All History",
        use_container_width=True
    ):

        clear_history()

        st.success("History Cleared Successfully")

        st.rerun()

with col2:

    if st.button(
        "🔄 Refresh",
        use_container_width=True
    ):

        st.rerun()

st.markdown("---")

st.info("""
History includes:

📷 Medicine Scans

🔍 Medicine Searches

⚠️ Drug Interaction Reports

💬 AI Health Chats
""")

st.warning("""
History is currently stored only for this Streamlit session.

In Version 2, history will be stored permanently using SQLite.
""")
