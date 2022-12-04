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
from geometry_msgs.msg import PoseStamped, Pose, Quaternion, Point
from std_msgs.msg import Header

from path_planner_cartesianv2 import PathPlanner

try:
    from controller import Controller
except ImportError:
    pass
    
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

        
    while not rospy.is_shutdown():
        try:
            # Might have to edit this . . .
            plan = planner.cartesian_plan_to_pose(waypoints, [orien_const])

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


if __name__ == '__main__':
    rospy.init_node('moveit_node')
    main()
