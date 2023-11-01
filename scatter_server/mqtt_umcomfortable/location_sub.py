import paho.mqtt.client as mqtt
from mqtt_umcomfortable.geo_distance import geo_distance, radius, coordinate
from mqtt_umcomfortable.pushalarm_pub import pushalarm


coordinate = coordinate
radius = radius
area = ""

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", str(rc))
    


def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    latitude, longitude = map(float, payload.split(',')[:2])
    firebasetoken = payload.split(',')[2]
    geo_distance(latitude , longitude, firebasetoken)
    firebasetoken = ""

    # 지역 내에 들어오면 알림 보내기 && 혼잡도
    # if area != area:
    #     pushalarm(area)

    print("Received location:", latitude, longitude)


client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.subscribe("location")

def location_subscribe():
    try:
        host_id = "115.21.135.45"
        port = 1883  # 수정: 포트 번호를 정수로 전달
        client.connect(host_id, port, 60)
        client.subscribe("location")
        client.loop_forever()
    except Exception as err:
        print('error:', err)

location_subscribe()