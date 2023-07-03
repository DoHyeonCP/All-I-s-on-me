import json
import requests

# 잠실역, 잠실역 롯데월드, 방이동 먹자골목
sk_songpagu_areas_id = ["9273", "9270"]

# 롯데월드어드벤처, 롯데월드잠실점, 롯데백화점잠실점, 롯데마트제타플레
sk_songpagu_pois_id = ["188485", "188592", "5783805", "5799878", "188633"]


areainfo = {"롯데월드": (), 
	    "방이동먹자골목":(),
		"롯데백화점":(), 
		"롯데마트제타플레닛":(), 
		"에비뉴엘월드타워점":(), 
		"롯데월드몰":(), 
		"올림픽공원":()}
area = ["롯데월드", "방이동 먹자골목"] 
pois = ["롯데백화점", "롯데마트제타플레닛", "에비뉴엘월드타우점", "롯데월드몰", "올림픽공원" ]
SK_APP_KEY = 'BFE8BDtYZK553WvHLrnHxagtLvBEypDq9ClJQpAs'
areainfo = {"롯데월드": (), 
	    "방이동먹자골목":(),
		"롯데백화점":(), 
		"롯데마트제타플레닛":(), 
		"에비뉴엘월드타워점":(), 
		"롯데월드몰":(), 
		"올림픽공원":()}

area = ["롯데월드", "방이동먹자골목", "롯데백화점", "롯데마트제타플레닛", "에비뉴엘월드타워점", "롯데월드몰", "올림픽공원" ]

def SkOpenApi(url): # json serialize
    url = url
    response = requests.get(url)
    hotspots_data = response.content.decode('utf-8')
    json_data = json.loads(hotspots_data)
    return json_data


def sk_api_areas_congetion(areaid, num):
    app_key = SK_APP_KEY
    jsonobject = SkOpenApi(f'https://apis.openapi.sk.com/puzzle/place/congestion/rltm/areas/{areaid}?appkey={app_key}')
    area= jsonobject.get("contents").get("areaName")
    congestion = jsonobject.get("contents").get("rltm").get("congestionLevel")
    datetime = jsonobject.get("contents").get("rltm").get("datetime")
    data = (datetime,area,congestion)
    area  = str(area[num])
    areainfo[area] = data
    print(areainfo[area])

def sk_api_pois_congetion(poiid,num,area):
    app_key = SK_APP_KEY
    jsonobject = SkOpenApi(f'https://apis.openapi.sk.com/puzzle/place/congestion/rltm/pois/{poiid}?appkey={app_key}')
    poi = jsonobject.get("contents").get("poiName")
    poiArray = jsonobject.get("contents").get("rltm")
    congestion = 0
    datetime = ""
    for lst in poiArray:
        if lst == datetime:
            datetime = str(lst.get("datetime"))
        if lst == "congestionLevel":
            congestion = lst.get("congestionLevel")       
    data = (datetime,poi,congestion)
    area = str(area[num])
    areainfo[area] = data
    print(areainfo[area])
	

def get_sk_hotspots(request):
    print("success")
    area_count = 0
    for sk_areaid in sk_songpagu_areas_id:
        sk_api_areas_congetion(sk_areaid, area_count)
        area_count += 1
        
    print("sk_area_finish")

    for sk_poiid in sk_songpagu_pois_id:
        sk_api_pois_congetion(sk_poiid, area_count, area)
        area_count += 1

    json_data = json.dumps(areainfo)


# get_sk_hotspots()
json_data = json.dumps(areainfo)
print(json_data)



# for i in areainfo.keys():
#     print(areainfo[i])


