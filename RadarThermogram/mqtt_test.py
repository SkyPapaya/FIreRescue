import paho.mqtt.client as mqtt
import ssl
import keyboard
import time
import json

# MQTT broker configuration
BROKER_HOSTNAME = "5e1d9e2307.st1.iotda-device.cn-north-4.myhuaweicloud.com"
BROKER_PORT = 8883
BROKER_USERNAME = "65feba432ccc1a58387dee47_java_server_01"
BROKER_PASSWORD = "da130da385d816b06447f2db309b25249a60913742c56fa4cc2d6aba9472b5cf"
CLIENT_ID = "65feba432ccc1a58387dee47_java_server_01_0_0_2024071308"

# Topic configuration
SUBSCRIBE_TOPIC = "$devices/java_server_01/user/get_post"
PUBLISH_TOPIC = "$oc/devices/65feba432ccc1a58387dee47_java_server_01/sys/properties/report"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker")
        client.subscribe(SUBSCRIBE_TOPIC)
    else:
        print("Failed to connect, return code %d\n", rc)


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print('Unexpected disconnection.')


def on_message(client, userdata, msg):
    string_content = msg.payload.decode("utf-8")
    # 解析JSON字符串
    json_content = json.loads(string_content)

    # 获取position信息
    position = json_content['services'][0]['properties']

    print(position)
    print("get message")
    # print("get message")
    # print(f"Received message: {msg.topic} -> {str(msg.payload)}")
    return


def publish_message(client):
    payload = {
        "services": [
            {
                "service_id": "BaseStatics",
                "properties": {
                    "timestamp": int(time.time()),
                    "exist": 1,
                },
                "event_time": int(time.time())
            }
        ]
    }
    message = json.dumps(payload)
    client.publish(PUBLISH_TOPIC, message)


def get_position():
    client = mqtt.Client(client_id=CLIENT_ID)

    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message

    client.username_pw_set(username=BROKER_USERNAME, password=BROKER_PASSWORD)

    client.tls_set(ca_certs=None, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
                   tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

    client.connect(BROKER_HOSTNAME, port=BROKER_PORT, keepalive=60)

    client.loop_start()

    try:
        while True:
            if keyboard.is_pressed('esc'):
                print("ESC pressed, exiting...")
                break
            time.sleep(5)
            #publish_message(client)
            #print("Message published...")
    except KeyboardInterrupt:
        print("Program interrupted by user.")

    client.disconnect()
    client.loop_stop()


if __name__ == '__main__':
    get_position()
