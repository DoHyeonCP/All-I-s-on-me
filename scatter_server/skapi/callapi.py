#-*- coding: utf-8 -*-
import requests
import json
from django.conf import settings
from .models import SKJsonAreasData,SkJsonPoisData


class CallApi(): 
    def __init__(self): 
        self.areainfo = {"롯데월드": { # 전송할 데이터를 담을 dict
        "datetime" : "",
        "congestion_level" : 0
            }, 
            "방이동먹자골목":{
                "datetime" : "",
                "congestion_level" : 0
                
            },
            "에비뉴엘월드타워점":{
                "datetime" : "",
        "congestion_level" : 0
                
            }, 
            "롯데월드몰":{
                "datetime" : "",
        "congestion_level" : 0
            }, 
            "올림픽공원":{
                "datetime" : "",
        "congestion_level" : 0
            }}
        self.sk_songpagu_areas_id = ["9273", "9270"]
        self.sk_songpagu_pois_id = ["5783805", "5799875", "188633"]

    def SkOpenApi(self, url): # json serialize
        url = url
        response = requests.get(url)
        hotspots_data = response.content.decode('utf-8')
        json_data = json.loads(hotspots_data)
        return json_data


    def sk_api_pois_congetion(self, poiid):
        app_key = settings.SK_APP_KEY
        json_data = self.SkOpenApi(f'https://apis.openapi.sk.com/puzzle/place/congestion/rltm/pois/{poiid}?appkey={app_key}')

        json_obj = SkJsonPoisData(
            sk_pois_data = json_data
        )
        json_obj.save()

    def sk_api_areas_congetion(self, areaid, area_n):
        app_key = settings.SK_APP_KEY
        json_data = self.SkOpenApi(f'https://apis.openapi.sk.com/puzzle/place/congestion/rltm/areas/{areaid}?appkey={app_key}')
        self.areapashing(json_data, area_n)

        json_obj = SKJsonAreasData(
            sk_areas_data = json_data
        )
        json_obj.save()
        

    def get_sk_hotspots(request):
        print("success")
        while True:
            for sk_areaid in self.sk_songpagu_areas_id:
                self.sk_api_areas_congetion(sk_areaid)
            print("sk_area_finish")
            for sk_poiid in self.sk_songpagu_pois_id:
                self.sk_api_pois_congetion(sk_poiid)
            print("sk_poi_finish")
            
    def areapashing(self, json):
        jsonobject = json.loads(json)
        area= jsonobject.get("contents").get("areaname")
        congestion = jsonobject.get("contents").get("rltm").get("congestionLevel")
        datetime = jsonobject.get("contents").get("rltm").get("datetime")
        data = (area, congestion, datetime)
        

    def renamelevel(congestion):
        if congestion < 0.0175:
            return "여유"
        elif congestion <= 0.035:
            return "보통"
        elif congestion <= 0.21:
            return "조금혼잡"
        elif congestion <= 0.4:
            return "혼잡"
        elif congestion > 0.4:
            return "매우혼잡"

    def update_congestion_data(self):
            for sk_areaid in self.sk_songpagu_areas_id:
                self.sk_api_areas_congestion(sk_areaid)
            for sk_poiid in self.sk_songpagu_pois_id:
                self.sk_api_pois_congestion(sk_poiid)


# 배치 작업에서 사용할 함수
def update_congestion_data_batch():
    api = CallApi()
    api.update_congestion_data()