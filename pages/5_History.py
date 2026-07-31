import streamlit as st
from utils.history import (
    get_history,
    clear_history
)

st.set_page_config(
    page_title="History",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Scan History")

st.write("""
View all previous:

• Medicine Scans

• Medicine Searches

• Drug Interaction Checks

• AI Health Chats
""")

history = get_history()

if len(history) == 0:

    st.info("No history available.")

else:

    st.success(f"{len(history)} Record(s) Found")

    st.markdown("---")

    for item in history:

        with st.expander(
            f"{item['type']} | {item['time']}"
        ):

            st.subheader(item["title"])

            st.write(item["content"])

    st.markdown("---")

    if st.button("🗑️ Clear History"):

        clear_history()

        st.success("History Cleared")

        st.rerun()

st.markdown("---")

st.info(
    "History is currently stored for this session only."
)
