# Jupyter Notebook 파일 삭제 오류

## 문제 상황
- Jupyter Notebook을 K8s Pod로 띄우고, PVC를 마운트 한 상태
- PVC 파일을 UI 상에서 삭제할 수 없다는 문의가 들어왔습니다.

## 문제 원인
- UI에서 파일 삭제 버튼을 누르면 즉시 영구 삭제가 이루어지는 것이 아니라,<br>휴지통 폴더로 해당 파일을 이동시킵니다.
- 이 과정에서 <span class="exclude">`os.rename`</span> 함수를 사용하는데,<br>이 함수는 [시작 위치와 도착 위치가 다른 파일 시스템 상에 존재할 경우 작동하지 않습니다.](https://stackoverflow.com/a/43967659)
- 이 경우는 시작 위치(삭제할 파일)가 PVC 상에 존재했고,<br>휴지통 폴더는 Pod 내부에 존재했기 때문에 에러가 발생하는 상황이었습니다.

## 해결 방법
- <span class="exclude">`os.rename`</span> 함수를 <span class="exclude">`shutil.move`</span> 함수로 교체하거나<br><span class="exclude">`shutil.copy` + `os.remove`</span> 함수 조합을 사용할 수 있습니다.<br>실제로는 [두 번째 방법으로 수정](https://github.com/arsenetar/send2trash/pull/63/commits/b6cb3653f8811949e96557c88e2e9f4b0c479972)된 것으로 보입니다.
- 하지만 Jupyter Notebook 자체의 문제이기 때문에<br>사내에서 버전이 고정된 경우 해결할 수 없는 문제였습니다.