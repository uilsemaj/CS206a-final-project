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

import pyaudio
import rospy
from signalprocessing.msg import AudioInfo

# These parameters all seem to work for the BPM detector
# RECORD_SECONDS is how long to sample audio from the 
# microphone before writing it and passing it to the detector. 
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 4

#can rename this if you want, I assume you don't already
# have a test.wav file
WAVE_OUTPUT_FILENAME = "test.wav"


# We'll use this function to publish AudioInfo messages
def talker(pub, beats, timestamp, top = 4, bottom = 4):


    # TODO: I'm not sure if you can move the below Publisher initialization into main
    # It seems like it's wasting overhead by initializing the object every time. 
    # It might be worth initializing pub in main and then passing it into this function
    # I'm also worried it might just create issues with the subscriber since the node needs to be
    # regenerated everytime

    # # Create an instance of the rospy.Publisher object which we can use to
    # # publish messages to a topic. This publisher publishes messages of type
    # # AudioInfo to the topic /audiosignal
    # pub = rospy.Publisher('audiosignal', AudioInfo, queue_size=10)
    
    # In lab we did a while loop around publish, but that doesn't seem to be relevant
    # here as we will publish when we receive a message, and won't when we don't 
    # have anything to send

    # Publish our string to the 'audiosignal' topic
    # pub.publish(beats, timestamp, top, bottom)


# this just records from your microphone
def record_voice():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("recording audio")
    frames = []
    # data_int = np.array(0)

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
        # print(data)
    #     test = np.array(struct.unpack(str(2*CHUNK)+'B',data), dtype='b')[::8]+ 128
    #     if np.size(data_int):
    #         data_int = test          #makes data integer values
    #     else:
    #         np.concatenate(data_int,test)
    # print(data_int)

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    # return b''.join(frames), RATE

    #return the time this finished recording
    return rospy.get_time()


def read_wav(filename):
    # open file, get metadata for audio
    try:
        wf = wave.open(WAVE_OUTPUT_FILENAME, "rb")
    except IOError as e:
        print(e)
        return

    # typ = choose_type( wf.getsampwidth() ) # TODO: implement choose_type
    nsamps = wf.getnframes()
    assert nsamps > 0

    fs = wf.getframerate()
    assert fs > 0

    # Read entire file and make into an array
    samps = list(array.array("i", wf.readframes(nsamps)))

    try:
        assert nsamps == len(samps)
    except AssertionError:
        print(nsamps, "not equal to", len(samps))

    return samps, fs


# print an error when no data can be found
def no_audio_data():
    print("No audio data for sample, skipping...")
    return None, None


# simple peak detection
def peak_detect(data):
    max_val = numpy.amax(abs(data))
    peak_ndx = numpy.where(data == max_val)
    if len(peak_ndx[0]) == 0:  # if nothing found then the max must be negative
        peak_ndx = numpy.where(data == -max_val)
    return peak_ndx


