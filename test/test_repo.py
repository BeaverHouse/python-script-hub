import json
import os
from hub.checking.repo_settings import check_repository_settings
from hub.making.readme import make_readme
from hub.util.files import get_text_from_file, get_text_from_url

def test_readme_template():
    os.makedirs('result/readme', exist_ok=True)
    make_readme("template")
    assert get_text_from_file('result/readme/template.md') \
        .replace("https://example.com", "") \
        .replace("template", "BeaverHouse/repo-template") \
        == get_text_from_url('https://raw.githubusercontent.com/BeaverHouse/repo-template/main/README-template.md')

def test_repo_settings():
    with open('assets/json/repo_features.json', 'r') as f:
        repo_config: dict = json.load(f)
    for repo in repo_config.keys():
        check_repository_settings(repo)