<p align="center">
  <a href="https://github.com/BeaverHouse/python-script-hub">
    <img src="logo.png" alt="Logo">
  </a>

  <p align="center">
    Effort to increase productivity by using Python
    <br>
    <br>
    <a href="https://github.com/BeaverHouse/python-script-hub/issues">Bug Report</a>
    |
    <a href="https://github.com/BeaverHouse/python-script-hub/issues">Request to HU-Lee</a>
  </p>

  <p align="center">
    <a href="https://www.python.org/">
      <img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
    </a>
    <a href="https://python-poetry.org/">
      <img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat&logo=Poetry&logoColor=white" alt="Poetry">
    </a>
    <a href="https://docs.pytest.org/en/8.0.x/">
      <img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white" alt="Pytest">
    </a>
    <a href="./LICENSE">
      <img src="https://img.shields.io/github/license/BeaverHouse/python-script-hub" alt="License">
    </a>
  </p>
</p>

<!-- Content -->

<br>

## Description

Effort to increase productivity by using [Python][py].

**Current features**

| **Feature**                          | **Location**                                   |
| :----------------------------------- | :--------------------------------------------- |
| Test LinkedIn profile                | `test/test_docs.py::test_linkedin_profile`     |
| Test blog posts from [my blog][blog] | `test/test_docs.py::test_blog_posts`           |
| README generation                    | `hub.making.readme`                            |
| Test README template                 | `test/test_readme.py::test_readme_template`    |
| Test repository settings\*           | `test/test_repo.py::test_repo_settings`        |
| Test repository README               | `test/test_readme.py::test_repo_readme`        |
| Test repository README sentence      | `test/test_docs.py::test_repo_readme_sentence` |

<sub>\*: GitHub API does not support entire access to its features.</sub>

[py]: https://www.python.org/
[blog]: https://github.com/BeaverHouse/blog

<br>

## Requirements

1. You need to install [Python 3.12][py312] and [Poetry][poetry] to manage the packages.  
   To install Poetry:

   ```
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. You need to set environment variables.  
   If you want to fork the repository and run GitHub Actions, set them as a repository secret too.

   - `GH_PAT_ORGANIZATION` : Fine-grained access token for organization repositories
   - `GH_PAT_PERSONAL` : Fine-grained access token for personal repositories

3. Configure [Codecov][codecov] to make code coverage analysis.  
   Delete the related code if unnecessary.

<br>

**Install packages**

```
poetry install
```

[poetry]: https://python-poetry.org/
[py312]: https://www.python.org/downloads/release/python-3120/
[codecov]: https://about.codecov.io/

<br>

## Getting Started

**Make README**

```
python -m hub.making.readme
```

**Test**

```
python -m pytest --cov test
```

<br>

## Contributing

See the [CONTRIBUTING.md][contributing].

[contributing]: ./CONTRIBUTING.md
