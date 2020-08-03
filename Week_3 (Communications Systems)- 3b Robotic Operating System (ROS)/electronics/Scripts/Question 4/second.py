#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String
rospy.init_node('seconds')
pub = rospy.Publisher('seconds', Int32, queue_size=10)
rate = rospy.Rate(1) # 1hz
s_count =0
while not rospy.is_shutdown():
	s_count += 1
	pub.publish(s_count)
	if s_count == 60:
		s_count =0
	rate.sleep() 
