#-*- coding: utf-8 -*-
import requests
from django.conf import settings
from .models import AreaInfo
import logging

class SkCallCongestion():
    def __init__(self):
        self.api_parser = SkApiParsing()

    def get_api(self, url): # json serialize
        response = requests.get(url)
        print(response)
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
        
        area= jsonobject.get("contents").get("areaName")
        rltm_data = jsonobject.get("contents").get("rltm")
        congestion = rltm_data.get("congestion")
        datetime = rltm_data.get("datetime")

        dateTimeFormat = self.datetime_format(datetime)
        congestion_level = self.renamelevel(congestion)
        
        if area and datetime and congestion_level:
            try:
                json_obj = AreaInfo(area_name= area,
                                    datetime = dateTimeFormat,
                                    congestion_level = congestion_level)
                json_obj.save()
            except Exception as e:
                    # Handle any exceptions that occur during the save operation
                    print(f"An error occurred while saving: {e}")

    def pois_parsing(self, json):
        jsonobject = json

        poi_name = jsonobject.get("contents").get("poiName")
        rltm_list = jsonobject.get("contents").get("rltm", [])

        if rltm_list:  # Check if the list is not empty
            rltm_data = rltm_list[0]  # Get the first item
            congestion = rltm_data.get("congestion")
            datetime_str = rltm_data.get("datetime")

            dateTimeFormat = self.datetime_format(datetime_str)
            congestion_level = self.renamelevel(congestion)
            
            if poi_name and dateTimeFormat and congestion_level is not None:
                try:
                    # Using update_or_create to avoid duplicate entries for the same area and datetime
                    json_obj = AreaInfo(area_name= poi_name,
                                datetime = dateTimeFormat,
                                congestion_level = congestion_level)
                    json_obj.save()
                except Exception as e:
                    # Handle any exceptions that occur during the save operation
                    print(f"An error occurred while saving: {e}")

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

class UpdateSkAPi:
    def __init__(self):
        self.sk_songpagu_areas_id = ["9273", "9270"]
        self.sk_songpagu_pois_id = ["5783805", "5799875", "188633"]
        self.sk_call_congestion = SkCallCongestion()

    def update_congestion_data(self):
        for sk_areaid in self.sk_songpagu_areas_id:
            self.sk_call_congestion.areas_get(sk_areaid)
        logging.info("save areas to AreaInfo")
        for sk_poiid in self.sk_songpagu_pois_id:
            self.sk_call_congestion.pois_get(sk_poiid)
        logging.info("save pois to AreaInfo")