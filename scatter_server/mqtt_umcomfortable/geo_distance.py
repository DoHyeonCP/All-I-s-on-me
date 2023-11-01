from haversine import haversine
from mqtt_umcomfortable.pushalarm_pub import *
# 지역들의 중심 좌표의 이중배열만들기
# coordinate['롯데마트제타플렉스점'] = (37.511612, 127.096311)
# coordinate['롯데백화점잠실점'] = (37.512160, 127.099437)
coordinate = {
    '롯데월드': (37.515358,127.101563),
    '롯데백화점에비뉴엘월드타워점': (37.512739,127.102087),
    '롯데월드몰': (37.513714,127.104169),
    '방이동먹자골목': (37.514503,127.108618),
    '올림픽공원': (37.520213,127.122233),
    # 디버깅용
    '우리집(부천)': (37.5332853, 126.80263334)
}

# 지역들의 범위 반지름 구하기 진입전 인도까지의 거리 m/ 구글지도로 측정
# radius['롯데백화점에비뉴엘월드타워점'] = 42
# radius['롯데월드몰'] = 84

radius = {
    '롯데월드': 230,
    '롯데백화점에비뉴엘월드타워점': 170,
    '롯데월드몰': 140,
    '방이동먹자골목': 290,
    '올림픽공원': 960,
    # 디버깅용
    '우리집(부천)': 500
}

# 지역list
area = ('롯데월드', '롯데백화점에비뉴엘월드타워점', '롯데월드몰', '방이동먹자골목', '올림픽공원', '우리집(부천)')
# 중심좌표와 범위반지름과 현재위치 정보를 받는 함수 만들기
# if(중심좌표와 중심좌표의 거리가 범위반지름보다 작으면 return 1 || 0
def geo_distance(latitude, longitude, firebasetoken):
    null = ""
    for a in area:
        client_location = (latitude, longitude)
        distance = haversine(coordinate[a], client_location, unit = 'm')
        print(distance)
        if distance <= radius[a]:
            k = str(a)
            return pushalarm(k, str(firebasetoken))
    return null