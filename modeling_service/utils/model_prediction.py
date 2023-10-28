from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Path to the best model
best_model_path = "modeling_service/samples/bert_document_classification_model_lr5e-05_Adam.pt"

# Load the model from the local file path
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=3)
model.load_state_dict(torch.load(best_model_path, map_location=torch.device('cpu')))

# Set the model in evaluation mode
model.eval()

# Load the tokenizer from 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

class_to_label = {'scientific_publication': 0, 'email': 1, 'resume': 2}
label_to_class = {v: k for k, v in class_to_label.items()}

# Function to predict document class
def predict_document_class(text):
    inputs = tokenizer(text, padding=True, truncation=True, return_tensors='pt')
    input_ids = inputs.input_ids
    attention_mask = inputs.attention_mask

    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask)
        logits = outputs.logits

    predicted_class = torch.argmax(logits, dim=1).item()
    return label_to_class[predicted_class]