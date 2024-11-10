#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

rospy.init_node('talker2')
pub = rospy.Publisher('my_chat_topic', String, queue_size=10)
overflow_pub = rospy.Publisher('overflow_topic', String, queue_size=10)



def start_talker():
    msg = String()
    num = 0
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        num += 2 % rospy.get_time()
        rospy.loginfo(num)

        msg.data = str(num)
        pub.publish(msg)

        if num >= 100:
            overflow_msg = String()
            overflow_msg.data = "Счетчик достиг 100! Сброс."
            overflow_pub.publish(overflow_msg)
            num = 0 # Сброс счетчика

        rate = rospy.Rate(10)

try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Обнаружено исключение')
