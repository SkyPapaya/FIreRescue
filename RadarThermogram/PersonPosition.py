import numpy as np
import DronePosition as dp


def get_human_pos(angle, Xp_drone, Yp_drone):
    # 定义无人机的偏向角度
    angle = -angle

    # 创建旋转矩阵
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])

    # 定义人相对无人机的坐标向量
    relative_position = np.array([[Xp_drone], [Yp_drone]])

#允许传入多个人的坐标
    # 将人相对无人机的坐标转换为世界坐标系下的坐标
    person_position = np.dot(rotation_matrix, relative_position)
    person_position = tuple(person_position.flatten())

    # 保留3位小数
    person_position = tuple([round(i, 3) for i in person_position])

    # 输出人位于世界坐标系的坐标
    person_position[0] += dp.poseCallback[0]
    person_position[1] += dp.poseCallback[1]
    return person_position


world_position = get_human_pos(np.pi / 4, 0, 5)
print(f"人位于世界坐标系的坐标为:{world_position}")
