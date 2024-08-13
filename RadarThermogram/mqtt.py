import paho.mqtt.client as mqtt
import ssl
import keyboard
import time
import json
import matplotlib.pyplot as plt
import numpy as np

# 设置字体以支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定黑体
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

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


position = None


def on_message(client, userdata, msg):
    global position
    string_content = msg.payload.decode("utf-8")
    json_content = json.loads(string_content)
    position = json_content['services'][0]['properties']['position']
    # print(f"Position updated: {position}")
    return position


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
    global position
    client = mqtt.Client(client_id=CLIENT_ID)

    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message

    client.username_pw_set(username=BROKER_USERNAME, password=BROKER_PASSWORD)

    client.tls_set(ca_certs=None, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
                   tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

    client.connect(BROKER_HOSTNAME, port=BROKER_PORT, keepalive=60)
    print(client.on_message)

    client.loop_start()

    try:
        while True:
            if keyboard.is_pressed('esc'):
                print("ESC pressed, exiting...")
                break

            if position is not None:
                print(f"Current position: {position}")
                plot_positions(position)

            else:
                print("Waiting for position update...")

            time.sleep(5)
    except KeyboardInterrupt:
        print("Program interrupted by user.")

    client.disconnect()
    client.loop_stop()


def plot_positions(position_str):
    # 移除多余的空格并用分号分割字符串
    parts = [part.strip() for part in position_str.split(';') if part.strip()]

    # 初始化两个空数组
    x = []
    y = []

    # 遍历分割后的每一部分，并按逗号分开
    for part in parts:
        before, after = part.split(',')
        x.append(float(before))
        y.append(float(after))

    # 创建图形
    plt.figure(figsize=(8, 6))

    # 在原点处绘制小盒子 (矩形)
    box_size = 0.5  # 盒子的大小
    rectangle = plt.Rectangle((-box_size / 2, -box_size / 2), box_size, box_size, color='green', alpha=0.5)
    plt.gca().add_patch(rectangle)

    # 绘制点
    plt.scatter(x, y, color='blue', marker='o')

    # 设置图形标题和标签
    plt.title('人员实时相对位置')
    plt.xlabel('X /m')
    plt.ylabel('Y /m')

    # 设置坐标轴范围
    plt.xlim(-8, 8)
    plt.ylim(-8, 8)

    # 绘制坐标轴经过原点
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # y=0 轴
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # x=0 轴

    # 显示网格
    plt.grid(True)

    plt.savefig("image/output/position.png")
    print("图片已刷新")
    # 显示图形
    plt.show()


# 使用函数时，将 position_str 作为参数传递
# 例如：
# position_str = "-2.1,1.3; 0,0 ; 0,0 ; 0,0 ; 0,0 ;"
# plot_positions(position_str)


if __name__ == '__main__':
    get_position()
