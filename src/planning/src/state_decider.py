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
import rospy

from moveit_msgs.msg import OrientationConstraint
from geometry_msgs.msg import PoseStamped, Pose, Quaternion, Point, PoseArray
from std_msgs.msg import Header

from signal_processing.msg import AudioInfo



# Import the String message type from the /msg directory of the std_msgs package.
from std_msgs.msg import String

this_file = os.path.dirname(os.path.abspath(__file__))
# CSV_DIR = "/home/cc/ee106a/fa22/class/ee106a-aeu/ros_workspaces/final_project/src/img_processing/src"
CSV_DIR = "/home/cc/ee106a/fa22/class/ee106a-aeq/ros_workspaces/lab7/src/img_processing/src"
print(CSV_DIR)

Dict = {}
pub = rospy.Publisher('state_info', PoseArray, queue_size=10)  


# def test_mode():
#     for i in range(0,500):
#         pub.publish(Dict["HIGH"])
#         print("hi")
#         rospy.sleep(3)

def callback(message):
    # Loop until the node is killed with Ctrl-C

    if message.bpm >170:
        speed = "HIGH"
    else:
        speed = "LOW"

    #publish the appropriate waypoint set
    pub_message = Dict[speed]

    global pub
    # Publish our waypoint set to the 'state_info' topic
    pub.publish(pub_message)
    print(pub_message)
    # print(rospy.get_name() + ": I sent \"%s\"" % pub_message)

    # # Use our rate object to sleep until it is time to publish again
    # r.sleep()


def listener():
    # Create a new instance of the rospy.Subscriber object which we can use to
    # receive messages of type std_msgs/String from the topic /chatter_talk.
    # Whenever a new message is received, the method main() will be called
    # with the received message as its first argument.
    rospy.Subscriber('audiosignal', AudioInfo, callback)
    # Wait for messages to arrive on the subscribed topics, and exit the node
    # when it is killed with Ctrl+C

    rospy.spin()

# Define the method which contains the node's main functionality
def talker():

    # Create an instance of the rospy.Publisher object which we can  use to
    # publish messages to a topic. This publisher publishes messages of type
    # geometry_msgs.Pose[] to topic /state_info


    #need to confirm if this is an okay data type because waypoints is an array of poses


    # Create a timer object that will sleep long enough to result in a 1Hz
    # publishing rate
    r = rospy.Rate(1) # 1hz

    #get all the required waypoints
    waypoints22 = wp22("22wp1_coords.csv")
    waypoints44 = wp22("44wp1_coords.csv")

    global Dict
    
    #save them in a dictionary
    Dict.update({"HIGH": waypoints22})
    Dict.update({"LOW": waypoints44})

    # #publish the appropriate waypoint set
    # pub_message = Dict[recieved_audio_message]

    # # Publish our waypoint set to the 'state_info' topic
    # pub.publish(pub_message)
    # # print(rospy.get_name() + ": I sent \"%s\"" % pub_message)

    # # Use our rate object to sleep until it is time to publish again
    # r.sleep()
    # print(Dict)


    return Dict

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

    point_array = np.loadtxt(CSV_DIR + "/" + csv_name, delimiter=",")
    # point_array = np.transpose(point_array)
    # print(point_array)
    
    for coords in point_array:
        # (wpose.position.x, wpose.position.y, wpose.position.z) = coords
        (wpose.position.z, wpose.position.y) = coords

        waypoints.poses.append(copy.deepcopy(wpose))

    return waypoints

# This is Python's syntax for a main() method, which is run by default when
# exectued in the shell
if __name__ == '__main__':

    print("initiating node...")
    # Run this program as a new node in the ROS computation graph called /talker.
    rospy.init_node('state_decider', anonymous=True)
    print("initiated node...") 

    # Check if the node has received a signal to shut down. If not, run the
    # talker method.
    talker()
    print("listener starting")
    listener()
    # test_mode()

