#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

rospy.init_node('talker')
pub = rospy.Publisher('my_chat_topic', String, queue_size=10)
overflow_pub = rospy.Publisher('overflow_topic', String, queue_size=10)
rate = rospy.Rate(1)

def start_talker():
    msg = String()
    overflow_msg = String()
    while not rospy.is_shutdown():
        hello_str = "hi =) %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        msg.data = hello_str        
        overflow_msg.data = "ЗНАЧЕНИЕ"
        overflow_pub.publish(overflow_msg)
        pub.publish(msg)
        rate.sleep()

try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
