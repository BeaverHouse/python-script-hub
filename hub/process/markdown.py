"""Module to process markdown content."""

import re
import logging
import bs4
from markdown.core import markdown
from hub.constant import SPECIAL_ENGLISH_WORDS

def standard_preprocess(content: str) -> str:
    """
    Exclude code blocks, markdown info and comments from the markdown content.

    Args:
        content (str): The markdown content to be processed.
    
    Returns:
        str: The processed markdown content.
    """

    content = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
    content = re.sub(r'---.*?---', '', content, flags=re.DOTALL)
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)

    return content

def custom_preprocess(content: str) -> str:
    """
    Preprocess content by replacing special English words 
    and removing backticks.
    
    Args:
        content (str): The input content to be preprocessed.
        
    Returns:
        str: The preprocessed content.
    """
    content = re.sub(
        r'<span class="exclude">.*?</span>',
        SPECIAL_ENGLISH_WORDS,
        content,
        flags=re.DOTALL
    )
    content = re.sub(r"`.*?`", "", content, flags=re.DOTALL)

    return content

def md_to_text(content: str) -> str:
    """
    Convert markdown content to plain text.

    Args:
        content (str): The markdown content to be converted.

    Returns:
        str: The plain text version of the markdown content.
    """
    html_content = markdown(content)
    return bs4.BeautifulSoup(html_content, features="html.parser").get_text() \
        .strip() \
        .replace('\xa0', ' ')

def codecov_preprocess(content: str) -> str:
    """
    Preprocesses the content by removing any Codecov-related HTML tags.

    Parameters:
    - content: str, the input content to be preprocessed

    Returns:
    - str, the preprocessed content
    """
    content = re.sub(
        r'\s*<a href="https://codecov.io.*?</a>\s',
        "\n",
        content,
        flags=re.DOTALL
    )

    return content


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
            else:
                raise AttributeError(
                    f"Failed to extract caption from line: {line}"
                )

    if len(captions) > 0:
        logging.info("captions: %s", captions)

    return captions
