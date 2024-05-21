import matplotlib.pyplot as plt
import cv2
import numpy as np
from numpy.random import randint
import seaborn as sns
import SafetyFactor as sf
import PersonPosition as pp


# 转换图像为二值矩阵
def convert_to_binary(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary_img = cv2.threshold(gray_img, 230, 255, cv2.THRESH_BINARY)
    inverted_binary_img = cv2.bitwise_not(binary_img)
    binary_matrix = (inverted_binary_img / 255).astype(np.uint8)
    return binary_matrix


# 读取图像
image_path = './img/map_new.png'
image = cv2.imread(image_path)
binary_matrix = convert_to_binary(image)


# 初始化map类
class Map():
    def __init__(self, width, height, binary_matrix):
        self.width = width
        self.height = height
        self.map = binary_matrix

    def generatePos(self, rangeX, rangeY):
        x, y = (randint(rangeX[0], rangeX[1]), randint(rangeY[0], rangeY[1]))
        while self.map[y][x] == 1:
            x, y = (randint(rangeX[0], rangeX[1]), randint(rangeY[0], rangeY[1]))
        return (x, y)

    def getMap(self):
        return self.map


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
        x, y = (location.x + offset[0], location.y + offset[1])
        if x < 0 or x >= map.width or y < 0 or y >= map.height or map.map[y][x] == 1:
            return None
        return (x, y)

    def getPositions(map, location):
        offsets = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
        feasibleDirection = []
        for offset in offsets:
            pos = getNewPosition(map, location, offset)
            if pos is not None:
                feasibleDirection.append(pos)
        return feasibleDirection

    def calHeuristic(pos, dest):
        return abs(dest.x - pos[0]) + abs(dest.y - pos[1])

    def getMoveCost(location, pos):
        if location.x != pos[0] and location.y != pos[1]:
            return 1.4
        else:
            return 1

    def isInList(list, pos):
        if pos in list:
            return list[pos]
        return None

    def addAdjacentPositions(map, location, dest, openlist, closedlist):
        poslist = getPositions(map, location)
        for pos in poslist:
            if isInList(closedlist, pos) is None:
                findEntry = isInList(openlist, pos)
                h_cost = calHeuristic(pos, dest)
                g_cost = location.g_cost + getMoveCost(location, pos)
                if findEntry is None:
                    openlist[pos] = SearchEntry(pos[0], pos[1], g_cost, g_cost + h_cost, location)
                elif findEntry.g_cost > g_cost:
                    findEntry.g_cost = g_cost
                    findEntry.f_cost = g_cost + h_cost
                    findEntry.pre_entry = location

    def getFastPosition(openlist):
        fast = None
        for entry in openlist.values():
            if fast is None:
                fast = entry
            elif fast.f_cost > entry.f_cost:
                fast = entry
        return fast

    # def get_final_map():
    openlist = {}
    closedlist = {}
    location = SearchEntry(source[0], source[1], 0.0)
    dest = SearchEntry(dest[0], dest[1], 0.0)
    openlist[source] = location
    while True:
        location = getFastPosition(openlist)
        if location is None:
            print("can't find valid path")
            break
        if location.x == dest.x and location.y == dest.y:
            break
        closedlist[location.getPos()] = location
        openlist.pop(location.getPos())
        addAdjacentPositions(map, location, dest, openlist, closedlist)
    path = []
    while location is not None:
        path.append(location.getPos())
        location = location.pre_entry
    return path


def get_final_map():
    WIDTH = binary_matrix.shape[1]
    HEIGHT = binary_matrix.shape[0]

    map = Map(WIDTH, HEIGHT, binary_matrix)
    dest = pp.get_human_pos()
    source_coordinates = [(400, 220)]

    all_paths = []

    for source in source_coordinates:
        path = AStarSearch(map, source, dest)
        all_paths.append(path)

    # 获取地图和安全系数数据
    map_data = map.getMap()
    safety_data = sf.get_data_frame()

    # 设置图表
    plt.figure(figsize=(8, 8))

    # 绘制热力图
    cmap = "RdYlGn_r"
    sns.heatmap(safety_data, cmap=cmap, square=True, cbar=True, xticklabels=False, yticklabels=False)

    # 标记终点
    plt.scatter(dest[0], dest[1], color='purple', s=50, marker='x', label='End')

    # 循环标记每个起点和对应的路径
    for i, source in enumerate(source_coordinates):
        plt.scatter(source[0], source[1], color='blue', s=50, marker='o', label=f'Start {i + 1}')
        if all_paths[i]:
            path_array = np.array(all_paths[i])
            plt.plot(path_array[:, 0], path_array[:, 1], linewidth=3, label=f'Path {i + 1}')

    plt.gca().invert_yaxis()
    plt.legend()
    plt.title('Map with Paths on Safety Heatmap')
    plt.show()
