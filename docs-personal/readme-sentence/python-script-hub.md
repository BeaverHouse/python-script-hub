Description
Effort to increase productivity by using Python.

Current features

Test LinkedIn profile
Test blog posts from my blog
README generation
Test README template
Test repository settings*
Test repository README
Test repository README sentence
*: GitHub API does not support entire access to its features.

Requirements
You need to install Python 3.12 and Poetry to manage the packages.
To install Poetry:

curl -sSL https://install.python-poetry.org | python3 -
You need to set environment variables.
If you want to fork the repository and run GitHub Actions, set them as a repository secret too.

Fine-grained access token for organization repositories
Fine-grained access token for personal repositories
Configure Codecov to make code coverage analysis.
Delete the related code if unnecessary.

Install packages

poetry install

Make README

python -m hub.making.readme
Test

python -m pytest --cov test