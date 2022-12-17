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
        
        while not rospy.is_shutdown():
            try:
                waypoints = []

                wpose = Pose()
                wpose.position.x = 0.886
                wpose.position.y = -0.108
                wpose.position.z = 0.835
                print(wpose.position.y)     #RH Added

                wpose.orientation.x = -0.445
                wpose.orientation.y = 0.536
                wpose.orientation.z = -0.451
                wpose.orientation.w = 0.558
                print(wpose.position.y)     #RH Added

                waypoints.append(copy.deepcopy(wpose))

                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.107  ,   0.890   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.112  ,   0.792   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.115  ,   0.765   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.120  ,   0.722   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.123  ,   0.678   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.126  ,   0.643   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.128  ,   0.622   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.131  ,   0.592   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.134  ,   0.549   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.138  ,   0.508   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.145  ,   0.468   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.149  ,   0.441   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.155  ,   0.411   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.163  ,   0.381   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.168  ,   0.365   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.181  ,   0.349   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.187  ,   0.373   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.191  ,   0.403   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.194  ,   0.419   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.196  ,   0.441   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.199  ,   0.468   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.200  ,   0.500   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.202  ,   0.530   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.203  ,   0.557   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.206  ,   0.500   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                # (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.206  ,   0.468   )
                # waypoints.append(copy.deepcopy(wpose))
                #print(wpose.position.y)     #RH Added
                # (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.206  ,   0.438   )
                # waypoints.append(copy.deepcopy(wpose))
                #print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.206  ,   0.411   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                # (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.206  ,   0.386   )
                # waypoints.append(copy.deepcopy(wpose))
                #print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.206  ,   0.365   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                # (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.206  ,   0.343   )
                # waypoints.append(copy.deepcopy(wpose))
                # (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.206  ,   0.330   )
                # waypoints.append(copy.deepcopy(wpose))
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.199  ,   0.346   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.194  ,   0.362   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.187  ,   0.384   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.180  ,   0.408   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.172  ,   0.443   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.163  ,   0.478   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                # (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.157  ,   0.522   )
                # waypoints.append(copy.deepcopy(wpose))
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.149  ,   0.568   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.143  ,   0.624   )
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.y)     #RH Added
                # (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.137  ,   0.659   )
                # waypoints.append(copy.deepcopy(wpose))
                # (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.129  ,   0.711   )
                # waypoints.append(copy.deepcopy(wpose))
                #print(wpose.position.y)     #RH Added
                # (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.121  ,   0.759   )
                # waypoints.append(copy.deepcopy(wpose))
                # print(wpose.position.y)     #RH Added
                # (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.113  ,   0.814   )
                # waypoints.append(copy.deepcopy(wpose))
                # (wpose.position.x, wpose.position.y, wpose.position.z) =    (   0.890   ,   -0.107  ,   0.890   )
                # waypoints.append(copy.deepcopy(wpose))

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
