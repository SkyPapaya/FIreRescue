from PIL import Image

# 打开图片
image_path = './img/red_position.png'  # 替换为你的图片路径
image = Image.open(image_path)

# 获取图片的大小
width, height = image.size

# 将图片转换为RGB模式（如果不是的话）
image = image.convert('RGB')

# 将图片转换为像素点数据
pixels = image.load()

# 存储红色像素点的坐标
red_pixel_coordinates = []

# 搜索红色像素点
for x in range(width):
    for y in range(height):
        if pixels[x, y] == (255, 0, 0):  # 红色像素点的RGB值为(255, 0, 0)
            red_pixel_coordinates.append((x, y))

# 输出红色像素点的坐标
if red_pixel_coordinates:
    print("红色像素点的坐标：")
    for coord in red_pixel_coordinates:
        print(coord)
else:
    print("图片中不存在红色像素点。")
