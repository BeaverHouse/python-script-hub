# Rally로 Elasticsearch 벤치마크 테스트하기

[Rally](https://github.com/elastic/rally)는 Elasticsearch의 성능을 측정하기 위한 프레임워크입니다.

## 필요 환경
- Rally는 Linux 환경에 설치되어야 합니다.<br>Rally는 Windows를 포함한 원격 Elasticsearch 벤치마킹을 지원하지만, Rally 자체를 Windows에서 실행할 수는 없습니다. (WSL에서는 실행 가능합니다.)
- 다음 환경이 설정되어 있어야 합니다.
	- [Python](https://www.python.org/) 3.8 이상
	- [Git](https://git-scm.com/) 1.9 이상
	- [Elasticsearch 버전에 맞는 JDK](https://www.elastic.co/kr/support/matrix#matrix_jvm)

## 설치
다음 명령어로 Rally를 설치합니다.

```
pip install esrally
```

## 벤치마크 테스트 방법

### 트랙 생성
트랙<span class="exclude">(Track)</span>은 벤치마킹 시나리오에 대한 정보를 담고 있으며 Rally를 실행할 때 반드시 참조되어야 합니다.

Repository의 트랙을 가져오거나 수동으로 만들 수도 있지만, 기존의 Elasticsearch에서 인덱스 또는 데이터 스트림(<span class="exclude">Data stream</span>)을 통해 생성할 수도 있습니다.<br>데이터 스트림은 Elasticsearch 최신 버전에서 추가된 기능으로 여기서는 인덱스를 통해 생성하겠습니다.

```
esrally create-track \
--track=<트랙 이름> \
--target-hosts=<host>:<port> \
--client-options="use_ssl:true,verify_certs:true,basic_auth_user:'your-id',basic_auth_password:'your-password'" \
--indices="idx1,idx2" \
--output-path=<저장할 경로>
```

`--target-hosts` 옵션의 경우 벤치마크 테스트를 수행할 Elasticsearch에 접근 가능한 주소를 적어야 합니다. 도메인으로 접근하는 경우에도 포트(80, 443...)를 명시해야 합니다.<br>`--client-options` 옵션의 경우 Elasticsearch 접근에 인증을 요구하는 경우 반드시 기입해야 합니다. 그렇지 않다면 생략해도 됩니다.<br>`--indices` 옵션에는 인덱스를 지정하면 되고 콤마(,)로 구분하여 여러 개를 지정할 수도 있습니다.<br>그 외는 상황에 맞게 설정값을 작성하면 됩니다.

### 테스트 수행

```
esrally race \
--track-path=<트랙 경로> \
--target-hosts=<host>:<port> \
--client-options="use_ssl:true,verify_certs:true,basic_auth_user:'your-id',basic_auth_password:'your-password'" \
--pipeline=benchmark-only \
--report-format=csv \
--report-file=<파일 이름(경로 포함)>
```

`--track-path` 옵션에는 트랙 경로를 지정합니다. 트랙을 생성했을 경우 성공 이후 어느 경로를 지정해야 할지 Rally에서 알려 줍니다.<br>`--pipeline` 옵션의 경우 크게 3가지 옵션이 있는데, 그중 `from-sources`, `from-distribution` 옵션은 각각 사용자 소스와 공식 배포 파일을 통해 직접 Elasticsearch를 구축하여 테스트하는 방식입니다. 원격으로 Elasticsearch를 테스트하려면 `benchmark-only` 옵션을 선택하면 됩니다.<br>그 외는 상황에 맞게 설정값을 작성하면 됩니다.

## 테스트 결과 확인
<span class="exclude">**Final Score**</span>라는 문구와 함께 테스트가 완료되고, 로그 또는 파일에 정상적으로 결과가 나오면 성공입니다. 테스트 결과는 <span class="exclude">Heap</span> 메모리 사용량, 지연 시간 등 여러 항목을 포함하고 있는데 관리 기준에 따라 성능을 판단하시면 됩니다.

## 참고 자료
- [Rally 공식 문서](https://esrally.readthedocs.io/en/stable/index.html)