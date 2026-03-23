#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def draw_square():
    rospy.init_node('square_turtle')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        # move forward
        move = Twist()
        move.linear.x = 2.0
        move.angular.z = 0.0
        pub.publish(move)
        rospy.sleep(2)

        # stop
        pub.publish(Twist())
        rospy.sleep(0.5)

        # turn 90 deg
        turn = Twist()
        turn.angular.z = 1.57
        pub.publish(turn)
        rospy.sleep(1)

        pub.publish(Twist())
        rospy.sleep(0.5)

if __name__ == '__main__':
    try:
        draw_square()
    except rospy.ROSInterruptException:
        pass
