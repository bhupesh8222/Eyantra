#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


def main():
    
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    
    rospy.init_node('turtle_revolve', anonymous=True)
    
    var_loop_rate = rospy.Rate(1)

    condition = True
        
    while not rospy.is_shutdown() and condition:
        
        vel_msg = Twist()
        vel_msg.linear.x = 1
        vel_msg.linear.y = 0
        vel_msg.angular.z = 0.5
    
        rospy.loginfo("Publishing: ")
    
        velocity_publisher.publish(vel_msg)
        
        
        def pose_callback(msg):
            rospy.loginfo(msg.theta)
            if msg.theta==float(0):
                global condition 
                rospy.loginfo("MSG.THETA IS ZERO")
                condition= False               
            
               
        rospy.Subscriber("/turtle1/pose", Pose, pose_callback)

        var_loop_rate.sleep()
        

        rospy.loginfo(condition)

       
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
