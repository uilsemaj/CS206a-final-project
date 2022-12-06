#!/usr/bin/env python
"""
Pub/Sub node for state deciding purposes
"""

import rospy
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
import csv
import os

from moveit_msgs.msg import OrientationConstraint
from geometry_msgs.msg import PoseStamped, Pose, Quaternion, Point, PoseArray
from std_msgs.msg import Header



# Import the String message type from the /msg directory of the std_msgs package.
from std_msgs.msg import String

this_file = os.path.dirname(os.path.abspath(__file__))
CSV_DIR = "/home/cc/ee106a/fa22/class/ee106a-aeu/ros_workspaces/final_project/src/planning/img_processing/src"
print(CSV_DIR)

# Define the method which contains the node's main functionality
def talker():

    # Create an instance of the rospy.Publisher object which we can  use to
    # publish messages to a topic. This publisher publishes messages of type
    # geometry_msgs.Pose[] to topic /state_info
    pub = rospy.Publisher('state_info', PoseArray, queue_size=10)

    #need to confirm if this is an okay data type because waypoints is an array of poses


    # Create a timer object that will sleep long enough to result in a 1Hz
    # publishing rate
    r = rospy.Rate(1) # 1hz

    # Loop until the node is killed with Ctrl-C
    while not rospy.is_shutdown():
        # Construct a string that we want to publish (in Python, the "%"
        # operator functions similarly to sprintf in C or MATLAB)
        recieved_audio_message = "2/2"

        #can probably make this more efficien  t too

        #get all the required waypoints
        waypoints22 = wp22("22wp1_coords.csv")
        
        #save them in a dictionary
        Dict = {"2/2": waypoints22}

        #publish the appropriate waypoint set
        pub_message = Dict[recieved_audio_message]

        # Publish our waypoint set to the 'state_info' topic
        pub.publish(pub_message)
        # print(rospy.get_name() + ": I sent \"%s\"" % pub_message)

        # Use our rate object to sleep until it is time to publish again
        r.sleep()

def wp22(csv_name):  

#hard-coded right now, but this is where the calculated waypoints will go.
# need to find a convenient way to store them without having to recompute every time. 
#maybe some separate data type like csv that the function can draw from? so the waypoint calculator will
#output a csv and this one can extract from it.
    waypoints = PoseArray()
    wpose = Pose()
    wpose.orientation.x = -0.445
    wpose.orientation.y = 0.536
    wpose.orientation.z = -0.451
    wpose.orientation.w = 0.558
    wpose.position.x = 0.890 #setting this here for now, will convert to spherical coords later
    print(wpose.position.y)     #RH Added

    point_array = np.loadtxt(CSV_DIR + "/" + csv_name, delimiter=",")
    # point_array = np.transpose(point_array)
    print(point_array)
    
    for coords in point_array:
        (wpose.position.z, wpose.position.y) = coords
        waypoints.poses.append(copy.deepcopy(wpose))

    return waypoints

# This is Python's syntax for a main() method, which is run by default when
# exectued in the shell
if __name__ == '__main__':

    # Run this program as a new node in the ROS computation graph called /talker.
    rospy.init_node('talker', anonymous=True)

    # Check if the node has received a signal to shut down. If not, run the
    # talker method.
    try:
        talker()
    except rospy.ROSInterruptException: pass
