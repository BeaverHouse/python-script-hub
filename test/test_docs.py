import glob
import hub.checking.docs.en as en_docs
from hub.util.files import get_text_from_file

def test_linkedin_profile():
    for file in glob.glob('docs-personal/linkedin/*.md'):
        text = get_text_from_file(file)
        en_docs.check_capitalization_on_content(text)