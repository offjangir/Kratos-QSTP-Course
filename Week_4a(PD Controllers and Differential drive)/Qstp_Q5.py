#!/usr/bin/env python

import rospy
import math
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point
from geometry_msgs.msg import Twist

def callback(msg):
    x_cor = msg.pose.pose.position.x
    y_cor = msg.pose.pose.position.y
    if x_cor>= 5:
        vel.linear.x = 0
        pub.publish(vel)
    else:
        vel.linear.x = .1
        pub.publish(vel)
    
if __name__ == '__main__':
    rospy.init_node('odom_move', anonymous=True)
    pub = rospy.Publisher('cmd_vel',Twist,queue_size="1")
    rate = rospy.Rate(2)
    while not rospy.is_shutdown():
        vel = Twist()


        sub = rospy.Subscriber('odom', Odometry, callback)

        rate.sleep()
