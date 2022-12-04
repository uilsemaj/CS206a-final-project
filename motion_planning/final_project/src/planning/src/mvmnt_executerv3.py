#!/usr/bin/env python
"""
Path Planning Script for Lab 7
Author: Valmik Prabhu
"""
import sys
from intera_interface import Limb
import rospy
import numpy as np
import traceback
import copy
import moveit_commander
import moveit_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

from moveit_msgs.msg import OrientationConstraint
from geometry_msgs.msg import PoseStamped, Pose, Quaternion, Point, PoseArray
from std_msgs.msg import Header

from path_planner_cartesianv3 import PathPlanner

try:
    from controller import Controller
except ImportError:
    pass

def execute_motion(planner, waypoints, orien_const):

    while not rospy.is_shutdown():
        try:
            # Might have to edit this . . .
            plan = planner.cartesian_plan_to_pose(waypoints.poses, [orien_const])
            # print(rostype.plan)

            # user_input = input("Press y to move the right arm to goal poses: ")
            user_input = 'y'

            if user_input == 'y':
                if not planner._group.execute(plan, wait=True):#planner.execute_plan(plan[1]):
                    raise Exception("Execution failed")
        except Exception as e:
            print(e)
            traceback.print_exc()
        else:
            break

def callback(data):
    old_waypoints = PoseArray()
    # waypoints = rospy.wait_for_message('state_info', PoseArray, timeout = 100000)

    # if data != old_waypoints:
    execute_motion(planner, data, orien_const)
    rospy.sleep(1)



def listener(planner, orien_const):

    # Create a new instance of the rospy.Subscriber object which we can use to
    # receive messages of type std_msgs/String from the topic /chatter_talk.
    # Whenever a new message is received, the method main() will be called
    # with the received message as its first argument.
    rospy.Subscriber('state_info', PoseArray, callback)
    # Wait for messages to arrive on the subscribed topics, and exit the node
    # when it is killed with Ctrl+C

    rospy.spin()

    

def main():
    """
    Main Script
    """

    # Make sure that you've looked at and understand path_planner.py before starting

    planner = PathPlanner("right_arm")


    #
    # Add the obstacle to the planning scene here
    #adding table
    #
    posestamped = PoseStamped()
    pose = Pose()
    posestamped.pose = pose

    quaternion = Quaternion()
    quaternion.x = 0.0
    quaternion.y = 0.0
    quaternion.z = 0.0
    quaternion.w = 1.0
    pose.orientation = quaternion

    position = Point()
    pose.position = position
    position.x = 0.5
    position.y = 0.0
    position.z = 0.0

    header = Header()
    header.frame_id = "base";
    posestamped.header = header

    size = np.array([0.4, 1.2, 0.1])

    obstacle_name = "table"

    planner.add_box_obstacle(size, obstacle_name, posestamped)
    #Create a path constraint for the arm
    #UNCOMMENT FOR THE ORIENTATION CONSTRAINTS PART
    orien_const = OrientationConstraint()
    orien_const.link_name = "right_gripper";
    orien_const.header.frame_id = "base";
    #orien_const.orientation.y = -1.0;

    orien_const.absolute_x_axis_tolerance = 0.1;
    orien_const.absolute_y_axis_tolerance = 0.1;
    orien_const.absolute_z_axis_tolerance = 0.1;
    orien_const.weight = 1.0;
    print(orien_const.orientation)

    return planner, orien_const
    


if __name__ == '__main__':

    # Run this program as a new node in the ROS computation graph called
    # /listener_<id>, where <id> is a randomly generated numeric string. This
    # randomly generated name means we can start multiple copies of this node
    # without having multiple nodes with the same name, which ROS doesn't allow.

    rospy.init_node('moveit_node')
    (planner, orien_const) = main()
    listener(planner, orien_const)



