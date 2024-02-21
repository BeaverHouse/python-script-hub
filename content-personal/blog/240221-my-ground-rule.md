---
slug: 240221-01
title: 생산성 올리기 (3) - 작업 프로세스
date: 2024-02-21T00:00:00+09:00
weight: 50
tags: ["Documentation", "Ground Rule"]
contributors: ["HU-Lee"]
---

앞의 두 글에서 개인 위키와 Repository 템플릿에 대한 이야기를 했습니다. 주로 문서화에 치중된 내용이었는데, 이번에는 전체적인 작업 프로세스에 대해 이야기하려 합니다.  
조직에서는 보통 효율적인 협업을 위해 그라운드 룰(<span class="exclude">Ground rule</span>)이라는 것을 정합니다. 완전히 동일하지는 않지만, 어느 정도의 규칙을 정해 두고 작업을 한다면 처음에는 불편하더라도 나중에는 능률이 올라가고, 협업을 할 때도 도움이 될 거라는 생각이 들었습니다. 실제로 앞에서 문서화에 대해 깊이 고민했던 경험이 실무에도 긍정적인 영향을 주고 있어서 망설임이 없었습니다.  
다만 혼자만의 규칙이기도 하고 이전에 너무 많은 제약을 설정했다가 고생했던 적도 있어서 어느 정도 유연성을 가지려고 노력했습니다.

<br>

### 글에 대하여

작년 10월부터 다시 블로그에 정착을 했고, 11~12월부터 커뮤니티 활동도 조금씩 하고 있습니다. 기본적으로 외부 반응에 대해 신경을 많이 쓰는 성격이라서 이전 글도 되찾아 보는 경우가 빈번했는데, 이번 기회에 명확한 기준을 정하기로 했습니다.  
우선 글을 몇 가지로 분류하기로 했습니다.

**커뮤니티 게시글**의 경우 글을 업로드하는 즉시 노출이 됩니다. 그리고 저의 경우 중요한 내용은 블로그 등에 따로 작성하기 때문에 이 쪽은 내용이 비교적 가벼운 편이고, 치명적인 오류나 실수가 없다면 가급적 관심을 줄이기로 하였습니다. 마치 우리가 메신저로 보낸 내용을 일일이 신경 쓰지 않는 것처럼 말이죠. 관리 포인트도 줄어들고, 다소 과도한 성향도 개선하는 방향이라고 생각하고 있습니다.

다음으로 **사내•개인 전용으로 작성하는 문서**가 있는데, 이 역시 특정 인원을 대상으로 하기 때문에 빡빡한 기준을 적용하지 않아도 된다고 판단했습니다. 지금도 제가 작성한 문서에 대한 별도의 피드백이 들어오지는 않고 있어서, 관리 포인트에서 제외하기로 했습니다.

**그 외**의 경우 블로그•위키•프로필•Repository 등을 모두 포함하는데, 이들은 공개적으로 장기간 노출이 되고 저를 지속적으로 표현하는 게시물이라고 판단했습니다. 그래서 최소한의 규칙을 준수하면서 글을 작성하고, 기존 글을 수정하기 위해 몇 가지 기준을 정했습니다.

