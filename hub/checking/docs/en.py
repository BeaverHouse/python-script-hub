import nltk
from ...constant import SPECIAL_ENGLISH_WORDS_ENG
import pandas as pd
    
def extract_sentences(content: str):
    nltk.download("punkt")
    return nltk.sent_tokenize(content)

def check_capitalization(sentence: str):
    words_data = pd.read_csv("words.csv")
    valid_words = list(words_data.iloc[:, 0])
    valid_words.sort(key=len, reverse=True)

    for word in valid_words:
        sentence = sentence.replace(word, SPECIAL_ENGLISH_WORDS_ENG)

    words = sentence.split()

    # 1. Words that start with uppercase letters
    # 2. exclude "I"
    # 3. exclude first word
    capitalized_words = sum([
        word[0].isupper() and word != "I" and not word.startswith('I\'') and idx > 0
        for idx, word in enumerate(words)
    ])
    
    assert capitalized_words == 0

def check_capitalization_on_content(raw_content: str) -> bool:
    sentences = extract_sentences(raw_content)
    for sentence in sentences:
        check_capitalization(sentence)