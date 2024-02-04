import requests
import dotenv
import platform
import os

if platform.system() in ["Windows", "Darwin"]:
    dotenv.load_dotenv(dotenv_path=".env.python-script-hub")

GH_PAT_ORGANIZATION = os.getenv('GH_PAT_ORGANIZATION')
GH_PAT_PERSONAL = os.getenv('GH_PAT_PERSONAL')

def get_headers(is_organization: bool):
    access_token = (GH_PAT_ORGANIZATION if is_organization else GH_PAT_PERSONAL)
    return {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github.v3+json",
    }

def get_graphql_response(query: str, org: bool) -> dict:
    url = "https://api.github.com/graphql"

    response = requests.post(url=url, json={"query": query}, headers=get_headers(org))
    response.raise_for_status()

    return response.json()