- 맞춤법•영문법
  - 각각 [다음 맞춤법검사기](https://alldic.daum.net/grammar_checker.do)와 [LanguageTool](https://languagetool.org/)을 사용했습니다.
  - 글자 제한이 여유롭고, 검사 기준이 적당한 도구를 선택했습니다. 몇몇 다른 검사기들이 더 많은 옵션을 제공하지만 개인적으로 너무 과도했습니다.
- 과도한 영단어 줄이기
  - 이전 글을 보았을 때 필요 이상으로 영단어를 사용하고 있어서, 고유명사 + 한글이 너무 부자연스러운 경우에만 사용하기로 했습니다.
  - 영문의 경우도 고유명사를 제외하면 가급적 대문자를 사용하지 않고 풀어쓰려 하고 있습니다.
- 문맥
  - 이 부분은 다소 주관적인데, 대표적으로 문장 내 중복된 표현을 많이 사용하고 있어 이런 부분들을 한 번 더 확인하고 있습니다.

<br>

### 코드 관리 규칙

코드를 작성하고 Repository를 관리하는 규칙도 정했습니다. [React] • [FastAPI] 등 평소에 사용하던 오픈소스들을 참고하였습니다.

<b>이슈(<span class="exclude">Issue</span>)</b>의 경우 일반적으로 외부 사용자에 대해서 열어두기로 하였습니다. [베타 버전]의 템플릿이 워낙 잘 되어 있어 추가적인 조정은 필요 없었습니다. 저는 가급적 답변만 수행하고, 혼자서 사용하는 코딩 문제 저장용 Repository에서만 이슈로 코드 개선사항을 적어 두고 있습니다.

코드 업데이트는 <b>풀 리퀘스트(<span class="exclude">Pull Request, PR</span>)</b>를 사용하기로 결정했습니다. 특별한 경우만 아니면 혼자 볼 내용이기 때문에 영어로 간단한 요약을 적고, 라벨을 설정하고, 메인 코드에 합치는 식으로 간단하게 프로세스를 구상했습니다.  
실제 오픈소스를 참고해 보았을 때 템플릿은 모두 천차만별이고 아예 자유롭게 둔 곳도 많았습니다. 라벨은 대부분의 오픈 소스에서 사용하고 [Flutter]의 경우 400개 이상의 라벨이 존재하기도 하는데, 프로세스만 알고 있으면 될 것 같아 크게 9개의 라벨만 설정했습니다.

<span class="exclude">커밋(Commit)</span>의 경우 너무 자주 커밋을 하는 것을 부정적으로 보는 시선도 있지만 저는 기본적으로 커밋은 저장의 목적도 있다고 생각하기 때문에 그에 대해 부정적인 입장을 가지고 있지는 않습니다. 그리고 <span class="exclude">Squash merge</span>를 사용한다면 커밋을 자주 하면서도 Repository는 깔끔하게 유지할 수 있다는 생각이 들어 그렇게 사용 중입니다.

그 외에는 Repository 템플릿에서 구상한 대로 규격을 맞추고, 설정도 통일하여 사용하고 있습니다.

<br>

### 테스트

위에서 진행한 내용에 대한 테스트 케이스를 [Pytest]를 통해 추가하고 있습니다. 물론 모든 것을 자동화할 수는 없고 수동 작업도 있지만, 테스트 코드를 활용하여 공수를 줄일 수 있고 테스트 케이스가 계속 누적되기 때문에 이전 작업에 대한 체크도 계속할 수 있습니다.  
현재는 게시글과 Repository 설정에 대한 테스트 코드가 작성되어 있는데, 계속 추가할 생각입니다.

<br>

### 주기적으로 확인하기

시간이 지날수록 작업물의 양이 늘어나고, 이와 함께 규칙이 깨질 수도 있습니다. 이를 별도로 확인하여 항상 어느 정도의 수준을 유지할 수 있도록 해야 합니다. 아직 규칙을 적용한 초기 단계이기 때문에 이 단계까지는 가지 않았습니다.

<br>

### 내려놓기

어쩌면 저에게 제일 중요하다고 할 수도 있는 부분입니다. 지금까지의 비효율적인 작업은 물론 방법을 몰라서도 있었지만, 계속 과거의 작업에 주의가 분산되어서 그랬던 것도 분명히 지분이 있었습니다. 하루이틀 만에 고쳐지지는 않겠지만, 다짐을 겸해서 몇 가지 적어두려 합니다.

- 위에서 공개된 내용에 대해 규칙을 적용하고 지속적으로 관리해야 한다고 했는데, 그렇다고 모든 것을 동일한 관리 레벨에 두어야 하는 것은 아닙니다. 예를 들어 프로필은 가장 많이 노출하게 될 나의 정보이기 때문에 최신 상태를 유지하는 것이 좋지만, 블로그 게시물 같은 경우 주기를 길게 두거나, 경우에 따라 업데이트를 하지 않아도 괜찮을 것입니다. 대상의 중요도와 지속성에 따라 유연하게 대처하는 것이 필요합니다.
- 프로세스를 거쳐 작업이 완료되었다면 평상시에는 관심을 내려두고, 다른 작업에 집중하는 것이 좋습니다. 이미 확인 작업을 거치기도 했고, 작업물을 자신이 보는 것과 타인이 보는 것은 엄연히 달라서 스스로 개선을 하는 데는 한계가 있기 때문입니다.
  - 정말 피드백이 필요하다면 작업물을 외부에 공유하거나 타인에게 요청하는 등 다른 방법을 찾아보는 것이 더 효과적입니다.
- 유지할 가치가 없는 내용은 과감히 내려놓아야 합니다. 개발자는 계속 변화에 적응해 나가며 새로운 가치를 찾아야 하고, 지나간 것에 집착하는 것은 불필요한 비용만 발생시키기 때문입니다. 저는 과거의 기록이나 GitHub 잔디에 연연하는 성격도 아니기 때문에, 과감히 삭제하는 방향으로 처리하고 있습니다.

[React]: https://github.com/facebook/react
[FastAPI]: https://github.com/tiangolo/fastapi
[Flutter]: https://github.com/flutter/flutter/labels
[베타 버전]: https://docs.github.com/ko/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository#creating-issue-forms
[Pytest]: https://docs.pytest.org/en