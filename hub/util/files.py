"""Module to store utility functions for files."""

import requests

def get_text_from_file(file_path: str) -> str:
    """
    Reads text data from the specified file path and returns the content as a string.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The text content of the file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read().strip()

def get_text_from_url(url: str) -> str:
    """
    Retrieves text content from the provided URL and returns it as a string.
    
    Args:
        url (str): The URL from which to retrieve the text content.
        
    Returns:
        str: The text content retrieved from the URL.
    """
    response = requests.get(url=url, timeout=15)
    response.raise_for_status()

    return response.text.strip()
