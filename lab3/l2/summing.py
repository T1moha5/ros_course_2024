#!/usr/bin/env python3
import rospy
import time

time.sleep(5)
rospy.init_node('params_study')
try:
    param1 = rospy.get_param('/param1')
except:
    param1 = 0
try:
    param2 = rospy.get_param('/param2')
except:
    param2 = 0
try:
    param3 = rospy.get_param('/param3')
except:
    param3 = 0
    
summ = param1 + param2 + param3

rospy.set_param('/summ', summ)
