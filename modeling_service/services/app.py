import gradio as gr
import base64
import json
import os
import requests

# URL of the API endpoint
url = "http://0.0.0.0:8000/classify_image"

# Headers for the API request
headers = {
  'Content-Type': 'application/json'
}

def classify(f):
    """
    Classify the given image file into one of the supported classes using BERT model.

    Args:
        f (binary): The image file to classify.

    Returns:
        str: The predicted class of the image file.
    """
    try:
        # Encode the image file to base64 string
        encoded_string = base64.b64encode(f)

        # Prepare the payload for the API request
        payload = json.dumps({"image_base64":str(encoded_string, 'UTF-8')})

        # Send the API request to classify the image
        response = requests.request("POST", url, headers=headers, data=payload)
        api_response = json.loads(response.text)

        # Return the predicted class of the image
        return api_response['predicted_class']
    except Exception as e:
        raise gr.Error("Error in Processing image Document")

# Define the file input for the Gradio interface
file = gr.File(file_count="single", file_types=[".png"],type = 'binary',show_label = False)

# Define the Gradio interface
i1 = gr.Interface(fn = classify, 
                    inputs = file, 
                    outputs = 'text',
                    allow_flagging = 'never'
                    )

# Define the Markdown content for the Gradio interface
i3 = gr.Markdown('''
## Building a Document Classifier using Docker, BERT, and FastAPI

This document classifier application is built using Docker, BERT, and FastAPI. The first service is responsible for converting the image file to a base64 encoded string, while the second service is responsible for classifying the document using BERT model.

The application supports the following classes:
                 
* Resume
* Email
* Scientific Publication

For detailed understanding of the data, visit [kaggle!!](https://www.kaggle.com/datasets/ritvik1909/document-classification-dataset).
                 
It only supports `.png` files.

To run the application, follow these steps:

1. Clone the repository using the following command: `git clone https://github.com/yesdeepakmittal/document-classification-using-bert.git`
2. Navigate to the base directory.
3. Build the Docker image using the following command: `docker build -t document-classifier .`
4. Run the Docker container using the following command: `docker run -itd --rm --name document-classifier-cont -p 8000:8000 -p 1998:1998 document-classifier`

Once the container is running, you can access the application at `http://localhost:1998`.

To classify a document, simply upload a `.png` file and click on the "Classify" button. You can also test the application using the example documents provided in the "Example Documents for Testing" section.

Happy classifying!
''')

# Define the Markdown content for the Gradio interface
i4 = gr.Markdown('''
                 # BERT based Document Classifier Application
                 ''')

# Define the Gradio interface blocks
with gr.Blocks(title = 'Document Classification using BERT') as demo1:
    with gr.Row():
        i4.render()
    with gr.Row():
        with gr.Column():
            i3.render()
    i1.render()
    print(os.path.join(os.getcwd(), "samples/examples"))
    gr.Examples(
        examples = [
                [os.path.join(os.getcwd(), "./modeling_service/samples/examples", f_name)] for f_name in os.listdir("./modeling_service/samples/examples")
                ],
        inputs=[file],
        # outputs=df,
        label = 'Example Documents for Testing'
        )

# Launch the Gradio interface
if __name__ == "__main__":
    demo1.launch(
        debug = True,
        server_port = 1998,
        auth_message = 'Welcome to the Document Classifier Application',
        show_api = False,
        server_name = '0.0.0.0'
        )