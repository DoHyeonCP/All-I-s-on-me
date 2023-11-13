import pandas as pd
from .sk_api import LoadDf

class DataProcessor():
    def __init__(self):
        self.origin = pd.read_csv('congestion3') # 기존데이터 불러오기
        self.df = LoadDf()

    def train_dataset(self):
        # origin 2일전까지의 데이터
        new= self.df.df #1일전(어제)데이터, api 불러오기
        merged_df = pd.concat([self.origin, new])
        merged_df.ds = pd.to_datetime(merged_df.ds)
        merged_df=merged_df.fillna(0)
        merged_df=merged_df[['ds','ticker','y']]
        merged_df=merged_df.drop_duplicates()
        merged_df.to_csv('congestion3.csv', index=False) #저장
        
        return merged_df

    def create_features(self, mul):
        mul['hour']=mul['ds'].dt.hour

        # weekday 열 생성 (주중: 1, 주말: 0)
        mul['weekday']=mul['ds'].dt.dayofweek
        mul['weekday']=mul['weekday'].apply(lambda x: 0 if x >= 5 else 1)

        # season 열 생성
        mul['season']=mul['ds'].dt.month
        mul['season']=mul['season'].replace(12,0)
        mul['season']=pd.cut(mul['season'], [-1,2,5,8,11], labels=['Winter', 'Spring', 'Summer', 'Fall'])
        season_ohe=pd.get_dummies(mul['season'], prefix='season')
        mul=mul.join(season_ohe)

        #timebin 열 생성
        mul['timebin']=pd.cut(mul['hour'], bins=4, labels=False) #[(-0.023, 5.75] < (5.75, 11.5] < (11.5, 17.25] < (17.25, 23.0]]
        time_ohe=pd.get_dummies(mul['timebin'], prefix='tbin')
        mul=mul.join(time_ohe)
        # 결과 출력
        mul=mul.drop(columns=['hour','season','timebin'])
        
        return mul