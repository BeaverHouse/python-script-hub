from ...process.markdown import *
from ...constant import SPECIAL_ENGLISH_WORDS
import uuid
import pandas as pd
import logging

def check_invalid_english(content: str):
    words_data = pd.read_csv("words.csv")
    valid_words = list(words_data.iloc[:, 0])
    valid_words.sort(key=len, reverse=True)

    for word in valid_words:
        content = content.replace(word, SPECIAL_ENGLISH_WORDS)

    english_words = re.findall(r"[a-zA-Z]+", content)  
    invalid_words = set(english_words) - {SPECIAL_ENGLISH_WORDS}

    if len(invalid_words) > 0:
        logging.error("invalid:", invalid_words)

    assert not invalid_words

def check_english_words(raw_content: str, name: str, is_hugo: bool = False) -> bool:
    
    # Preprocess
    content = standard_preprocess(raw_content)
    if is_hugo:
        image_captions = get_hugo_image_captions(content)
        content = hugo_preprocess(content)
    
    # Preserve raw text
    preserved_text = md_to_text(content)
    
    # Then process other words
    full_preprocessed_content = custom_preprocess(content)
    full_preprocessed_text = md_to_text(full_preprocessed_content)
    
    check_invalid_english(full_preprocessed_text)
    for caption in image_captions:
        check_invalid_english(caption)
    
    with open(f'text/{name}-{uuid.uuid4()}.md', "w", encoding="utf-8") as f:
        f.write(preserved_text)
        f.write("\n\n")
        for caption in image_captions:
            f.write(caption)
            f.write("\n")