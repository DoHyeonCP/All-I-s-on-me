## 붐비미
교통 약자를 위한 혼잡도 알림 서비스

![image](https://github.com/DoHyeonCP/All-I-s-on-me/assets/119473997/7395b09e-3895-4ea3-814a-b6bb1e6d10e6)


### 주요기능
1. 실시간 혼잡도 확인하기
   
![image](https://github.com/DoHyeonCP/All-I-s-on-me/assets/119473997/55e6af7d-16b9-4ac5-9bda-3bf75b734350)

2. 혼잡도 예측그래프 확인하기
![image](https://github.com/DoHyeonCP/All-I-s-on-me/assets/119473997/b941781b-6bad-4f32-92f3-c4053bf18b1f)

3. Push 알림
   
![image](https://github.com/DoHyeonCP/All-I-s-on-me/assets/119473997/3b86dc93-34cf-4c3d-95d2-57ae982e39ac)

AI 전달내용
--Python 3.7.10

실행 순서

1. main.py 실행
과정:
(Crontab-매일 0시 10분 경 1회 실행)
=> congestion3.csv 데이터 업데이트
=> train_weather.csv 데이터 업데이트
=> model1 에측
=> model2 예측
=> total_pred.csv 생성 (두 모델 예측값 병합)
=> plot.py 실행
=> 장소별 미래시간 그래프 생성
=> 장소 비교 그래프 생성
=> images 폴더에 png파일로 저장
=> html_files 폴더에 html파일로 저장


2. rltm_poi.py 실행
과정:
(Crontab-매시간 25분경 총 24회 실행)
=> rltm_data.csv 데이터 업데이트 (실시간 데이터 병합)
시간이 0시가 아닌 시간에 중도 실행할 경우 rltm_data.csv 내에 데이터 삭제(열이름 유지) 후 실행
=> 오늘 예측값 + 실제값 그래프 생성
=> images 폴더에 png파일로 저장
=> html_files 폴더에 html파일로 저장
