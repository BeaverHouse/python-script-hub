import json
from ..query.graphql import overview_query_template
from ..util.github_api import get_graphql_response
from ..config import ORG_NAME

def check_repository_settings(repo: str):    
    owner, name = repo.split("/")

    issue_query = overview_query_template.substitute(owner=owner, name=name)
    
    issue_response = get_graphql_response(issue_query, org= ORG_NAME in repo)
    repository_info = issue_response["data"]["repository"]
    issue_total_count = repository_info["issues"]["totalCount"]

    with open('hub/checking/json/repo_categories.json', 'r') as f:
        repo_config = json.load(f)
    categories = repo_config[repo]
    
    assert repository_info["name"] == name
    assert repository_info["description"]

    assert repository_info["isTemplate"] == ("Template" in categories)
    assert repository_info["hasWikiEnabled"] == ("Wiki" in categories)
    assert repository_info["hasDiscussionsEnabled"] == ("Discussions" in categories)
    assert repository_info["hasIssuesEnabled"] == ("Deprecated" not in categories or issue_total_count > 0)
    
    for key in ["name", "description", "isTemplate", "hasWikiEnabled", "hasDiscussionsEnabled", "hasIssuesEnabled"]:
        del repository_info[key]

    requiredStatusChecks = list(filter(
        lambda x: x not in ["Template", "Wiki", "Discussions", "Deprecated"], 
        categories
    ))
    assert sorted(
        [x["context"] for x in repository_info["branchProtectionRules"]["nodes"][0]["requiredStatusChecks"]]
    ) == sorted(requiredStatusChecks)
    del repository_info["branchProtectionRules"]["nodes"][0]["requiredStatusChecks"]

    del repository_info["issues"]


    with open('hub/checking/json/graphql_response.json', 'r') as f:
        response_template = json.load(f)
    
    # Sort labels separately
    repository_info["labels"]["nodes"] = sorted(repository_info["labels"]["nodes"], key=lambda x: x["name"])
    response_template["labels"]["nodes"] = sorted(response_template["labels"]["nodes"], key=lambda x: x["name"])
    
    assert json.dumps(response_template, sort_keys=True) == json.dumps(repository_info, sort_keys=True)