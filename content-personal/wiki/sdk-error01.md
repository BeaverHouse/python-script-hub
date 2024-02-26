# 네아로 SDK 사용 시 주의사항

몇 주 전, 다른 개발자 분이 앱에서 사용자 <span class="exclude">UID</span>가 개발 • 운영에 따라 값이 다르게 들어오는데 원인을 찾지 못하고 계셨습니다.<br>같이 조사를 해 보니 다음과 같은 공지사항이 있었습니다.

[<span class="exclude">[네이버 아이디로 로그인] '이용자 고유 식별자' 발급 스펙 변경 관련 공지 - 공지사항 (naver.com)</span>](https://developers.naver.com/notice/article/7524)

공지사항에 의하면 2021년 5월에 <span class="exclude">UID</span> 사양이 변경되었고,<br>문제를 찾고 계시던 분은 2021년 5월 이전에 만들어진 앱을 이후에 Flutter를 통해 다시 만들고 계셨기 때문에 <span class="exclude">UID</span>의 형식이 달라졌던 것이었습니다.

**외부 API나 SDK를 사용할 경우 중요한 변경사항이 있는지 확인이 필요하다**는 것을 알려준 사례였습니다. 다만, 이 경우는 검색으로도 찾기 꽤나 힘들었기 때문에 글로 작성해 두려고 합니다.
