import jinja2
import json
import sys
import os
from ..config import ORG_NAME
from ..query.graphql import readme_query_template
from ..util.files import get_text_from_file
from ..util.github_api import get_graphql_response

def make_readme(repo: str):
    if repo == "template":
        name = "template"
        repository_info = {"description": "Template for HU-Lee's repositories", "homepageUrl": "https://example.com"}
    else:
        owner, name = repo.split("/")
        issue_query = readme_query_template.substitute(owner=owner, name=name)
        
        issue_response = get_graphql_response(issue_query, org= ORG_NAME in repo)
        repository_info = issue_response["data"]["repository"]

    with open('hub/making/jinja_template/repository.json', 'r') as f:
        repo_config = json.load(f)
    stacks = repo_config[repo]
    
    template = jinja2.Template(get_text_from_file('hub/making/jinja_template/README-template.md'))
    
    rendered_readme = template.render(
        repo=repo,
        description=repository_info["description"], 
        homepage=repository_info["homepageUrl"],
        markdown = "Markdown" in stacks,
        yaml = "YAML" in stacks,
        python = "Python" in stacks,
        pytest = "Pytest" in stacks,
        pandas = "pandas" in stacks,
        poetry = "Poetry" in stacks,
        react = "React" in stacks,
        typescript = "TypeScript" in stacks,
        eslint = "ESLint" in stacks,
        yarn = "Yarn" in stacks
    )

    with open(f'result/readme/{name}.md', 'w+', encoding='utf-8') as readme:
        readme.write(rendered_readme)

if __name__ == '__main__':
    os.makedirs('result/readme', exist_ok=True)
    try:
        repo = sys.argv[1]
    except IndexError:        
        repo = input("Enter the repository name: ")
    make_readme(repo=repo)