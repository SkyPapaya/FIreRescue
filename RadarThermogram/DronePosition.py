import rospy
from turtlesim.msg import Pose


class PoseSubscriber:
    def __init__(self):
        # 初始化变量来存储最新的xy坐标
        self.latest_x = 0.0
        self.latest_y = 0.0

        # ROS节点初始化
        rospy.init_node('pose_subscriber', anonymous=True)

        # 创建一个Subscriber，订阅名为/turtle1/pose的topic，注册回调函数poseCallback
        self.sub = rospy.Subscriber("/turtle1/pose", Pose, self.poseCallback)

    def poseCallback(self, msg):
        rospy.loginfo("Turtle pose: x:%0.6f, y:%0.6f", msg.x, msg.y)
        # 更新最新的xy坐标值
        self.latest_x = msg.x
        self.latest_y = msg.y

    def get_latest_xy(self):
        # 返回最新的xy坐标值
        return self.latest_x, self.latest_y

    def spin(self):
        # 循环等待回调函数
        rospy.spin()


if __name__ == '__main__':
    # 实例化PoseSubscriber类
    pose_sub = PoseSubscriber()

    # 调用spin方法开始订阅
    pose_sub.spin()

    # 获取最新的xy坐标值
    latest_x, latest_y = pose_sub.get_latest_xy()
    print("Latest x: ", latest_x)
    print("Latest y: ", latest_y)