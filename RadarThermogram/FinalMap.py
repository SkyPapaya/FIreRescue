import GetPosition as gp
import SearchRoute as sr
import  SafetyFactor as sf

if __name__ == '__main__':
    # 无人机最后的位置
    initial_position = gp.get_initial_position()
    #print(initial_position)
    # 根据无人机位置修正后的路径信息
    path = sr.get_changed_path()
    #print(path)

