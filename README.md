# anime_recommend

이미 본 애니메이션의 제목을 입력하여 다른 애니메이션을 추천받는 웹 대시보드입니다.

Dataset : https://www.kaggle.com/datasets/snehaanbhawal/anime-list-for-recommendation-system-june-2021    
Deployment : http://15.164.213.131:8502/ - free tier 를 사용하여 메모리 부족으로 로컬로 작업

# columns
mal_id : 고유한 MyAnimeList ID
title : 애니메이션 제목
synopsis : 애니메이션의 개요
aired : 애니메이션 방영 기간
airing : 애니메이션 방영이 종료된 경우 0, 진행 중인 경우
duration : 각 에피소드의 방송 시간
episodes : 에피소드 수. Null 값은 -1 로 대체
type : 릴리스 유형
favorites : 애니메이션을 좋아하는 사람들의 수
members : 애니메이션의 구성원 수
rank : 애니메이션의 순위 Null 값은 -1 로 대체
popularity : 애니메이션의 순위 Null 값이 -1로 대체
score : 애니메이션의 평균 점수
scored_by : 점수를 준 사람의 수
rating : 애니메이션을 관람할 수 있는 연령대
premiered : 방영 연도와 시즌
genres : 장르
related : 문자열 형식의 관련 애니메이션
status : 방영현황
licensors : 쉼표로 구분된 문자열의 라이센스 사용 허가자 이름
producers : 쉼표로 구분된 문자열의 생산자, 생산 회사 이름
studios : 쉼표로 구분된 문자열의 제작 스튜디오 이름

------------------

# describe

![image](https://user-images.githubusercontent.com/105832386/172544853-c67f7380-0e07-4671-be76-b0303b68cbba.png)   


애니메이션의 정보가 들어있는 데이터프레임과   

최고 평점, 최고 인기 등 주요 컬럼을 기준으로 정렬된 데이터 프레임을 확인할 수 있다.

# search

![image](https://user-images.githubusercontent.com/105832386/172544917-1b595c87-27bb-4e9b-8803-cac84438356b.png)   

정렬의 기준이 될 컬럼을 선택하고

![image](https://user-images.githubusercontent.com/105832386/172545012-b222b417-9668-48f1-adc8-af329d6bcc60.png)


정렬 방식을 선택한 다음에   

![image](https://user-images.githubusercontent.com/105832386/172545066-dc75e55c-3f42-4161-9b24-e3166a3fd017.png)

일부 문자열을 통해 애니메이션의 제목을 찾아볼 수 있다.   

![image](https://user-images.githubusercontent.com/105832386/172545107-edbe0fa3-3def-4627-9503-011c4f662745.png)

찾은 애니메이션의 제목 또는 이미 알고 있는 제목을 통해 새로운 제목을 추천받을 수 있다.   
