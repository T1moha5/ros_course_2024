#!/usr/bin/env python
import rospy
import tf
from turtlesim.msg import Pose

def handle_turtle_pose(msg, turtlename):
    br = tf.TransformBroadcaster()
    current_time = rospy.Time.now()

    # Публикация трансформации черепахи
    br.sendTransform(
    (msg.x, msg.y, 0),
    tf.transformations.quaternion_from_euler(0, 0, msg.theta),
    current_time,
    turtlename,
    "world"
    )

if __name__ == '__main__':
    rospy.init_node('turtle_tf_broadcaster')
turtle_name = rospy.get_param('~turtle_tf_name', 'turtle1')
rospy.Subscriber(f'/{turtle_name}/pose', Pose, handle_turtle_pose, turtle_name)
rospy.spin()