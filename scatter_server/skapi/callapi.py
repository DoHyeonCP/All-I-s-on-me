#-*- coding: utf-8 -*-
import requests
import json
from django.conf import settings
from .models import AreaInfo
from rest_framework.response import Response


class CallApi(): 
    def __init__(self): 
        self.sk_songpagu_areas_id = ["9273", "9270"]
        self.sk_songpagu_pois_id = ["5783805", "5799875", "188633"]

    def sk_open_api(self, url): # json serialize
        response = requests.get(url)
        hotspots_data = response.content.decode('utf-8')
        return hotspots_data.json()

    def sk_api_pois_congetion(self, poiid):
        app_key = settings.SK_APP_KEY
        json_data = self.SkOpenApi(f'https://apis.openapi.sk.com/puzzle/place/congestion/rltm/pois/{poiid}?appkey={app_key}')
        self.areapashing(json_data, area_n)
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
        
            
    def areapashing(self, json):
        jsonobject = json.loads(json)
        area= jsonobject.get("contents").get("areaname")
        congestion = jsonobject.get("contents").get("rltm").get("congestionLevel")
        datetime = jsonobject.get("contents").get("rltm").get("datetime")
        
        congestion_level = self.renamelevel(congestion)
        data = (area, congestion, datetime)
        

    def renamelevel(self, congestion):
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
        print("sk_area_finish")
        for sk_poiid in self.sk_songpagu_pois_id:
            self.sk_api_pois_congestion(sk_poiid)
        print("sk_poi_finish")


# 배치 작업에서 사용할 함수
def update_congestion_data_batch():
    AreaInfo.objects.All().delete()

    api = CallApi()
    api.update_congestion_data()