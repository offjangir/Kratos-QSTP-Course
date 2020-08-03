#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
def callback(msg):
	print msg.data
rospy.init_node('ClockPrint')
sub = rospy.Subscriber('clock1', String, callback)
rospy.spin()
