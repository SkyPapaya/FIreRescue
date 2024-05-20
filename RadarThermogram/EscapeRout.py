import matplotlib.pyplot as plt
import cv2
import numpy as np
from numpy.random import randint


# 转换图像为二值矩阵
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
image_path = './img/map_new.png'
image = cv2.imread(image_path)
binary_matrix = convert_to_binary(image)


# 初始化map类，定义地图的长宽，并设置保存地图信息的二维数据map的值为0，0表示可以移动到这个点
class Map():
    # 初始化地图信息
    def __init__(self, width, height, binary_matrix):
        self.width = width
        self.height = height
        self.map = binary_matrix

    # 随机获取可移动节点的函数，后面是否在这里进行起点的自定义？
    def generatePos(self, rangeX, rangeY):
        x, y = (randint(rangeX[0], rangeX[1]), randint(rangeY[0], rangeY[1]))
        while self.map[y][x] == 1:
            x, y = (randint(rangeX[0], rangeX[1]), randint(rangeY[0], rangeY[1]))
        return (x, y)

    # 获取地图
    def getMap(self):
        return self.map


# 地图信息可视化
def showMapWithColors(map, start, end, path=None):
    map_copy = map.copy()  # 创建地图副本
    if path:
        for point in path:
            map_copy[point[1], point[0]] = 3  # 将路径标记为3，与其他值不重叠

    plt.figure(figsize=(8, 8))
    plt.imshow(map_copy, cmap='binary', interpolation='nearest', vmin=0, vmax=3)  # 使用binary colormap
    # 标记起点和终点
    plt.scatter(start[0], start[1], color='blue', s=50, marker='v', label='Start')
    plt.scatter(end[0], end[1], color='purple', s=50, marker='x', label='End')

    if path:
        path_array = np.array(path)
        plt.plot(path_array[:, 0], path_array[:, 1], color='red', linewidth=3)  # 加粗路径线条，使用红色标记

    plt.legend()
    plt.title('Map with Path')
    plt.xticks([])
    plt.yticks([])
    plt.show()


# A*算法找路
def AStarSearch(map, source, dest):
    class SearchEntry():
        def __init__(self, x, y, g_cost, f_cost=0, pre_entry=None):
            self.x = x
            self.y = y
            self.g_cost = g_cost
            self.f_cost = f_cost
            self.pre_entry = pre_entry

        def getPos(self):
            return (self.x, self.y)

    def getNewPosition(map, location, offset):
        # 获取新位置的坐标
        # 通过offset进行上下左右移动或者斜线移动
        x, y = (location.x + offset[0], location.y + offset[1])
        # 边界以及障碍物判断
        if x < 0 or x >= map.width or y < 0 or y >= map.height or map.map[y][x] == 1:
            return None
        return (x, y)

    def getPositions(map, location):
        # 获取相邻位置坐标
        # 值考虑上下左右移动

        # offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        # 考虑使用斜线移动
        offsets = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
        # 用来存储可移动的位置坐标（可移动方向）
        feasibleDirection = []
        for offset in offsets:
            pos = getNewPosition(map, location, offset)
            if pos is not None:
                feasibleDirection.append(pos)
        return feasibleDirection

    # 用来计算当前位置到目标位置的距离
    def calHeuristic(pos, dest):
        return abs(dest.x - pos[0]) + abs(dest.y - pos[1])

    # 获取移动代价
    def getMoveCost(location, pos):
        if location.x != pos[0] and location.y != pos[1]:
            # 1:1:2^(1/2)
            return 1.4
        else:
            return 1

    # 检查传入的位置是否在列表里面，作用是什么？
    def isInList(list, pos):
        if pos in list:
            return list[pos]
        return None

    # 将相邻的可行边（可以斜线），添加到openlist（）存储了当前位置周围的可移动方向
    def addAdjacentPositions(map, location, dest, openlist, closedlist):
        poslist = getPositions(map, location)
        for pos in poslist:
            if isInList(closedlist, pos) is None:
                findEntry = isInList(openlist, pos)
                h_cost = calHeuristic(pos, dest)
                g_cost = location.g_cost + getMoveCost(location, pos)
                if findEntry is None:
                    # 如果位置没有在可行方向列表中，加入位置
                    openlist[pos] = SearchEntry(pos[0], pos[1], g_cost, g_cost + h_cost, location)
                elif findEntry.g_cost > g_cost:
                    # 如果位置的行进方向代价小于以前放入的代价，更新位置
                    findEntry.g_cost = g_cost
                    findEntry.f_cost = g_cost + h_cost
                    findEntry.pre_entry = location

    # 找到最小代价路径，如果为空，返回none
    def getFastPosition(openlist):
        fast = None
        for entry in openlist.values():
            if fast is None:
                fast = entry
            elif fast.f_cost > entry.f_cost:
                fast = entry
        return fast

    openlist = {}
    closedlist = {}
    location = SearchEntry(source[0], source[1], 0.0)
    dest = SearchEntry(dest[0], dest[1], 0.0)
    openlist[source] = location
    while True:
        location = getFastPosition(openlist)
        if location is None:
            # not found valid path
            print("can't find valid path")
            break
        if location.x == dest.x and location.y == dest.y:
            break
        closedlist[location.getPos()] = location
        openlist.pop(location.getPos())
        addAdjacentPositions(map, location, dest, openlist, closedlist)
    path = []
    # 在地图中标记逃生路线
    while location is not None:
        path.append(location.getPos())
        location = location.pre_entry
    return path


WIDTH = binary_matrix.shape[1]
HEIGHT = binary_matrix.shape[0]

map = Map(WIDTH, HEIGHT, binary_matrix)
count = 0

dest = (700, 220)

# 多个起始坐标
source_coordinates = [(400, 220)]  # 你可以根据需要添加更多起始坐标

# 存储所有路径的列表
all_paths = []

# 对每个起始坐标进行路径搜索
for source in source_coordinates:
    path = AStarSearch(map, source, dest)
    all_paths.append(path)

# 在同一张图上展示所有路径
map_data = map.getMap()
plt.figure(figsize=(8, 8))
plt.imshow(map_data, cmap='binary', interpolation='nearest', vmin=0, vmax=3)

# 标记终点
plt.scatter(dest[0], dest[1], color='purple', s=50, marker='x', label='End')

# 循环标记每个起点和对应的路径
for i, source in enumerate(source_coordinates):
    plt.scatter(source[0], source[1], color='blue', s=50, marker='o', label=f'Start {i + 1}')
    if all_paths[i]:
        path_array = np.array(all_paths[i])
        plt.plot(path_array[:, 0], path_array[:, 1], linewidth=3, label=f'Path {i + 1}')

plt.legend()
plt.title('Map with Paths')
plt.xticks([])
plt.yticks([])
plt.show()
