#!/usr/bin/env python
#THIS NODE HAS BEEN CRETED TO TEST THE QUESTION 2
#A SAMPLE VALUE OF END EFFECTOR (0,2)
#IS PUBLISHED ON THE TOPIC TO CHECK IF THE CODE PUBLISHES RIGHT ANGLES
import rospy
from geometry_msgs.msg import Point

rospy.init_node('end_effector_position', anonymous=True)
pub = rospy.Publisher('end_effector_position', Point, queue_size=10)
rate = rospy.Rate(10)
vel = Point()
vel.x = 0
vel.y = 2
while not rospy.is_shutdown():
	pub.publish(vel)
   	rate.sleep()