import re
import string
import contractions
from spellchecker import SpellChecker
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import pos_tag

# Download NLTK resources
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


'''
The pos_tag function returns Part-of-Speech tags in the form of Penn Treebank POS tags, 
but the WordNetLemmatizer in NLTK expects WordNet POS tags and then perform lemmatization
'''
# Map Penn Treebank POS tags to WordNet POS tags for lemmatization
def penn_to_wordnet_pos(pos_tag):
    if pos_tag.startswith('J'):
        return wordnet.ADJ
    elif pos_tag.startswith('V'):
        return wordnet.VERB
    elif pos_tag.startswith('N'):
        return wordnet.NOUN
    elif pos_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # default to noun if POS tag is unknown

def preprocess_text(text):
    if text is None or not text.strip():
        print("Empty Text found")
        return "" 

    # Replace '\n' with whitespace
    text = text.replace('\n', ' ')
    
    # Lowercasing
    text = text.lower()
    
    # Fix contractions
    text = contractions.fix(text)
    
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenization
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    
    # Spelling correction
    spell = SpellChecker()
    corrected_tokens = [spell.correction(word) for word in tokens]
    # print(corrected_tokens)
    corrected_tokens = [word for word in corrected_tokens if word is not None]
    # print(corrected_tokens)
    

    # Part-of-Speech Tagging and Lemmatization
    pos_tags = pos_tag(corrected_tokens)
    lemmatizer = WordNetLemmatizer()

    # tokens = []
    # for word,pos in pos_tags:
    #     try:
    #         print(lemmatizer.lemmatize(word, pos=pos))
    #         tokens.append(lemmatizer.lemmatize(word, pos=pos))
    #     except:
    #         print("Exception",word, pos)
    # tokens = [lemmatizer.lemmatize(word, pos=pos) for word, pos in pos_tags]
    tokens = [lemmatizer.lemmatize(word, pos=penn_to_wordnet_pos(pos_tag)) for word, pos_tag in pos_tags]
    # print(tokens)

    
    # Rejoin tokens into text
    preprocessed_text = ' '.join(tokens)
    
    return preprocessed_text