# Git 관리 규칙

## Branch
- ```master``` : 항상 실행 가능한 상태 유지 
- ```develop``` : 개발용 
- ```feature``` :기능 단위 개발용 
- ```release``` : master로 옮기기전 검수용 
- ```hotfix``` : 급하게 고쳐야 하는 코드 디버깅용

## Commit 🌱
- ```Feat``` : 새로운 기능 추가
- ```Fix``` : 버그 해결
- ```Docs``` : README, 주석 작성
- ```Style``` : 스타일 관련 기능(코드 포맷팅, 세미콜론 누락, 코드 자체의 변경이 없는 경우)
- ```Refactor``` : 코드 개선, 리팩토링
- ```Test``` : 테스트 코드 추가 및 리팩토링
- ```Chore``` : 빌드 업무 수정, 패키지 매니저 수정 등 (ex. gitignore 수정)

아래의 명령어를 통해 commit setting
```
git config --global commit.template .gitmessage.txt
```

commit 작성 예시 ```(제목만 해도 됨)```
```
git commit -m "<feat> : 커밋 제목 // 짧고 간단하게
                                  // 2칸 띄고
부가 설명"                        // 이번 커밋으로 인한 변경점
```