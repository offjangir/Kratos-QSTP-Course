#SUBSCRIBES TO THE TOPIC AND ALTENATE PUBLISHES ON THE OTHER TOPIC
#!/usr/bin/env python
import rospy
from std_msgs.msg import String
def callback(msg):
	signal = String()
	if msg.data == "green":
		signal = "red"
	else:
		signal = "green"
	pub.publish(signal)
if __name__ ==  '__main__':
	rospy.init_node('s2')
	sub = rospy.Subscriber('s1', String, callback) #SUBSCRIBE \s1 
	pub = rospy.Publisher('s2', String, queue_size=10) #PUBLISH ON \s2
	rospy.spin() 