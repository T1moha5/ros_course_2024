#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


def callback(msg):
    rospy.loginfo("I heard %s", msg.data)

rospy.init_node('overflow_listener')
# Не требуется сохранять объект подписки, возврат функции игнорируется
rospy.Subscriber('overflow_topic', String, callback)
rospy.spin()
