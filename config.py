import streamlit as st
from google import genai

MODEL_NAME = "gemini-3.5-flash"

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)
