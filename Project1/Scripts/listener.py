#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib import SimpleActionClient

def send_goal(goal_index):
    # 설정할 좌표 값
    goals = [
        (0.29, 0.17, 75.11),   # x, y, w
        (0.67, 1.57, 176.91),  # x, y, w
        (-0.46, 1.72, -4.48)   # x, y, w
    ]

    # 선택된 인덱스에 해당하는 좌표 설정
    goal_x, goal_y, goal_w = goals[goal_index]

    # move_base 액션 클라이언트 설정
    client = SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    # 이동 목표 설정
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = goal_x
    goal.target_pose.pose.position.y = goal_y
    goal.target_pose.pose.orientation.w = goal_w

    # 목표 위치로 이동 요청
    rospy.loginfo("Sending goal to x=%f, y=%f, w=%f", goal_x, goal_y, goal_w)
    client.send_goal(goal)

    # 이동 완료까지 대기
    client.wait_for_result()
    rospy.loginfo("Reached goal!")

def callback(data):
    try:
        goal_index = int(data.data)
        if goal_index < 1 or goal_index > 3:
            rospy.logwarn("Invalid choice! Please enter a number between 0 and 2.")
            return
    except ValueError:
        rospy.logwarn("Invalid input! Please enter a number.")
        return

    send_goal((goal_index)-1)

def listener():
    # ROS 노드 초기화
    rospy.init_node('goal_listener', anonymous=True)
    rospy.Subscriber("sendstep", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
