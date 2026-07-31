from google import genai

# ------------------------------------
# Paste Your Gemini API Key
# ------------------------------------

GEMINI_API_KEY="AQ.Ab8RN6JE5z4DbCvTB2wRJWzhd7FYjDOEAC07y6f0F58Yy3TtCQ"

# ------------------------------------

MODEL_NAME="gemini-3.5-flash"

client=genai.Client(
    api_key=GEMINI_API_KEY
)

APP_NAME="PillVision AI"

VERSION="1.0"

DEVELOPER="Your Name"
