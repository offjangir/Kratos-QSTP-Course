#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from geometry_msgs.msg import Twist
import math
# FOR CHANGING THE QUTERNION TO THE ROLL PITCH YAW ANGLES I HAVE USED TF.TRANFORMATIONS 
def callback(msg):
    orientation_q = msg.pose.pose.orientation
    orientation = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = euler_from_quaternion (orientation) #TRANSFORMATION
    if yaw >= angle_radian:
        vel.angular.z = 0
        pub.publish(vel)
    else:
        vel.angular.z = .1
        pub.publish(vel)

if __name__ == '__main__':
    global angle_radian
    global roll, pitch, yaw
    roll = pitch = yaw = 0.0
    angle = float(input("Enter the angle to rotate from 0 to 180 : "))
    angle_radian = angle*math.pi/180 #CHANGING THE ANGLE DATA TO RADIANS
    pub = rospy.Publisher('cmd_vel',Twist,queue_size="1")
    rospy.init_node('odom_rotate', anonymous=True)
    rate = rospy.Rate(3)
    while not rospy.is_shutdown():
        vel = Twist()
        sub = rospy.Subscriber('odom', Odometry, callback)#SUBSCRBING TO THE ODOMETRY DATA 
        rate.sleep()