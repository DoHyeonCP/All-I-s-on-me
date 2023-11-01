import paho.mqtt.client as mqtt

def on_connect(client, userdata, falgs, rc):
    print("Connected with result code", str(rc))
    client.subscribe("location")
        
        
def on_message(client,userdata,msg):
    value = float(msg.payload.decode())
    print(value.topic + " " + str(value.payload))

    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


def location_subscribe():
    try:
        host_id = "172.30.67.117"
        port = 1883
        client.connect(host_id, port)
        client.loop_forever()
    except Exception as err:
        print('error : %s'%err)

location_subscribe()
        



