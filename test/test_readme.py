import os
from hub.making.readme import make_readme
from hub.util.files import get_text_from_file, get_text_from_url

def test_readme_template():
    os.makedirs('result/readme', exist_ok=True)
    make_readme("template")
    assert get_text_from_file('result/readme/template.md') \
        .replace("https://example.com", "") \
        .replace("template", "BeaverHouse/repo-template") \
        == get_text_from_url('https://raw.githubusercontent.com/BeaverHouse/repo-template/main/README-template.md')