---
slug: 240131-01
title: 생산성 올리기 (1) - Obsidian과 개인 위키
date: 2024-01-31T00:00:00+09:00
weight: 50
tags: ["MkDocs", "Obsidian", "Documentation"]
contributors: ["HU-Lee"]
---

최근에 저를 돌아보고, 생각과 지식을 정리하기 위해 문서화에 많은 관심을 가지고 있습니다.
하지만 최근 작업 방식이 매우 비효율적이고, 이로 인해 다른 일들까지 영향을 받고 있다는 생각이 들었습니다.

그래서 문서화 작업에 대한 개인적인 기준을 세우고, 이에 대한 테스팅과 공수 최소화 등을 통해 생산성을 높이려 합니다. 여기서 이야기할 내용은 그 첫 번째 작업입니다.

<br>

### 새로운 도구, [Obsidian][obsidian]

기존에는 거의 기본 기능만 있는 [Markor][markor]라는 앱을 사용하고 있었는데,
여러 가지를 찾아본 후 Obsidian을 사용하기 시작했습니다. 마음에 들었던 점은 다음과 같습니다.

- 완전히 개인을 위해 환경이 분리되어 있습니다.
- 로컬 파일 기반으로 자료를 보존할 수 있습니다.
- 플러그인을 직접 만들고, 공유할 수 있어 추가 결제 없이도 활용성이 매우 높습니다.

아직 적응 중이지만 마크다운은 이제 많이 익숙해졌고, UI도 깔끔해서 만족스럽게 사용하고 있습니다. macOS•Windows•모바일 모두 사용 가능한 것도 좋습니다.

<br>

### Obsidian + MkDocs로 간편하게 위키 만들기

단순히 Obsidian을 사용하는 것만으로도 생산성이 상당히 올라갔다고 느꼈습니다.  
하지만 더 나아가 Obsidian에서 작성한 파일을 그대로 사이트로 배포하고 싶었습니다.

궁극적으로 **블로그는 생각과 경험 위주**로 하고, **지식과 코드를 저장하는 곳을 따로** 두고 싶었습니다.
큰 주제는 Dive to Argo처럼 따로 문서를 제작할 때도 있지만, 틈틈이 배우는 소소한 지식들을 최대한 적은 공수를 통해 모아 두는 것이 목적이었습니다.

조사해 보니 Obsidian을 [MkDocs][mkdocs]로 배포하는 것이 가장 일반적이었습니다.
[GitLab의 가이드][gitlab-guide]를 따라 거의 그대로 진행했습니다. 다만 다크 모드를 포함한 테마 추가 설정을 하고 싶어서 그 부분은 [공식 문서][docs]를 참고했습니다.

그대로 GitLab Pages에 배포를 했습니다.
PC에서 편집할 때는 소스를 <span class="exclude">Clone</span> 받아 <span class="exclude">Vault</span> 폴더를 열면 Obsidian Git 동기화까지 작동하는 것을 확인했습니다. 작성 내용이 자동으로 동기화되고, CI/CD 스케줄까지 추가하면 사이트 업데이트까지 자동으로 이루어지게 됩니다.

모바일에서 작업한 파일도 PC로 옮겨 약간의 수정을 거치면 바로 하나의 페이지가 됩니다. 어디에서나 지식을 쌓아 두었다가 바로 배포할 수 있는 셈입니다.

<br>

### 후기

배포한 페이지는 도메인까지 설정해 두었습니다.  
아직 내용은 많지 않지만, 천천히 추가해 나가면 될 것이고 작성한 내용을 별도의 추가 작업 없이 배포할 수 있어 공수가 크게 줄어들 것 같습니다.
그리고 GitLab으로 처음 배포를 진행했는데, 비공개 소스를 유지한 채로 사이트를 노출시킬 수 있는 것도 소소한 장점이라고 생각합니다.

만들어진 위키는 아래 링크에서 확인하실 수 있습니다.  
[**위키 바로가기**][wiki]

[gitlab-guide]: https://about.gitlab.com/blog/2022/03/15/publishing-obsidian-notes-with-gitlab-pages/
[wiki]: https://wiki.haulrest.me
[docs]: https://squidfunk.github.io/mkdocs-material/
[obsidian]: https://obsidian.md/
[markor]: https://github.com/gsantner/markor
[mkdocs]: https://www.mkdocs.org/
