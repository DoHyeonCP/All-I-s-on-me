#-*- coding: utf-8 -*-
import xmltodict
import requests
import json
from django.conf import settings
from .models import SKJsonAreasData,SkJsonPoisData

# def seoul_api_space(area):
# 	api_key = settings.SEOUL_API_KEY
# 	url = f'http://openapi.seoul.go.kr:8088/{api_key}/xml/citydata/1/20/{area}'
# 	print(' get_seoul_hotspots')
# 	response = requests.get(url)
# 	hotspots_data = response.content.decode('utf-8')

# 	xml_dict = xmltodict.parse(hotspots_data)
# 	json_data = json.dumps(xml_dict, ensure_ascii=False)
# 	parsed_data = json.loads(json_data)
# 	area_nm = parsed_data['SeoulRtd.citydata']['CITYDATA']['AREA_NM']
# 	json_obj = SeoulJsonData(
# 		area_nm = area_nm,
# 		seoul_data = json_data
# 	)
# 	json_obj.save()


def SkOpenApi(url): # json serialize
    url = url
    response = requests.get(url)
    hotspots_data = response.content.decode('utf-8')
    json_data = json.loads(hotspots_data)
    return json_data


def sk_api_pois_congetion(poiid):
    app_key = settings.SK_APP_KEY
    json_data = SkOpenApi(f'https://apis.openapi.sk.com/puzzle/place/congestion/rltm/pois/{poiid}?appkey={app_key}')

    json_obj = SkJsonPoisData(
        sk_pois_data = json_data
    )
    json_obj.save()




def sk_api_areas_congetion(areaid, area_n):
    app_key = settings.SK_APP_KEY
    json_data = SkOpenApi(f'https://apis.openapi.sk.com/puzzle/place/congestion/rltm/areas/{areaid}?appkey={app_key}')
    areapashing(json_data, area_n)

    json_obj = SKJsonAreasData(
        sk_areas_data = json_data
    )
    json_obj.save()
    
sk_songpagu_areas_id = ["9270", "9272", "9273"]
# 롯데월드어드벤처, 롯데월드잠실점, 롯데백화점잠실점, 롯데마트제타플레
sk_songpagu_pois_id = ["6967166","187691","188485","188592","5783805","5799875","384515","188633"]
def get_sk_hotspots(request):
	print("success")
	while True:
		for sk_areaid in sk_songpagu_areas_id:
			sk_api_areas_congetion(sk_areaid)
		print("sk_area_finish")
		for sk_poiid in sk_songpagu_pois_id:
			sk_api_pois_congetion(sk_poiid)
		print("sk_poi_finish")
		
def areapashing(json):
	jsonobject = json.loads(json)
	area= jsonobject.get("contents").get("areaname")
	congestion = jsonobject.get("contents").get("rltm").get("congestionLevel")
	datetime = jsonobject.get("contents").get("rltm").get("datetime")
	data = (area, congestion, datetime)
	
	
    

def poipshing(json):
	jsonobject = json.loads(json)
	poi = jsonobject.get("contents").get("poiname")
	congestion = jsonobject.get("contents").get("rltm").get("congestionLevel")
	datetime = jsonobject.get("contents").get("rltm").get("datetime")
	
	

# def sk_api_pois_areas_congetion(poiid = None, areaid = None):
#     app_key = settings.SK_APP_KEY
#     areas_json_data = SkOpenApi(f'https://apis.openapi.sk.com/puzzle/place/congestion/stat/raw/hourly/areas/{areaid}?appkey={app_key}')
#     pois_json_data = SkOpenApi(f'https://apis.openapi.sk.com/puzzle/place/congestion/stat/raw/hourly/pois/{poiid}?appkey={app_key}')
#     json_obj = SkJsonPoisAreasHourData(
#         sk_pois_hour_data = pois_json_data,
#         sk_areas_hour_data = areas_json_data
#     )
#     json_obj.save()
 
# 시간대별 장소 혼잡도 https://apis.openapi.sk.com/puzzle/place/congestion/stat/raw/hourly/pois/{poiId}
# 시간대별 상권 혼잡도 https://apis.openapi.sk.com/puzzle/place/congestion/stat/raw/hourly/areas/{areaId}