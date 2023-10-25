from fastapi import FastAPI, Request
from typing import Dict

from modeling_service.utils.convert_image import convert_image
from modeling_service.utils.data_preprocessing import preprocess_text
from modeling_service.utils.model_prediction import predict_document_class
from modeling_service.utils.ocr import get_text

app = FastAPI()

@app.post("/convert_image")
async def make_prediction(request: Request):
    try:
        input_json: Dict = eval((await request.body()).decode())
        image_base64: str = input_json["image_base64"]
        
        # Convert image
        image = convert_image(image_base64)

        # Get OCR text
        text = get_text(image)
        
        # Get preprocessed text
        preprocessed_text = preprocess_text(text)
        print(preprocessed_text)

        # Predict the document class
        # predicted_class = predict_document_class(preprocessed_text)
        # print(predicted_class)
        
    except:
        print("Exception hit!!")

    