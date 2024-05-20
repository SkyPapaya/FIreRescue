from PIL import Image
import numpy as np

# 打开图片
image_path = "./img/test_map_1.png"
img = Image.open(image_path)
img_rgb = img.convert("RGB")
img_array = np.array(img_rgb)

# 获取图片的大小
h, w, _ = img_array.shape
print(f"Image dimensions: {h} x {w}")

# 指定修改像素点的位置
pos = [(1000, 779), (1000, 784), (1000, 780), (1000, 781)]

# 修改指定位置的像素点为红色
for y, x in pos:
    if 0 <= y < h and 0 <= x < w:  # 确保坐标在图片范围内
        img_array[y, x] = [255, 0, 0]

# 将修改后的数组转换回图像
img_modified = Image.fromarray(img_array)

# 显示并保存修改后的图像
# img_modified.show()
img_modified.save("./img/red_position.png")

from PIL import ImageGrab

import pyautogui

# 定义截图区域 (left, top, width, height)
region = (0, 100, 300, 300)

# 获取特定区域的屏幕截图
screenshot = pyautogui.screenshot(region=region)

# 保存截图
screenshot.save("screenshot_region.png")
