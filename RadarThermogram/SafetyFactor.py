import matplotlib.pyplot as plt
import cv2
import numpy as np
import pandas as pd
import seaborn as sns
import SearchRoute as sr
import GetPosition as gp


# import rospy
# from std_msgs.msg import String
# #获取消息
# def chatter_callback(msg):
#     rospy.loginfo("Received message: %s", msg.data)
#     return msg.data
# 计算安全值权重
def safety_factor(smoke, co, fire, temperature, humidity):
    return temperature * 0.1 + humidity * 0.1 + smoke * 0.8


# 根据传感器读数更新安全系数
def renew_safety_factor(temperature, humidity, smoke, co, fire):
    return safety_factor(temperature, humidity, smoke, co, fire)


# 将图像转换为二值矩阵
def convert_to_binary(img):
    # 转换为灰度图
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 根据像素亮度设置阈值
    _, binary_img = cv2.threshold(gray_img, 230, 255, cv2.THRESH_BINARY)

    # 反转二值图像
    inverted_binary_img = cv2.bitwise_not(binary_img)

    # 将二值图像转换为只含有0和1的矩阵
    binary_matrix = (inverted_binary_img / 255).astype(np.uint8)
    return binary_matrix


def get_data_frame():
    # 读取图像
    image_path = './img/map_new.png'
    image = cv2.imread(image_path)

    # 转换为只含有0和1的矩阵
    building = convert_to_binary(image)

    # 获取图像的尺寸
    rows, cols = building.shape

    # 确认起始位置在图像范围内
    start = (min(400, rows - 1), min(400, cols - 1))  # 起始位置

    # 主函数
    # 初始化无人机当前位置
    positionX, positionY = gp.get_initial_position()

    # 设置初始传感器参数
    smoke = 1
    humidity = 1
    temperature = 2
    co = 3
    fire = 4

    # 初始化安全系数数据
    safety_factor_data = safety_factor(smoke, humidity, temperature, co, fire)

    # 执行搜索以获取路径
    path = sr.get_initial_path(building, start)

    # 动态更新建筑矩阵中的安全系数
    for pos in path:
        # 模拟传感器数据更新
        smoke = np.random.randint(1, 4)
        humidity = np.random.randint(1, 3)
        temperature = np.random.randint(1, 3)

        # 根据更新的传感器数据更新安全系数
        safety_factor_data = renew_safety_factor(temperature, humidity, smoke, co, fire)

        # 更新当前路径点的建筑矩阵
        building[pos[0]][pos[1]] = safety_factor_data

        # 将二值矩阵转换为DataFrame
        df = pd.DataFrame(building)
        return df


# 设置颜色映射
cmap = "RdYlGn_r"  # 选择热力图颜色映射
# 绘制热力图
plt.figure(figsize=(12, 12))  # 设置图像大小
sns.heatmap(get_data_frame(), cmap=cmap, square=True, cbar=True)  # 绘制热力图
plt.gca().invert_yaxis()  # 反转y轴，使(0,0)在左上角
plt.show()  # 显示图像
