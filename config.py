# ==========================================
# PillVision AI Configuration File
# ==========================================

from google import genai

# -------------------------------------------------
# Paste your Gemini API Key below
# -------------------------------------------------

GEMINI_API_KEY = "AQ.Ab8RN6JE5z4DbCvTB2wRJWzhd7FYjDOEAC07y6f0F58Yy3TtCQ"

# -------------------------------------------------
# Gemini Client
# -------------------------------------------------

client = genai.Client(
    api_key=GEMINI_API_KEY
)

# -------------------------------------------------
# AI Model
# -------------------------------------------------

MODEL_NAME = "gemini-3.5-flash"

# -------------------------------------------------
# Application Details
# -------------------------------------------------

APP_NAME = "PillVision AI"

VERSION = "1.0"

DEVELOPER = "Your Name"

DESCRIPTION = """
AI Powered Medicine Recognition System
"""

DISCLAIMER = """
⚠️ PillVision AI provides educational information only.

Always consult a qualified doctor or pharmacist
before taking or changing any medicine.
"""
