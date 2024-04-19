#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib import SimpleActionClient

# Define the coordinates to move to
goals = [
    (1.09, 0.19, 90.01),  # First goal: x, y, w
    (1.44, 1.57, 173.11),  # Second goal: x, y, w
    (0.33, 1.75, -94.31)   # Third goal: x, y, w
]

def move_to_goal(x, y, w):
    # Set up the move_base action client
    client = SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    # Set the goal position
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.w = w

    # Send the goal position
    rospy.loginfo(f"Sending goal to x={x}, y={y}, w={w}")
    client.send_goal(goal, done_cb=move_done)

def move_done(state, result):
    rospy.loginfo("Reached goal!")

def callback(data):
    choice = data.data
    if choice == 1:
        rospy.loginfo("First goal: x=1.09, y=0.19, w=90.01")
        goal_x, goal_y, goal_w = goals[choice - 1]
        move_to_goal(goal_x, goal_y, goal_w)
    elif choice == 2:
        rospy.loginfo("Second goal: x=1.44, y=1.57, w=173.11")
        goal_x, goal_y, goal_w = goals[choice - 1]
        move_to_goal(goal_x, goal_y, goal_w)
    elif choice == 3:
        rospy.loginfo("Third goal: x=0.33, y=1.75, w=-94.31")
        goal_x, goal_y, goal_w = goals[choice - 1]
        move_to_goal(goal_x, goal_y, goal_w)
    else:
        rospy.loginfo("Invalid choice! Please enter a number between 1 and 3.")

if __name__ == '__main__':
    rospy.init_node('slave_node', anonymous=True)
    rospy.Subscriber('/move_coordinates', Int32, callback)
    rospy.spin()