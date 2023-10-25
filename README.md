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

### Challenges & Remedies

1. **Computational**:
    - Training a BERT model trains well if we have a dedicated GPU.
        - **Remedy**: Utilized the GPU in Google Colab
    - Preprocessing text of a single document require at least 30 seconds making it infeasible working with 1000s of document
        - **Remedy**: Run the preprocessing task at More Core processor and save the processed text as a .txt file.
2. **OCR Engine Performance**:
    - Input to the model is the text which is extracted using OCR Engine. The more accurate the OCR Engine is, the better the model fine-tuning will be.
        - **Remedy**: Premium OCR Engine like Google Vision OCR performs well and give the result faster as compare to Tesseract OCR Engine which is used in this project.

3. **Data Quality & Quantity**:
    - BERT models require large amounts of data for effective training, and obtaining a substantial, well-labeled dataset can be challenging, especially for specific domains.
        - **Remedy**:
            - **Data Augmentation**: Apply techniques such as synonym replacement to artificially increase the size of your dataset.
            - **Domain-Specific Pretraining**: Consider using domain-specific pretrained BERT models.
4. **Training Challenges**:
    - Training large transformer models like BERT can be time-consuming, especially if the dataset is vast and the model architecture is complex.
        - **Remedy**:
            - **Gradient Accumulation**: simulate training with larger batch sizes without increasing GPU memory requirements significantly.
5. **Fine-Tuning Challenges**:
    - Finding the optimal learning rate, batch size, and number of epochs for fine-tuning BERT can be challenging and time-consuming.
        - **Remedy**: Hyperparameter Tuning with multiple values & Early Stopping.
6. **Label Imbalance**:
    - classes might not be balanced, leading to biased models.
        - **Remedy**: Assign higher weights to minority classes during loss calculation to penalize misclassifications of minority classes more.
        

Feel free to customize the README.md file further to include additional sections, such as Acknowledgments, Troubleshooting, or Contributing guidelines, based on the needs of your project and the intended audience of your GitHub repository.

### Data Source
[Kaggle](https://www.kaggle.com/datasets/ritvik1909/document-classification-dataset)
