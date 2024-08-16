import matplotlib.pyplot as plt
import numpy as np
import mqtt

# 设置字体以支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定黑体  
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 输入字符串
position_str = mqtt.on_message()
print(position_str)

# 移除多余的空格并用分号分割字符串
parts = [part.strip() for part in position_str.split(';') if part.strip()]

# 初始化两个空数组
x = []
y = []

# 遍历分割后的每一部分，并按逗号分开
for part in parts:
    before, after = part.split(',')
    x.append(float(before))
    y.append(float(after))
# 手动输入坐标
num_points = 5  # 点的数量  
# x = np.array([-2.8, -6.5, 7.0, 5.5, 2.8])  # X坐标
# y = np.array([-0.8, 2.5, -6.2, 3.5, -6.5])  # Y坐标

# 创建图形  
plt.figure(figsize=(8, 6))

# 在原点处绘制小盒子 (矩形)  
box_size = 0.5  # 盒子的大小
rectangle = plt.Rectangle((-box_size / 2, -box_size / 2), box_size, box_size, color='green', alpha=0.5)
plt.gca().add_patch(rectangle)

# 绘制点  
plt.scatter(x, y, color='blue', marker='o')

# 设置图形标题和标签  
plt.title('人员实时相对位置')
plt.xlabel('X /m')
plt.ylabel('Y /m')

# 设置坐标轴范围  
plt.xlim(-8, 8)
plt.ylim(-8, 8)

# 绘制坐标轴经过原点  
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # y=0 轴  
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # x=0 轴  

# 显示网格  
plt.grid(True)

# 显示图形  
#plt.show()
