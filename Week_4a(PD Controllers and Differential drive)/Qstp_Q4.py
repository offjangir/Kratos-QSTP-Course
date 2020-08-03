#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
def circle(R):#THIS FUNCTION MOVES THE BOT IN THE DESIED CIRCLE
	rospy.init_node('CIRCLE', anonymous=True)
	pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
	rate = rospy.Rate(10)
	vel = Twist()
	v = 0.22  #LINEAR VELOCITY
	omega = v/R #ANGULAR VELOCITY
	vel.linear.x = v
	vel.angular.z = omega
	while not rospy.is_shutdown():
		pub.publish(vel)
    	rate.sleep()

if __name__ == '__main__':
	R = int(input("Enter Radius of circle : "))
	circle(R)