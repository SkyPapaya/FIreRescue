import rospy
from std_msgs.msg import String


def chatter_callback(msg):
    data = msg.data.split(';')
    voltage2 = float(data[0])
    voltage1 = float(data[1])
    voltage3 = float(data[2])
    temperature = float(data[3])
    humidity = float(data[4])
    x1y1 = data[5]
    x2y2 = data[6]
    x3y3 = data[7]
    x4y4 = data[8]
    x5y5 = data[9]

    #rospy.loginfo(
    #    "Received message - Voltage2: %s, Voltage1: %s, Voltage3: %s, Temperature: %s, Humidity: %s, X1Y1: %s, X2Y2: %s, X3Y3: %s, X4Y4: %s, X5Y5: %s",
    #    voltage2, voltage1, voltage3, temperature, humidity, x1y1, x2y2, x3y3, x4y4, x5y5)


def chatter_subscriber():
    rospy.init_node('chatter_subscriber', anonymous=True)
    rospy.Subscriber("chatter", String, chatter_callback)
    rospy.spin()


if __name__ == '__main__':
    chatter_subscriber()
