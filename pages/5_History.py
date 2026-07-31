import streamlit as st
from datetime import datetime

# --------------------------------------
# Initialize History
# --------------------------------------

def initialize_history():

    if "history" not in st.session_state:
        st.session_state.history = []


# --------------------------------------
# Add New Record
# --------------------------------------

def add_history(history_type, title, content):

    initialize_history()

    record = {
        "time": datetime.now().strftime("%d-%m-%Y %H:%M"),
        "type": history_type,
        "title": title,
        "content": content
    }

    st.session_state.history.insert(0, record)


# --------------------------------------
# Get History
# --------------------------------------

def get_history():

    initialize_history()

    return st.session_state.history


# --------------------------------------
# Clear History
# --------------------------------------

def clear_history():

    st.session_state.history = []
