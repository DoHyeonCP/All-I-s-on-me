리팩토리 남은 일


### 1. 실시간 혼잡도
- CallApi함수들 객체화하기, 끝
- SkOpen APi로 가져오는 횟수를 줄이기위해 스케줄러를 사용해 한시간에 한번 Db에 저장하고 JsonResponse하기(모델에 저장하는 코드 미완성. 스케줄러 뭐쓰지)
- DjangoRestFramework를 활용하여 api를 restful하게 바꾸기

### 2. 예측그래프
- api로 예측 그래프 내보내기(세부사항 미정)