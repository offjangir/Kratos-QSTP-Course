#!/usr/bin/env python
#THIS PROGRAM IS A TF BROADCASTER FOR THTE BASE TO OBJECT FRAME 
#CALCULATIONS HAVE BEEN DONE USING TF LIBRARY
#NUMPY IS USED TO MULTIPLY THE MATRICES
import rospy
import sys
import numpy as np

import tf
import tf2_ros
import geometry_msgs.msg

def message_from_transform(T):#THIS  FUNCTION CONVERTS THE TRANSFORM MATRIX IN THE MESSAGE FORM TO BROADCASTE
    t = geometry_msgs.msg.TransformStamped() #DECLARINT t AS A STAMPED TRANSFORM
    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "Base"
    t.child_frame_id = "Object"
    q = tf.transformations.quaternion_from_matrix(T)
    translation = tf.transformations.translation_from_matrix(T)
    #EXTRACTING  TRANSLATION AS POINTS AND ROTAIONS AS QUATERNION
    t.transform.translation.x = translation[0]
    t.transform.translation.y = translation[1]
    t.transform.translation.z = translation[2]
    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]
    return t

def calculate_publish_transforms():#THIS FUNCTIONS CALCULATES THE TRANSFORMS FOR ALL THE FRAMES AND BROADCASTS THE RESULTANT  TRANSFORM
    camera_tf = tf.transformations.concatenate_matrices(
                tf.transformations.quaternion_matrix(
                tf.transformations.quaternion_from_euler(0.79,0.0,0.79)),
                tf.transformations.translation_matrix((0.0,1.0,1.0))
    )
    object_tf = tf.transformations.concatenate_matrices(
                tf.transformations.quaternion_matrix(
                tf.transformations.quaternion_about_axis(1.5, (0,0,1)) ),
                tf.transformations.translation_matrix((0,1,0))
    )
    base_to_object_tf = np.dot(camera_tf,object_tf)
    t1 = message_from_transform(base_to_object_tf)
    br.sendTransform(t1) #SENDING FINAL TRANSFROM
    


if __name__ == '__main__':
    rospy.init_node('solution')

    br = tf2_ros.TransformBroadcaster()
    rospy.sleep(0.5)

    while not rospy.is_shutdown():
        calculate_publish_transforms()
        rospy.sleep(0.5)