"""Module to check repository settings."""

import json
from hub.query.graphql import overview_query_template
from hub.util.github_api import get_graphql_response, get_rest_response
from hub.config import ORG_NAME, OWNER

def check_repository_settings(repo: str):
    """
    Function to check the repository settings.

    1. Call GitHub GraphQL API to get repository settings
    2. Assert that:
        - repository name is same
        - repository description is not empty
        - repository follows configured categories
        - If repository has vulnerability alerts disabled:
            - repository is archived and has "Deprecated" category
        - status checks on branch protection is same as configured
        - labels are same as configured
        
    Args:
        repo (str): The repository in the format owner/name.

    Returns:
        None
    """
    owner, name = repo.split("/")

    issue_query = overview_query_template.substitute(owner=owner, name=name)

    issue_response = get_graphql_response(issue_query, org= ORG_NAME in repo)
    repository_info = issue_response["data"]["repository"]
    issue_total_count = repository_info["issues"]["totalCount"]

    with open('assets/json/repo_features.json', 'r', encoding='utf-8') as f:
        repo_config = json.load(f)
    categories = repo_config[repo]

    assert repository_info["name"] == name
    assert repository_info["description"]

    assert repository_info["isTemplate"] == ("Template" in categories)
    assert repository_info["hasWikiEnabled"] == ("Wiki" in categories)
    assert repository_info["hasDiscussionsEnabled"] \
        == ("Discussions" in categories)
    assert repository_info["hasIssuesEnabled"] \
        == ("Deprecated" not in categories or issue_total_count > 0)
    if not repository_info["hasVulnerabilityAlertsEnabled"]:
        assert repository_info["isArchived"] and ("Deprecated" in categories)

    for key in [
        "name",
        "description",
        "isTemplate",
        "hasWikiEnabled",
        "hasDiscussionsEnabled",
        "hasIssuesEnabled",
        "hasVulnerabilityAlertsEnabled",
        "isArchived",
        "issues"
    ]:
        del repository_info[key]

    configured_status_checks = list(filter(
        lambda x: x not in ["Template", "Wiki", "Discussions", "Deprecated"],
        categories
    ))
    protected_rules = repository_info["branchProtectionRules"]["nodes"][0]
    assert sorted(
        [x["context"] for x  \
            in protected_rules["requiredStatusChecks"]]
    ) == sorted(configured_status_checks)
    del protected_rules["requiredStatusChecks"]

    with open('assets/json/graphql_response.json', 'r', encoding='utf-8') as f:
        response_template = json.load(f)

    # Sort labels separately
    repository_info["labels"]["nodes"] \
        = sorted(repository_info["labels"]["nodes"], key=lambda x: x["name"])
    response_template["labels"]["nodes"] \
        = sorted(response_template["labels"]["nodes"], key=lambda x: x["name"])

    assert json.dumps(response_template, sort_keys=True) \
        == json.dumps(repository_info, sort_keys=True)

def check_pull_requests(repo: str):
    """
    Function to check the pull requests for a given repository.

    1. Call GitHub REST API to get pull requests
    2. Assert that:
        - each issue has at least one label
        - each issue's assignee is the owner
        - each issue is locked
        - each issue's active lock reason is resolved

    Args:
        repo (str): The repository in the format owner/name.

    Returns:
        None
    """
    endpoint = f"repos/{repo}/pulls?state=all"

    response = get_rest_response(endpoint, org= ORG_NAME in repo)
    for pr in response:
        assert len(pr["labels"]) > 0, \
            f'{repo} PR #{pr["number"]} has no label'
        assert pr["assignees"][0]["login"] == OWNER, \
            f'{repo} PR #{pr["number"]} is not assigned to {OWNER}'
        assert pr["locked"] is True, \
            f'{repo} PR #{pr["number"]} is not locked'
        assert pr["active_lock_reason"] == "resolved", \
            f'{repo} PR #{pr["number"]} is not resolved'

def check_issues(repo: str, is_ps: bool):
    """
    Function to check the issues in a given repository.

    1. Call GitHub REST API to get issues
    2. Assert that:
        - each issue has at least one label
        - each issue's assignee is the owner
        - each issue is locked
        - each issue's active lock reason is resolved
    3. If the repository is not about PS and the issue is not a pull request:
        - assert that each issue has "Request" label

    Args:
        repo (str): The repository in the format owner/name.
        is_ps (bool): A boolean indicating if the repository is about PS.

    Returns:
        None
    """
    endpoint = f"repos/{repo}/issues?state=all"

    response = get_rest_response(endpoint, org= ORG_NAME in repo)
    for issue in response:
        assert len(issue["labels"]) > 0, \
            f'{repo} Issue #{issue["number"]} has no label'
        assert issue["assignees"][0]["login"] == OWNER, \
            f'{repo} Issue #{issue["number"]} is not assigned to {OWNER}'
        assert issue["locked"] is True, \
            f'{repo} Issue #{issue["number"]} is not locked'
        assert issue["active_lock_reason"] == "resolved", \
            f'{repo} Issue #{issue["number"]} is not resolved'
        if not is_ps and "pull_request" not in issue:
            label_names = list(map(lambda x: x["name"], issue["labels"]))
            assert "Request" in label_names, \
                f'{repo} Issue #{issue["number"]} has no "Request" label'

def check_community_standards(repo: str):
    """
    Function to check the community standards in a given repository.

    1. Call GitHub REST API to get community standards
    2. Assert that:
        - the health percentage is 100
        - the description is not empty
        - the code of conduct is "Contributor Covenant"
        - the license is "MIT License"
        - If the repository is in the organization:
            - the content reports are enabled

    Args:
        repo (str): The repository in the format owner/name.

    Returns:
        None
    """
    profile_response = get_rest_response(
        f"repos/{repo}/community/profile",
        org= ORG_NAME in repo
    )

    assert profile_response["health_percentage"] == 100
    assert len(profile_response["description"]) > 0
    assert profile_response["files"]["code_of_conduct"]["name"] \
        == "Contributor Covenant"
    assert profile_response["files"]["license"]["name"] == "MIT License"

    if ORG_NAME in repo:
        assert profile_response["content_reports_enabled"] is True
