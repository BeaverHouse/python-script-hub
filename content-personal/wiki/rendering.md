# 렌더링

렌더링(<span class="exclude">Rendering</span>)이란 **개발자가 작성한 웹 페이지를 실제로 출력하는 과정**을 말합니다.<br>크게 CSR(Client-side Rendering)과 SSR(Server-side Rendering)으로 나뉩니다.

## CSR (Client-side Rendering)
![CSR Flow](img/csr.png)
유저가 방문했을 때 **뼈대만 있는 HTML + 필요한 JavaScript를 모두 다운로드**한 후, **클라이언트(브라우저)에서 JavaScript를 통해 페이지를 만들어 표시**합니다.

CSR의 대표적인 예시로 [React](https://react.dev/)가 있습니다. 일반적인 React 템플릿은 <span class="exclude">`index.html`</span> 파일 하나만을 가지고 있고, 파일 안을 살펴보아도 비어 있는 `<div>` 태그 하나만 존재합니다. 여기에 JavaScript를 연결하여 페이지를 만들게 됩니다.

#### 장점
- 서버의 부하가 적습니다 (일을 서버가 안 하니까)
- 로딩 이후의 반응속도가 빠릅니다.<br>이미 필요한 모든 코드를 다 받아왔기 때문입니다.
- 필요한 부분만 업데이트를 할 수 있습니다.
- 클라이언트가 로직을 직접 처리하기 때문에 반응속도가 빨라 상호작용에 유리하고 좋은 사용자 경험을 제공합니다.

## SSR (Server-side Rendering)
![SSR Flow](img/ssr.png)
유저가 방문했을 때 **서버에서 즉시 렌더링 가능한 HTML을 만들어 반환**하고, 이후에 JavaScript를 다운로드하여 로직을 연결합니다.

대표적으로 [Next.js](https://nextjs.org/)가 있습니다.

#### 장점
- 초기 로딩이 빠릅니다.<br>필요한 부분의 코드만 우선 다운로드하여 화면을 표시해 주기 때문입니다.
- 이미 렌더링 된 HTML을 크롤러가 읽어 정보를 파악하기 쉽기 때문에 SEO에 유리합니다.

## SPA•MPA와 CSR•SSR
SPA는 Single Page Application,<br>MPA는 Multi Page Application의 약자입니다.

- 일반적으로 SPA는 CSR을 주로 사용하고, MPA는 SSR을 주로 사용합니다.
- 하지만 SPA•MPA는 페이지가 하나인지, 여러 개인지를 구분하는 개념으로<br>렌더링 방식인 CSR•SSR과는 비교 대상이 아닙니다.

## CSR과 SSR 중 어느 것을 사용해야 할까?

### CSR을 사용하면 좋은 경우
- 상호작용이 많을 때
- SEO가 필요 없을 때 (내부 서비스 등)
- 서버 부담을 줄여야 할 때

### SSR을 사용하면 좋은 경우
- SEO가 중요할 때 - 유입이나 인지도를 원한다면 SEO는 매우 중요하고<br>그래서 서비스•스타트업 쪽은 거의 무조건 Next.js 혹은 [Nuxt](https://nuxt.com/)를 사용한다고 합니다.
- 초기 로딩이 중요할 때

꼭 CSR•SSR 중 하나만 사용해야 하는 것은 아닙니다. CSR, SSR을 적절히 사용하고, 하나의 서비스 안에서 혼용할 수도 있습니다.

## SSG (Static Site Generation)
~~신세계~~

미리 모든 페이지를 생성해 두고 요청에 따라 해당하는 페이지를 반환해 주는 방식입니다.<br>SSR은 요청이 들어온 뒤 HTML을 생성하기 때문에 차이가 있습니다. 다만 SSG도 HTML을 모두 만들어 두기 때문에 SSR의 최대 장점인 SEO의 유리함은 가져갈 수 있습니다.

SSG는 별도의 상호작용이 필요 없고, 변경사항이 거의 없으며 항상 같은 내용을 보여 주는 사이트를 만들 때 유용합니다. 대표적으로 개발 블로그에 SSG를 활용하는 경우가 많습니다.

## 참고 자료
- [SSR를 이용하여 리다이렉트 방식 수정하기 (velog.io)](https://velog.io/@codingsnom/study-server-side-rendering)<br>SSR의 특징을 잘 활용한 사례라고 생각합니다.
- [<span class="exclude">[10분 테코톡] 🎨 신세한탄의 CSR&SSR - YouTube</span>](https://www.youtube.com/watch?v=YuqB8D6eCKE&ab_channel=%EC%9A%B0%EC%95%84%ED%95%9C%ED%85%8C%ED%81%AC)
- [<span class="exclude">Next.js의 SSR과 React의 RSC(React Server Components) 완벽 이해 (mycodings.fly.dev)</span>](https://mycodings.fly.dev/blog/2024-01-28-complete-understanding-nextjs-ssr-and-react-rsc)
