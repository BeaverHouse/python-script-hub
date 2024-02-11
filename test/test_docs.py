import glob
import os
import shutil
import json
from hub.process.markdown import md_to_text
import hub.checking.docs.en as en_docs
import hub.checking.docs.ko as ko_docs
from hub.util.files import get_text_from_file, get_text_from_url

def test_linkedin_profile():
    for file in glob.glob('docs-personal/linkedin/*.md'):
        text = get_text_from_file(file)
        en_docs.check_capitalization_on_content(text)

def test_blog_posts():
    shutil.rmtree('text/blog', ignore_errors=True)
    os.makedirs('text/blog', exist_ok=True)
    for file in glob.glob('docs-personal/blog/*.md'):
        file_name = file.split(os.sep)[-1].replace('.md', '')
        text = get_text_from_file(file)
        ko_docs.check_english_words(raw_content=text, name=file_name, folder='blog')

def test_wiki_posts():
    shutil.rmtree('text/wiki', ignore_errors=True)
    os.makedirs('text/wiki', exist_ok=True)
    for file in glob.glob('docs-personal/wiki/*.md'):
        file_name = file.split(os.sep)[-1].replace('.md', '')
        text = get_text_from_file(file)
        ko_docs.check_english_words(raw_content=text, name=file_name, folder='wiki')

def test_repo_readme_sentence():
    with open('hub/making/jinja_template/repository.json', 'r') as f:
        repo_config: dict = json.load(f)
    for repo in repo_config.keys():
        if repo == "template":
            continue
        _, name = repo.split("/")
        readme_sentences = get_text_from_file(f'docs-personal/readme-sentence/{name}.md').split('\n')
        online_content = get_text_from_url(f'https://raw.githubusercontent.com/{repo}/main/README.md')
        online_text = md_to_text(online_content)
        for sentence in readme_sentences:
            assert sentence in online_text
            en_docs.check_capitalization(sentence)