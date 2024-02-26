# Helm

[Helm](https://helm.sh/)은 [Kubernetes](https://wiki.haulrest.me/concept/cloud/kubernetes/)를 위한 패키지 관리 도구입니다. CNCF의 졸업 단계 프로젝트(<span class="exclude">Graduated Project</span>)이기도 합니다.<br>Helm의 몇 가지 특징은 다음과 같습니다.

## YAML 파일 템플릿

컨테이너 기반 환경을 쉽게 관리할 수 있도록 도와주는 Kubernetes(K8s)는 그 자체로 훌륭한 도구입니다. 하지만, K8s는 각각의 구성 요소에 대해 YAML 설정 파일이 필요하고, 이러한 구성 요소들이 모였을 때 비로소 하나의 앱으로 작동할 수 있습니다.<br>예를 들어, 아주 작은 앱 하나를 K8s 환경에서 외부로 노출시키려고 한다면 무엇이 필요할까요? 저는 간단하게 생각해도 최소 3개의 요소가 필요할 것 같습니다.

- 앱을 구동시킬 [<span class="exclude">Pod</span>](https://kubernetes.io/docs/concepts/workloads/pods/)
- 이 <span class="exclude">Pod</span>를 네트워크에 노출시킬 [<span class="exclude">Service</span>](https://kubernetes.io/docs/concepts/services-networking/service/)
- 이 <span class="exclude">Service</span>를 외부에서 접근 가능하게 할 [<span class="exclude">Ingress</span>](https://kubernetes.io/docs/concepts/services-networking/ingress/)

아주 단순한 구조인데도, 벌써 3개의 YAML 파일을 관리해야 합니다. 그런데 구성이 더 복잡해진다면? 별도 스토리지가 필요하다면? 설정 파일을 따로 관리하고 싶다면? 관리해야 할 요소는 급격히 늘어날 것입니다.

Helm은 이 여러 개의 YAML 파일들을 묶어 하나의 템플릿으로 관리합니다. 이를 Helm에서는 <span class="exclude">chart</span>라고 정의합니다. <span class="exclude">Helm chart</span>를 통해 연관된 구성 요소들을 한 곳에서 관리하고, 배포도 구성 요소 하나하나를 각각 배포할 필요 없이 한 번에 배포를 수행할 수 있습니다.

## 사용자 변수의 통합 관리

거의 모든 앱에는 사용자 설정 변수들이 있습니다. 각각의 구성 요소에서 변수를 따로 관리해야 하는 것은 매우 귀찮고 골치 아픈 일입니다. K8s도 마찬가지입니다. 여러 설정 파일들 중에서 변경해야 할 변수가 어디에 있는지 찾아야 하고, 여러 곳에 영향을 주는 값을 변경해야 하는데 실수로 일부만 변경했다면 예상하지 못한 오류가 생길 수도 있습니다.<br>Helm은 이러한 사용자 변수를 `values.yaml` 파일에서 모두 관리합니다. 그리고 Helm 템플릿의 YAML 파일은 `values.yaml` 파일의 값을 읽을 수 있도록 [Go 템플릿](https://pkg.go.dev/text/template) 기반으로 구성되어 있습니다. 이를 통해 사용자는 설정 오류를 최대한 줄이면서 효율적으로 변수를 관리할 수 있습니다.

## 리소스 동적 배포/관리
Helm에서는 `values.yaml` 파일의 설정값을 [오버라이딩](https://helm.sh/docs/chart_template_guide/values_files/)할 수 있습니다. 명령어로 직접 변경할 필드를 지정할 수도 있고, 별도의 설정 파일을 만들어 해당 파일의 값으로 덮어씌우는 것도 가능합니다. 이를 통해 여러 문제 상황에서 유연하게 대응하고, 비슷한 리소스를 단일 <span class="exclude">Helm chart</span> 기반으로 배포하는 등 다양하게 응용이 가능합니다.

<br>
<br>

**Helm의 자세한 사용법은 [공식 문서](https://helm.sh/docs/)를 참고해 주세요.**