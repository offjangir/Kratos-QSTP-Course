#!/usr/bin/env python
#THE PROGRAM SUBSCRIBES TO GET THE END EFFECTOR OF ARM AND PUBLISHES THE ANGLES IN RADIANS 
#CALCULATIONS HAVE BEEN ATTACHED AS A PDF

import rospy
from geometry_msgs.msg import Point 
from numpy import *
import math

def callback(msg):
	P = Point() #P IS THE END EFFECTOR OF THE ARM
	P.x = msg.x
	P.y = msg.y # MSG DATA IS RECIEVED 
	theta = Point() #POINT REPRESENTATION FOR THE ANGLES
	theta.y = math.acos(( pow(P.x,2) + pow(P.y,2) - 2 )/2)
	theta.x = math.acos((P.x /2)/math.cos(theta.y / 2)) - theta.y /2
	pub.publish(theta) 
	
if __name__ ==  '__main__':
	rospy.init_node('inverse_theta')
	pub = rospy.Publisher('joint_angles', Point, queue_size=10)
	sub = rospy.Subscriber('end_effector_position', Point, callback)
	rospy.spin()