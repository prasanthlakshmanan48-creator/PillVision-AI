import streamlit as st
from utils.history import get_history, clear_history
from utils.pdf import create_pdf

st.set_page_config(
    page_title="History",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Scan History")

history = get_history()

st.metric("Total Records", len(history))

st.markdown("---")

search = st.text_input(
    "🔍 Search History",
    placeholder="Search medicine..."
)

if history:

    for i, item in enumerate(history):

        if search.lower() not in item["title"].lower() and search.lower() not in item["type"].lower():
            continue

        with st.expander(
            f"{item['type']} | {item['time']}"
        ):

            st.subheader(item["title"])

            st.markdown(item["content"])

            pdf=create_pdf(item["content"])

            with open(pdf,"rb") as file:

                st.download_button(
                    "📄 Download PDF",
                    data=file,
                    file_name=f"History_{i}.pdf",
                    mime="application/pdf",
                    key=i
                )

st.markdown("---")

col1,col2=st.columns(2)

with col1:

    if st.button(
        "🗑 Clear History",
        use_container_width=True
    ):

        clear_history()

        st.success("History Cleared")

        st.rerun()

with col2:

    if st.button(
        "🔄 Refresh",
        use_container_width=True
    ):

        st.rerun()

st.markdown("---")

st.info("""
History includes

📷 Medicine Scan

🔍 Medicine Search

⚠ Drug Interaction

💬 AI Chat
""")
