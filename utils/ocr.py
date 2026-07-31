import easyocr
import numpy as np
from PIL import Image

# ==========================================
# Initialize OCR Reader
# ==========================================

reader = easyocr.Reader(
    ['en'],
    gpu=False
)

# ==========================================
# Extract Text From Image
# ==========================================

def extract_text(image):

    try:

        # Convert PIL image to NumPy array
        if isinstance(image, Image.Image):
            image = np.array(image)

        results = reader.readtext(image)

        extracted_text = ""

        for result in results:
            extracted_text += result[1] + "\n"

        return extracted_text.strip()

    except Exception as e:

        return f"OCR Error: {e}"


# ==========================================
# Check if Text Exists
# ==========================================

def has_text(image):

    text = extract_text(image)

    return len(text.strip()) > 0


# ==========================================
# Get OCR Lines
# ==========================================

def extract_lines(image):

    try:

        if isinstance(image, Image.Image):
            image = np.array(image)

        results = reader.readtext(image)

        lines = []

        for result in results:
            lines.append(result[1])

        return lines

    except:

        return []


# ==========================================
# Get Full OCR Information
# ==========================================

def get_ocr_data(image):

    try:

        if isinstance(image, Image.Image):
            image = np.array(image)

        results = reader.readtext(image)

        data = []

        for result in results:

            data.append({
                "text": result[1],
                "confidence": round(result[2], 2)
            })

        return data

    except:

        return []
