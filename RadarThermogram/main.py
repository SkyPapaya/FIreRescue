import matplotlib.pyplot as plt
from random import randint


class SearchEntry():
    def __init__(self, x, y, g_cost, f_cost=0, pre_entry=None):
        self.x = x
        self.y = y
        # cost move form start entry to this entry
        self.g_cost = g_cost
        self.f_cost = f_cost
        self.pre_entry = pre_entry

    def getPos(self):
        return (self.x, self.y)


# 初始化map类，定义地图的长宽，并设置保存地图信息的二维数据map的值为0，0表示可以移动到这个点
class Map():
    # 初始化地图信息
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [[0 for x in range(self.width)] for y in range(self.height)]

    # 创建一个不可到达矩阵
    def createBlock(self, block_num):
        for i in range(block_num):
            x, y = (randint(0, self.width - 1), randint(0, self.height - 1))
            self.map[y][x] = 1

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
def showMapWithColors(map, start, end):
    plt.figure(figsize=(8, 8))
    plt.imshow(map, cmap='RdYlGn', interpolation='nearest')
    # 标记起点和终点
    plt.scatter(start[0], start[1], color='blue', s=100, marker='o', label='Start')
    plt.scatter(end[0], end[1], color='purple', s=100, marker='o', label='End')
    plt.legend()
    plt.title('Map with Path')
    plt.xticks([])
    plt.yticks([])
    plt.show()


# A*算法找路
def AStarSearch(map, source, dest):
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

        #offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        # 考虑使用斜线移动
        offsets = [(-1,0), (0, -1), (1, 0), (0, 1), (-1,-1), (1, -1), (-1, 1), (1, 1)]
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
            # if position is already in closedlist, do nothing
            if isInList(closedlist, pos) is None:
                findEntry = isInList(openlist, pos)
                h_cost = calHeuristic(pos, dest)
                g_cost = location.g_cost + getMoveCost(location, pos)
                if findEntry is None:
                    # if position is not in openlist, add it to openlist
                    openlist[pos] = SearchEntry(pos[0], pos[1], g_cost, g_cost + h_cost, location)
                elif findEntry.g_cost > g_cost:
                    # if position is in openlist and cost is larger than current one,
                    # then update cost and previous position
                    findEntry.g_cost = g_cost
                    findEntry.f_cost = g_cost + h_cost
                    findEntry.pre_entry = location

    # find the least cost position in openlist, return None if openlist is empty
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
            break;

        if location.x == dest.x and location.y == dest.y:
            break

        closedlist[location.getPos()] = location
        openlist.pop(location.getPos())
        addAdjacentPositions(map, location, dest, openlist, closedlist)

    # mark the found path at the map
    while location is not None:
        map.map[location.y][location.x] = 2
        location = location.pre_entry


WIDTH = 512
HEIGHT = 128
BLOCK_NUM = 2000
map = Map(WIDTH, HEIGHT)
map.createBlock(BLOCK_NUM)

source = map.generatePos((0, WIDTH // 3), (0, HEIGHT // 3))
dest = map.generatePos((WIDTH // 2, WIDTH - 1), (HEIGHT // 2, HEIGHT - 1))

AStarSearch(map, source, dest)

map_data = map.getMap()
showMapWithColors(map_data, source, dest)
