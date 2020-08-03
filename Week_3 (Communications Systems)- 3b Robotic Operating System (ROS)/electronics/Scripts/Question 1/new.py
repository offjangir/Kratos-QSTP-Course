#!/usr/bin/env python

import rospy
from std_msgs.msg import String

pub = rospy.Publisher('new', String, queue_size=10)
rospy.init_node('new', anonymous=True)
rate = rospy.Rate(15) # 15hz
hello_str = "Hello World!"
while not rospy.is_shutdown():
    pub.publish(hello_str)
    rate.sleep()