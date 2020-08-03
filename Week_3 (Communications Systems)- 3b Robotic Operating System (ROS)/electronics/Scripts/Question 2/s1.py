#THE PROGRAM WILL PUBLSIH ON THE TOPIC AS SAID IN THE QUESTION
#!/usr/bin/env python
import rospy
from std_msgs.msg import String

if __name__ ==  '__main__':
	rospy.init_node('s1', anonymous=True)
	pub = rospy.Publisher('s1', String, queue_size=10)#PUBLISH ON \s1
	rate = rospy.Rate(1) # 1hz
	count = 1 
	while not rospy.is_shutdown():
		if count<=10:
			signal_str = "green"
		else:
			signal_str = "red"
		pub.publish(signal_str)
		count +=1
		if count == 20:
			count = 1
		rate.sleep()