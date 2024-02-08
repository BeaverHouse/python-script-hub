Description
Data & processing code for AE Check.
It is processed manually and migrated to frontend repository.

Timeline

2022.09 ~ 2023.09
v2 code
2023.09 ~ 2024.02
add v3 code, auto-migrate data
2024.02 ~
delete v2 code, clean repository
Data source

Raw app data
Seesaa wiki
AE wiki
altema.jp

Requirements
You need to install Python 3.12 and Poetry to manage the packages.
To install Poetry:

curl -sSL https://install.python-poetry.org | python3 -
You need to set repository secret to run GitHub Actions.

Fine-grained access token for organization repositories

Install packages

poetry install

File description
step0.py
It imports personality data from Seesaa wiki.
step1.py
It adds the missing i18n tags.
step2.py
It processes the JSON files & images, then saves to result folder.
result/updates.tsx
It includes some configs and announcement formats used in frontend.
