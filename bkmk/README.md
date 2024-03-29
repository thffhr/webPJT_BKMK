# Final Project 🎥

## 팀원 정보 및 업무 분담 내역

| 담당업무                                                     | 사용언어/툴                                                  | 담당자 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------ |
| API management<br/>Recommendation algorithm<br/>Database management<br/>Website construction<br/> | Python<br/>HTML/CSSS<br/>Bootstrap<br/>Django<br/>SQLite<br/>c9 | 이솔   |
| Project management<br/>Database construction<br/>UX/UI design<br/>Website Distribution<br/> | Python<br/>HTML/CSSS<br/>Bootstrap<br/>Django<br/>SQLite<br/>c9 | 우지윤 |



---

## 목표 서비스 구현 및 실제 구현 정도

### BKMK  볼까말까 👀

- 장르를 선택하면 해당 장르의 영화를 추천하는 사이트
  - 영화 목록
  - 마이페이지
  - 맞춤 영화 추천
  - 리뷰
- 추천 알고리즘
  - 좋아하는 장르 선택 -> 해당 장르에 해당하는 영화 추천

### Accounts

- 메인 페이지
  - 로그인, 회원가입 버튼
  - 회원가입의 경우 좋아하는 장르, 나이대 선택 필수
  - 로그인 한 경우 선택한 장르의 영화 추천
  - 영화 목록

- 마이페이지 
  - 타 유저 팔로워, 팔로잉 목록
  - 리뷰 게시글 작성 갯수
  - 팔로우 버튼

### Movies

- 메인 영화 목록 > 영화 선택 후 넘어감
  - 해당 영화의 줄거리, 평점, 리뷰 작성, 리뷰 목록, 개봉일, 장르
  - 리뷰 작성하기를 누를 경우 리뷰 작성으로 넘어감
  - 장르를 누를 경우 해당 장르의 영화 목록으로 넘어감

### Reviews

- 리뷰 작성
- 해당 유저의 리뷰
  - 수정, 삭제
- 타 유저의 리뷰
  - 좋아요

- 유저들이 작성한 리뷰 목록

### 영화 데이터 입력

- ~~네이버 APi : 영화 정보 검색>관련 정보 탐색~~
- TMDB : 영화 리스트 + 개봉일 + 장르 + 줄거리

## 데이터베이스 모델링(ERD)

## 필수 기능

- 관리자
  - 영화 등록/수정/삭제 
  - 유저 관리

- 영화 정보
  - 50개 이상의 데이터 
  - 로그인한 유저 평점 등록/수정/삭제 가능

- 추천 알고리즘
  - 영화 추천 가능 
  - 최소 1개 이상의 방식
- 커뮤니티
  - 로그인한 유저 글 조회/생성 가능, 본인만 수정/삭제 가능
  - 댓글 작성 가능, 본인만 댓글 삭제 가능

## 배포 서버 URL

(생략)



## 기타(느낀점)

- API를 사용할 때 모델과 데이터베이스를 어떻게 설계해야 할지 어려웠음.
- 다양한 기능을 적용하고 싶었으나 시간적 한계로 구현이 어려워서 아쉬었음.
- 협업시 적절한 역할 분배의 모호성
- 사용하고 싶은 프로그램(Css, Vue)이 적용되지 않아 사용하기 어려웠음.



### 출처 및 참고사이트

1. The movie DB

   https://www.themoviedb.org/



2. fontawesome

   https://fontawesome.com/



3. bootstrap

   https://getbootstrap.com/