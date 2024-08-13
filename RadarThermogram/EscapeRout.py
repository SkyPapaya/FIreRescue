import matplotlib.pyplot as plt
import cv2
import numpy as np
import pandas as pd
import seaborn as sns
from numpy.random import randint

# Convert image to binary matrix
def convert_to_binary(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary_img = cv2.threshold(gray_img, 230, 255, cv2.THRESH_BINARY)
    inverted_binary_img = cv2.bitwise_not(binary_img)
    binary_matrix = (inverted_binary_img / 255).astype(np.uint8)
    return binary_matrix

# Read the image
image_path = 'image/source/nju_map.png'
image = cv2.imread(image_path)
binary_matrix = convert_to_binary(image)

# Initialize Map class
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

# A* algorithm for pathfinding
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
    return path[::-1]  # Reverse the path to go from source to dest

WIDTH = binary_matrix.shape[1]
HEIGHT = binary_matrix.shape[0]

map = Map(WIDTH, HEIGHT, binary_matrix)

# Generate the escape routes and move the start points along the paths
def get_escape_route(dest, source_coordinates, save_path=None):
    all_paths = []
    # Generate escape routes only once
    for source in source_coordinates:
        path = AStarSearch(map, source, dest)
        all_paths.append(path)

    def safety_factor(smoke, temperature, humidity):
        return temperature * 0.1 + humidity * 0.1 + smoke * 0.8

    def renew_safety_factor(temperature, humidity, smoke):
        return safety_factor(temperature, humidity, smoke)

    for path in all_paths:
        for pos in path:
            smoke = np.random.randint(1, 4)
            humidity = np.random.randint(1, 3)
            temperature = np.random.randint(1, 3)
            safety_factor_data = renew_safety_factor(temperature, humidity, smoke)
            binary_matrix[pos[1], pos[0]] = safety_factor_data

    df = pd.DataFrame(binary_matrix)
    cmap = "RdYlGn_r"

    # Move start points along the paths
    while any(tuple(pos) != dest for pos in source_coordinates):
        for i, path in enumerate(all_paths):
            if len(path) > 0:
                step = min(20, len(path))
                source_coordinates[i] = path[step - 1]
                all_paths[i] = path[step:]

        # Plot the map with paths and safety factor heatmap
        plt.figure(figsize=(12, 12))
        sns.heatmap(df, cmap=cmap, square=True, cbar=True, alpha=0.6)
        plt.gca().invert_yaxis()
        plt.imshow(map.getMap(), cmap='binary', interpolation='nearest', vmin=0, vmax=3, alpha=0.4)
        plt.scatter(dest[0], dest[1], color='purple', s=280, marker='x', label='End')
        for i, source in enumerate(source_coordinates):
            plt.scatter(source[0], source[1], color='blue', s=90, marker='o', label=f'Start {i + 1}')
            if len(all_paths[i]) > 0:
                path_array = np.array(all_paths[i])
                plt.plot(path_array[:, 0], path_array[:, 1], linewidth=4, label=f'Path {i + 1}')

        plt.legend()
        plt.title('Map with Paths and Safety Factor Heatmap')
        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')

        if save_path:
            plt.savefig(save_path)
        plt.show()
        plt.pause(0.01)

# Example usage
dest = (736, 400)
source_coordinates = [(256, 140), (270, 145), (275, 148), (279, 152)]
save_path = '../ManageSystemVue/vue-manage-system/src/img/map.png'
get_escape_route(dest, source_coordinates, save_path)
