import streamlit as st
from google import genai

MODEL_NAME = "gemini-3.5-flash"

client = genai.Client(
    api_key=st.secrets["AQ.Ab8RN6JE5z4DbCvTB2wRJWzhd7FYjDOEAC07y6f0F58Yy3TtCQ"]
)

APP_NAME = "PillVision AI"
VERSION = "1.0"
