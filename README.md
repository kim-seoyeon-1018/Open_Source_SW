# H2KE (Hand Sign to KOR/ENG)

## Intention of the plan  
  
전공을 살려 인공지능도 이용한 프로젝트를 진행하고자 하였습니다.  
평소 ==Social Impact Project==에 관심이 많은 팀원들이었기에 자연스럽게 수어 인식기를 생각하게 되었습니다.  
영어 수어 인식 기능은 많으나, 한국어 수어 인식 기능은 많이 없어 한국어 수어 인식기를 기획하고자 하였습니다.  
하지만 난이도의 문제와 자료가 많이 없어 오롯이 저희의 힘으로는 구현하기 어렵다고 판단하여 영어 수어를 인식 후, 한국어로 번역해 주는 기능을 생각하게 되었습니다.  

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
