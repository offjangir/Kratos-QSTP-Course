#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
m_count = 0
def callback(msg):
	global m_count
	if msg.data == 60:
		m_count+=1
	pub.publish(m_count)
	if m_count == 60:
		m_count = 0
if __name__ ==  '__main__':
	rospy.init_node('minutes')
	pub = rospy.Publisher('minutes', Int32, queue_size=10)
	sub = rospy.Subscriber('seconds', Int32, callback)
	rospy.spin()