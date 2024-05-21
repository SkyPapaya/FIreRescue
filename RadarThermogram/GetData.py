import rospy
from std_msgs.msg import String

# 定义全局变量
smoke = 0.0
co = 0.0
fire = 0.0
temperature = 0.0
humidity = 0.0
x1y1 = ''
x2y2 = ''
x3y3 = ''
x4y4 = ''
x5y5 = ''

def get_sensor_info(msg):
    global smoke, co, fire, temperature, humidity
    data = msg.data.split(';')
    smoke = float(data[0])
    co = float(data[1])
    fire = float(data[2])
    temperature = float(data[3])
    humidity = float(data[4])

def get_person_pos(msg):
    global x1y1, x2y2, x3y3, x4y4, x5y5
    data = msg.data.split(';')
    x1y1 = data[5]
    x2y2 = data[6]
    x3y3 = data[7]
    x4y4 = data[8]
    x5y5 = data[9]


def get_sensor_values():
    global smoke, co, fire, temperature, humidity
    return smoke, co, fire, temperature, humidity

def get_person_pos_values():
    global x1y1, x2y2, x3y3, x4y4, x5y5
    return x1y1, x2y2, x3y3, x4y4, x5y5

def chatter_subscriber():
    rospy.init_node('chatter_subscriber', anonymous=True)
    rospy.Subscriber("chatter", String, get_sensor_info())
    rospy.Subscriber("chatter", String, get_person_pos)
    rospy.spin()


if __name__ == '__main__':
    chatter_subscriber()
