#!/usr/bin/env python
##she bang tells ros to use python

import rospy
from std_msgs.msg import String
def callback(msg):
	print msg.data
def subscriber():
	rospy.init_node('check')
	sub = rospy.Subscriber('s2', String, callback)
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

if __name__ == '__main__':
    subscriber()