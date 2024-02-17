import glob
import os
import shutil
import json
from hub.process.markdown import md_to_text, codecov_preprocess
import hub.checking.docs.en as en_docs
import hub.checking.docs.ko as ko_docs
from hub.making.readme import make_readme
from hub.util.files import get_text_from_file, get_text_from_url

CONTENT_COMMENT = "<!-- Content -->"

def test_linkedin_profile():
    for file in glob.glob('docs-personal/linkedin/*.md'):
        text = get_text_from_file(file)
        en_docs.check_capitalization_on_content(text)

def test_disquiet_profile():
    shutil.rmtree('text/disquiet', ignore_errors=True)
    os.makedirs('text/disquiet', exist_ok=True)
    for file in glob.glob('docs-personal/disquiet/*.md'):
        file_name = file.split(os.sep)[-1].replace('.md', '')
        text = get_text_from_file(file)
        ko_docs.check_english_words(raw_content=text, name=file_name, folder='disquiet')

def test_peerlist_profile():
    for file in glob.glob('docs-personal/peerlist/*.md'):
        readme_sentences = get_text_from_file(file).split('\n')
        for sentence in readme_sentences:
            en_docs.check_capitalization(sentence)

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

def test_repo_readme():
    os.makedirs('result/readme', exist_ok=True)
    with open('assets/json/repo_stacks.json', 'r') as f:
        repo_config: dict = json.load(f)
    for repo, categories in repo_config.items():
        if repo == "template":
            continue
        make_readme(repo)
        _, name = repo.split("/")
        template_content = get_text_from_file(f'result/readme/{name}.md')
        readme_sentences = get_text_from_file(f'docs-personal/readme-sentence/{name}.md').split('\n')
        content_prefix = (template_content.split(CONTENT_COMMENT)[0] + CONTENT_COMMENT).strip()
        content_suffix = template_content.split(CONTENT_COMMENT)[1].strip()

        online_content = get_text_from_url(f'https://raw.githubusercontent.com/{repo}/main/README.md')
        if "Codecov" in categories:
            online_content = codecov_preprocess(online_content)
        assert online_content.startswith(content_prefix) 
        assert online_content.endswith(content_suffix)

        online_text = md_to_text(online_content)
        for sentence in readme_sentences:
            assert sentence in online_text
            en_docs.check_capitalization(sentence)