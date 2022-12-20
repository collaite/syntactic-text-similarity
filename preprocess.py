import re
from nltk.tokenize import word_tokenize, sent_tokenize
import string
from text_preprocessing import preprocess_text
from text_preprocessing import to_lower, remove_number, remove_itemized_bullet_and_numbering, remove_special_character, remove_punctuation, remove_whitespace, normalize_unicode

def preprocess_c(corpus, stopwords):
    preprocess_functions = [to_lower, remove_number, remove_itemized_bullet_and_numbering, remove_special_character, remove_punctuation, normalize_unicode]
    
    preprocessed_text = preprocess_text(corpus, preprocess_functions)
    
    tokens = word_tokenize(preprocessed_text)
    
    without_stopwords = [w for w in tokens if not w in stopwords]
    
    return without_stopwords