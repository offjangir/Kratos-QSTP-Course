#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
h_count = 0
def callback(msg):
	global h_count
	pub.publish(h_count)
	if msg.data == 60:
		h_count+=1
if __name__ ==  '__main__':
	rospy.init_node('hours')
	pub = rospy.Publisher('hours', Int32, queue_size=10)
	sub = rospy.Subscriber('minutes', Int32, callback)
	rospy.spin()