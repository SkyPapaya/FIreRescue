from PIL import Image


# 定义一个函数，判断一个像素点是否是蓝色的
def is_blue(pixel, tolerance=80):
    blue_rgb = (0, 0, 255)
    return all(abs(component - blue_rgb[i]) <= tolerance for i, component in enumerate(pixel))


# 定义一个函数，获取图片中所有蓝色像素点的坐标
def get_blue_pixel_coordinates(image):
    blue_pixel_coordinates = []

    # 获取图片的大小
    width, height = image.size

    # 将图片转换为RGB模式（如果不是的话）
    image = image.convert('RGB')

    # 将图片转换为像素点数据
    pixels = image.load()

    # 搜索蓝色像素点，接受一定的误差
    for x in range(width):
        for y in range(height):
            if is_blue(pixels[x, y]):
                blue_pixel_coordinates.append((x, y))

    # print("coordinates before:{%s}" % len(blue_pixel_coordinates))

    return blue_pixel_coordinates


# 定义一个函数，检测blue_pixel_coordinates中点之间的距离是否小于某个阈值，如果是则合并
def merge_close_points(coordinates, threshold=10):
    merged_coordinates = []
    for coord in coordinates:
        x, y = coord
        merged = False
        for merged_coord in merged_coordinates:
            merged_x, merged_y = merged_coord
            if abs(x - merged_x) <= threshold and abs(y - merged_y) <= threshold:
                merged = True
                break
        if not merged:
            merged_coordinates.append(coord)
    # print("coordinates after:{%s}" % len(blue_pixel_coordinates))
    return merged_coordinates


# 定义一个函数，接收一个栈和一个坐标列表，将新出现的坐标点压入栈中，并且如果栈内所有坐标点中有与新坐标点距离较近则视为同一坐标点
def push_coordinates(stack, coordinates):
    original_len = len(stack)
    tolerance = 10
    for coord in coordinates:
        x, y = coord
        merged = False
        for i, stack_coord in enumerate(stack):
            stack_x, stack_y = stack_coord
            if abs(x - stack_x) <= tolerance and abs(y - stack_y) <= tolerance:
                stack[i] = coord
                merged = True
                break
        if not merged:
            stack.append(coord)
    return stack


def get_initial_position():
    # 新建一个栈用于存放所有出现过的坐标点，且栈顶元素为最新的坐标点
    stack = []
    time_interval = 3
    # 打开图片
    image_path = f'./img/test_map_1.png'
    image = Image.open(image_path)
    # 获取所有蓝色像素点的坐标
    blue_pixel_coordinates = get_blue_pixel_coordinates(image)
    # 合并距离较近的点
    blue_pixel_coordinates = merge_close_points(blue_pixel_coordinates)
    # 将新出现的坐标点压入栈中
    stack = push_coordinates(stack, blue_pixel_coordinates)
    # 获取栈顶元素
    top_element = stack[-1]
    return top_element
