import numpy as np
import GetData as gd


def get_human_pos(angle, Xp_drone, Yp_drone):
    # 定义无人机的偏向角度
    angle = -angle

    # 创建旋转矩阵
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])

    # 定义人相对无人机的坐标向量
    relative_position = np.array([[Xp_drone], [Yp_drone]])

    # 将人相对无人机的坐标转换为世界坐标系下的坐标
    # 目前只实现单人路线规划
    person_relative_position = np.dot(rotation_matrix, relative_position)
    person_relative_position = tuple(person_relative_position.flatten())
    person_relative_position[0] += gd.get_person_pos_values[0][0]
    person_relative_position[1] += gd.get_person_pos_values[0][1]

    # 保留3位小数
    person_relative_position = tuple([round(i, 3) for i in person_relative_position])

    # 输出人位于世界坐标系的坐标
    return person_relative_position


world_position = get_human_pos(np.pi / 4, 0, 5)
print(f"人位于世界坐标系的坐标为:{world_position}")
