import os
import json
from hub.process.markdown import codecov_preprocess
from hub.making.readme import make_readme
from hub.util.files import get_text_from_file, get_text_from_url

CONTENT_COMMENT = "<!-- Content -->"

def test_repo_readme():
    os.makedirs('result/readme', exist_ok=True)
    with open('assets/json/repo_stacks.json', 'r') as f:
        repo_config: dict = json.load(f)
    for repo, categories in repo_config.items():
        if repo == "template":
            continue
        _, name = repo.split("/")

        # Make README skeleton & get content
        make_readme(repo)
        template_content = get_text_from_file(f'result/readme/{name}.md')
        content_prefix = (template_content.split(CONTENT_COMMENT)[0] + CONTENT_COMMENT).strip()
        content_suffix = template_content.split(CONTENT_COMMENT)[1].strip()

        # Check prefix and suffix
        online_content = get_text_from_url(f'https://raw.githubusercontent.com/{repo}/main/README.md')
        if "Codecov" in categories:
            online_content = codecov_preprocess(online_content)
        assert online_content.startswith(content_prefix) 
        assert online_content.endswith(content_suffix)