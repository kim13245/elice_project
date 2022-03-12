# 9성이 알찬 팀 기획서 - 마음의 소리
  **사용자가 신체, 증상에 관련한 단어들의 수화를 배우고, 직접 카메라를 통해 동작을 따라하며 학습하는 서비스입니다.**
<br>
## 프로젝트 구성 안내

 
## 1. 프로젝트 소개

수화 교육 서비스는 대부분 영상이나 이미지 자료 제공으로 그치는데 비해 학습된 모델로 사용자의 동작의 정확도를 알려주기 때문에 보다 효과적인 학습을 제공합니다.


<br><br>
  


## 2. 프로젝트 기획 의도


뉴스를 통해서 청각장애인들이 수어를 배울 수 있는 환경이 열악하다는 소식을 접했고 언어장애를 가지신 분들 중에 수어를 사용할 수 있는 사람은 14.1%에 불과하다는 사실을 알게 되었습니다.

또한 수어를 가르쳐야할 농학교에서 수어 가능 교원은 6.1%로 라는 통계를 보았습니다. 이렇듯 수어를 배우기에 열악한 환경 속에서 조금이나마 도움이 되고자 수어교육서비스를 구상하게 되었습니다.

저희는 수어 교육에 대한 주제를 선정하기 위해 고민을 하면서 후천적 요인으로 인해 급하게 수화를 익혀야 되는 사람들(당사자, 당사자의 주변인)에게는 가장 우선적으로 익혀야 할 표현이 건강 상태에 관한 표현들에 관심을 가지게 되었습니다.

또한 청각 장애 환자가 의료 기관을 이용하는 경우 의료진과의 소통이 제대로 이뤄지지 않아 중요한 정보를 놓치거나 잘못 전달될 경우가 있어 이러한 경우들을 도울 수 있도록 수어교육서비스 주제를 선정하였습니다. 

이후 팀원들과 '만약 우리의 자녀가 언어장애를 가졌다면 어떤 단어를 제일 먼저 알려주고 싶을까' 라는 생각을 하며 '어딘가가 불편하거나 아프다는 표현을 해줬으면 한다'는 의견이 많았고 이를 토대로 우선적으로 신체와 증상의 단어로 한정하여 구현하였습니다.



<br><br>


## 3. 서비스 주요 기능 설명


**- 메인기능**

1. 단어리스트 화면에서 배우고 싶은 단어를 선택

2. 해당하는 단어의 학습 영상을 시청하며 동작을 익힘

3. 동작을 따라하는 영상을 촬영 후 전송

4. 사용자의 영상을 가상환경으로 넘겨 영상 분석

5. 학습된 모델을 이용하여 사용자의 수화 동작을 분석하여 표현하고자 하는 단어와 비교

6. 비교 후 정확도를 계산해 점수로 표현하여 분석 결과를 화면에 보여줌

<br><br>
**- 서브기능**

1. 수화 통역 번역 센터 위치 제공

- 사용자 위치를 받아서 사용자 위치로 부터 가장 가까운 센터의 정보를 제공 


2.  마이페이지 기능

- 학습 결과에서 얻은 각 메달의 총 갯수, 학습 진행률, 최근 학습한 단어 목록을 보여줌


3. 퀴즈 

- 신체와 증상 중 주제를 선택하여 퀴즈를 풀며 학습한 단어에 대해 성취도를 알 수 있도록 함
  

<br><br>



## 4. 프로젝트 구성도
- Figma
    - https://www.figma.com/file/OensWKNd4JQh1LLIYR9kkx/Untitled?node-id=0%3A1 

- API 명세서
    - https://www.notion.so/elice/API-a5c42aaafcdd4f0293229f81de53d3f7

- ERD
    - https://www.notion.so/elice/ERD-fa2459fec7ae42eb8562444a0ffc187e
  

<br><br>

## 5. 기술 스택

- 프론트 : Next.js

- 백엔드 : Django, Python, Tensorflow

- 인공지능 : Mediapipe, Pandas, Tensorflow

- 사용 기술 스택 (Next.js, Django, Python, Tensorflow, Mediapipe, Pandas, )


<br><br>


## 6. 프로젝트 팀원 역할 분담

| 이름 | 담당 업무 |
|--|--|
| 김인기 | 팀장/백엔드 개발 / 인공지능 개발|
| 류진식 | 프론트엔드 개발 |
| 노영훈 | 백엔드 개발 / 인공지능 개발 |
| 김채원 | 백엔드 개발 / 프론트엔드 개발|
| 전소희 | 인공지능 개발 |
| 김세현 | 인공지능 개발 |

  

**멤버별 responsibility**

  

<b>1. 김인기: 팀장/백엔드 담당</b>

  

- 기획 단계: 구체적인 설계와 지표에 따른 프로젝트 제안서 작성

- 개발 단계: 팀원간의 일정 등 조율 + 프론트 or 백엔드 or 인공지능 개발

- 수정 단계: 기획, 스크럼 진행, 코치님 피드백 반영해서 수정, 발표 준비

  

<b>2. 김채원,  김인기, 노영훈: 백엔드 담당</b>

  

- 기획 단계: 큰 주제에서 문제 해결 아이디어 도출, 와이어프레임 작성

- 개발 단계: 와이어프레임을 기반으로 API 및 데이터베이스 완성

- 수정 단계: 피드백 반영해서 백엔드 설계 수정

  

<b>3. 김세현, 전소희: 인공지능 담당</b>

  

- 기획 단계: 큰 주제에서 문제 해결 아이디어 도출, 와이어프레임 작성

- 개발 단계: 와이어프레임을 기반으로 인공지능 모델 구현, 모델 학습 진행

- 수정 단계: 피드백 반영해서 모델 정확도 향상


<b>4. 류진식:  프론트 엔드 담당</b>

  

- 기획 단계: 큰 주제에서 문제 해결 아이디어 도출, 와이어프레임 작성

- 개발 단계: 와이어프레임을 기반으로 웹 페이지 디자인 구체화
- 수정 단계: 코치님 피드백 반영하여 프론트 유지 보수


<br><br>



## 7. GitLab 규칙

- master : 최종본
- sprint : 테스트 브랜치
- feature : 기능 브랜치
- fix : 수정 브랜치

- [GitLab사용법](docs/GitDocs.md)

<br><br>

## 8. 팀 페이지

- https://www.notion.so/elice/9-bb156497179849ab894e3d0c063385b4
