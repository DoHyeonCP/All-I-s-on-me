import pandas as pd
import requests
from django.conf import settings

api_keys=["j8VUTaKCsy9YwKQvy2FVR2fuz1HOvKdX8cWJFwDu","e8wHh2tya84M88aReEpXCa5XTQf3xgo01aZG39k5",
         "w3oFktJUat2NPpDorwHZE7avbxcvdq0S7wx4vXfN","Tt3yyROHTM8op2hEyv1Z34AXC2x8KPbn1iuD5Hlc",
         "RNM43SFreC8YwWjFIAGHY4VIpOi6jDHG98AHf7rN"]
api_key_index=0

#data 불러오기 - 1. Sk Api
class CallApi():
    # 시간대별 혼잡도: 상권의 과거 30일 간의 일자/시간대별 혼잡도 호출
    def get_data_pois(self, date, df):
        # 장소 id 리스트
        ids = [187961, 5783805, 5799875, 384515]
        # SK api 홈페이지에서 호출링크 가져옴
        base_url = "https://apis.openapi.sk.com/puzzle/place/congestion/stat/raw/hourly/pois/"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "appKey":api_keys[api_key_index]
        }
        # API 응답 저장할 빈 딕셔너리 생성
        responses = {}

        # for문으로 id리스트 이용, API 호출하기
        # id를 키로하여 Json형식으로 받아와서 저장
        for place_id in ids:
            url = base_url + str(place_id)
            query_params = "?date=" + str(date)
            full_url = url + query_params
            try:
                response = requests.get(full_url, headers=headers)
                response.raise_for_status()  # 오류가 있는 경우 예외 발생
                responses[place_id] = response.json()
            except requests.exceptions.RequestException as e:
                print(f"Error occurred: {e}")
                print("Switching to the next API key...")
                self.switch_to_next_key()
                return self.get_data_pois(date, df)

        # for문 reponse 딕셔너리 항목에서 키값으로 데이터 추출하고 각 변수에 저장
        for place_id, response_data in responses.items():
            poi_id = response_data['contents']['poiId']
            poi_name = response_data['contents']['poiName']
            for item in response_data['contents']['raw']:
                congestion = item['congestion']
                congestion_level = item['congestionLevel']
                datetime = item['datetime']

                # 'df'에 새로운 데이터 추가하고 인덱스 재설정
                new = pd.DataFrame({
                    #'Id': poi_id,
                    'ticker': [poi_name],
                    'y': [congestion],
                    #'CongestionLevel': congestion_level,
                    'ds': [datetime]
                })
                df=pd.concat([df,new], ignore_index=True)

        return df

    # 시간대별 혼잡도: 장소의 과거 30일 간의 일자/시간대별 혼잡도 호출
    def get_data_areas(self, date, df):
        ids = [9273,9270]
        base_url = "https://apis.openapi.sk.com/puzzle/place/congestion/stat/raw/hourly/areas/"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "appKey":api_keys[api_key_index]
        }

        responses = {}
        for areas_id in ids:
            url = base_url + str(areas_id)
            query_params = "?date=" + str(date)
            full_url = url + query_params
            try:
                response = requests.get(full_url, headers=headers)
                response.raise_for_status()  # 오류가 있는 경우 예외 발생
                responses[areas_id] = response.json()
            except requests.exceptions.RequestException as e:
                print(f"Error occurred: {e}")
                print("Switching to the next API key...")
                self.switch_to_next_key()
                return self.get_data_areas(date, df) 

        for areas_id, response_data in responses.items():
            area_id = response_data['contents']['areaId']
            area_name = response_data['contents']['areaName']

            for item in response_data['contents']['raw']:
                congestion = item['congestion']
                congestion_level = item['congestionLevel']
                datetime = item['datetime']
                new = pd.DataFrame({
                    #'Id': area_id,
                    'ticker': [area_name],
                    'y': [congestion],
                    #'CongestionLevel': congestion_level,
                    'ds': [datetime]
                })
                df=pd.concat([df,new], ignore_index=True)

        return df
    
    def switch_to_next_key(self):
        # 다음 API 키로 전환하는 함수
        global api_key_index
        api_key_index = (api_key_index + 1) % len(api_keys)


class LoadDf():
    def __init__(self):
        self.df = pd.DataFrame(columns=['ticker', 'y', 'ds'])
        self.call = Call()

    def pois(self):
        pois_df = self.call().get_data_pois('ystday',self.df)
        return pois_df
        
    def area(self):
        area_df = self.get_data_areas('ystday',self.df)
        return area_df


