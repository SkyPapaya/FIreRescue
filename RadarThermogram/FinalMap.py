import GetPosition as gp
import SearchRoute as sr

if __name__ == '__main__':
    # 无人机最后的位置
    initial_position = gp.get_initial_position()

    # 根据无人机位置修正后的路径信息
    path = sr.get_changed_path()
    print(path)

    # 将路径保存到txt文件
    with open('./path.txt', 'w') as file:
        for pos in path:
            file.write(f"{pos}\n")
    print("路径保存成功！")
