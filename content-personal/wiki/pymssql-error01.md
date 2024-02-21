# pymssql SQL Server 접속 불가 문제

SQL Server는 [TDS(<span class="exclude">Tabular Data Stream</span>)](https://learn.microsoft.com/ko-kr/sql/relational-databases/security/networking/tds-8?view=sql-server-ver16) 프로토콜을 사용하여 클라이언트와 데이터베이스 서버 간에 데이터를 전송합니다.

`pymssql` 패키지의 경우 TDS 버전을 제대로 명시해 주어야 연결이 되는 경우가 있습니다.

문제 당시에는 다음과 같이 해결했습니다.
```python
conn = pymssql.connect(
    server, user, password, db,
    tds_version='7.0'
)
```