#실시간 data 불러오기 - 1. Sk Api
api_keys=["w3oFktJUat2NPpDorwHZE7avbxcvdq0S7wx4vXfN","Tt3yyROHTM8op2hEyv1Z34AXC2x8KPbn1iuD5Hlc",
         "RNM43SFreC8YwWjFIAGHY4VIpOi6jDHG98AHf7rN","e8wHh2tya84M88aReEpXCa5XTQf3xgo01aZG39k5"]
api_key_index=0

class CallSkRltm():
    def get_rltm_pois(self, df):
        # 장소 id 리스트
        ids = [187961, 5783805, 5799875, 384515]
        # SK api 홈페이지에서 호출링크 가져옴
        base_url = "https://apis.openapi.sk.com/puzzle/place/congestion/rltm/pois/"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "appKey":api_keys[api_key_index]
        }
        # API 응답 저장할 빈 딕셔너리 생성
        responses = {}

        # for문으로 id리스트 이용, API 호출하기
        # id를 키로하여 Json형식으로 받아와서 저장
        for place_id in ids:
            url = base_url + str(place_id)
            #query_params = "?date=" + str(date)
            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()  # 오류가 있는 경우 예외 발생
                responses[place_id] = response.json()
            except requests.exceptions.RequestException as e:
                print(f"Error occurred: {e}")
                print("Switching to the next API key...")
                self.switch_to_next_key()
                return self.get_rltm_pois(df)


        # for문 reponse 딕셔너리 항목에서 키값으로 데이터 추출하고 각 변수에 저장
        for place_id, response_data in responses.items():
            #poi_id = response_data['contents']['poiId']
            poi_name = response_data['contents']['poiName']
            for item in response_data['contents']['rltm']:
                congestion = item['congestion']
                congestion_level = item['congestionLevel']
                datetime = item['datetime']

                # 'df'에 새로운 데이터 추가하고 인덱스 재설정
                new = pd.DataFrame({
                    #'Id': poi_id,
                    'ds': [datetime],
                    'ticker': [poi_name],
                    'y': [congestion],
                    'CongestionLevel': [congestion_level]
                })
                df=pd.concat([df, new], ignore_index=True)

        return df
    def get_rltm_areas(self, df):
        ids = [9273,9270]
        base_url = "https://apis.openapi.sk.com/puzzle/place/congestion/rltm/areas/"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "appKey":api_keys[api_key_index]
        }

        responses = {}
        for areas_id in ids:
            url = base_url + str(areas_id)
            #query_params = "?date=" + str(date)
            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()  # 오류가 있는 경우 예외 발생
                responses[areas_id] = response.json()
            except requests.exceptions.RequestException as e:
                print(f"Error occurred: {e}")
                print("Switching to the next API key...")
                self.switch_to_next_key()
                return self.get_rltm_areas(df)


        for areas_id, response_data in responses.items():
            #area_id = response_data['contents']['areaId']
            area_name = response_data['contents']['areaName']

            congestion = response_data['contents']['rltm']['congestion']
            congestion_level = response_data['contents']['rltm']['congestionLevel']
            datetime = response_data['contents']['rltm']['datetime']
            new = pd.DataFrame({
                #'Id': area_id,
                'ds': [datetime],
                'ticker': [area_name],
                'y': [congestion],
                'CongestionLevel': [congestion_level],
            })
            df=pd.concat([df, new], ignore_index=True)
        return df
    
    def switch_to_next_key(self):
        # 다음 API 키로 전환하는 함수
        global api_key_index
        api_key_index = (api_key_index + 1) % len(api_keys)

        df = self.get_rltm_pois(df)
        df = self.get_rltm_areas(df)
        df.ds=pd.to_datetime(df.ds)
        df=df.fillna(0)
        df['y_100m2']=df['y']*100
        
        return df

class ToFile():
    def __init__(self):
        self.df = pd.DataFrame(columns=['ds','ticker', 'y', 'CongestionLevel'])
        self.call = CallSkRltm()

    def append_rltm_data(self):
        df = pd.read_csv('rltm_data.csv')
        if len(df)<144:
            df_new = self.call().rltm_poi()
            df_new = self.call().rltm_area()
            df=pd.concat([df, df_new], ignore_index=True)
            df.ds=pd.to_datetime(df.ds)
            print("New data fetched and appended.")
            
            #레벨
            bins=[0,0.0175,0.035,0.21,0.4,float('inf')]
            labels=['여유','보통','조금 혼잡','혼잡','매우 혼잡']
            num_labels=[1,2,3,4,5]
            df['level']=pd.cut(df['y'], bins=bins, labels=labels)
            df['num_level']=pd.cut(df['y'], bins=bins, labels=num_labels)
            
            #시각화(png, html로 저장)
            # self.visualize_rltm_data(df)
            df.to_csv('rltm_data.csv', index=False)
        
        else:
            df=df.iloc[0:0]
            df.to_csv('rltm_data.csv',index=False)
            self.append_rltm_data()