from django.shortcuts import render
import xml.etree.ElementTree as ET
import datetime as dt
import time
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
# from .serializer import SkAreasserializer, SkPoisSerializer
# from .callapi import sk_api_areas_congetion,sk_api_pois_congetion
import requests
import json

# Create your views here.

# save request
# seoul_area_list = ['강남 MICE 관광특구', '동대문 관광특구', '명동 관광특구', '이태원 관광특구', '잠실 관광특구', '종로·청계 관광특구', '홍대 관광특구', '경복궁·서촌마을', '광화문·덕수궁', '창덕궁·종묘', '가산디지털단지역', '강남역', '건대입구역', '고속터미널역', '교대역', '구로디지털단지역', '서울역', '선릉역', '신도림역', '신림역', '신촌·이대역', '역삼역', '연신내역', '용산역', '왕십리역', 'DMC(디지털미디어시티)', '창동 신경제 중심지', '노량진', '낙산공원·이화마을', '북촌한옥마을', '가로수길', '성수카페거리', '수유리 먹자골목', '쌍문동 맛집거리', '압구정로데오거리', '여의도', '영등포 타임스퀘어', '인사동·익선동', '국립중앙박물관·용산가족공원', '남산공원', '뚝섬한강공원', '망원한강공원', '반포한강공원', '북서울꿈의숲', '서울대공원', '서울숲공원', '월드컵공원', '이촌한강공원', '잠실종합운동장', '잠실한강공원']
# def get_seoul_hotspots(request):
# 	print("success")
# 	while True:
# 		for seoul_area in seoul_area_list:
# 			seoul_api_space(seoul_area)
# 		print("finish")
# 		time.sleep(60*30) # 30minutes


areainfo = {"롯데월드": {
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
# 잠실역, 잠실역 롯데월드, 방이동 먹자골목
sk_songpagu_areas_id = ["9273", "9270"]

# 롯데월드어드벤처, 롯데월드잠실점, 롯데백화점잠실점, 롯데마트제타플레
sk_songpagu_pois_id = ["5783805", "5799875", "188633"]



area = ["롯데월드", "방이동 먹자골목"] 
pois = ["롯데백화점", "롯데마트제타플레닛", "에비뉴엘월드타우점", "롯데월드몰", "올림픽공원" ]
SK_APP_KEY = 'BFE8BDtYZK553WvHLrnHxagtLvBEypDq9ClJQpAs'
# SK_APP_KEY = 'RNM43SFreC8YwWjFIAGHY4VIpOi6jDHG98AHf7rN'
# SK_APP_KEY = 'e8wHh2tya84M88aReEpXCa5XTQf3xgo01aZG39k5'
# SK_APP_KEY = '6nPa8A9ij41zGV7x7QAeR9x9y3MuLPEgjiHjbhhc'
# SK_APP_KEY = 'W9DXjZKgAg4bVZwjN90m14SxPppyMoRzcYiBAB72'
# SK_APP_KEY = 'Tt3yyROHTM8op2hEyv1Z34AXC2x8KPbn1iuD5Hlc'
area = ["롯데월드", "방이동먹자골목","에비뉴엘월드타워점", "롯데월드몰", "올림픽공원" ]


def SkOpenApi(url): # json serialize
    url = url
    response = requests.get(url)
    hotspots_data = response.content.decode('utf-8')
    json_data = json.loads(hotspots_data)
    return json_data


def sk_api_areas_congetion(areaid, num, area):
    app_key = SK_APP_KEY
    jsonobject = SkOpenApi(f'https://apis.openapi.sk.com/puzzle/place/congestion/rltm/areas/{areaid}?appkey={app_key}')
    congestion = jsonobject['contents']['rltm']['congestion']
    congestion = renamelevel(congestion)

    datetime = jsonobject['contents']['rltm']['datetime']
    y = datetime[:4]
    M = datetime[4:6]
    d = datetime[6:8]
    h = datetime[8:10]
    m = datetime[10:12]
    s = datetime[12:]
    datetime_format = f"{y}년{M}월{d}일 {h}.{m}.{s}"
  
    area  = str(area[num])
    areainfo[area] = {
        "congestion_level": congestion,
        "datetime":  datetime_format
    }
    print(areainfo[area])
    return areainfo
    
def sk_api_pois_congetion(poiid,num,area):
  app_key = SK_APP_KEY
  jsonobject = SkOpenApi(f'https://apis.openapi.sk.com/puzzle/place/congestion/rltm/pois/{poiid}?appkey={app_key}')
  datetime = jsonobject['contents']['rltm'][0]['datetime']
  congestion = jsonobject['contents']['rltm'][0]['congestion']
  congestion = renamelevel(congestion)
  
  area = str(area[num])
  y = datetime[:4]
  M = datetime[4:6]
  d = datetime[6:8]
  h = datetime[8:10]
  m = datetime[10:12]
  s = datetime[12:]
  datetime_format = f"{y}년{M}월{d}일 {h}.{m}.{s}"
  areainfo[area] = {
        "congestion_level": congestion,
        "datetime": datetime_format
    }
  print(areainfo[area])
  return areainfo
    
def get_sk_hotspots(request):
    area_count = 0
    for sk_areaid in sk_songpagu_areas_id:
        areainfo = sk_api_areas_congetion(sk_areaid, area_count, area)
        area_count += 1
    print("sk_area_finish")
    for sk_poiid in sk_songpagu_pois_id:
        areainfo = sk_api_pois_congetion(sk_poiid, area_count, area)
        area_count += 1
    json_data = json.dumps(areainfo,ensure_ascii=False)

    return JsonResponse(areainfo, json_dumps_params={'ensure_ascii': False}, safe=False, content_type='application/json')

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

롯데백화점잠실점 = {
    "status": {
      "code": "00",
      "message": "success",
      "totalCount": 1
    },
    "contents": {
      "poiId": "188485",
      "poiName": "롯데백화점잠실점",
      "rltm": [
        {
          "datetime": "20230704012000",
          "congestion": 0.00004,
          "congestionLevel": 1,
          "type": 1
        }
      ]
    }
  }


    

롯데월드 ={"status": {"code": "00","message": "success","totalCount": 1},"contents": {"areaId": "9273","areaName": "롯데월드","rltm": {"congestion": 0.01541,"congestionLevel": 1,"datetime": "20230701002000"}}}

# 0.0175
# 0.03
# 0.2
# 0.4
# 0.4