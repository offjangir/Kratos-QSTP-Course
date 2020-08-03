#-------------------------------------------------------------------------------#

#THE CUSTON MESSAGE IS DEFINED AS FOLLOWS
#FOR DISTANCE
std_msgs/UInt64 distance_travelled 
#FOR STARTING TIME
std_msgs/Time t_start 
#FOR TIME TRAVELLED USE time.time()- t_start
std_msgs/Time t_travelled 
#FOR BATTERY LEVEL
std_msgs/UInt64 batterylvl
#FOR CORDINATES USE POSITION FROM POSE
geometry_msgs/Pose coordinates
#FOR VELOCITY USE LINEAR AND ANGULAR FROM TWIST
geometry_msgs/Twist velocity 


#--------------------------------------------------------------------------------#