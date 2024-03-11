"""Module to process markdown content."""

import re

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
