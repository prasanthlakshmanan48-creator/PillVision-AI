from config import client, MODEL_NAME
from PIL import Image


# ==========================================
# Medicine Image Analysis
# ==========================================

def analyze_medicine_image(image):

    prompt = """
You are an expert pharmacist and healthcare assistant.

Analyze the uploaded medicine image.

Provide your answer in the following format.

💊 Medicine Name

🧪 Active Ingredient

🏥 Manufacturer

💉 Strength

🩺 Uses

💊 Typical Dosage
(General information only)

⚠️ Common Side Effects

🚫 Contraindications

🔄 Drug Interactions

🍺 Alcohol Interaction

🥛 Food Interaction

🤰 Pregnancy

🤱 Breastfeeding

👶 Pediatric Use

📦 Storage Instructions

💵 Approximate Price (if known)

📝 Summary

If the medicine cannot be identified clearly,
say:

"Medicine could not be identified confidently.
Please upload a clearer image."

Do not invent information.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[prompt, image]
    )

    return response.text


# ==========================================
# Medicine Search
# ==========================================

def search_medicine(medicine_name):

    prompt = f"""
You are an expert pharmacist.

Provide complete information about:

Medicine:
{medicine_name}

Include

Medicine Name

Active Ingredient

Uses

Typical Dosage

Common Side Effects

Drug Interactions

Warnings

Pregnancy

Breastfeeding

Food Interaction

Alcohol Interaction

Storage

Approximate Price

Do not invent information.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text


# ==========================================
# Drug Interaction Checker
# ==========================================

def drug_interaction(medicine1, medicine2):

    prompt = f"""
Check interaction between

Medicine 1:
{medicine1}

Medicine 2:
{medicine2}

Return

Risk Level

Interaction

Reason

Recommendation

If interaction is unknown,
say so clearly.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text


# ==========================================
# AI Health Chat
# ==========================================

def health_chat(question):

    prompt = f"""
You are PillVision AI.

Answer only healthcare
and medicine-related questions.

Question:

{question}

Give safe, educational guidance.
Do not diagnose diseases.
Advise consulting a healthcare professional for emergencies.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text
