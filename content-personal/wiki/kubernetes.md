# Kubernetes

[Kubernetes](https://kubernetes.io/)(K8s)는 컨테이너화된 앱을 자동으로 관리하기 위한 오픈 소스 도구입니다. [Docker](https://wiki.haulrest.me/concept/cloud/docker/)를 기반으로 한 리소스 관리 방식을 한 차원 더 발전시켰으며, 현재 클라우드 리소스 관리의 사실상의 표준으로 높은 인기와 점유율을 자랑하고 있습니다.

Kubernetes의 생태계는 매우 방대하고, 저도 계속 알아가는 과정에 있습니다. 따라서 모든 것을 설명할 수는 없지만 몇 가지 내용들을 정리해 두려고 합니다.

## Kubernetes의 특징
### 컨테이너 환경 관리의 자동화
Docker로 앱 구동 환경을 통일한 것은 좋았으나, 여전히 대규모 환경에는 많은 작업이 필요했습니다. 확장과 축소, 장애 대응 등을 수동으로 해야 했기 때문입니다.
Kubernetes는 기본적으로 정의된 리소스에 대한 관리를 자동화합니다. 리소스 사용률을 체크하여 유동적으로 확장/축소를 하는 <span class="exclude">Autoscaling</span>, 리소스 구동 상태를 주기적으로 체크하고 장애가 생긴 리소스를 다시 복구할 수 있는 <span class="exclude">Deployment</span> 등이 이에 해당합니다.

- [<span class="exclude">Horizontal Pod Autoscaling | Kubernetes</span>](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)
- [<span class="exclude">Deployments | Kubernetes</span>](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [<span class="exclude">Configure Liveness, Readiness and Startup Probes | Kubernetes</span>](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)


### 리소스와 권한 관리
Kubernetes에서는 다양한 리소스 배포 정책을 설정할 수 있습니다. 특정 환경에만 배포를 하도록 설정하거나 역으로 막을 수도 있고, 리소스 간의 <span class="exclude">Affinity</span>를 설정하여 배포 환경을 집중/분산할 수도 있습니다. 여러 가지 전략을 통해 더 효율적인 리소스 관리가 가능합니다.
또한 안전한 관리를 위해 사용자에 대한 권한을 설정하여 특정 리소스에 대한 접근을 허용/제한할 수 있습니다.

- [<span class="exclude">Taints and Tolerations | Kubernetes</span>](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)
- [<span class="exclude">Assigning Pods to Nodes | Kubernetes</span>](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)
- [<span class="exclude">Using RBAC Authorization | Kubernetes</span>](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)

### 코드를 통한 리소스 제어
Docker에서도 배포 환경을 코드를 통해 정의했다고 했는데, Kubernetes에서는 더 나아가 네트워크, 권한 등 더 많은 구성 요소를 코드로 정의합니다. 심지어 [<span class="exclude">CRD</span>](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)를 통해 사용자가 직접 개념을 정의하고 활용할 수도 있습니다. 이로서 모든 인프라를 코드로 정의하여 관리하는 IaC(Infrastructure as Code)에 한 걸음 더 다가서게 되었습니다.

## CNCF
[CNCF](https://www.cncf.io/)는 리눅스 재단의 프로젝트 중 하나로, 컨테이너 기반 기술 산업의 발전을 위해 설립되었습니다.<br>CNCF의 핵심에는 바로 K8s가 있으며 대다수의 CNCF 프로젝트가 K8s 환경을 전제로 하고, K8s의 한계를 극복하고, K8s의 기능을 확장하는 방향성을 가지고 있습니다. 이 거대한 생태계는 K8s가 사실상의 클라우드 표준으로 지속적으로 발전할 수 있게 하는 원동력이라고 볼 수 있습니다.

## Kubernetes의 단점
- Kubernetes는 대규모 리소스 관리에 보다 적합한 도구입니다. 소규모 서비스의 경우에는 오히려 관리의 복잡도가 늘어날 가능성도 있습니다.
- 사용하는 데 꽤 많은 지식을 필요로 합니다.
- 직접 구축한 K8s와 클라우드 환경의 [Amazon EKS](https://aws.amazon.com/ko/eks/), [GKE](https://cloud.google.com/kubernetes-engine?hl=ko) 등은 비슷하지만 용어와 사용법 등이 조금씩 다릅니다. 따라서 플랫폼이 달라진다면 어느 정도의 추가 학습도 필요합니다.

위에서 이야기한 점들로 인해 아직 소규모 조직이나 스타트업에서는 대부분 Kubernetes를 거의 고려하지 않습니다.

## 참고 자료
- [<span class="exclude">Kubernetes Documentation | Kubernetes</span>](https://kubernetes.io/docs/home/)
- [<span class="exclude">Dive to Argo | Dive to Argo (haulrest.me)</span>](https://dive-argo.haulrest.me/)<br>직접 작성한 Kubernetes + Argo 실습 페이지입니다.
- [<span class="exclude">쿠버네티스 안내서 (subicura.com)</span>](https://subicura.com/k8s/)<br>가장 많이 언급되는 K8s 한국어 안내서입니다. 처음 K8s에 입문할 때 소개받았던 링크이기도 합니다.