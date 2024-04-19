#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def talker():
    pub = rospy.Publisher('/move_coordinates', Int32, queue_size=10)
    rospy.init_node('master_node', anonymous=True)
    
    while not rospy.is_shutdown():
        user_input = input("Enter A, B, or C to send coordinates, or 'q' to quit: ")
        if user_input.lower() == 'q':
            break
        elif user_input.upper() in ['A', 'B', 'C']:
            choice = ord(user_input.upper()) - ord('A') + 1
            rospy.loginfo(f"Sending choice: {choice}")
            pub.publish(choice)
        else:
            rospy.loginfo("Invalid input, please enter A, B, or C.")

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass