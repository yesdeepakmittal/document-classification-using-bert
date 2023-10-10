# Document Classification with OCR and BERT
### Overview
Document Classification with OCR and BERT is a project aimed at automatically categorizing textual images into predefined classes. This repository contains the code and resources necessary to train a powerful document classification model leveraging Optical Character Recognition (OCR) and the Bidirectional Encoder Representations from Transformers (BERT) algorithm.

### Project Highlights
- **Automated Document Classification**: Classify textual images into categories without manual intervention, enabling efficient sorting and organization of large document datasets.

- **OCR Integration**: Utilize Tesseract OCR, a popular open-source text recognition engine, to extract textual content from images, enabling the model to work with image-based documents.

- **BERT-based Document Understanding**: Leverage BERT, a state-of-the-art language model, to understand the context and semantics of extracted text, improving the accuracy of document classification.

- **Flexibility and Customization**: Adapt the project to your specific use case by easily modifying the number of classes, training data, and model architecture.

### How it Works
- **Text Extraction with Tesseract OCR**:

  - Images containing textual content are processed using Tesseract OCR to extract the text.
  - Extracted text is preprocessed and tokenized for further analysis.
  
- **BERT Model Training**:
  - Preprocessed text data and corresponding labels are used to train a BERT-based document classification model.
  - The model learns to classify documents into predefined categories.
    
- **Inference and Classification**:
  - Trained model is utilized to classify new textual images into appropriate classes.
  - Predictions enable automated sorting and organization of documents based on their content.

### Prerequisites
  - Python 3.x
  - Libraries: transformers, torch, pytesseract, PIL
  - Tesseract OCR Installed

### Usage
- **Clone the Repository**:
```git clone https://github.com/yesdeepakmittal/document-classification-using-bert.git```

- **Train the model using Jupyter Notebook**
- **Build a FastAPI/Flask Application for Model Serving**

Feel free to customize the README.md file further to include additional sections, such as Acknowledgments, Troubleshooting, or Contributing guidelines, based on the needs of your project and the intended audience of your GitHub repository.

### Data Source
[Kaggle](https://www.kaggle.com/datasets/ritvik1909/document-classification-dataset)
