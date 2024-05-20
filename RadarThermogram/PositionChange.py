import cv2
import numpy as np
import GetPosition as gp


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


def get_changed_position():
    # 读取图像
    image_path = './img/test_map_1.png'
    image = cv2.imread(image_path)

    # 转换为只含有0和1的矩阵
    building = convert_to_binary(image)

    # 获取图像的尺寸
    rows, cols = building.shape

    # 确认起始位置在图像范围内
    start = (min(400, rows - 1), min(400, cols - 1))  # 起始位置
    print(building)
    # 获取无人机初始坐标
    x = gp.get_initial_position()[0]
    y = gp.get_initial_position()[1]
    print(x)
    print(y)
    # 新初始化一个矩阵，它的大小和building一致，但是里面存放的数值是根据无人机初始坐标偏移之之后的值
    new_building = {}
    for i in range(rows):
        for j in range(cols):
            new_building[(i - x, j - y)] = building[(i, j)]
    return new_building
