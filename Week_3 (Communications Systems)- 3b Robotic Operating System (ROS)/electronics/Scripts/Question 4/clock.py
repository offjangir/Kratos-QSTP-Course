#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
seconds = 0
minutes = 0
hours = 0
def callback1(msg):
	global seconds
	seconds = msg.data
def callback2(msg):
	global minutes
	minutes = msg.data
def callback3(msg):
	global hours
	hours = msg.data
if __name__ ==  '__main__':
	rospy.init_node('clock1')
	rate = rospy.Rate(1) # 1hz
	while not rospy.is_shutdown():
		rospy.Subscriber('seconds', Int32, callback1)
		rospy.Subscriber('minutes', Int32, callback2)
		rospy.Subscriber('hours', Int32, callback3)
		pub = rospy.Publisher('clock1', String,queue_size=10)
		clockd = "{}:{}:{}".format(hours,minutes,seconds)
		pub.publish(clockd)
		rate.sleep()

