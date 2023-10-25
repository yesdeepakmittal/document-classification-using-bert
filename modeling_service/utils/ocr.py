import pytesseract

def get_text(img):
    return pytesseract.image_to_string(img)