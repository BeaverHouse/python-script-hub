# Obsidian 노트를 MkDocs로 배포하기

[Obsidian](https://obsidian.md/)은 그 자체로도 강력한 도구이지만,<br>여기서 더 나아가 Obsidian 노트를 거의 수정을 거치지 않고 사이트로 배포할 수 있습니다.

가장 잘 알려진 방법은 [MkDocs](https://www.mkdocs.org/)를 사용하는 것입니다.<br>**이 사이트도 Obsidian + MkDocs를 사용하였습니다.**

<sup>이 문서는 하나의 예시일 뿐입니다.<br>GitLab이 아닌 다른 환경에서 배포도 가능하고, Hugo를 사용하는 경우도 있습니다.</sup>

아래는 폴더 구조입니다. 매우 간단합니다.

![](img/folder.png)

## 파일 설명

#### <span class="exclude">Wiki</span> **폴더**
Obsidian에서 사용하는 <span class="exclude">Vault</span>를 그대로 가져다 놓으면 됩니다.<br>설정 파일까지 통째로 옮겨도 상관없습니다.

#### <span class="exclude">`requirements.txt`</span>
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) 테마를 사용하겠습니다.<br>다음 명령어로 패키지를 설치합니다.

```
pip install mkdocs-material
```

추가 플러그인을 설치하는 것은 자유입니다.<br>패키지 목록은 아래 명령어로 <span class="exclude">`requirements.txt`</span> 파일에 저장합니다.

```
pip freeze > requirements.txt
```


#### <span class="exclude">`mkdocs.yml`</span>
MkDocs 설정 파일입니다.<br>아래는 기본적인 다크 모드만 적용한 간단한 예시 설정입니다.<br>추가 플러그인은 [공식 문서](https://squidfunk.github.io/mkdocs-material/)를 참고하여 자유롭게 설정하시면 됩니다.

```yaml title="mkdocs.yml"
site_name: Obsidian test
site_url: https://example.com
site_dir: public
docs_dir: ./wiki        # Your Obsidian directory

theme:
  language: ko          # Language
  name: material        # Material theme
  palette:              # Dark mode
    - media: "(prefers-color-scheme: light)"
      scheme: default
      toggle:
        icon: material/weather-night
        name: Switch to dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      toggle:
        icon: material/weather-sunny
        name: Switch to light mode
```

#### <span class="exclude">`.gitlab-ci.yml`</span>
GitLab CI 설정 파일입니다.<br>저는 공개 소스는 GitHub에 두고, Obsidian을 포함한 개인 소스는 GitLab에 두고 있어서 이렇게 했는데, GitHub에서 GitHub Actions을 사용하여 배포할 수도 있습니다.<br>저의 경우 기본적으로 일정 시간마다 배포가 되고, 수동 배포도 할 수 있도록 설정하였습니다.

```yaml title=".gitlab-ci.yml"
image: python:3.12.1

pages:
  stage: deploy
  script:
    - pip install -r requirements.txt
    - mkdocs build --strict --verbose
  artifacts:
    paths:
      - public
  rules:
    - if: $CI_PIPELINE_SOURCE == "schedule"
    - when: manual
```

## 사이트 확인

다음 명령어로 사이트를 로컬에서 확인할 수 있습니다.

```
mkdocs serve
```

![](img/mkdocs-local.png)


## 사이트 업데이트

소스를 Repository에 올려놓은 상태에서 [Obsidian Git](https://github.com/denolehov/obsidian-git) 플러그인을 사용할 경우 작성한 파일이 자동으로 동기화(<span class="exclude">Commit/Push</span>)되기 때문에 수정과 업데이트가 아주 간편합니다.<br>다른 곳에서 작성한 파일도 <span class="exclude">Vault</span>로 복사해 오면 바로 페이지로 제작할 수 있고, 배포 스케줄까지 설정해 주면 사이트 작업을 반자동화할 수 있습니다.


## 참고 자료

- [<span class="exclude">Publishing Obsidian.md notes with GitLab Pages</span>](https://about.gitlab.com/blog/2022/03/15/publishing-obsidian-notes-with-gitlab-pages/)
- [<span class="exclude">Obsidian GitHub</span> 배포 템플릿](https://github.com/jobindjohn/obsidian-publish-mkdocs)