#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('sendstep', String, queue_size=10)
    rospy.init_node('robot', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        user_input = input("Enter a, b, or c: ")
        if user_input == 'a':
            msg = "1"
        elif user_input == 'b':
            msg = "2"
        elif user_input == 'c':
            msg = "3"
        else:
            rospy.logwarn("Invalid input. Please enter a, b, or c.")
            continue

        rospy.loginfo("Sending message: %s" % msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
