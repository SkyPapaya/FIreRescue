import matplotlib.pyplot as plt
from collections import deque
import cv2
import numpy as np


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


# 读取图像
image_path = './img/image1.png'
image = cv2.imread(image_path)

# 转换为只含有0和1的矩阵
building = convert_to_binary(image)

# 定义起始位置
start = (400, 400)  # 起始位置


# 定义结合DFS和BFS的算法
def combined_search(building, start):
    rows, cols = len(building), len(building[0])  # 获取建筑的行数和列数
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 定义四个移动方向：右、左、下、上
    stack = [start]  # 使用栈来实现深度优先搜索（DFS）
    queue = deque([start])  # 使用队列来记录已经探索过但还未完全展开的节点
    visited = set()  # 记录已访问的节点
    path = []  # 记录遍历路径

    while stack or queue:  # 当栈或队列不为空时继续循环
        if stack:  # 优先使用DFS
            current = stack.pop()
        else:  # 当栈为空时，使用队列中的节点继续搜索
            current = queue.popleft()

        if current not in visited:  # 如果当前节点未被访问
            visited.add(current)  # 将当前节点标记为已访问
            path.append(current)  # 将当前节点添加到路径中
            for direction in directions:  # 遍历所有可能的移动方向
                neighbor = (current[0] + direction[0], current[1] + direction[1])
                if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:  # 检查邻居节点是否在建筑范围内
                    if building[neighbor[0]][neighbor[1]] == 0 and neighbor not in visited:  # 检查邻居节点是否可通过且未访问
                        stack.append(neighbor)  # 将邻居节点添加到栈中
                        queue.append(neighbor)  # 将邻居节点添加到队列中

    return path  # 返回覆盖所有区域的路径


# 调用算法函数获取遍历路径
path = combined_search(building, start)

# 可视化
plt.figure(figsize=(8, 8))  # 设置图像大小
plt.imshow(building, cmap='Greys', origin='lower')  # 显示建筑地图，1表示白色（可通过），0表示黑色（障碍物）

# 绘制起始点
plt.plot(start[1], start[0], 'rx', markersize=10)  # 红色'x'标记起始位置

# 绘制路径
if path:
    path_x, path_y = zip(*path)  # 分离路径的x和y坐标
    plt.plot(path_y, path_x, marker='o', color='blue')  # 绘制蓝色路径

plt.gca().invert_yaxis()  # 反转y轴，使(0,0)在左上角
plt.show()  # 显示图像

# 输出路径坐标
if path:
    print("路径坐标:", path)
