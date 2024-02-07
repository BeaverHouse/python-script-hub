import glob
import os
import hub.checking.docs.en as en_docs
import hub.checking.docs.ko as ko_docs
from hub.util.files import get_text_from_file

def test_linkedin_profile():
    for file in glob.glob('docs-personal/linkedin/*.md'):
        text = get_text_from_file(file)
        en_docs.check_capitalization_on_content(text)

def test_blog_posts():
    os.makedirs('text/blog', exist_ok=True)
    for file in glob.glob('docs-personal/blog/*.md'):
        file_name = file.split('\\')[-1].replace('.md', '')
        text = get_text_from_file(file)
        ko_docs.check_english_words(raw_content=text, name=file_name, is_hugo=True)