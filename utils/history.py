import streamlit as st
from datetime import datetime

# ==========================================
# Initialize History
# ==========================================

def initialize_history():
    """
    Create history list if it doesn't exist.
    """
    if "history" not in st.session_state:
        st.session_state.history = []


# ==========================================
# Add History
# ==========================================

def add_history(history_type, title, content):
    """
    Add a new history record.
    """

    initialize_history()

    record = {
        "time": datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"),
        "type": history_type,
        "title": title,
        "content": content
    }

    # Add newest record at the beginning
    st.session_state.history.insert(0, record)


# ==========================================
# Get History
# ==========================================

def get_history():
    """
    Return all history records.
    """

    initialize_history()

    return st.session_state.history


# ==========================================
# Clear History
# ==========================================

def clear_history():
    """
    Remove all history.
    """

    initialize_history()

    st.session_state.history.clear()


# ==========================================
# Delete One Record
# ==========================================

def delete_history(index):
    """
    Delete a single history record.
    """

    initialize_history()

    if 0 <= index < len(st.session_state.history):
        st.session_state.history.pop(index)


# ==========================================
# History Count
# ==========================================

def history_count():
    """
    Return number of saved records.
    """

    initialize_history()

    return len(st.session_state.history)
