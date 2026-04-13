#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import time

def move_square():

    # Initialize node
    rospy.init_node('square_turtle_node', anonymous=True)

    # Publisher to control turtle
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # Wait a bit for connection
    time.sleep(2)

    msg = Twist()

    rospy.loginfo("Turtles are great at drawing squares!")

    for i in range(4):

        # MOVE FORWARD
        msg.linear.x = 2.0
        msg.angular.z = 0.0
        pub.publish(msg)
        time.sleep(2)

        # STOP
        msg.linear.x = 0.0
        pub.publish(msg)
        time.sleep(1)

        # TURN 90 DEGREE
        msg.angular.z = 1.57   # approx 90 degrees
        pub.publish(msg)
        time.sleep(1)

        # STOP AGAIN
        msg.angular.z = 0.0
        pub.publish(msg)
        time.sleep(1)

    rospy.loginfo("Finished drawing square!")

if __name__ == '__main__':
    try:
        move_square()
    except rospy.ROSInterruptException:
        pass