from config import client, MODEL_NAME

# ==========================================
# Scan Medicine Image
# ==========================================

def analyze_medicine_image(image, ocr_text=""):

    prompt = f"""
You are an expert pharmacist.

OCR Text:

{ocr_text}

Use BOTH the uploaded medicine image and OCR text.

Provide:

💊 Medicine Name

🧪 Active Ingredient

🏥 Manufacturer

💉 Strength

🩺 Uses

💊 Typical Dosage

⚠️ Common Side Effects

🚫 Contraindications

🔄 Drug Interactions

🍺 Alcohol Interaction

🥛 Food Interaction

🤰 Pregnancy

🤱 Breastfeeding

👶 Pediatric Use

📦 Storage

💵 Approximate Price

📝 Summary

If not confident, clearly say so.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[prompt, image]
    )

    return response.text


# ==========================================
# Medicine Search
# ==========================================

def search_medicine(name):

    prompt = f"""
Give detailed information about:

{name}

Include:

Medicine Name

Active Ingredient

Uses

Dosage

Side Effects

Drug Interactions

Warnings

Storage

Pregnancy

Breastfeeding

Food Interaction

Alcohol Interaction

Approximate Price
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text


# ==========================================
# Drug Interaction
# ==========================================

def drug_interaction(med1, med2):

    prompt = f"""
Check interaction.

Medicine 1:
{med1}

Medicine 2:
{med2}

Return

Risk Level

Reason

Recommendation
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text


# ==========================================
# AI Chat
# ==========================================

def health_chat(question):

    prompt = f"""
You are PillVision AI.

Answer only medicine and healthcare questions.

Question:

{question}

Provide educational guidance only.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text
