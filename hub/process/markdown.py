import re
from ..constant import SPECIAL_ENGLISH_WORDS
import markdown
import bs4
import logging

def standard_preprocess(content: str) -> str:
    """Preprocess for all markdown files"""
    # Exclude code blocks
    content = re.sub(r"```[\w\W]*```", "", content, flags=re.DOTALL)
    
    # Exclude markdown info
    content = re.sub(r'---.*?---', '', content, flags=re.DOTALL)

    # Exclude comments
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)

    return content

def custom_preprocess(content: str) -> str:
    """Exclude custom exceptions"""
    content = re.sub(r'<span class="exclude">.*?</span>', SPECIAL_ENGLISH_WORDS, content, flags=re.DOTALL)
    
    return content

def md_to_text(content: str) -> str:
    html_content = markdown.markdown(content)
    return bs4.BeautifulSoup(html_content, features="html.parser").get_text().strip()



##################################################
#                    HUGO 특화
##################################################

def hugo_preprocess(content: str) -> str:
    """Process Hugo expressions"""

    # Exclude Hugo shortcodes
    content = re.sub(r'{{<.*?>}}', '', content, flags=re.DOTALL)

    return content

def get_hugo_image_captions(content: str) -> list[str]:
    """Get Hugo image captions (Custom)"""   
    pattern = r'caption="(.+?)"'
    captions = []

    for line in content.split("\n"):
        if "< zoomimg" in line:
            match = re.search(pattern, line)
            if match:
                captions.append(match.group(1))

    if len(captions) > 0:
        logging.info("captions:", captions)

    return captions