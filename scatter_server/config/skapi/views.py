from django.shortcuts import render
import xml.etree.ElementTree as ET
import time
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
# from .serializer import SkAreasserializer, SkPoisSerializer
from .callapi import sk_api_areas_congetion,sk_api_pois_congetion,sk_api_pois_areas_congetion,seoul_api_space

# Create your views here.

# save request
seoul_area_list = ['강남 MICE 관광특구', '동대문 관광특구', '명동 관광특구', '이태원 관광특구', '잠실 관광특구', '종로·청계 관광특구', '홍대 관광특구', '경복궁·서촌마을', '광화문·덕수궁', '창덕궁·종묘', '가산디지털단지역', '강남역', '건대입구역', '고속터미널역', '교대역', '구로디지털단지역', '서울역', '선릉역', '신도림역', '신림역', '신촌·이대역', '역삼역', '연신내역', '용산역', '왕십리역', 'DMC(디지털미디어시티)', '창동 신경제 중심지', '노량진', '낙산공원·이화마을', '북촌한옥마을', '가로수길', '성수카페거리', '수유리 먹자골목', '쌍문동 맛집거리', '압구정로데오거리', '여의도', '영등포 타임스퀘어', '인사동·익선동', '국립중앙박물관·용산가족공원', '남산공원', '뚝섬한강공원', '망원한강공원', '반포한강공원', '북서울꿈의숲', '서울대공원', '서울숲공원', '월드컵공원', '이촌한강공원', '잠실종합운동장', '잠실한강공원']
def get_seoul_hotspots(request):
	print("success")
	while True:
		for seoul_area in seoul_area_list:
			seoul_api_space(seoul_area)
		print("finish")
		time.sleep(60*30) # 30minutes

# 잠실역, 잠실역 롯데월드, 방이동 먹자골목
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
		for sk_areaid in sk_songpagu_areas_id:
			sk_api_pois_areas_congetion(areaid = sk_areaid)
		for sk_poiid in sk_songpagu_pois_id:
			sk_api_pois_areas_congetion(poiid = sk_poiid)
		print("sk_pois_areas_hourly_finish")
		time.sleep(60*60) # 30minutes
		
	return HttpResponse('success')