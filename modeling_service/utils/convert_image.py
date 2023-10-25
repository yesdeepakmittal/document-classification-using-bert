import base64
import io
from PIL import Image

def convert_image(image_base64: str) -> Image:
    # Decode base64 image
    image_data = base64.b64decode(image_base64)
    
    # Open image using PIL
    image = Image.open(io.BytesIO(image_data))
    
    # Convert image to PNG format
    image = image.convert("RGB")
    png_image = io.BytesIO()
    image.save(png_image, format="PNG")
    
    # Reset the buffer to the beginning to read the image
    png_image.seek(0)
    
    return Image.open(png_image)