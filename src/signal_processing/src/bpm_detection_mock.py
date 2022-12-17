#!/usr/bin/env python
# Copyright 2012 Free Software Foundation, Inc.
#
# This file is part of The BPM Detector Python
#
# The BPM Detector Python is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# The BPM Detector Python is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with The BPM Detector Python; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

import argparse
import array
import math
import wave

import matplotlib.pyplot as plt
import numpy
import pywt
from scipy import signal
import time

# import pyaudio
import rospy
from signal_processing.msg import AudioInfo


if __name__ == "__main__":
    #test mode = true

    # Let's get the node "talker" started - can rename this if it conflicts
    # I just used example_pub.py code
    rospy.init_node('talker', anonymous=True)

    # I moved the below from talker(); hopefully it still works, but if it doesn't it might be 
    # worth uncommenting the old version in talker() and massing None as the first argument to talker()
    # the commit prior to this one should have the right version

    # Create an instance of the rospy.Publisher object which we can use to
    # publish messages to a topic. This publisher publishes messages of type
    # AudioInfo to the topic /audiosignal
    pub = rospy.Publisher('audiosignal', AudioInfo, queue_size=10)





    while True:
        time.sleep(4)
        pub.publish(40, 1, 2, 2)
        print("audiosignal published")


#NOTES: super interesting, it appears that if the BPM < 110, it doubles it, otherwise it's accurate. 