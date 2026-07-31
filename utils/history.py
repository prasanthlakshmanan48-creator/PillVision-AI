import streamlit as st
from datetime import datetime

def initialize_history():

    if "history" not in st.session_state:
        st.session_state.history=[]

def add_history(history_type,title,content):

    initialize_history()

    st.session_state.history.insert(0,{
        "time":datetime.now().strftime("%d-%m-%Y %I:%M %p"),
        "type":history_type,
        "title":title,
        "content":content
    })

def get_history():

    initialize_history()

    return st.session_state.history

def clear_history():

    initialize_history()

    st.session_state.history.clear()

def history_count():

    initialize_history()

    return len(st.session_state.history)
