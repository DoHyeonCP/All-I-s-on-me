# Create your views here.
# 완성될때까지 잠시 지우지 말기
# save request
# seoul_area_list = ['강남 MICE 관광특구', '동대문 관광특구', '명동 관광특구', '이태원 관광특구', '잠실 관광특구', '종로·청계 관광특구', '홍대 관광특구', '경복궁·서촌마을', '광화문·덕수궁', '창덕궁·종묘', '가산디지털단지역', '강남역', '건대입구역', '고속터미널역', '교대역', '구로디지털단지역', '서울역', '선릉역', '신도림역', '신림역', '신촌·이대역', '역삼역', '연신내역', '용산역', '왕십리역', 'DMC(디지털미디어시티)', '창동 신경제 중심지', '노량진', '낙산공원·이화마을', '북촌한옥마을', '가로수길', '성수카페거리', '수유리 먹자골목', '쌍문동 맛집거리', '압구정로데오거리', '여의도', '영등포 타임스퀘어', '인사동·익선동', '국립중앙박물관·용산가족공원', '남산공원', '뚝섬한강공원', '망원한강공원', '반포한강공원', '북서울꿈의숲', '서울대공원', '서울숲공원', '월드컵공원', '이촌한강공원', '잠실종합운동장', '잠실한강공원']
# def get_seoul_hotspots(request):
# 	print("success")
# 	while True:
# 		for seoul_area in seoul_area_list:
# 			seoul_api_space(seoul_area)
# 		print("finish")
# 		time.sleep(60*30) # 30minutes

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


# def SkOpenApi(url): # json serialize
#     url = url
#     response = requests.get(url)
#     hotspots_data = response.content.decode('utf-8')
#     json_data = json.loads(hotspots_data)
#     return json_data


# def sk_api_areas_congetion(areaid, num, area):
#     app_key = SK_APP_KEY
#     jsonobject = SkOpenApi(f'https://apis.openapi.sk.com/puzzle/place/congestion/rltm/areas/{areaid}?appkey={app_key}')
#     congestion = jsonobject['contents']['rltm']['congestion']
#     congestion = renamelevel(congestion)

#     datetime = jsonobject['contents']['rltm']['datetime']
#     y = datetime[:4]
#     M = datetime[4:6]
#     d = datetime[6:8]
#     h = datetime[8:10]
#     m = datetime[10:12]
#     s = datetime[12:]
#     datetime_format = f"{y}년{M}월{d}일 {h}.{m}.{s}"
  
#     area  = str(area[num])
#     areainfo[area] = {
#         "congestion_level": congestion,
#         "datetime":  datetime_format
#     }
#     print(areainfo[area])
#     return areainfo
    
# def sk_api_pois_congetion(poiid,num,area):
#   app_key = SK_APP_KEY
#   jsonobject = SkOpenApi(f'https://apis.openapi.sk.com/puzzle/place/congestion/rltm/pois/{poiid}?appkey={app_key}')
#   datetime = jsonobject['contents']['rltm'][0]['datetime']
#   congestion = jsonobject['contents']['rltm'][0]['congestion']
#   congestion = renamelevel(congestion)
  
#   area = str(area[num])
#   y = datetime[:4]
#   M = datetime[4:6]
#   d = datetime[6:8]
#   h = datetime[8:10]
#   m = datetime[10:12]
#   s = datetime[12:]
#   datetime_format = f"{y}년{M}월{d}일 {h}.{m}.{s}"
#   areainfo[area] = {
#         "congestion_level": congestion,
#         "datetime": datetime_format
#     }
#   print(areainfo[area])
#   return areainfo
    
# area = ["롯데월드", "방이동 먹자골목"] 
# pois = ["롯데백화점", "롯데마트제타플레닛", "에비뉴엘월드타우점", "롯데월드몰", "올림픽공원" ]

    # sk_songpagu_areas_id = ["9270", "9272", "9273"]
    # # 롯데월드어드벤처, 롯데월드잠실점, 롯데백화점잠실점, 롯데마트제타플레
    # sk_songpagu_pois_id = ["6967166","187691","188485","188592","5783805","5799875","384515","188633"]
    # def poipshing(json):
    #     jsonobject = json.loads(json)
    #     poi = jsonobject.get("contents").get("poiname")
    #     congestion = jsonobject.get("contents").get("rltm").get("congestionLevel")
    #     datetime = jsonobject.get("contents").get("rltm").get("datetime")
# area = ["롯데월드", "방이동먹자골목","에비뉴엘월드타워점", "롯데월드몰", "올림픽공원" ]|

# SK_APP_KEY = 'RNM43SFreC8YwWjFIAGHY4VIpOi6jDHG98AHf7rN'
# SK_APP_KEY = 'e8wHh2tya84M88aReEpXCa5XTQf3xgo01aZG39k5'
# SK_APP_KEY = '6nPa8A9ij41zGV7x7QAeR9x9y3MuLPEgjiHjbhhc'
# SK_APP_KEY = 'W9DXjZKgAg4bVZwjN90m14SxPppyMoRzcYiBAB72'
# SK_APP_KEY = 'Tt3yyROHTM8op2hEyv1Z34AXC2x8KPbn1iuD5Hlc'

# self.areainfo = {"롯데월드": { # 전송할 데이터를 담을 dict
#         "datetime" : "",
#         "congestion_level" : 0
#             }, 
#             "방이동먹자골목":{
#                 "datetime" : "",
#                 "congestion_level" : 0
                
#             },
#             "에비뉴엘월드타워점":{
#                 "datetime" : "",
#         "congestion_level" : 0
                
#             }, 
#             "롯데월드몰":{
#                 "datetime" : "",
#         "congestion_level" : 0
#             }, 
#             "올림픽공원":{
#                 "datetime" : "",
#         "congestion_level" : 0
#             }}

# Create your models here.
# class SkJsonPoisData(models.Model): # 지역
#     sk_pois_data = models.JSONField()
#     created_at = models.DateTimeField(auto_now_add = True)
    
# class SKJsonAreasData(models.Model): #상권
#     sk_areas_data = models.JSONField()
#     created_at = models.DateTimeField(auto_now_add = True)

    # def sk_open_api(self, url): # json serialize
    #     response = requests.get(url)
    #     hotspots_data = response.content.decode('utf-8')
    #     json_data = json.loads(hotspots_data)
    #     return json_data

    # def get_sk_hotspots(request):
    #     print("success")
    #     while True:
    #         for sk_areaid in self.sk_songpagu_areas_id:
    #             self.sk_api_areas_congetion(sk_areaid)
    #         print("sk_area_finish")
    #         for sk_poiid in self.sk_songpagu_pois_id:
    #             self.sk_api_pois_congetion(sk_poiid)
    #         print("sk_poi_finish")