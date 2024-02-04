import requests

def get_text_from_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read().strip()
    
def get_text_from_url(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    return response.text.strip()