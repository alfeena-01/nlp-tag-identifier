import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

# Download required NLTK resources (only needed once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def clean_text(text):
    """
    Tokenize, remove stopwords/punctuation, and lemmatize words.
    Returns a list of cleaned tokens.
    """
    tokens = nltk.word_tokenize(text.lower())
    sr = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    
    clean_tokens = [
        lemmatizer.lemmatize(token)
        for token in tokens
        if token not in sr and token not in string.punctuation and token.isalpha()
    ]
    return clean_tokens
