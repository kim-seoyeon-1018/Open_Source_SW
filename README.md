# H2KE (Hand Sign to KOR/ENG)

## Markdown contents
0. [README](./README.md) : 프로젝트 설명
1. [Git Rules](./Git_Rules.md) : Git 관리 규칙 설정
2. [History](./History.md) : commit history 작성

## Plan Design

> Lev 1.
> H2E - 알파벳 수어 인식, **Cmoplete**.
>> Lev 2.
>> H2K - 한글 수어 인식, **Continue**.

## Structure
프로젝트 파일 구조
```
Open_Source_SW/H2KE
> H2E
  > Data // Hand Sign 데이터 파일
    > A
    > B
    > C
  > Model // 생성된 모델 저장공간
  | dataCollection.py // 데이터를 가져오는 기능
  | handSignDetection.py // hand to ENG 메인 코드 
> E2K
| __init__.py // H2KE 모듈화
| test.py // 모델 테스트 코드
```
