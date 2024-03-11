"""Module to store utility functions for GitHub API."""

import platform
import os
import requests
import dotenv

if platform.system() in ["Windows", "Darwin"]:
    dotenv.load_dotenv(dotenv_path=".env.python-script-hub")

GH_PAT_ORGANIZATION = os.getenv('GH_PAT_ORGANIZATION')
GH_PAT_PERSONAL = os.getenv('GH_PAT_PERSONAL')

def get_headers(is_org: bool) -> dict:
    """
    Function to get headers based on organization flag.

    Args:
        is_org (bool): Flag indicating if the request is for an organization.

    Returns:
        dict: A header containing the Authorization and Accept headers.
    """
    access_token = (GH_PAT_ORGANIZATION if is_org else GH_PAT_PERSONAL)
    return {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github.v3+json",
    }

def get_graphql_response(query: str, org: bool) -> dict:
    """
    Get the response from a GitHub GraphQL API.

    Args:
        query (str): The GraphQL query string.
        org (bool): Flag indicating if the request is for an organization.

    Returns:
        dict: The JSON response from the GitHub GraphQL API.
    """
    url = "https://api.github.com/graphql"

    response = requests.post(
        url=url,
        json={"query": query},
        headers=get_headers(org),
        timeout=20
    )
    response.raise_for_status()

    return response.json()

def get_rest_response(endpoint: str, org: bool) -> dict:
    """
    Get the response from a GitHub REST API endpoint.

    Args:
        endpoint (str): The endpoint of the GitHub REST API.
        org (bool): Flag indicating if the request is for an organization.

    Returns:
        dict: The JSON response from the GitHub REST API.
    """
    url = f"https://api.github.com/{endpoint}"

    headers = get_headers(org)
    headers["Accept"] = "application/vnd.github+json"

    response = requests.get(url=url, headers=headers, timeout=15)
    response.raise_for_status()

    return response.json()
