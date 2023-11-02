#-*- coding: utf-8 -*-
import requests
from django.conf import settings
from .models import AreaInfo

class SkCallCongestion():
    def __init__(self):
        self.api_parser = SkApiParsing()

    def get_api(self, url): # json serialize
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        
        else:
            print("fail call sk_api")

    def pois_get(self, poiid):
        app_key = settings.SK_APP_KEY
        json_data = self.get_api(f'https://apis.openapi.sk.com/puzzle/place/congestion/rltm/pois/{poiid}?appkey={app_key}')
        if json_data:
            self.api_parser.pois_parsing(json_data)

    def areas_get(self, areaid):
        app_key = settings.SK_APP_KEY
        json_data = self.get_api(f'https://apis.openapi.sk.com/puzzle/place/congestion/rltm/areas/{areaid}?appkey={app_key}')
        if json_data:
            self.api_parser.area_parsing(json_data)

class SkApiParsing():
    def area_parsing(self, json):
        jsonobject = json

        area= jsonobject.get("contents").get("areaname")
        rltm_data = jsonobject.get("contents").get("rltm")
        congestion = rltm_data.get("congestionLevel")
        datetime = rltm_data.get("datetime")

        dateTimeFormat = self.datetime_format(datetime)
        congestion_level = self.renamelevel(congestion)
        
        if area and datetime and congestion_level:
            json_obj = AreaInfo(area_name= area,
                                datetime = dateTimeFormat,
                                congestion_level = congestion_level)
            json_obj.save()

    def pois_parsing(self, json):
        jsonobject = json

        area= jsonobject.get("contents", {}).get("areaname")
        rltm_data = jsonobject.get("contents", {}).get("rltm", {})
        congestion = rltm_data.get("congestionLevel")
        datetime = rltm_data.get("datetime")

        dateTimeFormat = self.datetime_format(datetime)
        congestion_level = self.renamelevel(congestion)
        
        if area and datetime and congestion_level:
            json_obj = AreaInfo(area_name= area,
                                datetime = dateTimeFormat,
                                congestion_level = congestion_level)
            json_obj.save()

    def datetime_format(self, datetime):
        y, M, d, h, m, s = datetime[:4],datetime[4:6],datetime[6:8],datetime[8:10],datetime[10:12],datetime[12:]
        dateTimeFormat = f"{y}년{M}월{d}일 {h}.{m}.{s}"
        return dateTimeFormat
        

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

