#!/usr/bin/env python
##she bang tells ros to use python

import rospy
from std_msgs.msg import String
def callback(msg):
	print msg.data
def subscriber():
	rospy.init_node('sub_new')
	sub = rospy.Subscriber('new', String, callback)
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

if __name__ == '__main__':
    subscriber()
    