def bpm_detector(data, fs):

    cA = []
    cD = []
    correl = []
    cD_sum = []
    levels = 4
    max_decimation = 2 ** (levels - 1)
    min_ndx = math.floor(60.0 / 220 * (fs / max_decimation))
    max_ndx = math.floor(60.0 / 40 * (fs / max_decimation))

    for loop in range(0, levels):
        cD = []
        # 1) DWT
        if loop == 0:
            [cA, cD] = pywt.dwt(data, "db4")
            cD_minlen = len(cD) / max_decimation + 1
            cD_sum = numpy.zeros(math.floor(cD_minlen))
        else:
            [cA, cD] = pywt.dwt(cA, "db4")

        # 2) Filter
        cD = signal.lfilter([0.01], [1 - 0.99], cD)

        # 4) Subtract out the mean.

        # 5) Decimate for reconstruction later.
        cD = abs(cD[:: (2 ** (levels - loop - 1))])
        cD = cD - numpy.mean(cD)

        # 6) Recombine the signal before ACF
        #    Essentially, each level the detail coefs (i.e. the HPF values) are concatenated to the beginning of the array
        cD_sum = cD[0 : math.floor(cD_minlen)] + cD_sum

    if [b for b in cA if b != 0.0] == []:
        return no_audio_data()

    # Adding in the approximate data as well...
    cA = signal.lfilter([0.01], [1 - 0.99], cA)
    cA = abs(cA)
    cA = cA - numpy.mean(cA)
    cD_sum = cA[0 : math.floor(cD_minlen)] + cD_sum

    # ACF
    correl = numpy.correlate(cD_sum, cD_sum, "full")

    midpoint = math.floor(len(correl) / 2)
    correl_midpoint_tmp = correl[midpoint:]
    peak_ndx = peak_detect(correl_midpoint_tmp[min_ndx:max_ndx])
    if len(peak_ndx) > 1:
        return no_audio_data()

    peak_ndx_adjusted = peak_ndx[0] + min_ndx
    bpm = 60.0 / peak_ndx_adjusted * (fs / max_decimation)
    print(bpm)
    return bpm, correl


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process .wav file to determine the Beats Per Minute.")
    parser.add_argument("--filename", required=True, help=".wav file for processing")
    parser.add_argument(
        "--window",
        type=float,
        default=3,
        help="Size of the the window (seconds) that will be scanned to determine the bpm. Typically less than 10 seconds. [3]",
    )

    args = parser.parse_args()

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


    # Keep track of the old BPM
    old_bpm = 0

    # Let's run this indefinitely
    # TODO: add end condition
    while True:
        #record 4 secs of audio and write it to the file at args.filename 
        time_processed = record_voice()

        #then read the recoding in
        samps, fs = read_wav(args.filename)

        # if we could record voice directly and pass it to this, that would be ideal
        # but this doesn't currently work
        # samps, fs = record_voice()
        
        data = []
        correl = []
        bpm = 0
        n = 0
        nsamps = len(samps)
        window_samps = int(args.window * fs)
        samps_ndx = 0  # First sample in window_ndx
        max_window_ndx = math.floor(nsamps / window_samps)
        bpms = numpy.zeros(max_window_ndx)

        # Iterate through all windows
        for window_ndx in range(0, max_window_ndx):

            # Get a new set of samples
            # print(n,":",len(bpms),":",max_window_ndx_int,":",fs,":",nsamps,":",samps_ndx)
            data = samps[samps_ndx : samps_ndx + window_samps]
            if not ((len(data) % window_samps) == 0):
                raise AssertionError(str(len(data)))

            bpm, correl_temp = bpm_detector(data, fs)
            if bpm is None:
                continue
            bpms[window_ndx] = bpm
            correl = correl_temp

            # Iterate at the end of the loop
            samps_ndx = samps_ndx + window_samps

            # Counter for debug...
            n = n + 1

        bpm = numpy.median(bpms)

        # Run this program as a new node in the ROS computation graph called /beatsignal.
        # Only run if we have a new BPM; otherwise, there's no point in sending a new message
        # We might also want to to set a buffer (e.g. if BPM doesn't change by more than 5,
        # there's no point in updating as this could just be margin of error)
        if bpm != old_bpm:
            
            # Check if the node has received a signal to shut down. If not, run the
            # talker method.
            try:
                # talker(pub, bpm, time_processed)
                # I replaced the call to talker() with just this core function
                pub.publish(beats, time_processed, 4, 4)
            except rospy.ROSInterruptException: pass

            old_bpm = bpm

        # Debug here - this is all old code
        # print("Completed!  Estimated Beats Per Minute:", bpm)
        # n = range(0, len(correl))
        # plt.plot(n, abs(correl))
        # plt.show(block=True)


#NOTES: super interesting, it appears that if the BPM < 110, it doubles it, otherwise it's accurate. 