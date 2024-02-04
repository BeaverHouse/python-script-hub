import json
from hub.checking.repo_settings import check_repository_settings

def test_repo_settings():
    with open('hub/checking/json/repo_categories.json', 'r') as f:
        repo_config: dict = json.load(f)
    for repo in repo_config.keys():
        check_repository_settings(repo)